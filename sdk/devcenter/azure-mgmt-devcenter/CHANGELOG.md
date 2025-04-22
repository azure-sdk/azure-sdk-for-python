# Release History

## 1.2.0b1 (2025-04-22)

### Features Added

  - Client `DevCenterMgmtClient` added operation group `encryption_sets`
  - Client `DevCenterMgmtClient` added operation group `project_policies`
  - Client `DevCenterMgmtClient` added operation group `customization_tasks`
  - Client `DevCenterMgmtClient` added operation group `dev_center_catalog_image_definitions`
  - Client `DevCenterMgmtClient` added operation group `dev_center_catalog_image_definition_builds`
  - Client `DevCenterMgmtClient` added operation group `dev_center_catalog_image_definition_build`
  - Client `DevCenterMgmtClient` added operation group `project_catalog_image_definitions`
  - Client `DevCenterMgmtClient` added operation group `project_catalog_image_definition_builds`
  - Client `DevCenterMgmtClient` added operation group `project_catalog_image_definition_build`
  - Enum `CatalogItemType` added member `IMAGE_DEFINITION`
  - Model `DevCenter` added property `network_settings`
  - Model `DevCenter` added property `dev_box_provisioning_settings`
  - Model `DevCenterProperties` added property `network_settings`
  - Model `DevCenterProperties` added property `dev_box_provisioning_settings`
  - Model `DevCenterUpdate` added property `network_settings`
  - Model `DevCenterUpdate` added property `dev_box_provisioning_settings`
  - Model `DevCenterUpdateProperties` added property `network_settings`
  - Model `DevCenterUpdateProperties` added property `dev_box_provisioning_settings`
  - Enum `DomainJoinType` added member `NONE`
  - Enum `HealthCheckStatus` added member `INFORMATIONAL`
  - Model `Pool` added property `dev_box_definition_type`
  - Model `Pool` added property `dev_box_definition`
  - Model `Pool` added property `stop_on_no_connect`
  - Model `Pool` added property `active_hours_configuration`
  - Model `Pool` added property `dev_box_tunnel_enable_status`
  - Model `PoolProperties` added property `dev_box_definition_type`
  - Model `PoolProperties` added property `dev_box_definition`
  - Model `PoolProperties` added property `stop_on_no_connect`
  - Model `PoolProperties` added property `active_hours_configuration`
  - Model `PoolProperties` added property `dev_box_tunnel_enable_status`
  - Model `PoolUpdate` added property `dev_box_definition_type`
  - Model `PoolUpdate` added property `dev_box_definition`
  - Model `PoolUpdate` added property `stop_on_no_connect`
  - Model `PoolUpdate` added property `active_hours_configuration`
  - Model `PoolUpdate` added property `dev_box_tunnel_enable_status`
  - Model `PoolUpdateProperties` added property `dev_box_definition_type`
  - Model `PoolUpdateProperties` added property `dev_box_definition`
  - Model `PoolUpdateProperties` added property `stop_on_no_connect`
  - Model `PoolUpdateProperties` added property `active_hours_configuration`
  - Model `PoolUpdateProperties` added property `dev_box_tunnel_enable_status`
  - Model `Project` added property `customization_settings`
  - Model `Project` added property `dev_box_auto_delete_settings`
  - Model `Project` added property `azure_ai_services_settings`
  - Model `Project` added property `serverless_gpu_sessions_settings`
  - Model `Project` added property `workspace_storage_settings`
  - Model `ProjectProperties` added property `customization_settings`
  - Model `ProjectProperties` added property `dev_box_auto_delete_settings`
  - Model `ProjectProperties` added property `azure_ai_services_settings`
  - Model `ProjectProperties` added property `serverless_gpu_sessions_settings`
  - Model `ProjectProperties` added property `workspace_storage_settings`
  - Model `ProjectUpdate` added property `customization_settings`
  - Model `ProjectUpdate` added property `dev_box_auto_delete_settings`
  - Model `ProjectUpdate` added property `azure_ai_services_settings`
  - Model `ProjectUpdate` added property `serverless_gpu_sessions_settings`
  - Model `ProjectUpdate` added property `workspace_storage_settings`
  - Model `ProjectUpdateProperties` added property `customization_settings`
  - Model `ProjectUpdateProperties` added property `dev_box_auto_delete_settings`
  - Model `ProjectUpdateProperties` added property `azure_ai_services_settings`
  - Model `ProjectUpdateProperties` added property `serverless_gpu_sessions_settings`
  - Model `ProjectUpdateProperties` added property `workspace_storage_settings`
  - Added model `ActiveHoursConfiguration`
  - Added enum `AutoImageBuildStatus`
  - Added enum `AutoStartEnableStatus`
  - Added enum `AzureAiServicesMode`
  - Added model `AzureAiServicesSettings`
  - Added model `CustomizationTask`
  - Added model `CustomizationTaskInput`
  - Added enum `CustomizationTaskInputType`
  - Added model `CustomizationTaskInstance`
  - Added model `CustomizationTaskListResult`
  - Added model `DefinitionParametersItem`
  - Added model `DevBoxAutoDeleteSettings`
  - Added enum `DevBoxDeleteMode`
  - Added model `DevBoxProvisioningSettings`
  - Added enum `DevBoxTunnelEnableStatus`
  - Added model `DevCenterEncryptionSet`
  - Added model `DevCenterEncryptionSetProperties`
  - Added model `DevCenterEncryptionSetUpdateProperties`
  - Added model `DevCenterNetworkSettings`
  - Added enum `DevCenterResourceType`
  - Added enum `DevboxDisksEncryptionEnableStatus`
  - Added model `EncryptionSetListResult`
  - Added model `EncryptionSetUpdate`
  - Added model `ImageCreationErrorDetails`
  - Added model `ImageDefinition`
  - Added model `ImageDefinitionBuild`
  - Added model `ImageDefinitionBuildDetails`
  - Added model `ImageDefinitionBuildListResult`
  - Added enum `ImageDefinitionBuildStatus`
  - Added model `ImageDefinitionBuildTask`
  - Added model `ImageDefinitionBuildTaskGroup`
  - Added model `ImageDefinitionBuildTaskParametersItem`
  - Added model `ImageDefinitionListResult`
  - Added model `ImageDefinitionReference`
  - Added model `InheritedSettingsForProject`
  - Added enum `InstallAzureMonitorAgentEnableStatus`
  - Added enum `KeepAwakeEnableStatus`
  - Added model `LatestImageBuild`
  - Added enum `MicrosoftHostedNetworkEnableStatus`
  - Added enum `PolicyAction`
  - Added model `PoolDevBoxDefinition`
  - Added enum `PoolDevBoxDefinitionType`
  - Added enum `ProjectCustomizationIdentityType`
  - Added model `ProjectCustomizationManagedIdentity`
  - Added model `ProjectCustomizationSettings`
  - Added model `ProjectNetworkSettings`
  - Added model `ProjectPolicy`
  - Added model `ProjectPolicyListResult`
  - Added model `ProjectPolicyProperties`
  - Added model `ProjectPolicyUpdate`
  - Added model `ProjectPolicyUpdateProperties`
  - Added model `ResourcePolicy`
  - Added enum `ServerlessGpuSessionsMode`
  - Added model `ServerlessGpuSessionsSettings`
  - Added model `StopOnNoConnectConfiguration`
  - Added enum `StopOnNoConnectEnableStatus`
  - Added enum `UserCustomizationsEnableStatus`
  - Added enum `WorkspaceStorageMode`
  - Added model `WorkspaceStorageSettings`
  - Model `ImageVersionsOperations` added method `get_by_project`
  - Model `ImageVersionsOperations` added method `list_by_project`
  - Model `ImagesOperations` added method `get_by_project`
  - Model `ImagesOperations` added method `list_by_project`
  - Model `ProjectsOperations` added method `get_inherited_settings`
  - Model `SkusOperations` added method `list_by_project`
  - Added model `CustomizationTasksOperations`
  - Added model `DevCenterCatalogImageDefinitionBuildOperations`
  - Added model `DevCenterCatalogImageDefinitionBuildsOperations`
  - Added model `DevCenterCatalogImageDefinitionsOperations`
  - Added model `EncryptionSetsOperations`
  - Added model `ProjectCatalogImageDefinitionBuildOperations`
  - Added model `ProjectCatalogImageDefinitionBuildsOperations`
  - Added model `ProjectCatalogImageDefinitionsOperations`
  - Added model `ProjectPoliciesOperations`
  - Method `EncryptionSetsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, dev_center_name: str, encryption_set_name: str, body: DevCenterEncryptionSet, content_type: str)`
  - Method `EncryptionSetsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, dev_center_name: str, encryption_set_name: str, body: IO[bytes], content_type: str)`
  - Method `EncryptionSetsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, dev_center_name: str, encryption_set_name: str, body: EncryptionSetUpdate, content_type: str)`
  - Method `EncryptionSetsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, dev_center_name: str, encryption_set_name: str, body: IO[bytes], content_type: str)`
  - Method `ProjectPoliciesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, dev_center_name: str, project_policy_name: str, body: ProjectPolicy, content_type: str)`
  - Method `ProjectPoliciesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, dev_center_name: str, project_policy_name: str, body: IO[bytes], content_type: str)`
  - Method `ProjectPoliciesOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, dev_center_name: str, project_policy_name: str, body: ProjectPolicyUpdate, content_type: str)`
  - Method `ProjectPoliciesOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, dev_center_name: str, project_policy_name: str, body: IO[bytes], content_type: str)`

## 1.1.0 (2024-04-22)

### Features Added

  - Added operation CatalogsOperations.begin_connect
  - Added operation CatalogsOperations.get_sync_error_details
  - Added operation group CheckScopedNameAvailabilityOperations
  - Added operation group EnvironmentDefinitionsOperations
  - Added operation group ProjectCatalogEnvironmentDefinitionsOperations
  - Added operation group ProjectCatalogsOperations
  - Model AllowedEnvironmentType has a new parameter display_name
  - Model Catalog has a new parameter connection_state
  - Model Catalog has a new parameter last_connection_time
  - Model Catalog has a new parameter last_sync_stats
  - Model Catalog has a new parameter sync_type
  - Model Catalog has a new parameter tags
  - Model CatalogProperties has a new parameter connection_state
  - Model CatalogProperties has a new parameter last_connection_time
  - Model CatalogProperties has a new parameter last_sync_stats
  - Model CatalogProperties has a new parameter sync_type
  - Model CatalogProperties has a new parameter tags
  - Model CatalogUpdate has a new parameter sync_type
  - Model CatalogUpdateProperties has a new parameter sync_type
  - Model CatalogUpdateProperties has a new parameter tags
  - Model DevBoxDefinition has a new parameter validation_status
  - Model DevBoxDefinitionProperties has a new parameter validation_status
  - Model DevCenter has a new parameter display_name
  - Model DevCenter has a new parameter encryption
  - Model DevCenter has a new parameter project_catalog_settings
  - Model DevCenterUpdate has a new parameter display_name
  - Model DevCenterUpdate has a new parameter encryption
  - Model DevCenterUpdate has a new parameter project_catalog_settings
  - Model EnvironmentType has a new parameter display_name
  - Model EnvironmentTypeUpdate has a new parameter display_name
  - Model OperationStatusResult has a new parameter resource_id
  - Model Pool has a new parameter dev_box_count
  - Model Pool has a new parameter display_name
  - Model Pool has a new parameter managed_virtual_network_regions
  - Model Pool has a new parameter single_sign_on_status
  - Model Pool has a new parameter virtual_network_type
  - Model PoolProperties has a new parameter dev_box_count
  - Model PoolProperties has a new parameter display_name
  - Model PoolProperties has a new parameter managed_virtual_network_regions
  - Model PoolProperties has a new parameter single_sign_on_status
  - Model PoolProperties has a new parameter virtual_network_type
  - Model PoolUpdate has a new parameter display_name
  - Model PoolUpdate has a new parameter managed_virtual_network_regions
  - Model PoolUpdate has a new parameter single_sign_on_status
  - Model PoolUpdate has a new parameter virtual_network_type
  - Model PoolUpdateProperties has a new parameter display_name
  - Model PoolUpdateProperties has a new parameter managed_virtual_network_regions
  - Model PoolUpdateProperties has a new parameter single_sign_on_status
  - Model PoolUpdateProperties has a new parameter virtual_network_type
  - Model Project has a new parameter catalog_settings
  - Model Project has a new parameter display_name
  - Model Project has a new parameter identity
  - Model ProjectEnvironmentType has a new parameter display_name
  - Model ProjectEnvironmentType has a new parameter environment_count
  - Model ProjectEnvironmentTypeProperties has a new parameter display_name
  - Model ProjectEnvironmentTypeProperties has a new parameter environment_count
  - Model ProjectEnvironmentTypeUpdate has a new parameter display_name
  - Model ProjectEnvironmentTypeUpdateProperties has a new parameter display_name
  - Model ProjectProperties has a new parameter catalog_settings
  - Model ProjectProperties has a new parameter display_name
  - Model ProjectUpdate has a new parameter catalog_settings
  - Model ProjectUpdate has a new parameter display_name
  - Model ProjectUpdate has a new parameter identity
  - Model ProjectUpdateProperties has a new parameter catalog_settings
  - Model ProjectUpdateProperties has a new parameter display_name
  - Model Schedule has a new parameter location
  - Model Schedule has a new parameter tags
  - Model ScheduleProperties has a new parameter location
  - Model ScheduleProperties has a new parameter tags
  - Model ScheduleUpdateProperties has a new parameter location
  - Model ScheduleUpdateProperties has a new parameter tags
  - Model Usage has a new parameter id

## 1.1.0b1 (2023-10-23)

### Features Added

  - Added operation CatalogsOperations.begin_connect
  - Added operation CatalogsOperations.get_sync_error_details
  - Added operation group CatalogDevBoxDefinitionsOperations
  - Added operation group CustomizationTasksOperations
  - Added operation group EnvironmentDefinitionsOperations
  - Model AllowedEnvironmentType has a new parameter display_name
  - Model Catalog has a new parameter connection_state
  - Model Catalog has a new parameter last_connection_time
  - Model Catalog has a new parameter last_sync_stats
  - Model Catalog has a new parameter sync_type
  - Model CatalogProperties has a new parameter connection_state
  - Model CatalogProperties has a new parameter last_connection_time
  - Model CatalogProperties has a new parameter last_sync_stats
  - Model CatalogProperties has a new parameter sync_type
  - Model CatalogUpdate has a new parameter sync_type
  - Model CatalogUpdateProperties has a new parameter sync_type
  - Model DevBoxDefinition has a new parameter validation_status
  - Model DevBoxDefinitionProperties has a new parameter validation_status
  - Model DevCenter has a new parameter display_name
  - Model DevCenter has a new parameter encryption
  - Model DevCenterUpdate has a new parameter display_name
  - Model DevCenterUpdate has a new parameter encryption
  - Model EnvironmentType has a new parameter display_name
  - Model EnvironmentTypeUpdate has a new parameter display_name
  - Model Pool has a new parameter dev_box_count
  - Model Pool has a new parameter display_name
  - Model Pool has a new parameter managed_virtual_network_regions
  - Model Pool has a new parameter single_sign_on_status
  - Model Pool has a new parameter virtual_network_type
  - Model PoolProperties has a new parameter dev_box_count
  - Model PoolProperties has a new parameter display_name
  - Model PoolProperties has a new parameter managed_virtual_network_regions
  - Model PoolProperties has a new parameter single_sign_on_status
  - Model PoolProperties has a new parameter virtual_network_type
  - Model PoolUpdate has a new parameter display_name
  - Model PoolUpdate has a new parameter managed_virtual_network_regions
  - Model PoolUpdate has a new parameter single_sign_on_status
  - Model PoolUpdate has a new parameter virtual_network_type
  - Model PoolUpdateProperties has a new parameter display_name
  - Model PoolUpdateProperties has a new parameter managed_virtual_network_regions
  - Model PoolUpdateProperties has a new parameter single_sign_on_status
  - Model PoolUpdateProperties has a new parameter virtual_network_type
  - Model Project has a new parameter display_name
  - Model ProjectEnvironmentType has a new parameter display_name
  - Model ProjectEnvironmentType has a new parameter environment_count
  - Model ProjectEnvironmentTypeProperties has a new parameter display_name
  - Model ProjectEnvironmentTypeProperties has a new parameter environment_count
  - Model ProjectProperties has a new parameter display_name
  - Model ProjectUpdate has a new parameter display_name
  - Model ProjectUpdateProperties has a new parameter display_name
  - Model Usage has a new parameter id

## 1.0.0 (2023-05-20)

### Features Added

  - Added operation NetworkConnectionsOperations.list_outbound_network_dependencies_endpoints
  - Added operation PoolsOperations.begin_run_health_checks
  - Model Image has a new parameter hibernate_support
  - Model Pool has a new parameter health_status
  - Model Pool has a new parameter health_status_details
  - Model Pool has a new parameter stop_on_disconnect
  - Model PoolProperties has a new parameter health_status
  - Model PoolProperties has a new parameter health_status_details
  - Model PoolProperties has a new parameter stop_on_disconnect
  - Model PoolUpdate has a new parameter stop_on_disconnect
  - Model PoolUpdateProperties has a new parameter stop_on_disconnect
  - Model Project has a new parameter max_dev_boxes_per_user
  - Model ProjectProperties has a new parameter max_dev_boxes_per_user
  - Model ProjectUpdate has a new parameter max_dev_boxes_per_user
  - Model ProjectUpdateProperties has a new parameter max_dev_boxes_per_user

### Breaking Changes

  - Model ImageReference no longer has parameter offer
  - Model ImageReference no longer has parameter publisher
  - Model ImageReference no longer has parameter sku

## 1.0.0b4 (2022-11-24)

### Features Added

  - Added operation group CheckNameAvailabilityOperations
  - Model DevBoxDefinition has a new parameter hibernate_support
  - Model DevBoxDefinitionProperties has a new parameter hibernate_support
  - Model DevBoxDefinitionUpdate has a new parameter hibernate_support
  - Model DevBoxDefinitionUpdateProperties has a new parameter hibernate_support
  - Model DevCenter has a new parameter dev_center_uri
  - Model Project has a new parameter dev_center_uri
  - Model ProjectProperties has a new parameter dev_center_uri

### Breaking Changes

  - Renamed operation NetworkConnectionsOperations.run_health_checks to NetworkConnectionsOperations.begin_run_health_checks

## 1.0.0b3 (2022-11-08)

### Features Added

  - Model Catalog has a new parameter sync_state
  - Model CatalogProperties has a new parameter sync_state
  - Model OperationStatus has a new parameter operations
  - Model OperationStatus has a new parameter resource_id

### Breaking Changes

  - Client name is changed from `DevCenterClient` to `DevCenterMgmtClient`
  - Parameter status of model OperationStatus is now required

## 1.0.0b2 (2022-09-29)

### Features Added

  - Added operation group ProjectAllowedEnvironmentTypesOperations

## 1.0.0b1 (2022-08-15)

* Initial Release
