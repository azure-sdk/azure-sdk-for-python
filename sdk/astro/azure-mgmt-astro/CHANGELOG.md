# Release History

## 1.0.0 (2025-05-13)

### Features Added

  - Client `AstroMgmtClient` added method `send_request`
  - Enum `ManagedServiceIdentityType` added member `SYSTEM_AND_USER_ASSIGNED`
  - Model `OrganizationResourceUpdateProperties` added property `marketplace`
  - Added model `ManagedServiceIdentityV4`
  - Added model `MarketplaceDetails`
  - Added model `OfferDetails`
  - Added model `OrganizationProperties`
  - Added model `PartnerOrganizationProperties`
  - Added enum `RenewalMode`
  - Added model `SingleSignOnProperties`
  - Added model `UserDetails`
  - Method `ErrorResponse.__init__` has a new overload `def __init__(self: None, error: Optional[_models.ErrorDetail])`
  - Method `ErrorResponse.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, display: Optional[_models.OperationDisplay])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OrganizationResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]], properties: Optional[_models.OrganizationProperties], identity: Optional[_models.ManagedServiceIdentityV4])`
  - Method `OrganizationResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OrganizationResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `OrganizationResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OrganizationResourceUpdate.__init__` has a new overload `def __init__(self: None, identity: Optional[_models.ManagedServiceIdentityV4], tags: Optional[Dict[str, str]], properties: Optional[_models.OrganizationResourceUpdateProperties])`
  - Method `OrganizationResourceUpdate.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OrganizationResourceUpdateProperties.__init__` has a new overload `def __init__(self: None, marketplace: Optional[_models.MarketplaceDetails], user: Optional[_models.UserDetails], partner_organization_properties: Optional[_models.PartnerOrganizationProperties])`
  - Method `OrganizationResourceUpdateProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, created_by: Optional[str], created_by_type: Optional[Union[str, _models.CreatedByType]], created_at: Optional[datetime], last_modified_by: Optional[str], last_modified_by_type: Optional[Union[str, _models.CreatedByType]], last_modified_at: Optional[datetime])`
  - Method `SystemData.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `TrackedResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `ManagedServiceIdentityV4.__init__` has a new overload `def __init__(self: None, type: Union[str, _models.ManagedServiceIdentityType], user_assigned_identities: Optional[Dict[str, _models.UserAssignedIdentity]])`
  - Method `ManagedServiceIdentityV4.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `MarketplaceDetails.__init__` has a new overload `def __init__(self: None, offer_details: _models.OfferDetails, subscription_id: Optional[str], subscription_status: Optional[Union[str, _models.MarketplaceSubscriptionStatus]])`
  - Method `MarketplaceDetails.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OfferDetails.__init__` has a new overload `def __init__(self: None, publisher_id: str, offer_id: str, plan_id: str, plan_name: Optional[str], term_unit: Optional[str], term_id: Optional[str], renewal_mode: Optional[Union[str, _models.RenewalMode]])`
  - Method `OfferDetails.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OrganizationProperties.__init__` has a new overload `def __init__(self: None, marketplace: _models.MarketplaceDetails, user: _models.UserDetails, partner_organization_properties: Optional[_models.PartnerOrganizationProperties])`
  - Method `OrganizationProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `PartnerOrganizationProperties.__init__` has a new overload `def __init__(self: None, organization_name: str, organization_id: Optional[str], workspace_id: Optional[str], workspace_name: Optional[str], single_sign_on_properties: Optional[_models.SingleSignOnProperties])`
  - Method `PartnerOrganizationProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SingleSignOnProperties.__init__` has a new overload `def __init__(self: None, single_sign_on_state: Optional[Union[str, _models.SingleSignOnStates]], enterprise_app_id: Optional[str], single_sign_on_url: Optional[str], aad_domains: Optional[List[str]])`
  - Method `SingleSignOnProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `UserDetails.__init__` has a new overload `def __init__(self: None, first_name: str, last_name: str, email_address: str, upn: Optional[str], phone_number: Optional[str])`
  - Method `UserDetails.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `OrganizationsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, organization_name: str, resource: IO[bytes], content_type: str)`
  - Method `OrganizationsOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, organization_name: str, resource: JSON, content_type: str)`
  - Method `OrganizationsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, organization_name: str, properties: IO[bytes], content_type: str)`
  - Method `OrganizationsOperations.begin_update` has a new overload `def begin_update(self: None, resource_group_name: str, organization_name: str, properties: JSON, content_type: str)`

### Breaking Changes

  - Model `ErrorAdditionalInfo` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorDetail` deleted or renamed its instance variable `additional_properties`
  - Model `ErrorResponse` deleted or renamed its instance variable `additional_properties`
  - Deleted or renamed enum value `ManagedServiceIdentityType.SYSTEM_ASSIGNED_USER_ASSIGNED`
  - Model `Operation` deleted or renamed its instance variable `additional_properties`
  - Model `OperationDisplay` deleted or renamed its instance variable `additional_properties`
  - Model `OrganizationResource` deleted or renamed its instance variable `additional_properties`
  - Model `OrganizationResourceUpdate` deleted or renamed its instance variable `additional_properties`
  - Model `OrganizationResourceUpdateProperties` deleted or renamed its instance variable `additional_properties`
  - Model `Resource` deleted or renamed its instance variable `additional_properties`
  - Model `SystemData` deleted or renamed its instance variable `additional_properties`
  - Model `TrackedResource` deleted or renamed its instance variable `additional_properties`
  - Model `UserAssignedIdentity` deleted or renamed its instance variable `additional_properties`
  - Deleted or renamed model `LiftrBaseDataOrganizationProperties`
  - Deleted or renamed model `LiftrBaseDataPartnerOrganizationProperties`
  - Deleted or renamed model `LiftrBaseDataPartnerOrganizationPropertiesUpdate`
  - Deleted or renamed model `LiftrBaseMarketplaceDetails`
  - Deleted or renamed model `LiftrBaseOfferDetails`
  - Deleted or renamed model `LiftrBaseSingleSignOnProperties`
  - Deleted or renamed model `LiftrBaseUserDetails`
  - Deleted or renamed model `LiftrBaseUserDetailsUpdate`
  - Deleted or renamed model `ManagedServiceIdentity`
  - Deleted or renamed model `Versions`

## 1.0.0b1 (2024-02-22)

* Initial Release
