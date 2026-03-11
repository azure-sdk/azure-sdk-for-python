# Release History

## 1.0.0b2 (2026-03-11)

### Features Added

  - Model `TrafficCollectorMgmtClient` added parameter `cloud_setting` in method `__init__`
  - Client `TrafficCollectorMgmtClient` added method `send_request`
  - Model `AzureTrafficCollector` added property `properties`
  - Model `CollectorPolicy` added property `properties`
  - Model `ProxyResource` added property `system_data`
  - Model `SystemData` added property `last_modified_at`
  - Added model `AzureTrafficCollectorPropertiesFormat`
  - Added model `CloudError`
  - Added model `CollectorPolicyPropertiesFormat`
  - Added model `Resource`

### Breaking Changes

  - Model `AzureTrafficCollector` deleted or renamed its instance variable `collector_policies`
  - Model `AzureTrafficCollector` deleted or renamed its instance variable `virtual_hub`
  - Model `AzureTrafficCollector` deleted or renamed its instance variable `provisioning_state`
  - Model `CollectorPolicy` deleted or renamed its instance variable `ingestion_policy`
  - Model `CollectorPolicy` deleted or renamed its instance variable `emission_policies`
  - Model `CollectorPolicy` deleted or renamed its instance variable `provisioning_state`
  - Deleted or renamed model `ApiVersionParameter`
  - Deleted or renamed model `TrackedResource`
  - Deleted or renamed model `TrackedResourceSystemData`
  - Method `AzureTrafficCollectorsOperations.begin_create_or_update` inserted a `positional_or_keyword` parameter `parameters`
  - Method `AzureTrafficCollectorsOperations.begin_create_or_update` deleted or renamed its parameter `location` of kind `positional_or_keyword`
  - Method `AzureTrafficCollectorsOperations.begin_create_or_update` deleted or renamed its parameter `tags` of kind `positional_or_keyword`
  - Method `AzureTrafficCollectorsOperations.begin_create_or_update` deleted or renamed its parameter `virtual_hub` of kind `positional_or_keyword`
  - Method `CollectorPoliciesOperations.begin_create_or_update` inserted a `positional_or_keyword` parameter `parameters`
  - Method `CollectorPoliciesOperations.begin_create_or_update` deleted or renamed its parameter `location` of kind `positional_or_keyword`
  - Method `CollectorPoliciesOperations.begin_create_or_update` deleted or renamed its parameter `tags` of kind `positional_or_keyword`
  - Method `CollectorPoliciesOperations.begin_create_or_update` deleted or renamed its parameter `ingestion_policy` of kind `positional_or_keyword`
  - Method `CollectorPoliciesOperations.begin_create_or_update` deleted or renamed its parameter `emission_policies` of kind `positional_or_keyword`

## 1.0.0b1 (2022-11-18)

* Initial Release
