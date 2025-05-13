# Release History

## 3.0.0 (2025-05-13)

### Features Added

  - Client `QumuloMgmtClient` added method `send_request`
  - Model `FileSystemResource` added property `properties`
  - Added model `FileSystemResourceProperties`
  - Method `ErrorResponse.__init__` has a new overload `def __init__(self: None, error: Optional[_models.ErrorDetail])`
  - Method `ErrorResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `FileSystemResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]], properties: Optional[_models.FileSystemResourceProperties], identity: Optional[_models.ManagedServiceIdentity])`
  - Method `FileSystemResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `FileSystemResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `FileSystemResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `FileSystemResourceUpdate.__init__` has a new overload `def __init__(self: None, identity: Optional[_models.ManagedServiceIdentity], tags: Optional[Dict[str, str]], properties: Optional[_models.FileSystemResourceUpdateProperties])`
  - Method `FileSystemResourceUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `FileSystemResourceUpdateProperties.__init__` has a new overload `def __init__(self: None, marketplace_details: Optional[_models.MarketplaceDetails], user_details: Optional[_models.UserDetails], delegated_subnet_id: Optional[str])`
  - Method `FileSystemResourceUpdateProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ManagedServiceIdentity.__init__` has a new overload `def __init__(self: None, type: Union[str, _models.ManagedServiceIdentityType], user_assigned_identities: Optional[Dict[str, _models.UserAssignedIdentity]])`
  - Method `ManagedServiceIdentity.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `MarketplaceDetails.__init__` has a new overload `def __init__(self: None, plan_id: str, offer_id: str, marketplace_subscription_id: Optional[str], publisher_id: Optional[str], term_unit: Optional[str])`
  - Method `MarketplaceDetails.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, display: Optional[_models.OperationDisplay])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, created_by: Optional[str], created_by_type: Optional[Union[str, _models.CreatedByType]], created_at: Optional[datetime], last_modified_by: Optional[str], last_modified_by_type: Optional[Union[str, _models.CreatedByType]], last_modified_at: Optional[datetime])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `UserDetails.__init__` has a new overload `def __init__(self: None, email: str)`
  - Method `UserDetails.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `FileSystemResourceProperties.__init__` has a new overload `def __init__(self: None, marketplace_details: _models.MarketplaceDetails, storage_sku: str, user_details: _models.UserDetails, delegated_subnet_id: str, admin_password: str, cluster_login_url: Optional[str], private_i_ps: Optional[List[str]], availability_zone: Optional[str])`
  - Method `FileSystemResourceProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `FileSystemsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, file_system_name: str, resource: JSON, content_type: str)`
  - Method `FileSystemsOperations.update` has a new overload `def update(self: None, resource_group_name: str, file_system_name: str, properties: JSON, content_type: str)`

### Breaking Changes

  - Model `ErrorAdditionalInfo` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorDetail` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorResponse` deleted or renamed its instance variable `additional_properties`
  - Model `FileSystemResource` deleted or renamed its instance variable `marketplace_details`
  - Model `FileSystemResource` deleted or renamed its instance variable `provisioning_state`
  - Model `FileSystemResource` deleted or renamed its instance variable `storage_sku`
  - Model `FileSystemResource` deleted or renamed its instance variable `user_details`
  - Model `FileSystemResource` deleted or renamed its instance variable `delegated_subnet_id`
  - Model `FileSystemResource` deleted or renamed its instance variable `cluster_login_url`
  - Model `FileSystemResource` deleted or renamed its instance variable `private_ips`
  - Model `FileSystemResource` deleted or renamed its instance variable `admin_password`
  - Model `FileSystemResource` deleted or renamed its instance variable `availability_zone`
  - Model `FileSystemResource` deleted or renamed its instance variable `additional_properties`
  - Model `FileSystemResourceUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `FileSystemResourceUpdateProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ManagedServiceIdentity` deleted or renamed its instance variable `additional_properties`
  - Model `MarketplaceDetails` deleted or renamed its instance variable `additional_properties`
  - Model `Operation` deleted or renamed its instance variable `additional_properties`
  - Model `OperationDisplay` deleted or renamed its instance variable `additional_properties`
  - Model `Resource` deleted or renamed its instance variable `additional_properties`
  - Model `SystemData` deleted or renamed its instance variable `additional_properties`
  - Model `TrackedResource` deleted or renamed its instance variable `additional_properties`
  - Model `UserAssignedIdentity` deleted or renamed its instance variable `additional_properties`
  - Model `UserDetails` deleted or renamed its instance variable `additional_properties`

## 1.0.0b1 (1970-01-01)

- Initial version
