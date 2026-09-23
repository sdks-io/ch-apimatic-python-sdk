from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .postgres_configuration import PostgresConfiguration, PostgresConfigurationDict


class PostgresInstanceUpdateConfigResponse(SdkBaseModel):
    pg_config: PostgresConfiguration = Field(alias="pgConfig")
    """Postgres `runtime configuration <https://www.postgresql.org/docs/current/runtime-config.html>`__
    configuration."""

    pg_bouncer_config: dict[str, str] = Field(alias="pgBouncerConfig")
    """PgBouncer `runtime configuration <https://www.pgbouncer.org/config.html>`__ configuration."""

    message: Optional[str] = UNSET
    """Informational message about the configuration update, such as restart requirements."""


class PostgresInstanceUpdateConfigResponseDict(TypedDict):
    pg_config: PostgresConfigurationDict
    pg_bouncer_config: dict[str, str]
    message: NotRequired[str]
