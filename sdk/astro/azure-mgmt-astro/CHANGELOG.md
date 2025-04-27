# Release History

## 1.0.0 (2025-04-27)

### Features Added

  - Model `LiftrBaseOfferDetails` added property `renewal_mode`
  - Model `LiftrBaseOfferDetails` added property `end_date`
  - Model `OrganizationResourceUpdateProperties` added property `marketplace`
  - Added model `LiftrBaseMarketplaceDetailsUpdate`
  - Added model `LiftrBaseOfferDetailsUpdate`
  - Added enum `RenewalMode`
  - Method `OrganizationsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, organization_name: str, resource: IO[bytes], content_type: str)`
  - Method `OrganizationsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, organization_name: str, properties: IO[bytes], content_type: str)`

### Breaking Changes

  - Deleted or renamed model `Versions`

## 1.0.0b1 (2024-02-22)

* Initial Release
