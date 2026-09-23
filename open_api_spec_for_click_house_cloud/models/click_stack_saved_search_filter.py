from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type20 import Type20OrStr


class ClickStackSavedSearchFilter(SdkBaseModel):
    type_: Optional[Type20OrStr] = Field(default=UNSET, alias="type")
    """Always ``sql``. Only SQL predicate filters render in the sidebar."""

    condition: str
    """SQL predicate applied to the search, in ``<column> IN (...)`` form."""


class ClickStackSavedSearchFilterDict(TypedDict):
    type_: NotRequired[Type20OrStr]
    condition: str
