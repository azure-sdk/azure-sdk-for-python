# Release History

## 1.0.0 (2026-03-16)

### Features Added

  - Model `KubernetesConfigurationExtensionsMgmtClient` added parameter `cloud_setting` in method `__init__`
  - Client `KubernetesConfigurationExtensionsMgmtClient` added method `send_request`
  - Model `ProxyResource` added property `system_data`
  - Model `Resource` added property `system_data`
  - Added model `PatchExtensionProperties`
  - Added enum `ResourceIdentityType`

### Breaking Changes

  - Model `PatchExtension` deleted or renamed its instance variable `auto_upgrade_minor_version`
  - Model `PatchExtension` deleted or renamed its instance variable `release_train`
  - Model `PatchExtension` deleted or renamed its instance variable `version`
  - Model `PatchExtension` deleted or renamed its instance variable `configuration_settings`
  - Model `PatchExtension` deleted or renamed its instance variable `configuration_protected_settings`
  - Deleted or renamed model `ExtensionsList`
  - Method `ExtensionsOperations.begin_delete` changed its parameter `force_delete` from `positional_or_keyword` to `keyword_only`

## 1.0.0b1 (2025-05-19)

### Other Changes

  - Initial version
