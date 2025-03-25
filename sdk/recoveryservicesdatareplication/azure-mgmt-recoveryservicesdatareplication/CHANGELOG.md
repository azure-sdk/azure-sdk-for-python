# Release History

## 1.0.0 (2025-03-25)

### Features Added

  - Added operation ProtectedItemOperations.begin_update
  - Added operation group CheckNameAvailabilityOperations
  - Added operation group DeploymentPreflightOperations
  - Added operation group FabricAgentOperations
  - Added operation group JobOperations
  - Added operation group LocationBasedOperationResultsOperations
  - Added operation group OperationResultsOperations
  - Added operation group PrivateEndpointConnectionProxiesOperations
  - Added operation group PrivateEndpointConnectionsOperations
  - Added operation group PrivateLinkResourcesOperations
  - Added operation group RecoveryPointOperations
  - Model DeploymentPreflightResource has a new parameter properties
  - Model EmailConfigurationModelProperties has a new parameter provisioning_state
  - Model EventModelProperties has a new parameter provisioning_state
  - Model HyperVToAzStackHCIDiskInput has a new parameter disk_block_size
  - Model HyperVToAzStackHCIDiskInput has a new parameter disk_controller
  - Model HyperVToAzStackHCIDiskInput has a new parameter disk_identifier
  - Model HyperVToAzStackHCIDiskInput has a new parameter disk_logical_sector_size
  - Model HyperVToAzStackHCIDiskInput has a new parameter disk_physical_sector_size
  - Model HyperVToAzStackHCINicInput has a new parameter is_mac_migration_enabled
  - Model HyperVToAzStackHCINicInput has a new parameter is_static_ip_migration_enabled
  - Model HyperVToAzStackHCIProtectedDiskProperties has a new parameter disk_block_size
  - Model HyperVToAzStackHCIProtectedDiskProperties has a new parameter disk_logical_sector_size
  - Model HyperVToAzStackHCIProtectedDiskProperties has a new parameter disk_physical_sector_size
  - Model ProtectedItemModelProperties has a new parameter fabric_agent_id
  - Model ProtectedItemModelProperties has a new parameter target_fabric_agent_id
  - Model RecoveryPointModelProperties has a new parameter provisioning_state
  - Model TaskModel has a new parameter children_jobs
  - Model VMwareToAzStackHCIDiskInput has a new parameter disk_block_size
  - Model VMwareToAzStackHCIDiskInput has a new parameter disk_controller
  - Model VMwareToAzStackHCIDiskInput has a new parameter disk_identifier
  - Model VMwareToAzStackHCIDiskInput has a new parameter disk_logical_sector_size
  - Model VMwareToAzStackHCIDiskInput has a new parameter disk_physical_sector_size
  - Model VMwareToAzStackHCINicInput has a new parameter is_mac_migration_enabled
  - Model VMwareToAzStackHCINicInput has a new parameter is_static_ip_migration_enabled
  - Model VMwareToAzStackHCIProtectedDiskProperties has a new parameter disk_block_size
  - Model VMwareToAzStackHCIProtectedDiskProperties has a new parameter disk_logical_sector_size
  - Model VMwareToAzStackHCIProtectedDiskProperties has a new parameter disk_physical_sector_size
  - Model VaultModel has a new parameter identity
  - Model VaultModelUpdate has a new parameter identity
  - Operation EventOperations.list has a new optional parameter odata_options
  - Operation EventOperations.list has a new optional parameter page_size
  - Operation ProtectedItemOperations.list has a new optional parameter continuation_token_parameter
  - Operation ProtectedItemOperations.list has a new optional parameter odata_options
  - Operation ProtectedItemOperations.list has a new optional parameter page_size

### Breaking Changes

  - Client name is changed from `RecoveryServicesDataReplicationMgmtClient` to `DataReplicationClient`
  - Model HyperVToAzStackHCIProtectedItemModelCustomProperties has a new required parameter source_fabric_agent_name
  - Model HyperVToAzStackHCIProtectedItemModelCustomProperties has a new required parameter target_fabric_agent_name
  - Model HyperVToAzStackHCIProtectedItemModelCustomProperties no longer has parameter source_dra_name
  - Model HyperVToAzStackHCIProtectedItemModelCustomProperties no longer has parameter target_dra_name
  - Model ProtectedItemModelProperties no longer has parameter dra_id
  - Model ProtectedItemModelProperties no longer has parameter target_dra_id
  - Model TaskModel no longer has parameter children_workflows
  - Model VMwareToAzStackHCIProtectedItemModelCustomProperties has a new required parameter source_fabric_agent_name
  - Model VMwareToAzStackHCIProtectedItemModelCustomProperties has a new required parameter target_fabric_agent_name
  - Model VMwareToAzStackHCIProtectedItemModelCustomProperties no longer has parameter source_dra_name
  - Model VMwareToAzStackHCIProtectedItemModelCustomProperties no longer has parameter target_dra_name
  - Operation EmailConfigurationOperations.create has a new required parameter resource
  - Operation EmailConfigurationOperations.create no longer has parameter body
  - Operation EventOperations.list no longer has parameter filter
  - Operation FabricOperations.begin_create has a new required parameter resource
  - Operation FabricOperations.begin_create no longer has parameter body
  - Operation FabricOperations.begin_update has a new required parameter properties
  - Operation FabricOperations.begin_update no longer has parameter body
  - Operation FabricOperations.list_by_subscription no longer has parameter continuation_token_parameter
  - Operation PolicyOperations.begin_create has a new required parameter resource
  - Operation PolicyOperations.begin_create no longer has parameter body
  - Operation ProtectedItemOperations.begin_create has a new required parameter resource
  - Operation ProtectedItemOperations.begin_create no longer has parameter body
  - Operation ReplicationExtensionOperations.begin_create has a new required parameter resource
  - Operation ReplicationExtensionOperations.begin_create no longer has parameter body
  - Operation VaultOperations.begin_create has a new required parameter resource
  - Operation VaultOperations.begin_create no longer has parameter body
  - Operation VaultOperations.begin_update has a new required parameter properties
  - Operation VaultOperations.begin_update no longer has parameter body
  - Operation VaultOperations.list_by_subscription no longer has parameter continuation_token_parameter
  - Removed operation group DraOperationStatusOperations
  - Removed operation group DraOperations
  - Removed operation group FabricOperationsStatusOperations
  - Removed operation group PolicyOperationStatusOperations
  - Removed operation group ProtectedItemOperationStatusOperations
  - Removed operation group RecoveryPointsOperations
  - Removed operation group RecoveryServicesDataReplicationMgmtClientOperationsMixin
  - Removed operation group ReplicationExtensionOperationStatusOperations
  - Removed operation group VaultOperationStatusOperations
  - Removed operation group WorkflowOperationStatusOperations
  - Removed operation group WorkflowOperations

## 1.0.0b1 (2023-10-23)

* Initial Release
