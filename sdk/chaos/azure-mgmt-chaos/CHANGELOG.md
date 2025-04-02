# Release History

## 2.0.0 (2025-04-02)

### Features Added

  - Added operation Operations.list
  - Added operation group ExperimentExecutionsOperations
  - Model Capability has a new parameter properties
  - Model CapabilityType has a new parameter properties
  - Model ExperimentExecution has a new parameter properties
  - Model ExperimentExecution has a new parameter system_data
  - Model ExperimentExecutionDetails has a new parameter properties
  - Model Resource has a new parameter system_data
  - Model TrackedResource has a new parameter system_data

### Breaking Changes

  - Model Capability no longer has parameter description
  - Model Capability no longer has parameter parameters_schema
  - Model Capability no longer has parameter publisher
  - Model Capability no longer has parameter target_type
  - Model Capability no longer has parameter urn
  - Model CapabilityType no longer has parameter azure_rbac_actions
  - Model CapabilityType no longer has parameter azure_rbac_data_actions
  - Model CapabilityType no longer has parameter description
  - Model CapabilityType no longer has parameter display_name
  - Model CapabilityType no longer has parameter kind
  - Model CapabilityType no longer has parameter location
  - Model CapabilityType no longer has parameter parameters_schema
  - Model CapabilityType no longer has parameter publisher
  - Model CapabilityType no longer has parameter runtime_properties
  - Model CapabilityType no longer has parameter target_type
  - Model CapabilityType no longer has parameter urn
  - Model ChaosTargetListSelector no longer has parameter additional_properties
  - Model ChaosTargetQuerySelector no longer has parameter additional_properties
  - Model ChaosTargetSelector no longer has parameter additional_properties
  - Model Experiment has a new required parameter properties
  - Model Experiment no longer has parameter provisioning_state
  - Model Experiment no longer has parameter selectors
  - Model Experiment no longer has parameter steps
  - Model ExperimentExecution no longer has parameter started_at
  - Model ExperimentExecution no longer has parameter status
  - Model ExperimentExecution no longer has parameter stopped_at
  - Model ExperimentExecutionDetails no longer has parameter failure_reason
  - Model ExperimentExecutionDetails no longer has parameter last_action_at
  - Model ExperimentExecutionDetails no longer has parameter run_information
  - Model ExperimentExecutionDetails no longer has parameter started_at
  - Model ExperimentExecutionDetails no longer has parameter status
  - Model ExperimentExecutionDetails no longer has parameter stopped_at
  - Model TargetType has a new required parameter properties
  - Model TargetType no longer has parameter description
  - Model TargetType no longer has parameter display_name
  - Model TargetType no longer has parameter location
  - Model TargetType no longer has parameter properties_schema
  - Model TargetType no longer has parameter resource_types
  - Operation CapabilitiesOperations.create_or_update has a new required parameter resource
  - Operation CapabilitiesOperations.create_or_update no longer has parameter capability
  - Operation CapabilityTypesOperations.get has a new required parameter location
  - Operation CapabilityTypesOperations.get no longer has parameter location_name
  - Operation CapabilityTypesOperations.list has a new required parameter location
  - Operation CapabilityTypesOperations.list no longer has parameter location_name
  - Operation ExperimentsOperations.begin_create_or_update has a new required parameter resource
  - Operation ExperimentsOperations.begin_create_or_update no longer has parameter experiment
  - Operation ExperimentsOperations.begin_update has a new required parameter properties
  - Operation ExperimentsOperations.begin_update no longer has parameter experiment
  - Operation OperationStatusesOperations.get has a new required parameter operation_id
  - Operation OperationStatusesOperations.get no longer has parameter async_operation_id
  - Operation TargetTypesOperations.get has a new required parameter location
  - Operation TargetTypesOperations.get no longer has parameter location_name
  - Operation TargetTypesOperations.list has a new required parameter location
  - Operation TargetTypesOperations.list no longer has parameter location_name
  - Operation TargetsOperations.create_or_update has a new required parameter resource
  - Operation TargetsOperations.create_or_update no longer has parameter target
  - Removed operation ExperimentsOperations.execution_details
  - Removed operation ExperimentsOperations.get_execution
  - Removed operation ExperimentsOperations.list_all_executions
  - Removed operation Operations.list_all

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
