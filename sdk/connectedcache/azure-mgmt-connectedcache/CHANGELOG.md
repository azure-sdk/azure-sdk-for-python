# Release History

## 1.0.0b2 (2025-05-06)

### Features Added

  - Model `AdditionalCacheNodeProperties` added property `issues_list`
  - Model `AdditionalCacheNodeProperties` added property `issues_count`
  - Model `AdditionalCacheNodeProperties` added property `current_tls_certificate`
  - Model `AdditionalCacheNodeProperties` added property `last_auto_update_info`
  - Model `AdditionalCacheNodeProperties` added property `creation_method`
  - Model `AdditionalCacheNodeProperties` added property `tls_status`
  - Model `CacheNodeInstallProperties` added property `tls_certificate_provisioning_key`
  - Model `CacheNodeInstallProperties` added property `drive_configuration`
  - Model `CacheNodeInstallProperties` added property `proxy_url_configuration`
  - Added model `MccCacheNodeAutoUpdateHistory`
  - Added model `MccCacheNodeAutoUpdateHistoryProperties`
  - Added model `MccCacheNodeAutoUpdateInfo`
  - Added model `MccCacheNodeIssueHistory`
  - Added model `MccCacheNodeIssueHistoryProperties`
  - Added model `MccCacheNodeTlsCertificate`
  - Added model `MccCacheNodeTlsCertificateHistory`
  - Added model `MccCacheNodeTlsCertificateProperties`
  - Added model `MccIssue`
  - Model `EnterpriseMccCacheNodesOperationsOperations` added method `get_cache_node_auto_update_history`
  - Model `EnterpriseMccCacheNodesOperationsOperations` added method `get_cache_node_mcc_issue_details_history`
  - Model `EnterpriseMccCacheNodesOperationsOperations` added method `get_cache_node_tls_certificate_history`
  - Model `IspCacheNodesOperationsOperations` added method `get_cache_node_auto_update_history`
  - Model `IspCacheNodesOperationsOperations` added method `get_cache_node_mcc_issue_details_history`
  - Method `AdditionalCacheNodeProperties.__init__` has a new overload `def __init__(self: None, cache_node_properties_details_issues_list: Optional[List[str]], drive_configuration: Optional[List[_models.CacheNodeDriveConfiguration]], bgp_configuration: Optional[_models.BgpConfiguration], proxy_url_configuration: Optional[_models.ProxyUrlConfiguration], is_proxy_required: Optional[Union[str, _models.ProxyRequired]], os_type: Optional[Union[str, _models.OsType]], auto_update_version: Optional[str], update_info_details: Optional[str], update_requested_date_time: Optional[datetime], creation_method: Optional[int], optional_property1: Optional[str], optional_property2: Optional[str], optional_property3: Optional[str], optional_property4: Optional[str], optional_property5: Optional[str])`
  - Method `CacheNodeInstallProperties.__init__` has a new overload `def __init__(self: None, customer_id: Optional[str], cache_node_id: Optional[str], drive_configuration: Optional[List[_models.CacheNodeDriveConfiguration]], proxy_url_configuration: Optional[_models.ProxyUrlConfiguration])`
  - Method `Operation.__init__` has a new overload `def __init__(self: None, display: Optional[_models.OperationDisplay])`
  - Method `MccCacheNodeAutoUpdateHistory.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]], properties: Optional[_models.MccCacheNodeAutoUpdateHistoryProperties])`
  - Method `MccCacheNodeAutoUpdateHistory.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `MccCacheNodeAutoUpdateHistory.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `MccCacheNodeAutoUpdateHistory.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `MccCacheNodeAutoUpdateHistoryProperties.__init__` has a new overload `def __init__(self: None, auto_update_history: Optional[List[_models.MccCacheNodeAutoUpdateInfo]])`
  - Method `MccCacheNodeAutoUpdateHistoryProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `MccCacheNodeIssueHistory.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]], properties: Optional[_models.MccCacheNodeIssueHistoryProperties])`
  - Method `MccCacheNodeIssueHistory.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `MccCacheNodeIssueHistory.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `MccCacheNodeIssueHistory.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `MccCacheNodeIssueHistoryProperties.__init__` has a new overload `def __init__(self: None, mcc_issue_history: Optional[List[_models.MccIssue]])`
  - Method `MccCacheNodeIssueHistoryProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `MccCacheNodeTlsCertificateHistory.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]], properties: Optional[_models.MccCacheNodeTlsCertificateProperties])`
  - Method `MccCacheNodeTlsCertificateHistory.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `MccCacheNodeTlsCertificateHistory.__init__` has a new overload `def __init__(self: None, location: str, tags: Optional[Dict[str, str]])`
  - Method `MccCacheNodeTlsCertificateHistory.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`
  - Method `MccCacheNodeTlsCertificateProperties.__init__` has a new overload `def __init__(self: None, tls_certificate_history: Optional[List[_models.MccCacheNodeTlsCertificate]])`
  - Method `MccCacheNodeTlsCertificateProperties.__init__` has a new overload `def __init__(self: None, mapping: Mapping[str, Any])`

### Breaking Changes

  - Deleted or renamed client operation group `ConnectedCacheMgmtClient.enterprise_customer_operations`
  - Deleted or renamed client operation group `ConnectedCacheMgmtClient.cache_nodes_operations`
  - Model `AdditionalCacheNodeProperties` deleted or renamed its instance variable `proxy_url`
  - Model `AdditionalCacheNodeProperties` deleted or renamed its instance variable `update_cycle_type`
  - Model `AdditionalCustomerProperties` deleted or renamed its instance variable `peering_db_last_update_time`
  - Deleted or renamed model `CacheNodeOldResponse`
  - Deleted or renamed model `CacheNodePreviewResource`
  - Deleted or renamed model `CycleType`
  - Deleted or renamed model `EnterprisePreviewResource`
  - Deleted or renamed model `CacheNodesOperationsOperations`
  - Deleted or renamed model `EnterpriseCustomerOperationsOperations`

## 1.0.0b1 (2024-11-21)

### Other Changes

  - Initial version
