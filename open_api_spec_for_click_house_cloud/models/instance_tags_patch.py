from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .resource_tags_v1 import ResourceTagsV1, ResourceTagsV1Dict


class InstanceTagsPatch(SdkBaseModel):
    add: Optional[list[ResourceTagsV1]] = UNSET
    """Elements to add. Executed after "remove" part is processed."""

    remove: Optional[list[ResourceTagsV1]] = UNSET
    """Elements to remove. Executed before "add" part is processed."""


class InstanceTagsPatchDict(TypedDict):
    add: NotRequired[list[ResourceTagsV1Dict]]
    remove: NotRequired[list[ResourceTagsV1Dict]]
