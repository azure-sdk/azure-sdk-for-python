# Release History

## 2.0.0 (2025-04-09)

### Features Added

  - Model `MarketplaceSaaSInfo` added property `publisher_id`
  - Model `MarketplaceSaaSInfo` added property `offer_id`
  - Added model `ResubscribeProperties`
  - Model `MonitoredSubscriptionsOperations` added method `begin_create_or_update`
  - Model `MonitorsOperations` added method `begin_resubscribe`
  - Model `MonitorsOperations` added method `begin_update`
  - Model `MonitorsOperations` added method `refresh_ingestion_key`
  - Method `MonitoredSubscriptionsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, monitor_name: str, configuration_name: Union[str, ConfigurationName], body: Optional[IO[bytes]], content_type: str)`
  - Method `MonitoredSubscriptionsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, monitor_name: str, configuration_name: Union[str, ConfigurationName], body: Optional[MonitoredSubscriptionProperties], content_type: str)`
  - Method `MonitoredSubscriptionsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, monitor_name: str, configuration_name: Union[str, ConfigurationName], body: Optional[IO[bytes]], content_type: str)`
  - Method `MonitorsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, monitor_name: str, resource: IO[bytes], content_type: str)`
  - Method `MonitorsOperations.get_metric_rules` has a new overload `def get_metric_rules(self: None, resource_group_name: str, monitor_name: str, request: IO[bytes], content_type: str)`
  - Method `MonitorsOperations.get_metric_status` has a new overload `def get_metric_status(self: None, resource_group_name: str, monitor_name: str, request: IO[bytes], content_type: str)`
  - Method `MonitorsOperations.list_app_services` has a new overload `def list_app_services(self: None, resource_group_name: str, monitor_name: str, request: IO[bytes], content_type: str)`
  - Method `MonitorsOperations.list_hosts` has a new overload `def list_hosts(self: None, resource_group_name: str, monitor_name: str, request: IO[bytes], content_type: str)`
  - Method `MonitorsOperations.switch_billing` has a new overload `def switch_billing(self: None, resource_group_name: str, monitor_name: str, request: IO[bytes], content_type: str)`
  - Method `MonitorsOperations.begin_resubscribe` has a new overload `def begin_resubscribe(self: None, resource_group_name: str, monitor_name: str, body: Optional[ResubscribeProperties], content_type: str)`
  - Method `MonitorsOperations.begin_resubscribe` has a new overload `def begin_resubscribe(self: None, resource_group_name: str, monitor_name: str, body: Optional[IO[bytes]], content_type: str)`
  - Method `MonitorsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, monitor_name: str, properties: NewRelicMonitorResourceUpdate, content_type: str)`
  - Method `MonitorsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, monitor_name: str, properties: IO[bytes], content_type: str)`
  - Method `TagRulesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, monitor_name: str, rule_set_name: str, resource: IO[bytes], content_type: str)`
  - Method `TagRulesOperations.update` has a new overload `def update(self: None, resource_group_name: str, monitor_name: str, rule_set_name: str, properties: IO[bytes], content_type: str)`

### Breaking Changes

  - Deleted or renamed model `BillingCycle`
  - Deleted or renamed method `MonitoredSubscriptionsOperations.begin_createor_update`
  - Deleted or renamed method `MonitorsOperations.update`

## 1.1.0 (2024-03-18)

### Features Added

  - Added operation MonitorsOperations.list_linked_resources
  - Added operation group BillingInfoOperations
  - Added operation group ConnectedPartnerResourcesOperations
  - Added operation group MonitoredSubscriptionsOperations
  - Model NewRelicMonitorResource has a new parameter saa_s_azure_subscription_status
  - Model NewRelicMonitorResource has a new parameter subscription_state

## 1.0.0 (2023-05-20)

### Other Changes

  - First GA

## 1.0.0b1 (2023-03-24)

* Initial Release
