# Release History

## 2.0.0 (2025-04-11)

### Features Added

  - Client `InformaticaDataMgmtClient` added method `send_request`
  - Method `AdvancedCustomProperties.__init__` has a new overload `def __init__(self: None, key: Optional[str], value: Optional[str])`
  - Method `AdvancedCustomProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ApplicationConfigs.__init__` has a new overload `def __init__(self: None, type: str, name: str, value: str, platform: str, customized: str, default_value: str)`
  - Method `ApplicationConfigs.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ApplicationTypeMetadata.__init__` has a new overload `def __init__(self: None, name: Optional[str], value: Optional[str])`
  - Method `ApplicationTypeMetadata.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CdiConfigProps.__init__` has a new overload `def __init__(self: None, engine_name: str, engine_version: str, application_configs: List[_models.ApplicationConfigs])`
  - Method `CdiConfigProps.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CheckDependenciesResponse.__init__` has a new overload `def __init__(self: None, count: int, id: str, references: List[_models.ServerlessRuntimeDependency])`
  - Method `CheckDependenciesResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CompanyDetails.__init__` has a new overload `def __init__(self: None, company_name: Optional[str], office_address: Optional[str], country: Optional[str], domain: Optional[str], business: Optional[str], number_of_employees: Optional[int])`
  - Method `CompanyDetails.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CompanyDetailsUpdate.__init__` has a new overload `def __init__(self: None, company_name: Optional[str], office_address: Optional[str], country: Optional[str], domain: Optional[str], business: Optional[str], number_of_employees: Optional[int])`
  - Method `CompanyDetailsUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ComputeUnitsMetadata.__init__` has a new overload `def __init__(self: None, name: Optional[str], value: Optional[List[str]])`
  - Method `ComputeUnitsMetadata.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ErrorResponse.__init__` has a new overload `def __init__(self: None, error: Optional[_models.ErrorDetail])`
  - Method `ErrorResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `InfaRuntimeResourceFetchMetaData.__init__` has a new overload `def __init__(self: None, name: str, created_time: str, updated_time: str, created_by: str, updated_by: str, id: str, type: Union[str, _models.RuntimeType], status: str, status_localized: str, status_message: str, serverless_config_properties: _models.InfaServerlessFetchConfigProperties, description: Optional[str])`
  - Method `InfaRuntimeResourceFetchMetaData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `InfaServerlessFetchConfigProperties.__init__` has a new overload `def __init__(self: None, subnet: Optional[str], application_type: Optional[str], resource_group_name: Optional[str], advanced_custom_properties: Optional[str], supplementary_file_location: Optional[str], platform: Optional[str], tags: Optional[str], vnet: Optional[str], execution_timeout: Optional[str], compute_units: Optional[str], tenant_id: Optional[str], subscription_id: Optional[str], region: Optional[str], serverless_arm_resource_id: Optional[str])`
  - Method `InfaServerlessFetchConfigProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `InformaticaOrganizationResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]], properties: Optional[_models.OrganizationProperties])`
  - Method `InformaticaOrganizationResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `InformaticaOrganizationResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `InformaticaOrganizationResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `InformaticaOrganizationResourceUpdate.__init__` has a new overload `def __init__(self: None, tags: Optional[Dict[str, str]], properties: Optional[_models.OrganizationPropertiesCustomUpdate])`
  - Method `InformaticaOrganizationResourceUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `InformaticaProperties.__init__` has a new overload `def __init__(self: None, organization_id: Optional[str], organization_name: Optional[str], informatica_region: Optional[str], single_sign_on_url: Optional[str])`
  - Method `InformaticaProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `InformaticaServerlessRuntimeProperties.__init__` has a new overload `def __init__(self: None, serverless_account_location: str, description: Optional[str], platform: Optional[Union[str, _models.PlatformType]], application_type: Optional[Union[str, _models.ApplicationType]], compute_units: Optional[str], execution_timeout: Optional[str], serverless_runtime_network_profile: Optional[_models.ServerlessRuntimeNetworkProfile], advanced_custom_properties: Optional[List[_models.AdvancedCustomProperties]], supplementary_file_location: Optional[str], serverless_runtime_config: Optional[_models.ServerlessRuntimeConfigProperties], serverless_runtime_tags: Optional[List[_models.ServerlessRuntimeTag]], serverless_runtime_user_context_properties: Optional[_models.ServerlessRuntimeUserContextProperties])`
  - Method `InformaticaServerlessRuntimeProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `InformaticaServerlessRuntimeResource.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.InformaticaServerlessRuntimeProperties])`
  - Method `InformaticaServerlessRuntimeResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `InformaticaServerlessRuntimeResourceList.__init__` has a new overload `def __init__(self: None, informatica_runtime_resources: List[_models.InfaRuntimeResourceFetchMetaData])`
  - Method `InformaticaServerlessRuntimeResourceList.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `InformaticaServerlessRuntimeResourceUpdate.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.ServerlessRuntimePropertiesCustomUpdate])`
  - Method `InformaticaServerlessRuntimeResourceUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `LinkOrganization.__init__` has a new overload `def __init__(self: None, token: Optional[str])`
  - Method `LinkOrganization.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `MarketplaceDetails.__init__` has a new overload `def __init__(self: None, offer_details: _models.OfferDetails, marketplace_subscription_id: Optional[str])`
  - Method `MarketplaceDetails.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `MarketplaceDetailsUpdate.__init__` has a new overload `def __init__(self: None, marketplace_subscription_id: Optional[str], offer_details: Optional[_models.OfferDetailsUpdate])`
  - Method `MarketplaceDetailsUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `NetworkInterfaceConfiguration.__init__` has a new overload `def __init__(self: None, vnet_id: str, subnet_id: str, vnet_resource_guid: Optional[str])`
  - Method `NetworkInterfaceConfiguration.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `NetworkInterfaceConfigurationUpdate.__init__` has a new overload `def __init__(self: None, vnet_id: Optional[str], subnet_id: Optional[str], vnet_resource_guid: Optional[str])`
  - Method `NetworkInterfaceConfigurationUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OfferDetails.__init__` has a new overload `def __init__(self: None, publisher_id: str, offer_id: str, plan_id: str, plan_name: str, term_id: str, term_unit: Optional[str])`
  - Method `OfferDetails.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OfferDetailsUpdate.__init__` has a new overload `def __init__(self: None, publisher_id: Optional[str], offer_id: Optional[str], plan_id: Optional[str], plan_name: Optional[str], term_unit: Optional[str], term_id: Optional[str])`
  - Method `OfferDetailsUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OrganizationProperties.__init__` has a new overload `def __init__(self: None, informatica_properties: Optional[_models.InformaticaProperties], marketplace_details: Optional[_models.MarketplaceDetails], user_details: Optional[_models.UserDetails], company_details: Optional[_models.CompanyDetails], link_organization: Optional[_models.LinkOrganization])`
  - Method `OrganizationProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OrganizationPropertiesCustomUpdate.__init__` has a new overload `def __init__(self: None, informatica_organization_properties: Optional[_models.InformaticaOrganizationResourceUpdate], marketplace_details: Optional[_models.MarketplaceDetailsUpdate], user_details: Optional[_models.UserDetailsUpdate], company_details: Optional[_models.CompanyDetailsUpdate], existing_resource_id: Optional[str])`
  - Method `OrganizationPropertiesCustomUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `RegionsMetadata.__init__` has a new overload `def __init__(self: None, id: Optional[str], name: Optional[str])`
  - Method `RegionsMetadata.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerlessConfigProperties.__init__` has a new overload `def __init__(self: None, platform: Optional[Union[str, _models.PlatformType]], application_types: Optional[List[_models.ApplicationTypeMetadata]], compute_units: Optional[List[_models.ComputeUnitsMetadata]], execution_timeout: Optional[str], regions: Optional[List[_models.RegionsMetadata]])`
  - Method `ServerlessConfigProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerlessMetadataResponse.__init__` has a new overload `def __init__(self: None, type: Optional[Union[str, _models.RuntimeType]], serverless_config_properties: Optional[_models.ServerlessConfigProperties], serverless_runtime_config_properties: Optional[_models.ServerlessRuntimeConfigProperties])`
  - Method `ServerlessMetadataResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerlessRuntimeConfigProperties.__init__` has a new overload `def __init__(self: None, cdi_config_props: Optional[List[_models.CdiConfigProps]], cdie_config_props: Optional[List[_models.CdiConfigProps]])`
  - Method `ServerlessRuntimeConfigProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerlessRuntimeConfigPropertiesUpdate.__init__` has a new overload `def __init__(self: None, cdi_config_props: Optional[List[_models.CdiConfigProps]], cdie_config_props: Optional[List[_models.CdiConfigProps]])`
  - Method `ServerlessRuntimeConfigPropertiesUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerlessRuntimeDependency.__init__` has a new overload `def __init__(self: None, id: str, app_context_id: str, path: str, document_type: str, description: str, last_updated_time: str)`
  - Method `ServerlessRuntimeDependency.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerlessRuntimeNetworkProfile.__init__` has a new overload `def __init__(self: None, network_interface_configuration: _models.NetworkInterfaceConfiguration)`
  - Method `ServerlessRuntimeNetworkProfile.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerlessRuntimeNetworkProfileUpdate.__init__` has a new overload `def __init__(self: None, network_interface_configuration: _models.NetworkInterfaceConfigurationUpdate)`
  - Method `ServerlessRuntimeNetworkProfileUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerlessRuntimePropertiesCustomUpdate.__init__` has a new overload `def __init__(self: None, description: Optional[str], platform: Optional[Union[str, _models.PlatformType]], application_type: Optional[Union[str, _models.ApplicationType]], compute_units: Optional[str], execution_timeout: Optional[str], serverless_account_location: Optional[str], serverless_runtime_network_profile: Optional[_models.ServerlessRuntimeNetworkProfileUpdate], advanced_custom_properties: Optional[List[_models.AdvancedCustomProperties]], supplementary_file_location: Optional[str], serverless_runtime_config: Optional[_models.ServerlessRuntimeConfigPropertiesUpdate], serverless_runtime_tags: Optional[List[_models.ServerlessRuntimeTag]], serverless_runtime_user_context_properties: Optional[_models.ServerlessRuntimeUserContextPropertiesUpdate])`
  - Method `ServerlessRuntimePropertiesCustomUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerlessRuntimeTag.__init__` has a new overload `def __init__(self: None, name: Optional[str], value: Optional[str])`
  - Method `ServerlessRuntimeTag.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerlessRuntimeUserContextProperties.__init__` has a new overload `def __init__(self: None, user_context_token: str)`
  - Method `ServerlessRuntimeUserContextProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ServerlessRuntimeUserContextPropertiesUpdate.__init__` has a new overload `def __init__(self: None, user_context_token: Optional[str])`
  - Method `ServerlessRuntimeUserContextPropertiesUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, created_by: Optional[str], created_by_type: Optional[Union[str, _models.CreatedByType]], created_at: Optional[datetime], last_modified_by: Optional[str], last_modified_by_type: Optional[Union[str, _models.CreatedByType]], last_modified_at: Optional[datetime])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `UserDetails.__init__` has a new overload `def __init__(self: None, first_name: Optional[str], last_name: Optional[str], email_address: Optional[str], upn: Optional[str], phone_number: Optional[str])`
  - Method `UserDetails.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `UserDetailsUpdate.__init__` has a new overload `def __init__(self: None, first_name: Optional[str], last_name: Optional[str], email_address: Optional[str], upn: Optional[str], phone_number: Optional[str])`
  - Method `UserDetailsUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OrganizationsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, organization_name: str, resource: JSON, content_type: str)`
  - Method `OrganizationsOperations.update` has a new overload `def update(self: None, resource_group_name: str, organization_name: str, properties: JSON, content_type: str)`
  - Method `ServerlessRuntimesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, organization_name: str, serverless_runtime_name: str, resource: JSON, content_type: str)`
  - Method `ServerlessRuntimesOperations.update` has a new overload `def update(self: None, resource_group_name: str, organization_name: str, serverless_runtime_name: str, properties: JSON, content_type: str)`

### Breaking Changes

  - Model `AdvancedCustomProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ApplicationConfigs` deleted or renamed its instance variable `additional_properties`
  - Model `ApplicationTypeMetadata` deleted or renamed its instance variable `additional_properties`
  - Model `CdiConfigProps` deleted or renamed its instance variable `additional_properties`
  - Model `CheckDependenciesResponse` deleted or renamed its instance variable `additional_properties`
  - Model `CompanyDetails` deleted or renamed its instance variable `additional_properties`
  - Model `CompanyDetailsUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `ComputeUnitsMetadata` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorAdditionalInfo` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorDetail` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorResponse` deleted or renamed its instance variable `additional_properties`
  - Model `InfaRuntimeResourceFetchMetaData` deleted or renamed its instance variable `additional_properties`
  - Model `InfaServerlessFetchConfigProperties` deleted or renamed its instance variable `additional_properties`
  - Model `InformaticaOrganizationResource` deleted or renamed its instance variable `additional_properties`
  - Model `InformaticaOrganizationResourceUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `InformaticaProperties` deleted or renamed its instance variable `additional_properties`
  - Model `InformaticaServerlessRuntimeProperties` deleted or renamed its instance variable `additional_properties`
  - Model `InformaticaServerlessRuntimeResource` deleted or renamed its instance variable `additional_properties`
  - Model `InformaticaServerlessRuntimeResourceList` deleted or renamed its instance variable `additional_properties`
  - Model `InformaticaServerlessRuntimeResourceUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `LinkOrganization` deleted or renamed its instance variable `additional_properties`
  - Model `MarketplaceDetails` deleted or renamed its instance variable `additional_properties`
  - Model `MarketplaceDetailsUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `NetworkInterfaceConfiguration` deleted or renamed its instance variable `additional_properties`
  - Model `NetworkInterfaceConfigurationUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `OfferDetails` deleted or renamed its instance variable `additional_properties`
  - Model `OfferDetailsUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `OrganizationProperties` deleted or renamed its instance variable `additional_properties`
  - Model `OrganizationPropertiesCustomUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `ProxyResource` deleted or renamed its instance variable `additional_properties`
  - Model `RegionsMetadata` deleted or renamed its instance variable `additional_properties`
  - Model `Resource` deleted or renamed its instance variable `additional_properties`
  - Model `ServerlessConfigProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ServerlessMetadataResponse` deleted or renamed its instance variable `additional_properties`
  - Model `ServerlessRuntimeConfigProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ServerlessRuntimeConfigPropertiesUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `ServerlessRuntimeDependency` deleted or renamed its instance variable `additional_properties`
  - Model `ServerlessRuntimeNetworkProfile` deleted or renamed its instance variable `additional_properties`
  - Model `ServerlessRuntimeNetworkProfileUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `ServerlessRuntimePropertiesCustomUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `ServerlessRuntimeTag` deleted or renamed its instance variable `additional_properties`
  - Model `ServerlessRuntimeUserContextProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ServerlessRuntimeUserContextPropertiesUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `SystemData` deleted or renamed its instance variable `additional_properties`
  - Model `TrackedResource` deleted or renamed its instance variable `additional_properties`
  - Model `UserDetails` deleted or renamed its instance variable `additional_properties`
  - Model `UserDetailsUpdate` deleted or renamed its instance variable `additional_properties`
  - Deleted or renamed model `ActionType`
  - Deleted or renamed model `Operation`
  - Deleted or renamed model `OperationDisplay`
  - Deleted or renamed model `Origin`
  - Deleted or renamed method `Operations.list`

## 1.0.0 (2024-07-15)

### Features Added

  - Added model InformaticaOrganizationResourceListResult
  - Added model InformaticaServerlessRuntimeResourceListResult
  - Added model OperationListResult

## 1.0.0b1 (2024-05-29)

- Initial version
