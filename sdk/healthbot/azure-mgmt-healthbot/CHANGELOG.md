# Release History

## 1.0.0 (2025-05-09)

### Features Added

  - Enum `SkuName` added member `C1`
  - Enum `SkuName` added member `PES`
  - Added enum `CreatedByType`
  - Added model `ErrorDetail`
  - Added model `UserAssignedIdentityMap`
  - Added model `HealthBotsOperations`
  - Method `Error.__init__` has a new overload `def __init__(self: None, error: Optional[_models.ErrorDetail])`
  - Method `Error.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `HealthBot.__init__` has a new overload `def __init__(self: None, location: str, sku: _models.Sku, tags: Optional[Dict[str, str]], identity: Optional[_models.Identity], properties: Optional[_models.HealthBotProperties])`
  - Method `HealthBot.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `HealthBot.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `HealthBot.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `HealthBotKey.__init__` has a new overload `def __init__(self: None, key_name: Optional[str], value: Optional[str])`
  - Method `HealthBotKey.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `HealthBotKeysResponse.__init__` has a new overload `def __init__(self: None, secrets: Optional[List[_models.HealthBotKey]])`
  - Method `HealthBotKeysResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `HealthBotProperties.__init__` has a new overload `def __init__(self: None, key_vault_properties: Optional[_models.KeyVaultProperties])`
  - Method `HealthBotProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `HealthBotUpdateParameters.__init__` has a new overload `def __init__(self: None, properties: Optional[_models.HealthBotProperties], tags: Optional[Dict[str, str]], sku: Optional[_models.Sku], identity: Optional[_models.Identity], location: Optional[str])`
  - Method `HealthBotUpdateParameters.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Identity.__init__` has a new overload `def __init__(self: None, type: Optional[Union[str, _models.ResourceIdentityType]], user_assigned_identities: Optional[_models.UserAssignedIdentityMap])`
  - Method `Identity.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `KeyVaultProperties.__init__` has a new overload `def __init__(self: None, key_name: str, key_vault_uri: str, key_version: Optional[str], user_identity: Optional[str])`
  - Method `KeyVaultProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OperationDetail.__init__` has a new overload `def __init__(self: None, name: Optional[str], is_data_action: Optional[bool], display: Optional[_models.OperationDisplay], origin: Optional[str], properties: Optional[Any])`
  - Method `OperationDetail.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OperationDisplay.__init__` has a new overload `def __init__(self: None, provider: Optional[str], resource: Optional[str], operation: Optional[str], description: Optional[str])`
  - Method `OperationDisplay.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Sku.__init__` has a new overload `def __init__(self: None, name: Union[str, _models.SkuName])`
  - Method `Sku.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, created_by: Optional[str], created_by_type: Optional[Union[str, _models.CreatedByType]], created_at: Optional[datetime], last_modified_by: Optional[str], last_modified_by_type: Optional[Union[str, _models.CreatedByType]], last_modified_at: Optional[datetime])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `HealthBotsOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, bot_name: str, parameters: HealthBot, content_type: str)`
  - Method `HealthBotsOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, bot_name: str, parameters: JSON, content_type: str)`
  - Method `HealthBotsOperations.begin_create` has a new overload `def begin_create(self: None, resource_group_name: str, bot_name: str, parameters: IO[bytes], content_type: str)`
  - Method `HealthBotsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, bot_name: str, parameters: HealthBotUpdateParameters, content_type: str)`
  - Method `HealthBotsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, bot_name: str, parameters: JSON, content_type: str)`
  - Method `HealthBotsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, bot_name: str, parameters: IO[bytes], content_type: str)`

### Breaking Changes

  - Deleted or renamed client `HealthBotMgmtClient`
  - Model `Error` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorAdditionalInfo` deleted or renamed its instance variable `additional_properties`
  - Model `HealthBot` deleted or renamed its instance variable `additional_properties`
  - Model `HealthBotKey` deleted or renamed its instance variable `additional_properties`
  - Model `HealthBotKeysResponse` deleted or renamed its instance variable `additional_properties`
  - Model `HealthBotProperties` deleted or renamed its instance variable `additional_properties`
  - Model `HealthBotUpdateParameters` deleted or renamed its instance variable `additional_properties`
  - Model `Identity` deleted or renamed its instance variable `additional_properties`
  - Model `KeyVaultProperties` deleted or renamed its instance variable `additional_properties`
  - Model `OperationDetail` deleted or renamed its instance variable `additional_properties`
  - Model `OperationDisplay` deleted or renamed its instance variable `additional_properties`
  - Model `Resource` deleted or renamed its instance variable `additional_properties`
  - Model `Sku` deleted or renamed its instance variable `additional_properties`
  - Model `SystemData` deleted or renamed its instance variable `additional_properties`
  - Model `TrackedResource` deleted or renamed its instance variable `additional_properties`
  - Model `UserAssignedIdentity` deleted or renamed its instance variable `additional_properties`
  - Deleted or renamed model `AvailableOperations`
  - Deleted or renamed model `BotResponseList`
  - Deleted or renamed model `ErrorError`
  - Deleted or renamed model `IdentityType`
  - Deleted or renamed model `ValidationResult`
  - Deleted or renamed model `BotsOperations`

## 1.0.0b2 (2022-10-28)

### Features Added

  - Added operation BotsOperations.list_secrets
  - Added operation BotsOperations.regenerate_api_jwt_secret
  - Model HealthBot has a new parameter identity
  - Model HealthBotProperties has a new parameter key_vault_properties
  - Model HealthBotUpdateParameters has a new parameter identity
  - Model HealthBotUpdateParameters has a new parameter location
  - Model HealthBotUpdateParameters has a new parameter properties

### Breaking Changes

  - Client name is changed from `Healthbot` to `HealthBotMgmtClient`

## 1.0.0b1 (2021-01-06)

* Initial Release
