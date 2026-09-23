from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ClickStackFilterSettingsColumn(SdkBaseModel):
    name: str
    """Column of the source's table that selected filter values are matched against. Also the key the selection is
    persisted under in links, saved searches, and dashboards."""

    label: str
    """Display label for the column"""

    value_expression: OptionalNullable[str] = Field(default=UNSET, alias="valueExpression")
    """Optional SQL expression, evaluated against the filter-values table, that produces the available filter options.
    Use it when the options live in a differently-named column, or must be transformed to match the values stored in the
    source table. Defaults to reading ``name`` as a plain column when omitted."""

    allow_all: Optional[bool] = Field(default=UNSET, alias="allowAll")
    """Whether to offer an "All" option that expands to every available value at query time. Best suited to
    low-cardinality columns. Defaults to false."""


class ClickStackFilterSettingsColumnDict(TypedDict):
    name: str
    label: str
    value_expression: NotRequired[str | None]
    allow_all: NotRequired[bool]
