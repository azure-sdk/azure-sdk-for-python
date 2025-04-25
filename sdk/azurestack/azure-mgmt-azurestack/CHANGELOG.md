# Release History

## 2.0.0 (2025-04-25)

### Features Added

  - Client `AzureStackManagementClient` added operation group `deployment_license`
  - Added model `DeploymentLicenseRequest`
  - Added model `DeploymentLicenseResponse`
  - Model `CloudManifestFileOperations` added parameter `kwargs` in method `__init__`
  - Model `CustomerSubscriptionsOperations` added parameter `kwargs` in method `__init__`
  - Model `Operations` added parameter `kwargs` in method `__init__`
  - Model `ProductsOperations` added parameter `kwargs` in method `__init__`
  - Model `ProductsOperations` added method `list_products`
  - Model `RegistrationsOperations` added parameter `kwargs` in method `__init__`
  - Model `RegistrationsOperations` added method `list_by_subscription`
  - Added model `DeploymentLicenseOperations`
  - Method `CustomerSubscriptionsOperations.create` has a new overload `def create(self: None, resource_group: str, registration_name: str, customer_subscription_name: str, customer_creation_parameters: CustomerSubscription, content_type: str)`
  - Method `CustomerSubscriptionsOperations.create` has a new overload `def create(self: None, resource_group: str, registration_name: str, customer_subscription_name: str, customer_creation_parameters: IO[bytes], content_type: str)`
  - Method `ProductsOperations.get_product` has a new overload `def get_product(self: None, resource_group: str, registration_name: str, product_name: str, device_configuration: Optional[DeviceConfiguration], content_type: str)`
  - Method `ProductsOperations.get_product` has a new overload `def get_product(self: None, resource_group: str, registration_name: str, product_name: str, device_configuration: Optional[IO[bytes]], content_type: str)`
  - Method `ProductsOperations.get_products` has a new overload `def get_products(self: None, resource_group: str, registration_name: str, product_name: str, device_configuration: Optional[DeviceConfiguration], content_type: str)`
  - Method `ProductsOperations.get_products` has a new overload `def get_products(self: None, resource_group: str, registration_name: str, product_name: str, device_configuration: Optional[IO[bytes]], content_type: str)`
  - Method `ProductsOperations.upload_log` has a new overload `def upload_log(self: None, resource_group: str, registration_name: str, product_name: str, marketplace_product_log_update: Optional[MarketplaceProductLogUpdate], content_type: str)`
  - Method `ProductsOperations.upload_log` has a new overload `def upload_log(self: None, resource_group: str, registration_name: str, product_name: str, marketplace_product_log_update: Optional[IO[bytes]], content_type: str)`
  - Method `ProductsOperations.list_products` has a new overload `def list_products(self: None, resource_group: str, registration_name: str, product_name: str, device_configuration: Optional[DeviceConfiguration], content_type: str)`
  - Method `ProductsOperations.list_products` has a new overload `def list_products(self: None, resource_group: str, registration_name: str, product_name: str, device_configuration: Optional[IO[bytes]], content_type: str)`
  - Method `RegistrationsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group: str, registration_name: str, token: RegistrationParameter, content_type: str)`
  - Method `RegistrationsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group: str, registration_name: str, token: IO[bytes], content_type: str)`
  - Method `RegistrationsOperations.update` has a new overload `def update(self: None, resource_group: str, registration_name: str, token: RegistrationParameter, content_type: str)`
  - Method `RegistrationsOperations.update` has a new overload `def update(self: None, resource_group: str, registration_name: str, token: IO[bytes], content_type: str)`
  - Method `DeploymentLicenseOperations.create` has a new overload `def create(self: None, deployment_license_request: DeploymentLicenseRequest, content_type: str)`
  - Method `DeploymentLicenseOperations.create` has a new overload `def create(self: None, deployment_license_request: IO[bytes], content_type: str)`

### Breaking Changes

  - Deleted or renamed client operation group `AzureStackManagementClient.linked_subscriptions`
  - Model `CustomerSubscription` deleted or renamed its instance variable `system_data`
  - Deleted or renamed enum value `Location.GLOBAL_ENUM`
  - Model `Product` deleted or renamed its instance variable `system_data`
  - Model `Registration` deleted or renamed its instance variable `kind`
  - Model `Registration` deleted or renamed its instance variable `system_data`
  - Model `TrackedResource` deleted or renamed its instance variable `kind`
  - Model `TrackedResource` deleted or renamed its instance variable `system_data`
  - Deleted or renamed model `CreatedByType`
  - Deleted or renamed model `LinkedSubscription`
  - Deleted or renamed model `LinkedSubscriptionParameter`
  - Deleted or renamed model `LinkedSubscriptionsList`
  - Deleted or renamed model `SystemData`
  - Deleted or renamed model `LinkedSubscriptionsOperations`

## 2.0.0b1 (2022-11-17)

### Features Added

  - Added operation ProductsOperations.list_products
  - Added operation RegistrationsOperations.list_by_subscription
  - Added operation group DeploymentLicenseOperations

### Breaking Changes

  - Model CustomerSubscription no longer has parameter system_data
  - Model Product no longer has parameter system_data
  - Model Registration no longer has parameter kind
  - Model Registration no longer has parameter system_data
  - Model TrackedResource no longer has parameter kind
  - Model TrackedResource no longer has parameter system_data
  - Removed operation group LinkedSubscriptionsOperations

## 1.0.0 (2021-04-08)

**Features**

  - Model Registration has a new parameter system_data
  - Model Registration has a new parameter kind
  - Model TrackedResource has a new parameter system_data
  - Model TrackedResource has a new parameter kind
  - Model CustomerSubscription has a new parameter system_data
  - Model Product has a new parameter system_data
  - Added operation RegistrationsOperations.enable_remote_management
  - Added operation group LinkedSubscriptionsOperations

**Breaking changes**

  - Operation ProductsOperations.get_products has a new signature

## 1.0.0b1 (2020-12-03)

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

## 0.1.0 (2020-01-15)

  - Initial Release
