# Release History

## 1.0.0 (2025-05-13)

### Features Added

  - Client `GuestConfigurationClient` added operation group `guest_configuration_connected_vmwarev_sphere_assignments`
  - Client `GuestConfigurationClient` added operation group `guest_configuration_connected_vmwarev_sphere_assignments_reports`
  - Model `GuestConfigurationNavigation` added property `content_managed_identity`
  - Model `Operation` added property `is_data_action`
  - Model `Operation` added property `origin`
  - Model `Operation` added property `action_type`
  - Model `ProxyResource` added property `system_data`
  - Model `Resource` added property `system_data`
  - Added enum `ActionType`
  - Added model `ErrorAdditionalInfo`
  - Added model `ErrorDetail`
  - Added model `OperationListResult`
  - Added enum `Origin`
  - Added model `VmssvmInfo`
  - Model `GuestConfigurationAssignmentsVMSSOperations` added method `create_or_update`
  - Added model `GuestConfigurationConnectedVMwarevSphereAssignmentsOperations`
  - Added model `GuestConfigurationConnectedVMwarevSphereAssignmentsReportsOperations`
  - Method `GuestConfigurationAssignmentsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, vm_name: str, guest_configuration_assignment_name: str, parameters: IO[bytes], content_type: str)`
  - Method `GuestConfigurationAssignmentsVMSSOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, vmss_name: str, name: str, parameters: GuestConfigurationAssignment, content_type: str)`
  - Method `GuestConfigurationAssignmentsVMSSOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, vmss_name: str, name: str, parameters: IO[bytes], content_type: str)`
  - Method `GuestConfigurationHCRPAssignmentsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, machine_name: str, guest_configuration_assignment_name: str, parameters: IO[bytes], content_type: str)`
  - Method `GuestConfigurationConnectedVMwarevSphereAssignmentsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, vm_name: str, guest_configuration_assignment_name: str, parameters: GuestConfigurationAssignment, content_type: str)`
  - Method `GuestConfigurationConnectedVMwarevSphereAssignmentsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, vm_name: str, guest_configuration_assignment_name: str, parameters: IO[bytes], content_type: str)`

### Breaking Changes

  - Method `GuestConfigurationAssignmentReportsVMSSOperations.list` changed from `synchronous` to `asynchronous`
  - Method `GuestConfigurationAssignmentsOperations.list` changed from `synchronous` to `asynchronous`
  - Method `GuestConfigurationAssignmentsOperations.rg_list` changed from `synchronous` to `asynchronous`
  - Method `GuestConfigurationAssignmentsVMSSOperations.list` changed from `synchronous` to `asynchronous`
  - Method `GuestConfigurationHCRPAssignmentsOperations.list` changed from `synchronous` to `asynchronous`
  - Model `GuestConfigurationAssignment` deleted or renamed its instance variable `location`
  - Model `Operation` deleted or renamed its instance variable `status_code`
  - Model `ProxyResource` deleted or renamed its instance variable `location`
  - Model `Resource` deleted or renamed its instance variable `location`
  - Deleted or renamed model `ErrorResponseError`
  - Deleted or renamed model `OperationList`
  - Deleted or renamed model `VMSSVMInfo`
  - Deleted or renamed method `GuestConfigurationAssignmentsOperations.subscription_list`
  - Method `GuestConfigurationAssignmentsOperations.create_or_update` re-ordered its parameters from `['self', 'guest_configuration_assignment_name', 'resource_group_name', 'vm_name', 'parameters', 'kwargs']` to `['self', 'resource_group_name', 'vm_name', 'guest_configuration_assignment_name', 'parameters', 'kwargs']`
  - Method `GuestConfigurationAssignmentsOperations.get` re-ordered its parameters from `['self', 'resource_group_name', 'guest_configuration_assignment_name', 'vm_name', 'kwargs']` to `['self', 'resource_group_name', 'vm_name', 'guest_configuration_assignment_name', 'kwargs']`
  - Method `GuestConfigurationAssignmentsOperations.delete` re-ordered its parameters from `['self', 'resource_group_name', 'guest_configuration_assignment_name', 'vm_name', 'kwargs']` to `['self', 'resource_group_name', 'vm_name', 'guest_configuration_assignment_name', 'kwargs']`
  - Method `GuestConfigurationAssignmentReportsOperations.get` re-ordered its parameters from `['self', 'resource_group_name', 'guest_configuration_assignment_name', 'report_id', 'vm_name', 'kwargs']` to `['self', 'resource_group_name', 'vm_name', 'guest_configuration_assignment_name', 'report_id', 'kwargs']`
  - Method `GuestConfigurationAssignmentReportsOperations.list` re-ordered its parameters from `['self', 'resource_group_name', 'guest_configuration_assignment_name', 'vm_name', 'kwargs']` to `['self', 'resource_group_name', 'vm_name', 'guest_configuration_assignment_name', 'kwargs']`
  - Method `GuestConfigurationHCRPAssignmentsOperations.create_or_update` re-ordered its parameters from `['self', 'guest_configuration_assignment_name', 'resource_group_name', 'machine_name', 'parameters', 'kwargs']` to `['self', 'resource_group_name', 'machine_name', 'guest_configuration_assignment_name', 'parameters', 'kwargs']`
  - Method `GuestConfigurationHCRPAssignmentsOperations.get` re-ordered its parameters from `['self', 'resource_group_name', 'guest_configuration_assignment_name', 'machine_name', 'kwargs']` to `['self', 'resource_group_name', 'machine_name', 'guest_configuration_assignment_name', 'kwargs']`
  - Method `GuestConfigurationHCRPAssignmentsOperations.delete` re-ordered its parameters from `['self', 'resource_group_name', 'guest_configuration_assignment_name', 'machine_name', 'kwargs']` to `['self', 'resource_group_name', 'machine_name', 'guest_configuration_assignment_name', 'kwargs']`
  - Method `GuestConfigurationHCRPAssignmentReportsOperations.get` re-ordered its parameters from `['self', 'resource_group_name', 'guest_configuration_assignment_name', 'report_id', 'machine_name', 'kwargs']` to `['self', 'resource_group_name', 'machine_name', 'guest_configuration_assignment_name', 'report_id', 'kwargs']`
  - Method `GuestConfigurationHCRPAssignmentReportsOperations.list` re-ordered its parameters from `['self', 'resource_group_name', 'guest_configuration_assignment_name', 'machine_name', 'kwargs']` to `['self', 'resource_group_name', 'machine_name', 'guest_configuration_assignment_name', 'kwargs']`

## 1.0.0b2 (2022-11-04)

### Features Added

  - Added operation GuestConfigurationAssignmentsOperations.rg_list
  - Added operation GuestConfigurationAssignmentsOperations.subscription_list
  - Added operation group GuestConfigurationAssignmentReportsVMSSOperations
  - Added operation group GuestConfigurationAssignmentsVMSSOperations
  - Model GuestConfigurationAssignment has a new parameter system_data
  - Model GuestConfigurationAssignmentProperties has a new parameter parameter_hash
  - Model GuestConfigurationAssignmentProperties has a new parameter resource_type
  - Model GuestConfigurationAssignmentProperties has a new parameter vmss_vm_list
  - Model GuestConfigurationAssignmentReportProperties has a new parameter vmss_resource_id
  - Model GuestConfigurationNavigation has a new parameter assignment_source
  - Model GuestConfigurationNavigation has a new parameter configuration_protected_parameter
  - Model GuestConfigurationNavigation has a new parameter content_type

## 1.0.0b1 (2021-07-13)

* Initial Release

