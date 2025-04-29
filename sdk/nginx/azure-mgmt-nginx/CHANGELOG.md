# Release History

## 3.1.0b3 (2025-04-29)

### Features Added

  - Model `NginxCertificate` added property `provisioning_state`
  - Model `NginxCertificate` added property `key_virtual_path`
  - Model `NginxCertificate` added property `certificate_virtual_path`
  - Model `NginxCertificate` added property `key_vault_secret_id`
  - Model `NginxCertificate` added property `sha1_thumbprint`
  - Model `NginxCertificate` added property `key_vault_secret_version`
  - Model `NginxCertificate` added property `key_vault_secret_created`
  - Model `NginxCertificate` added property `certificate_error`
  - Model `NginxConfigurationResponse` added property `provisioning_state`
  - Model `NginxConfigurationResponse` added property `files`
  - Model `NginxConfigurationResponse` added property `protected_files`
  - Model `NginxConfigurationResponse` added property `package`
  - Model `NginxConfigurationResponse` added property `root_file`
  - Model `NginxDeployment` added property `provisioning_state`
  - Model `NginxDeployment` added property `nginx_version`
  - Model `NginxDeployment` added property `network_profile`
  - Model `NginxDeployment` added property `ip_address`
  - Model `NginxDeployment` added property `enable_diagnostics_support`
  - Model `NginxDeployment` added property `logging`
  - Model `NginxDeployment` added property `scaling_properties`
  - Model `NginxDeployment` added property `auto_upgrade_profile`
  - Model `NginxDeployment` added property `user_profile`
  - Model `NginxDeployment` added property `nginx_app_protect`
  - Model `NginxDeployment` added property `dataplane_api_endpoint`
  - Model `NginxDeploymentApiKeyResponse` added property `hint`
  - Model `NginxDeploymentApiKeyResponse` added property `end_date_time`
  - Model `NginxDeploymentApiKeyResponse` added property `system_data`
  - Added enum `ActionType`
  - Added model `AzureResourceManagerArmResponseNginxDeployment`
  - Added model `AzureResourceManagerResourceSkuProperty`
  - Added model `Operation`
  - Added enum `Origin`
  - Added model `ProxyResource`
  - Added model `Resource`
  - Added model `Sku`
  - Added enum `SkuTier`
  - Added model `TrackedResource`
  - Method `ApiKeysOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, deployment_name: str, api_key_name: str, body: NginxDeploymentApiKeyResponse, content_type: str)`
  - Method `ApiKeysOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, deployment_name: str, api_key_name: str, body: IO[bytes], content_type: str)`
  - Method `CertificatesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, deployment_name: str, certificate_name: str, body: NginxCertificate, content_type: str)`
  - Method `CertificatesOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, deployment_name: str, certificate_name: str, body: IO[bytes], content_type: str)`
  - Method `ConfigurationsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, deployment_name: str, configuration_name: str, body: NginxConfigurationResponse, content_type: str)`
  - Method `ConfigurationsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, deployment_name: str, configuration_name: str, body: IO[bytes], content_type: str)`
  - Method `DeploymentsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, deployment_name: str, body: NginxDeployment, content_type: str)`
  - Method `DeploymentsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, deployment_name: str, body: IO[bytes], content_type: str)`
  - Method `DeploymentsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, deployment_name: str, body: NginxDeploymentUpdateParameters, content_type: str)`
  - Method `DeploymentsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, deployment_name: str, body: IO[bytes], content_type: str)`

### Breaking Changes

  - Model `NginxCertificate` deleted or renamed its instance variable `properties`
  - Method `NginxCertificateListResponse.__init__` removed default value `None` from its parameter `value`
  - Method `NginxConfigurationListResponse.__init__` removed default value `None` from its parameter `value`
  - Model `NginxConfigurationResponse` deleted or renamed its instance variable `properties`
  - Model `NginxDeployment` deleted or renamed its instance variable `properties`
  - Method `NginxDeployment.__init__` removed default value `None` from its parameter `location`
  - Method `NginxDeploymentApiKeyListResponse.__init__` removed default value `None` from its parameter `value`
  - Model `NginxDeploymentApiKeyResponse` deleted or renamed its instance variable `properties`
  - Method `NginxDeploymentListResponse.__init__` removed default value `None` from its parameter `value`
  - Deleted or renamed model `NginxCertificateProperties`
  - Deleted or renamed model `NginxConfigurationRequest`
  - Deleted or renamed model `NginxConfigurationRequestProperties`
  - Deleted or renamed model `NginxConfigurationResponseProperties`
  - Deleted or renamed model `NginxDeploymentApiKeyRequest`
  - Deleted or renamed model `NginxDeploymentApiKeyRequestProperties`
  - Deleted or renamed model `NginxDeploymentApiKeyResponseProperties`
  - Deleted or renamed model `NginxDeploymentProperties`
  - Deleted or renamed model `OperationResult`
  - Deleted or renamed model `ResourceSku`
  - Method `ApiKeysOperations.create_or_update` removed default value `None` from its parameter `body`
  - Method `CertificatesOperations.begin_create_or_update` removed default value `None` from its parameter `body`
  - Method `ConfigurationsOperations.begin_create_or_update` removed default value `None` from its parameter `body`
  - Method `DeploymentsOperations.begin_create_or_update` removed default value `None` from its parameter `body`
  - Method `DeploymentsOperations.begin_update` removed default value `None` from its parameter `body`

## 3.1.0b2 (2025-02-23)

### Features Added

  - Client `NginxManagementClient` added operation group `api_keys`
  - Model `AnalysisResultData` added property `diagnostics`
  - Model `NginxDeploymentProperties` added property `nginx_app_protect`
  - Model `NginxDeploymentProperties` added property `dataplane_api_endpoint`
  - Model `NginxDeploymentUpdateProperties` added property `network_profile`
  - Model `NginxDeploymentUpdateProperties` added property `nginx_app_protect`
  - Added enum `ActivationState`
  - Added model `DiagnosticItem`
  - Added model `ErrorResponse`
  - Added enum `Level`
  - Added model `NginxConfigurationProtectedFileRequest`
  - Added model `NginxConfigurationProtectedFileResponse`
  - Added model `NginxConfigurationRequest`
  - Added model `NginxConfigurationRequestProperties`
  - Added model `NginxConfigurationResponse`
  - Added model `NginxConfigurationResponseProperties`
  - Added model `NginxDeploymentApiKeyListResponse`
  - Added model `NginxDeploymentApiKeyRequest`
  - Added model `NginxDeploymentApiKeyRequestProperties`
  - Added model `NginxDeploymentApiKeyResponse`
  - Added model `NginxDeploymentApiKeyResponseProperties`
  - Added model `NginxDeploymentPropertiesNginxAppProtect`
  - Added model `NginxDeploymentUpdatePropertiesNginxAppProtect`
  - Added model `WebApplicationFirewallComponentVersions`
  - Added model `WebApplicationFirewallPackage`
  - Added model `WebApplicationFirewallSettings`
  - Added model `WebApplicationFirewallStatus`
  - Added operation group `ApiKeysOperations`

### Breaking Changes

  - Model `NginxDeploymentProperties` deleted or renamed its instance variable `managed_resource_group`
  - Deleted or renamed model `NginxConfiguration`
  - Deleted or renamed model `NginxConfigurationProperties`
  - Deleted or renamed model `ResourceProviderDefaultErrorResponse`

## 3.1.0b1 (2024-03-18)

### Features Added

  - Added operation ConfigurationsOperations.analysis
  - Model NginxCertificateProperties has a new parameter certificate_error
  - Model NginxCertificateProperties has a new parameter key_vault_secret_created
  - Model NginxCertificateProperties has a new parameter key_vault_secret_version
  - Model NginxCertificateProperties has a new parameter sha1_thumbprint
  - Model NginxDeploymentProperties has a new parameter auto_upgrade_profile
  - Model NginxDeploymentScalingProperties has a new parameter profiles
  - Model NginxDeploymentUpdateProperties has a new parameter auto_upgrade_profile

## 3.0.0 (2023-11-20)

### Features Added

  - Model NginxConfigurationPackage has a new parameter protected_files
  - Model NginxDeploymentProperties has a new parameter scaling_properties
  - Model NginxDeploymentProperties has a new parameter user_profile
  - Model NginxDeploymentUpdateProperties has a new parameter scaling_properties
  - Model NginxDeploymentUpdateProperties has a new parameter user_profile

### Breaking Changes

  - Model NginxCertificate no longer has parameter tags
  - Model NginxConfiguration no longer has parameter tags

## 2.1.0 (2023-03-14)

### Other Changes

  - Regular update

## 2.1.0b1 (2022-12-29)

### Other Changes

  - Added generated samples in github repo
  - Drop support for python<3.7.0

## 2.0.0 (2022-10-18)

### Features Added

  - Added operation CertificatesOperations.begin_create_or_update
  - Added operation DeploymentsOperations.begin_create_or_update

### Breaking Changes

  - Removed operation CertificatesOperations.begin_create
  - Removed operation DeploymentsOperations.begin_create

## 1.1.0 (2022-09-20)

### Features Added

  - Model NginxConfigurationProperties has a new parameter protected_files

## 1.0.0 (2022-08-26)

### Features Added

  - Model NginxDeploymentProperties has a new parameter logging
  - Model NginxDeploymentUpdateProperties has a new parameter logging

## 1.0.0b1 (2022-06-13)

* Initial Release
