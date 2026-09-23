from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_pipe_postgres_pipe_settings import ClickPipePostgresPipeSettings, ClickPipePostgresPipeSettingsDict
from .click_pipe_postgres_pipe_table_mapping import (
    ClickPipePostgresPipeTableMapping,
    ClickPipePostgresPipeTableMappingDict,
)
from .enums.authentication11 import Authentication11OrStr
from .enums.type7 import Type7OrStr


class ClickPipePostgresSource(SdkBaseModel):
    type_: OptionalNullable[Type7OrStr] = Field(default=UNSET, alias="type")
    """Type of the Postgres source. Defaults to "postgres" if not specified."""

    host: Optional[str] = UNSET
    """PostgreSQL server hostname or IP address. To use a reverse private endpoint, pass the endpoint hostname here."""

    port: Optional[int] = UNSET
    """PostgreSQL server port."""

    database: Optional[str] = UNSET
    """PostgreSQL database name to replicate from."""

    authentication: Optional[Authentication11OrStr] = UNSET
    """Authentication method for Postgres connection."""

    iam_role: Optional[str] = Field(default=UNSET, alias="iamRole")
    """IAM role ARN for IAM authentication (required for IAM_ROLE authentication)."""

    tls_host: Optional[str] = Field(default=UNSET, alias="tlsHost")
    """TLS/SSL host for secure connections."""

    ca_certificate: Optional[str] = Field(default=UNSET, alias="caCertificate")
    """PEM encoded CA certificate to validate the Postgres server certificate."""

    disable_tls: Optional[bool] = Field(default=UNSET, alias="disableTls")
    """Disable TLS for the Postgres connection. Use with caution in production environments."""

    skip_cert_verification: Optional[bool] = Field(default=UNSET, alias="skipCertVerification")
    """Skip TLS certificate verification for the Postgres connection. Use with caution in production environments."""

    settings: Optional[ClickPipePostgresPipeSettings] = UNSET
    table_mappings: Optional[list[ClickPipePostgresPipeTableMapping]] = Field(default=UNSET, alias="tableMappings")
    """List of table mappings defining which PostgreSQL tables to replicate and how they map to ClickHouse tables."""


class ClickPipePostgresSourceDict(TypedDict):
    type_: NotRequired[Type7OrStr | None]
    host: NotRequired[str]
    port: NotRequired[int]
    database: NotRequired[str]
    authentication: NotRequired[Authentication11OrStr]
    iam_role: NotRequired[str]
    tls_host: NotRequired[str]
    ca_certificate: NotRequired[str]
    disable_tls: NotRequired[bool]
    skip_cert_verification: NotRequired[bool]
    settings: NotRequired[ClickPipePostgresPipeSettingsDict]
    table_mappings: NotRequired[list[ClickPipePostgresPipeTableMappingDict]]
