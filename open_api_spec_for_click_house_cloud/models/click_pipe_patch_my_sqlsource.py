from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_pipe_my_sqlpipe_table_mapping import ClickPipeMySqlpipeTableMapping, ClickPipeMySqlpipeTableMappingDict
from .click_pipe_patch_my_sqlpipe_remove_table_mapping import (
    ClickPipePatchMySqlpipeRemoveTableMapping,
    ClickPipePatchMySqlpipeRemoveTableMappingDict,
)
from .click_pipe_patch_my_sqlpipe_settings import ClickPipePatchMySqlpipeSettings, ClickPipePatchMySqlpipeSettingsDict
from .enums.authentication13 import Authentication13OrStr
from .plain import Plain, PlainDict


class ClickPipePatchMySqlsource(SdkBaseModel):
    credentials: Optional[Plain] = UNSET
    host: str | None
    """MySQL server hostname or IP address. To use a reverse private endpoint, pass the endpoint hostname here."""

    port: int | None
    """MySQL server port."""

    authentication: OptionalNullable[Authentication13OrStr] = UNSET
    """Authentication method for MySQL connection."""

    iam_role: OptionalNullable[str] = Field(default=UNSET, alias="iamRole")
    """IAM role ARN for IAM authentication (required for IAM_ROLE authentication)."""

    tls_host: OptionalNullable[str] = Field(default=UNSET, alias="tlsHost")
    """TLS/SSL host for secure connections."""

    ca_certificate: OptionalNullable[str] = Field(default=UNSET, alias="caCertificate")
    """PEM encoded CA certificate to validate the MySQL server certificate."""

    disable_tls: OptionalNullable[bool] = Field(default=UNSET, alias="disableTls")
    """Disable TLS for the MySQL connection. Use with caution in production environments."""

    skip_cert_verification: OptionalNullable[bool] = Field(default=UNSET, alias="skipCertVerification")
    """Skip TLS certificate verification for the MySQL connection. Use with caution in production environments."""

    server_id: OptionalNullable[int] = Field(default=UNSET, alias="serverId")
    """Optional MySQL server_id the pipe declares itself as in the MySQL replication topology. Must be unique across
    replicas connected to the source. If omitted, one is assigned automatically."""

    settings: Optional[ClickPipePatchMySqlpipeSettings] = UNSET
    table_mappings_to_add: Optional[list[ClickPipeMySqlpipeTableMapping]] = Field(
        default=UNSET, alias="tableMappingsToAdd"
    )
    """Table mappings to add to the pipe. Can be an empty array if no tables are being added."""

    table_mappings_to_remove: Optional[list[ClickPipePatchMySqlpipeRemoveTableMapping]] = Field(
        default=UNSET, alias="tableMappingsToRemove"
    )
    """Table mappings to remove from the pipe. Only sourceSchemaName, sourceTable, and targetTable are required for
    removal."""


class ClickPipePatchMySqlsourceDict(TypedDict):
    credentials: NotRequired[PlainDict]
    host: str | None
    port: int | None
    authentication: NotRequired[Authentication13OrStr | None]
    iam_role: NotRequired[str | None]
    tls_host: NotRequired[str | None]
    ca_certificate: NotRequired[str | None]
    disable_tls: NotRequired[bool | None]
    skip_cert_verification: NotRequired[bool | None]
    server_id: NotRequired[int | None]
    settings: NotRequired[ClickPipePatchMySqlpipeSettingsDict]
    table_mappings_to_add: NotRequired[list[ClickPipeMySqlpipeTableMappingDict]]
    table_mappings_to_remove: NotRequired[list[ClickPipePatchMySqlpipeRemoveTableMappingDict]]
