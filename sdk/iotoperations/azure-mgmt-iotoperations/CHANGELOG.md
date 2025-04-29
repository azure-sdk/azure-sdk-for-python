# Release History

## 1.1.0 (2025-04-29)

### Features Added

  - Model `InstanceProperties` added property `features`
  - Added model `InstanceFeature`
  - Added enum `InstanceFeatureMode`
  - Method `InstanceProperties.__init__` has a new overload `def __init__(self: None, schema_registry_ref: _models.SchemaRegistryRef, description: Optional[str], features: Optional[Dict[str, _models.InstanceFeature]])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, display: Optional[_models.OperationDisplay])`
  - Method `InstanceFeature.__init__` has a new overload `def __init__(self: None, mode: Optional[Union[str, _models.InstanceFeatureMode]], settings: Optional[Dict[str, Union[str, _models.OperationalMode]]])`
  - Method `InstanceFeature.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`

## 1.0.0 (2024-12-16)

### Other Changes

  - First GA

## 1.0.0b1 (2024-10-21)

### Other Changes

  - Initial version
