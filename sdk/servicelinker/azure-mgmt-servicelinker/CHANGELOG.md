# Release History

## 1.2.0b4 (2025-05-07)

### Features Added

  - Added model `AzureResourceManagerArmResponseDryrunResource`
  - Added model `AzureResourceManagerArmResponseValidateOperationResult`
  - Method `ConnectorOperations.begin_create_dryrun` has a new overload `def begin_create_dryrun(self: None, resource_group_name: str, location: str, dryrun_name: str, parameters: DryrunResource, content_type: str)`
  - Method `ConnectorOperations.begin_create_dryrun` has a new overload `def begin_create_dryrun(self: None, resource_group_name: str, location: str, dryrun_name: str, parameters: IO[bytes], content_type: str)`
  - Method `ConnectorOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, location: str, connector_name: str, parameters: LinkerResource, content_type: str)`
  - Method `ConnectorOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, location: str, connector_name: str, parameters: IO[bytes], content_type: str)`
  - Method `ConnectorOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, location: str, connector_name: str, parameters: LinkerPatch, content_type: str)`
  - Method `ConnectorOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, location: str, connector_name: str, parameters: IO[bytes], content_type: str)`
  - Method `ConnectorOperations.begin_update_dryrun` has a new overload `def begin_update_dryrun(self: None, resource_group_name: str, location: str, dryrun_name: str, parameters: DryrunPatch, content_type: str)`
  - Method `ConnectorOperations.begin_update_dryrun` has a new overload `def begin_update_dryrun(self: None, resource_group_name: str, location: str, dryrun_name: str, parameters: IO[bytes], content_type: str)`
  - Method `ConnectorOperations.generate_configurations` has a new overload `def generate_configurations(self: None, resource_group_name: str, location: str, connector_name: str, parameters: Optional[ConfigurationInfo], content_type: str)`
  - Method `ConnectorOperations.generate_configurations` has a new overload `def generate_configurations(self: None, resource_group_name: str, location: str, connector_name: str, parameters: Optional[IO[bytes]], content_type: str)`
  - Method `LinkerOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, providers: str, linkers: str, resource_uri: str, linker_name: str, parameters: LinkerResource, content_type: str)`
  - Method `LinkerOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, providers: str, linkers: str, resource_uri: str, linker_name: str, parameters: IO[bytes], content_type: str)`
  - Method `LinkerOperations.update` has a new overload `def update(self: None, providers: str, linkers: str, resource_uri: str, linker_name: str, parameters: LinkerPatch, content_type: str)`
  - Method `LinkerOperations.update` has a new overload `def update(self: None, providers: str, linkers: str, resource_uri: str, linker_name: str, parameters: IO[bytes], content_type: str)`
  - Method `LinkersOperations.begin_create_dryrun` has a new overload `def begin_create_dryrun(self: None, providers: str, dryruns: str, resource_uri: str, dryrun_name: str, parameters: DryrunResource, content_type: str)`
  - Method `LinkersOperations.begin_create_dryrun` has a new overload `def begin_create_dryrun(self: None, providers: str, dryruns: str, resource_uri: str, dryrun_name: str, parameters: IO[bytes], content_type: str)`
  - Method `LinkersOperations.begin_update_dryrun` has a new overload `def begin_update_dryrun(self: None, providers: str, dryruns: str, resource_uri: str, dryrun_name: str, parameters: DryrunPatch, content_type: str)`
  - Method `LinkersOperations.begin_update_dryrun` has a new overload `def begin_update_dryrun(self: None, providers: str, dryruns: str, resource_uri: str, dryrun_name: str, parameters: IO[bytes], content_type: str)`
  - Method `LinkersOperations.generate_configurations` has a new overload `def generate_configurations(self: None, providers: str, linkers: str, resource_uri: str, linker_name: str, parameters: Optional[ConfigurationInfo], content_type: str)`
  - Method `LinkersOperations.generate_configurations` has a new overload `def generate_configurations(self: None, providers: str, linkers: str, resource_uri: str, linker_name: str, parameters: Optional[IO[bytes]], content_type: str)`

### Breaking Changes

  - Method `ServiceLinkerManagementClient.__init__` inserted a `positional_or_keyword` parameter `subscription_id`
  - Deleted or renamed enum value `ActionType.ENABLE`
  - Deleted or renamed enum value `ActionType.OPT_OUT`
  - Method `ConfigurationNameResult.__init__` removed default value `None` from its parameter `value`
  - Method `DaprConfigurationList.__init__` removed default value `None` from its parameter `value`
  - Method `DryrunList.__init__` removed default value `None` from its parameter `value`
  - Method `ResourceList.__init__` removed default value `None` from its parameter `value`
  - Deleted or renamed model `DatabaseAadAuthInfo`
  - Deleted or renamed model `LinkerProperties`
  - Method `ConnectorOperations.begin_create_dryrun` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ConnectorOperations.begin_create_or_update` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ConnectorOperations.begin_delete` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ConnectorOperations.begin_update` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ConnectorOperations.begin_update_dryrun` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ConnectorOperations.begin_validate` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ConnectorOperations.delete_dryrun` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ConnectorOperations.generate_configurations` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ConnectorOperations.get` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ConnectorOperations.get_dryrun` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ConnectorOperations.list` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `ConnectorOperations.list_dryrun` deleted or renamed its parameter `subscription_id` of kind `positional_or_keyword`
  - Method `LinkerOperations.begin_create_or_update` inserted a `positional_or_keyword` parameter `providers`
  - Method `LinkerOperations.begin_create_or_update` inserted a `positional_or_keyword` parameter `linkers`
  - Method `LinkerOperations.begin_delete` inserted a `positional_or_keyword` parameter `providers`
  - Method `LinkerOperations.begin_delete` inserted a `positional_or_keyword` parameter `linkers`
  - Method `LinkerOperations.begin_validate` inserted a `positional_or_keyword` parameter `providers`
  - Method `LinkerOperations.begin_validate` inserted a `positional_or_keyword` parameter `linkers`
  - Method `LinkerOperations.get` inserted a `positional_or_keyword` parameter `providers`
  - Method `LinkerOperations.get` inserted a `positional_or_keyword` parameter `linkers`
  - Method `LinkerOperations.list` inserted a `positional_or_keyword` parameter `providers`
  - Method `LinkerOperations.list_configurations` inserted a `positional_or_keyword` parameter `providers`
  - Method `LinkerOperations.list_configurations` inserted a `positional_or_keyword` parameter `linkers`
  - Deleted or renamed method `LinkerOperations.begin_update`
  - Method `LinkersOperations.begin_create_dryrun` inserted a `positional_or_keyword` parameter `providers`
  - Method `LinkersOperations.begin_create_dryrun` inserted a `positional_or_keyword` parameter `dryruns`
  - Method `LinkersOperations.begin_update_dryrun` inserted a `positional_or_keyword` parameter `providers`
  - Method `LinkersOperations.begin_update_dryrun` inserted a `positional_or_keyword` parameter `dryruns`
  - Method `LinkersOperations.delete_dryrun` inserted a `positional_or_keyword` parameter `providers`
  - Method `LinkersOperations.delete_dryrun` inserted a `positional_or_keyword` parameter `dryruns`
  - Method `LinkersOperations.generate_configurations` inserted a `positional_or_keyword` parameter `providers`
  - Method `LinkersOperations.generate_configurations` inserted a `positional_or_keyword` parameter `linkers`
  - Method `LinkersOperations.get_dryrun` inserted a `positional_or_keyword` parameter `providers`
  - Method `LinkersOperations.get_dryrun` inserted a `positional_or_keyword` parameter `dryruns`
  - Method `LinkersOperations.list_dryrun` inserted a `positional_or_keyword` parameter `providers`

## 1.2.0b3 (2024-10-11)

### Features Added

  - Enum `AzureResourceType` added member `APP_CONFIG`
  - Enum `TargetServiceType` added member `FABRIC_PLATFORM`
  - Added model `AzureAppConfigProperties`
  - Added model `FabricPlatform`

## 1.2.0b2 (2024-03-19)

### Features Added

  - Added operation LinkersOperations.list_dapr_configurations
  - Model AccessKeyInfoBase has a new parameter auth_mode
  - Model AuthInfoBase has a new parameter auth_mode
  - Model ConfigurationInfo has a new parameter additional_connection_string_properties
  - Model ConfigurationInfo has a new parameter configuration_store
  - Model ConfigurationInfo has a new parameter dapr_properties
  - Model ConfigurationName has a new parameter required
  - Model ConfigurationNameItem has a new parameter dapr_properties
  - Model ConfigurationNameItem has a new parameter secret_type
  - Model SecretAuthInfo has a new parameter auth_mode
  - Model ServicePrincipalCertificateAuthInfo has a new parameter auth_mode
  - Model ServicePrincipalSecretAuthInfo has a new parameter auth_mode
  - Model SourceConfiguration has a new parameter config_type
  - Model SourceConfiguration has a new parameter description
  - Model SourceConfiguration has a new parameter key_vault_reference_identity
  - Model SystemAssignedIdentityAuthInfo has a new parameter auth_mode
  - Model UserAccountAuthInfo has a new parameter auth_mode
  - Model UserAssignedIdentityAuthInfo has a new parameter auth_mode

## 1.2.0b1 (2022-12-02)

### Features Added

  - Added operation group ConfigurationNamesOperations
  - Added operation group ConnectorOperations
  - Added operation group LinkersOperations
  - Model LinkerPatch has a new parameter configuration_info
  - Model LinkerPatch has a new parameter public_network_solution
  - Model LinkerResource has a new parameter configuration_info
  - Model LinkerResource has a new parameter public_network_solution
  - Model ProxyResource has a new parameter system_data
  - Model Resource has a new parameter system_data
  - Model SecretStore has a new parameter key_vault_secret_name
  - Model ServicePrincipalCertificateAuthInfo has a new parameter delete_or_update_behavior
  - Model ServicePrincipalCertificateAuthInfo has a new parameter roles
  - Model ServicePrincipalSecretAuthInfo has a new parameter delete_or_update_behavior
  - Model ServicePrincipalSecretAuthInfo has a new parameter roles
  - Model ServicePrincipalSecretAuthInfo has a new parameter user_name
  - Model SystemAssignedIdentityAuthInfo has a new parameter delete_or_update_behavior
  - Model SystemAssignedIdentityAuthInfo has a new parameter roles
  - Model SystemAssignedIdentityAuthInfo has a new parameter user_name
  - Model UserAssignedIdentityAuthInfo has a new parameter delete_or_update_behavior
  - Model UserAssignedIdentityAuthInfo has a new parameter roles
  - Model UserAssignedIdentityAuthInfo has a new parameter user_name
  - Model VNetSolution has a new parameter delete_or_update_behavior

## 1.1.0 (2022-05-16)

**Features**

  - Added model AzureResourceType
  - Added model TargetServiceType
  - Added model ValidateOperationResult

## 1.0.0 (2022-04-22)

**Features**

  - Model LinkerPatch has a new parameter scope
  - Model LinkerPatch has a new parameter target_service
  - Model LinkerResource has a new parameter scope
  - Model LinkerResource has a new parameter target_service
  - Model SecretAuthInfo has a new parameter secret_info
  - Model ValidateResult has a new parameter is_connection_available
  - Model ValidateResult has a new parameter linker_name
  - Model ValidateResult has a new parameter source_id
  - Model ValidateResult has a new parameter validation_detail

**Breaking changes**

  - Model LinkerPatch no longer has parameter target_id
  - Model LinkerResource no longer has parameter target_id
  - Model SecretAuthInfo no longer has parameter secret
  - Model ValidateResult no longer has parameter linker_status
  - Model ValidateResult no longer has parameter name
  - Model ValidateResult no longer has parameter reason

## 1.0.0b2 (2022-02-24)

**Features**

  - Model LinkerPatch has a new parameter secret_store
  - Model LinkerPatch has a new parameter v_net_solution
  - Model LinkerResource has a new parameter secret_store
  - Model LinkerResource has a new parameter v_net_solution

## 1.0.0b1 (2021-09-28)

* Initial Release
