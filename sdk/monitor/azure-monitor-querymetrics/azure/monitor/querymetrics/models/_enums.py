# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class MetricUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The unit of the metric."""

    COUNT = "Count"
    """Unit of raw quantity."""
    BYTES = "Bytes"
    """Unit of memory in bytes."""
    SECONDS = "Seconds"
    """Unit of time in seconds."""
    COUNT_PER_SECOND = "CountPerSecond"
    """Rate unit of raw quantity per second."""
    BYTES_PER_SECOND = "BytesPerSecond"
    """Rate unit of memory in bytes per second."""
    PERCENT = "Percent"
    """Percentage unit."""
    MILLI_SECONDS = "MilliSeconds"
    """Unit of time in 1/1000th of a second."""
    BYTE_SECONDS = "ByteSeconds"
    """Unit of data transfer or storage. It is the size of the data in bytes
    multiplied by the time it takes to transfer or store the data in seconds."""
    UNSPECIFIED = "Unspecified"
    """No specified unit."""
    CORES = "Cores"
    """Unit of processing power."""
    MILLI_CORES = "MilliCores"
    """Unit of processing power in 1/1000th of a CPU core."""
    NANO_CORES = "NanoCores"
    """Unit of processing power in one billionth of a CPU core."""
    BITS_PER_SECOND = "BitsPerSecond"
    """Rate unit of binary digits per second."""
