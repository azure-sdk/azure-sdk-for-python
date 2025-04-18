# Release History

## 1.0.0b4 (2025-04-18)

### Features Added

  - Client `AgriFoodMgmtClient` added operation group `check_name_availability`
  - Client `AgriFoodMgmtClient` added operation group `data_connectors`
  - Client `AgriFoodMgmtClient` added operation group `data_manager_for_agriculture_extensions`
  - Client `AgriFoodMgmtClient` added operation group `data_manager_for_agriculture_resources`
  - Client `AgriFoodMgmtClient` added operation group `operation_results`
  - Model `ApiProperties` added property `api_freshness_time_in_minutes`
  - Model `ArmAsyncOperation` added property `error`
  - Model `DetailedInformation` added property `api_docs_link`
  - Model `DetailedInformation` added property `api_type`
  - Model `DetailedInformation` added property `api_default_input_parameters`
  - Model `ExtensionListResponse` added property `skip_token`
  - Enum `ProvisioningState` added member `RUNNING`
  - Enum `PublicNetworkAccess` added member `DISABLED`
  - Model `SolutionProperties` added property `role_assignment_id`
  - Added model `ApiKeyAuthCredentials`
  - Added model `ArmAsyncOperationError`
  - Added model `AuthCredentials`
  - Added enum `AuthCredentialsKind`
  - Added model `DataConnector`
  - Added model `DataConnectorListResponse`
  - Added model `DataConnectorProperties`
  - Added model `DataManagerForAgriculture`
  - Added model `DataManagerForAgricultureExtension`
  - Added model `DataManagerForAgricultureExtensionListResponse`
  - Added model `DataManagerForAgricultureExtensionProperties`
  - Added model `DataManagerForAgricultureListResponse`
  - Added model `DataManagerForAgricultureSolution`
  - Added model `DataManagerForAgricultureSolutionListResponse`
  - Added model `DataManagerForAgricultureSolutionProperties`
  - Added model `DataManagerForAgricultureUpdateProperties`
  - Added model `DataManagerForAgricultureUpdateRequestModel`
  - Added model `KeyVaultProperties`
  - Added model `OAuthClientCredentials`
  - Model `ExtensionsOperations` added method `list_by_data_manager_for_agriculture`
  - Added model `CheckNameAvailabilityOperations`
  - Added model `DataConnectorsOperations`
  - Added model `DataManagerForAgricultureExtensionsOperations`
  - Added model `DataManagerForAgricultureResourcesOperations`
  - Added model `OperationResultsOperations`
  - Method `ExtensionsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, data_manager_for_agriculture_resource_name: str, extension_id: str, request_body: Optional[ExtensionInstallationRequest], content_type: str)`
  - Method `ExtensionsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, data_manager_for_agriculture_resource_name: str, extension_id: str, request_body: Optional[IO[bytes]], content_type: str)`
  - Method `PrivateEndpointConnectionsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, data_manager_for_agriculture_resource_name: str, private_endpoint_connection_name: str, request: PrivateEndpointConnection, content_type: str)`
  - Method `PrivateEndpointConnectionsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, data_manager_for_agriculture_resource_name: str, private_endpoint_connection_name: str, request: IO[bytes], content_type: str)`
  - Method `SolutionsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, data_manager_for_agriculture_resource_name: str, solution_id: str, request_body: Optional[Solution], content_type: str)`
  - Method `SolutionsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, data_manager_for_agriculture_resource_name: str, solution_id: str, request_body: Optional[IO[bytes]], content_type: str)`
  - Method `CheckNameAvailabilityOperations.check_name_availability` has a new overload `def check_name_availability(self: None, name_availability_request: CheckNameAvailabilityRequest, content_type: str)`
  - Method `CheckNameAvailabilityOperations.check_name_availability` has a new overload `def check_name_availability(self: None, name_availability_request: IO[bytes], content_type: str)`
  - Method `DataConnectorsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, data_manager_for_agriculture_resource_name: str, data_connector_name: str, body: DataConnector, content_type: str)`
  - Method `DataConnectorsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, data_manager_for_agriculture_resource_name: str, data_connector_name: str, body: IO[bytes], content_type: str)`
  - Method `DataManagerForAgricultureResourcesOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, data_manager_for_agriculture_resource_name: str, request: DataManagerForAgricultureUpdateRequestModel, content_type: str)`
  - Method `DataManagerForAgricultureResourcesOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, data_manager_for_agriculture_resource_name: str, request: IO[bytes], content_type: str)`
  - Method `DataManagerForAgricultureResourcesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, data_manager_for_agriculture_resource_name: str, request: DataManagerForAgriculture, content_type: str)`
  - Method `DataManagerForAgricultureResourcesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, data_manager_for_agriculture_resource_name: str, request: IO[bytes], content_type: str)`

### Breaking Changes

  - Deleted or renamed client operation group `AgriFoodMgmtClient.farm_beats_extensions`
  - Deleted or renamed client operation group `AgriFoodMgmtClient.farm_beats_models`
  - Deleted or renamed client operation group `AgriFoodMgmtClient.locations`
  - Method `AgriFoodMgmtClient.__init__` parameter `base_url` changed default value from `str` to `none`
  - Method `AgriFoodMgmtClient.__init__` deleted or renamed its parameter `solution_id` of kind `positional_or_keyword`
  - Method `PrivateEndpointConnectionsOperations.list_by_resource` changed from `synchronous` to `asynchronous`
  - Method `PrivateLinkResourcesOperations.list_by_resource` changed from `synchronous` to `asynchronous`
  - Model `ApiProperties` deleted or renamed its instance variable `api_freshness_window_in_minutes`
  - Method `ExtensionListResponse.__init__` removed default value `None` from its parameter `value`
  - Deleted or renamed enum value `PublicNetworkAccess.HYBRID`
  - Method `SolutionListResponse.__init__` removed default value `None` from its parameter `value`
  - Model `SolutionProperties` deleted or renamed its instance variable `solution_id`
  - Deleted or renamed model `FarmBeats`
  - Deleted or renamed model `FarmBeatsExtension`
  - Deleted or renamed model `FarmBeatsExtensionListResponse`
  - Deleted or renamed model `FarmBeatsListResponse`
  - Deleted or renamed model `FarmBeatsSolution`
  - Deleted or renamed model `FarmBeatsSolutionListResponse`
  - Deleted or renamed model `FarmBeatsSolutionProperties`
  - Deleted or renamed model `FarmBeatsUpdateProperties`
  - Deleted or renamed model `FarmBeatsUpdateRequestModel`
  - Deleted or renamed model `Insight`
  - Deleted or renamed model `InsightAttachment`
  - Deleted or renamed model `Measure`
  - Deleted or renamed model `ResourceParameter`
  - Deleted or renamed model `SolutionEvaluatedOutput`
  - Deleted or renamed model `SolutionInstallationRequest`
  - Method `ExtensionsOperations.create_or_update` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `ExtensionsOperations.create_or_update` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Method `ExtensionsOperations.delete` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `ExtensionsOperations.delete` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Method `ExtensionsOperations.get` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `ExtensionsOperations.get` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Deleted or renamed method `ExtensionsOperations.list_by_farm_beats`
  - Method `PrivateEndpointConnectionsOperations.begin_delete` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `PrivateEndpointConnectionsOperations.begin_delete` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Method `PrivateEndpointConnectionsOperations.create_or_update` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `PrivateEndpointConnectionsOperations.create_or_update` inserted a `positional_or_keyword` parameter `request`
  - Method `PrivateEndpointConnectionsOperations.create_or_update` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Method `PrivateEndpointConnectionsOperations.create_or_update` deleted or renamed its parameter `body` of kind `positional_or_keyword`
  - Method `PrivateEndpointConnectionsOperations.get` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `PrivateEndpointConnectionsOperations.get` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Method `PrivateEndpointConnectionsOperations.list_by_resource` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `PrivateEndpointConnectionsOperations.list_by_resource` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Method `PrivateLinkResourcesOperations.get` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `PrivateLinkResourcesOperations.get` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Method `PrivateLinkResourcesOperations.list_by_resource` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `PrivateLinkResourcesOperations.list_by_resource` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Method `SolutionsDiscoverabilityOperations.get` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_solution_id`
  - Method `SolutionsDiscoverabilityOperations.get` deleted or renamed its parameter `farm_beats_solution_id` of kind `positional_or_keyword`
  - Method `SolutionsOperations.create_or_update` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `SolutionsOperations.create_or_update` inserted a `positional_or_keyword` parameter `solution_id`
  - Method `SolutionsOperations.create_or_update` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Method `SolutionsOperations.create_or_update` deleted or renamed its parameter `body` of kind `positional_or_keyword`
  - Method `SolutionsOperations.delete` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `SolutionsOperations.delete` inserted a `positional_or_keyword` parameter `solution_id`
  - Method `SolutionsOperations.delete` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Method `SolutionsOperations.get` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `SolutionsOperations.get` inserted a `positional_or_keyword` parameter `solution_id`
  - Method `SolutionsOperations.get` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Method `SolutionsOperations.list` inserted a `positional_or_keyword` parameter `data_manager_for_agriculture_resource_name`
  - Method `SolutionsOperations.list` deleted or renamed its parameter `farm_beats_resource_name` of kind `positional_or_keyword`
  - Deleted or renamed model `FarmBeatsExtensionsOperations`
  - Deleted or renamed model `FarmBeatsModelsOperations`
  - Deleted or renamed model `LocationsOperations`
  - Method `SolutionsDiscoverabilityOperations.get` re-ordered its parameters from `['self', 'farm_beats_solution_id', 'kwargs']` to `['self', 'data_manager_for_agriculture_solution_id', 'kwargs']`
  - Method `SolutionsOperations.list` re-ordered its parameters from `['self', 'resource_group_name', 'farm_beats_resource_name', 'solution_ids', 'ids', 'names', 'property_filters', 'statuses', 'min_created_date_time', 'max_created_date_time', 'min_last_modified_date_time', 'max_last_modified_date_time', 'max_page_size', 'skip_token', 'kwargs']` to `['self', 'resource_group_name', 'data_manager_for_agriculture_resource_name', 'solution_ids', 'ids', 'names', 'property_filters', 'statuses', 'min_created_date_time', 'max_created_date_time', 'min_last_modified_date_time', 'max_last_modified_date_time', 'max_page_size', 'skip_token', 'kwargs']`
  - Method `ExtensionsOperations.get` re-ordered its parameters from `['self', 'resource_group_name', 'farm_beats_resource_name', 'extension_id', 'kwargs']` to `['self', 'resource_group_name', 'data_manager_for_agriculture_resource_name', 'extension_id', 'kwargs']`
  - Method `ExtensionsOperations.delete` re-ordered its parameters from `['self', 'resource_group_name', 'farm_beats_resource_name', 'extension_id', 'kwargs']` to `['self', 'resource_group_name', 'data_manager_for_agriculture_resource_name', 'extension_id', 'kwargs']`
  - Method `ExtensionsOperations.create_or_update` re-ordered its parameters from `['self', 'resource_group_name', 'farm_beats_resource_name', 'extension_id', 'request_body', 'kwargs']` to `['self', 'resource_group_name', 'data_manager_for_agriculture_resource_name', 'extension_id', 'request_body', 'kwargs']`
  - Method `PrivateEndpointConnectionsOperations.begin_delete` re-ordered its parameters from `['self', 'resource_group_name', 'farm_beats_resource_name', 'private_endpoint_connection_name', 'kwargs']` to `['self', 'resource_group_name', 'data_manager_for_agriculture_resource_name', 'private_endpoint_connection_name', 'kwargs']`
  - Method `PrivateEndpointConnectionsOperations.list_by_resource` re-ordered its parameters from `['self', 'resource_group_name', 'farm_beats_resource_name', 'kwargs']` to `['self', 'resource_group_name', 'data_manager_for_agriculture_resource_name', 'kwargs']`
  - Method `PrivateEndpointConnectionsOperations.get` re-ordered its parameters from `['self', 'resource_group_name', 'farm_beats_resource_name', 'private_endpoint_connection_name', 'kwargs']` to `['self', 'resource_group_name', 'data_manager_for_agriculture_resource_name', 'private_endpoint_connection_name', 'kwargs']`
  - Method `PrivateEndpointConnectionsOperations.create_or_update` re-ordered its parameters from `['self', 'resource_group_name', 'farm_beats_resource_name', 'private_endpoint_connection_name', 'body', 'kwargs']` to `['self', 'resource_group_name', 'data_manager_for_agriculture_resource_name', 'private_endpoint_connection_name', 'request', 'kwargs']`
  - Method `PrivateLinkResourcesOperations.list_by_resource` re-ordered its parameters from `['self', 'resource_group_name', 'farm_beats_resource_name', 'kwargs']` to `['self', 'resource_group_name', 'data_manager_for_agriculture_resource_name', 'kwargs']`
  - Method `PrivateLinkResourcesOperations.get` re-ordered its parameters from `['self', 'resource_group_name', 'farm_beats_resource_name', 'sub_resource_name', 'kwargs']` to `['self', 'resource_group_name', 'data_manager_for_agriculture_resource_name', 'sub_resource_name', 'kwargs']`

## 1.0.0b3 (2022-12-26)

### Features Added

  - Added operation ExtensionsOperations.create_or_update
  - Added operation group SolutionsDiscoverabilityOperations
  - Added operation group SolutionsOperations
  - Model Extension has a new parameter additional_api_properties
  - Model PrivateEndpointConnection has a new parameter group_ids

### Breaking Changes

  - Removed operation ExtensionsOperations.create
  - Removed operation ExtensionsOperations.update

## 1.0.0b2 (2022-09-02)

### Features Added

  - Added operation FarmBeatsModelsOperations.begin_update
  - Added operation FarmBeatsModelsOperations.get_operation_result
  - Added operation group PrivateEndpointConnectionsOperations
  - Added operation group PrivateLinkResourcesOperations
  - Model FarmBeats has a new parameter identity
  - Model FarmBeats has a new parameter private_endpoint_connections
  - Model FarmBeats has a new parameter public_network_access
  - Model FarmBeats has a new parameter sensor_integration
  - Model FarmBeatsUpdateRequestModel has a new parameter identity
  - Model FarmBeatsUpdateRequestModel has a new parameter properties
  - Model ProxyResource has a new parameter system_data
  - Model Resource has a new parameter system_data
  - Model TrackedResource has a new parameter system_data

### Breaking Changes

  - Client name is changed to `AgriFoodMgmtClient`
  - Removed operation FarmBeatsModelsOperations.update

## 1.0.0b1 (2021-06-09)

* Initial Release

