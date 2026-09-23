from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_pipe_my_sqlpipe_settings import ClickPipeMySqlpipeSettings, ClickPipeMySqlpipeSettingsDict
from .click_pipe_my_sqlpipe_table_mapping import ClickPipeMySqlpipeTableMapping, ClickPipeMySqlpipeTableMappingDict
from .enums.authentication13 import Authentication13OrStr
from .enums.type9 import Type9OrStr


class ClickPipeMySqlsource(SdkBaseModel):
    type_: OptionalNullable[Type9OrStr] = Field(default=UNSET, alias="type")
    """Type of the MySQL source. Defaults to "mysql" if not specified."""

    host: str
    """MySQL server hostname or IP address. To use a reverse private endpoint, pass the endpoint hostname here."""

    port: int
    """MySQL server port."""

    authentication: Optional[Authentication13OrStr] = UNSET
    """Authentication method for MySQL connection."""

    iam_role: Optional[str] = Field(default=UNSET, alias="iamRole")
    """IAM role ARN for IAM authentication (required for IAM_ROLE authentication)."""

    tls_host: Optional[str] = Field(default=UNSET, alias="tlsHost")
    """TLS/SSL host for secure connections."""

    ca_certificate: Optional[str] = Field(default=UNSET, alias="caCertificate")
    """PEM encoded CA certificate to validate the MySQL server certificate."""

    disable_tls: Optional[bool] = Field(default=UNSET, alias="disableTls")
    """Disable TLS for the MySQL connection. Use with caution in production environments."""

    skip_cert_verification: Optional[bool] = Field(default=UNSET, alias="skipCertVerification")
    """Skip TLS certificate verification for the MySQL connection. Use with caution in production environments."""

    server_id: Optional[int] = Field(default=UNSET, alias="serverId")
    """Optional MySQL server_id the pipe declares itself as in the MySQL replication topology. Must be unique across
    replicas connected to the source. If omitted, one is assigned automatically."""

    settings: ClickPipeMySqlpipeSettings
    table_mappings: list[ClickPipeMySqlpipeTableMapping] = Field(alias="tableMappings")
    """List of table mappings defining which MySQL tables to replicate and how they map to ClickHouse tables."""


class ClickPipeMySqlsourceDict(TypedDict):
    type_: NotRequired[Type9OrStr | None]
    host: str
    port: int
    authentication: NotRequired[Authentication13OrStr]
    iam_role: NotRequired[str]
    tls_host: NotRequired[str]
    ca_certificate: NotRequired[str]
    disable_tls: NotRequired[bool]
    skip_cert_verification: NotRequired[bool]
    server_id: NotRequired[int]
    settings: ClickPipeMySqlpipeSettingsDict
    table_mappings: list[ClickPipeMySqlpipeTableMappingDict]
