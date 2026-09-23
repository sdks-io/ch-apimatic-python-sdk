from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .active_balance import ActiveBalance, ActiveBalanceDict


class ActiveBalances(SdkBaseModel):
    total_remaining_prepaid_credits: Optional[float] = Field(default=UNSET, alias="totalRemainingPrepaidCredits")
    """Total remaining credits across all active prepaid balances, in ClickHouse Credits (CHCs)."""

    prepaid_balances: Optional[list[ActiveBalance]] = Field(default=UNSET, alias="prepaidBalances")
    """List of active prepaid balances for the organization."""


class ActiveBalancesDict(TypedDict):
    total_remaining_prepaid_credits: NotRequired[float]
    prepaid_balances: NotRequired[list[ActiveBalanceDict]]
