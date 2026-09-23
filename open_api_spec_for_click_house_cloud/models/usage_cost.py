from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .usage_cost_record import UsageCostRecord, UsageCostRecordDict


class UsageCost(SdkBaseModel):
    grand_total_chc: Optional[float] = Field(default=UNSET, alias="grandTotalCHC")
    """Grand total cost of usage in ClickHouse Credits (CHCs)."""

    costs: Optional[list[UsageCostRecord]] = UNSET
    """List of daily, per-entity usage cost records."""


class UsageCostDict(TypedDict):
    grand_total_chc: NotRequired[float]
    costs: NotRequired[list[UsageCostRecordDict]]
