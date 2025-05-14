# Release History

## 2.0.0 (2025-05-14)

### Features Added

  - Client `AzureSphereMgmtClient` added method `send_request`
  - Method `Catalog.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]], properties: Optional[_models.CatalogProperties])`
  - Method `Catalog.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Catalog.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `Catalog.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CatalogUpdate.__init__` has a new overload `def __init__(self: None, tags: Optional[Dict[str, str]])`
  - Method `CatalogUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Certificate.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.CertificateProperties])`
  - Method `Certificate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ClaimDevicesRequest.__init__` has a new overload `def __init__(self: None, device_identifiers: List[str])`
  - Method `ClaimDevicesRequest.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CountDevicesResponse.__init__` has a new overload `def __init__(self: None, value: int)`
  - Method `CountDevicesResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CountDevicesResponse.__init__` has a new overload `def __init__(self: None, value: int)`
  - Method `CountDevicesResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CountElementsResponse.__init__` has a new overload `def __init__(self: None, value: int)`
  - Method `CountElementsResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Deployment.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.DeploymentProperties])`
  - Method `Deployment.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DeploymentProperties.__init__` has a new overload `def __init__(self: None, deployment_id: Optional[str], deployed_images: Optional[List[_models.Image]])`
  - Method `DeploymentProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Device.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.DeviceProperties])`
  - Method `Device.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DeviceGroup.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.DeviceGroupProperties])`
  - Method `DeviceGroup.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DeviceGroupProperties.__init__` has a new overload `def __init__(self: None, description: Optional[str], os_feed_type: Optional[Union[str, _models.OSFeedType]], update_policy: Optional[Union[str, _models.UpdatePolicy]], allow_crash_dumps_collection: Optional[Union[str, _models.AllowCrashDumpCollection]], regional_data_boundary: Optional[Union[str, _models.RegionalDataBoundary]])`
  - Method `DeviceGroupProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DeviceGroupUpdate.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.DeviceGroupUpdateProperties])`
  - Method `DeviceGroupUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DeviceGroupUpdateProperties.__init__` has a new overload `def __init__(self: None, description: Optional[str], os_feed_type: Optional[Union[str, _models.OSFeedType]], update_policy: Optional[Union[str, _models.UpdatePolicy]], allow_crash_dumps_collection: Optional[Union[str, _models.AllowCrashDumpCollection]], regional_data_boundary: Optional[Union[str, _models.RegionalDataBoundary]])`
  - Method `DeviceGroupUpdateProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DeviceInsight.__init__` has a new overload `def __init__(self: None, device_id: str, description: str, start_timestamp_utc: datetime, end_timestamp_utc: datetime, event_category: str, event_class: str, event_type: str, event_count: int)`
  - Method `DeviceInsight.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DeviceProperties.__init__` has a new overload `def __init__(self: None, device_id: Optional[str])`
  - Method `DeviceProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DeviceUpdate.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.DeviceUpdateProperties])`
  - Method `DeviceUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DeviceUpdateProperties.__init__` has a new overload `def __init__(self: None, device_group_id: Optional[str])`
  - Method `DeviceUpdateProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ErrorResponse.__init__` has a new overload `def __init__(self: None, error: Optional[_models.ErrorDetail])`
  - Method `ErrorResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `GenerateCapabilityImageRequest.__init__` has a new overload `def __init__(self: None, capabilities: List[Union[str, _models.CapabilityType]])`
  - Method `GenerateCapabilityImageRequest.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Image.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.ImageProperties])`
  - Method `Image.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ImageProperties.__init__` has a new overload `def __init__(self: None, image: Optional[str], image_id: Optional[str], regional_data_boundary: Optional[Union[str, _models.RegionalDataBoundary]])`
  - Method `ImageProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ListDeviceGroupsRequest.__init__` has a new overload `def __init__(self: None, device_group_name: Optional[str])`
  - Method `ListDeviceGroupsRequest.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, display: Optional[_models.OperationDisplay])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Product.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.ProductProperties])`
  - Method `Product.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ProductProperties.__init__` has a new overload `def __init__(self: None, description: Optional[str])`
  - Method `ProductProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ProductUpdate.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.ProductUpdateProperties])`
  - Method `ProductUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ProductUpdateProperties.__init__` has a new overload `def __init__(self: None, description: Optional[str])`
  - Method `ProductUpdateProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ProofOfPossessionNonceRequest.__init__` has a new overload `def __init__(self: None, proof_of_possession_nonce: str)`
  - Method `ProofOfPossessionNonceRequest.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, created_by: Optional[str], created_by_type: Optional[Union[str, _models.CreatedByType]], created_at: Optional[datetime], last_modified_by: Optional[str], last_modified_by_type: Optional[Union[str, _models.CreatedByType]], last_modified_at: Optional[datetime])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CatalogsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, catalog_name: str, resource: JSON, content_type: str)`
  - Method `CatalogsOperations.begin_upload_image` has a new overload `def begin_upload_image(self: None, resource_group_name: str, catalog_name: str, upload_image_request: JSON, content_type: str)`
  - Method `CatalogsOperations.list_device_groups` has a new overload `def list_device_groups(self: None, resource_group_name: str, catalog_name: str, list_device_groups_request: ListDeviceGroupsRequest, filter: Optional[str], top: Optional[int], skip: Optional[int], content_type: str)`
  - Method `CatalogsOperations.list_device_groups` has a new overload `def list_device_groups(self: None, resource_group_name: str, catalog_name: str, list_device_groups_request: IO[bytes], filter: Optional[str], top: Optional[int], skip: Optional[int], content_type: str)`
  - Method `CatalogsOperations.list_device_groups` has a new overload `def list_device_groups(self: None, resource_group_name: str, catalog_name: str, list_device_groups_request: JSON, filter: Optional[str], top: Optional[int], skip: Optional[int], content_type: str)`
  - Method `CatalogsOperations.update` has a new overload `def update(self: None, resource_group_name: str, catalog_name: str, properties: JSON, content_type: str)`
  - Method `CertificatesOperations.retrieve_proof_of_possession_nonce` has a new overload `def retrieve_proof_of_possession_nonce(self: None, resource_group_name: str, catalog_name: str, serial_number: str, proof_of_possession_nonce_request: JSON, content_type: str)`
  - Method `DeploymentsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, catalog_name: str, product_name: str, device_group_name: str, deployment_name: str, resource: JSON, content_type: str)`
  - Method `DeviceGroupsOperations.begin_claim_devices` has a new overload `def begin_claim_devices(self: None, resource_group_name: str, catalog_name: str, product_name: str, device_group_name: str, claim_devices_request: JSON, content_type: str)`
  - Method `DeviceGroupsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, catalog_name: str, product_name: str, device_group_name: str, resource: JSON, content_type: str)`
  - Method `DeviceGroupsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, catalog_name: str, product_name: str, device_group_name: str, properties: JSON, content_type: str)`
  - Method `DevicesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, catalog_name: str, product_name: str, device_group_name: str, device_name: str, resource: JSON, content_type: str)`
  - Method `DevicesOperations.begin_generate_capability_image` has a new overload `def begin_generate_capability_image(self: None, resource_group_name: str, catalog_name: str, product_name: str, device_group_name: str, device_name: str, generate_device_capability_request: JSON, content_type: str)`
  - Method `DevicesOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, catalog_name: str, product_name: str, device_group_name: str, device_name: str, properties: JSON, content_type: str)`
  - Method `ImagesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, catalog_name: str, image_name: str, resource: JSON, content_type: str)`
  - Method `ProductsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, catalog_name: str, product_name: str, resource: JSON, content_type: str)`
  - Method `ProductsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, catalog_name: str, product_name: str, properties: JSON, content_type: str)`

### Breaking Changes

  - Model `Catalog` deleted or renamed its instance variable `additional_properties`
  - Model `CatalogProperties` deleted or renamed its instance variable `additional_properties`
  - Model `CatalogUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `Certificate` deleted or renamed its instance variable `additional_properties`
  - Model `CertificateChainResponse` deleted or renamed its instance variable `additional_properties`
  - Model `CertificateProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ClaimDevicesRequest` deleted or renamed its instance variable `additional_properties`
  - Model `CountDevicesResponse` deleted or renamed its instance variable `additional_properties`
  - Model `CountElementsResponse` deleted or renamed its instance variable `additional_properties`
  - Model `Deployment` deleted or renamed its instance variable `additional_properties`
  - Model `DeploymentProperties` deleted or renamed its instance variable `additional_properties`
  - Model `Device` deleted or renamed its instance variable `additional_properties`
  - Model `DeviceGroup` deleted or renamed its instance variable `additional_properties`
  - Model `DeviceGroupProperties` deleted or renamed its instance variable `additional_properties`
  - Model `DeviceGroupUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `DeviceGroupUpdateProperties` deleted or renamed its instance variable `additional_properties`
  - Model `DeviceInsight` deleted or renamed its instance variable `additional_properties`
  - Model `DeviceProperties` deleted or renamed its instance variable `additional_properties`
  - Model `DeviceUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `DeviceUpdateProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorAdditionalInfo` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorDetail` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorResponse` deleted or renamed its instance variable `additional_properties`
  - Model `GenerateCapabilityImageRequest` deleted or renamed its instance variable `additional_properties`
  - Model `Image` deleted or renamed its instance variable `additional_properties`
  - Model `ImageProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ListDeviceGroupsRequest` deleted or renamed its instance variable `additional_properties`
  - Model `Operation` deleted or renamed its instance variable `additional_properties`
  - Model `OperationDisplay` deleted or renamed its instance variable `additional_properties`
  - Model `Product` deleted or renamed its instance variable `additional_properties`
  - Model `ProductProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ProductUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `ProductUpdateProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ProofOfPossessionNonceRequest` deleted or renamed its instance variable `additional_properties`
  - Model `ProofOfPossessionNonceResponse` deleted or renamed its instance variable `additional_properties`
  - Model `ProxyResource` deleted or renamed its instance variable `additional_properties`
  - Model `Resource` deleted or renamed its instance variable `additional_properties`
  - Model `SignedCapabilityImageResponse` deleted or renamed its instance variable `additional_properties`
  - Model `SystemData` deleted or renamed its instance variable `additional_properties`
  - Model `TrackedResource` deleted or renamed its instance variable `additional_properties`
  - Deleted or renamed model `CountDeviceResponse`
  - Deleted or renamed model `PagedDeviceInsight`

## 1.0.0 (2024-03-26)

### Features Added

  - Added operation CatalogsOperations.begin_upload_image
  - Model Catalog has a new parameter properties
  - Model Certificate has a new parameter properties
  - Model Deployment has a new parameter properties
  - Model Device has a new parameter properties
  - Model DeviceGroup has a new parameter properties
  - Model DeviceGroupUpdate has a new parameter properties
  - Model DeviceUpdate has a new parameter properties
  - Model Image has a new parameter properties
  - Model Product has a new parameter properties
  - Model ProductUpdate has a new parameter properties

### Breaking Changes

  - Model Catalog no longer has parameter provisioning_state
  - Model Certificate no longer has parameter certificate
  - Model Certificate no longer has parameter expiry_utc
  - Model Certificate no longer has parameter not_before_utc
  - Model Certificate no longer has parameter provisioning_state
  - Model Certificate no longer has parameter status
  - Model Certificate no longer has parameter subject
  - Model Certificate no longer has parameter thumbprint
  - Model Deployment no longer has parameter deployed_images
  - Model Deployment no longer has parameter deployment_date_utc
  - Model Deployment no longer has parameter deployment_id
  - Model Deployment no longer has parameter provisioning_state
  - Model Device no longer has parameter chip_sku
  - Model Device no longer has parameter device_id
  - Model Device no longer has parameter last_available_os_version
  - Model Device no longer has parameter last_installed_os_version
  - Model Device no longer has parameter last_os_update_utc
  - Model Device no longer has parameter last_update_request_utc
  - Model Device no longer has parameter provisioning_state
  - Model DeviceGroup no longer has parameter allow_crash_dumps_collection
  - Model DeviceGroup no longer has parameter description
  - Model DeviceGroup no longer has parameter has_deployment
  - Model DeviceGroup no longer has parameter os_feed_type
  - Model DeviceGroup no longer has parameter provisioning_state
  - Model DeviceGroup no longer has parameter regional_data_boundary
  - Model DeviceGroup no longer has parameter update_policy
  - Model DeviceGroupUpdate no longer has parameter allow_crash_dumps_collection
  - Model DeviceGroupUpdate no longer has parameter description
  - Model DeviceGroupUpdate no longer has parameter os_feed_type
  - Model DeviceGroupUpdate no longer has parameter regional_data_boundary
  - Model DeviceGroupUpdate no longer has parameter update_policy
  - Model DeviceUpdate no longer has parameter device_group_id
  - Model Image no longer has parameter component_id
  - Model Image no longer has parameter description
  - Model Image no longer has parameter image
  - Model Image no longer has parameter image_id
  - Model Image no longer has parameter image_name
  - Model Image no longer has parameter image_type
  - Model Image no longer has parameter provisioning_state
  - Model Image no longer has parameter regional_data_boundary
  - Model Image no longer has parameter uri
  - Model Product no longer has parameter description
  - Model Product no longer has parameter provisioning_state
  - Model ProductUpdate no longer has parameter description

## 1.0.0b1 (2023-07-21)

* Initial Release
