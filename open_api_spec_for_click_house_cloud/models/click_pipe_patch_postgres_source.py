from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_pipe_patch_postgres_pipe_remove_table_mapping import (
    ClickPipePatchPostgresPipeRemoveTableMapping,
    ClickPipePatchPostgresPipeRemoveTableMappingDict,
)
from .click_pipe_patch_postgres_pipe_settings import (
    ClickPipePatchPostgresPipeSettings,
    ClickPipePatchPostgresPipeSettingsDict,
)
from .click_pipe_postgres_pipe_table_mapping import (
    ClickPipePostgresPipeTableMapping,
    ClickPipePostgresPipeTableMappingDict,
)
from .plain import Plain, PlainDict


class ClickPipePatchPostgresSource(SdkBaseModel):
    credentials: Optional[Plain] = UNSET
    host: OptionalNullable[str] = UNSET
    """PostgreSQL server hostname or IP address. To use a reverse private endpoint, pass the endpoint hostname here."""

    port: OptionalNullable[int] = UNSET
    """PostgreSQL server port."""

    database: OptionalNullable[str] = UNSET
    """PostgreSQL database name to replicate from."""

    tls_host: OptionalNullable[str] = Field(default=UNSET, alias="tlsHost")
    """TLS/SSL host for secure connections."""

    ca_certificate: OptionalNullable[str] = Field(default=UNSET, alias="caCertificate")
    """PEM encoded CA certificate to validate the Postgres server certificate."""

    disable_tls: OptionalNullable[bool] = Field(default=UNSET, alias="disableTls")
    """Disable TLS for the Postgres connection. Use with caution in production environments."""

    skip_cert_verification: OptionalNullable[bool] = Field(default=UNSET, alias="skipCertVerification")
    """Skip TLS certificate verification for the Postgres connection. Use with caution in production environments."""

    settings: Optional[ClickPipePatchPostgresPipeSettings] = UNSET
    table_mappings_to_add: Optional[list[ClickPipePostgresPipeTableMapping]] = Field(
        default=UNSET, alias="tableMappingsToAdd"
    )
    """Table mappings to add to the pipe. Can be an empty array if no tables are being added."""

    table_mappings_to_remove: Optional[list[ClickPipePatchPostgresPipeRemoveTableMapping]] = Field(
        default=UNSET, alias="tableMappingsToRemove"
    )
    """Table mappings to remove from the pipe. Only sourceSchemaName, sourceTable, and targetTable are required for
    removal."""


class ClickPipePatchPostgresSourceDict(TypedDict):
    credentials: NotRequired[PlainDict]
    host: NotRequired[str | None]
    port: NotRequired[int | None]
    database: NotRequired[str | None]
    tls_host: NotRequired[str | None]
    ca_certificate: NotRequired[str | None]
    disable_tls: NotRequired[bool | None]
    skip_cert_verification: NotRequired[bool | None]
    settings: NotRequired[ClickPipePatchPostgresPipeSettingsDict]
    table_mappings_to_add: NotRequired[list[ClickPipePostgresPipeTableMappingDict]]
    table_mappings_to_remove: NotRequired[list[ClickPipePatchPostgresPipeRemoveTableMappingDict]]
