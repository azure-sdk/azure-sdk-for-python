# Release History

## 2.0.0b1 (2025-04-18)

### Features Added

  - Client `ApiCenterMgmtClient` added operation group `deleted_services`
  - Client `ApiCenterMgmtClient` added operation group `api_sources`
  - Model `Api` added property `title`
  - Model `Api` added property `kind`
  - Model `Api` added property `description`
  - Model `Api` added property `summary`
  - Model `Api` added property `lifecycle_stage`
  - Model `Api` added property `terms_of_service`
  - Model `Api` added property `external_documentation`
  - Model `Api` added property `contacts`
  - Model `Api` added property `license`
  - Model `Api` added property `custom_properties`
  - Model `ApiDefinition` added property `title`
  - Model `ApiDefinition` added property `description`
  - Model `ApiDefinition` added property `specification`
  - Model `ApiVersion` added property `title`
  - Model `ApiVersion` added property `lifecycle_stage`
  - Model `Deployment` added property `title`
  - Model `Deployment` added property `description`
  - Model `Deployment` added property `environment_id`
  - Model `Deployment` added property `definition_id`
  - Model `Deployment` added property `state`
  - Model `Deployment` added property `server`
  - Model `Deployment` added property `custom_properties`
  - Model `Environment` added property `title`
  - Model `Environment` added property `description`
  - Model `Environment` added property `kind`
  - Model `Environment` added property `server`
  - Model `Environment` added property `onboarding`
  - Model `Environment` added property `custom_properties`
  - Model `MetadataSchema` added property `schema`
  - Model `MetadataSchema` added property `assigned_to`
  - Model `Service` added property `provisioning_state`
  - Model `Service` added property `restore`
  - Model `ServiceUpdate` added property `restore`
  - Model `Workspace` added property `title`
  - Model `Workspace` added property `description`
  - Added model `ApiSource`
  - Added enum `ApiSourceLinkState`
  - Added model `ApiSourceListResult`
  - Added model `AzureApiManagementSource`
  - Added model `DeletedService`
  - Added model `DeletedServiceListResult`
  - Added enum `ImportSpecificationOptions`
  - Added model `LinkState`
  - Added model `ApiSourcesOperations`
  - Added model `DeletedServicesOperations`
  - Method `ApiDefinitionsOperations.begin_import_specification` has a new overload `def begin_import_specification(self: None, resource_group_name: str, service_name: str, workspace_name: str, api_name: str, version_name: str, definition_name: str, body: IO[bytes], content_type: str)`
  - Method `ApiDefinitionsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, service_name: str, workspace_name: str, api_name: str, version_name: str, definition_name: str, resource: IO[bytes], content_type: str)`
  - Method `ApiVersionsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, service_name: str, workspace_name: str, api_name: str, version_name: str, resource: IO[bytes], content_type: str)`
  - Method `ApisOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, service_name: str, workspace_name: str, api_name: str, resource: IO[bytes], content_type: str)`
  - Method `DeploymentsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, service_name: str, workspace_name: str, api_name: str, deployment_name: str, resource: IO[bytes], content_type: str)`
  - Method `EnvironmentsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, service_name: str, workspace_name: str, environment_name: str, resource: IO[bytes], content_type: str)`
  - Method `MetadataSchemasOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, service_name: str, metadata_schema_name: str, resource: IO[bytes], content_type: str)`
  - Method `ServicesOperations.begin_export_metadata_schema` has a new overload `def begin_export_metadata_schema(self: None, resource_group_name: str, service_name: str, body: IO[bytes], content_type: str)`
  - Method `ServicesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, service_name: str, resource: IO[bytes], content_type: str)`
  - Method `ServicesOperations.update` has a new overload `def update(self: None, resource_group_name: str, service_name: str, properties: IO[bytes], content_type: str)`
  - Method `WorkspacesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, service_name: str, workspace_name: str, resource: IO[bytes], content_type: str)`
  - Method `ApiSourcesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, service_name: str, workspace_name: str, api_source_name: str, resource: ApiSource, content_type: str)`
  - Method `ApiSourcesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, service_name: str, workspace_name: str, api_source_name: str, resource: IO[bytes], content_type: str)`

### Breaking Changes

  - Method `ApiCenterMgmtClient.__init__` parameter `base_url` changed default value from `str` to `none`
  - Model `Api` deleted or renamed its instance variable `properties`
  - Model `ApiDefinition` deleted or renamed its instance variable `properties`
  - Model `ApiVersion` deleted or renamed its instance variable `properties`
  - Model `Deployment` deleted or renamed its instance variable `properties`
  - Model `Environment` deleted or renamed its instance variable `properties`
  - Model `MetadataSchema` deleted or renamed its instance variable `properties`
  - Model `Service` deleted or renamed its instance variable `properties`
  - Model `Workspace` deleted or renamed its instance variable `properties`
  - Deleted or renamed model `ApiDefinitionProperties`
  - Deleted or renamed model `ApiProperties`
  - Deleted or renamed model `ApiVersionProperties`
  - Deleted or renamed model `DeploymentProperties`
  - Deleted or renamed model `EnvironmentProperties`
  - Deleted or renamed model `MetadataSchemaProperties`
  - Deleted or renamed model `ServiceProperties`
  - Deleted or renamed model `Versions`
  - Deleted or renamed model `WorkspaceProperties`

## 1.0.0 (2024-02-19)

### Features Added

  - Added operation ServicesOperations.begin_export_metadata_schema
  - Added operation group ApiDefinitionsOperations
  - Added operation group ApiVersionsOperations
  - Added operation group ApisOperations
  - Added operation group DeploymentsOperations
  - Added operation group EnvironmentsOperations
  - Added operation group MetadataSchemasOperations
  - Added operation group WorkspacesOperations
  - Model Service has a new parameter properties
  - Model ServiceUpdate has a new parameter identity
  - Model ServiceUpdate has a new parameter tags

### Breaking Changes

  - Model Service no longer has parameter provisioning_state
  - Model ServiceUpdate no longer has parameter provisioning_state
  - Operation ServicesOperations.update has a new required parameter properties
  - Operation ServicesOperations.update no longer has parameter parameters

## 1.0.0b1 (2023-08-25)

* Initial Release
