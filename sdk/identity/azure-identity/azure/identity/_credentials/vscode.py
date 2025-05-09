# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import abc
import os
import sys
from typing import cast, Any, Dict, Optional
import warnings

from azure.core.credentials import AccessToken, TokenRequestOptions, AccessTokenInfo
from azure.core.exceptions import ClientAuthenticationError
from .._exceptions import CredentialUnavailableError
from .._constants import AzureAuthorityHosts, AZURE_VSCODE_CLIENT_ID, EnvironmentVariables
from .._internal import normalize_authority, validate_tenant_id, within_dac
from .._internal.aad_client import AadClient, AadClientBase
from .._internal.get_token_mixin import GetTokenMixin
from .._internal.decorators import log_get_token

if sys.platform.startswith("win"):
    from .._internal.win_vscode_adapter import get_refresh_token, get_user_settings
elif sys.platform.startswith("darwin"):
    from .._internal.macos_vscode_adapter import get_refresh_token, get_user_settings
else:
    from .._internal.linux_vscode_adapter import get_refresh_token, get_user_settings


class _VSCodeCredentialBase(abc.ABC):
    def __init__(self, **kwargs: Any) -> None:
        warnings.warn(
            "This credential is deprecated because the Azure Account extension for Visual Studio Code, which this "
            "credential relies on, has been deprecated. See the Azure Account extension deprecation notice here: "
            "https://github.com/microsoft/vscode-azure-account/issues/964. Consider using other developer credentials "
            "such as AzureCliCredential, AzureDeveloperCliCredential, or AzurePowerShellCredential.",
            DeprecationWarning,
            stacklevel=2,
        )
        super(_VSCodeCredentialBase, self).__init__()

        user_settings = get_user_settings()
        self._cloud = user_settings.get("azure.cloud", "AzureCloud")
        self._refresh_token = None
        self._unavailable_reason = ""

        self._client = kwargs.get("_client")
        if not self._client:
            self._initialize(user_settings, **kwargs)
        if not (self._client or self._unavailable_reason):
            self._unavailable_reason = "Initialization failed"

    @abc.abstractmethod
    def _get_client(self, **kwargs: Any) -> AadClientBase:
        pass

    def _get_refresh_token(self) -> str:
        if not self._refresh_token:
            self._refresh_token = get_refresh_token(self._cloud)
            if not self._refresh_token:
                message = (
                    "Failed to get Azure user details from Visual Studio Code. "
                    "Currently, the VisualStudioCodeCredential only works with the Azure "
                    "Account extension version 0.9.11 and earlier. A long-term fix is in "
                    "progress, see https://github.com/Azure/azure-sdk-for-python/issues/25713"
                )
                raise CredentialUnavailableError(message=message)
        return self._refresh_token

    def _initialize(self, vscode_user_settings: Dict, **kwargs: Any) -> None:
        """Build a client from kwargs merged with VS Code user settings.

        The first stable version of this credential defaulted to Public Cloud and the "organizations"
        tenant when it failed to read VS Code user settings. That behavior is preserved here.

        :param dict vscode_user_settings: VS Code user settings
        """

        # Precedence for authority:
        #  1) VisualStudioCodeCredential(authority=...)
        #  2) $AZURE_AUTHORITY_HOST
        #  3) authority matching VS Code's "azure.cloud" setting
        #  4) default: Public Cloud
        authority = kwargs.pop("authority", None) or os.environ.get(EnvironmentVariables.AZURE_AUTHORITY_HOST)
        if not authority:
            # the application didn't specify an authority, so we figure it out from VS Code settings
            if self._cloud == "AzureCloud":
                authority = AzureAuthorityHosts.AZURE_PUBLIC_CLOUD
            elif self._cloud == "AzureChinaCloud":
                authority = AzureAuthorityHosts.AZURE_CHINA
            elif self._cloud == "AzureUSGovernment":
                authority = AzureAuthorityHosts.AZURE_GOVERNMENT
            else:
                # If the value is anything else ("AzureCustomCloud" is the only other known value),
                # we need the user to provide the authority because VS Code has no setting for it and
                # we can't guess confidently.
                self._unavailable_reason = (
                    'VS Code is configured to use a custom cloud. Set keyword argument "authority"'
                    + ' with the Microsoft Entra endpoint for cloud "{}"'.format(self._cloud)
                )
                return

        # Precedence for tenant ID:
        #  1) VisualStudioCodeCredential(tenant_id=...)
        #  2) "azure.tenant" in VS Code user settings
        #  3) default: organizations
        tenant_id = kwargs.pop("tenant_id", None) or vscode_user_settings.get("azure.tenant", "organizations")
        validate_tenant_id(tenant_id)
        if tenant_id.lower() == "adfs":
            self._unavailable_reason = "VisualStudioCodeCredential authentication unavailable. ADFS is not supported."
            return

        self._client = self._get_client(
            authority=normalize_authority(authority), client_id=AZURE_VSCODE_CLIENT_ID, tenant_id=tenant_id, **kwargs
        )


class VisualStudioCodeCredential(_VSCodeCredentialBase, GetTokenMixin):
    """Authenticates as the Azure user signed in to Visual Studio Code via the 'Azure Account' extension.

    **Deprecated**: This credential is deprecated because the Azure Account extension for Visual Studio Code, which
    this credential relies on, has been deprecated. See the Azure Account extension deprecation notice here:
    https://github.com/microsoft/vscode-azure-account/issues/964. Consider using other developer credentials such as
    AzureCliCredential, AzureDeveloperCliCredential, or AzurePowerShellCredential.

    :keyword str authority: Authority of a Microsoft Entra endpoint, for example "login.microsoftonline.com".
        This argument is required for a custom cloud and usually unnecessary otherwise. Defaults to the authority
        matching the "Azure: Cloud" setting in VS Code's user settings or, when that setting has no value, the
        authority for Azure Public Cloud.
    :keyword str tenant_id: ID of the tenant the credential should authenticate in. Defaults to the "Azure: Tenant"
        setting in VS Code's user settings or, when that setting has no value, the "organizations" tenant, which
        supports only Microsoft Entra work or school accounts.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.
    """

    def __enter__(self) -> "VisualStudioCodeCredential":
        if self._client:
            self._client.__enter__()
        return self

    def __exit__(self, *args: Any) -> None:
        if self._client:
            self._client.__exit__(*args)

    def close(self) -> None:
        """Close the credential's transport session."""
        self.__exit__()

    @log_get_token
    def get_token(
        self, *scopes: str, claims: Optional[str] = None, tenant_id: Optional[str] = None, **kwargs: Any
    ) -> AccessToken:
        """Request an access token for `scopes` as the user currently signed in to Visual Studio Code.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
            For more information about scopes, see
            https://learn.microsoft.com/entra/identity-platform/scopes-oidc.
        :keyword str claims: additional claims required in the token, such as those returned in a resource provider's
            claims challenge following an authorization failure.
        :keyword str tenant_id: optional tenant to include in the token request.

        :return: An access token with the desired scopes.
        :rtype: ~azure.core.credentials.AccessToken
        :raises ~azure.identity.CredentialUnavailableError: the credential cannot retrieve user details from Visual
          Studio Code
        """
        if self._unavailable_reason:
            error_message = (
                self._unavailable_reason + "\n"
                "Visit https://aka.ms/azsdk/python/identity/vscodecredential/troubleshoot"
                " to troubleshoot this issue."
            )
            raise CredentialUnavailableError(message=error_message)
        if within_dac.get():
            try:
                token = super().get_token(*scopes, claims=claims, tenant_id=tenant_id, **kwargs)
                return token
            except ClientAuthenticationError as ex:
                raise CredentialUnavailableError(message=ex.message) from ex
        return super().get_token(*scopes, claims=claims, tenant_id=tenant_id, **kwargs)

    def get_token_info(self, *scopes: str, options: Optional[TokenRequestOptions] = None) -> AccessTokenInfo:
        """Request an access token for `scopes` as the user currently signed in to Visual Studio Code.

        This is an alternative to `get_token` to enable certain scenarios that require additional properties
        on the token. This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
            For more information about scopes, see https://learn.microsoft.com/entra/identity-platform/scopes-oidc.
        :keyword options: A dictionary of options for the token request. Unknown options will be ignored. Optional.
        :paramtype options: ~azure.core.credentials.TokenRequestOptions

        :rtype: ~azure.core.credentials.AccessTokenInfo
        :return: An AccessTokenInfo instance containing information about the token.
        :raises ~azure.identity.CredentialUnavailableError: the credential cannot retrieve user details from Visual
          Studio Code.
        """
        if self._unavailable_reason:
            error_message = (
                self._unavailable_reason + "\n"
                "Visit https://aka.ms/azsdk/python/identity/vscodecredential/troubleshoot"
                " to troubleshoot this issue."
            )
            raise CredentialUnavailableError(message=error_message)
        if within_dac.get():
            try:
                token = super().get_token_info(*scopes, options=options)
                return token
            except ClientAuthenticationError as ex:
                raise CredentialUnavailableError(message=ex.message) from ex
        return super().get_token_info(*scopes, options=options)

    def _acquire_token_silently(self, *scopes: str, **kwargs: Any) -> Optional[AccessTokenInfo]:
        self._client = cast(AadClient, self._client)
        return self._client.get_cached_access_token(scopes, **kwargs)

    def _request_token(self, *scopes: str, **kwargs: Any) -> AccessTokenInfo:
        refresh_token = self._get_refresh_token()
        self._client = cast(AadClient, self._client)
        return self._client.obtain_token_by_refresh_token(scopes, refresh_token, **kwargs)

    def _get_client(self, **kwargs: Any) -> AadClient:
        return AadClient(**kwargs)
