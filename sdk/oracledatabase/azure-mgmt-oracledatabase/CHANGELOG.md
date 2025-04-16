# Release History

## 2.0.0 (2025-04-16)

### Features Added

  - Added operation AutonomousDatabaseBackupsOperations.list_by_parent
  - Added operation AutonomousDatabasesOperations.begin_change_disaster_recovery_configuration
  - Added operation DbNodesOperations.list_by_parent
  - Added operation DbServersOperations.list_by_parent
  - Added operation OracleSubscriptionsOperations.begin_add_azure_subscriptions
  - Added operation VirtualNetworkAddressesOperations.list_by_parent
  - Added operation group ExadbVmClustersOperations
  - Added operation group ExascaleDbNodesOperations
  - Added operation group ExascaleDbStorageVaultsOperations
  - Added operation group FlexComponentsOperations
  - Added operation group GiMinorVersionsOperations
  - Added operation group ListActionsOperations
  - Model AutonomousDatabaseBaseProperties has a new parameter remote_disaster_recovery_configuration
  - Model AutonomousDatabaseBaseProperties has a new parameter time_disaster_recovery_role_changed
  - Model AutonomousDatabaseCloneProperties has a new parameter remote_disaster_recovery_configuration
  - Model AutonomousDatabaseCloneProperties has a new parameter time_disaster_recovery_role_changed
  - Model AutonomousDatabaseProperties has a new parameter remote_disaster_recovery_configuration
  - Model AutonomousDatabaseProperties has a new parameter time_disaster_recovery_role_changed
  - Model CloudExadataInfrastructureProperties has a new parameter compute_model
  - Model CloudExadataInfrastructureProperties has a new parameter database_server_type
  - Model CloudExadataInfrastructureProperties has a new parameter defined_file_system_configuration
  - Model CloudExadataInfrastructureProperties has a new parameter storage_server_type
  - Model CloudVmClusterProperties has a new parameter compute_model
  - Model CloudVmClusterProperties has a new parameter file_system_configuration_details
  - Model CloudVmClusterUpdateProperties has a new parameter file_system_configuration_details
  - Model DbServerProperties has a new parameter compute_model
  - Model DbSystemShapeProperties has a new parameter are_server_types_supported
  - Model DbSystemShapeProperties has a new parameter compute_model
  - Model DbSystemShapeProperties has a new parameter display_name
  - Model OracleSubscriptionProperties has a new parameter add_subscription_operation_state
  - Model OracleSubscriptionProperties has a new parameter azure_subscription_ids
  - Model OracleSubscriptionProperties has a new parameter last_operation_status_detail
  - Model PeerDbDetails has a new parameter peer_db_location
  - Model PeerDbDetails has a new parameter peer_db_ocid
  - Operation DbSystemShapesOperations.list_by_location has a new optional parameter zone
  - Operation GiVersionsOperations.list_by_location has a new optional parameter shape
  - Operation GiVersionsOperations.list_by_location has a new optional parameter zone

### Breaking Changes

  - Model DbSystemShapeProperties has a new required parameter shape_name
  - Parameter display_name of model DnsPrivateViewProperties is now required
  - Parameter lifecycle_state of model DbNodeProperties is now required
  - Parameter lifecycle_state of model DnsPrivateViewProperties is now required
  - Parameter lifecycle_state of model DnsPrivateZoneProperties is now required
  - Parameter time_created of model DbNodeProperties is now required
  - Parameter vnic_id of model DbNodeProperties is now required
  - Removed operation AutonomousDatabaseBackupsOperations.list_by_autonomous_database
  - Removed operation DbNodesOperations.list_by_cloud_vm_cluster
  - Removed operation DbServersOperations.list_by_cloud_exadata_infrastructure
  - Removed operation VirtualNetworkAddressesOperations.list_by_cloud_vm_cluster

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
