# Release History

## 2.0.0 (2025-05-12)

### Features Added

  - Client `PeeringManagementClient` added operation group `cdn_peering_prefixes`
  - Client `PeeringManagementClient` added operation group `looking_glass`
  - Client `PeeringManagementClient` added operation group `registered_asns`
  - Client `PeeringManagementClient` added operation group `registered_prefixes`
  - Client `PeeringManagementClient` added operation group `received_routes`
  - Client `PeeringManagementClient` added operation group `connection_monitor_tests`
  - Client `PeeringManagementClient` added operation group `peering_service_countries`
  - Client `PeeringManagementClient` added operation group `rp_unbilled_prefixes`
  - Enum `ConnectionState` added member `EXTERNAL_BLOCKER`
  - Enum `ConnectionState` added member `TYPE_CHANGE_IN_PROGRESS`
  - Enum `ConnectionState` added member `TYPE_CHANGE_REQUESTED`
  - Model `DirectConnection` added property `microsoft_tracking_id`
  - Model `DirectConnection` added property `migration_work_window_bgp_session_same_device`
  - Model `DirectConnection` added property `last_failure_time_utc`
  - Model `DirectConnection` added property `error_message`
  - Model `DirectConnection` added property `previous_connection_provisioning_state`
  - Model `DirectConnection` added property `migration_work_window_tracker`
  - Enum `DirectPeeringType` added member `EDGE_ZONE_FOR_OPERATORS`
  - Enum `DirectPeeringType` added member `IX`
  - Enum `DirectPeeringType` added member `IX_RS`
  - Enum `DirectPeeringType` added member `PEER_PROP`
  - Enum `DirectPeeringType` added member `VOICE`
  - Enum `Enum0` added member `UNAVAILABLE`
  - Model `ErrorResponse` added property `error`
  - Model `ExchangeConnection` added property `migration_work_window_bgp_session_same_device`
  - Model `ExchangeConnection` added property `last_failure_time_utc`
  - Model `ExchangeConnection` added property `error_message`
  - Model `ExchangeConnection` added property `previous_connection_provisioning_state`
  - Model `ExchangeConnection` added property `migration_work_window_tracker`
  - Enum `LearnedType` added member `VIA_SERVICE_PROVIDER`
  - Model `Operation` added property `service_specification`
  - Model `PeerAsn` added property `peer_contact_detail`
  - Model `PeerAsn` added property `error_message`
  - Model `Peering` added property `connectivity_probes`
  - Model `PeeringService` added property `sku`
  - Model `PeeringService` added property `provider_primary_peering_location`
  - Model `PeeringService` added property `provider_backup_peering_location`
  - Model `PeeringService` added property `log_analytics_workspace_properties`
  - Model `PeeringServicePrefix` added property `error_message`
  - Model `PeeringServicePrefix` added property `events`
  - Model `PeeringServicePrefix` added property `peering_service_prefix_key`
  - Model `PeeringServiceProvider` added property `peering_locations`
  - Enum `PrefixValidationState` added member `WARNING`
  - Added model `CdnPeeringPrefix`
  - Added model `CdnPeeringPrefixListResult`
  - Added enum `Command`
  - Added model `ConnectionMonitorTest`
  - Added model `ConnectionMonitorTestListResult`
  - Added model `ConnectivityProbe`
  - Added model `ContactDetail`
  - Added enum `Enum11`
  - Added enum `Enum13`
  - Added model `ErrorDetail`
  - Added enum `LegacyPeeringsKind`
  - Added model `LogAnalyticsWorkspaceProperties`
  - Added enum `LookingGlassCommand`
  - Added model `LookingGlassOutput`
  - Added enum `LookingGlassSourceType`
  - Added model `MetricDimension`
  - Added model `MetricSpecification`
  - Added enum `PeeringLocationsDirectPeeringType`
  - Added enum `PeeringLocationsKind`
  - Added model `PeeringReceivedRoute`
  - Added model `PeeringReceivedRouteListResult`
  - Added model `PeeringRegisteredAsn`
  - Added model `PeeringRegisteredAsnListResult`
  - Added model `PeeringRegisteredPrefix`
  - Added model `PeeringRegisteredPrefixListResult`
  - Added model `PeeringServiceCountry`
  - Added model `PeeringServiceCountryListResult`
  - Added model `PeeringServicePrefixEvent`
  - Added model `PeeringServiceSku`
  - Added enum `PreviousConnectionProvisioningState`
  - Added enum `Protocol`
  - Added enum `Role`
  - Added model `RpUnbilledPrefix`
  - Added model `RpUnbilledPrefixListResult`
  - Added model `ServiceSpecification`
  - Model `LegacyPeeringsOperations` added parameter `kwargs` in method `__init__`
  - Model `Operations` added parameter `kwargs` in method `__init__`
  - Model `PeerAsnsOperations` added parameter `kwargs` in method `__init__`
  - Model `PeeringLocationsOperations` added parameter `kwargs` in method `__init__`
  - Model `PeeringServiceLocationsOperations` added parameter `kwargs` in method `__init__`
  - Model `PeeringServiceProvidersOperations` added parameter `kwargs` in method `__init__`
  - Model `PeeringServicesOperations` added parameter `kwargs` in method `__init__`
  - Model `PeeringServicesOperations` added method `initialize_connection_monitor`
  - Model `PeeringsOperations` added parameter `kwargs` in method `__init__`
  - Model `PrefixesOperations` added parameter `kwargs` in method `__init__`
  - Model `PrefixesOperations` added method `create_or_update`
  - Model `PrefixesOperations` added method `delete`
  - Added model `CdnPeeringPrefixesOperations`
  - Added model `ConnectionMonitorTestsOperations`
  - Added model `LookingGlassOperations`
  - Added model `PeeringServiceCountriesOperations`
  - Added model `ReceivedRoutesOperations`
  - Added model `RegisteredAsnsOperations`
  - Added model `RegisteredPrefixesOperations`
  - Added model `RpUnbilledPrefixesOperations`
  - Method `PeeringManagementClient.check_service_provider_availability` has a new overload `def check_service_provider_availability(self: None, check_service_provider_availability_input: CheckServiceProviderAvailabilityInput, content_type: str)`
  - Method `PeeringManagementClient.check_service_provider_availability` has a new overload `def check_service_provider_availability(self: None, check_service_provider_availability_input: IO[bytes], content_type: str)`
  - Method `PeerAsnsOperations.create_or_update` has a new overload `def create_or_update(self: None, peer_asn_name: str, peer_asn: PeerAsn, content_type: str)`
  - Method `PeerAsnsOperations.create_or_update` has a new overload `def create_or_update(self: None, peer_asn_name: str, peer_asn: IO[bytes], content_type: str)`
  - Method `PeeringManagementClientOperationsMixin.check_service_provider_availability` has a new overload `def check_service_provider_availability(self: None, check_service_provider_availability_input: CheckServiceProviderAvailabilityInput, content_type: str)`
  - Method `PeeringManagementClientOperationsMixin.check_service_provider_availability` has a new overload `def check_service_provider_availability(self: None, check_service_provider_availability_input: IO[bytes], content_type: str)`
  - Method `PeeringServicesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, peering_service_name: str, peering_service: PeeringService, content_type: str)`
  - Method `PeeringServicesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, peering_service_name: str, peering_service: IO[bytes], content_type: str)`
  - Method `PeeringServicesOperations.update` has a new overload `def update(self: None, resource_group_name: str, peering_service_name: str, tags: ResourceTags, content_type: str)`
  - Method `PeeringServicesOperations.update` has a new overload `def update(self: None, resource_group_name: str, peering_service_name: str, tags: IO[bytes], content_type: str)`
  - Method `PeeringsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, peering_name: str, peering: Peering, content_type: str)`
  - Method `PeeringsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, peering_name: str, peering: IO[bytes], content_type: str)`
  - Method `PeeringsOperations.update` has a new overload `def update(self: None, resource_group_name: str, peering_name: str, tags: ResourceTags, content_type: str)`
  - Method `PeeringsOperations.update` has a new overload `def update(self: None, resource_group_name: str, peering_name: str, tags: IO[bytes], content_type: str)`
  - Method `PrefixesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, peering_service_name: str, prefix_name: str, peering_service_prefix: PeeringServicePrefix, content_type: str)`
  - Method `PrefixesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, peering_service_name: str, prefix_name: str, peering_service_prefix: IO[bytes], content_type: str)`
  - Method `ConnectionMonitorTestsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, peering_service_name: str, connection_monitor_test_name: str, connection_monitor_test: ConnectionMonitorTest, content_type: str)`
  - Method `ConnectionMonitorTestsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, peering_service_name: str, connection_monitor_test_name: str, connection_monitor_test: IO[bytes], content_type: str)`
  - Method `RegisteredAsnsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, peering_name: str, registered_asn_name: str, registered_asn: PeeringRegisteredAsn, content_type: str)`
  - Method `RegisteredAsnsOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, peering_name: str, registered_asn_name: str, registered_asn: IO[bytes], content_type: str)`
  - Method `RegisteredPrefixesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, peering_name: str, registered_prefix_name: str, registered_prefix: PeeringRegisteredPrefix, content_type: str)`
  - Method `RegisteredPrefixesOperations.create_or_update` has a new overload `def create_or_update(self: None, resource_group_name: str, peering_name: str, registered_prefix_name: str, registered_prefix: IO[bytes], content_type: str)`

### Breaking Changes

  - Deleted or renamed client operation group `PeeringManagementClient.peering_service_prefixes`
  - Deleted or renamed enum value `Enum0.UN_AVAILABLE`
  - Model `ErrorResponse` deleted or renamed its instance variable `code`
  - Model `ErrorResponse` deleted or renamed its instance variable `message`
  - Deleted or renamed enum value `LearnedType.VIA_PARTNER`
  - Model `PeerAsn` deleted or renamed its instance variable `peer_contact_info`
  - Deleted or renamed model `ContactInfo`
  - Deleted or renamed model `Enum1`
  - Deleted or renamed model `Enum14`
  - Deleted or renamed model `Enum15`
  - Deleted or renamed model `Name`
  - Deleted or renamed model `PeeringServicePrefixesOperations`

## 2.0.0b1 (2022-11-01)

### Features Added

  - Added operation PeeringServicesOperations.initialize_connection_monitor
  - Added operation PrefixesOperations.create_or_update
  - Added operation PrefixesOperations.delete
  - Added operation PrefixesOperations.get
  - Added operation group CdnPeeringPrefixesOperations
  - Added operation group ConnectionMonitorTestsOperations
  - Added operation group LookingGlassOperations
  - Added operation group PeeringServiceCountriesOperations
  - Added operation group ReceivedRoutesOperations
  - Added operation group RegisteredAsnsOperations
  - Added operation group RegisteredPrefixesOperations
  - Added operation group RpUnbilledPrefixesOperations
  - Model DirectConnection has a new parameter error_message
  - Model DirectConnection has a new parameter microsoft_tracking_id
  - Model ErrorResponse has a new parameter error
  - Model ExchangeConnection has a new parameter error_message
  - Model Operation has a new parameter service_specification
  - Model PeerAsn has a new parameter error_message
  - Model PeerAsn has a new parameter peer_contact_detail
  - Model PeeringService has a new parameter log_analytics_workspace_properties
  - Model PeeringService has a new parameter provider_backup_peering_location
  - Model PeeringService has a new parameter provider_primary_peering_location
  - Model PeeringService has a new parameter sku
  - Model PeeringServicePrefix has a new parameter error_message
  - Model PeeringServicePrefix has a new parameter events
  - Model PeeringServicePrefix has a new parameter peering_service_prefix_key
  - Model PeeringServiceProvider has a new parameter peering_locations

### Breaking Changes

  - Model ErrorResponse no longer has parameter code
  - Model ErrorResponse no longer has parameter message
  - Model PeerAsn no longer has parameter peer_contact_info
  - Operation LegacyPeeringsOperations.list has a new parameter asn
  - Operation LegacyPeeringsOperations.list has a new parameter direct_peering_type
  - Operation PeeringServiceLocationsOperations.list has a new parameter country
  - Operation PrefixesOperations.list_by_peering_service has a new parameter expand
  - Removed operation group PeeringServicePrefixesOperations

## 1.0.0 (2021-04-25)

**Features**

  - Model PeerAsn has a new parameter peer_contact_info
  - Added operation group PeeringServicePrefixesOperations

**Breaking changes**

  - Operation PrefixesOperations.list_by_peering_service has a new signature
  - Operation PeeringServiceLocationsOperations.list has a new signature
  - Operation LegacyPeeringsOperations.list has a new signature
  - Model DirectConnection no longer has parameter error_message
  - Model DirectConnection no longer has parameter microsoft_tracking_id
  - Model PeeringServicePrefix no longer has parameter events
  - Model PeeringServicePrefix no longer has parameter error_message
  - Model PeeringServicePrefix no longer has parameter peering_service_prefix_key
  - Model ExchangeConnection no longer has parameter error_message
  - Model PeerAsn no longer has parameter error_message
  - Model PeerAsn no longer has parameter peer_contact_detail
  - Model PeeringService no longer has parameter sku
  - Model ErrorResponse has a new signature
  - Removed operation PrefixesOperations.delete
  - Removed operation PrefixesOperations.create_or_update
  - Removed operation PrefixesOperations.get
  - Removed operation group CdnPeeringPrefixesOperations
  - Removed operation group ReceivedRoutesOperations
  - Removed operation group RegisteredAsnsOperations
  - Removed operation group PeeringServiceCountriesOperations
  - Removed operation group RegisteredPrefixesOperations

## 1.0.0b1 (2020-12-07)

This is beta preview version.

This version uses a next-generation code generator that introduces important breaking changes, but also important new features (like unified authentication and async programming).

**General breaking changes**

- Credential system has been completly revamped:

  - `azure.common.credentials` or `msrestazure.azure_active_directory` instances are no longer supported, use the `azure-identity` classes instead: https://pypi.org/project/azure-identity/
  - `credentials` parameter has been renamed `credential`

- The `config` attribute no longer exists on a client, configuration should be passed as kwarg. Example: `MyClient(credential, subscription_id, enable_logging=True)`. For a complete set of
  supported options, see the [parameters accept in init documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)
- You can't import a `version` module anymore, use `__version__` instead
- Operations that used to return a `msrest.polling.LROPoller` now returns a `azure.core.polling.LROPoller` and are prefixed with `begin_`.
- Exceptions tree have been simplified and most exceptions are now `azure.core.exceptions.HttpResponseError` (`CloudError` has been removed).
- Most of the operation kwarg have changed. Some of the most noticeable:

  - `raw` has been removed. Equivalent feature can be found using `cls`, a callback that will give access to internal HTTP response for advanced user
  - For a complete set of
  supported options, see the [parameters accept in Request documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)

**General new features**

- Type annotations support using `typing`. SDKs are mypy ready.
- This client has now stable and official support for async. Check the `aio` namespace of your package to find the async client.
- This client now support natively tracing library like OpenCensus or OpenTelemetry. See this [tracing quickstart](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-tracing-opentelemetry) for an overview.

## 0.2.0 (2020-04-12)

**Features**

  - Model PeeringServicePrefix has a new parameter peering_service_prefix_key
  - Model PeerAsn has a new parameter peer_contact_detail
  - Model PeeringService has a new parameter sku
  - Added operation group RegisteredPrefixesOperations
  - Added operation group PeeringServiceCountriesOperations
  - Added operation group RegisteredAsnsOperations

**Breaking changes**

  - Operation LegacyPeeringsOperations.list has a new signature
  - Operation PrefixesOperations.create_or_update has a new signature
  - Operation PeeringServiceLocationsOperations.list has a new signature
  - Model PeerAsn no longer has parameter peer_contact_info

## 0.1.0rc2 (2019-10-24)

**Breaking changes**

  - Migrated operations from PeeringServicePrefixesOperations to
    PrefixesOperations

## 0.1.0rc1 (2019-09-26)

  - Initial Release
