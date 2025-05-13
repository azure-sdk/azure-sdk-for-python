# Release History

## 1.1.0b1 (2025-05-13)

### Features Added

  - Added model `Quota`
  - Added model `QuotaName`
  - Model `FabricCapacitiesOperations` added method `list_usages`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, display: Optional[_models.OperationDisplay])`
  - Method `Quota.__init__` has a new overload `def __init__(self: None, unit: str, current_value: int, limit: int)`
  - Method `Quota.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `QuotaName.__init__` has a new overload `def __init__(self: None, value: Optional[str], localized_value: Optional[str])`
  - Method `QuotaName.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`

## 1.0.0 (2024-10-21)

### Other Changes

  - First GA

## 1.0.0b1 (2024-09-22)

### Other Changes

  - Initial version
