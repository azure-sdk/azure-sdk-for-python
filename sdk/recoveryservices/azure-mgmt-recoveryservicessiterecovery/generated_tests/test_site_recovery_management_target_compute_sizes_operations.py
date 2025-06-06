# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.recoveryservicessiterecovery import SiteRecoveryManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSiteRecoveryManagementTargetComputeSizesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SiteRecoveryManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_target_compute_sizes_list_by_replication_protected_items(self, resource_group):
        response = self.client.target_compute_sizes.list_by_replication_protected_items(
            fabric_name="str",
            protection_container_name="str",
            replicated_protected_item_name="str",
            api_version="2025-01-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
