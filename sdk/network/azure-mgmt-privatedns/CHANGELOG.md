# Release History

## 2.0.0 (2025-04-29)

### Features Added

  - Model `PrivateZone` added property `system_data`
  - Model `ProxyResource` added property `system_data`
  - Model `RecordSet` added property `system_data`
  - Model `Resource` added property `system_data`
  - Model `TrackedResource` added property `system_data`
  - Model `VirtualNetworkLink` added property `system_data`
  - Added enum `CreatedByType`
  - Added model `ErrorAdditionalInfo`
  - Added model `ErrorDetail`
  - Added model `ErrorResponse`
  - Added model `SystemData`

### Breaking Changes

  - Method `PrivateZone.__init__` removed default value `None` from its parameter `location`
  - Method `PrivateZoneListResult.__init__` removed default value `None` from its parameter `value`
  - Method `RecordSetListResult.__init__` removed default value `None` from its parameter `value`
  - Method `TrackedResource.__init__` removed default value `None` from its parameter `location`
  - Method `VirtualNetworkLink.__init__` removed default value `None` from its parameter `location`
  - Method `VirtualNetworkLinkListResult.__init__` removed default value `None` from its parameter `value`
  - Deleted or renamed model `CloudErrorBody`
  - Method `RecordSetsOperations.update` re-ordered its parameters from `['self', 'resource_group_name', 'private_zone_name', 'record_type', 'relative_record_set_name', 'parameters', 'if_match', 'kwargs']` to `['self', 'resource_group_name', 'private_zone_name', 'relative_record_set_name', 'record_type', 'parameters', 'if_match', 'kwargs']`
  - Method `RecordSetsOperations.get` re-ordered its parameters from `['self', 'resource_group_name', 'private_zone_name', 'record_type', 'relative_record_set_name', 'kwargs']` to `['self', 'resource_group_name', 'private_zone_name', 'relative_record_set_name', 'record_type', 'kwargs']`
  - Method `RecordSetsOperations.create_or_update` re-ordered its parameters from `['self', 'resource_group_name', 'private_zone_name', 'record_type', 'relative_record_set_name', 'parameters', 'if_match', 'if_none_match', 'kwargs']` to `['self', 'resource_group_name', 'private_zone_name', 'relative_record_set_name', 'record_type', 'parameters', 'if_match', 'if_none_match', 'kwargs']`
  - Method `RecordSetsOperations.delete` re-ordered its parameters from `['self', 'resource_group_name', 'private_zone_name', 'record_type', 'relative_record_set_name', 'if_match', 'kwargs']` to `['self', 'resource_group_name', 'private_zone_name', 'relative_record_set_name', 'record_type', 'if_match', 'kwargs']`

## 1.2.0 (2024-09-23)

### Features Added

  - Model `VirtualNetworkLink` added property `resolution_policy`
  - Added enum `ResolutionPolicy`

## 1.1.0 (2023-05-20)

### Features Added

  - Model PrivateZone has a new parameter internal_id

## 1.1.0b1 (2022-10-28)

### Features Added

  - Model PrivateZone has a new parameter internal_id

## 1.0.0 (2021-03-25)

- GA release

## 1.0.0b1 (2021-02-09)

This is beta preview version.
For detailed changelog please refer to equivalent stable version 10.2.0 (https://pypi.org/project/azure-mgmt-network/10.2.0/)

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


## 0.1.0 (2019-02-26)

  - Initial Release
