from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_pipe_mongo_dbpipe_settings import ClickPipeMongoDbpipeSettings, ClickPipeMongoDbpipeSettingsDict
from .click_pipe_mongo_dbpipe_table_mapping import (
    ClickPipeMongoDbpipeTableMapping,
    ClickPipeMongoDbpipeTableMappingDict,
)
from .enums.read_preference import ReadPreferenceOrStr
from .plain import Plain, PlainDict


class ClickPipeMutateMongoDbsource(SdkBaseModel):
    credentials: Optional[Plain] = UNSET
    uri: str
    """MongoDB connection URI. Supports both standard URIs (mongodb://...) and SRV URIs (mongodb+srv://...). Embedded
    credentials are redacted from API responses, so the returned value can differ from what was submitted."""

    read_preference: ReadPreferenceOrStr = Field(alias="readPreference")
    """MongoDB read preference for replica set reads."""

    tls_host: Optional[str] = Field(default=UNSET, alias="tlsHost")
    """TLS/SSL host for secure connections."""

    disable_tls: bool = Field(default=False, alias="disableTls")
    """Disable TLS for the MongoDB connection. Defaults to false (TLS enabled)."""

    skip_cert_verification: Optional[bool] = Field(default=UNSET, alias="skipCertVerification")
    """Skip TLS certificate verification for the MongoDB connection. Use with caution in production environments."""

    ca_certificate: Optional[str] = Field(default=UNSET, alias="caCertificate")
    """PEM encoded CA certificate to validate the MongoDB server certificate."""

    settings: ClickPipeMongoDbpipeSettings
    table_mappings: list[ClickPipeMongoDbpipeTableMapping] = Field(alias="tableMappings")
    """List of collection mappings defining which MongoDB collections to replicate and how they map to ClickHouse
    tables."""


class ClickPipeMutateMongoDbsourceDict(TypedDict):
    credentials: NotRequired[PlainDict]
    uri: str
    read_preference: ReadPreferenceOrStr
    tls_host: NotRequired[str]
    disable_tls: NotRequired[bool]
    skip_cert_verification: NotRequired[bool]
    ca_certificate: NotRequired[str]
    settings: ClickPipeMongoDbpipeSettingsDict
    table_mappings: list[ClickPipeMongoDbpipeTableMappingDict]
