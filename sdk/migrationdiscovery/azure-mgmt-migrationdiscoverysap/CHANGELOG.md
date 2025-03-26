# Release History

## 1.0.0b2 (2025-03-26)

### Features Added

  - Client `MigrationDiscoverySapMgmtClient` added method `send_request`
  - Added model `SAPDiscoverySitesOperations`
  - Added model `SAPInstancesOperations`
  - Method `ErrorResponse.__init__` has a new overload `def __init__(self: None, error: Optional[_models.ErrorDetail])`
  - Method `ErrorResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ExcelPerformanceData.__init__` has a new overload `def __init__(self: None)`
  - Method `ExcelPerformanceData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ExcelPerformanceData.__init__` has a new overload `def __init__(self: None, data_source: str)`
  - Method `ExcelPerformanceData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ExtendedLocation.__init__` has a new overload `def __init__(self: None, type: str, name: str)`
  - Method `ExtendedLocation.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `NativePerformanceData.__init__` has a new overload `def __init__(self: None)`
  - Method `NativePerformanceData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `NativePerformanceData.__init__` has a new overload `def __init__(self: None, data_source: str)`
  - Method `NativePerformanceData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OperationStatusResult.__init__` has a new overload `def __init__(self: None, status: str, id: Optional[str], name: Optional[str], percent_complete: Optional[float], start_time: Optional[datetime], end_time: Optional[datetime], operations: Optional[List[_models.OperationStatusResult]], error: Optional[_models.ErrorDetail])`
  - Method `OperationStatusResult.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `PerformanceData.__init__` has a new overload `def __init__(self: None, data_source: str)`
  - Method `PerformanceData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SAPDiscoverySite.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]], properties: Optional[_models.SAPDiscoverySiteProperties], extended_location: Optional[_models.ExtendedLocation])`
  - Method `SAPDiscoverySite.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SAPDiscoverySite.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `SAPDiscoverySite.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SAPDiscoverySiteProperties.__init__` has a new overload `def __init__(self: None, master_site_id: Optional[str], migrate_project_id: Optional[str])`
  - Method `SAPDiscoverySiteProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SAPDiscoverySiteTagsUpdate.__init__` has a new overload `def __init__(self: None, tags: Optional[Dict[str, str]])`
  - Method `SAPDiscoverySiteTagsUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SAPInstance.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]], properties: Optional[_models.SAPInstanceProperties])`
  - Method `SAPInstance.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SAPInstance.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `SAPInstance.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SAPInstanceTagsUpdate.__init__` has a new overload `def __init__(self: None, tags: Optional[Dict[str, str]])`
  - Method `SAPInstanceTagsUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SAPMigrateError.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.ErrorDefinition])`
  - Method `SAPMigrateError.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerInstance.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.ServerInstanceProperties])`
  - Method `ServerInstance.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, created_by: Optional[str], created_by_type: Optional[Union[str, _models.CreatedByType]], created_at: Optional[datetime], last_modified_by: Optional[str], last_modified_by_type: Optional[Union[str, _models.CreatedByType]], last_modified_at: Optional[datetime])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `UpdateServerInstanceRequest.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.ServerInstanceProperties])`
  - Method `UpdateServerInstanceRequest.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerInstancesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, server_instance_name: str, resource: IO[bytes], content_type: str)`
  - Method `ServerInstancesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, server_instance_name: str, resource: JSON, content_type: str)`
  - Method `ServerInstancesOperations.update` has a new overload `def update(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, server_instance_name: str, properties: IO[bytes], content_type: str)`
  - Method `ServerInstancesOperations.update` has a new overload `def update(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, server_instance_name: str, properties: JSON, content_type: str)`
  - Method `SAPDiscoverySitesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, sap_discovery_site_name: str, resource: SAPDiscoverySite, content_type: str)`
  - Method `SAPDiscoverySitesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, sap_discovery_site_name: str, resource: JSON, content_type: str)`
  - Method `SAPDiscoverySitesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, sap_discovery_site_name: str, resource: IO[bytes], content_type: str)`
  - Method `SAPDiscoverySitesOperations.update` has a new overload `def update(self: None, resource_group_name: str, sap_discovery_site_name: str, properties: SAPDiscoverySiteTagsUpdate, content_type: str)`
  - Method `SAPDiscoverySitesOperations.update` has a new overload `def update(self: None, resource_group_name: str, sap_discovery_site_name: str, properties: JSON, content_type: str)`
  - Method `SAPDiscoverySitesOperations.update` has a new overload `def update(self: None, resource_group_name: str, sap_discovery_site_name: str, properties: IO[bytes], content_type: str)`
  - Method `SAPInstancesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, resource: SAPInstance, content_type: str)`
  - Method `SAPInstancesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, resource: JSON, content_type: str)`
  - Method `SAPInstancesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, resource: IO[bytes], content_type: str)`
  - Method `SAPInstancesOperations.update` has a new overload `def update(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, properties: SAPInstanceTagsUpdate, content_type: str)`
  - Method `SAPInstancesOperations.update` has a new overload `def update(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, properties: JSON, content_type: str)`
  - Method `SAPInstancesOperations.update` has a new overload `def update(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, properties: IO[bytes], content_type: str)`

### Breaking Changes

  - Deleted or renamed client operation group `MigrationDiscoverySapMgmtClient.operations`
  - Model `ConfigurationData` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorAdditionalInfo` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorDefinition` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorDetail` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorResponse` deleted or renamed its instance variable `additional_properties`
  - Model `ExcelPerformanceData` deleted or renamed its instance variable `additional_properties`
  - Model `ExtendedLocation` deleted or renamed its instance variable `additional_properties`
  - Model `NativePerformanceData` deleted or renamed its instance variable `additional_properties`
  - Model `OperationStatusResult` deleted or renamed its instance variable `additional_properties`
  - Model `PerformanceData` deleted or renamed its instance variable `additional_properties`
  - Model `ProxyResource` deleted or renamed its instance variable `additional_properties`
  - Model `Resource` deleted or renamed its instance variable `additional_properties`
  - Model `SAPDiscoverySite` deleted or renamed its instance variable `additional_properties`
  - Model `SAPDiscoverySiteProperties` deleted or renamed its instance variable `additional_properties`
  - Model `SAPDiscoverySiteTagsUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `SAPInstance` deleted or renamed its instance variable `additional_properties`
  - Model `SAPInstanceProperties` deleted or renamed its instance variable `additional_properties`
  - Model `SAPInstanceTagsUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `SAPMigrateError` deleted or renamed its instance variable `additional_properties`
  - Model `ServerInstance` deleted or renamed its instance variable `additional_properties`
  - Model `ServerInstanceProperties` deleted or renamed its instance variable `additional_properties`
  - Model `SystemData` deleted or renamed its instance variable `additional_properties`
  - Model `TrackedResource` deleted or renamed its instance variable `additional_properties`
  - Model `UpdateServerInstanceRequest` deleted or renamed its instance variable `additional_properties`
  - Deleted or renamed model `ActionType`
  - Deleted or renamed model `Operation`
  - Deleted or renamed model `OperationDisplay`
  - Deleted or renamed model `Origin`
  - Deleted or renamed model `Versions`
  - Deleted or renamed model `Operations`
  - Deleted or renamed model `SapDiscoverySitesOperations`
  - Deleted or renamed model `SapInstancesOperations`

## 1.0.0b1 (2024-04-07)

* Initial Release
