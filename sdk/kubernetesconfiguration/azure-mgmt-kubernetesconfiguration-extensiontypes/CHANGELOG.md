# Release History

## 1.0.0b2 (2026-03-16)

### Features Added

  - Model `KubernetesConfigurationExtensionTypesMgmtClient` added parameter `cloud_setting` in method `__init__`
  - Client `KubernetesConfigurationExtensionTypesMgmtClient` added method `send_request`
  - Model `ClusterScopeSettings` added property `system_data`
  - Model `ExtensionType` added property `system_data`
  - Model `ExtensionTypeVersionForReleaseTrain` added property `system_data`
  - Model `ProxyResource` added property `system_data`
  - Model `Resource` added property `system_data`
  - Added enum `CreatedByType`
  - Added model `SystemData`

### Breaking Changes

  - Deleted or renamed model `ExtensionTypeVersionsList`
  - Deleted or renamed model `ExtensionTypesList`
  - Method `ExtensionTypesOperations.cluster_list_versions` changed its parameter `release_train` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.cluster_list_versions` changed its parameter `major_version` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.cluster_list_versions` changed its parameter `show_latest` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.list` changed its parameter `publisher_id` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.list` changed its parameter `offer_id` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.list` changed its parameter `plan_id` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.list` changed its parameter `release_train` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.list_versions` changed its parameter `release_train` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.list_versions` changed its parameter `cluster_type` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.list_versions` changed its parameter `major_version` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.list_versions` changed its parameter `show_latest` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.location_list` changed its parameter `publisher_id` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.location_list` changed its parameter `offer_id` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.location_list` changed its parameter `plan_id` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.location_list` changed its parameter `release_train` from `positional_or_keyword` to `keyword_only`
  - Method `ExtensionTypesOperations.location_list` changed its parameter `cluster_type` from `positional_or_keyword` to `keyword_only`

## 1.0.0b1 (2025-05-19)

### Other Changes

  - Initial version
