from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_on_click_filter_template import ClickStackOnClickFilterTemplate, ClickStackOnClickFilterTemplateDict
from .enums.where_language5 import WhereLanguage5OrStr
from .unions.click_stack_on_click_target import ClickStackOnClickTarget, ClickStackOnClickTargetDict


class ClickStackOnClickDashboard(SdkBaseModel):
    type_: Literal["dashboard"] = Field(default="dashboard", alias="type")
    """OnClick variant discriminator. Must be "dashboard" for dashboard link-outs."""

    target: ClickStackOnClickTarget
    where_template: Optional[str] = Field(default=UNSET, alias="whereTemplate")
    """Optional WHERE clause template applied to the destination dashboard."""

    where_language: Optional[WhereLanguage5OrStr] = Field(default=UNSET, alias="whereLanguage")
    """Language of the rendered whereTemplate."""

    filters: Optional[list[ClickStackOnClickFilterTemplate]] = UNSET
    """Optional dashboard filter templates rendered against the clicked row."""


class ClickStackOnClickDashboardDict(TypedDict):
    type_: Literal["dashboard"]
    target: ClickStackOnClickTargetDict
    where_template: NotRequired[str]
    where_language: NotRequired[WhereLanguage5OrStr]
    filters: NotRequired[list[ClickStackOnClickFilterTemplateDict]]
