# Release History

## 1.1.0b3 (2025-04-17)

### Features Added

  - Model `AzureBareMetalStorageInstance` added property `identity`
  - Added model `AzureBareMetalInstanceListResult`
  - Added model `AzureBareMetalStorageInstanceBody`
  - Added model `AzureBareMetalStorageInstanceIdentity`
  - Added model `AzureBareMetalStorageInstanceListResult`
  - Added model `AzureResourceManagerArmResponseOperationStatus`
  - Added enum `ResourceIdentityType`
  - Model `AzureBareMetalInstancesOperations` added method `create`
  - Model `AzureBareMetalInstancesOperations` added method `delete`
  - Method `AzureBareMetalInstancesOperations.begin_restart` has a new overload `def begin_restart(self: None, resource_group_name: str, azure_bare_metal_instance_name: str, force_parameter: Optional[IO[bytes]], content_type: str)`
  - Method `AzureBareMetalInstancesOperations.update` has a new overload `def update(self: None, resource_group_name: str, azure_bare_metal_instance_name: str, tags_parameter: IO[bytes], content_type: str)`
  - Method `AzureBareMetalInstancesOperations.create` has a new overload `def create(self: None, resource_group_name: str, azure_bare_metal_instance_name: str, request_body_parameters: AzureBareMetalInstance, content_type: str)`
  - Method `AzureBareMetalInstancesOperations.create` has a new overload `def create(self: None, resource_group_name: str, azure_bare_metal_instance_name: str, request_body_parameters: IO[bytes], content_type: str)`
  - Method `AzureBareMetalStorageInstancesOperations.create` has a new overload `def create(self: None, resource_group_name: str, azure_bare_metal_storage_instance_name: str, request_body_parameters: IO[bytes], content_type: str)`
  - Method `AzureBareMetalStorageInstancesOperations.update` has a new overload `def update(self: None, resource_group_name: str, azure_bare_metal_storage_instance_name: str, azure_bare_metal_storage_instance_body_parameter: AzureBareMetalStorageInstanceBody, content_type: str)`
  - Method `AzureBareMetalStorageInstancesOperations.update` has a new overload `def update(self: None, resource_group_name: str, azure_bare_metal_storage_instance_name: str, azure_bare_metal_storage_instance_body_parameter: IO[bytes], content_type: str)`

### Breaking Changes

  - Method `AzureBareMetalStorageInstancesOperations.update` inserted a `positional_or_keyword` parameter `azure_bare_metal_storage_instance_body_parameter`
  - Method `AzureBareMetalStorageInstancesOperations.update` deleted or renamed its parameter `tags_parameter` of kind `positional_or_keyword`
  - Method `AzureBareMetalStorageInstancesOperations.update` re-ordered its parameters from `['self', 'resource_group_name', 'azure_bare_metal_storage_instance_name', 'tags_parameter', 'kwargs']` to `['self', 'resource_group_name', 'azure_bare_metal_storage_instance_name', 'azure_bare_metal_storage_instance_body_parameter', 'kwargs']`

## 1.1.0b2 (2023-10-23)

### Features Added

  - Added operation AzureBareMetalInstancesOperations.begin_restart
  - Added operation AzureBareMetalInstancesOperations.begin_shutdown
  - Added operation AzureBareMetalInstancesOperations.begin_start
  - Added operation group AzureBareMetalStorageInstancesOperations
  - Model Operation has a new parameter action_type
  - Model Operation has a new parameter origin
  - Model Resource has a new parameter system_data
  - Model TrackedResource has a new parameter system_data

## 1.1.0b1 (2022-11-09)

### Other Changes

  - Added generated samples in github repo
  - Drop support for python<3.7.0

## 1.0.0 (2021-10-14)

**Features**

  - Model AzureBareMetalInstance has a new parameter system_data
  - Added operation AzureBareMetalInstancesOperations.list_by_resource_group

**Breaking changes**

  - Model Display no longer has parameter origin
  - Removed operation AzureBareMetalInstancesOperations.list
  - Removed operation AzureBareMetalInstancesOperations.begin_shutdown
  - Removed operation AzureBareMetalInstancesOperations.begin_start
  - Removed operation AzureBareMetalInstancesOperations.begin_restart
  - Removed operation AzureBareMetalInstancesOperations.begin_delete

## 1.0.0b2 (2021-06-28)

* Fix dependencies

## 1.0.0b1 (2020-09-22)

* Initial Release
