# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ApiVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    V2022_01_11_PREVIEW2 = "2022-01-11-preview2"
    V2022_12_01 = "2022-12-01"
    V2023_05_01_PREVIEW = "2023-05-01-preview"
    V2024_03_01_PREVIEW = "2024-03-01-preview"
    V2025_02_11 = "2025-02-11"
    V2025_04_01 = "2025-04-01"


DEFAULT_VERSION = ApiVersion.V2025_04_01
