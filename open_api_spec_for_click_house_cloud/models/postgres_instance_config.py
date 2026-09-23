from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .postgres_configuration import PostgresConfiguration, PostgresConfigurationDict


class PostgresInstanceConfig(SdkBaseModel):
    pg_config: PostgresConfiguration = Field(alias="pgConfig")
    """Postgres `runtime configuration <https://www.postgresql.org/docs/current/runtime-config.html>`__
    configuration."""

    pg_bouncer_config: dict[str, str] = Field(alias="pgBouncerConfig")
    """PgBouncer `runtime configuration <https://www.pgbouncer.org/config.html>`__ configuration."""


class PostgresInstanceConfigDict(TypedDict):
    pg_config: PostgresConfigurationDict
    pg_bouncer_config: dict[str, str]
