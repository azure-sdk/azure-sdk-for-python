# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._action_groups_operations import ActionGroupsOperations  # type: ignore
from ._activity_log_alerts_operations import ActivityLogAlertsOperations  # type: ignore
from ._activity_logs_operations import ActivityLogsOperations  # type: ignore
from ._tenant_activity_logs_operations import TenantActivityLogsOperations  # type: ignore
from ._alert_rule_incidents_operations import AlertRuleIncidentsOperations  # type: ignore
from ._autoscale_settings_operations import AutoscaleSettingsOperations  # type: ignore
from ._predictive_metric_operations import PredictiveMetricOperations  # type: ignore
from ._baselines_operations import BaselinesOperations  # type: ignore
from ._diagnostic_settings_operations import DiagnosticSettingsOperations  # type: ignore
from ._diagnostic_settings_category_operations import DiagnosticSettingsCategoryOperations  # type: ignore
from ._event_categories_operations import EventCategoriesOperations  # type: ignore
from ._guest_diagnostics_settings_operations import GuestDiagnosticsSettingsOperations  # type: ignore
from ._guest_diagnostics_settings_association_operations import GuestDiagnosticsSettingsAssociationOperations  # type: ignore
from ._log_profiles_operations import LogProfilesOperations  # type: ignore
from ._metric_alerts_operations import MetricAlertsOperations  # type: ignore
from ._metric_alerts_status_operations import MetricAlertsStatusOperations  # type: ignore
from ._metric_definitions_operations import MetricDefinitionsOperations  # type: ignore
from ._metric_namespaces_operations import MetricNamespacesOperations  # type: ignore
from ._metrics_operations import MetricsOperations  # type: ignore
from ._operations import Operations  # type: ignore
from ._scheduled_query_rules_operations import ScheduledQueryRulesOperations  # type: ignore
from ._service_diagnostic_settings_operations import ServiceDiagnosticSettingsOperations  # type: ignore
from ._vm_insights_operations import VMInsightsOperations  # type: ignore
from ._private_link_scopes_operations import PrivateLinkScopesOperations  # type: ignore
from ._private_link_scope_operation_status_operations import PrivateLinkScopeOperationStatusOperations  # type: ignore
from ._private_link_resources_operations import PrivateLinkResourcesOperations  # type: ignore
from ._private_endpoint_connections_operations import PrivateEndpointConnectionsOperations  # type: ignore
from ._private_link_scoped_resources_operations import PrivateLinkScopedResourcesOperations  # type: ignore
from ._subscription_diagnostic_settings_operations import SubscriptionDiagnosticSettingsOperations  # type: ignore
from ._azure_monitor_workspaces_operations import AzureMonitorWorkspacesOperations  # type: ignore
from ._monitor_operations_operations import MonitorOperationsOperations  # type: ignore
from ._data_collection_endpoints_operations import DataCollectionEndpointsOperations  # type: ignore
from ._data_collection_rule_associations_operations import DataCollectionRuleAssociationsOperations  # type: ignore
from ._data_collection_rules_operations import DataCollectionRulesOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ActionGroupsOperations",
    "ActivityLogAlertsOperations",
    "ActivityLogsOperations",
    "TenantActivityLogsOperations",
    "AlertRuleIncidentsOperations",
    "AutoscaleSettingsOperations",
    "PredictiveMetricOperations",
    "BaselinesOperations",
    "DiagnosticSettingsOperations",
    "DiagnosticSettingsCategoryOperations",
    "EventCategoriesOperations",
    "GuestDiagnosticsSettingsOperations",
    "GuestDiagnosticsSettingsAssociationOperations",
    "LogProfilesOperations",
    "MetricAlertsOperations",
    "MetricAlertsStatusOperations",
    "MetricDefinitionsOperations",
    "MetricNamespacesOperations",
    "MetricsOperations",
    "Operations",
    "ScheduledQueryRulesOperations",
    "ServiceDiagnosticSettingsOperations",
    "VMInsightsOperations",
    "PrivateLinkScopesOperations",
    "PrivateLinkScopeOperationStatusOperations",
    "PrivateLinkResourcesOperations",
    "PrivateEndpointConnectionsOperations",
    "PrivateLinkScopedResourcesOperations",
    "SubscriptionDiagnosticSettingsOperations",
    "AzureMonitorWorkspacesOperations",
    "MonitorOperationsOperations",
    "DataCollectionEndpointsOperations",
    "DataCollectionRuleAssociationsOperations",
    "DataCollectionRulesOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
