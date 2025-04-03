# Release History

## 1.1.0 (2025-04-03)

### Features Added

  - Model `Organization` added property `open_access`
  - Model `PoolImage` added property `ephemeral_type`
  - Model `SecretsManagementSettings` added property `certificate_store_name`
  - Added enum `ActionType`
  - Added enum `AvailabilityStatus`
  - Added enum `CertificateStoreNameOption`
  - Added model `CheckNameAvailability`
  - Added enum `CheckNameAvailabilityReason`
  - Added model `CheckNameAvailabilityResult`
  - Added enum `DevOpsInfrastructureResourceType`
  - Added enum `EphemeralType`
  - Added model `Operation`
  - Added model `OperationDisplay`
  - Added enum `Origin`
  - Model `PoolsOperations` added method `check_name_availability`
  - Method `Organization.__init__` has a new overload `def __init__(self: None, url: str, projects: Optional[List[str]], parallelism: Optional[int], open_access: Optional[bool])`
  - Method `PoolImage.__init__` has a new overload `def __init__(self: None, resource_id: Optional[str], well_known_image_name: Optional[str], aliases: Optional[List[str]], buffer: Optional[str], ephemeral_type: Optional[Union[str, _models.EphemeralType]])`
  - Method `SecretsManagementSettings.__init__` has a new overload `def __init__(self: None, observed_certificates: List[str], key_exportable: bool, certificate_store_location: Optional[str], certificate_store_name: Optional[Union[str, _models.CertificateStoreNameOption]])`
  - Method `CheckNameAvailability.__init__` has a new overload `def __init__(self: None, name: str, type: Union[str, _models.DevOpsInfrastructureResourceType])`
  - Method `CheckNameAvailability.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CheckNameAvailabilityResult.__init__` has a new overload `def __init__(self: None, available: Union[str, _models.AvailabilityStatus], message: str, name: str, reason: Union[str, _models.CheckNameAvailabilityReason])`
  - Method `CheckNameAvailabilityResult.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, display: Optional[_models.OperationDisplay])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `PoolsOperations.check_name_availability` has a new overload `def check_name_availability(self: None, body: CheckNameAvailability, content_type: str)`
  - Method `PoolsOperations.check_name_availability` has a new overload `def check_name_availability(self: None, body: JSON, content_type: str)`
  - Method `PoolsOperations.check_name_availability` has a new overload `def check_name_availability(self: None, body: IO[bytes], content_type: str)`

## 1.0.0 (2024-11-21)

### Features Added

  - Model `Quota` added property `unit`
  - Model `Quota` added property `current_value`
  - Model `Quota` added property `limit`
  - Operation group `SubscriptionUsagesOperations` added method `usages`

### Breaking Changes

  - Enum `ManagedServiceIdentityType` renamed its value `SYSTEM_AND_USER_ASSIGNED` to `SYSTEM_ASSIGNED_USER_ASSIGNED`
  - Enum `OsDiskStorageAccountType` renamed its value `STANDARD_S_S_D` to `STANDARD_SSD`
  - Model `Quota` deleted or renamed its instance variable `properties`
  - Model `Quota` deleted or renamed its instance variable `type`
  - Model `Quota` deleted or renamed its instance variable `system_data`
  - Deleted or renamed enum value `StorageAccountType.PREMIUM_L_R_S`
  - Deleted or renamed enum value `StorageAccountType.PREMIUM_Z_R_S`
  - Deleted or renamed enum value `StorageAccountType.STANDARD_L_R_S`
  - Deleted or renamed enum value `StorageAccountType.STANDARD_S_S_D_L_R_S`
  - Deleted or renamed enum value `StorageAccountType.STANDARD_S_S_D_Z_R_S`
  - Deleted or renamed model `ActionType`
  - Deleted or renamed model `Operation`
  - Deleted or renamed model `OperationDisplay`
  - Deleted or renamed model `Origin`
  - Deleted or renamed model `QuotaProperties`
  - Deleted or renamed method `SubscriptionUsagesOperations.list_by_location`

## 1.0.0b1 (2024-05-29)

- Initial version
