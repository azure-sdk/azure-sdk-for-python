# Release History

## 5.0.0b1 (2025-07-23)

### Features Added

  - Client `AuthorizationManagementClient` added operation group `classic_administrators`
  - Client `AuthorizationManagementClient` added operation group `global_administrator`
  - Client `AuthorizationManagementClient` added operation group `deny_assignments`
  - Client `AuthorizationManagementClient` added operation group `provider_operations_metadata`
  - Client `AuthorizationManagementClient` added operation group `role_assignments`
  - Client `AuthorizationManagementClient` added operation group `permissions`
  - Client `AuthorizationManagementClient` added operation group `role_definitions`
  - Client `AuthorizationManagementClient` added operation group `operations`
  - Client `AuthorizationManagementClient` added operation group `access_review_history_definitions`
  - Client `AuthorizationManagementClient` added operation group `access_review_history_definition`
  - Client `AuthorizationManagementClient` added operation group `access_review_history_definition_instance`
  - Client `AuthorizationManagementClient` added operation group `access_review_history_definition_instances`
  - Client `AuthorizationManagementClient` added operation group `access_review_schedule_definitions`
  - Client `AuthorizationManagementClient` added operation group `access_review_instances`
  - Client `AuthorizationManagementClient` added operation group `access_review_instance`
  - Client `AuthorizationManagementClient` added operation group `access_review_instance_decisions`
  - Client `AuthorizationManagementClient` added operation group `access_review_instance_contacted_reviewers`
  - Client `AuthorizationManagementClient` added operation group `access_review_default_settings`
  - Client `AuthorizationManagementClient` added operation group `scope_access_review_history_definitions`
  - Client `AuthorizationManagementClient` added operation group `scope_access_review_history_definition`
  - Client `AuthorizationManagementClient` added operation group `scope_access_review_history_definition_instance`
  - Client `AuthorizationManagementClient` added operation group `scope_access_review_history_definition_instances`
  - Client `AuthorizationManagementClient` added operation group `scope_access_review_schedule_definitions`
  - Client `AuthorizationManagementClient` added operation group `scope_access_review_instances`
  - Client `AuthorizationManagementClient` added operation group `scope_access_review_instance`
  - Client `AuthorizationManagementClient` added operation group `scope_access_review_instance_decisions`
  - Client `AuthorizationManagementClient` added operation group `scope_access_review_instance_contacted_reviewers`
  - Client `AuthorizationManagementClient` added operation group `scope_access_review_default_settings`
  - Client `AuthorizationManagementClient` added operation group `access_review_schedule_definitions_assigned_for_my_approval`
  - Client `AuthorizationManagementClient` added operation group `access_review_instances_assigned_for_my_approval`
  - Client `AuthorizationManagementClient` added operation group `access_review_instance_my_decisions`
  - Client `AuthorizationManagementClient` added operation group `tenant_level_access_review_instance_contacted_reviewers`
  - Client `AuthorizationManagementClient` added operation group `eligible_child_resources`
  - Client `AuthorizationManagementClient` added operation group `role_assignment_schedules`
  - Client `AuthorizationManagementClient` added operation group `role_assignment_schedule_instances`
  - Client `AuthorizationManagementClient` added operation group `role_assignment_schedule_requests`
  - Client `AuthorizationManagementClient` added operation group `role_eligibility_schedules`
  - Client `AuthorizationManagementClient` added operation group `role_eligibility_schedule_instances`
  - Client `AuthorizationManagementClient` added operation group `role_eligibility_schedule_requests`
  - Client `AuthorizationManagementClient` added operation group `role_management_policies`
  - Client `AuthorizationManagementClient` added operation group `role_management_policy_assignments`
  - Added enum `AccessRecommendationType`
  - Added enum `AccessReviewActorIdentityType`
  - Added enum `AccessReviewApplyResult`
  - Added model `AccessReviewContactedReviewer`
  - Added model `AccessReviewContactedReviewerListResult`
  - Added model `AccessReviewDecision`
  - Added model `AccessReviewDecisionIdentity`
  - Added model `AccessReviewDecisionInsight`
  - Added model `AccessReviewDecisionInsightProperties`
  - Added enum `AccessReviewDecisionInsightType`
  - Added model `AccessReviewDecisionListResult`
  - Added enum `AccessReviewDecisionPrincipalResourceMembershipType`
  - Added model `AccessReviewDecisionProperties`
  - Added model `AccessReviewDecisionServicePrincipalIdentity`
  - Added model `AccessReviewDecisionUserIdentity`
  - Added model `AccessReviewDecisionUserSignInInsightProperties`
  - Added model `AccessReviewDefaultSettings`
  - Added model `AccessReviewHistoryDefinition`
  - Added model `AccessReviewHistoryDefinitionInstanceListResult`
  - Added model `AccessReviewHistoryDefinitionListResult`
  - Added model `AccessReviewHistoryDefinitionProperties`
  - Added enum `AccessReviewHistoryDefinitionStatus`
  - Added model `AccessReviewHistoryInstance`
  - Added model `AccessReviewInstance`
  - Added model `AccessReviewInstanceListResult`
  - Added model `AccessReviewInstanceProperties`
  - Added enum `AccessReviewInstanceReviewersType`
  - Added enum `AccessReviewInstanceStatus`
  - Added enum `AccessReviewRecurrencePatternType`
  - Added enum `AccessReviewRecurrenceRangeType`
  - Added enum `AccessReviewResult`
  - Added model `AccessReviewReviewer`
  - Added enum `AccessReviewReviewerType`
  - Added model `AccessReviewScheduleDefinition`
  - Added model `AccessReviewScheduleDefinitionListResult`
  - Added model `AccessReviewScheduleDefinitionProperties`
  - Added enum `AccessReviewScheduleDefinitionReviewersType`
  - Added enum `AccessReviewScheduleDefinitionStatus`
  - Added model `AccessReviewScheduleSettings`
  - Added model `AccessReviewScope`
  - Added enum `AccessReviewScopeAssignmentState`
  - Added enum `AccessReviewScopePrincipalType`
  - Added enum `ApprovalMode`
  - Added model `ApprovalSettings`
  - Added model `ApprovalStage`
  - Added enum `AssignmentType`
  - Added model `ClassicAdministrator`
  - Added model `ClassicAdministratorListResult`
  - Added enum `DecisionResourceType`
  - Added enum `DecisionTargetType`
  - Added enum `DefaultDecisionType`
  - Added model `DenyAssignment`
  - Added model `DenyAssignmentFilter`
  - Added model `DenyAssignmentListResult`
  - Added model `DenyAssignmentPermission`
  - Added model `EligibleChildResource`
  - Added model `EligibleChildResourcesListResult`
  - Added enum `EnablementRules`
  - Added model `ErrorAdditionalInfo`
  - Added model `ErrorDefinition`
  - Added model `ErrorDefinitionProperties`
  - Added model `ErrorDetail`
  - Added model `ErrorResponse`
  - Added enum `ExcludedPrincipalTypes`
  - Added model `ExpandedProperties`
  - Added model `ExpandedPropertiesPrincipal`
  - Added model `ExpandedPropertiesRoleDefinition`
  - Added model `ExpandedPropertiesScope`
  - Added enum `MemberType`
  - Added enum `NotificationDeliveryMechanism`
  - Added enum `NotificationLevel`
  - Added model `Operation`
  - Added model `OperationDisplay`
  - Added model `OperationListResult`
  - Added enum `PIMOnlyMode`
  - Added model `PIMOnlyModeSettings`
  - Added model `Permission`
  - Added model `PermissionGetResult`
  - Added model `PolicyAssignmentProperties`
  - Added model `PolicyAssignmentPropertiesPolicy`
  - Added model `PolicyAssignmentPropertiesRoleDefinition`
  - Added model `PolicyAssignmentPropertiesScope`
  - Added model `PolicyProperties`
  - Added model `PolicyPropertiesScope`
  - Added model `Principal`
  - Added enum `PrincipalType`
  - Added model `ProviderOperation`
  - Added model `ProviderOperationsMetadata`
  - Added model `ProviderOperationsMetadataListResult`
  - Added enum `RecipientType`
  - Added model `RecordAllDecisionsProperties`
  - Added enum `RecordAllDecisionsResult`
  - Added enum `RequestType`
  - Added model `ResourceType`
  - Added model `RoleAssignment`
  - Added model `RoleAssignmentCreateParameters`
  - Added model `RoleAssignmentFilter`
  - Added model `RoleAssignmentListResult`
  - Added model `RoleAssignmentSchedule`
  - Added model `RoleAssignmentScheduleFilter`
  - Added model `RoleAssignmentScheduleInstance`
  - Added model `RoleAssignmentScheduleInstanceFilter`
  - Added model `RoleAssignmentScheduleInstanceListResult`
  - Added model `RoleAssignmentScheduleListResult`
  - Added model `RoleAssignmentScheduleRequest`
  - Added model `RoleAssignmentScheduleRequestFilter`
  - Added model `RoleAssignmentScheduleRequestListResult`
  - Added model `RoleAssignmentScheduleRequestPropertiesScheduleInfo`
  - Added model `RoleAssignmentScheduleRequestPropertiesScheduleInfoExpiration`
  - Added model `RoleAssignmentScheduleRequestPropertiesTicketInfo`
  - Added model `RoleDefinition`
  - Added model `RoleDefinitionFilter`
  - Added model `RoleDefinitionListResult`
  - Added model `RoleEligibilitySchedule`
  - Added model `RoleEligibilityScheduleFilter`
  - Added model `RoleEligibilityScheduleInstance`
  - Added model `RoleEligibilityScheduleInstanceFilter`
  - Added model `RoleEligibilityScheduleInstanceListResult`
  - Added model `RoleEligibilityScheduleListResult`
  - Added model `RoleEligibilityScheduleRequest`
  - Added model `RoleEligibilityScheduleRequestFilter`
  - Added model `RoleEligibilityScheduleRequestListResult`
  - Added model `RoleEligibilityScheduleRequestPropertiesScheduleInfo`
  - Added model `RoleEligibilityScheduleRequestPropertiesScheduleInfoExpiration`
  - Added model `RoleEligibilityScheduleRequestPropertiesTicketInfo`
  - Added model `RoleManagementPolicy`
  - Added model `RoleManagementPolicyApprovalRule`
  - Added model `RoleManagementPolicyAssignment`
  - Added model `RoleManagementPolicyAssignmentListResult`
  - Added model `RoleManagementPolicyAuthenticationContextRule`
  - Added model `RoleManagementPolicyEnablementRule`
  - Added model `RoleManagementPolicyExpirationRule`
  - Added model `RoleManagementPolicyListResult`
  - Added model `RoleManagementPolicyNotificationRule`
  - Added model `RoleManagementPolicyPimOnlyModeRule`
  - Added model `RoleManagementPolicyRule`
  - Added model `RoleManagementPolicyRuleTarget`
  - Added enum `RoleManagementPolicyRuleType`
  - Added enum `Status`
  - Added enum `Type`
  - Added model `UserSet`
  - Added enum `UserType`
  - Added model `UsersOrServicePrincipalSet`
  - Added model `ValidationResponse`
  - Added model `ValidationResponseErrorInfo`
  - Added model `AccessReviewDefaultSettingsOperations`
  - Added model `AccessReviewHistoryDefinitionInstanceOperations`
  - Added model `AccessReviewHistoryDefinitionInstancesOperations`
  - Added model `AccessReviewHistoryDefinitionOperations`
  - Added model `AccessReviewHistoryDefinitionsOperations`
  - Added model `AccessReviewInstanceContactedReviewersOperations`
  - Added model `AccessReviewInstanceDecisionsOperations`
  - Added model `AccessReviewInstanceMyDecisionsOperations`
  - Added model `AccessReviewInstanceOperations`
  - Added model `AccessReviewInstancesAssignedForMyApprovalOperations`
  - Added model `AccessReviewInstancesOperations`
  - Added model `AccessReviewScheduleDefinitionsAssignedForMyApprovalOperations`
  - Added model `AccessReviewScheduleDefinitionsOperations`
  - Added model `ClassicAdministratorsOperations`
  - Added model `DenyAssignmentsOperations`
  - Added model `EligibleChildResourcesOperations`
  - Added model `GlobalAdministratorOperations`
  - Added model `Operations`
  - Added model `PermissionsOperations`
  - Added model `ProviderOperationsMetadataOperations`
  - Added model `RoleAssignmentScheduleInstancesOperations`
  - Added model `RoleAssignmentScheduleRequestsOperations`
  - Added model `RoleAssignmentSchedulesOperations`
  - Added model `RoleAssignmentsOperations`
  - Added model `RoleDefinitionsOperations`
  - Added model `RoleEligibilityScheduleInstancesOperations`
  - Added model `RoleEligibilityScheduleRequestsOperations`
  - Added model `RoleEligibilitySchedulesOperations`
  - Added model `RoleManagementPoliciesOperations`
  - Added model `RoleManagementPolicyAssignmentsOperations`
  - Added model `ScopeAccessReviewDefaultSettingsOperations`
  - Added model `ScopeAccessReviewHistoryDefinitionInstanceOperations`
  - Added model `ScopeAccessReviewHistoryDefinitionInstancesOperations`
  - Added model `ScopeAccessReviewHistoryDefinitionOperations`
  - Added model `ScopeAccessReviewHistoryDefinitionsOperations`
  - Added model `ScopeAccessReviewInstanceContactedReviewersOperations`
  - Added model `ScopeAccessReviewInstanceDecisionsOperations`
  - Added model `ScopeAccessReviewInstanceOperations`
  - Added model `ScopeAccessReviewInstancesOperations`
  - Added model `ScopeAccessReviewScheduleDefinitionsOperations`
  - Added model `TenantLevelAccessReviewInstanceContactedReviewersOperations`

### Breaking Changes

  - This package now only targets the latest Api-Version available on Azure and removes APIs of other Api-Version. After this change, the package can have much smaller size. If your application requires a specific and non-latest Api-Version, it's recommended to pin this package to the previous released version; If your application always only use latest Api-Version, please ignore this change.

## 4.0.0 (2023-07-21)

### Features Added

  - Added operation RoleAssignmentScheduleRequestsOperations.validate
  - Added operation RoleEligibilityScheduleRequestsOperations.validate
  - Model AlertConfiguration has a new parameter alert_definition
  - Model AlertConfigurationProperties has a new parameter alert_definition
  - Model AlertOperationResult has a new parameter created_date_time
  - Model AlertOperationResult has a new parameter last_action_date_time
  - Model AlertOperationResult has a new parameter resource_location
  - Model AlertOperationResult has a new parameter status_detail
  - Model AzureRolesAssignedOutsidePimAlertConfigurationProperties has a new parameter alert_definition
  - Model DenyAssignment has a new parameter condition
  - Model DenyAssignment has a new parameter condition_version
  - Model DenyAssignment has a new parameter created_by
  - Model DenyAssignment has a new parameter created_on
  - Model DenyAssignment has a new parameter updated_by
  - Model DenyAssignment has a new parameter updated_on
  - Model DuplicateRoleCreatedAlertConfigurationProperties has a new parameter alert_definition
  - Model Permission has a new parameter condition
  - Model Permission has a new parameter condition_version
  - Model RoleDefinition has a new parameter created_by
  - Model RoleDefinition has a new parameter created_on
  - Model RoleDefinition has a new parameter updated_by
  - Model RoleDefinition has a new parameter updated_on
  - Model TooManyOwnersAssignedToResourceAlertConfigurationProperties has a new parameter alert_definition
  - Model TooManyPermanentOwnersAssignedToResourceAlertConfigurationProperties has a new parameter alert_definition

### Breaking Changes

  - Removed operation AlertOperationOperations.list_for_scope

## 3.1.0b1 (2023-02-15)

### Features Added

  - Model AlertConfiguration has a new parameter alert_definition
  - Model AlertConfigurationProperties has a new parameter alert_definition
  - Model AzureRolesAssignedOutsidePimAlertConfigurationProperties has a new parameter alert_definition
  - Model DenyAssignment has a new parameter condition
  - Model DenyAssignment has a new parameter condition_version
  - Model DenyAssignment has a new parameter created_by
  - Model DenyAssignment has a new parameter created_on
  - Model DenyAssignment has a new parameter updated_by
  - Model DenyAssignment has a new parameter updated_on
  - Model DuplicateRoleCreatedAlertConfigurationProperties has a new parameter alert_definition
  - Model RoleDefinition has a new parameter created_by
  - Model RoleDefinition has a new parameter created_on
  - Model RoleDefinition has a new parameter updated_by
  - Model RoleDefinition has a new parameter updated_on
  - Model TooManyOwnersAssignedToResourceAlertConfigurationProperties has a new parameter alert_definition
  - Model TooManyPermanentOwnersAssignedToResourceAlertConfigurationProperties has a new parameter alert_definition

## 3.0.0 (2022-10-11)

### Features Added

  - Added operation AccessReviewInstancesOperations.create
  - Added operation group AccessReviewHistoryDefinitionInstanceOperations
  - Added operation group AccessReviewHistoryDefinitionInstancesOperations
  - Added operation group AccessReviewHistoryDefinitionOperations
  - Added operation group AccessReviewHistoryDefinitionsOperations
  - Added operation group AccessReviewInstanceContactedReviewersOperations
  - Added operation group AlertConfigurationsOperations
  - Added operation group AlertDefinitionsOperations
  - Added operation group AlertIncidentsOperations
  - Added operation group AlertOperationOperations
  - Added operation group AlertsOperations
  - Added operation group ScopeAccessReviewDefaultSettingsOperations
  - Added operation group ScopeAccessReviewHistoryDefinitionInstanceOperations
  - Added operation group ScopeAccessReviewHistoryDefinitionInstancesOperations
  - Added operation group ScopeAccessReviewHistoryDefinitionOperations
  - Added operation group ScopeAccessReviewHistoryDefinitionsOperations
  - Added operation group ScopeAccessReviewInstanceContactedReviewersOperations
  - Added operation group ScopeAccessReviewInstanceDecisionsOperations
  - Added operation group ScopeAccessReviewInstanceOperations
  - Added operation group ScopeAccessReviewInstancesOperations
  - Added operation group ScopeAccessReviewScheduleDefinitionsOperations
  - Added operation group TenantLevelAccessReviewInstanceContactedReviewersOperations
  - Model AccessReviewDecision has a new parameter insights
  - Model AccessReviewDecision has a new parameter membership_types
  - Model AccessReviewDecisionProperties has a new parameter insights
  - Model AccessReviewDecisionProperties has a new parameter membership_types
  - Model AccessReviewDefaultSettings has a new parameter recommendation_look_back_duration
  - Model AccessReviewInstance has a new parameter backup_reviewers
  - Model AccessReviewInstance has a new parameter reviewers
  - Model AccessReviewInstance has a new parameter reviewers_type
  - Model AccessReviewScheduleDefinition has a new parameter exclude_resource_id
  - Model AccessReviewScheduleDefinition has a new parameter exclude_role_definition_id
  - Model AccessReviewScheduleDefinition has a new parameter expand_nested_memberships
  - Model AccessReviewScheduleDefinition has a new parameter include_access_below_resource
  - Model AccessReviewScheduleDefinition has a new parameter include_inherited_access
  - Model AccessReviewScheduleDefinition has a new parameter recommendation_look_back_duration
  - Model AccessReviewScheduleDefinitionProperties has a new parameter exclude_resource_id
  - Model AccessReviewScheduleDefinitionProperties has a new parameter exclude_role_definition_id
  - Model AccessReviewScheduleDefinitionProperties has a new parameter expand_nested_memberships
  - Model AccessReviewScheduleDefinitionProperties has a new parameter include_access_below_resource
  - Model AccessReviewScheduleDefinitionProperties has a new parameter include_inherited_access
  - Model AccessReviewScheduleDefinitionProperties has a new parameter recommendation_look_back_duration
  - Model AccessReviewScheduleSettings has a new parameter recommendation_look_back_duration
  - Model DenyAssignmentPermission has a new parameter condition
  - Model DenyAssignmentPermission has a new parameter condition_version

### Breaking Changes

  - Operation RoleAssignmentsOperations.list_for_scope has a new parameter skip_token
  - Removed operation RoleAssignmentsOperations.validate
  - Removed operation RoleAssignmentsOperations.validate_by_id

## 2.0.0 (2021-09-26)

**Features**

  - Model RoleAssignment has a new parameter created_on
  - Model RoleAssignment has a new parameter delegated_managed_identity_resource_id
  - Model RoleAssignment has a new parameter updated_by
  - Model RoleAssignment has a new parameter condition
  - Model RoleAssignment has a new parameter description
  - Model RoleAssignment has a new parameter updated_on
  - Model RoleAssignment has a new parameter condition_version
  - Model RoleAssignment has a new parameter created_by
  - Added operation RoleAssignmentsOperations.validate
  - Added operation RoleAssignmentsOperations.list_for_subscription
  - Added operation RoleAssignmentsOperations.validate_by_id
  - Added operation RoleAssignmentsOperations.create_by_id
  - Added operation RoleAssignmentsOperations.get_by_id
  - Added operation RoleAssignmentsOperations.delete_by_id
  - Added operation group AccessReviewInstancesAssignedForMyApprovalOperations
  - Added operation group RoleManagementPolicyAssignmentsOperations
  - Added operation group EligibleChildResourcesOperations
  - Added operation group AccessReviewInstanceDecisionsOperations
  - Added operation group RoleAssignmentSchedulesOperations
  - Added operation group RoleEligibilityScheduleRequestsOperations
  - Added operation group RoleEligibilitySchedulesOperations
  - Added operation group RoleAssignmentScheduleInstancesOperations
  - Added operation group AccessReviewInstanceMyDecisionsOperations
  - Added operation group RoleAssignmentApprovalStepOperations
  - Added operation group AccessReviewInstancesOperations
  - Added operation group AccessReviewScheduleDefinitionsOperations
  - Added operation group ScopeRoleAssignmentApprovalOperations
  - Added operation group RoleAssignmentScheduleRequestsOperations
  - Added operation group RoleAssignmentApprovalStepsOperations
  - Added operation group RoleAssignmentApprovalOperations
  - Added operation group ScopeRoleAssignmentApprovalStepsOperations
  - Added operation group AccessReviewDefaultSettingsOperations
  - Added operation group RoleEligibilityScheduleInstancesOperations
  - Added operation group AccessReviewScheduleDefinitionsAssignedForMyApprovalOperations
  - Added operation group ScopeRoleAssignmentApprovalStepOperations
  - Added operation group RoleAssignmentMetricsOperations
  - Added operation group RoleManagementPoliciesOperations
  - Added operation group Operations
  - Added operation group AccessReviewInstanceOperations

**Breaking changes**

  - Operation RoleAssignmentsOperations.list_for_resource has a new signature
  - Operation RoleAssignmentsOperations.delete has a new signature
  - Operation RoleAssignmentsOperations.get has a new signature
  - Operation RoleAssignmentsOperations.list_for_resource has a new signature
  - Operation RoleAssignmentsOperations.list_for_resource_group has a new signature
  - Operation RoleAssignmentsOperations.list_for_scope has a new signature
  - Model RoleAssignmentFilter no longer has parameter can_delegate
  - Model RoleAssignment no longer has parameter can_delegate
  - Model Principal has a new signature
  - Model RoleAssignmentCreateParameters has a new signature
  - Removed operation RoleAssignmentsOperations.list

## 1.0.0 (2020-11-23)

## 1.0.0b1 (2020-10-13)

This is beta preview version.

This version uses a next-generation code generator that introduces important breaking changes, but also important new features (like unified authentication and async programming).

**General breaking changes**

- Credential system has been completly revamped:

  - `azure.common.credentials` or `msrestazure.azure_active_directory` instances are no longer supported, use the `azure-identity` classes instead: https://pypi.org/project/azure-identity/
  - `credentials` parameter has been renamed `credential`

- The `config` attribute no longer exists on a client, configuration should be passed as kwarg. Example: `MyClient(credential, subscription_id, enable_logging=True)`. For a complete set of
  supported options, see the [parameters accept in init documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)
- You can't import a `version` module anymore, use `__version__` instead
- Operations that used to return a `msrest.polling.LROPoller` now returns a `azure.core.polling.LROPoller` and are prefixed with `begin_`.
- Exceptions tree have been simplified and most exceptions are now `azure.core.exceptions.HttpResponseError` (`CloudError` has been removed).
- Most of the operation kwarg have changed. Some of the most noticeable:

  - `raw` has been removed. Equivalent feature can be found using `cls`, a callback that will give access to internal HTTP response for advanced user
  - For a complete set of
  supported options, see the [parameters accept in Request documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)

**General new features**

- Type annotations support using `typing`. SDKs are mypy ready.
- This client has now stable and official support for async. Check the `aio` namespace of your package to find the async client.
- This client now support natively tracing library like OpenCensus or OpenTelemetry. See this [tracing quickstart](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-tracing-opentelemetry) for an overview.

## 0.61.0 (2020-08-10)

**Features**

  - Model RoleAssignmentCreateParameters has a new parameter condition
  - Model RoleAssignmentCreateParameters has a new parameter description
  - Model RoleAssignmentCreateParameters has a new parameter condition_version
  - Model RoleAssignment has a new parameter condition
  - Model RoleAssignment has a new parameter description
  - Model RoleAssignment has a new parameter condition_version

## 0.60.0 (2019-06-25)

**Breaking changes**

  - Rename elevate_access.post to global_administrator.elevate_access

**General Breaking changes**

This version uses a next-generation code generator that *might*
introduce breaking changes if you were importing from the v20xx_yy_zz
API folders. In summary, some modules were incorrectly
visible/importable and have been renamed. This fixed several issues
caused by usage of classes that were not supposed to be used in the
first place.

  - AuthorizationManagementClient cannot be imported from
    `azure.mgmt.authorization.v20xx_yy_zz.authorization_management_client`
    anymore (import from `azure.mgmt.authorization.v20xx_yy_zz`
    works like before)
  - AuthorizationManagementClientConfiguration import has been moved
    from
    `azure.mgmt.authorization.v20xx_yy_zz.authorization_management_client`
    to `azure.mgmt.authorization.v20xx_yy_zz`
  - A model `MyClass` from a "models" sub-module cannot be imported
    anymore using
    `azure.mgmt.authorization.v20xx_yy_zz.models.my_class` (import
    from `azure.mgmt.authorization.v20xx_yy_zz.models` works like
    before)
  - An operation class `MyClassOperations` from an `operations`
    sub-module cannot be imported anymore using
    `azure.mgmt.authorization.v20xx_yy_zz.operations.my_class_operations`
    (import from `azure.mgmt.authorization.v20xx_yy_zz.operations`
    works like before)

Last but not least, HTTP connection pooling is now enabled by default.
You should always use a client as a context manager, or call close(), or
use no more than one client per process.

## 0.52.0 (2019-05-23)

**Features**

  - Add elevate_access API

## 0.51.1 (2018-11-27)

**Bugfixes**

  - Missing principal_type in role assignment class #3802

## 0.51.0 (2018-11-12)

**Features**

  - Model RoleAssignmentCreateParameters has a new parameter
    principal_type

**Breaking changes**

  - Parameter role_definition_id of model
    RoleAssignmentCreateParameters is now required
  - Parameter principal_id of model RoleAssignmentCreateParameters is
    now required

Role Assignments API version is now 2018-09-01-preview

## 0.50.0 (2018-05-29)

**Features**

  - Support Azure Stack (multi API versionning)
  - Client class can be used as a context manager to keep the underlying
    HTTP session open for performance

**Bugfixes**

  - Compatibility of the sdist with wheel 0.31.0

## 0.40.0 (2018-03-13)

**Breaking changes**

  - Several properties have been flattened and "properties" attribute is
    not needed anymore (e.g. properties.email_address =>
    email_address)
  - Some method signature change (e.g. create_by_id)

**Features**

  - Adding attributes data_actions / not_data_actions /
    is_data_actions

API version is now 2018-01-01-preview

## 0.30.0 (2017-04-28)

  - Initial Release
  - This wheel package is built with the azure wheel extension
