# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.netapp import NetAppManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-netapp
# USAGE
    python volume_groups_create_oracle.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetAppManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.volume_groups.begin_create(
        resource_group_name="myRG",
        account_name="account1",
        volume_group_name="group1",
        body={
            "location": "westus",
            "properties": {
                "groupMetaData": {
                    "applicationIdentifier": "OR2",
                    "applicationType": "ORACLE",
                    "groupDescription": "Volume group",
                },
                "volumes": [
                    {
                        "name": "test-ora-data1",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-ora-data1",
                            "exportPolicy": {
                                "rules": [
                                    {
                                        "allowedClients": "0.0.0.0/0",
                                        "cifs": False,
                                        "hasRootAccess": True,
                                        "kerberos5ReadOnly": False,
                                        "kerberos5ReadWrite": False,
                                        "kerberos5iReadOnly": False,
                                        "kerberos5iReadWrite": False,
                                        "kerberos5pReadOnly": False,
                                        "kerberos5pReadWrite": False,
                                        "nfsv3": False,
                                        "nfsv41": True,
                                        "ruleIndex": 1,
                                        "unixReadOnly": True,
                                        "unixReadWrite": True,
                                    }
                                ]
                            },
                            "protocolTypes": ["NFSv4.1"],
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "ora-data1",
                        },
                        "zones": ["1"],
                    },
                    {
                        "name": "test-ora-data2",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-ora-data2",
                            "exportPolicy": {
                                "rules": [
                                    {
                                        "allowedClients": "0.0.0.0/0",
                                        "cifs": False,
                                        "hasRootAccess": True,
                                        "kerberos5ReadOnly": False,
                                        "kerberos5ReadWrite": False,
                                        "kerberos5iReadOnly": False,
                                        "kerberos5iReadWrite": False,
                                        "kerberos5pReadOnly": False,
                                        "kerberos5pReadWrite": False,
                                        "nfsv3": False,
                                        "nfsv41": True,
                                        "ruleIndex": 1,
                                        "unixReadOnly": True,
                                        "unixReadWrite": True,
                                    }
                                ]
                            },
                            "protocolTypes": ["NFSv4.1"],
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "ora-data2",
                        },
                        "zones": ["1"],
                    },
                    {
                        "name": "test-ora-data3",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-ora-data3",
                            "exportPolicy": {
                                "rules": [
                                    {
                                        "allowedClients": "0.0.0.0/0",
                                        "cifs": False,
                                        "hasRootAccess": True,
                                        "kerberos5ReadOnly": False,
                                        "kerberos5ReadWrite": False,
                                        "kerberos5iReadOnly": False,
                                        "kerberos5iReadWrite": False,
                                        "kerberos5pReadOnly": False,
                                        "kerberos5pReadWrite": False,
                                        "nfsv3": False,
                                        "nfsv41": True,
                                        "ruleIndex": 1,
                                        "unixReadOnly": True,
                                        "unixReadWrite": True,
                                    }
                                ]
                            },
                            "protocolTypes": ["NFSv4.1"],
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "ora-data3",
                        },
                        "zones": ["1"],
                    },
                    {
                        "name": "test-ora-data4",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-ora-data4",
                            "exportPolicy": {
                                "rules": [
                                    {
                                        "allowedClients": "0.0.0.0/0",
                                        "cifs": False,
                                        "hasRootAccess": True,
                                        "kerberos5ReadOnly": False,
                                        "kerberos5ReadWrite": False,
                                        "kerberos5iReadOnly": False,
                                        "kerberos5iReadWrite": False,
                                        "kerberos5pReadOnly": False,
                                        "kerberos5pReadWrite": False,
                                        "nfsv3": False,
                                        "nfsv41": True,
                                        "ruleIndex": 1,
                                        "unixReadOnly": True,
                                        "unixReadWrite": True,
                                    }
                                ]
                            },
                            "protocolTypes": ["NFSv4.1"],
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "ora-data4",
                        },
                        "zones": ["1"],
                    },
                    {
                        "name": "test-ora-data5",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-ora-data5",
                            "exportPolicy": {
                                "rules": [
                                    {
                                        "allowedClients": "0.0.0.0/0",
                                        "cifs": False,
                                        "hasRootAccess": True,
                                        "kerberos5ReadOnly": False,
                                        "kerberos5ReadWrite": False,
                                        "kerberos5iReadOnly": False,
                                        "kerberos5iReadWrite": False,
                                        "kerberos5pReadOnly": False,
                                        "kerberos5pReadWrite": False,
                                        "nfsv3": False,
                                        "nfsv41": True,
                                        "ruleIndex": 1,
                                        "unixReadOnly": True,
                                        "unixReadWrite": True,
                                    }
                                ]
                            },
                            "protocolTypes": ["NFSv4.1"],
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "ora-data5",
                        },
                        "zones": ["1"],
                    },
                    {
                        "name": "test-ora-data6",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-ora-data6",
                            "exportPolicy": {
                                "rules": [
                                    {
                                        "allowedClients": "0.0.0.0/0",
                                        "cifs": False,
                                        "hasRootAccess": True,
                                        "kerberos5ReadOnly": False,
                                        "kerberos5ReadWrite": False,
                                        "kerberos5iReadOnly": False,
                                        "kerberos5iReadWrite": False,
                                        "kerberos5pReadOnly": False,
                                        "kerberos5pReadWrite": False,
                                        "nfsv3": False,
                                        "nfsv41": True,
                                        "ruleIndex": 1,
                                        "unixReadOnly": True,
                                        "unixReadWrite": True,
                                    }
                                ]
                            },
                            "protocolTypes": ["NFSv4.1"],
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "ora-data6",
                        },
                        "zones": ["1"],
                    },
                    {
                        "name": "test-ora-data7",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-ora-data7",
                            "exportPolicy": {
                                "rules": [
                                    {
                                        "allowedClients": "0.0.0.0/0",
                                        "cifs": False,
                                        "hasRootAccess": True,
                                        "kerberos5ReadOnly": False,
                                        "kerberos5ReadWrite": False,
                                        "kerberos5iReadOnly": False,
                                        "kerberos5iReadWrite": False,
                                        "kerberos5pReadOnly": False,
                                        "kerberos5pReadWrite": False,
                                        "nfsv3": False,
                                        "nfsv41": True,
                                        "ruleIndex": 1,
                                        "unixReadOnly": True,
                                        "unixReadWrite": True,
                                    }
                                ]
                            },
                            "protocolTypes": ["NFSv4.1"],
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "ora-data7",
                        },
                        "zones": ["1"],
                    },
                    {
                        "name": "test-ora-data8",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-ora-data8",
                            "exportPolicy": {
                                "rules": [
                                    {
                                        "allowedClients": "0.0.0.0/0",
                                        "cifs": False,
                                        "hasRootAccess": True,
                                        "kerberos5ReadOnly": False,
                                        "kerberos5ReadWrite": False,
                                        "kerberos5iReadOnly": False,
                                        "kerberos5iReadWrite": False,
                                        "kerberos5pReadOnly": False,
                                        "kerberos5pReadWrite": False,
                                        "nfsv3": False,
                                        "nfsv41": True,
                                        "ruleIndex": 1,
                                        "unixReadOnly": True,
                                        "unixReadWrite": True,
                                    }
                                ]
                            },
                            "protocolTypes": ["NFSv4.1"],
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "ora-data8",
                        },
                        "zones": ["1"],
                    },
                    {
                        "name": "test-ora-log",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-ora-log",
                            "exportPolicy": {
                                "rules": [
                                    {
                                        "allowedClients": "0.0.0.0/0",
                                        "cifs": False,
                                        "hasRootAccess": True,
                                        "kerberos5ReadOnly": False,
                                        "kerberos5ReadWrite": False,
                                        "kerberos5iReadOnly": False,
                                        "kerberos5iReadWrite": False,
                                        "kerberos5pReadOnly": False,
                                        "kerberos5pReadWrite": False,
                                        "nfsv3": False,
                                        "nfsv41": True,
                                        "ruleIndex": 1,
                                        "unixReadOnly": True,
                                        "unixReadWrite": True,
                                    }
                                ]
                            },
                            "protocolTypes": ["NFSv4.1"],
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "ora-log",
                        },
                        "zones": ["1"],
                    },
                    {
                        "name": "test-ora-log-mirror",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-ora-log-mirror",
                            "exportPolicy": {
                                "rules": [
                                    {
                                        "allowedClients": "0.0.0.0/0",
                                        "cifs": False,
                                        "hasRootAccess": True,
                                        "kerberos5ReadOnly": False,
                                        "kerberos5ReadWrite": False,
                                        "kerberos5iReadOnly": False,
                                        "kerberos5iReadWrite": False,
                                        "kerberos5pReadOnly": False,
                                        "kerberos5pReadWrite": False,
                                        "nfsv3": False,
                                        "nfsv41": True,
                                        "ruleIndex": 1,
                                        "unixReadOnly": True,
                                        "unixReadWrite": True,
                                    }
                                ]
                            },
                            "protocolTypes": ["NFSv4.1"],
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "ora-log-mirror",
                        },
                        "zones": ["1"],
                    },
                    {
                        "name": "test-ora-binary",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-ora-binary",
                            "exportPolicy": {
                                "rules": [
                                    {
                                        "allowedClients": "0.0.0.0/0",
                                        "cifs": False,
                                        "hasRootAccess": True,
                                        "kerberos5ReadOnly": False,
                                        "kerberos5ReadWrite": False,
                                        "kerberos5iReadOnly": False,
                                        "kerberos5iReadWrite": False,
                                        "kerberos5pReadOnly": False,
                                        "kerberos5pReadWrite": False,
                                        "nfsv3": False,
                                        "nfsv41": True,
                                        "ruleIndex": 1,
                                        "unixReadOnly": True,
                                        "unixReadWrite": True,
                                    }
                                ]
                            },
                            "protocolTypes": ["NFSv4.1"],
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "ora-binary",
                        },
                        "zones": ["1"],
                    },
                    {
                        "name": "test-ora-backup",
                        "properties": {
                            "capacityPoolResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRG/providers/Microsoft.NetApp/netAppAccounts/account1/capacityPools/pool1",
                            "creationToken": "test-ora-backup",
                            "exportPolicy": {
                                "rules": [
                                    {
                                        "allowedClients": "0.0.0.0/0",
                                        "cifs": False,
                                        "hasRootAccess": True,
                                        "kerberos5ReadOnly": False,
                                        "kerberos5ReadWrite": False,
                                        "kerberos5iReadOnly": False,
                                        "kerberos5iReadWrite": False,
                                        "kerberos5pReadOnly": False,
                                        "kerberos5pReadWrite": False,
                                        "nfsv3": False,
                                        "nfsv41": True,
                                        "ruleIndex": 1,
                                        "unixReadOnly": True,
                                        "unixReadWrite": True,
                                    }
                                ]
                            },
                            "protocolTypes": ["NFSv4.1"],
                            "serviceLevel": "Premium",
                            "subnetId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myRP/providers/Microsoft.Network/virtualNetworks/testvnet3/subnets/testsubnet3",
                            "throughputMibps": 10,
                            "usageThreshold": 107374182400,
                            "volumeSpecName": "ora-backup",
                        },
                        "zones": ["1"],
                    },
                ],
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/netapp/resource-manager/Microsoft.NetApp/stable/2025-03-01/examples/VolumeGroups_Create_Oracle.json
if __name__ == "__main__":
    main()
