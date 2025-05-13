# Release History

## 1.2.0b3 (2025-05-13)

### Features Added

  - Model `GroupIdInformation` added property `system_data`
  - Model `IotHubDefinitionDescription` added property `authentication_type`
  - Model `IotHubDefinitionDescription` added property `selected_user_assigned_identity_resource_id`
  - Model `Resource` added property `system_data`
  - Added model `ErrorAdditionalInfo`
  - Added model `ErrorDetail`
  - Added model `ErrorResponse`
  - Added enum `IotHubAuthenticationType`
  - Added model `ProxyResource`
  - Added model `TrackedResource`
  - Method `DpsCertificateOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, provisioning_service_name: str, certificate_name: str, certificate_description: IO[bytes], if_match: Optional[str], content_type: str)`
  - Method `DpsCertificateOperations.verify_certificate` has a new overload `def verify_certificate(self: None, resource_group_name: str, provisioning_service_name: str, certificate_name: str, if_match: str, request: IO[bytes], certificate_name1: Optional[str], certificate_raw_bytes: Optional[bytes], certificate_is_verified: Optional[bool], certificate_purpose: Optional[Union[str, CertificatePurpose]], certificate_created: Optional[datetime], certificate_last_updated: Optional[datetime], certificate_has_private_key: Optional[bool], certificate_nonce: Optional[str], content_type: str)`
  - Method `IotDpsResourceOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, provisioning_service_name: str, iot_dps_description: IO[bytes], content_type: str)`
  - Method `IotDpsResourceOperations.begin_create_or_update_private_endpoint_connection` has a new overload `def begin_create_or_update_private_endpoint_connection(self: None, resource_group_name: str, provisioning_service_name: str, private_endpoint_connection_name: str, private_endpoint_connection: PrivateEndpointConnection, content_type: str)`
  - Method `IotDpsResourceOperations.begin_create_or_update_private_endpoint_connection` has a new overload `def begin_create_or_update_private_endpoint_connection(self: None, resource_group_name: str, provisioning_service_name: str, private_endpoint_connection_name: str, private_endpoint_connection: IO[bytes], content_type: str)`
  - Method `IotDpsResourceOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, provisioning_service_name: str, provisioning_service_tags: IO[bytes], content_type: str)`
  - Method `IotDpsResourceOperations.check_provisioning_service_name_availability` has a new overload `def check_provisioning_service_name_availability(self: None, arguments: IO[bytes], content_type: str)`

### Breaking Changes

  - Method `IotDpsSkuDefinitionListResult.__init__` removed default value `None` from its parameter `value`
  - Model `ProvisioningServiceDescription` deleted or renamed its instance variable `resourcegroup`
  - Model `ProvisioningServiceDescription` deleted or renamed its instance variable `subscriptionid`
  - Method `ProvisioningServiceDescriptionListResult.__init__` removed default value `None` from its parameter `value`
  - Model `Resource` deleted or renamed its instance variable `location`
  - Model `Resource` deleted or renamed its instance variable `resourcegroup`
  - Model `Resource` deleted or renamed its instance variable `subscriptionid`
  - Model `Resource` deleted or renamed its instance variable `tags`
  - Method `SharedAccessSignatureAuthorizationRuleListResult.__init__` removed default value `None` from its parameter `value`
  - Deleted or renamed model `CertificateBodyDescription`
  - Method `IotDpsResourceOperations.begin_create_or_update_private_endpoint_connection` inserted a `positional_or_keyword` parameter `provisioning_service_name`
  - Method `IotDpsResourceOperations.begin_create_or_update_private_endpoint_connection` deleted or renamed its parameter `resource_name` of kind `positional_or_keyword`
  - Method `IotDpsResourceOperations.begin_delete_private_endpoint_connection` inserted a `positional_or_keyword` parameter `provisioning_service_name`
  - Method `IotDpsResourceOperations.begin_delete_private_endpoint_connection` deleted or renamed its parameter `resource_name` of kind `positional_or_keyword`
  - Method `IotDpsResourceOperations.get_private_endpoint_connection` inserted a `positional_or_keyword` parameter `provisioning_service_name`
  - Method `IotDpsResourceOperations.get_private_endpoint_connection` deleted or renamed its parameter `resource_name` of kind `positional_or_keyword`
  - Method `IotDpsResourceOperations.get_private_link_resources` inserted a `positional_or_keyword` parameter `provisioning_service_name`
  - Method `IotDpsResourceOperations.get_private_link_resources` deleted or renamed its parameter `resource_name` of kind `positional_or_keyword`
  - Method `IotDpsResourceOperations.list_private_endpoint_connections` inserted a `positional_or_keyword` parameter `provisioning_service_name`
  - Method `IotDpsResourceOperations.list_private_endpoint_connections` deleted or renamed its parameter `resource_name` of kind `positional_or_keyword`
  - Method `IotDpsResourceOperations.list_private_link_resources` inserted a `positional_or_keyword` parameter `provisioning_service_name`
  - Method `IotDpsResourceOperations.list_private_link_resources` deleted or renamed its parameter `resource_name` of kind `positional_or_keyword`
  - Method `IotDpsResourceOperations.list_valid_skus` re-ordered its parameters from `['self', 'provisioning_service_name', 'resource_group_name', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'kwargs']`
  - Method `IotDpsResourceOperations.begin_create_or_update_private_endpoint_connection` re-ordered its parameters from `['self', 'resource_group_name', 'resource_name', 'private_endpoint_connection_name', 'private_endpoint_connection', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'private_endpoint_connection_name', 'private_endpoint_connection', 'kwargs']`
  - Method `IotDpsResourceOperations.list_keys` re-ordered its parameters from `['self', 'provisioning_service_name', 'resource_group_name', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'kwargs']`
  - Method `IotDpsResourceOperations.begin_delete` re-ordered its parameters from `['self', 'provisioning_service_name', 'resource_group_name', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'kwargs']`
  - Method `IotDpsResourceOperations.list_keys_for_key_name` re-ordered its parameters from `['self', 'provisioning_service_name', 'key_name', 'resource_group_name', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'key_name', 'kwargs']`
  - Method `IotDpsResourceOperations.list_private_link_resources` re-ordered its parameters from `['self', 'resource_group_name', 'resource_name', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'kwargs']`
  - Method `IotDpsResourceOperations.list_private_endpoint_connections` re-ordered its parameters from `['self', 'resource_group_name', 'resource_name', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'kwargs']`
  - Method `IotDpsResourceOperations.get_private_endpoint_connection` re-ordered its parameters from `['self', 'resource_group_name', 'resource_name', 'private_endpoint_connection_name', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'private_endpoint_connection_name', 'kwargs']`
  - Method `IotDpsResourceOperations.get_operation_result` re-ordered its parameters from `['self', 'operation_id', 'resource_group_name', 'provisioning_service_name', 'asyncinfo', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'operation_id', 'asyncinfo', 'kwargs']`
  - Method `IotDpsResourceOperations.get` re-ordered its parameters from `['self', 'provisioning_service_name', 'resource_group_name', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'kwargs']`
  - Method `IotDpsResourceOperations.get_private_link_resources` re-ordered its parameters from `['self', 'resource_group_name', 'resource_name', 'group_id', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'group_id', 'kwargs']`
  - Method `IotDpsResourceOperations.begin_delete_private_endpoint_connection` re-ordered its parameters from `['self', 'resource_group_name', 'resource_name', 'private_endpoint_connection_name', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'private_endpoint_connection_name', 'kwargs']`
  - Method `DpsCertificateOperations.generate_verification_code` re-ordered its parameters from `['self', 'certificate_name', 'if_match', 'resource_group_name', 'provisioning_service_name', 'certificate_name1', 'certificate_raw_bytes', 'certificate_is_verified', 'certificate_purpose', 'certificate_created', 'certificate_last_updated', 'certificate_has_private_key', 'certificate_nonce', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'certificate_name', 'if_match', 'certificate_name1', 'certificate_raw_bytes', 'certificate_is_verified', 'certificate_purpose', 'certificate_created', 'certificate_last_updated', 'certificate_has_private_key', 'certificate_nonce', 'kwargs']`
  - Method `DpsCertificateOperations.verify_certificate` re-ordered its parameters from `['self', 'certificate_name', 'if_match', 'resource_group_name', 'provisioning_service_name', 'request', 'certificate_name1', 'certificate_raw_bytes', 'certificate_is_verified', 'certificate_purpose', 'certificate_created', 'certificate_last_updated', 'certificate_has_private_key', 'certificate_nonce', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'certificate_name', 'if_match', 'request', 'certificate_name1', 'certificate_raw_bytes', 'certificate_is_verified', 'certificate_purpose', 'certificate_created', 'certificate_last_updated', 'certificate_has_private_key', 'certificate_nonce', 'kwargs']`
  - Method `DpsCertificateOperations.delete` re-ordered its parameters from `['self', 'resource_group_name', 'if_match', 'provisioning_service_name', 'certificate_name', 'certificate_name1', 'certificate_raw_bytes', 'certificate_is_verified', 'certificate_purpose', 'certificate_created', 'certificate_last_updated', 'certificate_has_private_key', 'certificate_nonce', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'certificate_name', 'if_match', 'certificate_name1', 'certificate_raw_bytes', 'certificate_is_verified', 'certificate_purpose', 'certificate_created', 'certificate_last_updated', 'certificate_has_private_key', 'certificate_nonce', 'kwargs']`
  - Method `DpsCertificateOperations.get` re-ordered its parameters from `['self', 'certificate_name', 'resource_group_name', 'provisioning_service_name', 'if_match', 'kwargs']` to `['self', 'resource_group_name', 'provisioning_service_name', 'certificate_name', 'if_match', 'kwargs']`

## 1.2.0b2 (2023-06-16)

### Features Added

  - Model IotDpsPropertiesDescription has a new parameter portal_operations_host_name
  - Model ProvisioningServiceDescription has a new parameter identity
  - Model ProvisioningServiceDescription has a new parameter resourcegroup
  - Model ProvisioningServiceDescription has a new parameter subscriptionid
  - Model Resource has a new parameter resourcegroup
  - Model Resource has a new parameter subscriptionid

## 1.2.0b1 (2022-11-15)

### Features Added

  - Added model ErrorMessage

## 1.1.0 (2022-02-07)

**Features**

  - Model CertificateResponse has a new parameter system_data
  - Model IotDpsPropertiesDescription has a new parameter enable_data_residency
  - Model PrivateEndpointConnection has a new parameter system_data
  - Model ProvisioningServiceDescription has a new parameter system_data

## 1.0.0 (2021-08-18)

**Features**

  - Model CertificateBodyDescription has a new parameter is_verified

## 1.0.0b1 (2021-05-14)

This is beta preview version.

This version uses a next-generation code generator that introduces important breaking changes, but also important new features (like unified authentication and async programming).

**General breaking changes**

- Credential system has been completly revamped:

  - `azure.common.credentials` or `msrestazure.azure_active_directory` instances are no longer supported, use the `azure-identity` classes instead: https://pypi.org/project/azure-identity/
  - `credentials` parameter has been renamed `credential`

- The `config` attribute no longer exists on a client, configuration should be passed as kwarg. Example: `MyClient(credential, subscription_id, enable_logging=True)`. For a complete set of
  supported options, see the [parameters accept in init documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)
- You can't import a `version` module anymore, use `__version__` instead
- Operations that used to return a `msrest.polling.LROPoller` now returns a `azure.core.polling.LROPoller` and are prefixed with `begin_`.
- Exceptions tree have been simplified and most exceptions are now `azure.core.exceptions.HttpResponseError` (`CloudError` has been removed).
- Most of the operation kwarg have changed. Some of the most noticeable:

  - `raw` has been removed. Equivalent feature can be found using `cls`, a callback that will give access to internal HTTP response for advanced user
  - For a complete set of
  supported options, see the [parameters accept in Request documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)

**General new features**

- Type annotations support using `typing`. SDKs are mypy ready.
- This client has now stable and official support for async. Check the `aio` namespace of your package to find the async client.
- This client now support natively tracing library like OpenCensus or OpenTelemetry. See this [tracing quickstart](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-tracing-opentelemetry) for an overview.


## 0.2.0 (2018-04-17)

**General Breaking changes**

This version uses a next-generation code generator that *might*
introduce breaking changes.

  - Model signatures now use only keyword-argument syntax. All
    positional arguments must be re-written as keyword-arguments. To
    keep auto-completion in most cases, models are now generated for
    Python 2 and Python 3. Python 3 uses the "*" syntax for
    keyword-only arguments.
  - Enum types now use the "str" mixin (class AzureEnum(str, Enum)) to
    improve the behavior when unrecognized enum values are encountered.
    While this is not a breaking change, the distinctions are important,
    and are documented here:
    <https://docs.python.org/3/library/enum.html#others> At a glance:
      - "is" should not be used at all.
      - "format" will return the string value, where "%s" string
        formatting will return `NameOfEnum.stringvalue`. Format syntax
        should be prefered.
  - New Long Running Operation:
      - Return type changes from
        `msrestazure.azure_operation.AzureOperationPoller` to
        `msrest.polling.LROPoller`. External API is the same.
      - Return type is now **always** a `msrest.polling.LROPoller`,
        regardless of the optional parameters used.
      - The behavior has changed when using `raw=True`. Instead of
        returning the initial call result as `ClientRawResponse`,
        without polling, now this returns an LROPoller. After polling,
        the final resource will be returned as a `ClientRawResponse`.
      - New `polling` parameter. The default behavior is
        `Polling=True` which will poll using ARM algorithm. When
        `Polling=False`, the response of the initial call will be
        returned without polling.
      - `polling` parameter accepts instances of subclasses of
        `msrest.polling.PollingMethod`.
      - `add_done_callback` will no longer raise if called after
        polling is finished, but will instead execute the callback right
        away.

**Bugfixes**

  - Compatibility of the sdist with wheel 0.31.0

**Features**

  - New ApiVersion 2018-01-22

## 0.1.0 (2018-01-04)

  - Initial Release
