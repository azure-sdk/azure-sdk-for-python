# Release History

## 1.1.0 (2025-04-29)

### Features Added

  - Added model `CreateResourceOperationResponse`
  - Added model `DeleteResourceOperationResponse`
  - Added model `ExecuteCreateRequest`
  - Added model `ExecuteDeleteRequest`
  - Added model `ResourceProvisionPayload`
  - Added model `SubmitCreateRequest`
  - Added model `SubmitDeleteRequest`
  - Model `ScheduledActionsOperations` added method `virtual_machines_execute_create`
  - Model `ScheduledActionsOperations` added method `virtual_machines_execute_delete`
  - Model `ScheduledActionsOperations` added method `virtual_machines_submit_create`
  - Model `ScheduledActionsOperations` added method `virtual_machines_submit_delete`
  - Method `CreateResourceOperationResponse.__init__` has a new overload `def __init__(self: None, description: str, type: str, location: str, results: Optional[List[_models.ResourceOperation]])`
  - Method `CreateResourceOperationResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DeleteResourceOperationResponse.__init__` has a new overload `def __init__(self: None, description: str, type: str, location: str, results: Optional[List[_models.ResourceOperation]])`
  - Method `DeleteResourceOperationResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ExecuteCreateRequest.__init__` has a new overload `def __init__(self: None, resource_config_parameters: _models.ResourceProvisionPayload, execution_parameters: _models.ExecutionParameters, correlationid: Optional[str])`
  - Method `ExecuteCreateRequest.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ExecuteDeleteRequest.__init__` has a new overload `def __init__(self: None, execution_parameters: _models.ExecutionParameters, resources: _models.Resources, correlationid: Optional[str], force_deletion: Optional[bool])`
  - Method `ExecuteDeleteRequest.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ResourceProvisionPayload.__init__` has a new overload `def __init__(self: None, resource_count: int, base_profile: Optional[str], resource_overrides: Optional[List[str]], resource_prefix: Optional[str])`
  - Method `ResourceProvisionPayload.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SubmitCreateRequest.__init__` has a new overload `def __init__(self: None, schedule: _models.Schedule, resource_config_parameters: _models.ResourceProvisionPayload, execution_parameters: Optional[_models.ExecutionParameters], correlationid: Optional[str])`
  - Method `SubmitCreateRequest.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SubmitDeleteRequest.__init__` has a new overload `def __init__(self: None, schedule: _models.Schedule, execution_parameters: _models.ExecutionParameters, resources: _models.Resources, correlationid: Optional[str], force_deletion: Optional[bool])`
  - Method `SubmitDeleteRequest.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ScheduledActionsOperations.virtual_machines_execute_create` has a new overload `def virtual_machines_execute_create(self: None, locationparameter: str, request_body: ExecuteCreateRequest, content_type: str)`
  - Method `ScheduledActionsOperations.virtual_machines_execute_create` has a new overload `def virtual_machines_execute_create(self: None, locationparameter: str, request_body: JSON, content_type: str)`
  - Method `ScheduledActionsOperations.virtual_machines_execute_create` has a new overload `def virtual_machines_execute_create(self: None, locationparameter: str, request_body: IO[bytes], content_type: str)`
  - Method `ScheduledActionsOperations.virtual_machines_execute_delete` has a new overload `def virtual_machines_execute_delete(self: None, locationparameter: str, request_body: ExecuteDeleteRequest, content_type: str)`
  - Method `ScheduledActionsOperations.virtual_machines_execute_delete` has a new overload `def virtual_machines_execute_delete(self: None, locationparameter: str, request_body: JSON, content_type: str)`
  - Method `ScheduledActionsOperations.virtual_machines_execute_delete` has a new overload `def virtual_machines_execute_delete(self: None, locationparameter: str, request_body: IO[bytes], content_type: str)`
  - Method `ScheduledActionsOperations.virtual_machines_submit_create` has a new overload `def virtual_machines_submit_create(self: None, locationparameter: str, request_body: SubmitCreateRequest, content_type: str)`
  - Method `ScheduledActionsOperations.virtual_machines_submit_create` has a new overload `def virtual_machines_submit_create(self: None, locationparameter: str, request_body: JSON, content_type: str)`
  - Method `ScheduledActionsOperations.virtual_machines_submit_create` has a new overload `def virtual_machines_submit_create(self: None, locationparameter: str, request_body: IO[bytes], content_type: str)`
  - Method `ScheduledActionsOperations.virtual_machines_submit_delete` has a new overload `def virtual_machines_submit_delete(self: None, locationparameter: str, request_body: SubmitDeleteRequest, content_type: str)`
  - Method `ScheduledActionsOperations.virtual_machines_submit_delete` has a new overload `def virtual_machines_submit_delete(self: None, locationparameter: str, request_body: JSON, content_type: str)`
  - Method `ScheduledActionsOperations.virtual_machines_submit_delete` has a new overload `def virtual_machines_submit_delete(self: None, locationparameter: str, request_body: IO[bytes], content_type: str)`

## 1.0.0 (2025-01-20)

### Features Added

  - Model `OperationErrorDetails` added property `timestamp`
  - Model `OperationErrorDetails` added property `azure_operation_name`
  - Model `ResourceOperationDetails` added property `timezone`
  - Model `Schedule` added property `deadline`
  - Model `Schedule` added property `timezone`

## 1.0.0b1 (2024-09-26)

### Other Changes

  - Initial version
