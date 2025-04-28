# Release History

## 2.0.0 (2025-04-28)

### Features Added

  - Model `AutoScaleVCoreListResult` added property `next_link`
  - Model `CapacitySku` added property `capacity`
  - Model `DedicatedCapacity` added property `tenant_id`
  - Model `DedicatedCapacity` added property `friendly_name`
  - Model `DedicatedCapacityMutableProperties` added property `tenant_id`
  - Model `DedicatedCapacityMutableProperties` added property `friendly_name`
  - Model `DedicatedCapacityProperties` added property `tenant_id`
  - Model `DedicatedCapacityProperties` added property `friendly_name`
  - Model `DedicatedCapacityUpdateParameters` added property `tenant_id`
  - Model `DedicatedCapacityUpdateParameters` added property `friendly_name`
  - Model `Operation` added property `origin`
  - Model `Operation` added property `properties`
  - Model `OperationDisplay` added property `description`
  - Model `SkuDetailsForExistingResource` added property `resource_type`
  - Added enum `CreatedByType`
  - Added model `LogSpecification`
  - Added model `MetricSpecification`
  - Added model `MetricSpecificationDimensionsItem`
  - Added model `OperationProperties`
  - Added model `ServiceSpecification`
  - Added model `TrackedResource`
  - Model `AutoScaleVCoresOperations` added parameter `kwargs` in method `__init__`
  - Model `CapacitiesOperations` added parameter `kwargs` in method `__init__`
  - Model `Operations` added parameter `kwargs` in method `__init__`
  - Method `AutoScaleVCoresOperations.create` has a new overload `def create(self: None, resource_group_name: str, vcore_name: str, v_core_parameters: AutoScaleVCore, content_type: str)`
  - Method `AutoScaleVCoresOperations.create` has a new overload `def create(self: None, resource_group_name: str, vcore_name: str, v_core_parameters: IO[bytes], content_type: str)`
  - Method `AutoScaleVCoresOperations.update` has a new overload `def update(self: None, resource_group_name: str, vcore_name: str, v_core_update_parameters: AutoScaleVCoreUpdateParameters, content_type: str)`
  - Method `AutoScaleVCoresOperations.update` has a new overload `def update(self: None, resource_group_name: str, vcore_name: str, v_core_update_parameters: IO[bytes], content_type: str)`
  - Method `CapacitiesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, dedicated_capacity_name: str, capacity_parameters: DedicatedCapacity, content_type: str)`
  - Method `CapacitiesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, dedicated_capacity_name: str, capacity_parameters: IO[bytes], content_type: str)`
  - Method `CapacitiesOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, dedicated_capacity_name: str, capacity_update_parameters: DedicatedCapacityUpdateParameters, content_type: str)`
  - Method `CapacitiesOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, dedicated_capacity_name: str, capacity_update_parameters: IO[bytes], content_type: str)`
  - Method `CapacitiesOperations.check_name_availability` has a new overload `def check_name_availability(self: None, location: str, capacity_parameters: CheckCapacityNameAvailabilityParameters, content_type: str)`
  - Method `CapacitiesOperations.check_name_availability` has a new overload `def check_name_availability(self: None, location: str, capacity_parameters: IO[bytes], content_type: str)`

### Breaking Changes

  - Method `CapacitiesOperations.list` changed from `synchronous` to `asynchronous`
  - Method `CapacitiesOperations.list_by_resource_group` changed from `synchronous` to `asynchronous`
  - Model `Resource` deleted or renamed its instance variable `location`
  - Model `Resource` deleted or renamed its instance variable `tags`
  - Deleted or renamed model `IdentityType`

## 1.1.0b1 (2022-10-28)

### Features Added

  - Model CapacitySku has a new parameter capacity
  - Model DedicatedCapacity has a new parameter friendly_name
  - Model DedicatedCapacity has a new parameter tenant_id
  - Model DedicatedCapacityMutableProperties has a new parameter friendly_name
  - Model DedicatedCapacityMutableProperties has a new parameter tenant_id
  - Model DedicatedCapacityProperties has a new parameter friendly_name
  - Model DedicatedCapacityProperties has a new parameter tenant_id
  - Model DedicatedCapacityUpdateParameters has a new parameter friendly_name
  - Model DedicatedCapacityUpdateParameters has a new parameter tenant_id
  - Model Operation has a new parameter origin
  - Model Operation has a new parameter properties
  - Model OperationDisplay has a new parameter description
  - Model SkuDetailsForExistingResource has a new parameter resource_type

## 1.0.0 (2021-03-26)

**Features**

  - Model DedicatedCapacityProperties has a new parameter mode
  - Model DedicatedCapacityMutableProperties has a new parameter mode
  - Model DedicatedCapacityUpdateParameters has a new parameter mode
  - Model DedicatedCapacity has a new parameter system_data
  - Model DedicatedCapacity has a new parameter mode
  - Model Resource has a new parameter system_data
  - Added operation group AutoScaleVCoresOperations

**Breaking changes**

  - Model Resource no longer has parameter sku
  - Model ErrorResponse has a new signature

## 1.0.0b1 (2020-12-02)

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

## 0.1.0 (2020-01-19)

  - Initial Release
