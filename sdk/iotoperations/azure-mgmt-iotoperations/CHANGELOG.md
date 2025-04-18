# Release History

## 1.1.0b1 (2025-04-18)

### Features Added

  - Client `IoTOperationsMgmtClient` added operation group `diagnostics`
  - Client `IoTOperationsMgmtClient` added operation group `diagnostic`
  - Model `BrokerProperties` added property `persistence`
  - Model `DataflowEndpointProperties` added property `otel_settings`
  - Enum `EndpointType` added member `EVENTHUB`
  - Enum `EndpointType` added member `EVENT_GRID`
  - Enum `EndpointType` added member `FABRIC_RT`
  - Enum `EndpointType` added member `LOCAL_MQ`
  - Enum `EndpointType` added member `OTEL`
  - Model `InstanceProperties` added property `secret_provider_class_ref`
  - Model `InstanceProperties` added property `features`
  - Model `InstanceProperties` added property `adr_namespace`
  - Model `VolumeClaimResourceRequirements` added property `claims`
  - Added model `CustomStateStoreRetainmentPolicy`
  - Added model `CustomSubscriberQueueRetainmentPolicy`
  - Added model `CustomTopicRetainmentPolicy`
  - Added model `DataflowEndpointOtel`
  - Added model `DiagnosticProperties`
  - Added model `DiagnosticResource`
  - Added model `DynamicPersistenceSettings`
  - Added model `DynamicRetainmentSettings`
  - Added model `InstanceFeature`
  - Added enum `InstanceFeatureMode`
  - Added model `Persistence`
  - Added enum `RemoteSupportAccessLevels`
  - Added enum `RemoteSupportActivationState`
  - Added model `RemoteSupportProperties`
  - Added enum `RetainmentPolicyMode`
  - Added model `StateStoreRetainmentPolicy`
  - Added model `StateStoreRetainmentResources`
  - Added model `StateStoreRetainmentSettings`
  - Added model `SubscriberQueueRetainmentPolicy`
  - Added model `SubscriberQueueRetainmentSettings`
  - Added model `TopicRetainmentPolicy`
  - Added model `TopicRetainmentSettings`
  - Added model `VolumeClaimResourceRequirementsClaims`
  - Added model `DiagnosticOperations`
  - Added model `DiagnosticsOperations`
  - Method `BrokerProperties.__init__` has a new overload `def __init__(self: None, advanced: Optional[_models.AdvancedSettings], cardinality: Optional[_models.Cardinality], diagnostics: Optional[_models.BrokerDiagnostics], disk_backed_message_buffer: Optional[_models.DiskBackedMessageBuffer], generate_resource_limits: Optional[_models.GenerateResourceLimits], memory_profile: Optional[Union[str, _models.BrokerMemoryProfile]], persistence: Optional[_models.Persistence])`
  - Method `DataflowEndpointProperties.__init__` has a new overload `def __init__(self: None, endpoint_type: Union[str, _models.EndpointType], data_explorer_settings: Optional[_models.DataflowEndpointDataExplorer], data_lake_storage_settings: Optional[_models.DataflowEndpointDataLakeStorage], fabric_one_lake_settings: Optional[_models.DataflowEndpointFabricOneLake], kafka_settings: Optional[_models.DataflowEndpointKafka], local_storage_settings: Optional[_models.DataflowEndpointLocalStorage], mqtt_settings: Optional[_models.DataflowEndpointMqtt], otel_settings: Optional[_models.DataflowEndpointOtel])`
  - Method `InstanceProperties.__init__` has a new overload `def __init__(self: None, schema_registry_ref: _models.SchemaRegistryRef, description: Optional[str], features: Optional[Dict[str, _models.InstanceFeature]], adr_namespace: Optional[str])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, display: Optional[_models.OperationDisplay])`
  - Method `VolumeClaimResourceRequirements.__init__` has a new overload `def __init__(self: None, limits: Optional[Dict[str, str]], requests: Optional[Dict[str, str]], claims: Optional[List[_models.VolumeClaimResourceRequirementsClaims]])`
  - Method `CustomStateStoreRetainmentPolicy.__init__` has a new overload `def __init__(self: None, state_store_settings: Optional[_models.StateStoreRetainmentSettings])`
  - Method `CustomStateStoreRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CustomStateStoreRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mode: str, state_store_settings: Optional[_models.StateStoreRetainmentSettings])`
  - Method `CustomStateStoreRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CustomSubscriberQueueRetainmentPolicy.__init__` has a new overload `def __init__(self: None, subscriber_queue_settings: Optional[_models.SubscriberQueueRetainmentSettings])`
  - Method `CustomSubscriberQueueRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CustomSubscriberQueueRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mode: str, subscriber_queue_settings: Optional[_models.SubscriberQueueRetainmentSettings])`
  - Method `CustomSubscriberQueueRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CustomTopicRetainmentPolicy.__init__` has a new overload `def __init__(self: None, retain_settings: Optional[_models.TopicRetainmentSettings])`
  - Method `CustomTopicRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `CustomTopicRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mode: str)`
  - Method `CustomTopicRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DataflowEndpointOtel.__init__` has a new overload `def __init__(self: None, host: str, metric_interval_sec: Optional[int], batching: Optional[_models.BatchingConfiguration], tls: Optional[_models.TlsProperties])`
  - Method `DataflowEndpointOtel.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DiagnosticProperties.__init__` has a new overload `def __init__(self: None, remote_support: Optional[_models.RemoteSupportProperties])`
  - Method `DiagnosticProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DiagnosticResource.__init__` has a new overload `def __init__(self: None, extended_location: _models.ExtendedLocation, properties: Optional[_models.DiagnosticProperties])`
  - Method `DiagnosticResource.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DynamicPersistenceSettings.__init__` has a new overload `def __init__(self: None, user_property_key: Optional[str], user_property_value: Optional[str])`
  - Method `DynamicPersistenceSettings.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DynamicRetainmentSettings.__init__` has a new overload `def __init__(self: None, mode: Optional[Union[str, _models.OperationalMode]])`
  - Method `DynamicRetainmentSettings.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `InstanceFeature.__init__` has a new overload `def __init__(self: None, mode: Optional[Union[str, _models.InstanceFeatureMode]], settings: Optional[Dict[str, Union[str, _models.OperationalMode]]])`
  - Method `InstanceFeature.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `Persistence.__init__` has a new overload `def __init__(self: None, max_size: str, dynamic_settings: Optional[_models.DynamicPersistenceSettings], persistent_volume_claim_spec: Optional[_models.VolumeClaimSpec], retain: Optional[_models.TopicRetainmentPolicy], state_store: Optional[_models.StateStoreRetainmentPolicy], subscriber_queue: Optional[_models.SubscriberQueueRetainmentPolicy])`
  - Method `Persistence.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `RemoteSupportProperties.__init__` has a new overload `def __init__(self: None, state: Optional[Union[str, _models.RemoteSupportActivationState]], access_level: Optional[Union[str, _models.RemoteSupportAccessLevels]], expiration_timestamp: Optional[str])`
  - Method `RemoteSupportProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `StateStoreRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mode: str, state_store_settings: Optional[_models.StateStoreRetainmentSettings])`
  - Method `StateStoreRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `StateStoreRetainmentResources.__init__` has a new overload `def __init__(self: None, key_type: str, keys_property: List[str])`
  - Method `StateStoreRetainmentResources.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `StateStoreRetainmentSettings.__init__` has a new overload `def __init__(self: None, state_store_resources: Optional[List[_models.StateStoreRetainmentResources]], dynamic: Optional[_models.DynamicRetainmentSettings])`
  - Method `StateStoreRetainmentSettings.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SubscriberQueueRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mode: str, subscriber_queue_settings: Optional[_models.SubscriberQueueRetainmentSettings])`
  - Method `SubscriberQueueRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `SubscriberQueueRetainmentSettings.__init__` has a new overload `def __init__(self: None, subscriber_client_ids: Optional[List[str]], dynamic: Optional[_models.DynamicRetainmentSettings], topics: Optional[List[str]])`
  - Method `SubscriberQueueRetainmentSettings.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `TopicRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mode: str)`
  - Method `TopicRetainmentPolicy.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `TopicRetainmentSettings.__init__` has a new overload `def __init__(self: None, topics: Optional[List[str]], dynamic: Optional[_models.DynamicRetainmentSettings])`
  - Method `TopicRetainmentSettings.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `VolumeClaimResourceRequirementsClaims.__init__` has a new overload `def __init__(self: None, name: str, resources: Optional[_models.VolumeClaimResourceRequirements])`
  - Method `VolumeClaimResourceRequirementsClaims.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `DiagnosticOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, instance_name: str, diagnostic_name: str, resource: DiagnosticResource, content_type: str)`
  - Method `DiagnosticOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, instance_name: str, diagnostic_name: str, resource: JSON, content_type: str)`
  - Method `DiagnosticOperations.begin_create_or_update` has a new overload `def begin_create_or_update(self: None, resource_group_name: str, instance_name: str, diagnostic_name: str, resource: IO[bytes], content_type: str)`

## 1.0.0 (2024-12-16)

### Other Changes

  - First GA

## 1.0.0b1 (2024-10-21)

### Other Changes

  - Initial version
