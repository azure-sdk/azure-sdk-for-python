﻿# The MIT License (MIT)
# Copyright (c) 2014 Microsoft Corporation

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# pylint: disable=too-many-lines, protected-access

"""Document client class for the Azure Cosmos database service.
"""
import os
import urllib.parse
import uuid
from typing import Callable, Dict, Any, Iterable, List, Mapping, Optional, Sequence, Tuple, Union, cast
from typing_extensions import TypedDict
from urllib3.util.retry import Retry

from azure.core import PipelineClient
from azure.core.credentials import TokenCredential
from azure.core.paging import ItemPaged
from azure.core.pipeline.policies import (
    HTTPPolicy,
    ContentDecodePolicy,
    HeadersPolicy,
    UserAgentPolicy,
    NetworkTraceLoggingPolicy,
    CustomHookPolicy,
    DistributedTracingPolicy,
    ProxyPolicy
)
from azure.core.utils import CaseInsensitiveDict
from azure.core.pipeline.transport import HttpRequest, \
    HttpResponse  # pylint: disable=no-legacy-azure-core-http-response-import

from . import _base as base
from ._global_partition_endpoint_manager_circuit_breaker import _GlobalPartitionEndpointManagerForCircuitBreaker
from . import _query_iterable as query_iterable
from . import _runtime_constants as runtime_constants
from . import _session
from . import _synchronized_request as synchronized_request
from . import _utils
from . import documents
from . import http_constants, exceptions
from ._auth_policy import CosmosBearerTokenCredentialPolicy
from ._base import _build_properties_cache
from ._change_feed.change_feed_iterable import ChangeFeedIterable
from ._change_feed.change_feed_state import ChangeFeedState
from ._change_feed.feed_range_internal import FeedRangeInternalEpk
from ._constants import _Constants as Constants
from ._cosmos_http_logging_policy import CosmosHttpLoggingPolicy
from ._cosmos_responses import CosmosDict, CosmosList
from ._range_partition_resolver import RangePartitionResolver
from ._request_object import RequestObject
from ._retry_utility import ConnectionRetryPolicy
from ._routing import routing_map_provider, routing_range
from .documents import ConnectionPolicy, DatabaseAccount
from .partition_key import (
    _Undefined,
    _Empty,
    _PartitionKeyKind,
    _PartitionKeyType,
    _SequentialPartitionKeyType,
    _return_undefined_or_empty_partition_key,
)

class CredentialDict(TypedDict, total=False):
    masterKey: str
    resourceTokens: Mapping[str, Any]
    permissionFeed: Iterable[Mapping[str, Any]]
    clientSecretCredential: TokenCredential


class CosmosClientConnection:  # pylint: disable=too-many-public-methods,too-many-instance-attributes
    """Represents a document client.

    Provides a client-side logical representation of the Azure Cosmos
    service. This client is used to configure and execute requests against the
    service.

    The service client encapsulates the endpoint and credentials used to access
    the Azure Cosmos service.
    """

    class _QueryCompatibilityMode:
        Default = 0
        Query = 1
        SqlQuery = 2

    # default number precisions
    _DefaultNumberHashPrecision = 3
    _DefaultNumberRangePrecision = -1

    # default string precision
    _DefaultStringHashPrecision = 3
    _DefaultStringRangePrecision = -1

    def __init__( # pylint: disable=too-many-statements
        self,
        url_connection: str,
        auth: CredentialDict,
        connection_policy: Optional[ConnectionPolicy] = None,
        consistency_level: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :param str url_connection:
            The URL for connecting to the DB server.
        :param dict auth:
            Contains 'masterKey' or 'resourceTokens', where
            auth['masterKey'] is the default authorization key to use to
            create the client, and auth['resourceTokens'] is the alternative
            authorization key.
        :param documents.ConnectionPolicy connection_policy:
            The connection policy for the client.
        :param documents.ConsistencyLevel consistency_level:
            The default consistency policy for client operations.

        """
        self.client_id = str(uuid.uuid4())
        self.url_connection = url_connection
        self.master_key: Optional[str] = None
        self.resource_tokens: Optional[Mapping[str, Any]] = None
        self.aad_credentials: Optional[TokenCredential] = None
        if auth is not None:
            self.master_key = auth.get("masterKey")
            self.resource_tokens = auth.get("resourceTokens")
            self.aad_credentials = auth.get("clientSecretCredential")

            if auth.get("permissionFeed"):
                self.resource_tokens = {}
                for permission_feed in auth["permissionFeed"]:
                    resource_parts = permission_feed["resource"].split("/")
                    id_ = resource_parts[-1]
                    self.resource_tokens[id_] = permission_feed["_token"]

        self.connection_policy = connection_policy or ConnectionPolicy()
        self.partition_resolvers: Dict[str, RangePartitionResolver] = {}
        self.__container_properties_cache: Dict[str, Dict[str, Any]] = {}
        self.default_headers: Dict[str, Any] = {
            http_constants.HttpHeaders.CacheControl: "no-cache",
            http_constants.HttpHeaders.Version: http_constants.Versions.CurrentVersion,
            # For single partition query with aggregate functions we would try to accumulate the results on the SDK.
            # We need to set continuation as not expected.
            http_constants.HttpHeaders.IsContinuationExpected: False,
        }

        throughput_bucket = kwargs.pop('throughput_bucket', None)
        if throughput_bucket:
            self.default_headers[http_constants.HttpHeaders.ThroughputBucket] = throughput_bucket

        # Keeps the latest response headers from the server.
        self.last_response_headers: CaseInsensitiveDict = CaseInsensitiveDict()

        self.UseMultipleWriteLocations = False
        self._global_endpoint_manager = _GlobalPartitionEndpointManagerForCircuitBreaker(self)

        retry_policy = None
        if isinstance(self.connection_policy.ConnectionRetryConfiguration, HTTPPolicy):
            retry_policy = self.connection_policy.ConnectionRetryConfiguration
        elif isinstance(self.connection_policy.ConnectionRetryConfiguration, int):
            retry_policy = ConnectionRetryPolicy(total=self.connection_policy.ConnectionRetryConfiguration)
        elif isinstance(self.connection_policy.ConnectionRetryConfiguration, Retry):
            # Convert a urllib3 retry policy to a Pipeline policy
            retry_policy = ConnectionRetryPolicy(
                retry_total=self.connection_policy.ConnectionRetryConfiguration.total,
                retry_connect=self.connection_policy.ConnectionRetryConfiguration.connect,
                retry_read=self.connection_policy.ConnectionRetryConfiguration.read,
                retry_status=self.connection_policy.ConnectionRetryConfiguration.status,
                retry_backoff_max=self.connection_policy.ConnectionRetryConfiguration.DEFAULT_BACKOFF_MAX,
                retry_on_status_codes=list(self.connection_policy.ConnectionRetryConfiguration.status_forcelist),
                retry_backoff_factor=self.connection_policy.ConnectionRetryConfiguration.backoff_factor
            )
        else:
            raise TypeError(
                "Unsupported retry policy. Must be an azure.cosmos.ConnectionRetryPolicy, int, or urllib3.Retry")

        proxies = kwargs.pop('proxies', {})
        if self.connection_policy.ProxyConfiguration and self.connection_policy.ProxyConfiguration.Host:
            host = self.connection_policy.ProxyConfiguration.Host
            url = urllib.parse.urlparse(host)
            proxy = host if url.port else host + ":" + str(self.connection_policy.ProxyConfiguration.Port)
            proxies.update({url.scheme: proxy})

        suffix = kwargs.pop('user_agent_suffix', None)
        self._user_agent: str = _utils.get_user_agent(suffix)

        credentials_policy = None
        if self.aad_credentials:
            scope_override = os.environ.get(Constants.AAD_SCOPE_OVERRIDE, "")
            if scope_override:
                scope = scope_override
            else:
                scope = base.create_scope_from_url(self.url_connection)
            credentials_policy = CosmosBearerTokenCredentialPolicy(self.aad_credentials, scope)

        policies = [
            HeadersPolicy(**kwargs),
            ProxyPolicy(proxies=proxies),
            UserAgentPolicy(base_user_agent=self._user_agent, **kwargs),
            ContentDecodePolicy(),
            retry_policy,
            credentials_policy,
            CustomHookPolicy(**kwargs),
            NetworkTraceLoggingPolicy(**kwargs),
            DistributedTracingPolicy(**kwargs),
            CosmosHttpLoggingPolicy(
                logger=kwargs.pop("logger", None),
                enable_diagnostics_logging=kwargs.pop("enable_diagnostics_logging", False),
                global_endpoint_manager=self._global_endpoint_manager,
                **kwargs
            ),
        ]

        transport = kwargs.pop("transport", None)
        self.pipeline_client: PipelineClient[HttpRequest, HttpResponse] = PipelineClient(
            base_url=url_connection,
            transport=transport,
            policies=policies
        )

        # Query compatibility mode.
        # Allows to specify compatibility mode used by client when making query requests. Should be removed when
        # application/sql is no longer supported.
        self._query_compatibility_mode = CosmosClientConnection._QueryCompatibilityMode.Default

        # Routing map provider
        self._routing_map_provider = routing_map_provider.SmartRoutingMapProvider(self)

        database_account, _ = self._global_endpoint_manager._GetDatabaseAccount(**kwargs)
        self._global_endpoint_manager.force_refresh_on_startup(database_account)

        # Use database_account if no consistency passed in to verify consistency level to be used
        self.session: Optional[_session.Session] = None
        self._set_client_consistency_level(database_account, consistency_level)

    @property
    def _container_properties_cache(self) -> Dict[str, Dict[str, Any]]:
        """Gets the container properties cache from the client.
        :returns: the container properties cache for the client.
        :rtype: Dict[str, Dict[str, Any]]"""
        return self.__container_properties_cache

    def _set_container_properties_cache(self, container_link: str, properties: Optional[Dict[str, Any]]) -> None:
        """Sets the container properties cache for the specified container.

        This will only update the properties cache for a specified container.
        :param container_link: The container link will be used as the key to cache the container properties.
        :type container_link: str
        :param properties: These are the container properties to cache.
        :type properties:  Optional[Dict[str, Any]]"""
        if properties:
            self.__container_properties_cache[container_link] = properties
            self.__container_properties_cache[properties["_rid"]] = properties
        else:
            self.__container_properties_cache[container_link] = {}

    def _set_client_consistency_level(
        self,
        database_account: DatabaseAccount,
        consistency_level: Optional[str],
    ) -> None:
        """Checks if consistency level param was passed in by user and sets it to that value or to the account default.

        :param database_account: The database account to be used to check consistency levels
        :type database_account: ~azure.cosmos.documents.DatabaseAccount
        :param consistency_level: The consistency level passed in by the user
        :type consistency_level: Optional[str]
        :rtype: None
        """
        if consistency_level is None and database_account.ConsistencyPolicy:
            # Set to default level present in account
            user_consistency_policy = database_account.ConsistencyPolicy
            consistency_level = user_consistency_policy.get(Constants.DefaultConsistencyLevel)
        else:
            # Set consistency level header to be used for the client
            self.default_headers[http_constants.HttpHeaders.ConsistencyLevel] = consistency_level

        if consistency_level == documents.ConsistencyLevel.Session:
            # create a session - this is maintained only if the default consistency level
            # on the client is set to session, or if the user explicitly sets it as a property
            # via setter
            self.default_headers[http_constants.HttpHeaders.ConsistencyLevel] = consistency_level
            self.session = _session.Session(self.url_connection)
        else:
            self.session = None

    @property
    def Session(self) -> Optional[_session.Session]:
        """Gets the session object from the client.
         :returns: the session for the client
         :rtype: _session.Session
         """
        return self.session

    @Session.setter
    def Session(self, session: Optional[_session.Session]) -> None:
        """Sets a session object on the document client.
        This will override the existing session
        :param _session.Session session: the session to set
        """
        self.session = session

    @property
    def WriteEndpoint(self) -> str:
        """Gets the current write endpoint for a geo-replicated database account.
        :returns: the write endpoint for the database account
        :rtype: str
        """
        return self._global_endpoint_manager.get_write_endpoint()

    @property
    def ReadEndpoint(self) -> str:
        """Gets the current read endpoint for a geo-replicated database account.
        :returns: the read endpoint for the database account
        :rtype: str
        """
        return self._global_endpoint_manager.get_read_endpoint()

    def RegisterPartitionResolver(self, database_link: str, partition_resolver: RangePartitionResolver) -> None:
        """Registers the partition resolver associated with the database link

        :param str database_link:
            Database Self Link or ID based link.
        :param object partition_resolver:
            An instance of PartitionResolver.
        """
        if not database_link:
            raise ValueError("database_link is None or empty.")

        if partition_resolver is None:
            raise ValueError("partition_resolver is None.")

        self.partition_resolvers = {base.TrimBeginningAndEndingSlashes(database_link): partition_resolver}

    def GetPartitionResolver(self, database_link: str) -> Optional[RangePartitionResolver]:
        """Gets the partition resolver associated with the database link

        :param str database_link:
            Database self link or ID based link.

        :return:
            An instance of PartitionResolver.
        :rtype: object

        """
        if not database_link:
            raise ValueError("database_link is None or empty.")
        return self.partition_resolvers.get(base.TrimBeginningAndEndingSlashes(database_link))

    def CreateDatabase(
        self,
        database: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Creates a database.

        :param dict database:
            The Azure Cosmos database to create.
        :param dict options:
            The request options for the request.

        :return:
            The Database that was created.
        :rtype: dict
        """
        if options is None:
            options = {}
        base._validate_resource(database)
        path = "/dbs"
        return self.Create(database, path, http_constants.ResourceType.Database, None, None, options, **kwargs)

    def ReadDatabase(
        self,
        database_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Reads a database.

        :param str database_link:
            The link to the database.
        :param dict options:
            The request options for the request.

        :return:
            The Database that was read.
        :rtype: dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(database_link)
        database_id = base.GetResourceIdOrFullNameFromLink(database_link)
        return self.Read(path, http_constants.ResourceType.Database, database_id, None, options, **kwargs)

    def ReadDatabases(
        self,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Reads all databases.

        :param dict options:
            The request options for the request.

        :return:
            Query Iterable of Databases.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        return self.QueryDatabases(None, options, **kwargs)

    def QueryDatabases(
        self,
        query: Optional[Union[str, Dict[str, Any]]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Queries databases.

        :param (str or dict) query:
        :param dict options:
            The request options for the request.

        :return: Query Iterable of Databases.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        def fetch_fn(options: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
            return self.__QueryFeed(
                    "/dbs", http_constants.ResourceType.Database, "", lambda r: r["Databases"],
                    lambda _, b: b, query, options, **kwargs)

        return ItemPaged(
            self, query, options, fetch_function=fetch_fn, page_iterator_class=query_iterable.QueryIterable
        )

    def ReadContainers(
        self,
        database_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Reads all collections in a database.

        :param str database_link:
            The link to the database.
        :param dict options:
            The request options for the request.

        :return: Query Iterable of Collections.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        return self.QueryContainers(database_link, None, options, **kwargs)

    def QueryContainers(
        self,
        database_link: str,
        query: Optional[Union[str, Dict[str, Any]]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Queries collections in a database.

        :param str database_link:
            The link to the database.
        :param (str or dict) query:
        :param dict options:
            The request options for the request.

        :return: Query Iterable of Collections.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(database_link, http_constants.ResourceType.Collection)
        database_id = base.GetResourceIdOrFullNameFromLink(database_link)

        def fetch_fn(options: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
            return self.__QueryFeed(
                    path, http_constants.ResourceType.Collection, database_id, lambda r: r["DocumentCollections"],
                    lambda _, body: body, query, options, **kwargs)

        return ItemPaged(
            self, query, options, fetch_function=fetch_fn, page_iterator_class=query_iterable.QueryIterable
        )

    def CreateContainer(
        self,
        database_link: str,
        collection: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Creates a collection in a database.

        :param str database_link:
            The link to the database.
        :param dict collection:
            The Azure Cosmos collection to create.
        :param dict options:
            The request options for the request.

        :return: The Collection that was created.
        :rtype: dict

        """
        if options is None:
            options = {}

        base._validate_resource(collection)
        path = base.GetPathFromLink(database_link, http_constants.ResourceType.Collection)
        database_id = base.GetResourceIdOrFullNameFromLink(database_link)
        return self.Create(collection, path, http_constants.ResourceType.Collection, database_id, None,
                           options, **kwargs)

    def ReplaceContainer(
        self,
        collection_link: str,
        collection: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Replaces a collection and return it.

        :param str collection_link:
            The link to the collection entity.
        :param dict collection:
            The collection to be used.
        :param dict options:
            The request options for the request.

        :return:
            The new Collection.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        base._validate_resource(collection)
        path = base.GetPathFromLink(collection_link)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)
        return self.Replace(collection, path, http_constants.ResourceType.Collection, collection_id, None,
                            options, **kwargs)

    def ReadContainer(
        self,
        collection_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Reads a collection.

        :param str collection_link:
            The link to the document collection.
        :param dict options:
            The request options for the request.

        :return:
            The read Collection.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(collection_link)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)
        return self.Read(path, http_constants.ResourceType.Collection, collection_id, None, options, **kwargs)

    def CreateUser(
        self,
        database_link: str,
        user: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Creates a user.

        :param str database_link:
            The link to the database.
        :param dict user:
            The Azure Cosmos user to create.
        :param dict options:
            The request options for the request.

        :return:
            The created User.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        database_id, path = self._GetDatabaseIdWithPathForUser(database_link, user)
        return self.Create(user, path, http_constants.ResourceType.User, database_id, None, options, **kwargs)

    def UpsertUser(
        self,
        database_link: str,
        user: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Upserts a user.

        :param str database_link:
            The link to the database.
        :param dict user:
            The Azure Cosmos user to upsert.
        :param dict options:
            The request options for the request.

        :return:
            The upserted User.
        :rtype: dict
        """
        if options is None:
            options = {}

        database_id, path = self._GetDatabaseIdWithPathForUser(database_link, user)
        return self.Upsert(user, path, http_constants.ResourceType.User, database_id, None, options, **kwargs)

    def _GetDatabaseIdWithPathForUser(self, database_link: str, user: Mapping[str, Any]) -> Tuple[Optional[str], str]:
        base._validate_resource(user)
        path = base.GetPathFromLink(database_link, http_constants.ResourceType.User)
        database_id = base.GetResourceIdOrFullNameFromLink(database_link)
        return database_id, path

    def ReadUser(
        self,
        user_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Reads a user.

        :param str user_link:
            The link to the user entity.
        :param dict options:
            The request options for the request.

        :return:
            The read User.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(user_link)
        user_id = base.GetResourceIdOrFullNameFromLink(user_link)
        return self.Read(path, http_constants.ResourceType.User, user_id, None, options, **kwargs)

    def ReadUsers(
        self,
        database_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Reads all users in a database.

        :param str database_link:
            The link to the database.
        :param dict[str, Any] options:
            The request options for the request.
        :return:
            Query iterable of Users.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        return self.QueryUsers(database_link, None, options, **kwargs)

    def QueryUsers(
        self,
        database_link: str,
        query: Optional[Union[str, Dict[str, Any]]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Queries users in a database.

        :param str database_link:
            The link to the database.
        :param (str or dict) query:
        :param dict options:
            The request options for the request.

        :return:
            Query Iterable of Users.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(database_link, http_constants.ResourceType.User)
        database_id = base.GetResourceIdOrFullNameFromLink(database_link)

        def fetch_fn(options: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
            return self.__QueryFeed(
                    path, http_constants.ResourceType.User, database_id, lambda r: r["Users"],
                    lambda _, b: b, query, options, **kwargs)

        return ItemPaged(
            self, query, options, fetch_function=fetch_fn, page_iterator_class=query_iterable.QueryIterable
        )

    def DeleteDatabase(
        self,
        database_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a database.

        :param str database_link:
            The link to the database.
        :param dict options:
            The request options for the request.

        :return:
            The deleted Database.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(database_link)
        database_id = base.GetResourceIdOrFullNameFromLink(database_link)
        self.DeleteResource(path, http_constants.ResourceType.Database, database_id, None, options, **kwargs)

    def CreatePermission(
        self,
        user_link: str,
        permission: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Creates a permission for a user.

        :param str user_link:
            The link to the user entity.
        :param dict permission:
            The Azure Cosmos user permission to create.
        :param dict options:
            The request options for the request.

        :return:
            The created Permission.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path, user_id = self._GetUserIdWithPathForPermission(permission, user_link)
        return self.Create(permission, path, http_constants.ResourceType.Permission, user_id, None, options, **kwargs)

    def UpsertPermission(
        self,
        user_link: str,
        permission: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Upserts a permission for a user.

        :param str user_link:
            The link to the user entity.
        :param dict permission:
            The Azure Cosmos user permission to upsert.
        :param dict options:
            The request options for the request.

        :return:
            The upserted permission.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path, user_id = self._GetUserIdWithPathForPermission(permission, user_link)
        return self.Upsert(permission, path, http_constants.ResourceType.Permission, user_id, None, options, **kwargs)

    def _GetUserIdWithPathForPermission(
        self,
        permission: Mapping[str, Any],
        user_link: str
    ) -> Tuple[str, Optional[str]]:
        base._validate_resource(permission)
        path = base.GetPathFromLink(user_link, http_constants.ResourceType.Permission)
        user_id = base.GetResourceIdOrFullNameFromLink(user_link)
        return path, user_id

    def ReadPermission(
        self,
        permission_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Reads a permission.

        :param str permission_link:
            The link to the permission.
        :param dict options:
            The request options for the request.

        :return:
            The read permission.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(permission_link)
        permission_id = base.GetResourceIdOrFullNameFromLink(permission_link)
        return self.Read(path, http_constants.ResourceType.Permission, permission_id, None, options, **kwargs)

    def ReadPermissions(
        self,
        user_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Reads all permissions for a user.

        :param str user_link:
            The link to the user entity.
        :param dict options:
            The request options for the request.

        :return:
            Query Iterable of Permissions.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        return self.QueryPermissions(user_link, None, options, **kwargs)

    def QueryPermissions(
        self,
        user_link: str,
        query: Optional[Union[str, Dict[str, Any]]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Queries permissions for a user.

        :param str user_link:
            The link to the user entity.
        :param (str or dict) query:
        :param dict options:
            The request options for the request.

        :return:
            Query Iterable of Permissions.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(user_link, http_constants.ResourceType.Permission)
        user_id = base.GetResourceIdOrFullNameFromLink(user_link)

        def fetch_fn(options: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
            return self.__QueryFeed(
                    path, http_constants.ResourceType.Permission, user_id, lambda r: r["Permissions"],
                    lambda _, b: b, query, options, **kwargs)

        return ItemPaged(
            self, query, options, fetch_function=fetch_fn, page_iterator_class=query_iterable.QueryIterable
        )

    def ReplaceUser(
        self,
        user_link: str,
        user: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Replaces a user and return it.

        :param str user_link:
            The link to the user entity.
        :param dict user:
        :param dict options:
            The request options for the request.

        :return:
            The new User.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        base._validate_resource(user)
        path = base.GetPathFromLink(user_link)
        user_id = base.GetResourceIdOrFullNameFromLink(user_link)
        return self.Replace(user, path, http_constants.ResourceType.User, user_id, None, options, **kwargs)

    def DeleteUser(
        self,
        user_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a user.

        :param str user_link:
            The link to the user entity.
        :param dict options:
            The request options for the request.

        :return:
            The deleted user.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(user_link)
        user_id = base.GetResourceIdOrFullNameFromLink(user_link)
        self.DeleteResource(path, http_constants.ResourceType.User, user_id, None, options, **kwargs)

    def ReplacePermission(
        self,
        permission_link: str,
        permission: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Replaces a permission and return it.

        :param str permission_link:
            The link to the permission.
        :param dict permission:
        :param dict options:
            The request options for the request.

        :return:
            The new Permission.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        base._validate_resource(permission)
        path = base.GetPathFromLink(permission_link)
        permission_id = base.GetResourceIdOrFullNameFromLink(permission_link)
        return self.Replace(permission, path, http_constants.ResourceType.Permission, permission_id, None,
                            options, **kwargs)

    def DeletePermission(
        self,
        permission_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a permission.

        :param str permission_link:
            The link to the permission.
        :param dict options:
            The request options for the request.

        :return:
            The deleted Permission.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(permission_link)
        permission_id = base.GetResourceIdOrFullNameFromLink(permission_link)
        self.DeleteResource(path, http_constants.ResourceType.Permission, permission_id, None, options,
                            **kwargs)

    def ReadItems(
        self,
        collection_link: str,
        feed_options: Optional[Mapping[str, Any]] = None,
        response_hook: Optional[Callable[[Mapping[str, Any], Dict[str, Any]], None]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Reads all documents in a collection.
        :param str collection_link: The link to the document collection.
        :param dict feed_options: The additional options for the operation.
        :param response_hook: A callable invoked with the response metadata.
        :type response_hook: Callable[[Mapping[str, Any], Dict[str, Any]]
        :return: Query Iterable of Documents.
        :rtype: query_iterable.QueryIterable
        """
        if feed_options is None:
            feed_options = {}

        return self.QueryItems(collection_link, None, feed_options, response_hook=response_hook, **kwargs)

    def QueryItems(
        self,
        database_or_container_link: str,
        query: Optional[Union[str, Dict[str, Any]]],
        options: Optional[Mapping[str, Any]] = None,
        partition_key: Optional[_PartitionKeyType] = None,
        response_hook: Optional[Callable[[Mapping[str, Any], Dict[str, Any]], None]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Queries documents in a collection.

        :param str database_or_container_link:
            The link to the database when using partitioning, otherwise link to the document collection.
        :param (str or dict) query: the query to be used
        :param dict options: The request options for the request.
        :param partition_key: Partition key for the query(default value None)
        :type: partition_key: Union[str, int, float, bool, List[Union[str, int, float, bool]]]
        :param response_hook: A callable invoked with the response metadata.
        :type response_hook: Callable[[Mapping[str, Any], Dict[str, Any]], None]

        :return:
            Query Iterable of Documents.
        :rtype:
            query_iterable.QueryIterable

        """
        database_or_container_link = base.TrimBeginningAndEndingSlashes(database_or_container_link)

        if options is None:
            options = {}

        if base.IsDatabaseLink(database_or_container_link):
            return ItemPaged(
                self,
                query,
                options,
                database_link=database_or_container_link,
                partition_key=partition_key,
                page_iterator_class=query_iterable.QueryIterable
            )

        path = base.GetPathFromLink(database_or_container_link, http_constants.ResourceType.Document)
        collection_id = base.GetResourceIdOrFullNameFromLink(database_or_container_link)

        def fetch_fn(options: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
            return self.__QueryFeed(
                    path,
                    http_constants.ResourceType.Document,
                    collection_id,
                    lambda r: r["Documents"],
                    lambda _, b: b,
                    query,
                    options,
                    response_hook=response_hook,
                    **kwargs)

        return ItemPaged(
            self,
            query,
            options,
            fetch_function=fetch_fn,
            collection_link=database_or_container_link,
            page_iterator_class=query_iterable.QueryIterable,
            response_hook=response_hook,
            raw_response_hook=kwargs.get('raw_response_hook'),
            resource_type=http_constants.ResourceType.Document
        )

    def QueryItemsChangeFeed(
        self,
        collection_link: str,
        options: Optional[Mapping[str, Any]] = None,
        response_hook: Optional[Callable[[Mapping[str, Any], Mapping[str, Any]], None]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Queries documents change feed in a collection.

        :param str collection_link: The link to the document collection.
        :param dict options: The request options for the request.
        :param response_hook: A callable invoked with the response metadata.
        :type response_hook: Callable[[Dict[str, str], Dict[str, Any]]

        :return:
            Query Iterable of Documents.
        :rtype:
            query_iterable.QueryIterable

        """

        partition_key_range_id = None
        if options is not None and "partitionKeyRangeId" in options:
            partition_key_range_id = options["partitionKeyRangeId"]

        return self._QueryChangeFeed(collection_link, options, partition_key_range_id,response_hook=response_hook,
                                     **kwargs)

    def _QueryChangeFeed(
        self,
        collection_link: str,
        options: Optional[Mapping[str, Any]] = None,
        partition_key_range_id: Optional[str] = None,
        response_hook: Optional[Callable[[Mapping[str, Any], Mapping[str, Any]], None]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Queries change feed of a resource in a collection.

        :param str collection_link: The link to the document collection.
        :param dict options: The request options for the request.
        :param str partition_key_range_id: Specifies partition key range id.
        :param response_hook: A callable invoked with the response metadata
        :type response_hook: Callable[[Dict[str, str], Dict[str, Any]]

        :return:
            Query Iterable of Documents.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}
        else:
            options = dict(options)

        path = base.GetPathFromLink(collection_link, http_constants.ResourceType.Document)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)

        def fetch_fn(options: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
            if collection_link in self.__container_properties_cache:
                # TODO: This will make deep copy. Check if this has any performance impact
                new_options = dict(options)
                new_options["containerRID"] = self.__container_properties_cache[collection_link]["_rid"]
                options = new_options
            return self.__QueryFeed(
                path,
                http_constants.ResourceType.Document,
                collection_id,
                lambda r: r["Documents"],
                lambda _, b: b,
                None,
                options,
                partition_key_range_id,
                response_hook=response_hook,
                **kwargs)

        return ItemPaged(
            self,
            options,
            fetch_function=fetch_fn,
            collection_link=collection_link,
            page_iterator_class=ChangeFeedIterable
        )

    def _ReadPartitionKeyRanges(
        self,
        collection_link: str,
        feed_options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Reads Partition Key Ranges.

        :param str collection_link: The link to the document collection.
        :param dict feed_options: The request options.
        :return: Query Iterable of PartitionKeyRanges.
        :rtype: query_iterable.QueryIterable

        """
        if feed_options is None:
            feed_options = {}

        return self._QueryPartitionKeyRanges(collection_link, None, feed_options, **kwargs)

    def _QueryPartitionKeyRanges(
        self,
        collection_link: str,
        query: Optional[Union[str, Dict[str, Any]]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Queries Partition Key Ranges in a collection.

        :param str collection_link:
            The link to the document collection.
        :param (str or dict) query:
        :param dict options:
            The request options for the request.

        :return:
            Query Iterable of PartitionKeyRanges.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(collection_link, http_constants.ResourceType.PartitionKeyRange)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)

        def fetch_fn(options: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
            return self.__QueryFeed(
                    path, http_constants.ResourceType.PartitionKeyRange, collection_id,
                    lambda r: r["PartitionKeyRanges"],
                    lambda _, b: b, query, options, **kwargs)

        return ItemPaged(
            self, query, options, fetch_function=fetch_fn, page_iterator_class=query_iterable.QueryIterable,
            resource_type=http_constants.ResourceType.PartitionKeyRange
        )

    def CreateItem(
        self,
        database_or_container_link: str,
        document: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> CosmosDict:
        """Creates a document in a collection.

        :param str database_or_container_link:
            The link to the database when using partitioning, otherwise link to the document collection.
        :param dict document: The Azure Cosmos document to create.
        :param dict options: The request options for the request.
        :return: The created Document.
        :rtype: CosmosDict
        """
        # Python's default arguments are evaluated once when the function is defined,
        # not each time the function is called (like it is in say, Ruby). This means
        # that if you use a mutable default argument and mutate it, you will and have
        # mutated that object for all future calls to the function as well. So, using
        # a non-mutable default in this case(None) and assigning an empty dict(mutable)
        # inside the method For more details on this gotcha, please refer
        # http://docs.python-guide.org/en/latest/writing/gotchas/
        if options is None:
            options = {}

        # We check the link to be document collection link since it can be database
        # link in case of client side partitioning
        collection_id, document, path = self._GetContainerIdWithPathForItem(
            database_or_container_link, document, options
        )

        if base.IsItemContainerLink(database_or_container_link):
            options = self._AddPartitionKey(database_or_container_link, document, options)
        return self.Create(document,
                           path,
                           http_constants.ResourceType.Document,
                           collection_id,
                           None,
                           options,
                           **kwargs)

    def UpsertItem(
        self,
        database_or_container_link: str,
        document: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> CosmosDict:
        """Upserts a document in a collection.

        :param str database_or_container_link:
            The link to the database when using partitioning, otherwise link to the document collection.
        :param dict document: The Azure Cosmos document to upsert.
        :param dict options: The request options for the request.
        :return: The upserted Document.
        :rtype: CosmosDict
        """
        # Python's default arguments are evaluated once when the function is defined,
        # not each time the function is called (like it is in say, Ruby). This means
        # that if you use a mutable default argument and mutate it, you will and have
        # mutated that object for all future calls to the function as well. So, using
        # a non-mutable deafult in this case(None) and assigning an empty dict(mutable)
        # inside the method For more details on this gotcha, please refer
        # http://docs.python-guide.org/en/latest/writing/gotchas/
        if options is None:
            options = {}

        # We check the link to be document collection link since it can be database
        # link in case of client side partitioning
        if base.IsItemContainerLink(database_or_container_link):
            options = self._AddPartitionKey(database_or_container_link, document, options)

        collection_id, document, path = self._GetContainerIdWithPathForItem(
            database_or_container_link, document, options
        )
        return self.Upsert(document,
                           path,
                           http_constants.ResourceType.Document,
                           collection_id,
                           None,
                           options,
                           **kwargs)

    PartitionResolverErrorMessage = (
            "Couldn't find any partition resolvers for the database link provided. "
            + "Ensure that the link you used when registering the partition resolvers "
            + "matches the link provided or you need to register both types of database "
            + "link(self link as well as ID based link)."
    )

    # Gets the collection id and path for the document
    def _GetContainerIdWithPathForItem(
        self,
        database_or_container_link: str,
        document: Mapping[str, Any],
        options: Mapping[str, Any]
    ) -> Tuple[Optional[str], Dict[str, Any], str]:

        if not database_or_container_link:
            raise ValueError("database_or_container_link is None or empty.")

        if document is None:
            raise ValueError("document is None.")

        base._validate_resource(document)
        document = dict(document)
        if not document.get("id") and not options.get("disableAutomaticIdGeneration"):
            document["id"] = base.GenerateGuidId()

        collection_link = database_or_container_link

        if base.IsDatabaseLink(database_or_container_link):
            partition_resolver = self.GetPartitionResolver(database_or_container_link)

            if partition_resolver is not None:
                collection_link = partition_resolver.ResolveForCreate(document)
            else:
                raise ValueError(CosmosClientConnection.PartitionResolverErrorMessage)

        path = base.GetPathFromLink(collection_link, http_constants.ResourceType.Document)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)
        return collection_id, document, path

    def ReadItem(
        self,
        document_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs
    ) -> CosmosDict:
        """Reads a document.

        :param str document_link:
            The link to the document.
        :param dict options:
            The request options for the request.

        :return:
            The read Document.
        :rtype:
            CosmosDict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(document_link)
        document_id = base.GetResourceIdOrFullNameFromLink(document_link)
        return self.Read(path, http_constants.ResourceType.Document, document_id, None, options, **kwargs)

    def ReadTriggers(
        self,
        collection_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Reads all triggers in a collection.

        :param str collection_link:
            The link to the document collection.
        :param dict options:
            The request options for the request.

        :return:
            Query Iterable of Triggers.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        return self.QueryTriggers(collection_link, None, options, **kwargs)

    def QueryTriggers(
        self,
        collection_link: str,
        query: Optional[Union[str, Dict[str, Any]]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Queries triggers in a collection.

        :param str collection_link:
            The link to the document collection.
        :param (str or dict) query:
        :param dict options:
            The request options for the request.

        :return:
            Query Iterable of Triggers.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(collection_link, http_constants.ResourceType.Trigger)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)

        def fetch_fn(options: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
            return self.__QueryFeed(
                path, http_constants.ResourceType.Trigger, collection_id, lambda r: r["Triggers"],
                lambda _, b: b, query, options, **kwargs)

        return ItemPaged(
            self, query, options, fetch_function=fetch_fn, page_iterator_class=query_iterable.QueryIterable
        )

    def CreateTrigger(
        self,
        collection_link: str,
        trigger: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Creates a trigger in a collection.

        :param str collection_link:
            The link to the document collection.
        :param dict trigger:
        :param dict options:
            The request options for the request.

        :return:
            The created Trigger.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        collection_id, path, trigger = self._GetContainerIdWithPathForTrigger(collection_link, trigger)
        return self.Create(trigger, path, http_constants.ResourceType.Trigger, collection_id, None, options, **kwargs)

    def _GetContainerIdWithPathForTrigger(
        self,
        collection_link: str,
        trigger: Mapping[str, Any]
    ) -> Tuple[Optional[str], str, Dict[str, Any]]:
        base._validate_resource(trigger)
        trigger = dict(trigger)
        if trigger.get("serverScript"):
            trigger["body"] = str(trigger.pop("serverScript", ""))
        elif trigger.get("body"):
            trigger["body"] = str(trigger["body"])

        path = base.GetPathFromLink(collection_link, http_constants.ResourceType.Trigger)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)
        return collection_id, path, trigger

    def ReadTrigger(
        self,
        trigger_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Reads a trigger.

        :param str trigger_link:
            The link to the trigger.
        :param dict options:
            The request options for the request.

        :return:
            The read Trigger.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(trigger_link)
        trigger_id = base.GetResourceIdOrFullNameFromLink(trigger_link)
        return self.Read(path, http_constants.ResourceType.Trigger, trigger_id, None, options, **kwargs)

    def UpsertTrigger(
        self,
        collection_link: str,
        trigger: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Upserts a trigger in a collection.
        :param str collection_link:
            The link to the document collection.
        :param dict trigger:
        :param dict options:
            The request options for the request.
        :return:
            The upserted Trigger.
        :rtype:
            dict
        """
        if options is None:
            options = {}

        collection_id, path, trigger = self._GetContainerIdWithPathForTrigger(collection_link, trigger)
        return self.Upsert(trigger, path, http_constants.ResourceType.Trigger, collection_id, None,
                           options, **kwargs)

    def ReadUserDefinedFunctions(
        self,
        collection_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Reads all user-defined functions in a collection.

        :param str collection_link:
            The link to the document collection.
        :param dict options:
            The request options for the request.

        :return:
            Query Iterable of UDFs.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        return self.QueryUserDefinedFunctions(collection_link, None, options, **kwargs)

    def QueryUserDefinedFunctions(
        self,
        collection_link: str,
        query: Optional[Union[str, Dict[str, Any]]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Queries user-defined functions in a collection.

        :param str collection_link:
            The link to the collection.
        :param (str or dict) query:
        :param dict options:
            The request options for the request.

        :return:
            Query Iterable of UDFs.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(collection_link, http_constants.ResourceType.UserDefinedFunction)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)

        def fetch_fn(options: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
            return self.__QueryFeed(
                    path, http_constants.ResourceType.UserDefinedFunction, collection_id,
                    lambda r: r["UserDefinedFunctions"],
                    lambda _, b: b, query, options, **kwargs)

        return ItemPaged(
            self, query, options, fetch_function=fetch_fn, page_iterator_class=query_iterable.QueryIterable
        )

    def CreateUserDefinedFunction(
        self,
        collection_link: str,
        udf: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Creates a user-defined function in a collection.

        :param str collection_link:
            The link to the collection.
        :param str udf:
        :param dict options:
            The request options for the request.

        :return:
            The created UDF.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        collection_id, path, udf = self._GetContainerIdWithPathForUDF(collection_link, udf)
        return self.Create(udf, path, http_constants.ResourceType.UserDefinedFunction, collection_id, None,
                           options, **kwargs)

    def UpsertUserDefinedFunction(
        self,
        collection_link: str,
        udf: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Upserts a user-defined function in a collection.

        :param str collection_link:
            The link to the collection.
        :param str udf:
        :param dict options:
            The request options for the request.

        :return:
            The upserted UDF.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        collection_id, path, udf = self._GetContainerIdWithPathForUDF(collection_link, udf)
        return self.Upsert(udf, path, http_constants.ResourceType.UserDefinedFunction, collection_id, None,
                           options, **kwargs)

    def _GetContainerIdWithPathForUDF(
        self,
        collection_link: str,
        udf: Mapping[str, Any]
    ) -> Tuple[Optional[str], str, Dict[str, Any]]:
        base._validate_resource(udf)
        udf = dict(udf)
        if udf.get("serverScript"):
            udf["body"] = str(udf.pop("serverScript", ""))
        elif udf.get("body"):
            udf["body"] = str(udf["body"])

        path = base.GetPathFromLink(collection_link, http_constants.ResourceType.UserDefinedFunction)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)
        return collection_id, path, udf

    def ReadUserDefinedFunction(
        self,
        udf_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Reads a user-defined function.

        :param str udf_link:
            The link to the user-defined function.
        :param dict options:
            The request options for the request.

        :return:
            The read UDF.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(udf_link)
        udf_id = base.GetResourceIdOrFullNameFromLink(udf_link)
        return self.Read(path, http_constants.ResourceType.UserDefinedFunction, udf_id, None, options, **kwargs)

    def ReadStoredProcedures(
        self,
        collection_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Reads all store procedures in a collection.

        :param str collection_link:
            The link to the document collection.
        :param dict options:
            The request options for the request.

        :return:
            Query Iterable of Stored Procedures.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        return self.QueryStoredProcedures(collection_link, None, options, **kwargs)

    def QueryStoredProcedures(
        self,
        collection_link: str,
        query: Optional[Union[str, Dict[str, Any]]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Queries stored procedures in a collection.

        :param str collection_link:
            The link to the document collection.
        :param (str or dict) query:
        :param dict options:
            The request options for the request.

        :return:
            Query Iterable of Stored Procedures.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(collection_link, http_constants.ResourceType.StoredProcedure)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)

        def fetch_fn(options: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
            return self.__QueryFeed(
                path, http_constants.ResourceType.StoredProcedure, collection_id, lambda r: r["StoredProcedures"],
                lambda _, b: b, query, options, **kwargs)

        return ItemPaged(
            self, query, options, fetch_function=fetch_fn, page_iterator_class=query_iterable.QueryIterable
        )

    def CreateStoredProcedure(
        self,
        collection_link: str,
        sproc: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Creates a stored procedure in a collection.

        :param str collection_link:
            The link to the document collection.
        :param str sproc:
        :param dict options:
            The request options for the request.

        :return:
            The created Stored Procedure.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        collection_id, path, sproc = self._GetContainerIdWithPathForSproc(collection_link, sproc)
        return self.Create(sproc, path, http_constants.ResourceType.StoredProcedure, collection_id, None,
                           options, **kwargs)

    def UpsertStoredProcedure(
        self,
        collection_link: str,
        sproc: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Upserts a stored procedure in a collection.

        :param str collection_link:
            The link to the document collection.
        :param str sproc:
        :param dict options:
            The request options for the request.

        :return:
            The upserted Stored Procedure.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        collection_id, path, sproc = self._GetContainerIdWithPathForSproc(collection_link, sproc)
        return self.Upsert(sproc, path, http_constants.ResourceType.StoredProcedure, collection_id, None,
                           options, **kwargs)

    def _GetContainerIdWithPathForSproc(
        self,
        collection_link: str,
        sproc: Mapping[str, Any]
    ) -> Tuple[Optional[str], str, Dict[str, Any]]:
        base._validate_resource(sproc)
        sproc = dict(sproc)
        if sproc.get("serverScript"):
            sproc["body"] = str(sproc.pop("serverScript", ""))
        elif sproc.get("body"):
            sproc["body"] = str(sproc["body"])
        path = base.GetPathFromLink(collection_link, http_constants.ResourceType.StoredProcedure)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)
        return collection_id, path, sproc

    def ReadStoredProcedure(
        self,
        sproc_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Reads a stored procedure.

        :param str sproc_link:
            The link to the stored procedure.
        :param dict options:
            The request options for the request.

        :return:
            The read Stored Procedure.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(sproc_link)
        sproc_id = base.GetResourceIdOrFullNameFromLink(sproc_link)
        return self.Read(path, http_constants.ResourceType.StoredProcedure, sproc_id, None, options, **kwargs)

    def ReadConflicts(
        self,
        collection_link: str,
        feed_options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Reads conflicts.

        :param str collection_link:
            The link to the document collection.
        :param dict feed_options:

        :return:
            Query Iterable of Conflicts.
        :rtype:
            query_iterable.QueryIterable

        """
        if feed_options is None:
            feed_options = {}

        return self.QueryConflicts(collection_link, None, feed_options, **kwargs)

    def QueryConflicts(
        self,
        collection_link: str,
        query: Optional[Union[str, Dict[str, Any]]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Queries conflicts in a collection.

        :param str collection_link:
            The link to the document collection.
        :param (str or dict) query:
        :param dict options:
            The request options for the request.

        :return:
            Query Iterable of Conflicts.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(collection_link, http_constants.ResourceType.Conflict)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)

        def fetch_fn(options: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
            return self.__QueryFeed(
                path, http_constants.ResourceType.Conflict, collection_id, lambda r: r["Conflicts"],
                lambda _, b: b, query, options, **kwargs)

        return ItemPaged(
            self, query, options, fetch_function=fetch_fn, page_iterator_class=query_iterable.QueryIterable
        )

    def ReadConflict(
        self,
        conflict_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Reads a conflict.

        :param str conflict_link:
            The link to the conflict.
        :param dict options:

        :return:
            The read Conflict.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(conflict_link)
        conflict_id = base.GetResourceIdOrFullNameFromLink(conflict_link)
        return self.Read(path, http_constants.ResourceType.Conflict, conflict_id, None, options, **kwargs)

    def DeleteContainer(
        self,
        collection_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a collection.

        :param str collection_link:
            The link to the document collection.
        :param dict options:
            The request options for the request.

        :return:
            The deleted Collection.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(collection_link)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)
        self.DeleteResource(path, http_constants.ResourceType.Collection, collection_id, None, options, **kwargs)

    def ReplaceItem(
        self,
        document_link: str,
        new_document: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> CosmosDict:
        """Replaces a document and returns it.

        :param str document_link:
            The link to the document.
        :param dict new_document:
        :param dict options:
            The request options for the request.

        :return:
            The new Document.
        :rtype:
            CosmosDict

        """
        base._validate_resource(new_document)
        path = base.GetPathFromLink(document_link)
        document_id = base.GetResourceIdOrFullNameFromLink(document_link)

        # Python's default arguments are evaluated once when the function is defined,
        # not each time the function is called (like it is in say, Ruby). This means
        # that if you use a mutable default argument and mutate it, you will and have
        # mutated that object for all future calls to the function as well. So, using
        # a non-mutable deafult in this case(None) and assigning an empty dict(mutable)
        # inside the function so that it remains local For more details on this gotcha,
        # please refer http://docs.python-guide.org/en/latest/writing/gotchas/
        if options is None:
            options = {}

        # Extract the document collection link and add the partition key to options
        collection_link = base.GetItemContainerLink(document_link)
        options = self._AddPartitionKey(collection_link, new_document, options)

        return self.Replace(new_document,
                            path,
                            http_constants.ResourceType.Document,
                            document_id,
                            None,
                            options,
                            **kwargs)

    def PatchItem(
        self,
        document_link: str,
        operations: List[Dict[str, Any]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> CosmosDict:
        """Patches a document and returns it.

        :param str document_link: The link to the document.
        :param list operations: The operations for the patch request.
        :param dict options: The request options for the request.

        :return:
            The new Document.
        :rtype:
            CosmosDict

        """
        response_hook = kwargs.pop("response_hook", None)
        path = base.GetPathFromLink(document_link)
        document_id = base.GetResourceIdOrFullNameFromLink(document_link)
        resource_type = http_constants.ResourceType.Document
        if options is None:
            options = {}

        headers = base.GetHeaders(self, self.default_headers, "patch", path, document_id, resource_type,
                                  documents._OperationType.Patch, options)
        # Patch will use WriteEndpoint since it uses PUT operation
        request_params = RequestObject(resource_type,
                                       documents._OperationType.Patch,
                                       headers)
        request_params.set_excluded_location_from_options(options)
        base.set_session_token_header(self, headers, path, request_params, options)
        request_params.set_retry_write(options, self.connection_policy.RetryNonIdempotentWrites)
        request_data = {}
        if options.get("filterPredicate"):
            request_data["condition"] = options.get("filterPredicate")
        request_data["operations"] = operations
        result, last_response_headers = self.__Patch(path, request_params, request_data, headers, **kwargs)
        self.last_response_headers = last_response_headers

        # update session for request mutates data on server side
        self._UpdateSessionIfRequired(headers, result, last_response_headers)
        if response_hook:
            response_hook(last_response_headers, result)
        return CosmosDict(result, response_headers=last_response_headers)

    def Batch(
        self,
        collection_link: str,
        batch_operations: Sequence[Union[Tuple[str, Tuple[Any, ...]], Tuple[str, Tuple[Any, ...], Dict[str, Any]]]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> CosmosList:
        """Executes the given operations in transactional batch.

        :param str collection_link: The link to the collection
        :param list batch_operations: The batch of operations for the batch request.
        :param dict options: The request options for the request.

        :return:
            The result of the batch operation.
        :rtype:
            CosmosList

        """
        response_hook = kwargs.pop("response_hook", None)
        if options is None:
            options = {}

        path = base.GetPathFromLink(collection_link, http_constants.ResourceType.Document)
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)
        formatted_operations = base._format_batch_operations(batch_operations)

        results, last_response_headers = self._Batch(
            formatted_operations,
            path,
            collection_id,
            options,
            **kwargs
        )
        self.last_response_headers = last_response_headers
        final_responses = []
        is_error = False
        error_status = 0
        error_index = 0
        for i, result in enumerate(results):
            final_responses.append(result)
            status_code = int(result["statusCode"])
            if status_code >= 400:
                is_error = True
                if status_code != 424:  # Find the operation that had the error
                    error_status = status_code
                    error_index = i
        if is_error:
            raise exceptions.CosmosBatchOperationError(
                error_index=error_index,
                headers=last_response_headers,
                status_code=error_status,
                message="There was an error in the transactional batch on index {}. Error message: {}".format(
                    str(error_index),
                    Constants.ERROR_TRANSLATIONS.get(error_status)
                ),
                operation_responses=final_responses
            )
        if response_hook:
            response_hook(last_response_headers, final_responses)
        return CosmosList(final_responses, response_headers=last_response_headers)

    def _Batch(
        self,
        batch_operations: List[Dict[str, Any]],
        path: str,
        collection_id: Optional[str],
        options: Mapping[str, Any],
        **kwargs: Any
    ) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
        initial_headers = self.default_headers.copy()
        base._populate_batch_headers(initial_headers)
        headers = base.GetHeaders(self, initial_headers, "post", path, collection_id,
                                  http_constants.ResourceType.Document,
                                  documents._OperationType.Batch, options)
        request_params = RequestObject(http_constants.ResourceType.Document,
                                       documents._OperationType.Batch,
                                       headers)
        request_params.set_excluded_location_from_options(options)
        base.set_session_token_header(self, headers, path, request_params, options)
        return cast(
            Tuple[List[Dict[str, Any]], CaseInsensitiveDict],
            self.__Post(path, request_params, batch_operations, headers, **kwargs)
        )

    def DeleteItem(
        self,
        document_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a document.

        :param str document_link:
            The link to the document.
        :param dict options:
            The request options for the request.

        :return:
            The deleted Document.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(document_link)
        document_id = base.GetResourceIdOrFullNameFromLink(document_link)
        self.DeleteResource(path, http_constants.ResourceType.Document, document_id, None, options, **kwargs)

    def DeleteAllItemsByPartitionKey(
        self,
        collection_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        """Exposes an API to delete all items with a single partition key without the user having
         to explicitly call delete on each record in the partition key.

        :param str collection_link:
            The link to the document collection.
        :param dict options:
            The request options for the request.
        :return:
            None
        :rtype:
            None
        """
        response_hook = kwargs.pop("response_hook", None)
        if options is None:
            options = {}

        path = base.GetPathFromLink(collection_link)
        # Specified url to perform background operation to delete all items by partition key
        path = '{}{}/{}'.format(path, "operations", "partitionkeydelete")
        collection_id = base.GetResourceIdOrFullNameFromLink(collection_link)
        headers = base.GetHeaders(self, self.default_headers, "post", path, collection_id,
                                  http_constants.ResourceType.PartitionKey, documents._OperationType.Delete, options)
        request_params = RequestObject(http_constants.ResourceType.PartitionKey,
                                       documents._OperationType.Delete,
                                       headers)
        request_params.set_excluded_location_from_options(options)
        _, last_response_headers = self.__Post(
            path=path,
            request_params=request_params,
            req_headers=headers,
            body=None,
            **kwargs
        )
        self._UpdateSessionIfRequired(headers, None, last_response_headers)
        self.last_response_headers = last_response_headers
        if response_hook:
            response_hook(last_response_headers, None)

    def ReplaceTrigger(
        self,
        trigger_link: str,
        trigger: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Replaces a trigger and returns it.

        :param str trigger_link:
            The link to the trigger.
        :param dict trigger:
        :param dict options:
            The request options for the request.

        :return:
            The replaced Trigger.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        base._validate_resource(trigger)
        trigger = dict(trigger)
        if trigger.get("serverScript"):
            trigger["body"] = str(trigger.pop("serverScript", ""))
        elif trigger.get("body"):
            trigger["body"] = str(trigger["body"])

        path = base.GetPathFromLink(trigger_link)
        trigger_id = base.GetResourceIdOrFullNameFromLink(trigger_link)
        return self.Replace(trigger, path, http_constants.ResourceType.Trigger, trigger_id, None, options, **kwargs)

    def DeleteTrigger(
        self,
        trigger_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a trigger.

        :param str trigger_link:
            The link to the trigger.
        :param dict options:
            The request options for the request.

        :return:
            The deleted Trigger.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(trigger_link)
        trigger_id = base.GetResourceIdOrFullNameFromLink(trigger_link)
        self.DeleteResource(path, http_constants.ResourceType.Trigger, trigger_id, None, options, **kwargs)

    def ReplaceUserDefinedFunction(
        self,
        udf_link: str,
        udf: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Replaces a user-defined function and returns it.

        :param str udf_link:
            The link to the user-defined function.
        :param dict udf:
        :param dict options:
            The request options for the request.

        :return:
            The new UDF.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        base._validate_resource(udf)
        udf = dict(udf)
        if udf.get("serverScript"):
            udf["body"] = str(udf.pop("serverScript", ""))
        elif udf.get("body"):
            udf["body"] = str(udf["body"])

        path = base.GetPathFromLink(udf_link)
        udf_id = base.GetResourceIdOrFullNameFromLink(udf_link)
        return self.Replace(udf, path, http_constants.ResourceType.UserDefinedFunction, udf_id, None, options, **kwargs)

    def DeleteUserDefinedFunction(
        self,
        udf_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a user-defined function.

        :param str udf_link:
            The link to the user-defined function.
        :param dict options:
            The request options for the request.

        :return:
            The deleted UDF.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(udf_link)
        udf_id = base.GetResourceIdOrFullNameFromLink(udf_link)
        self.DeleteResource(path, http_constants.ResourceType.UserDefinedFunction, udf_id, None, options, **kwargs)

    def ExecuteStoredProcedure(
        self,
        sproc_link: str,
        params: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Executes a store procedure.

        :param str sproc_link:
            The link to the stored procedure.
        :param dict params:
            List or None
        :param dict options:
            The request options for the request.

        :return:
            The Stored Procedure response.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        initial_headers = self.default_headers.copy()
        initial_headers[http_constants.HttpHeaders.Accept] = runtime_constants.MediaTypes.Json

        if params and not isinstance(params, list):
            params = [params]

        path = base.GetPathFromLink(sproc_link)
        sproc_id = base.GetResourceIdOrFullNameFromLink(sproc_link)
        headers = base.GetHeaders(self, initial_headers, "post", path, sproc_id,
                                  http_constants.ResourceType.StoredProcedure,
                                  documents._OperationType.ExecuteJavaScript, options)

        # ExecuteStoredProcedure will use WriteEndpoint since it uses POST operation
        request_params = RequestObject(http_constants.ResourceType.StoredProcedure,
                                       documents._OperationType.ExecuteJavaScript, headers)
        result, self.last_response_headers = self.__Post(path, request_params, params, headers, **kwargs)
        return result

    def ReplaceStoredProcedure(
        self,
        sproc_link: str,
        sproc: Dict[str, Any],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Replaces a stored procedure and returns it.

        :param str sproc_link:
            The link to the stored procedure.
        :param dict sproc:
        :param dict options:
            The request options for the request.

        :return:
            The replaced Stored Procedure.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        base._validate_resource(sproc)
        sproc = dict(sproc)
        if sproc.get("serverScript"):
            sproc["body"] = str(sproc.pop("serverScript", ""))
        elif sproc.get("body"):
            sproc["body"] = str(sproc["body"])

        path = base.GetPathFromLink(sproc_link)
        sproc_id = base.GetResourceIdOrFullNameFromLink(sproc_link)
        return self.Replace(sproc, path, http_constants.ResourceType.StoredProcedure, sproc_id, None, options, **kwargs)

    def DeleteStoredProcedure(
        self,
        sproc_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a stored procedure.

        :param str sproc_link:
            The link to the stored procedure.
        :param dict options:
            The request options for the request.

        :return:
            The deleted Stored Procedure.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(sproc_link)
        sproc_id = base.GetResourceIdOrFullNameFromLink(sproc_link)
        self.DeleteResource(path, http_constants.ResourceType.StoredProcedure, sproc_id, None, options, **kwargs)

    def DeleteConflict(
        self,
        conflict_link: str,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a conflict.

        :param str conflict_link:
            The link to the conflict.
        :param dict options:
            The request options for the request.

        :return:
            The deleted Conflict.
        :rtype:
            dict

        """
        if options is None:
            options = {}

        path = base.GetPathFromLink(conflict_link)
        conflict_id = base.GetResourceIdOrFullNameFromLink(conflict_link)
        self.DeleteResource(path, http_constants.ResourceType.Conflict, conflict_id, None, options, **kwargs)

    def ReplaceOffer(
        self,
        offer_link: str,
        offer: Dict[str, Any],
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Replaces an offer and returns it.

        :param str offer_link:
            The link to the offer.
        :param dict offer:

        :return:
            The replaced Offer.
        :rtype:
            dict

        """
        base._validate_resource(offer)
        path = base.GetPathFromLink(offer_link)
        offer_id = base.GetResourceIdOrFullNameFromLink(offer_link)
        return self.Replace(offer, path, http_constants.ResourceType.Offer, offer_id, None, None, **kwargs)

    def ReadOffer(
        self,
        offer_link: str,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Reads an offer.
        :param str offer_link:
            The link to the offer.
        :return:
            The read Offer.
        :rtype:
            dict
        """
        path = base.GetPathFromLink(offer_link)
        offer_id = base.GetResourceIdOrFullNameFromLink(offer_link)
        return self.Read(path, http_constants.ResourceType.Offer, offer_id, None, {}, **kwargs)

    def ReadOffers(
        self,
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Reads all offers.
        :param dict options:
            The request options for the request
        :return:
            Query Iterable of Offers.
        :rtype:
            query_iterable.QueryIterable
        """
        if options is None:
            options = {}

        return self.QueryOffers(None, options, **kwargs)

    def QueryOffers(
        self,
        query: Optional[Union[str, Dict[str, Any]]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> ItemPaged[Dict[str, Any]]:
        """Query for all offers.

        :param (str or dict) query:
        :param dict options:
            The request options for the request

        :return:
            Query Iterable of Offers.
        :rtype:
            query_iterable.QueryIterable

        """
        if options is None:
            options = {}

        def fetch_fn(options: Mapping[str, Any]) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
            return self.__QueryFeed(
                    "/offers", http_constants.ResourceType.Offer, "", lambda r: r["Offers"],
                    lambda _, b: b, query, options, **kwargs)

        return ItemPaged(
            self, query, options, fetch_function=fetch_fn, page_iterator_class=query_iterable.QueryIterable
        )

    def GetDatabaseAccount(
        self,
        url_connection: Optional[str] = None,
        **kwargs: Any
    ) -> DatabaseAccount:
        """Gets database account info.

        :param str url_connection: the endpoint used to get the database account
        :return: The Database Account.
        :rtype: documents.DatabaseAccount
        """
        response_hook = kwargs.pop("response_hook", None)
        if url_connection is None:
            url_connection = self.url_connection

        headers = base.GetHeaders(self, self.default_headers, "get", "", "", "",
                                  documents._OperationType.Read,{}, client_id=self.client_id)
        request_params = RequestObject(http_constants.ResourceType.DatabaseAccount,
                                       documents._OperationType.Read,
                                       headers,
                                       url_connection)
        result, last_response_headers = self.__Get("", request_params, headers, **kwargs)
        self.last_response_headers = last_response_headers
        database_account = DatabaseAccount()
        database_account.DatabasesLink = "/dbs/"
        database_account.MediaLink = "/media/"
        if http_constants.HttpHeaders.MaxMediaStorageUsageInMB in self.last_response_headers:
            database_account.MaxMediaStorageUsageInMB = self.last_response_headers[
                http_constants.HttpHeaders.MaxMediaStorageUsageInMB
            ]
        if http_constants.HttpHeaders.CurrentMediaStorageUsageInMB in self.last_response_headers:
            database_account.CurrentMediaStorageUsageInMB = self.last_response_headers[
                http_constants.HttpHeaders.CurrentMediaStorageUsageInMB
            ]
        database_account.ConsistencyPolicy = result.get(Constants.UserConsistencyPolicy)

        # WritableLocations and ReadableLocations fields will be available only for geo-replicated database accounts
        if Constants.WritableLocations in result:
            database_account._WritableLocations = result[Constants.WritableLocations]
        if Constants.ReadableLocations in result:
            database_account._ReadableLocations = result[Constants.ReadableLocations]
        if Constants.EnableMultipleWritableLocations in result:
            database_account._EnableMultipleWritableLocations = result[
                Constants.EnableMultipleWritableLocations
            ]

        self.UseMultipleWriteLocations = (
                self.connection_policy.UseMultipleWriteLocations and database_account._EnableMultipleWritableLocations
        )
        if response_hook:
            response_hook(last_response_headers, result)
        return database_account

    def _GetDatabaseAccountCheck(
            self,
            url_connection: Optional[str] = None,
            **kwargs: Any
    ):
        """Gets database account info.

        :param str url_connection: the endpoint used to get the database account
        :return: The Database Account.
        :rtype: documents.DatabaseAccount
        """
        if url_connection is None:
            url_connection = self.url_connection

        headers = base.GetHeaders(self, self.default_headers, "get", "", "", "",
                                  documents._OperationType.Read,{}, client_id=self.client_id)
        request_params = RequestObject(http_constants.ResourceType.DatabaseAccount,
                                       documents._OperationType.Read,
                                       headers,
                                       url_connection)
        self.__Get("", request_params, headers, **kwargs)


    def Create(
        self,
        body: Dict[str, Any],
        path: str,
        resource_type: str,
        id: Optional[str],
        initial_headers: Optional[Mapping[str, Any]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> CosmosDict:
        """Creates an Azure Cosmos resource and returns it.

        :param dict body:
        :param str path:
        :param str resource_type:
        :param str id:
        :param dict initial_headers:
        :param dict options:
            The request options for the request.

        :return:
            The created Azure Cosmos resource.
        :rtype:
            CosmosDict

        """
        response_hook = kwargs.pop('response_hook', None)
        if options is None:
            options = {}

        initial_headers = initial_headers or self.default_headers
        headers = base.GetHeaders(self, initial_headers, "post", path, id, resource_type,
                                    documents._OperationType.Create, options)
        # Create will use WriteEndpoint since it uses POST operation
        request_params = RequestObject(resource_type, documents._OperationType.Create, headers)
        request_params.set_excluded_location_from_options(options)
        base.set_session_token_header(self, headers, path, request_params, options)
        request_params.set_retry_write(options, self.connection_policy.RetryNonIdempotentWrites)
        result, last_response_headers = self.__Post(path, request_params, body, headers, **kwargs)
        self.last_response_headers = last_response_headers

        # update session for write request
        self._UpdateSessionIfRequired(headers, result, last_response_headers)
        if response_hook:
            response_hook(last_response_headers, result)
        return CosmosDict(result, response_headers=last_response_headers)

    def Upsert(
        self,
        body: Dict[str, Any],
        path: str,
        resource_type: str,
        id: Optional[str],
        initial_headers: Optional[Mapping[str, Any]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> CosmosDict:
        """Upserts an Azure Cosmos resource and returns it.

        :param dict body:
        :param str path:
        :param str resource_type:
        :param str id:
        :param dict initial_headers:
        :param dict options:
            The request options for the request.

        :return:
            The upserted Azure Cosmos resource.
        :rtype:
            CosmosDict

        """
        response_hook = kwargs.pop('response_hook', None)
        if options is None:
            options = {}

        initial_headers = initial_headers or self.default_headers
        headers = base.GetHeaders(self, initial_headers, "post", path, id, resource_type,
                                    documents._OperationType.Upsert, options)
        headers[http_constants.HttpHeaders.IsUpsert] = True
        # Upsert will use WriteEndpoint since it uses POST operation
        request_params = RequestObject(resource_type, documents._OperationType.Upsert, headers)
        request_params.set_excluded_location_from_options(options)
        base.set_session_token_header(self, headers, path, request_params, options)
        request_params.set_retry_write(options, self.connection_policy.RetryNonIdempotentWrites)
        result, last_response_headers = self.__Post(path, request_params, body, headers, **kwargs)
        self.last_response_headers = last_response_headers
        # update session for write request
        self._UpdateSessionIfRequired(headers, result, last_response_headers)
        if response_hook:
            response_hook(last_response_headers, result)
        return CosmosDict(result, response_headers=last_response_headers)

    def Replace(
        self,
        resource: Dict[str, Any],
        path: str,
        resource_type: str,
        id: Optional[str],
        initial_headers: Optional[Mapping[str, Any]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> CosmosDict:
        """Replaces an Azure Cosmos resource and returns it.

        :param dict resource:
        :param str path:
        :param str resource_type:
        :param str id:
        :param dict initial_headers:
        :param dict options:
            The request options for the request.

        :return:
            The new Azure Cosmos resource.
        :rtype:
            CosmosDict

        """
        response_hook = kwargs.pop('response_hook', None)
        if options is None:
            options = {}

        initial_headers = initial_headers or self.default_headers
        headers = base.GetHeaders(self, initial_headers, "put", path, id, resource_type,
                                    documents._OperationType.Replace, options)
        # Replace will use WriteEndpoint since it uses PUT operation
        request_params = RequestObject(resource_type, documents._OperationType.Replace, headers)
        request_params.set_excluded_location_from_options(options)
        base.set_session_token_header(self, headers, path, request_params, options)
        request_params.set_retry_write(options, self.connection_policy.RetryNonIdempotentWrites)
        result, last_response_headers = self.__Put(path, request_params, resource, headers, **kwargs)
        self.last_response_headers = last_response_headers

        # update session for request mutates data on server side
        self._UpdateSessionIfRequired(headers, result, last_response_headers)
        if response_hook:
            response_hook(last_response_headers, result)
        return CosmosDict(result, response_headers=last_response_headers)

    def Read(
        self,
        path: str,
        resource_type: str,
        id: Optional[str],
        initial_headers: Optional[Mapping[str, Any]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> CosmosDict:
        """Reads an Azure Cosmos resource and returns it.

        :param str path:
        :param str resource_type:
        :param str id:
        :param dict initial_headers:
        :param dict options:
            The request options for the request.

        :return:
            The requested Azure Cosmos resource.
        :rtype:
            CosmosDict

        """
        response_hook = kwargs.pop('response_hook', None)
        if options is None:
            options = {}

        initial_headers = initial_headers or self.default_headers
        headers = base.GetHeaders(self, initial_headers, "get", path, id, resource_type,
                                    documents._OperationType.Read, options)
        # Read will use ReadEndpoint since it uses GET operation
        request_params = RequestObject(resource_type, documents._OperationType.Read, headers)
        request_params.set_excluded_location_from_options(options)
        base.set_session_token_header(self, headers, path, request_params, options)
        result, last_response_headers = self.__Get(path, request_params, headers, **kwargs)
        # update session for request mutates data on server side
        self._UpdateSessionIfRequired(headers, result, last_response_headers)

        self.last_response_headers = last_response_headers
        if response_hook:
            response_hook(last_response_headers, result)
        return CosmosDict(result, response_headers=last_response_headers)

    def DeleteResource(
        self,
        path: str,
        resource_type: str,
        id: Optional[str],
        initial_headers: Optional[Mapping[str, Any]],
        options: Optional[Mapping[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        """Deletes an Azure Cosmos resource and returns it.

        :param str path:
        :param str resource_type:
        :param str id:
        :param dict initial_headers:
        :param dict options:
            The request options for the request.

        :return:
            The deleted Azure Cosmos resource.
        :rtype:
            dict

        """
        response_hook = kwargs.pop('response_hook', None)
        if options is None:
            options = {}

        initial_headers = initial_headers or self.default_headers
        headers = base.GetHeaders(self, initial_headers, "delete", path, id, resource_type,
                                    documents._OperationType.Delete, options)
        # Delete will use WriteEndpoint since it uses DELETE operation
        request_params = RequestObject(resource_type, documents._OperationType.Delete, headers)
        base.set_session_token_header(self, headers, path, request_params, options)
        request_params.set_retry_write(options, self.connection_policy.RetryNonIdempotentWrites)
        request_params.set_excluded_location_from_options(options)
        result, last_response_headers = self.__Delete(path, request_params, headers, **kwargs)
        self.last_response_headers = last_response_headers

        # update session for request mutates data on server side
        self._UpdateSessionIfRequired(headers, result, last_response_headers)
        if response_hook:
            response_hook(last_response_headers, None)

    def __Get(
        self,
        path: str,
        request_params: RequestObject,
        req_headers: Dict[str, Any],
        **kwargs: Any
    ) -> Tuple[Dict[str, Any], CaseInsensitiveDict]:
        """Azure Cosmos 'GET' http request.

        :param str path: the url to be used for the request.
        :param ~azure.cosmos._request_object.RequestObject request_params: the request parameters.
        :param Dict[str, Any] req_headers: the request headers.
        :return: Tuple of (result, headers).
        :rtype: tuple of (dict, dict)
        """
        request = self.pipeline_client.get(url=path, headers=req_headers)
        return synchronized_request.SynchronizedRequest(
            client=self,
            request_params=request_params,
            global_endpoint_manager=self._global_endpoint_manager,
            connection_policy=self.connection_policy,
            pipeline_client=self.pipeline_client,
            request=request,
            request_data=None,
            **kwargs
        )

    def __Post(
        self,
        path: str,
        request_params: RequestObject,
        body: Optional[Union[str, List[Dict[str, Any]], Dict[str, Any]]],
        req_headers: Dict[str, Any],
        **kwargs: Any
    ) -> Tuple[Dict[str, Any], CaseInsensitiveDict]:
        """Azure Cosmos 'POST' http request.

        :param str path: the url to be used for the request.
        :param ~azure.cosmos._request_object.RequestObject request_params: the request parameters.
        :param Union[str, List[Dict[str, Any]], Dict[Any, Any]] body: the request body.
        :param Dict[str, Any] req_headers: the request headers.
        :return: Tuple of (result, headers).
        :rtype: tuple of (dict, dict)
        """
        request = self.pipeline_client.post(url=path, headers=req_headers)
        return synchronized_request.SynchronizedRequest(
            client=self,
            request_params=request_params,
            global_endpoint_manager=self._global_endpoint_manager,
            connection_policy=self.connection_policy,
            pipeline_client=self.pipeline_client,
            request=request,
            request_data=body,
            **kwargs
        )

    def __Put(
        self,
        path: str,
        request_params: RequestObject,
        body: Dict[str, Any],
        req_headers: Dict[str, Any],
        **kwargs: Any
    ) -> Tuple[Dict[str, Any], CaseInsensitiveDict]:
        """Azure Cosmos 'PUT' http request.

        :param str path: the url to be used for the request.
        :param ~azure.cosmos._request_object.RequestObject request_params: the request parameters.
        :param Union[str, unicode, Dict[Any, Any]] body: the request body.
        :param Dict[str, Any] req_headers: the request headers.
        :return: Tuple of (result, headers).
        :rtype: tuple of (dict, dict)
        """
        request = self.pipeline_client.put(url=path, headers=req_headers)
        return synchronized_request.SynchronizedRequest(
            client=self,
            request_params=request_params,
            global_endpoint_manager=self._global_endpoint_manager,
            connection_policy=self.connection_policy,
            pipeline_client=self.pipeline_client,
            request=request,
            request_data=body,
            **kwargs
        )

    def __Patch(
        self,
        path: str,
        request_params: RequestObject,
        request_data: Dict[str, Any],
        req_headers: Dict[str, Any],
        **kwargs: Any
    ) -> Tuple[Dict[str, Any], CaseInsensitiveDict]:
        """Azure Cosmos 'PATCH' http request.

        :param str path: the url to be used for the request.
        :param ~azure.cosmos._request_object.RequestObject request_params: the request parameters.
        :param Union[str, Dict[Any, Any]] request_data: the request body.
        :param Dict[str, Any] req_headers: the request headers.
        :return: Tuple of (result, headers).
        :rtype: tuple of (dict, dict)
        """
        request = self.pipeline_client.patch(url=path, headers=req_headers)
        return synchronized_request.SynchronizedRequest(
            client=self,
            request_params=request_params,
            global_endpoint_manager=self._global_endpoint_manager,
            connection_policy=self.connection_policy,
            pipeline_client=self.pipeline_client,
            request=request,
            request_data=request_data,
            **kwargs
        )

    def __Delete(
        self,
        path: str,
        request_params: RequestObject,
        req_headers: Dict[str, Any],
        **kwargs: Any
    ) -> Tuple[None, CaseInsensitiveDict]:
        """Azure Cosmos 'DELETE' http request.

        :param str path: the url to be used for the request.
        :param ~azure.cosmos._request_object.RequestObject request_params: the request parameters.
        :param Dict[str, Any] req_headers: the request headers.
        :return: Tuple of (result, headers).
        :rtype: tuple of (dict, dict)
        """
        request = self.pipeline_client.delete(url=path, headers=req_headers)
        return synchronized_request.SynchronizedRequest(
            client=self,
            request_params=request_params,
            global_endpoint_manager=self._global_endpoint_manager,
            connection_policy=self.connection_policy,
            pipeline_client=self.pipeline_client,
            request=request,
            request_data=None,
            **kwargs
        )

    def QueryFeed(
        self,
        path: str,
        collection_id: str,
        query: Optional[Union[str, Dict[str, Any]]],
        options: Mapping[str, Any],
        partition_key_range_id: Optional[str] = None,
        **kwargs: Any
    ) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
        """Query Feed for Document Collection resource.

        :param str path: Path to the document collection.
        :param str collection_id: Id of the document collection.
        :param (str or dict) query:
        :param dict options: The request options for the request.
        :param str partition_key_range_id: Partition key range id.
        :return: Tuple of (result, headers).
        :rtype: tuple of (dict, dict)
        """
        return self.__QueryFeed(
                path,
                http_constants.ResourceType.Document,
                collection_id,
                lambda r: r["Documents"],
                lambda _, b: b,
                query,
                options,
                partition_key_range_id,
                **kwargs)

    def __QueryFeed(  # pylint: disable=too-many-locals, too-many-statements, too-many-branches
        self,
        path: str,
        resource_type: str,
        resource_id: Optional[str],
        result_fn: Callable[[Dict[str, Any]], List[Dict[str, Any]]],
        create_fn: Optional[Callable[['CosmosClientConnection', Dict[str, Any]], Dict[str, Any]]],
        query: Optional[Union[str, Dict[str, Any]]],
        options: Optional[Mapping[str, Any]] = None,
        partition_key_range_id: Optional[str] = None,
        response_hook: Optional[Callable[[Mapping[str, Any], Dict[str, Any]], None]] = None,
        is_query_plan: bool = False,
        **kwargs: Any
    ) -> Tuple[List[Dict[str, Any]], CaseInsensitiveDict]:
        """Query for more than one Azure Cosmos resources.

        :param str path:
        :param str resource_type:
        :param str resource_id:
        :param function result_fn:
        :param function create_fn:
        :param (str or dict) query:
        :param dict options:
            The request options for the request.
        :param str partition_key_range_id:
            Specifies partition key range id.
        :param response_hook: A callable invoked with the response metadata.
        :type response_hook: Callable[[Mapping[str, Any], Dict[str, Any]], None]
        :param bool is_query_plan:
            Specifies if the call is to fetch query plan
        :returns: A list of the queried resources.
        :rtype: list
        :raises SystemError: If the query compatibility mode is undefined.
        """
        if options is None:
            options = {}

        if query:
            __GetBodiesFromQueryResult = result_fn
        else:

            def __GetBodiesFromQueryResult(result: Dict[str, Any]) -> List[Dict[str, Any]]:
                if create_fn and result is not None:
                    return [create_fn(self, body) for body in result_fn(result)]
                # If there is no change feed, the result data is empty and result is None.
                # This case should be interpreted as an empty array.
                return []

        # TODO: copy is not needed if query was none, since the header was copied inside of "base.GetHeaders"
        initial_headers = self.default_headers.copy()
        # Copy to make sure that default_headers won't be changed.
        if query is None:
            op_type = documents._OperationType.QueryPlan if is_query_plan else documents._OperationType.ReadFeed
            # Query operations will use ReadEndpoint even though it uses GET(for feed requests)
            headers = base.GetHeaders(
                self,
                initial_headers,
                "get",
                path,
                resource_id,
                resource_type,
                op_type,
                options,
                partition_key_range_id
            )
            request_params = RequestObject(
                resource_type,
                op_type,
                headers
            )
            request_params.set_excluded_location_from_options(options)
            base.set_session_token_header(self, headers, path, request_params, options, partition_key_range_id)

            change_feed_state: Optional[ChangeFeedState] = options.get("changeFeedState")
            if change_feed_state is not None:
                feed_options = {}
                if 'excludedLocations' in options:
                    feed_options['excludedLocations'] = options['excludedLocations']
                change_feed_state.populate_request_headers(self._routing_map_provider, headers, feed_options)
                request_params.headers = headers

            result, last_response_headers = self.__Get(path, request_params, headers, **kwargs)
            self.last_response_headers = last_response_headers
            if response_hook:
                response_hook(last_response_headers, result)
            return __GetBodiesFromQueryResult(result), last_response_headers

        query = self.__CheckAndUnifyQueryFormat(query)

        if (self._query_compatibility_mode in (CosmosClientConnection._QueryCompatibilityMode.Default,
                                               CosmosClientConnection._QueryCompatibilityMode.Query)):
            initial_headers[http_constants.HttpHeaders.ContentType] = runtime_constants.MediaTypes.QueryJson
        elif self._query_compatibility_mode == CosmosClientConnection._QueryCompatibilityMode.SqlQuery:
            initial_headers[http_constants.HttpHeaders.ContentType] = runtime_constants.MediaTypes.SQL
        else:
            raise SystemError("Unexpected query compatibility mode.")

        # Query operations will use ReadEndpoint even though it uses POST(for regular query operations)
        req_headers = base.GetHeaders(
            self,
            initial_headers,
            "post",
            path,
            resource_id,
            resource_type,
            documents._OperationType.SqlQuery,
            options,
            partition_key_range_id
        )
        request_params = RequestObject(resource_type, documents._OperationType.SqlQuery, req_headers)
        request_params.set_excluded_location_from_options(options)
        if not is_query_plan:
            req_headers[http_constants.HttpHeaders.IsQuery] = "true"
            base.set_session_token_header(self, req_headers, path, request_params, options, partition_key_range_id)

        # Check if the over lapping ranges can be populated
        feed_range_epk = None
        if "feed_range" in kwargs:
            feed_range = kwargs.pop("feed_range")
            feed_range_epk = FeedRangeInternalEpk.from_json(feed_range).get_normalized_range()
        elif "prefix_partition_key_object" in kwargs and "prefix_partition_key_value" in kwargs:
            prefix_partition_key_obj = kwargs.pop("prefix_partition_key_object")
            prefix_partition_key_value: _SequentialPartitionKeyType = kwargs.pop("prefix_partition_key_value")
            feed_range_epk = (
                prefix_partition_key_obj._get_epk_range_for_prefix_partition_key(prefix_partition_key_value))

        # If feed_range_epk exist, query with the range
        if feed_range_epk is not None:
            last_response_headers = CaseInsensitiveDict()
            over_lapping_ranges = self._routing_map_provider.get_overlapping_ranges(resource_id, [feed_range_epk],
                                                                                    options)
            # It is possible to get more than one over lapping range. We need to get the query results for each one
            results: Dict[str, Any] = {}
            # For each over lapping range we will take a sub range of the feed range EPK that overlaps with the over
            # lapping physical partition. The EPK sub range will be one of four:
            # 1) Will have a range min equal to the feed range EPK min, and a range max equal to the over lapping
            # partition
            # 2) Will have a range min equal to the over lapping partition range min, and a range max equal to the
            # feed range EPK range max.
            # 3) will match exactly with the current over lapping physical partition, so we just return the over lapping
            # physical partition's partition key id.
            # 4) Will equal the feed range EPK since it is a sub range of a single physical partition
            for over_lapping_range in over_lapping_ranges:
                single_range = routing_range.Range.PartitionKeyRangeToRange(over_lapping_range)
                # Since the range min and max are all Upper Cased string Hex Values,
                # we can compare the values lexicographically
                EPK_sub_range = routing_range.Range(range_min=max(single_range.min, feed_range_epk.min),
                                                    range_max=min(single_range.max, feed_range_epk.max),
                                                    isMinInclusive=True, isMaxInclusive=False)
                if single_range.min == EPK_sub_range.min and EPK_sub_range.max == single_range.max:
                    # The Epk Sub Range spans exactly one physical partition
                    # In this case we can route to the physical pk range id
                    req_headers[http_constants.HttpHeaders.PartitionKeyRangeID] = over_lapping_range["id"]
                else:
                    # The Epk Sub Range spans less than a single physical partition
                    # In this case we route to the physical partition and
                    # pass the epk sub range to the headers to filter within partition
                    req_headers[http_constants.HttpHeaders.PartitionKeyRangeID] = over_lapping_range["id"]
                    req_headers[http_constants.HttpHeaders.StartEpkString] = EPK_sub_range.min
                    req_headers[http_constants.HttpHeaders.EndEpkString] = EPK_sub_range.max
                req_headers[http_constants.HttpHeaders.ReadFeedKeyType] = "EffectivePartitionKeyRange"
                partial_result, last_response_headers = self.__Post(
                    path, request_params, query, req_headers, **kwargs
                )
                self.last_response_headers = last_response_headers
                self._UpdateSessionIfRequired(req_headers, partial_result, last_response_headers)
                if results:
                    # add up all the query results from all over lapping ranges
                    results["Documents"].extend(partial_result["Documents"])
                else:
                    results = partial_result
                if response_hook:
                    response_hook(last_response_headers, partial_result)
            # if the prefix partition query has results lets return it
            if results:
                return __GetBodiesFromQueryResult(results), last_response_headers

        result, last_response_headers = self.__Post(path, request_params, query, req_headers, **kwargs)
        self.last_response_headers = last_response_headers
        self._UpdateSessionIfRequired(req_headers, result, last_response_headers)
        if last_response_headers.get(http_constants.HttpHeaders.IndexUtilization) is not None:
            INDEX_METRICS_HEADER = http_constants.HttpHeaders.IndexUtilization
            index_metrics_raw = last_response_headers[INDEX_METRICS_HEADER]
            last_response_headers[INDEX_METRICS_HEADER] = _utils.get_index_metrics_info(index_metrics_raw)
        if response_hook:
            response_hook(last_response_headers, result)

        return __GetBodiesFromQueryResult(result), last_response_headers

    def _GetQueryPlanThroughGateway(self, query: str, resource_link: str, excluded_locations: Optional[str] = None,
                                    **kwargs: Any) -> List[Dict[str, Any]]:
        supported_query_features = (documents._QueryFeature.Aggregate + "," +
                                    documents._QueryFeature.CompositeAggregate + "," +
                                    documents._QueryFeature.Distinct + "," +
                                    documents._QueryFeature.MultipleOrderBy + "," +
                                    documents._QueryFeature.OffsetAndLimit + "," +
                                    documents._QueryFeature.OrderBy + "," +
                                    documents._QueryFeature.Top + "," +
                                    documents._QueryFeature.NonStreamingOrderBy + "," +
                                    documents._QueryFeature.HybridSearch + "," +
                                    documents._QueryFeature.CountIf + "," +
                                    documents._QueryFeature.WeightedRankFusion)
        if os.environ.get(Constants.NON_STREAMING_ORDER_BY_DISABLED_CONFIG,
                          Constants.NON_STREAMING_ORDER_BY_DISABLED_CONFIG_DEFAULT) == "True":
            supported_query_features = (documents._QueryFeature.Aggregate + "," +
                                        documents._QueryFeature.CompositeAggregate + "," +
                                        documents._QueryFeature.Distinct + "," +
                                        documents._QueryFeature.MultipleOrderBy + "," +
                                        documents._QueryFeature.OffsetAndLimit + "," +
                                        documents._QueryFeature.OrderBy + "," +
                                        documents._QueryFeature.Top)

        options = {
            "contentType": runtime_constants.MediaTypes.Json,
            "isQueryPlanRequest": True,
            "supportedQueryFeatures": supported_query_features,
            "queryVersion": http_constants.Versions.QueryVersion
        }
        if excluded_locations is not None:
            options["excludedLocations"] = excluded_locations
        path = base.GetPathFromLink(resource_link, http_constants.ResourceType.Document)
        resource_id = base.GetResourceIdOrFullNameFromLink(resource_link)

        results, last_response_headers = self.__QueryFeed(
            path,
            http_constants.ResourceType.Document,
            resource_id,
            lambda r: cast(List[Dict[str, Any]], r),
            None,
            query,
            options,
            is_query_plan=True,
            **kwargs
        )
        self.last_response_headers = last_response_headers
        return results

    def __CheckAndUnifyQueryFormat(self, query_body: Union[str, Dict[str, Any]]) -> Union[str, Dict[str, Any]]:
        """Checks and unifies the format of the query body.

        :raises TypeError: If query_body is not of expected type (depending on the query compatibility mode).
        :raises ValueError: If query_body is a dict but doesn't have valid query text.
        :raises SystemError: If the query compatibility mode is undefined.

        :param (str or dict) query_body:

        :return:
            The formatted query body.
        :rtype:
            dict or string
        """
        if (self._query_compatibility_mode in (CosmosClientConnection._QueryCompatibilityMode.Default,
                                               CosmosClientConnection._QueryCompatibilityMode.Query)):
            if not isinstance(query_body, dict) and not isinstance(query_body, str):
                raise TypeError("query body must be a dict or string.")
            if isinstance(query_body, dict) and not query_body.get("query"):
                raise ValueError('query body must have valid query text with key "query".')
            if isinstance(query_body, str):
                return {"query": query_body}
        elif (
                self._query_compatibility_mode == CosmosClientConnection._QueryCompatibilityMode.SqlQuery
                and not isinstance(query_body, str)
        ):
            raise TypeError("query body must be a string.")
        else:
            raise SystemError("Unexpected query compatibility mode.")
        return query_body

    # Adds the partition key to options
    def _AddPartitionKey(
        self,
        collection_link: str,
        document: Mapping[str, Any],
        options: Mapping[str, Any]
    ) -> Dict[str, Any]:
        collection_link = base.TrimBeginningAndEndingSlashes(collection_link)
        partitionKeyDefinition = self._get_partition_key_definition(collection_link, options)
        new_options = dict(options)
        # If the collection doesn't have a partition key definition, skip it as it's a legacy collection
        if partitionKeyDefinition:
            # If the user has passed in the partitionKey in options use that else extract it from the document
            if "partitionKey" not in options:
                partitionKeyValue = self._ExtractPartitionKey(partitionKeyDefinition, document)
                new_options["partitionKey"] = partitionKeyValue
        return new_options

    # Extracts the partition key from the document using the partitionKey definition
    def _ExtractPartitionKey(
        self,
        partitionKeyDefinition: Mapping[str, Any],
        document: Mapping[str, Any]
    ) -> Union[List[Optional[Union[str, float, bool]]], str, float, bool, _Empty, _Undefined]:
        if partitionKeyDefinition["kind"] == _PartitionKeyKind.MULTI_HASH:
            ret: List[Optional[Union[str, float, bool]]] = []
            for partition_key_level in partitionKeyDefinition["paths"]:
                # Parses the paths into a list of token each representing a property
                partition_key_parts = base.ParsePaths([partition_key_level])
                # Check if the partitionKey is system generated or not
                is_system_key = partitionKeyDefinition["systemKey"] if "systemKey" in partitionKeyDefinition else False
                # Navigates the document to retrieve the partitionKey specified in the paths
                val: Optional[Union[str, float, bool, _Empty, _Undefined]] = self._retrieve_partition_key(
                    partition_key_parts, document, is_system_key)
                if isinstance(val, (_Undefined, _Empty)):
                    val = None
                ret.append(val)
            return ret

        # Parses the paths into a list of token each representing a property
        partition_key_parts = base.ParsePaths(partitionKeyDefinition["paths"])
        # Check if the partitionKey is system generated or not
        is_system_key = partitionKeyDefinition["systemKey"] if "systemKey" in partitionKeyDefinition else False

        # Navigates the document to retrieve the partitionKey specified in the paths
        return self._retrieve_partition_key(partition_key_parts, document, is_system_key)

    # Navigates the document to retrieve the partitionKey specified in the partition key parts
    def _retrieve_partition_key(
        self,
        partition_key_parts: List[str],
        document: Mapping[str, Any],
        is_system_key: bool
    ) -> Union[str, float, bool, _Empty, _Undefined]:
        expected_matchCount = len(partition_key_parts)
        matchCount = 0
        partitionKey: Union[str, float, bool, Mapping[str, Any]] = document
        for part in partition_key_parts:
            # Once we reach the "leaf" value(not a dict), we break from loop
            if not isinstance(partitionKey, Mapping):
                break
            # At any point if we don't find the value of a sub-property in the document, we return as Undefined
            if part not in partitionKey:
                return _return_undefined_or_empty_partition_key(is_system_key)
            partitionKey = partitionKey[part]
            matchCount += 1

        # Match the count of hops we did to get the partitionKey with the length of
        # partition key parts and validate that it's not a dict at that level
        if (matchCount != expected_matchCount) or isinstance(partitionKey, Mapping):
            return _return_undefined_or_empty_partition_key(is_system_key)
        return partitionKey

    def refresh_routing_map_provider(self) -> None:
        # re-initializes the routing map provider, effectively refreshing the current partition key range cache
        self._routing_map_provider = routing_map_provider.SmartRoutingMapProvider(self)

    def _refresh_container_properties_cache(self, container_link: str):
        # If container properties cache is stale, refresh it by reading the container.
        container = self.ReadContainer(container_link, options=None)
        # Only cache Container Properties that will not change in the lifetime of the container
        self._set_container_properties_cache(container_link, _build_properties_cache(container, container_link))

    def _UpdateSessionIfRequired(
        self,
        request_headers: Mapping[str, Any],
        response_result: Optional[Mapping[str, Any]],
        response_headers: Optional[Mapping[str, Any]]
    ) -> None:
        """
        Updates session if necessary.

        :param dict request_headers: The request headers.
        :param dict response_result: The response result.
        :param dict response_headers: The response headers.
        """

        # if this request was made with consistency level as session, then update the session
        if response_headers is None:
            return
        # deal with delete requests
        if response_result is None:
            response_result = {}

        is_session_consistency = False
        if http_constants.HttpHeaders.ConsistencyLevel in request_headers:
            if documents.ConsistencyLevel.Session == request_headers[http_constants.HttpHeaders.ConsistencyLevel]:
                is_session_consistency = True

        if (is_session_consistency and self.session and http_constants.HttpHeaders.SessionToken in response_headers and
                not base.IsMasterResource(request_headers[http_constants.HttpHeaders.ThinClientProxyResourceType])):
            # update session
            self.session.update_session(self, response_result, response_headers)

    def _get_partition_key_definition(
            self,
            collection_link: str,
            options: Mapping[str, Any]
    ) -> Optional[Dict[str, Any]]:
        partition_key_definition: Optional[Dict[str, Any]]
        # If the document collection link is present in the cache, then use the cached partitionkey definition
        if collection_link in self.__container_properties_cache:
            cached_container: Dict[str, Any] = self.__container_properties_cache.get(collection_link, {})
            partition_key_definition = cached_container.get("partitionKey")
        # Else read the collection from backend and add it to the cache
        else:
            container = self.ReadContainer(collection_link, options)
            partition_key_definition = container.get("partitionKey")
            self._set_container_properties_cache(collection_link, _build_properties_cache(container, collection_link))
        return partition_key_definition
