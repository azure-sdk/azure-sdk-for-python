# Release History

## 1.2.0 (2025-04-11)

### Features Added

  - Model `AvailabilitySetResourceSettings` added property `target_subscription_id`
  - Model `DiskEncryptionSetResourceSettings` added property `target_subscription_id`
  - Model `KeyVaultResourceSettings` added property `target_subscription_id`
  - Model `LoadBalancerResourceSettings` added property `target_subscription_id`
  - Model `NetworkInterfaceResourceSettings` added property `target_subscription_id`
  - Model `NetworkSecurityGroupResourceSettings` added property `target_subscription_id`
  - Model `PublicIPAddressResourceSettings` added property `target_subscription_id`
  - Model `ResourceGroupResourceSettings` added property `target_subscription_id`
  - Model `ResourceSettings` added property `target_subscription_id`
  - Model `SqlDatabaseResourceSettings` added property `target_subscription_id`
  - Model `SqlElasticPoolResourceSettings` added property `target_subscription_id`
  - Model `SqlServerResourceSettings` added property `target_subscription_id`
  - Model `VirtualMachineResourceSettings` added property `target_disk_details`
  - Model `VirtualMachineResourceSettings` added property `target_subscription_id`
  - Model `VirtualNetworkResourceSettings` added property `target_subscription_id`
  - Added model `DiskDetails`
  - Method `MoveCollectionsOperations.begin_bulk_remove` has a new overload `def begin_bulk_remove(self: None, resource_group_name: str, move_collection_name: str, body: Optional[IO[bytes]], content_type: str)`
  - Method `MoveCollectionsOperations.begin_commit` has a new overload `def begin_commit(self: None, resource_group_name: str, move_collection_name: str, body: Optional[IO[bytes]], content_type: str)`
  - Method `MoveCollectionsOperations.begin_discard` has a new overload `def begin_discard(self: None, resource_group_name: str, move_collection_name: str, body: Optional[IO[bytes]], content_type: str)`
  - Method `MoveCollectionsOperations.begin_initiate_move` has a new overload `def begin_initiate_move(self: None, resource_group_name: str, move_collection_name: str, body: Optional[IO[bytes]], content_type: str)`
  - Method `MoveCollectionsOperations.begin_prepare` has a new overload `def begin_prepare(self: None, resource_group_name: str, move_collection_name: str, body: Optional[IO[bytes]], content_type: str)`
  - Method `MoveCollectionsOperations.create` has a new overload `def create(self: None, resource_group_name: str, move_collection_name: str, body: Optional[IO[bytes]], content_type: str)`
  - Method `MoveCollectionsOperations.update` has a new overload `def update(self: None, resource_group_name: str, move_collection_name: str, body: Optional[IO[bytes]], content_type: str)`
  - Method `MoveResourcesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, move_collection_name: str, move_resource_name: str, body: Optional[IO[bytes]], content_type: str)`

## 1.1.0 (2023-10-23)

### Features Added

  - Model AvailabilitySetResourceSettings has a new parameter tags
  - Model AvailabilitySetResourceSettings has a new parameter target_resource_group_name
  - Model DiskEncryptionSetResourceSettings has a new parameter target_resource_group_name
  - Model KeyVaultResourceSettings has a new parameter target_resource_group_name
  - Model LoadBalancerResourceSettings has a new parameter tags
  - Model LoadBalancerResourceSettings has a new parameter target_resource_group_name
  - Model MoveCollection has a new parameter system_data
  - Model MoveCollectionProperties has a new parameter move_region
  - Model MoveCollectionProperties has a new parameter move_type
  - Model MoveCollectionProperties has a new parameter version
  - Model MoveResource has a new parameter system_data
  - Model NetworkInterfaceResourceSettings has a new parameter tags
  - Model NetworkInterfaceResourceSettings has a new parameter target_resource_group_name
  - Model NetworkSecurityGroupResourceSettings has a new parameter tags
  - Model NetworkSecurityGroupResourceSettings has a new parameter target_resource_group_name
  - Model PublicIPAddressResourceSettings has a new parameter tags
  - Model PublicIPAddressResourceSettings has a new parameter target_resource_group_name
  - Model ResourceGroupResourceSettings has a new parameter target_resource_group_name
  - Model ResourceSettings has a new parameter target_resource_group_name
  - Model SqlDatabaseResourceSettings has a new parameter tags
  - Model SqlDatabaseResourceSettings has a new parameter target_resource_group_name
  - Model SqlElasticPoolResourceSettings has a new parameter tags
  - Model SqlElasticPoolResourceSettings has a new parameter target_resource_group_name
  - Model SqlServerResourceSettings has a new parameter target_resource_group_name
  - Model VirtualMachineResourceSettings has a new parameter tags
  - Model VirtualMachineResourceSettings has a new parameter target_resource_group_name
  - Model VirtualMachineResourceSettings has a new parameter user_managed_identities
  - Model VirtualNetworkResourceSettings has a new parameter tags
  - Model VirtualNetworkResourceSettings has a new parameter target_resource_group_name

## 1.1.0b3 (2022-11-04)

### Features Added

  - Model AvailabilitySetResourceSettings has a new parameter tags
  - Model LoadBalancerResourceSettings has a new parameter tags
  - Model MoveCollection has a new parameter system_data
  - Model MoveResource has a new parameter system_data
  - Model NetworkInterfaceResourceSettings has a new parameter tags
  - Model NetworkSecurityGroupResourceSettings has a new parameter tags
  - Model PublicIPAddressResourceSettings has a new parameter tags
  - Model SqlDatabaseResourceSettings has a new parameter tags
  - Model SqlElasticPoolResourceSettings has a new parameter tags
  - Model VirtualMachineResourceSettings has a new parameter tags
  - Model VirtualMachineResourceSettings has a new parameter user_managed_identities
  - Model VirtualNetworkResourceSettings has a new parameter tags

## 1.1.0b2 (2021-05-24)

  - Models rename

## 1.1.0b1 (2021-03-09)

* version number change

## 1.0.0 (2021-02-19)

* GA release

## 1.0.0b2 (2021-02-03)

* Initial Release
