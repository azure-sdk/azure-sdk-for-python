# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.storage.aio import StorageManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestStorageManagementFileSharesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(StorageManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_file_shares_list(self, resource_group):
        response = self.client.file_shares.list(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-01-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_file_shares_create(self, resource_group):
        response = await self.client.file_shares.create(
            resource_group_name=resource_group.name,
            account_name="str",
            share_name="str",
            file_share={
                "accessTier": "str",
                "accessTierChangeTime": "2020-02-20 00:00:00",
                "accessTierStatus": "str",
                "deleted": bool,
                "deletedTime": "2020-02-20 00:00:00",
                "enabledProtocols": "str",
                "etag": "str",
                "fileSharePaidBursting": {
                    "paidBurstingEnabled": bool,
                    "paidBurstingMaxBandwidthMibps": 0,
                    "paidBurstingMaxIops": 0,
                },
                "id": "str",
                "includedBurstIops": 0,
                "lastModifiedTime": "2020-02-20 00:00:00",
                "leaseDuration": "str",
                "leaseState": "str",
                "leaseStatus": "str",
                "maxBurstCreditsForIops": 0,
                "metadata": {"str": "str"},
                "name": "str",
                "nextAllowedProvisionedBandwidthDowngradeTime": "2020-02-20 00:00:00",
                "nextAllowedProvisionedIopsDowngradeTime": "2020-02-20 00:00:00",
                "nextAllowedQuotaDowngradeTime": "2020-02-20 00:00:00",
                "provisionedBandwidthMibps": 0,
                "provisionedIops": 0,
                "remainingRetentionDays": 0,
                "rootSquash": "str",
                "shareQuota": 0,
                "shareUsageBytes": 0,
                "signedIdentifiers": [
                    {
                        "accessPolicy": {
                            "expiryTime": "2020-02-20 00:00:00",
                            "permission": "str",
                            "startTime": "2020-02-20 00:00:00",
                        },
                        "id": "str",
                    }
                ],
                "snapshotTime": "2020-02-20 00:00:00",
                "type": "str",
                "version": "str",
            },
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_file_shares_update(self, resource_group):
        response = await self.client.file_shares.update(
            resource_group_name=resource_group.name,
            account_name="str",
            share_name="str",
            file_share={
                "accessTier": "str",
                "accessTierChangeTime": "2020-02-20 00:00:00",
                "accessTierStatus": "str",
                "deleted": bool,
                "deletedTime": "2020-02-20 00:00:00",
                "enabledProtocols": "str",
                "etag": "str",
                "fileSharePaidBursting": {
                    "paidBurstingEnabled": bool,
                    "paidBurstingMaxBandwidthMibps": 0,
                    "paidBurstingMaxIops": 0,
                },
                "id": "str",
                "includedBurstIops": 0,
                "lastModifiedTime": "2020-02-20 00:00:00",
                "leaseDuration": "str",
                "leaseState": "str",
                "leaseStatus": "str",
                "maxBurstCreditsForIops": 0,
                "metadata": {"str": "str"},
                "name": "str",
                "nextAllowedProvisionedBandwidthDowngradeTime": "2020-02-20 00:00:00",
                "nextAllowedProvisionedIopsDowngradeTime": "2020-02-20 00:00:00",
                "nextAllowedQuotaDowngradeTime": "2020-02-20 00:00:00",
                "provisionedBandwidthMibps": 0,
                "provisionedIops": 0,
                "remainingRetentionDays": 0,
                "rootSquash": "str",
                "shareQuota": 0,
                "shareUsageBytes": 0,
                "signedIdentifiers": [
                    {
                        "accessPolicy": {
                            "expiryTime": "2020-02-20 00:00:00",
                            "permission": "str",
                            "startTime": "2020-02-20 00:00:00",
                        },
                        "id": "str",
                    }
                ],
                "snapshotTime": "2020-02-20 00:00:00",
                "type": "str",
                "version": "str",
            },
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_file_shares_get(self, resource_group):
        response = await self.client.file_shares.get(
            resource_group_name=resource_group.name,
            account_name="str",
            share_name="str",
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_file_shares_delete(self, resource_group):
        response = await self.client.file_shares.delete(
            resource_group_name=resource_group.name,
            account_name="str",
            share_name="str",
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_file_shares_restore(self, resource_group):
        response = await self.client.file_shares.restore(
            resource_group_name=resource_group.name,
            account_name="str",
            share_name="str",
            deleted_share={"deletedShareName": "str", "deletedShareVersion": "str"},
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_file_shares_lease(self, resource_group):
        response = await self.client.file_shares.lease(
            resource_group_name=resource_group.name,
            account_name="str",
            share_name="str",
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...
