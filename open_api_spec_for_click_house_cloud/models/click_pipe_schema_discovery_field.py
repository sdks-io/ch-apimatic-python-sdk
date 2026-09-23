from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ClickPipeSchemaDiscoveryField(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the inferred field."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Inferred ClickHouse data type of the field."""

    optional: OptionalNullable[bool] = UNSET
    """Whether the field is optional (nullable) in the source."""


class ClickPipeSchemaDiscoveryFieldDict(TypedDict):
    name: NotRequired[str]
    type_: NotRequired[str]
    optional: NotRequired[bool | None]
