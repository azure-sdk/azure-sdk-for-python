# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.containerservice import ContainerServiceClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestContainerServiceTrustedAccessRoleBindingsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ContainerServiceClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_trusted_access_role_bindings_list(self, resource_group):
        response = self.client.trusted_access_role_bindings.list(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2025-05-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_trusted_access_role_bindings_get(self, resource_group):
        response = self.client.trusted_access_role_bindings.get(
            resource_group_name=resource_group.name,
            resource_name="str",
            trusted_access_role_binding_name="str",
            api_version="2025-05-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_trusted_access_role_bindings_begin_create_or_update(self, resource_group):
        response = self.client.trusted_access_role_bindings.begin_create_or_update(
            resource_group_name=resource_group.name,
            resource_name="str",
            trusted_access_role_binding_name="str",
            trusted_access_role_binding={
                "roles": ["str"],
                "sourceResourceId": "str",
                "id": "str",
                "name": "str",
                "provisioningState": "str",
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
            api_version="2025-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_trusted_access_role_bindings_begin_delete(self, resource_group):
        response = self.client.trusted_access_role_bindings.begin_delete(
            resource_group_name=resource_group.name,
            resource_name="str",
            trusted_access_role_binding_name="str",
            api_version="2025-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
