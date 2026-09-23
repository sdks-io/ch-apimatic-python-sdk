from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ScimServiceProviderConfigBulk(SdkBaseModel):
    supported: bool
    """Whether bulk operations are supported."""

    max_operations: int = Field(alias="maxOperations")
    """Maximum number of bulk operations per request."""

    max_payload_size: int = Field(alias="maxPayloadSize")
    """Maximum payload size for bulk requests in bytes."""


class ScimServiceProviderConfigBulkDict(TypedDict):
    supported: bool
    max_operations: int
    max_payload_size: int
