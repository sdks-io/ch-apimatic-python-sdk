from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_pipe_mongo_dbpipe_table_mapping import (
    ClickPipeMongoDbpipeTableMapping,
    ClickPipeMongoDbpipeTableMappingDict,
)
from .click_pipe_patch_mongo_dbpipe_remove_table_mapping import (
    ClickPipePatchMongoDbpipeRemoveTableMapping,
    ClickPipePatchMongoDbpipeRemoveTableMappingDict,
)
from .click_pipe_patch_mongo_dbpipe_settings import (
    ClickPipePatchMongoDbpipeSettings,
    ClickPipePatchMongoDbpipeSettingsDict,
)
from .enums.read_preference import ReadPreferenceOrStr
from .plain import Plain, PlainDict


class ClickPipePatchMongoDbsource(SdkBaseModel):
    credentials: Optional[Plain] = UNSET
    uri: str | None
    """MongoDB connection URI (mongodb:// or mongodb+srv://). Credentials are redacted in responses; a masked value is
    never saved as a credential, so a real credential equal to [REDACTED] cannot be set. To change the connection, send
    the full URI with real credentials; omit this field or resend the redacted value to leave it unchanged."""

    read_preference: ReadPreferenceOrStr | None = Field(alias="readPreference")
    """MongoDB read preference for replica set reads."""

    tls_host: OptionalNullable[str] = Field(default=UNSET, alias="tlsHost")
    """TLS/SSL host for secure connections."""

    disable_tls: OptionalNullable[bool] = Field(default=UNSET, alias="disableTls")
    """Disable TLS for the MongoDB connection. Defaults to false (TLS enabled)."""

    skip_cert_verification: OptionalNullable[bool] = Field(default=UNSET, alias="skipCertVerification")
    """Skip TLS certificate verification for the MongoDB connection. Use with caution in production environments."""

    ca_certificate: OptionalNullable[str] = Field(default=UNSET, alias="caCertificate")
    """PEM encoded CA certificate to validate the MongoDB server certificate."""

    settings: Optional[ClickPipePatchMongoDbpipeSettings] = UNSET
    table_mappings_to_add: Optional[list[ClickPipeMongoDbpipeTableMapping]] = Field(
        default=UNSET, alias="tableMappingsToAdd"
    )
    """Collection mappings to add to the pipe. Can be an empty array if no collections are being added."""

    table_mappings_to_remove: Optional[list[ClickPipePatchMongoDbpipeRemoveTableMapping]] = Field(
        default=UNSET, alias="tableMappingsToRemove"
    )
    """Collection mappings to remove from the pipe. Only sourceDatabaseName, sourceCollection, and targetTable are
    required for removal."""


class ClickPipePatchMongoDbsourceDict(TypedDict):
    credentials: NotRequired[PlainDict]
    uri: str | None
    read_preference: ReadPreferenceOrStr | None
    tls_host: NotRequired[str | None]
    disable_tls: NotRequired[bool | None]
    skip_cert_verification: NotRequired[bool | None]
    ca_certificate: NotRequired[str | None]
    settings: NotRequired[ClickPipePatchMongoDbpipeSettingsDict]
    table_mappings_to_add: NotRequired[list[ClickPipeMongoDbpipeTableMappingDict]]
    table_mappings_to_remove: NotRequired[list[ClickPipePatchMongoDbpipeRemoveTableMappingDict]]
