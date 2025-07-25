# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.applicationinsights import ApplicationInsightsManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestApplicationInsightsManagementComponentCurrentBillingFeaturesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ApplicationInsightsManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_component_current_billing_features_get(self, resource_group):
        response = self.client.component_current_billing_features.get(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2015-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_component_current_billing_features_update(self, resource_group):
        response = self.client.component_current_billing_features.update(
            resource_group_name=resource_group.name,
            resource_name="str",
            billing_features_properties={
                "CurrentBillingFeatures": ["str"],
                "DataVolumeCap": {
                    "Cap": 0.0,
                    "MaxHistoryCap": 0.0,
                    "ResetTime": 0,
                    "StopSendNotificationWhenHitCap": bool,
                    "StopSendNotificationWhenHitThreshold": bool,
                    "WarningThreshold": 0,
                },
            },
            api_version="2015-05-01",
        )

        # please add some check logic here by yourself
        # ...
