# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.network.aio import NetworkManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkManagementHubVirtualNetworkConnectionsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_hub_virtual_network_connections_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.hub_virtual_network_connections.begin_create_or_update(
                resource_group_name=resource_group.name,
                virtual_hub_name="str",
                connection_name="str",
                hub_virtual_network_connection_parameters={
                    "allowHubToRemoteVnetTransit": bool,
                    "allowRemoteVnetToUseHubVnetGateways": bool,
                    "enableInternetSecurity": bool,
                    "etag": "str",
                    "id": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "remoteVirtualNetwork": {"id": "str"},
                    "routingConfiguration": {
                        "associatedRouteTable": {"id": "str"},
                        "inboundRouteMap": {"id": "str"},
                        "outboundRouteMap": {"id": "str"},
                        "propagatedRouteTables": {"ids": [{"id": "str"}], "labels": ["str"]},
                        "vnetRoutes": {
                            "bgpConnections": [{"id": "str"}],
                            "staticRoutes": [{"addressPrefixes": ["str"], "name": "str", "nextHopIpAddress": "str"}],
                            "staticRoutesConfig": {
                                "propagateStaticRoutes": bool,
                                "vnetLocalRouteOverrideCriteria": "str",
                            },
                        },
                    },
                },
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_hub_virtual_network_connections_begin_delete(self, resource_group):
        response = await (
            await self.client.hub_virtual_network_connections.begin_delete(
                resource_group_name=resource_group.name,
                virtual_hub_name="str",
                connection_name="str",
                api_version="2024-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_hub_virtual_network_connections_get(self, resource_group):
        response = await self.client.hub_virtual_network_connections.get(
            resource_group_name=resource_group.name,
            virtual_hub_name="str",
            connection_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_hub_virtual_network_connections_list(self, resource_group):
        response = self.client.hub_virtual_network_connections.list(
            resource_group_name=resource_group.name,
            virtual_hub_name="str",
            api_version="2024-07-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
