from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .postgres_configuration import PostgresConfiguration, PostgresConfigurationDict
from .resource_tags_v1 import ResourceTagsV1, ResourceTagsV1Dict


class PostgresServiceRestoreRequest(SdkBaseModel):
    name: str
    """Name of the Postgres service. Alphanumerical string with whitespaces up to 50 characters."""

    restore_target: RFC3339DateTime = Field(alias="restoreTarget")
    """The point in time at which to recover, as either date/time, named restore point, or a specific transaction ID."""

    pg_config: Optional[PostgresConfiguration] = Field(default=UNSET, alias="pgConfig")
    """Postgres `runtime configuration <https://www.postgresql.org/docs/current/runtime-config.html>`__
    configuration."""

    pg_bouncer_config: Optional[dict[str, str]] = Field(default=UNSET, alias="pgBouncerConfig")
    """PgBouncer `runtime configuration <https://www.pgbouncer.org/config.html>`__ configuration."""

    tags: Optional[list[ResourceTagsV1]] = UNSET
    """Tags associated with the Postgres service. Tag keys starting with “chc_” are reserved for internal use."""


class PostgresServiceRestoreRequestDict(TypedDict):
    name: str
    restore_target: RFC3339DateTime
    pg_config: NotRequired[PostgresConfigurationDict]
    pg_bouncer_config: NotRequired[dict[str, str]]
    tags: NotRequired[list[ResourceTagsV1Dict]]
