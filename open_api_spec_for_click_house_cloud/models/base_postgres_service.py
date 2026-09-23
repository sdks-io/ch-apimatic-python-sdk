from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cloud_provider import CloudProviderOrStr
from .enums.pg_ha_type import PgHaTypeOrStr
from .enums.postgres_major_version import PostgresMajorVersionOrStr
from .enums.vm_size import VmSizeOrStr
from .resource_tags_v1 import ResourceTagsV1, ResourceTagsV1Dict


class BasePostgresService(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the Postgres service. Alphanumerical string with whitespaces up to 50 characters."""

    provider: Optional[CloudProviderOrStr] = UNSET
    """The cloud provider for a Postgres service."""

    region: Optional[str] = UNSET
    """The cloud region for a Postgres service."""

    postgres_version: Optional[PostgresMajorVersionOrStr] = Field(default=UNSET, alias="postgresVersion")
    size: Optional[VmSizeOrStr] = UNSET
    """The VM size for a Postgres service."""

    ha_type: Optional[PgHaTypeOrStr] = Field(default=UNSET, alias="haType")
    """Type of high availability: “none” for no replication, “async” for asynchronous replication to a single standby,
    and “sync” for synchronous replication to two standbys."""

    tags: Optional[list[ResourceTagsV1]] = UNSET
    """Tags associated with the Postgres service. Tag keys starting with “chc_” are reserved for internal use."""


class BasePostgresServiceDict(TypedDict):
    name: NotRequired[str]
    provider: NotRequired[CloudProviderOrStr]
    region: NotRequired[str]
    postgres_version: NotRequired[PostgresMajorVersionOrStr]
    size: NotRequired[VmSizeOrStr]
    ha_type: NotRequired[PgHaTypeOrStr]
    tags: NotRequired[list[ResourceTagsV1Dict]]
