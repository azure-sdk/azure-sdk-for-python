# Release History

## 2.0.0 (2025-05-13)

### Features Added

  - Client `ChaosManagementClient` added method `send_request`
  - Client `ChaosManagementClient` added operation group `experiment_executions`
  - Model `Capability` added property `properties`
  - Model `CapabilityType` added property `properties`
  - Model `Experiment` added property `properties`
  - Model `ExperimentExecution` added property `properties`
  - Model `ExperimentExecution` added property `system_data`
  - Model `ExperimentExecutionDetails` added property `properties`
  - Model `Resource` added property `system_data`
  - Model `TargetType` added property `properties`
  - Model `TrackedResource` added property `system_data`
  - Added model `CapabilityProperties`
  - Added model `CapabilityTypeProperties`
  - Added enum `ExperimentActionType`
  - Added model `ExperimentProperties`
  - Added model `ManagedServiceIdentity`
  - Added enum `ManagedServiceIdentityType`
  - Added model `OperationStatusResult`
  - Added model `ProxyResource`
  - Added model `TargetTypeProperties`
  - Model `Operations` added method `list`
  - Added model `ExperimentExecutionsOperations`
  - Method `Capability.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.CapabilityProperties])`
  - Method `Capability.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CapabilityType.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.CapabilityTypeProperties])`
  - Method `CapabilityType.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ChaosExperimentAction.__init__` has a new overload `def __init__(self: None, name: str, type: str)`
  - Method `ChaosExperimentAction.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ChaosExperimentBranch.__init__` has a new overload `def __init__(self: None, name: str, actions: List[_models.ChaosExperimentAction])`
  - Method `ChaosExperimentBranch.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ChaosExperimentStep.__init__` has a new overload `def __init__(self: None, name: str, branches: List[_models.ChaosExperimentBranch])`
  - Method `ChaosExperimentStep.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ChaosTargetFilter.__init__` has a new overload `def __init__(self: None, type: str)`
  - Method `ChaosTargetFilter.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ChaosTargetListSelector.__init__` has a new overload `def __init__(self: None, id: str, targets: List[_models.TargetReference], filter: Optional[_models.ChaosTargetFilter])`
  - Method `ChaosTargetListSelector.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ChaosTargetListSelector.__init__` has a new overload `def __init__(self: None, id: str, type: str, filter: Optional[_models.ChaosTargetFilter])`
  - Method `ChaosTargetListSelector.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ChaosTargetQuerySelector.__init__` has a new overload `def __init__(self: None, id: str, query_string: str, subscription_ids: List[str], filter: Optional[_models.ChaosTargetFilter])`
  - Method `ChaosTargetQuerySelector.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ChaosTargetQuerySelector.__init__` has a new overload `def __init__(self: None, id: str, type: str, filter: Optional[_models.ChaosTargetFilter])`
  - Method `ChaosTargetQuerySelector.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ChaosTargetSelector.__init__` has a new overload `def __init__(self: None, id: str, type: str, filter: Optional[_models.ChaosTargetFilter])`
  - Method `ChaosTargetSelector.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ChaosTargetSimpleFilter.__init__` has a new overload `def __init__(self: None, parameters: Optional[_models.ChaosTargetSimpleFilterParameters])`
  - Method `ChaosTargetSimpleFilter.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ChaosTargetSimpleFilter.__init__` has a new overload `def __init__(self: None, type: str)`
  - Method `ChaosTargetSimpleFilter.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ChaosTargetSimpleFilterParameters.__init__` has a new overload `def __init__(self: None, zones: Optional[List[str]])`
  - Method `ChaosTargetSimpleFilterParameters.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ContinuousAction.__init__` has a new overload `def __init__(self: None, name: str, duration: timedelta, parameters: List[_models.KeyValuePair], selector_id: str)`
  - Method `ContinuousAction.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ContinuousAction.__init__` has a new overload `def __init__(self: None, name: str, type: str)`
  - Method `ContinuousAction.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DelayAction.__init__` has a new overload `def __init__(self: None, name: str, duration: timedelta)`
  - Method `DelayAction.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DelayAction.__init__` has a new overload `def __init__(self: None, name: str, type: str)`
  - Method `DelayAction.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DiscreteAction.__init__` has a new overload `def __init__(self: None, name: str, parameters: List[_models.KeyValuePair], selector_id: str)`
  - Method `DiscreteAction.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DiscreteAction.__init__` has a new overload `def __init__(self: None, name: str, type: str)`
  - Method `DiscreteAction.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ErrorResponse.__init__` has a new overload `def __init__(self: None, error: Optional[_models.ErrorDetail])`
  - Method `ErrorResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Experiment.__init__` has a new overload `def __init__(self: None, location: str, properties: _models.ExperimentProperties, tags: Optional[Dict[str, str]], identity: Optional[_models.ManagedServiceIdentity])`
  - Method `Experiment.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Experiment.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `Experiment.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ExperimentExecution.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.ExperimentExecutionProperties])`
  - Method `ExperimentExecution.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ExperimentUpdate.__init__` has a new overload `def __init__(self: None, tags: Optional[Dict[str, str]], identity: Optional[_models.ManagedServiceIdentity])`
  - Method `ExperimentUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `KeyValuePair.__init__` has a new overload `def __init__(self: None, key: str, value: str)`
  - Method `KeyValuePair.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, display: Optional[_models.OperationDisplay])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, created_by: Optional[str], created_by_type: Optional[Union[str, _models.CreatedByType]], created_at: Optional[datetime], last_modified_by: Optional[str], last_modified_by_type: Optional[Union[str, _models.CreatedByType]], last_modified_at: Optional[datetime])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Target.__init__` has a new overload `def __init__(self: None, properties: Dict[str, Any], location: Optional[str])`
  - Method `Target.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `TargetReference.__init__` has a new overload `def __init__(self: None, type: Union[str, _models.TargetReferenceType], id: str)`
  - Method `TargetReference.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `TargetType.__init__` has a new overload `def __init__(self: None, properties: _models.TargetTypeProperties)`
  - Method `TargetType.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ExperimentProperties.__init__` has a new overload `def __init__(self: None, steps: List[_models.ChaosExperimentStep], selectors: List[_models.ChaosTargetSelector])`
  - Method `ExperimentProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ManagedServiceIdentity.__init__` has a new overload `def __init__(self: None, type: Union[str, _models.ManagedServiceIdentityType], user_assigned_identities: Optional[Dict[str, _models.UserAssignedIdentity]])`
  - Method `ManagedServiceIdentity.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OperationStatusResult.__init__` has a new overload `def __init__(self: None, status: str, id: Optional[str], name: Optional[str], percent_complete: Optional[float], start_time: Optional[datetime], end_time: Optional[datetime], operations: Optional[List[_models.OperationStatusResult]], error: Optional[_models.ErrorDetail])`
  - Method `OperationStatusResult.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CapabilitiesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, parent_provider_namespace: str, parent_resource_type: str, parent_resource_name: str, target_name: str, capability_name: str, resource: JSON, content_type: str)`
  - Method `CapabilitiesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, parent_provider_namespace: str, parent_resource_type: str, parent_resource_name: str, target_name: str, capability_name: str, resource: IO[bytes], content_type: str)`
  - Method `CapabilitiesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, parent_provider_namespace: str, parent_resource_type: str, parent_resource_name: str, target_name: str, capability_name: str, resource: Capability, content_type: str)`
  - Method `ExperimentsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, experiment_name: str, resource: JSON, content_type: str)`
  - Method `ExperimentsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, experiment_name: str, resource: IO[bytes], content_type: str)`
  - Method `ExperimentsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, experiment_name: str, resource: Experiment, content_type: str)`
  - Method `ExperimentsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, experiment_name: str, properties: JSON, content_type: str)`
  - Method `ExperimentsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, experiment_name: str, properties: IO[bytes], content_type: str)`
  - Method `ExperimentsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, experiment_name: str, properties: ExperimentUpdate, content_type: str)`
  - Method `TargetsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, parent_provider_namespace: str, parent_resource_type: str, parent_resource_name: str, target_name: str, resource: JSON, content_type: str)`
  - Method `TargetsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, parent_provider_namespace: str, parent_resource_type: str, parent_resource_name: str, target_name: str, resource: IO[bytes], content_type: str)`
  - Method `TargetsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, parent_provider_namespace: str, parent_resource_type: str, parent_resource_name: str, target_name: str, resource: Target, content_type: str)`

### Breaking Changes

  - Model `ActionStatus` deleted or renamed its instance variable `additional_properties`
  - Model `BranchStatus` deleted or renamed its instance variable `additional_properties`
  - Model `Capability` deleted or renamed its instance variable `publisher`
  - Model `Capability` deleted or renamed its instance variable `target_type`
  - Model `Capability` deleted or renamed its instance variable `description`
  - Model `Capability` deleted or renamed its instance variable `parameters_schema`
  - Model `Capability` deleted or renamed its instance variable `urn`
  - Model `Capability` deleted or renamed its instance variable `additional_properties`
  - Model `CapabilityType` deleted or renamed its instance variable `location`
  - Model `CapabilityType` deleted or renamed its instance variable `publisher`
  - Model `CapabilityType` deleted or renamed its instance variable `target_type`
  - Model `CapabilityType` deleted or renamed its instance variable `display_name`
  - Model `CapabilityType` deleted or renamed its instance variable `description`
  - Model `CapabilityType` deleted or renamed its instance variable `parameters_schema`
  - Model `CapabilityType` deleted or renamed its instance variable `urn`
  - Model `CapabilityType` deleted or renamed its instance variable `kind`
  - Model `CapabilityType` deleted or renamed its instance variable `azure_rbac_actions`
  - Model `CapabilityType` deleted or renamed its instance variable `azure_rbac_data_actions`
  - Model `CapabilityType` deleted or renamed its instance variable `runtime_properties`
  - Model `CapabilityType` deleted or renamed its instance variable `additional_properties`
  - Model `CapabilityTypePropertiesRuntimeProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ChaosExperimentAction` deleted or renamed its instance variable `additional_properties`
  - Model `ChaosExperimentBranch` deleted or renamed its instance variable `additional_properties`
  - Model `ChaosExperimentStep` deleted or renamed its instance variable `additional_properties`
  - Model `ChaosTargetFilter` deleted or renamed its instance variable `additional_properties`
  - Model `ChaosTargetListSelector` deleted or renamed its instance variable `additional_properties`
  - Model `ChaosTargetQuerySelector` deleted or renamed its instance variable `additional_properties`
  - Model `ChaosTargetSelector` deleted or renamed its instance variable `additional_properties`
  - Model `ChaosTargetSimpleFilter` deleted or renamed its instance variable `additional_properties`
  - Model `ChaosTargetSimpleFilterParameters` deleted or renamed its instance variable `additional_properties`
  - Model `ContinuousAction` deleted or renamed its instance variable `additional_properties`
  - Model `DelayAction` deleted or renamed its instance variable `additional_properties`
  - Model `DiscreteAction` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorAdditionalInfo` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorDetail` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorResponse` deleted or renamed its instance variable `additional_properties`
  - Model `Experiment` deleted or renamed its instance variable `provisioning_state`
  - Model `Experiment` deleted or renamed its instance variable `steps`
  - Model `Experiment` deleted or renamed its instance variable `selectors`
  - Model `Experiment` deleted or renamed its instance variable `additional_properties`
  - Model `ExperimentExecution` deleted or renamed its instance variable `status`
  - Model `ExperimentExecution` deleted or renamed its instance variable `started_at`
  - Model `ExperimentExecution` deleted or renamed its instance variable `stopped_at`
  - Model `ExperimentExecution` deleted or renamed its instance variable `additional_properties`
  - Model `ExperimentExecutionActionTargetDetailsError` deleted or renamed its instance variable `additional_properties`
  - Model `ExperimentExecutionActionTargetDetailsProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ExperimentExecutionDetails` deleted or renamed its instance variable `status`
  - Model `ExperimentExecutionDetails` deleted or renamed its instance variable `started_at`
  - Model `ExperimentExecutionDetails` deleted or renamed its instance variable `stopped_at`
  - Model `ExperimentExecutionDetails` deleted or renamed its instance variable `failure_reason`
  - Model `ExperimentExecutionDetails` deleted or renamed its instance variable `last_action_at`
  - Model `ExperimentExecutionDetails` deleted or renamed its instance variable `run_information`
  - Model `ExperimentExecutionDetails` deleted or renamed its instance variable `additional_properties`
  - Model `ExperimentExecutionDetailsProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ExperimentExecutionDetailsPropertiesRunInformation` deleted or renamed its instance variable `additional_properties`
  - Model `ExperimentExecutionProperties` deleted or renamed its instance variable `additional_properties`
  - Model `ExperimentUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `KeyValuePair` deleted or renamed its instance variable `additional_properties`
  - Model `Operation` deleted or renamed its instance variable `additional_properties`
  - Model `OperationDisplay` deleted or renamed its instance variable `additional_properties`
  - Model `Resource` deleted or renamed its instance variable `additional_properties`
  - Model `StepStatus` deleted or renamed its instance variable `additional_properties`
  - Model `SystemData` deleted or renamed its instance variable `additional_properties`
  - Model `Target` deleted or renamed its instance variable `additional_properties`
  - Model `TargetReference` deleted or renamed its instance variable `additional_properties`
  - Model `TargetType` deleted or renamed its instance variable `location`
  - Model `TargetType` deleted or renamed its instance variable `display_name`
  - Model `TargetType` deleted or renamed its instance variable `description`
  - Model `TargetType` deleted or renamed its instance variable `properties_schema`
  - Model `TargetType` deleted or renamed its instance variable `resource_types`
  - Model `TargetType` deleted or renamed its instance variable `additional_properties`
  - Model `TrackedResource` deleted or renamed its instance variable `additional_properties`
  - Model `UserAssignedIdentity` deleted or renamed its instance variable `additional_properties`
  - Deleted or renamed model `OperationStatus`
  - Deleted or renamed model `ResourceIdentity`
  - Deleted or renamed model `ResourceIdentityType`
  - Method `CapabilitiesOperations.create_or_update` inserted a `positional_or_keyword` parameter `resource`
  - Method `CapabilitiesOperations.create_or_update` deleted or renamed its parameter `capability` of kind `positional_or_keyword`
  - Method `CapabilitiesOperations.list` changed its parameter `continuation_token_parameter` from `positional_or_keyword` to `keyword_only`
  - Method `CapabilityTypesOperations.get` inserted a `positional_or_keyword` parameter `location`
  - Method `CapabilityTypesOperations.get` deleted or renamed its parameter `location_name` of kind `positional_or_keyword`
  - Method `CapabilityTypesOperations.list` changed its parameter `continuation_token_parameter` from `positional_or_keyword` to `keyword_only`
  - Method `CapabilityTypesOperations.list` inserted a `positional_or_keyword` parameter `location`
  - Method `CapabilityTypesOperations.list` deleted or renamed its parameter `location_name` of kind `positional_or_keyword`
  - Method `ExperimentsOperations.begin_create_or_update` inserted a `positional_or_keyword` parameter `resource`
  - Method `ExperimentsOperations.begin_create_or_update` deleted or renamed its parameter `experiment` of kind `positional_or_keyword`
  - Method `ExperimentsOperations.begin_update` inserted a `positional_or_keyword` parameter `properties`
  - Method `ExperimentsOperations.begin_update` deleted or renamed its parameter `experiment` of kind `positional_or_keyword`
  - Method `ExperimentsOperations.list` changed its parameter `running` from `positional_or_keyword` to `keyword_only`
  - Method `ExperimentsOperations.list` changed its parameter `continuation_token_parameter` from `positional_or_keyword` to `keyword_only`
  - Method `ExperimentsOperations.list_all` changed its parameter `running` from `positional_or_keyword` to `keyword_only`
  - Method `ExperimentsOperations.list_all` changed its parameter `continuation_token_parameter` from `positional_or_keyword` to `keyword_only`
  - Deleted or renamed method `ExperimentsOperations.execution_details`
  - Deleted or renamed method `ExperimentsOperations.get_execution`
  - Deleted or renamed method `ExperimentsOperations.list_all_executions`
  - Method `OperationStatusesOperations.get` inserted a `positional_or_keyword` parameter `operation_id`
  - Method `OperationStatusesOperations.get` deleted or renamed its parameter `async_operation_id` of kind `positional_or_keyword`
  - Deleted or renamed method `Operations.list_all`
  - Method `TargetTypesOperations.get` inserted a `positional_or_keyword` parameter `location`
  - Method `TargetTypesOperations.get` deleted or renamed its parameter `location_name` of kind `positional_or_keyword`
  - Method `TargetTypesOperations.list` changed its parameter `continuation_token_parameter` from `positional_or_keyword` to `keyword_only`
  - Method `TargetTypesOperations.list` inserted a `positional_or_keyword` parameter `location`
  - Method `TargetTypesOperations.list` deleted or renamed its parameter `location_name` of kind `positional_or_keyword`
  - Method `TargetsOperations.create_or_update` inserted a `positional_or_keyword` parameter `resource`
  - Method `TargetsOperations.create_or_update` deleted or renamed its parameter `target` of kind `positional_or_keyword`
  - Method `TargetsOperations.list` changed its parameter `continuation_token_parameter` from `positional_or_keyword` to `keyword_only`
  - Method `ExperimentsOperations.begin_update` re-ordered its parameters from `['self', 'resource_group_name', 'experiment_name', 'experiment', 'kwargs']` to `['self', 'resource_group_name', 'experiment_name', 'properties', 'kwargs']`
  - Method `ExperimentsOperations.begin_create_or_update` re-ordered its parameters from `['self', 'resource_group_name', 'experiment_name', 'experiment', 'kwargs']` to `['self', 'resource_group_name', 'experiment_name', 'resource', 'kwargs']`
  - Method `OperationStatusesOperations.get` re-ordered its parameters from `['self', 'location', 'async_operation_id', 'kwargs']` to `['self', 'location', 'operation_id', 'kwargs']`
  - Method `TargetTypesOperations.list` re-ordered its parameters from `['self', 'location_name', 'continuation_token_parameter', 'kwargs']` to `['self', 'location', 'continuation_token_parameter', 'kwargs']`
  - Method `TargetTypesOperations.get` re-ordered its parameters from `['self', 'location_name', 'target_type_name', 'kwargs']` to `['self', 'location', 'target_type_name', 'kwargs']`
  - Method `CapabilitiesOperations.create_or_update` re-ordered its parameters from `['self', 'resource_group_name', 'parent_provider_namespace', 'parent_resource_type', 'parent_resource_name', 'target_name', 'capability_name', 'capability', 'kwargs']` to `['self', 'resource_group_name', 'parent_provider_namespace', 'parent_resource_type', 'parent_resource_name', 'target_name', 'capability_name', 'resource', 'kwargs']`
  - Method `TargetsOperations.create_or_update` re-ordered its parameters from `['self', 'resource_group_name', 'parent_provider_namespace', 'parent_resource_type', 'parent_resource_name', 'target_name', 'target', 'kwargs']` to `['self', 'resource_group_name', 'parent_provider_namespace', 'parent_resource_type', 'parent_resource_name', 'target_name', 'resource', 'kwargs']`
  - Method `CapabilityTypesOperations.list` re-ordered its parameters from `['self', 'location_name', 'target_type_name', 'continuation_token_parameter', 'kwargs']` to `['self', 'location', 'target_type_name', 'continuation_token_parameter', 'kwargs']`
  - Method `CapabilityTypesOperations.get` re-ordered its parameters from `['self', 'location_name', 'target_type_name', 'capability_type_name', 'kwargs']` to `['self', 'location', 'target_type_name', 'capability_type_name', 'kwargs']`

## 1.1.0 (2024-03-04)

### Features Added

  - Model ExperimentUpdate has a new parameter tags

## 1.0.0 (2023-11-20)

### Features Added

  - Added operation ExperimentsOperations.execution_details
  - Added operation ExperimentsOperations.get_execution
  - Added operation ExperimentsOperations.list_all_executions
  - Added operation group OperationStatusesOperations
  - Model Experiment has a new parameter provisioning_state
  - Model ExperimentExecutionDetails has a new parameter last_action_at
  - Model ExperimentExecutionDetails has a new parameter started_at
  - Model ExperimentExecutionDetails has a new parameter stopped_at

### Breaking Changes

  - Model Experiment no longer has parameter start_on_creation
  - Model ExperimentExecutionDetails no longer has parameter created_date_time
  - Model ExperimentExecutionDetails no longer has parameter experiment_id
  - Model ExperimentExecutionDetails no longer has parameter last_action_date_time
  - Model ExperimentExecutionDetails no longer has parameter start_date_time
  - Model ExperimentExecutionDetails no longer has parameter stop_date_time
  - Removed operation ExperimentsOperations.get_execution_details
  - Removed operation ExperimentsOperations.get_status
  - Removed operation ExperimentsOperations.list_all_statuses
  - Removed operation ExperimentsOperations.list_execution_details
  - Renamed operation ExperimentsOperations.cancel to ExperimentsOperations.begin_cancel
  - Renamed operation ExperimentsOperations.create_or_update to ExperimentsOperations.begin_create_or_update
  - Renamed operation ExperimentsOperations.delete to ExperimentsOperations.begin_delete
  - Renamed operation ExperimentsOperations.start to ExperimentsOperations.begin_start
  - Renamed operation ExperimentsOperations.update to ExperimentsOperations.begin_update

## 1.0.0b7 (2023-08-18)

### Features Added

  - Added operation ExperimentsOperations.update
  - Model CapabilityType has a new parameter azure_rbac_actions
  - Model CapabilityType has a new parameter azure_rbac_data_actions
  - Model ResourceIdentity has a new parameter user_assigned_identities
  - Model Selector has a new parameter additional_properties

### Breaking Changes

  - Model Selector no longer has parameter targets

## 1.0.0b6 (2022-12-14)

### Features Added

  - Model Selector has a new parameter filter

## 1.0.0b5 (2022-08-01)

**Features**

  - Added operation ExperimentsOperations.cancel
  - Added operation ExperimentsOperations.create_or_update
  - Model CapabilityType has a new parameter kind
  - Model CapabilityType has a new parameter runtime_properties

**Breaking changes**

  - Removed operation ExperimentsOperations.begin_cancel
  - Removed operation ExperimentsOperations.begin_create_or_update

## 1.0.0b4 (2022-06-28)

**Features**

  - Model ActionStatus has a new parameter action_id
  - Model ActionStatus has a new parameter action_name
  - Model BranchStatus has a new parameter branch_id
  - Model BranchStatus has a new parameter branch_name
  - Model ExperimentExecutionActionTargetDetailsProperties has a new parameter target_completed_time
  - Model ExperimentExecutionActionTargetDetailsProperties has a new parameter target_failed_time
  - Model ExperimentExecutionDetails has a new parameter created_date_time
  - Model ExperimentExecutionDetails has a new parameter last_action_date_time
  - Model ExperimentExecutionDetails has a new parameter start_date_time
  - Model ExperimentExecutionDetails has a new parameter stop_date_time
  - Model StepStatus has a new parameter step_id
  - Model StepStatus has a new parameter step_name

**Breaking changes**

  - Model ActionStatus no longer has parameter id
  - Model ActionStatus no longer has parameter name
  - Model BranchStatus no longer has parameter id
  - Model BranchStatus no longer has parameter name
  - Model ExperimentExecutionActionTargetDetailsProperties no longer has parameter completed_date_utc
  - Model ExperimentExecutionActionTargetDetailsProperties no longer has parameter failed_date_utc
  - Model ExperimentExecutionDetails no longer has parameter created_date_utc
  - Model ExperimentExecutionDetails no longer has parameter last_action_date_utc
  - Model ExperimentExecutionDetails no longer has parameter start_date_utc
  - Model ExperimentExecutionDetails no longer has parameter stop_date_utc
  - Model StepStatus no longer has parameter id
  - Model StepStatus no longer has parameter name

## 1.0.0b3 (2022-05-07)

**Features**

  - Model ActionStatus has a new parameter end_time
  - Model ActionStatus has a new parameter start_time

## 1.0.0b2 (2021-10-25)

**Features**

  - Modified client name

## 1.0.0b1 (2021-10-21)

* Initial Release
