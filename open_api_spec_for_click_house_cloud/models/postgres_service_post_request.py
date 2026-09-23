from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cloud_provider import CloudProviderOrStr
from .enums.pg_ha_type import PgHaTypeOrStr
from .enums.postgres_major_version import PostgresMajorVersionOrStr
from .enums.vm_size import VmSizeOrStr
from .postgres_configuration import PostgresConfiguration, PostgresConfigurationDict
from .resource_tags_v1 import ResourceTagsV1, ResourceTagsV1Dict


class PostgresServicePostRequest(SdkBaseModel):
    name: str
    """Name of the Postgres service. Alphanumerical string with whitespaces up to 50 characters."""

    provider: CloudProviderOrStr
    """The cloud provider for a Postgres service."""

    region: str
    """The cloud region for a Postgres service."""

    postgres_version: Optional[PostgresMajorVersionOrStr] = Field(default=UNSET, alias="postgresVersion")
    size: VmSizeOrStr
    """The VM size for a Postgres service."""

    ha_type: Optional[PgHaTypeOrStr] = Field(default=UNSET, alias="haType")
    """Type of high availability: “none” for no replication, “async” for asynchronous replication to a single standby,
    and “sync” for synchronous replication to two standbys."""

    tags: Optional[list[ResourceTagsV1]] = UNSET
    """Tags associated with the Postgres service. Tag keys starting with “chc_” are reserved for internal use."""

    pg_config: Optional[PostgresConfiguration] = Field(default=UNSET, alias="pgConfig")
    """Postgres `runtime configuration <https://www.postgresql.org/docs/current/runtime-config.html>`__
    configuration."""

    pg_bouncer_config: Optional[dict[str, str]] = Field(default=UNSET, alias="pgBouncerConfig")
    """PgBouncer `runtime configuration <https://www.pgbouncer.org/config.html>`__ configuration."""


class PostgresServicePostRequestDict(TypedDict):
    name: str
    provider: CloudProviderOrStr
    region: str
    postgres_version: NotRequired[PostgresMajorVersionOrStr]
    size: VmSizeOrStr
    ha_type: NotRequired[PgHaTypeOrStr]
    tags: NotRequired[list[ResourceTagsV1Dict]]
    pg_config: NotRequired[PostgresConfigurationDict]
    pg_bouncer_config: NotRequired[dict[str, str]]
