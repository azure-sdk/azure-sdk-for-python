# Release History

## 1.1.0 (2025-03-26)

### Features Added

  - Client `ContentSafetyClient` added method `detect_text_protected_material`
  - Client `ContentSafetyClient` added method `shield_prompt`
  - Model `TextBlocklistItem` added property `is_regex`
  - Added model `DetectTextProtectedMaterialOptions`
  - Added model `DetectTextProtectedMaterialResult`
  - Added model `DocumentInjectionAnalysisResult`
  - Added model `ShieldPromptOptions`
  - Added model `ShieldPromptResult`
  - Added model `TextProtectedMaterialAnalysisResult`
  - Added model `UserPromptInjectionAnalysisResult`
  - Method `ContentSafetyClient.detect_text_protected_material` has a new overload `def detect_text_protected_material(self: None, options: DetectTextProtectedMaterialOptions, content_type: str)`
  - Method `ContentSafetyClient.detect_text_protected_material` has a new overload `def detect_text_protected_material(self: None, options: JSON, content_type: str)`
  - Method `ContentSafetyClient.detect_text_protected_material` has a new overload `def detect_text_protected_material(self: None, options: IO[bytes], content_type: str)`
  - Method `ContentSafetyClient.shield_prompt` has a new overload `def shield_prompt(self: None, options: ShieldPromptOptions, content_type: str)`
  - Method `ContentSafetyClient.shield_prompt` has a new overload `def shield_prompt(self: None, options: JSON, content_type: str)`
  - Method `ContentSafetyClient.shield_prompt` has a new overload `def shield_prompt(self: None, options: IO[bytes], content_type: str)`
  - Method `TextBlocklistItem.__init__` has a new overload `def __init__(self: None, text: str, description: Optional[str], is_regex: Optional[bool])`
  - Method `DetectTextProtectedMaterialOptions.__init__` has a new overload `def __init__(self: None, text: str)`
  - Method `DetectTextProtectedMaterialOptions.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DetectTextProtectedMaterialResult.__init__` has a new overload `def __init__(self: None, protected_material_analysis: _models.TextProtectedMaterialAnalysisResult)`
  - Method `DetectTextProtectedMaterialResult.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DocumentInjectionAnalysisResult.__init__` has a new overload `def __init__(self: None, attack_detected: bool)`
  - Method `DocumentInjectionAnalysisResult.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ShieldPromptOptions.__init__` has a new overload `def __init__(self: None, user_prompt: Optional[str], documents: Optional[List[str]])`
  - Method `ShieldPromptOptions.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ShieldPromptResult.__init__` has a new overload `def __init__(self: None, user_prompt_analysis: Optional[_models.UserPromptInjectionAnalysisResult], documents_analysis: Optional[List[_models.DocumentInjectionAnalysisResult]])`
  - Method `ShieldPromptResult.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `TextProtectedMaterialAnalysisResult.__init__` has a new overload `def __init__(self: None, detected: bool)`
  - Method `TextProtectedMaterialAnalysisResult.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `UserPromptInjectionAnalysisResult.__init__` has a new overload `def __init__(self: None, attack_detected: bool)`
  - Method `UserPromptInjectionAnalysisResult.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`

## 1.0.0 (2023-12-15)

### Features Added

- Support Microsoft Entra ID Authentication
- Support 8 severity level for AnalyzeText

### Breaking Changes

Contract change for AnalyzeText, AnalyzeImage, Blocklist management related methods. The changes are listed below:

#### AnalyzeText

- AnalyzeTextOptions
  - Renamed breakByBlocklists to haltOnBlocklistHit
  - Added AnalyzeTextOutputType model for the `output_type` property.
- AnalyzeTextResult
  - Renamed TextBlocklistMatchResult to TextBlocklistMatch
  - Replaced TextAnalyzeSeverityResult by TextCategoriesAnalysis

#### AnalyzeImage

- AnalyzeImageOptions
  - Added AnalyzeImageOutputType
- AnalyzeImageResult
  - Replaced ImageAnalyzeSeverityResult by ImageCategoriesAnalysis

#### Blocklist management

- Added BlocklistClient
- Renamed AddBlockItemsOptions to AddOrUpdateTextBlocklistItemsOptions
- Renamed AddBlockItemsResult to AddOrUpdateTextBlocklistItemsResult
- Renamed RemoveBlockItemsOptions to RemoveTextBlocklistItemsOptions
- Renamed TextBlockItemInfo to TextBlocklistItem

## 1.0.0b1 (2023-05-22)

- Initial version
