# Release History

## 1.0.0b2 (2025-04-23)

### Features Added

  - Method `SapDiscoverySitesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, sap_discovery_site_name: str, resource: IO[bytes], content_type: str)`
  - Method `SapDiscoverySitesOperations.update` has a new overload `def update(self: None, resource_group_name: str, sap_discovery_site_name: str, properties: IO[bytes], content_type: str)`
  - Method `SapInstancesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, resource: IO[bytes], content_type: str)`
  - Method `SapInstancesOperations.update` has a new overload `def update(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, properties: IO[bytes], content_type: str)`
  - Method `ServerInstancesOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, server_instance_name: str, resource: IO[bytes], content_type: str)`
  - Method `ServerInstancesOperations.update` has a new overload `def update(self: None, resource_group_name: str, sap_discovery_site_name: str, sap_instance_name: str, server_instance_name: str, properties: IO[bytes], content_type: str)`

### Breaking Changes

  - Deleted or renamed model `Versions`

## 1.0.0b1 (2024-04-07)

* Initial Release
