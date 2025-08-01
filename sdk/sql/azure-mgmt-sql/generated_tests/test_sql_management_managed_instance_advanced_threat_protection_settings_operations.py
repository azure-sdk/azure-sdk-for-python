# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.sql import SqlManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSqlManagementManagedInstanceAdvancedThreatProtectionSettingsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SqlManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_managed_instance_advanced_threat_protection_settings_list_by_instance(self, resource_group):
        response = self.client.managed_instance_advanced_threat_protection_settings.list_by_instance(
            resource_group_name=resource_group.name,
            managed_instance_name="str",
            api_version="2024-11-01-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_managed_instance_advanced_threat_protection_settings_get(self, resource_group):
        response = self.client.managed_instance_advanced_threat_protection_settings.get(
            resource_group_name=resource_group.name,
            managed_instance_name="str",
            advanced_threat_protection_name="str",
            api_version="2024-11-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_managed_instance_advanced_threat_protection_settings_begin_create_or_update(self, resource_group):
        response = self.client.managed_instance_advanced_threat_protection_settings.begin_create_or_update(
            resource_group_name=resource_group.name,
            managed_instance_name="str",
            advanced_threat_protection_name="str",
            parameters={
                "creationTime": "2020-02-20 00:00:00",
                "id": "str",
                "name": "str",
                "state": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2024-11-01-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
