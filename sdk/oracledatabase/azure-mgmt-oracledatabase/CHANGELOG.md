# Release History

## 2.0.0 (2025-05-13)

### Features Added

  - Client `OracleDatabaseMgmtClient` added operation group `exadb_vm_clusters`
  - Client `OracleDatabaseMgmtClient` added operation group `exascale_db_storage_vaults`
  - Client `OracleDatabaseMgmtClient` added operation group `flex_components`
  - Client `OracleDatabaseMgmtClient` added operation group `gi_minor_versions`
  - Client `OracleDatabaseMgmtClient` added operation group `exascale_db_nodes`
  - Model `AutonomousDatabaseBackupUpdate` added property `id`
  - Model `AutonomousDatabaseBackupUpdate` added property `name`
  - Model `AutonomousDatabaseBackupUpdate` added property `type`
  - Model `AutonomousDatabaseBackupUpdate` added property `system_data`
  - Model `AutonomousDatabaseBaseProperties` added property `time_disaster_recovery_role_changed`
  - Model `AutonomousDatabaseBaseProperties` added property `remote_disaster_recovery_configuration`
  - Model `AutonomousDatabaseCloneProperties` added property `time_disaster_recovery_role_changed`
  - Model `AutonomousDatabaseCloneProperties` added property `remote_disaster_recovery_configuration`
  - Model `AutonomousDatabaseProperties` added property `time_disaster_recovery_role_changed`
  - Model `AutonomousDatabaseProperties` added property `remote_disaster_recovery_configuration`
  - Model `CloudExadataInfrastructureProperties` added property `defined_file_system_configuration`
  - Model `CloudExadataInfrastructureProperties` added property `database_server_type`
  - Model `CloudExadataInfrastructureProperties` added property `storage_server_type`
  - Model `CloudExadataInfrastructureProperties` added property `compute_model`
  - Model `CloudVmClusterProperties` added property `file_system_configuration_details`
  - Model `CloudVmClusterProperties` added property `compute_model`
  - Model `CloudVmClusterUpdateProperties` added property `file_system_configuration_details`
  - Enum `DataBaseType` added member `CLONE_FROM_BACKUP_TIMESTAMP`
  - Enum `DataBaseType` added member `CROSS_REGION_DISASTER_RECOVERY`
  - Model `DbServerProperties` added property `compute_model`
  - Model `DbSystemShapeProperties` added property `shape_name`
  - Model `DbSystemShapeProperties` added property `compute_model`
  - Model `DbSystemShapeProperties` added property `are_server_types_supported`
  - Model `DbSystemShapeProperties` added property `display_name`
  - Model `OracleSubscriptionProperties` added property `azure_subscription_ids`
  - Model `OracleSubscriptionProperties` added property `add_subscription_operation_state`
  - Model `OracleSubscriptionProperties` added property `last_operation_status_detail`
  - Model `PeerDbDetails` added property `peer_db_ocid`
  - Model `PeerDbDetails` added property `peer_db_location`
  - Added enum `AddSubscriptionOperationState`
  - Added model `AutonomousDatabaseCrossRegionDisasterRecoveryProperties`
  - Added model `AutonomousDatabaseFromBackupTimestampProperties`
  - Added model `AzureSubscriptions`
  - Added model `DbActionResponse`
  - Added model `DbNodeDetails`
  - Added model `DefinedFileSystemConfiguration`
  - Added model `DisasterRecoveryConfigurationDetails`
  - Added model `ExadbVmCluster`
  - Added enum `ExadbVmClusterLifecycleState`
  - Added model `ExadbVmClusterListResult`
  - Added model `ExadbVmClusterProperties`
  - Added model `ExadbVmClusterStorageDetails`
  - Added model `ExadbVmClusterUpdate`
  - Added model `ExadbVmClusterUpdateProperties`
  - Added model `ExascaleDbNode`
  - Added model `ExascaleDbNodeListResult`
  - Added model `ExascaleDbNodeProperties`
  - Added model `ExascaleDbStorageDetails`
  - Added model `ExascaleDbStorageInputDetails`
  - Added model `ExascaleDbStorageVault`
  - Added enum `ExascaleDbStorageVaultLifecycleState`
  - Added model `ExascaleDbStorageVaultListResult`
  - Added model `ExascaleDbStorageVaultProperties`
  - Added model `ExascaleDbStorageVaultTagsUpdate`
  - Added model `FileSystemConfigurationDetails`
  - Added model `FlexComponent`
  - Added model `FlexComponentListResult`
  - Added model `FlexComponentProperties`
  - Added model `GiMinorVersion`
  - Added model `GiMinorVersionListResult`
  - Added model `GiMinorVersionProperties`
  - Added enum `GridImageType`
  - Added enum `HardwareType`
  - Added model `RemoveVirtualMachineFromExadbVmClusterDetails`
  - Added enum `ShapeFamily`
  - Added enum `SystemShapes`
  - Model `AutonomousDatabaseBackupsOperations` added method `list_by_parent`
  - Model `AutonomousDatabasesOperations` added method `begin_change_disaster_recovery_configuration`
  - Model `DbNodesOperations` added method `list_by_parent`
  - Model `DbServersOperations` added method `list_by_parent`
  - Model `OracleSubscriptionsOperations` added method `begin_add_azure_subscriptions`
  - Model `VirtualNetworkAddressesOperations` added method `list_by_parent`
  - Added model `ExadbVmClustersOperations`
  - Added model `ExascaleDbNodesOperations`
  - Added model `ExascaleDbStorageVaultsOperations`
  - Added model `FlexComponentsOperations`
  - Added model `GiMinorVersionsOperations`
  - Method `AutonomousDatabasesOperations.begin_change_disaster_recovery_configuration` has a new overload `def begin_change_disaster_recovery_configuration(self: None, resource_group_name: str, autonomousdatabasename: str, body: DisasterRecoveryConfigurationDetails, content_type: str)`
  - Method `AutonomousDatabasesOperations.begin_change_disaster_recovery_configuration` has a new overload `def begin_change_disaster_recovery_configuration(self: None, resource_group_name: str, autonomousdatabasename: str, body: IO[bytes], content_type: str)`
  - Method `OracleSubscriptionsOperations.begin_add_azure_subscriptions` has a new overload `def begin_add_azure_subscriptions(self: None, body: AzureSubscriptions, content_type: str)`
  - Method `OracleSubscriptionsOperations.begin_add_azure_subscriptions` has a new overload `def begin_add_azure_subscriptions(self: None, body: IO[bytes], content_type: str)`
  - Method `ExadbVmClustersOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, exadb_vm_cluster_name: str, resource: ExadbVmCluster, content_type: str)`
  - Method `ExadbVmClustersOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, exadb_vm_cluster_name: str, resource: IO[bytes], content_type: str)`
  - Method `ExadbVmClustersOperations.begin_remove_vms` has a new overload `def begin_remove_vms(self: None, resource_group_name: str, exadb_vm_cluster_name: str, body: RemoveVirtualMachineFromExadbVmClusterDetails, content_type: str)`
  - Method `ExadbVmClustersOperations.begin_remove_vms` has a new overload `def begin_remove_vms(self: None, resource_group_name: str, exadb_vm_cluster_name: str, body: IO[bytes], content_type: str)`
  - Method `ExadbVmClustersOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, exadb_vm_cluster_name: str, properties: ExadbVmClusterUpdate, content_type: str)`
  - Method `ExadbVmClustersOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, exadb_vm_cluster_name: str, properties: IO[bytes], content_type: str)`
  - Method `ExascaleDbNodesOperations.begin_action` has a new overload `def begin_action(self: None, resource_group_name: str, exadb_vm_cluster_name: str, exascale_db_node_name: str, body: DbNodeAction, content_type: str)`
  - Method `ExascaleDbNodesOperations.begin_action` has a new overload `def begin_action(self: None, resource_group_name: str, exadb_vm_cluster_name: str, exascale_db_node_name: str, body: IO[bytes], content_type: str)`
  - Method `ExascaleDbStorageVaultsOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, exascale_db_storage_vault_name: str, resource: ExascaleDbStorageVault, content_type: str)`
  - Method `ExascaleDbStorageVaultsOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, exascale_db_storage_vault_name: str, resource: IO[bytes], content_type: str)`
  - Method `ExascaleDbStorageVaultsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, exascale_db_storage_vault_name: str, properties: ExascaleDbStorageVaultTagsUpdate, content_type: str)`
  - Method `ExascaleDbStorageVaultsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, exascale_db_storage_vault_name: str, properties: IO[bytes], content_type: str)`

### Breaking Changes

  - Deleted or renamed model `AutonomousDatabaseBackupUpdateProperties`
  - Deleted or renamed method `AutonomousDatabaseBackupsOperations.list_by_autonomous_database`
  - Deleted or renamed method `DbNodesOperations.list_by_cloud_vm_cluster`
  - Deleted or renamed method `DbServersOperations.list_by_cloud_exadata_infrastructure`
  - Deleted or renamed method `VirtualNetworkAddressesOperations.list_by_cloud_vm_cluster`

## 1.0.0 (2024-07-04)

### Other Changes

  - First GA

## 1.0.0b2 (2024-06-21)

### Features Added

  - Added operation AutonomousDatabasesOperations.begin_restore
  - Added operation AutonomousDatabasesOperations.begin_shrink
  - Added operation group SystemVersionsOperations
  - Model AutonomousDatabaseBackupProperties has a new parameter autonomous_database_ocid
  - Model AutonomousDatabaseBackupProperties has a new parameter backup_type
  - Model AutonomousDatabaseBackupProperties has a new parameter database_size_in_tbs
  - Model AutonomousDatabaseBackupProperties has a new parameter size_in_tbs
  - Model AutonomousDatabaseBackupProperties has a new parameter time_started
  - Model AutonomousDatabaseBaseProperties has a new parameter long_term_backup_schedule
  - Model AutonomousDatabaseBaseProperties has a new parameter next_long_term_backup_time_stamp
  - Model AutonomousDatabaseCloneProperties has a new parameter long_term_backup_schedule
  - Model AutonomousDatabaseCloneProperties has a new parameter next_long_term_backup_time_stamp
  - Model AutonomousDatabaseProperties has a new parameter long_term_backup_schedule
  - Model AutonomousDatabaseProperties has a new parameter next_long_term_backup_time_stamp
  - Model AutonomousDatabaseUpdateProperties has a new parameter long_term_backup_schedule

### Breaking Changes

  - Model AutonomousDatabaseBackupProperties no longer has parameter autonomous_database_id
  - Model AutonomousDatabaseBackupProperties no longer has parameter database_size_in_t_bs
  - Model AutonomousDatabaseBackupProperties no longer has parameter size_in_t_bs
  - Model AutonomousDatabaseBackupProperties no longer has parameter type

## 1.0.0b1 (2024-05-27)

* Initial Release
