# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.hybridcompute import HybridComputeManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestHybridComputeManagementLicenseProfilesOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(HybridComputeManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_license_profiles_begin_create_or_update(self, resource_group):
        response = self.client.license_profiles.begin_create_or_update(
            resource_group_name=resource_group.name,
            machine_name="str",
            parameters={
                "location": "str",
                "assignedLicense": "str",
                "assignedLicenseImmutableId": "str",
                "billingEndDate": "2020-02-20 00:00:00",
                "billingStartDate": "2020-02-20 00:00:00",
                "disenrollmentDate": "2020-02-20 00:00:00",
                "enrollmentDate": "2020-02-20 00:00:00",
                "error": {
                    "additionalInfo": [{"info": {}, "type": "str"}],
                    "code": "str",
                    "details": [...],
                    "message": "str",
                    "target": "str",
                },
                "esuEligibility": "str",
                "esuKeyState": "str",
                "esuKeys": [{"licenseStatus": 0, "sku": "str"}],
                "id": "str",
                "name": "str",
                "productFeatures": [
                    {
                        "billingEndDate": "2020-02-20 00:00:00",
                        "billingStartDate": "2020-02-20 00:00:00",
                        "disenrollmentDate": "2020-02-20 00:00:00",
                        "enrollmentDate": "2020-02-20 00:00:00",
                        "error": {
                            "additionalInfo": [{"info": {}, "type": "str"}],
                            "code": "str",
                            "details": [...],
                            "message": "str",
                            "target": "str",
                        },
                        "name": "str",
                        "subscriptionStatus": "str",
                    }
                ],
                "productType": "str",
                "provisioningState": "str",
                "serverType": "str",
                "softwareAssuranceCustomer": bool,
                "subscriptionStatus": "str",
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
            api_version="2025-02-19-preview",
            license_profile_name="default",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_license_profiles_begin_update(self, resource_group):
        response = self.client.license_profiles.begin_update(
            resource_group_name=resource_group.name,
            machine_name="str",
            parameters={
                "assignedLicense": "str",
                "productFeatures": [{"name": "str", "subscriptionStatus": "str"}],
                "productType": "str",
                "softwareAssuranceCustomer": bool,
                "subscriptionStatus": "str",
                "tags": {"str": "str"},
            },
            api_version="2025-02-19-preview",
            license_profile_name="default",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_license_profiles_get(self, resource_group):
        response = self.client.license_profiles.get(
            resource_group_name=resource_group.name,
            machine_name="str",
            api_version="2025-02-19-preview",
            license_profile_name="default",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_license_profiles_begin_delete(self, resource_group):
        response = self.client.license_profiles.begin_delete(
            resource_group_name=resource_group.name,
            machine_name="str",
            api_version="2025-02-19-preview",
            license_profile_name="default",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_license_profiles_list(self, resource_group):
        response = self.client.license_profiles.list(
            resource_group_name=resource_group.name,
            machine_name="str",
            api_version="2025-02-19-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
