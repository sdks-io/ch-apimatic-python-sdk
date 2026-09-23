from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ClickStackHighlightedAttributeExpression(SdkBaseModel):
    sql_expression: str = Field(alias="sqlExpression")
    """SQL expression for the attribute"""

    lucene_expression: OptionalNullable[str] = Field(default=UNSET, alias="luceneExpression")
    """An optional, Lucene version of the sqlExpression expression. If provided, it is used when searching for this
    attribute value."""

    alias: OptionalNullable[str] = UNSET
    """Optional alias for the attribute"""


class ClickStackHighlightedAttributeExpressionDict(TypedDict):
    sql_expression: str
    lucene_expression: NotRequired[str | None]
    alias: NotRequired[str | None]
