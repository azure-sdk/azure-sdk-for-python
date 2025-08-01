# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.sql.aio import SqlManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSqlManagementLongTermRetentionBackupsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SqlManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_list_by_location(self, resource_group):
        response = self.client.long_term_retention_backups.list_by_location(
            location_name="str",
            api_version="2024-11-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_list_by_server(self, resource_group):
        response = self.client.long_term_retention_backups.list_by_server(
            location_name="str",
            long_term_retention_server_name="str",
            api_version="2024-11-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_list_by_database(self, resource_group):
        response = self.client.long_term_retention_backups.list_by_database(
            location_name="str",
            long_term_retention_server_name="str",
            long_term_retention_database_name="str",
            api_version="2024-11-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_get(self, resource_group):
        response = await self.client.long_term_retention_backups.get(
            location_name="str",
            long_term_retention_server_name="str",
            long_term_retention_database_name="str",
            backup_name="str",
            api_version="2024-11-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_delete(self, resource_group):
        response = await (
            await self.client.long_term_retention_backups.begin_delete(
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_change_access_tier(self, resource_group):
        response = await (
            await self.client.long_term_retention_backups.begin_change_access_tier(
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                parameters={"backupStorageAccessTier": "str", "operationMode": "str"},
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_copy(self, resource_group):
        response = await (
            await self.client.long_term_retention_backups.begin_copy(
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                parameters={
                    "targetBackupStorageRedundancy": "str",
                    "targetDatabaseName": "str",
                    "targetResourceGroup": "str",
                    "targetServerFullyQualifiedDomainName": "str",
                    "targetServerResourceId": "str",
                    "targetSubscriptionId": "str",
                },
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_lock_time_based_immutability(self, resource_group):
        response = await (
            await self.client.long_term_retention_backups.begin_lock_time_based_immutability(
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_remove_legal_hold_immutability(self, resource_group):
        response = await (
            await self.client.long_term_retention_backups.begin_remove_legal_hold_immutability(
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_remove_time_based_immutability(self, resource_group):
        response = await (
            await self.client.long_term_retention_backups.begin_remove_time_based_immutability(
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_set_legal_hold_immutability(self, resource_group):
        response = await (
            await self.client.long_term_retention_backups.begin_set_legal_hold_immutability(
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_update(self, resource_group):
        response = await (
            await self.client.long_term_retention_backups.begin_update(
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                parameters={"requestedBackupStorageRedundancy": "str"},
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_list_by_resource_group_location(self, resource_group):
        response = self.client.long_term_retention_backups.list_by_resource_group_location(
            resource_group_name=resource_group.name,
            location_name="str",
            api_version="2024-11-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_list_by_resource_group_server(self, resource_group):
        response = self.client.long_term_retention_backups.list_by_resource_group_server(
            resource_group_name=resource_group.name,
            location_name="str",
            long_term_retention_server_name="str",
            api_version="2024-11-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_list_by_resource_group_database(self, resource_group):
        response = self.client.long_term_retention_backups.list_by_resource_group_database(
            resource_group_name=resource_group.name,
            location_name="str",
            long_term_retention_server_name="str",
            long_term_retention_database_name="str",
            api_version="2024-11-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_get_by_resource_group(self, resource_group):
        response = await self.client.long_term_retention_backups.get_by_resource_group(
            resource_group_name=resource_group.name,
            location_name="str",
            long_term_retention_server_name="str",
            long_term_retention_database_name="str",
            backup_name="str",
            api_version="2024-11-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_delete_by_resource_group(self, resource_group):
        response = await (
            await self.client.long_term_retention_backups.begin_delete_by_resource_group(
                resource_group_name=resource_group.name,
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_change_access_tier_by_resource_group(self, resource_group):
        response = await (
            await self.client.long_term_retention_backups.begin_change_access_tier_by_resource_group(
                resource_group_name=resource_group.name,
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                parameters={"backupStorageAccessTier": "str", "operationMode": "str"},
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_copy_by_resource_group(self, resource_group):
        response = await (
            await self.client.long_term_retention_backups.begin_copy_by_resource_group(
                resource_group_name=resource_group.name,
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                parameters={
                    "targetBackupStorageRedundancy": "str",
                    "targetDatabaseName": "str",
                    "targetResourceGroup": "str",
                    "targetServerFullyQualifiedDomainName": "str",
                    "targetServerResourceId": "str",
                    "targetSubscriptionId": "str",
                },
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_lock_time_based_immutability_by_resource_group(
        self, resource_group
    ):
        response = await (
            await self.client.long_term_retention_backups.begin_lock_time_based_immutability_by_resource_group(
                resource_group_name=resource_group.name,
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_remove_legal_hold_immutability_by_resource_group(
        self, resource_group
    ):
        response = await (
            await self.client.long_term_retention_backups.begin_remove_legal_hold_immutability_by_resource_group(
                resource_group_name=resource_group.name,
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_remove_time_based_immutability_by_resource_group(
        self, resource_group
    ):
        response = await (
            await self.client.long_term_retention_backups.begin_remove_time_based_immutability_by_resource_group(
                resource_group_name=resource_group.name,
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_set_legal_hold_immutability_by_resource_group(
        self, resource_group
    ):
        response = await (
            await self.client.long_term_retention_backups.begin_set_legal_hold_immutability_by_resource_group(
                resource_group_name=resource_group.name,
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_long_term_retention_backups_begin_update_by_resource_group(self, resource_group):
        response = await (
            await self.client.long_term_retention_backups.begin_update_by_resource_group(
                resource_group_name=resource_group.name,
                location_name="str",
                long_term_retention_server_name="str",
                long_term_retention_database_name="str",
                backup_name="str",
                parameters={"requestedBackupStorageRedundancy": "str"},
                api_version="2024-11-01-preview",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
