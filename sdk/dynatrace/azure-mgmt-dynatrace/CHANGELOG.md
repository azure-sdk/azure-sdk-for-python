# Release History

## 2.1.0 (2025-04-11)

### Features Added

  - Client `DynatraceObservabilityMgmtClient` added operation group `monitored_subscriptions`
  - Client `DynatraceObservabilityMgmtClient` added operation group `creation_supported`
  - Model `AccountInfo` added property `company_name`
  - Model `MarketplaceSaaSResourceDetailsResponse` added property `marketplace_saa_s_resource_name`
  - Enum `MarketplaceSubscriptionStatus` added member `UNSUBSCRIBED`
  - Model `MonitorResource` added property `marketplace_saas_auto_renew`
  - Model `MonitorResourceUpdate` added property `properties`
  - Model `MonitorResourceUpdate` added property `identity`
  - Enum `MonitoringType` added member `DISCOVERY`
  - Model `ProxyResource` added property `system_data`
  - Model `Resource` added property `system_data`
  - Model `TrackedResource` added property `system_data`
  - Added enum `Action`
  - Added model `AgentStatus`
  - Added model `AgentStatusRequest`
  - Added model `ConnectedResourcesCountResponse`
  - Added model `CreateResourceSupportedProperties`
  - Added model `CreateResourceSupportedResponse`
  - Added model `LogStatusRequest`
  - Added model `ManagedServiceIdentity`
  - Added enum `ManagedServiceIdentityType`
  - Added enum `MarketplaceSaasAutoRenew`
  - Added model `MarketplaceSubscriptionIdRequest`
  - Added model `MetricStatusRequest`
  - Added model `MonitorUpdateProperties`
  - Added model `MonitoredSubscription`
  - Added model `MonitoredSubscriptionProperties`
  - Added model `MonitoredSubscriptionPropertiesList`
  - Added model `MonitoringTagRulesProperties`
  - Added enum `Status`
  - Added model `SubscriptionList`
  - Added enum `SubscriptionListOperation`
  - Added model `UpgradePlanRequest`
  - Model `MonitorsOperations` added method `begin_upgrade_plan`
  - Model `MonitorsOperations` added method `get_all_connected_resources_count`
  - Model `MonitorsOperations` added method `update_agent_status`
  - Added model `CreationSupportedOperations`
  - Added model `MonitoredSubscriptionsOperations`
  - Method `MonitorsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, monitor_name: str, resource: IO[bytes], content_type: str)`
  - Method `MonitorsOperations.get_marketplace_saa_s_resource_details` has a new overload `def get_marketplace_saa_s_resource_details(self: None, request: IO[bytes], content_type: str)`
  - Method `MonitorsOperations.get_metric_status` has a new overload `def get_metric_status(self: None, resource_group_name: str, monitor_name: str, request: Optional[MetricStatusRequest], content_type: str)`
  - Method `MonitorsOperations.get_metric_status` has a new overload `def get_metric_status(self: None, resource_group_name: str, monitor_name: str, request: Optional[IO[bytes]], content_type: str)`
  - Method `MonitorsOperations.get_sso_details` has a new overload `def get_sso_details(self: None, resource_group_name: str, monitor_name: str, request: Optional[IO[bytes]], content_type: str)`
  - Method `MonitorsOperations.list_linkable_environments` has a new overload `def list_linkable_environments(self: None, resource_group_name: str, monitor_name: str, request: IO[bytes], content_type: str)`
  - Method `MonitorsOperations.list_monitored_resources` has a new overload `def list_monitored_resources(self: None, resource_group_name: str, monitor_name: str, request: Optional[LogStatusRequest], content_type: str)`
  - Method `MonitorsOperations.list_monitored_resources` has a new overload `def list_monitored_resources(self: None, resource_group_name: str, monitor_name: str, request: Optional[IO[bytes]], content_type: str)`
  - Method `MonitorsOperations.update` has a new overload `def update(self: None, resource_group_name: str, monitor_name: str, resource: IO[bytes], content_type: str)`
  - Method `MonitorsOperations.begin_upgrade_plan` has a new overload `def begin_upgrade_plan(self: None, resource_group_name: str, monitor_name: str, request: UpgradePlanRequest, content_type: str)`
  - Method `MonitorsOperations.begin_upgrade_plan` has a new overload `def begin_upgrade_plan(self: None, resource_group_name: str, monitor_name: str, request: IO[bytes], content_type: str)`
  - Method `MonitorsOperations.get_all_connected_resources_count` has a new overload `def get_all_connected_resources_count(self: None, request: MarketplaceSubscriptionIdRequest, content_type: str)`
  - Method `MonitorsOperations.get_all_connected_resources_count` has a new overload `def get_all_connected_resources_count(self: None, request: IO[bytes], content_type: str)`
  - Method `MonitorsOperations.update_agent_status` has a new overload `def update_agent_status(self: None, resource_group_name: str, monitor_name: str, request: AgentStatusRequest, content_type: str)`
  - Method `MonitorsOperations.update_agent_status` has a new overload `def update_agent_status(self: None, resource_group_name: str, monitor_name: str, request: IO[bytes], content_type: str)`
  - Method `SingleSignOnOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, monitor_name: str, configuration_name: str, resource: IO[bytes], content_type: str)`
  - Method `TagRulesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, monitor_name: str, rule_set_name: str, resource: IO[bytes], content_type: str)`
  - Method `MonitoredSubscriptionsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, monitor_name: str, body: Optional[MonitoredSubscriptionProperties], content_type: str)`
  - Method `MonitoredSubscriptionsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, monitor_name: str, body: Optional[IO[bytes]], content_type: str)`
  - Method `MonitoredSubscriptionsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, monitor_name: str, body: Optional[MonitoredSubscriptionProperties], content_type: str)`
  - Method `MonitoredSubscriptionsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, monitor_name: str, body: Optional[IO[bytes]], content_type: str)`

## 2.0.0 (2023-08-18)

### Features Added

  - Added operation MonitorsOperations.get_marketplace_saa_s_resource_details
  - Added operation MonitorsOperations.get_metric_status
  - Model MetricRules has a new parameter sending_metrics

### Breaking Changes

  - Model MonitorResourceUpdate no longer has parameter dynatrace_environment_properties
  - Model MonitorResourceUpdate no longer has parameter marketplace_subscription_status
  - Model MonitorResourceUpdate no longer has parameter monitoring_status
  - Model MonitorResourceUpdate no longer has parameter plan_data
  - Model MonitorResourceUpdate no longer has parameter user_info
  - Parameter region of model LinkableEnvironmentRequest is now required
  - Parameter tenant_id of model LinkableEnvironmentRequest is now required
  - Parameter user_principal of model LinkableEnvironmentRequest is now required
  - Parameter user_principal of model SSODetailsRequest is now required
  - Removed operation MonitorsOperations.get_account_credentials
  - Removed operation TagRulesOperations.update

## 1.1.0b1 (2022-12-27)

### Other Changes

  - Added generated samples in github repo
  - Drop support for python<3.7.0

## 1.0.0 (2022-09-16)

### Breaking Changes

  - Client name is changed from `DynatraceObservability` to `DynatraceObservabilityMgmtClient`

## 1.0.0b1 (2022-05-19)

* Initial Release
