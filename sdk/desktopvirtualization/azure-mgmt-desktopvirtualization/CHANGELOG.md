# Release History

## 3.0.0b1 (2025-05-12)

### Features Added

  - Client `DesktopVirtualizationMgmtClient` added operation group `session_host_managements`
  - Client `DesktopVirtualizationMgmtClient` added operation group `initiate_session_host_update`
  - Client `DesktopVirtualizationMgmtClient` added operation group `control_session_host_update`
  - Client `DesktopVirtualizationMgmtClient` added operation group `control_session_host_provisioning`
  - Client `DesktopVirtualizationMgmtClient` added operation group `session_host_managements_update_status`
  - Client `DesktopVirtualizationMgmtClient` added operation group `session_host_provisioning_statuses`
  - Client `DesktopVirtualizationMgmtClient` added operation group `session_host_configurations`
  - Client `DesktopVirtualizationMgmtClient` added operation group `active_session_host_configurations`
  - Client `DesktopVirtualizationMgmtClient` added operation group `session_host`
  - Model `AppAttachPackagePatch` added property `tags`
  - Model `AppAttachPackagePatchProperties` added property `package_lookback_url`
  - Model `AppAttachPackagePatchProperties` added property `custom_data`
  - Model `AppAttachPackageProperties` added property `package_owner_name`
  - Model `AppAttachPackageProperties` added property `package_lookback_url`
  - Model `AppAttachPackageProperties` added property `custom_data`
  - Model `HostPool` added property `management_type`
  - Model `HostPool` added property `managed_private_udp`
  - Model `HostPool` added property `direct_udp`
  - Model `HostPool` added property `public_udp`
  - Model `HostPool` added property `relay_udp`
  - Model `HostPoolPatch` added property `managed_private_udp`
  - Model `HostPoolPatch` added property `direct_udp`
  - Model `HostPoolPatch` added property `public_udp`
  - Model `HostPoolPatch` added property `relay_udp`
  - Enum `LoadBalancerType` added member `MULTIPLE_PERSISTENT`
  - Enum `ScalingHostPoolType` added member `PERSONAL`
  - Model `ScalingPlanPooledSchedule` added property `name_properties_name`
  - Model `ScalingPlanPooledSchedule` added property `scaling_method`
  - Model `ScalingPlanPooledSchedule` added property `create_delete`
  - Model `ScalingPlanPooledSchedulePatch` added property `name_properties_name`
  - Model `ScalingPlanPooledSchedulePatch` added property `scaling_method`
  - Model `ScalingPlanPooledSchedulePatch` added property `create_delete`
  - Model `ScalingSchedule` added property `scaling_method`
  - Model `ScalingSchedule` added property `create_delete`
  - Model `SessionHost` added property `active_sessions`
  - Model `SessionHost` added property `disconnected_sessions`
  - Model `SessionHost` added property `pending_sessions`
  - Model `SessionHost` added property `last_session_host_update_time`
  - Model `SessionHost` added property `session_host_configuration`
  - Added model `ActiveDirectoryInfoPatchProperties`
  - Added model `ActiveDirectoryInfoProperties`
  - Added model `ActiveSessionHostConfiguration`
  - Added model `ActiveSessionHostConfigurationList`
  - Added model `AzureActiveDirectoryInfoProperties`
  - Added model `BootDiagnosticsInfoPatchProperties`
  - Added model `BootDiagnosticsInfoProperties`
  - Added enum `CanaryPolicy`
  - Added model `CreateDeleteProperties`
  - Added model `CustomInfoPatchProperties`
  - Added model `CustomInfoProperties`
  - Added enum `DiffDiskOption`
  - Added enum `DiffDiskPlacement`
  - Added model `DiffDiskProperties`
  - Added enum `DirectUDP`
  - Added model `DiskInfoProperties`
  - Added model `DomainInfoPatchProperties`
  - Added model `DomainInfoProperties`
  - Added enum `DomainJoinType`
  - Added enum `FailedSessionHostCleanupPolicySHC`
  - Added enum `FaultType`
  - Added enum `HostPoolProvisioningAction`
  - Added model `HostPoolProvisioningControlParameter`
  - Added enum `HostPoolUpdateAction`
  - Added model `HostPoolUpdateConfigurationPatchProperties`
  - Added model `HostPoolUpdateConfigurationProperties`
  - Added model `HostPoolUpdateControlParameter`
  - Added model `HostPoolUpdateFault`
  - Added model `ImageInfoPatchProperties`
  - Added model `ImageInfoProperties`
  - Added model `KeyVaultCredentialsPatchProperties`
  - Added model `KeyVaultCredentialsProperties`
  - Added model `ManagedDiskProperties`
  - Added enum `ManagedPrivateUDP`
  - Added model `ManagedServiceIdentity`
  - Added enum `ManagedServiceIdentityType`
  - Added enum `ManagementType`
  - Added model `MarketplaceInfoPatchProperties`
  - Added model `MarketplaceInfoProperties`
  - Added model `NetworkInfoPatchProperties`
  - Added model `NetworkInfoProperties`
  - Added enum `OperationTypeSHM`
  - Added enum `ProvisioningStateSHC`
  - Added enum `PublicUDP`
  - Added enum `RelayUDP`
  - Added enum `ScalingMethod`
  - Added model `SecurityInfoPatchProperties`
  - Added model `SecurityInfoProperties`
  - Added model `SessionHostConfiguration`
  - Added model `SessionHostConfigurationList`
  - Added model `SessionHostConfigurationPatch`
  - Added model `SessionHostManagement`
  - Added model `SessionHostManagementList`
  - Added model `SessionHostManagementOperationProgress`
  - Added model `SessionHostManagementPatch`
  - Added model `SessionHostManagementProvisioningOperationProgress`
  - Added model `SessionHostManagementProvisioningStatus`
  - Added model `SessionHostManagementUpdateStatus`
  - Added model `SessionHostProvisioningConfigurationPatchProperties`
  - Added model `SessionHostProvisioningConfigurationProperties`
  - Added enum `Type`
  - Added model `UpdateSessionHostsRequestBody`
  - Added model `UserAssignedIdentity`
  - Added enum `VirtualMachineDiskType`
  - Added enum `VirtualMachineSecurityType`
  - Added model `ActiveSessionHostConfigurationsOperations`
  - Added model `ControlSessionHostProvisioningOperations`
  - Added model `ControlSessionHostUpdateOperations`
  - Added model `InitiateSessionHostUpdateOperations`
  - Added model `SessionHostConfigurationsOperations`
  - Added model `SessionHostManagementsOperations`
  - Added model `SessionHostManagementsUpdateStatusOperations`
  - Added model `SessionHostOperations`
  - Added model `SessionHostProvisioningStatusesOperations`
  - Method `ControlSessionHostProvisioningOperations.begin_post` has a new overload `def begin_post(self: None, resource_group_name: str, host_pool_name: str, host_pool_provisioning_control_parameter: HostPoolProvisioningControlParameter, content_type: str)`
  - Method `ControlSessionHostProvisioningOperations.begin_post` has a new overload `def begin_post(self: None, resource_group_name: str, host_pool_name: str, host_pool_provisioning_control_parameter: IO[bytes], content_type: str)`
  - Method `ControlSessionHostUpdateOperations.begin_post` has a new overload `def begin_post(self: None, resource_group_name: str, host_pool_name: str, host_pool_update_control_parameter: HostPoolUpdateControlParameter, content_type: str)`
  - Method `ControlSessionHostUpdateOperations.begin_post` has a new overload `def begin_post(self: None, resource_group_name: str, host_pool_name: str, host_pool_update_control_parameter: IO[bytes], content_type: str)`
  - Method `InitiateSessionHostUpdateOperations.post` has a new overload `def post(self: None, resource_group_name: str, host_pool_name: str, update_session_hosts_request_body: Optional[UpdateSessionHostsRequestBody], content_type: str)`
  - Method `InitiateSessionHostUpdateOperations.post` has a new overload `def post(self: None, resource_group_name: str, host_pool_name: str, update_session_hosts_request_body: Optional[IO[bytes]], content_type: str)`
  - Method `SessionHostConfigurationsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, host_pool_name: str, session_host_configuration: SessionHostConfiguration, content_type: str)`
  - Method `SessionHostConfigurationsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, host_pool_name: str, session_host_configuration: IO[bytes], content_type: str)`
  - Method `SessionHostConfigurationsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, host_pool_name: str, session_host_configuration: Optional[SessionHostConfigurationPatch], content_type: str)`
  - Method `SessionHostConfigurationsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, host_pool_name: str, session_host_configuration: Optional[IO[bytes]], content_type: str)`
  - Method `SessionHostManagementsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, host_pool_name: str, session_host_management: SessionHostManagement, content_type: str)`
  - Method `SessionHostManagementsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, host_pool_name: str, session_host_management: IO[bytes], content_type: str)`
  - Method `SessionHostManagementsOperations.update` has a new overload `def update(self: None, resource_group_name: str, host_pool_name: str, session_host_management: Optional[SessionHostManagementPatch], content_type: str)`
  - Method `SessionHostManagementsOperations.update` has a new overload `def update(self: None, resource_group_name: str, host_pool_name: str, session_host_management: Optional[IO[bytes]], content_type: str)`

### Breaking Changes

  - Method `ScalingPlanPersonalSchedule.__init__` removed default value `None` from its parameter `days_of_week`
  - Method `ScalingPlanPersonalSchedule.__init__` removed default value `None` from its parameter `ramp_up_start_time`
  - Method `ScalingPlanPersonalSchedule.__init__` removed default value `None` from its parameter `peak_start_time`
  - Method `ScalingPlanPersonalSchedule.__init__` removed default value `None` from its parameter `ramp_down_start_time`
  - Method `ScalingPlanPersonalSchedule.__init__` removed default value `None` from its parameter `off_peak_start_time`
  - Method `ScalingPlanPooledSchedule.__init__` removed default value `None` from its parameter `days_of_week`
  - Method `ScalingPlanPooledSchedule.__init__` removed default value `None` from its parameter `ramp_up_start_time`
  - Method `ScalingPlanPooledSchedule.__init__` removed default value `None` from its parameter `ramp_up_capacity_threshold_pct`
  - Method `ScalingPlanPooledSchedule.__init__` removed default value `None` from its parameter `peak_start_time`
  - Method `ScalingPlanPooledSchedule.__init__` removed default value `None` from its parameter `ramp_down_start_time`
  - Method `ScalingPlanPooledSchedule.__init__` removed default value `None` from its parameter `ramp_down_capacity_threshold_pct`
  - Method `ScalingPlanPooledSchedule.__init__` removed default value `None` from its parameter `off_peak_start_time`
  - Deleted or renamed model `Identity`
  - Deleted or renamed model `ResourceModelWithAllowedPropertySetIdentity`
  - Deleted or renamed model `ResourceModelWithAllowedPropertySetPlan`
  - Deleted or renamed model `ResourceModelWithAllowedPropertySetSku`
  - Deleted or renamed model `ScalingScheduleDaysOfWeekItem`

## 2.0.0 (2024-09-23)

### Features Added

  - The 'DesktopVirtualizationMgmtClient' client had operation group 'app_attach_package_info' added in the current version
  - The 'DesktopVirtualizationMgmtClient' client had operation group 'app_attach_package' added in the current version
  - The model or publicly exposed class 'ExpandMsixImage' had property 'certificate_name' added in the current version
  - The model or publicly exposed class 'ExpandMsixImage' had property 'certificate_expiry' added in the current version
  - The model or publicly exposed class 'HostPool' had property 'app_attach_package_references' added in the current version
  - The model or publicly exposed class 'PrivateEndpointConnection' had property 'group_ids' added in the current version
  - The model or publicly exposed class 'PrivateEndpointConnectionWithSystemData' had property 'group_ids' added in the current version
  - The model or publicly exposed class 'PrivateEndpointConnectionWithSystemData' had property 'private_endpoint' added in the current version
  - The model or publicly exposed class 'PrivateEndpointConnectionWithSystemData' had property 'private_link_service_connection_state' added in the current version
  - The model or publicly exposed class 'PrivateEndpointConnectionWithSystemData' had property 'provisioning_state' added in the current version
  - The model or publicly exposed class 'PrivateEndpointConnectionWithSystemData' had property 'id' added in the current version
  - The model or publicly exposed class 'PrivateEndpointConnectionWithSystemData' had property 'name' added in the current version
  - The model or publicly exposed class 'PrivateEndpointConnectionWithSystemData' had property 'type' added in the current version
  - The model or publicly exposed class 'PrivateEndpointConnectionWithSystemData' had property 'additional_properties' added in the current version
  - The model or publicly exposed class 'Resource' had property 'system_data' added in the current version
  - The model or publicly exposed class 'AppAttachPackage' was added in the current version
  - The model or publicly exposed class 'AppAttachPackageArchitectures' was added in the current version
  - The model or publicly exposed class 'AppAttachPackageInfoProperties' was added in the current version
  - The model or publicly exposed class 'AppAttachPackageList' was added in the current version
  - The model or publicly exposed class 'AppAttachPackagePatch' was added in the current version
  - The model or publicly exposed class 'AppAttachPackagePatchProperties' was added in the current version
  - The model or publicly exposed class 'AppAttachPackageProperties' was added in the current version
  - The model or publicly exposed class 'ErrorAdditionalInfo' was added in the current version
  - The model or publicly exposed class 'ErrorDetail' was added in the current version
  - The model or publicly exposed class 'ErrorResponse' was added in the current version
  - The model or publicly exposed class 'FailHealthCheckOnStagingFailure' was added in the current version
  - The model or publicly exposed class 'ImportPackageInfoRequest' was added in the current version
  - The model or publicly exposed class 'PackageTimestamped' was added in the current version
  - The model or publicly exposed class 'ProvisioningState' was added in the current version
  - The model or publicly exposed class 'RegistrationTokenList' was added in the current version
  - The model or publicly exposed class 'RegistrationTokenMinimal' was added in the current version
  - The model or publicly exposed class 'TrackedResource' was added in the current version
  - The 'HostPoolsOperations' method 'list_registration_tokens' was added in the current version
  - The model or publicly exposed class 'AppAttachPackageInfoOperations' was added in the current version
  - The model or publicly exposed class 'AppAttachPackageOperations' was added in the current version

### Breaking Changes

  - Parameter `location` of model `ApplicationGroup` is now required
  - Parameter `location` of model `HostPool` is now required
  - Parameter `location` of model `ResourceModelWithAllowedPropertySet` is now required
  - Parameter `location` of model `ScalingPlan` is now required
  - Parameter `location` of model `Workspace` is now required

## 1.1.0 (2023-10-23)

### Features Added

  - Added operation group PrivateEndpointConnectionsOperations
  - Added operation group PrivateLinkResourcesOperations
  - Added operation group ScalingPlanPersonalSchedulesOperations
  - Model ApplicationGroup has a new parameter show_in_feed
  - Model ApplicationGroupPatch has a new parameter show_in_feed
  - Model HostPool has a new parameter private_endpoint_connections
  - Model HostPool has a new parameter public_network_access
  - Model HostPoolPatch has a new parameter public_network_access
  - Model Workspace has a new parameter private_endpoint_connections
  - Model Workspace has a new parameter public_network_access
  - Model WorkspacePatch has a new parameter public_network_access

## 1.0.0 (2023-03-20)

### other changes

  - First GA version

## 1.0.0b2 (2022-11-09)

### Features Added

  - Added operation group ScalingPlanPooledSchedulesOperations
  - Model HostPool has a new parameter agent_update
  - Model HostPoolPatch has a new parameter agent_update
  - Model SessionHost has a new parameter friendly_name
  - Model SessionHostPatch has a new parameter friendly_name

### Breaking Changes

  - Client name is changed from `DesktopVirtualizationAPIClient` to `DesktopVirtualizationMgmtClient`
  - Model ApplicationGroup no longer has parameter migration_request
  - Model HostPool no longer has parameter migration_request
  - Model HostPool no longer has parameter public_network_access
  - Model HostPoolPatch no longer has parameter public_network_access
  - Model Workspace no longer has parameter public_network_access
  - Model WorkspacePatch no longer has parameter public_network_access
  - Operation ApplicationGroupsOperations.list_by_resource_group has a new parameter initial_skip
  - Operation ApplicationGroupsOperations.list_by_resource_group has a new parameter is_descending
  - Operation ApplicationGroupsOperations.list_by_resource_group has a new parameter page_size
  - Operation ApplicationsOperations.list has a new parameter initial_skip
  - Operation ApplicationsOperations.list has a new parameter is_descending
  - Operation ApplicationsOperations.list has a new parameter page_size
  - Operation DesktopsOperations.list has a new parameter initial_skip
  - Operation DesktopsOperations.list has a new parameter is_descending
  - Operation DesktopsOperations.list has a new parameter page_size
  - Operation HostPoolsOperations.list has a new parameter initial_skip
  - Operation HostPoolsOperations.list has a new parameter is_descending
  - Operation HostPoolsOperations.list has a new parameter page_size
  - Operation HostPoolsOperations.list_by_resource_group has a new parameter initial_skip
  - Operation HostPoolsOperations.list_by_resource_group has a new parameter is_descending
  - Operation HostPoolsOperations.list_by_resource_group has a new parameter page_size
  - Operation MSIXPackagesOperations.list has a new parameter initial_skip
  - Operation MSIXPackagesOperations.list has a new parameter is_descending
  - Operation MSIXPackagesOperations.list has a new parameter page_size
  - Operation ScalingPlansOperations.list_by_host_pool has a new parameter initial_skip
  - Operation ScalingPlansOperations.list_by_host_pool has a new parameter is_descending
  - Operation ScalingPlansOperations.list_by_host_pool has a new parameter page_size
  - Operation ScalingPlansOperations.list_by_resource_group has a new parameter initial_skip
  - Operation ScalingPlansOperations.list_by_resource_group has a new parameter is_descending
  - Operation ScalingPlansOperations.list_by_resource_group has a new parameter page_size
  - Operation ScalingPlansOperations.list_by_subscription has a new parameter initial_skip
  - Operation ScalingPlansOperations.list_by_subscription has a new parameter is_descending
  - Operation ScalingPlansOperations.list_by_subscription has a new parameter page_size
  - Operation SessionHostsOperations.list has a new parameter initial_skip
  - Operation SessionHostsOperations.list has a new parameter is_descending
  - Operation SessionHostsOperations.list has a new parameter page_size
  - Operation StartMenuItemsOperations.list has a new parameter initial_skip
  - Operation StartMenuItemsOperations.list has a new parameter is_descending
  - Operation StartMenuItemsOperations.list has a new parameter page_size
  - Operation UserSessionsOperations.list has a new parameter initial_skip
  - Operation UserSessionsOperations.list has a new parameter is_descending
  - Operation UserSessionsOperations.list has a new parameter page_size
  - Operation UserSessionsOperations.list_by_host_pool has a new parameter initial_skip
  - Operation UserSessionsOperations.list_by_host_pool has a new parameter is_descending
  - Operation UserSessionsOperations.list_by_host_pool has a new parameter page_size
  - Operation WorkspacesOperations.list_by_resource_group has a new parameter initial_skip
  - Operation WorkspacesOperations.list_by_resource_group has a new parameter is_descending
  - Operation WorkspacesOperations.list_by_resource_group has a new parameter page_size
  - Parameter time_zone of model ScalingPlan is now required
  - Removed operation group PrivateEndpointConnectionsOperations
  - Removed operation group PrivateLinkResourcesOperations

## 1.0.0b1 (2021-11-11)

* Initial Release
