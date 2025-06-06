# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
# pylint: disable=too-few-public-methods

from typing import Any, List, Optional

from azure.storage.blob.aio._models import ContainerPropertiesPaged
from .._models import FileSystemProperties


class FileSystemPropertiesPaged(ContainerPropertiesPaged):
    """An Iterable of File System properties.

    :param command: Function to retrieve the next page of items.
    :paramtype command: ~typing.Callable[]
    :param str prefix: Filters the results to return only file systems whose names
        begin with the specified prefix.
    :param int results_per_page: The maximum number of file system names to retrieve per call.
    :param str continuation_token: An opaque continuation token.
    """

    service_endpoint: Optional[str]
    """The service URL."""
    prefix: Optional[str]
    """A file system name prefix being used to filter the list."""
    marker: Optional[str]
    """The continuation token of the current page of results."""
    results_per_page: Optional[int]
    """The maximum number of results retrieved per API call."""
    continuation_token: Optional[str]
    """The continuation token to retrieve the next page of results."""
    location_mode: Optional[str]
    """The location mode being used to list results. The available
        options include "primary" and "secondary"."""
    current_page: List[FileSystemProperties]  # type: ignore [assignment]
    """The current page of listed results."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(FileSystemPropertiesPaged, self).__init__(
            *args,
            **kwargs
        )

    @staticmethod
    def _build_item(item):
        return FileSystemProperties._from_generated(item)  # pylint: disable=protected-access
