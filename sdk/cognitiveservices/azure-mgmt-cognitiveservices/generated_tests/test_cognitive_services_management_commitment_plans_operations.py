# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCognitiveServicesManagementCommitmentPlansOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(CognitiveServicesManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_list(self, resource_group):
        response = self.client.commitment_plans.list(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2025-06-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_get(self, resource_group):
        response = self.client.commitment_plans.get(
            resource_group_name=resource_group.name,
            account_name="str",
            commitment_plan_name="str",
            api_version="2025-06-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_create_or_update(self, resource_group):
        response = self.client.commitment_plans.create_or_update(
            resource_group_name=resource_group.name,
            account_name="str",
            commitment_plan_name="str",
            commitment_plan={
                "etag": "str",
                "id": "str",
                "kind": "str",
                "location": "str",
                "name": "str",
                "properties": {
                    "autoRenew": bool,
                    "commitmentPlanGuid": "str",
                    "current": {
                        "count": 0,
                        "endDate": "str",
                        "quota": {"quantity": 0, "unit": "str"},
                        "startDate": "str",
                        "tier": "str",
                    },
                    "hostingModel": "str",
                    "last": {
                        "count": 0,
                        "endDate": "str",
                        "quota": {"quantity": 0, "unit": "str"},
                        "startDate": "str",
                        "tier": "str",
                    },
                    "next": {
                        "count": 0,
                        "endDate": "str",
                        "quota": {"quantity": 0, "unit": "str"},
                        "startDate": "str",
                        "tier": "str",
                    },
                    "planType": "str",
                    "provisioningIssues": ["str"],
                    "provisioningState": "str",
                },
                "sku": {"name": "str", "capacity": 0, "family": "str", "size": "str", "tier": "str"},
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "type": "str",
            },
            api_version="2025-06-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_begin_delete(self, resource_group):
        response = self.client.commitment_plans.begin_delete(
            resource_group_name=resource_group.name,
            account_name="str",
            commitment_plan_name="str",
            api_version="2025-06-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_begin_create_or_update_plan(self, resource_group):
        response = self.client.commitment_plans.begin_create_or_update_plan(
            resource_group_name=resource_group.name,
            commitment_plan_name="str",
            commitment_plan={
                "etag": "str",
                "id": "str",
                "kind": "str",
                "location": "str",
                "name": "str",
                "properties": {
                    "autoRenew": bool,
                    "commitmentPlanGuid": "str",
                    "current": {
                        "count": 0,
                        "endDate": "str",
                        "quota": {"quantity": 0, "unit": "str"},
                        "startDate": "str",
                        "tier": "str",
                    },
                    "hostingModel": "str",
                    "last": {
                        "count": 0,
                        "endDate": "str",
                        "quota": {"quantity": 0, "unit": "str"},
                        "startDate": "str",
                        "tier": "str",
                    },
                    "next": {
                        "count": 0,
                        "endDate": "str",
                        "quota": {"quantity": 0, "unit": "str"},
                        "startDate": "str",
                        "tier": "str",
                    },
                    "planType": "str",
                    "provisioningIssues": ["str"],
                    "provisioningState": "str",
                },
                "sku": {"name": "str", "capacity": 0, "family": "str", "size": "str", "tier": "str"},
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "type": "str",
            },
            api_version="2025-06-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_begin_update_plan(self, resource_group):
        response = self.client.commitment_plans.begin_update_plan(
            resource_group_name=resource_group.name,
            commitment_plan_name="str",
            commitment_plan={
                "sku": {"name": "str", "capacity": 0, "family": "str", "size": "str", "tier": "str"},
                "tags": {"str": "str"},
            },
            api_version="2025-06-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_begin_delete_plan(self, resource_group):
        response = self.client.commitment_plans.begin_delete_plan(
            resource_group_name=resource_group.name,
            commitment_plan_name="str",
            api_version="2025-06-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_get_plan(self, resource_group):
        response = self.client.commitment_plans.get_plan(
            resource_group_name=resource_group.name,
            commitment_plan_name="str",
            api_version="2025-06-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_list_plans_by_resource_group(self, resource_group):
        response = self.client.commitment_plans.list_plans_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2025-06-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_list_plans_by_subscription(self, resource_group):
        response = self.client.commitment_plans.list_plans_by_subscription(
            api_version="2025-06-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_list_associations(self, resource_group):
        response = self.client.commitment_plans.list_associations(
            resource_group_name=resource_group.name,
            commitment_plan_name="str",
            api_version="2025-06-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_get_association(self, resource_group):
        response = self.client.commitment_plans.get_association(
            resource_group_name=resource_group.name,
            commitment_plan_name="str",
            commitment_plan_association_name="str",
            api_version="2025-06-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_begin_create_or_update_association(self, resource_group):
        response = self.client.commitment_plans.begin_create_or_update_association(
            resource_group_name=resource_group.name,
            commitment_plan_name="str",
            commitment_plan_association_name="str",
            association={
                "accountId": "str",
                "etag": "str",
                "id": "str",
                "name": "str",
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "tags": {"str": "str"},
                "type": "str",
            },
            api_version="2025-06-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_commitment_plans_begin_delete_association(self, resource_group):
        response = self.client.commitment_plans.begin_delete_association(
            resource_group_name=resource_group.name,
            commitment_plan_name="str",
            commitment_plan_association_name="str",
            api_version="2025-06-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
