from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ip_access_list_entry import IpAccessListEntry, IpAccessListEntryDict


class IpAccessListPatch(SdkBaseModel):
    add: Optional[list[IpAccessListEntry]] = UNSET
    """Elements to add. Executed after "remove" part is processed."""

    remove: Optional[list[IpAccessListEntry]] = UNSET
    """Elements to remove. Executed before "add" part is processed."""


class IpAccessListPatchDict(TypedDict):
    add: NotRequired[list[IpAccessListEntryDict]]
    remove: NotRequired[list[IpAccessListEntryDict]]
