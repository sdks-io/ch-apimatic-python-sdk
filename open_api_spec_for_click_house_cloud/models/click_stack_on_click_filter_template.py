from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClickStackOnClickFilterTemplate(SdkBaseModel):
    kind: Literal["expressionTemplate"] = "expressionTemplate"
    """Filter template kind. Currently only "expressionTemplate" is supported."""

    expression: str
    """The column/expression to filter the destination by (e.g. "ServiceName")."""

    template: str
    """Value template rendered against the clicked row; supports row column variables in ``{{column}}`` form (e.g.
    ``{{ServiceName}}``)."""


class ClickStackOnClickFilterTemplateDict(TypedDict):
    kind: Literal["expressionTemplate"]
    expression: str
    template: str
