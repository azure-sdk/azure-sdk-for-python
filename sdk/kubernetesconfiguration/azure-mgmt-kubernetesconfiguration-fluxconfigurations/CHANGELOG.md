# Release History

## 1.0.0 (2026-03-16)

### Features Added

  - Model `KubernetesConfigurationFluxConfigurationsMgmtClient` added parameter `cloud_setting` in method `__init__`
  - Client `KubernetesConfigurationFluxConfigurationsMgmtClient` added method `send_request`
  - Model `ProxyResource` added property `system_data`
  - Model `Resource` added property `system_data`
  - Added model `FluxConfigurationPatchProperties`

### Breaking Changes

  - Model `FluxConfigurationPatch` deleted or renamed its instance variable `source_kind`
  - Model `FluxConfigurationPatch` deleted or renamed its instance variable `suspend`
  - Model `FluxConfigurationPatch` deleted or renamed its instance variable `git_repository`
  - Model `FluxConfigurationPatch` deleted or renamed its instance variable `bucket`
  - Model `FluxConfigurationPatch` deleted or renamed its instance variable `azure_blob`
  - Model `FluxConfigurationPatch` deleted or renamed its instance variable `oci_repository`
  - Model `FluxConfigurationPatch` deleted or renamed its instance variable `kustomizations`
  - Model `FluxConfigurationPatch` deleted or renamed its instance variable `configuration_protected_settings`
  - Deleted or renamed model `FluxConfigurationsList`
  - Deleted or renamed model `KustomizationValidationType`
  - Method `FluxConfigurationsOperations.begin_delete` changed its parameter `force_delete` from `positional_or_keyword` to `keyword_only`

## 1.0.0b1 (2025-05-19)

### Other Changes

  - Initial version
