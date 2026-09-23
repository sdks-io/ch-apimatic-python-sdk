from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.pg_ha_type import PgHaTypeOrStr
from .enums.vm_size import VmSizeOrStr
from .resource_tags_v1 import ResourceTagsV1, ResourceTagsV1Dict


class PostgresServicePatchRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the Postgres service. Alphanumerical string with whitespaces up to 50 characters."""

    size: Optional[VmSizeOrStr] = UNSET
    """The VM size for a Postgres service."""

    ha_type: Optional[PgHaTypeOrStr] = Field(default=UNSET, alias="haType")
    """Type of high availability: “none” for no replication, “async” for asynchronous replication to a single standby,
    and “sync” for synchronous replication to two standbys."""

    tags: Optional[list[ResourceTagsV1]] = UNSET
    """Tags associated with the Postgres service. Tag keys starting with “chc_” are reserved for internal use."""


class PostgresServicePatchRequestDict(TypedDict):
    name: NotRequired[str]
    size: NotRequired[VmSizeOrStr]
    ha_type: NotRequired[PgHaTypeOrStr]
    tags: NotRequired[list[ResourceTagsV1Dict]]
