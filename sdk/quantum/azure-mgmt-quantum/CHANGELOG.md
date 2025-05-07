# Release History

## 1.0.0b6 (2025-05-07)

### Features Added

  - Model `Operation` added property `origin`
  - Model `Operation` added property `action_type`
  - Model `WorkspaceResourceProperties` added property `managed_on_behalf_of_configuration`
  - Model `WorkspaceResourceProperties` added property `managed_storage_account`
  - Added enum `ActionType`
  - Added model `ApiKeys`
  - Added enum `CheckNameAvailabilityReason`
  - Added model `CheckNameAvailabilityRequest`
  - Added model `CheckNameAvailabilityResponse`
  - Added model `ManagedOnBehalfOfConfiguration`
  - Added model `ManagedServiceIdentity`
  - Added enum `ManagedServiceIdentityType`
  - Added model `MoboBrokerResource`
  - Added model `OperationListResult`
  - Added enum `Origin`
  - Added enum `ProviderStatus`
  - Added model `QuantumWorkspaceListResult`
  - Added model `QuantumWorkspaceTagsUpdate`
  - Added model `UserAssignedIdentity`
  - Added enum `WorkspaceProvisioningStatus`
  - Model `WorkspacesOperations` added method `check_name_availability`
  - Model `WorkspacesOperations` added method `list_keys`
  - Model `WorkspacesOperations` added method `regenerate_keys`
  - Method `WorkspacesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, workspace_name: str, resource: QuantumWorkspace, content_type: str)`
  - Method `WorkspacesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, workspace_name: str, resource: IO[bytes], content_type: str)`
  - Method `WorkspacesOperations.update_tags` has a new overload `def update_tags(self: None, resource_group_name: str, workspace_name: str, properties: QuantumWorkspaceTagsUpdate, content_type: str)`
  - Method `WorkspacesOperations.update_tags` has a new overload `def update_tags(self: None, resource_group_name: str, workspace_name: str, properties: IO[bytes], content_type: str)`
  - Method `WorkspacesOperations.check_name_availability` has a new overload `def check_name_availability(self: None, location: str, body: CheckNameAvailabilityRequest, content_type: str)`
  - Method `WorkspacesOperations.check_name_availability` has a new overload `def check_name_availability(self: None, location: str, body: IO[bytes], content_type: str)`
  - Method `WorkspacesOperations.regenerate_keys` has a new overload `def regenerate_keys(self: None, resource_group_name: str, workspace_name: str, body: ApiKeys, content_type: str)`
  - Method `WorkspacesOperations.regenerate_keys` has a new overload `def regenerate_keys(self: None, resource_group_name: str, workspace_name: str, body: IO[bytes], content_type: str)`

### Breaking Changes

  - Deleted or renamed client operation group `AzureQuantumMgmtClient.workspace`
  - Method `OfferingsListResult.__init__` removed default value `None` from its parameter `value`
  - Deleted or renamed model `APIKeys`
  - Deleted or renamed model `CheckNameAvailabilityParameters`
  - Deleted or renamed model `CheckNameAvailabilityResult`
  - Deleted or renamed model `OperationsList`
  - Deleted or renamed model `ProvisioningStatus`
  - Deleted or renamed model `QuantumWorkspaceIdentity`
  - Deleted or renamed model `ResourceIdentityType`
  - Deleted or renamed model `Status`
  - Deleted or renamed model `TagsObject`
  - Method `WorkspacesOperations.begin_create_or_update` inserted a `positional_or_keyword` parameter `resource`
  - Method `WorkspacesOperations.begin_create_or_update` deleted or renamed its parameter `quantum_workspace` of kind `positional_or_keyword`
  - Method `WorkspacesOperations.update_tags` inserted a `positional_or_keyword` parameter `properties`
  - Method `WorkspacesOperations.update_tags` deleted or renamed its parameter `workspace_tags` of kind `positional_or_keyword`
  - Deleted or renamed model `WorkspaceOperations`
  - Method `WorkspacesOperations.begin_create_or_update` re-ordered its parameters from `['self', 'resource_group_name', 'workspace_name', 'quantum_workspace', 'kwargs']` to `['self', 'resource_group_name', 'workspace_name', 'resource', 'kwargs']`
  - Method `WorkspacesOperations.update_tags` re-ordered its parameters from `['self', 'resource_group_name', 'workspace_name', 'workspace_tags', 'kwargs']` to `['self', 'resource_group_name', 'workspace_name', 'properties', 'kwargs']`

## 1.0.0b5 (2024-03-18)

### Features Added

  - Added operation WorkspaceOperations.list_keys
  - Added operation WorkspaceOperations.regenerate_keys
  - Model QuantumWorkspace has a new parameter properties
  - Model Resource has a new parameter system_data
  - Model TrackedResource has a new parameter system_data

### Breaking Changes

  - Client name is changed from `AzureQuantumManagementClient` to `AzureQuantumMgmtClient`
  - Model QuantumWorkspace no longer has parameter endpoint_uri
  - Model QuantumWorkspace no longer has parameter providers
  - Model QuantumWorkspace no longer has parameter provisioning_state
  - Model QuantumWorkspace no longer has parameter storage_account
  - Model QuantumWorkspace no longer has parameter usable

## 1.0.0b4 (2023-07-21)

### Other Changes

  - Regular release

## 1.0.0b3 (2022-11-07)

### Features Added

  - Added operation group WorkspaceOperations
  - Model QuantumWorkspace has a new parameter system_data
  - Model SkuDescription has a new parameter auto_add
  - Model SkuDescription has a new parameter restricted_access_uri
  - Model SkuDescription has a new parameter version

## 1.0.0b2 (2021-08-04)

**Features**

 - Model SkuDescription has a new parameter version
 - Model SkuDescription has a new parameter restricted_access_uri
 - Model QuantumWorkspace has a new parameter system_data
 - Added operation group WorkspaceOperations

## 1.0.0b1 (2021-01-28)

* Initial Release
