# Release History

## 2.0.0b5 (2025-05-09)

### Features Added

  - Method `DiagnosticsOperations.begin_create` has a new overload `def begin_create(self: None, scope: str, diagnostics_resource_name: str, diagnostic_resource_request: DiagnosticResource, content_type: str)`
  - Method `DiagnosticsOperations.begin_create` has a new overload `def begin_create(self: None, scope: str, diagnostics_resource_name: str, diagnostic_resource_request: IO[bytes], content_type: str)`
  - Method `DiscoverySolutionNLPOperations.discover_solutions` has a new overload `def discover_solutions(self: None, discover_solution_request: DiscoveryNlpRequest, content_type: str)`
  - Method `DiscoverySolutionNLPOperations.discover_solutions` has a new overload `def discover_solutions(self: None, discover_solution_request: IO[bytes], content_type: str)`
  - Method `DiscoverySolutionNLPOperations.discover_solutions_by_subscription` has a new overload `def discover_solutions_by_subscription(self: None, discover_solution_request: DiscoveryNlpRequest, content_type: str)`
  - Method `DiscoverySolutionNLPOperations.discover_solutions_by_subscription` has a new overload `def discover_solutions_by_subscription(self: None, discover_solution_request: IO[bytes], content_type: str)`
  - Method `SimplifiedSolutionsOperations.begin_create` has a new overload `def begin_create(self: None, scope: str, simplified_solutions_resource_name: str, simplified_solutions_request_body: SimplifiedSolutionsResource, content_type: str)`
  - Method `SimplifiedSolutionsOperations.begin_create` has a new overload `def begin_create(self: None, scope: str, simplified_solutions_resource_name: str, simplified_solutions_request_body: IO[bytes], content_type: str)`
  - Method `SolutionOperations.begin_create` has a new overload `def begin_create(self: None, scope: str, solution_resource_name: str, solution_request_body: SolutionResource, content_type: str)`
  - Method `SolutionOperations.begin_create` has a new overload `def begin_create(self: None, scope: str, solution_resource_name: str, solution_request_body: IO[bytes], content_type: str)`
  - Method `SolutionOperations.begin_update` has a new overload `def begin_update(self: None, scope: str, solution_resource_name: str, solution_patch_request_body: SolutionPatchRequestBody, content_type: str)`
  - Method `SolutionOperations.begin_update` has a new overload `def begin_update(self: None, scope: str, solution_resource_name: str, solution_patch_request_body: IO[bytes], content_type: str)`
  - Method `TroubleshootersOperations.create` has a new overload `def create(self: None, scope: str, troubleshooter_name: str, create_troubleshooter_request_body: TroubleshooterResource, content_type: str)`
  - Method `TroubleshootersOperations.create` has a new overload `def create(self: None, scope: str, troubleshooter_name: str, create_troubleshooter_request_body: IO[bytes], content_type: str)`

### Breaking Changes

  - Method `SelfHelpMgmtClient.__init__` inserted a `positional_or_keyword` parameter `subscription_id`
  - Method `DiscoveryResponse.__init__` removed default value `None` from its parameter `value`
  - Method `DiagnosticsOperations.begin_create` removed default value `None` from its parameter `diagnostic_resource_request`
  - Method `DiscoverySolutionNLPOperations.discover_solutions` removed default value `None` from its parameter `discover_solution_request`
  - Method `DiscoverySolutionNLPOperations.discover_solutions_by_subscription` removed default value `None` from its parameter `discover_solution_request`
  - Method `DiscoverySolutionNLPOperations.discover_solutions_by_subscription` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `SimplifiedSolutionsOperations.begin_create` removed default value `None` from its parameter `simplified_solutions_request_body`
  - Method `SolutionOperations.begin_create` removed default value `None` from its parameter `solution_request_body`
  - Method `SolutionOperations.begin_update` removed default value `None` from its parameter `solution_patch_request_body`
  - Method `TroubleshootersOperations.create` removed default value `None` from its parameter `create_troubleshooter_request_body`

## 2.0.0b4 (2024-05-27)

### Features Added

  - Added operation CheckNameAvailabilityOperations.check_availability
  - Added operation group DiscoverySolutionNLPOperations

### Breaking Changes

  - Removed operation CheckNameAvailabilityOperations.post
  - Removed operation group DiscoverySolutionNLPSubscriptionScopeOperations
  - Removed operation group DiscoverySolutionNLPTenantScopeOperations

## 2.0.0b3 (2024-04-22)

### Features Added

  - Added operation SolutionOperations.warm_up
  - Added operation group DiscoverySolutionNLPSubscriptionScopeOperations
  - Added operation group DiscoverySolutionNLPTenantScopeOperations
  - Added operation group SimplifiedSolutionsOperations
  - Added operation group SolutionSelfHelpOperations
  - Model AutomatedCheckResult has a new parameter status
  - Model AutomatedCheckResult has a new parameter version
  - Model ResponseValidationProperties has a new parameter validation_scope
  - Model SolutionsDiagnostic has a new parameter estimated_completion_time
  - Model StepInput has a new parameter question_title

### Breaking Changes

  - Operation DiscoverySolutionOperations.list no longer has parameter scope

## 2.0.0b2 (2023-12-18)

### Features Added

  - Model SolutionPatchRequestBody has a new parameter content
  - Model SolutionPatchRequestBody has a new parameter parameters
  - Model SolutionPatchRequestBody has a new parameter provisioning_state
  - Model SolutionPatchRequestBody has a new parameter replacement_maps
  - Model SolutionPatchRequestBody has a new parameter sections
  - Model SolutionPatchRequestBody has a new parameter solution_id
  - Model SolutionPatchRequestBody has a new parameter title
  - Model SolutionPatchRequestBody has a new parameter trigger_criteria
  - Model SolutionResource has a new parameter content
  - Model SolutionResource has a new parameter parameters
  - Model SolutionResource has a new parameter provisioning_state
  - Model SolutionResource has a new parameter replacement_maps
  - Model SolutionResource has a new parameter sections
  - Model SolutionResource has a new parameter solution_id
  - Model SolutionResource has a new parameter system_data
  - Model SolutionResource has a new parameter title
  - Model SolutionResource has a new parameter trigger_criteria

### Breaking Changes

  - Model SolutionPatchRequestBody no longer has parameter properties
  - Model SolutionResource no longer has parameter properties

## 2.0.0b1 (2023-10-23)

### Features Added

  - Added operation group CheckNameAvailabilityOperations
  - Added operation group SolutionOperations
  - Added operation group TroubleshootersOperations
  - Model SolutionMetadataResource has a new parameter solutions

### Breaking Changes

  - Model SolutionMetadataResource no longer has parameter description
  - Model SolutionMetadataResource no longer has parameter required_parameter_sets
  - Model SolutionMetadataResource no longer has parameter solution_id
  - Model SolutionMetadataResource no longer has parameter solution_type
  - Removed operation DiagnosticsOperations.check_name_availability

## 1.0.0 (2023-06-25)

- First GA version


## 1.0.0b1 (2023-05-17)

* Initial Release
