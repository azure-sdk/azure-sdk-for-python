# Release History

## 3.0.0b1 (2025-04-22)

### Features Added

  - Model `CustomLocations` added property `operations`
  - Model `CustomLocations` added property `resource_sync_rules`
  - Model `ProxyResource` added property `system_data`
  - Model `Resource` added property `system_data`
  - Model `TrackedResource` added property `system_data`
  - Added enum `ActionType`
  - Added model `CustomLocationFindTargetResourceGroupProperties`
  - Added model `CustomLocationFindTargetResourceGroupResult`
  - Added model `EnabledResourceTypeListResult`
  - Added model `MatchExpressionsProperties`
  - Added model `Operation`
  - Added model `OperationDisplay`
  - Added model `OperationListResult`
  - Added enum `Origin`
  - Added model `PatchableResourceSyncRule`
  - Added model `ResourceSyncRule`
  - Added model `ResourceSyncRuleListResult`
  - Added model `ResourceSyncRulePropertiesSelector`
  - Model `CustomLocationsOperations` added method `find_target_resource_group`
  - Added model `Operations`
  - Added model `ResourceSyncRulesOperations`
  - Method `CustomLocationsOperations.find_target_resource_group` has a new overload `def find_target_resource_group(self: None, resource_group_name: str, resource_name: str, parameters: CustomLocationFindTargetResourceGroupProperties, content_type: str)`
  - Method `CustomLocationsOperations.find_target_resource_group` has a new overload `def find_target_resource_group(self: None, resource_group_name: str, resource_name: str, parameters: IO[bytes], content_type: str)`
  - Method `ResourceSyncRulesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, resource_name: str, child_resource_name: str, parameters: ResourceSyncRule, content_type: str)`
  - Method `ResourceSyncRulesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, resource_name: str, child_resource_name: str, parameters: IO[bytes], content_type: str)`

### Breaking Changes

  - Deleted or renamed model `CustomLocationOperation`
  - Deleted or renamed model `CustomLocationOperationsList`
  - Deleted or renamed method `CustomLocationsOperations.list_operations`

## 2.0.0 (2024-10-30)

### Breaking Changes

  - This package now only targets the latest Api-Version available on Azure and removes APIs of other Api-Version. After this change, the package can have much smaller size. If your application requires a specific and non-latest Api-Version, it's recommended to pin this package to the previous released version; If your application always only use latest Api-Version, please ignore this change.

## 1.2.0b1 (2023-02-14)

### Other Changes

  - Added generated samples in github repo
  - Drop support for python<3.7.0

## 1.1.0 (2022-07-12)

**Features**

  - Added operation CustomLocationsOperations.find_target_resource_group
  - Added operation group ResourceSyncRulesOperations

## 1.0.0 (2021-09-22)

**Features**
  - Adding a new API Version 2021-08-15
  - Adding support for Managed Identity [SystemAssigned]
  - Model PatchableCustomLocations has a new parameter identity
  - Model CustomLocation has a new parameter identity

**Breaking changes**

  - Operation CustomLocationsOperations.update has a new signature

## 1.0.0b2 (2021-05-06)

* Remove v2020_07_15_privatepreview

## 1.0.0b1 (2021-03-25)

* Initial Release
