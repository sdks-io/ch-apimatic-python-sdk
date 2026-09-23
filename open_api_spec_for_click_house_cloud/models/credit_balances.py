from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .credit_balance import CreditBalance, CreditBalanceDict


class CreditBalances(SdkBaseModel):
    total_remaining_credits: Optional[float] = Field(default=UNSET, alias="totalRemainingCredits")
    """Total remaining credits across all active balances, in ClickHouse Credits (CHCs)."""

    balances: Optional[list[CreditBalance]] = UNSET
    """List of active balances for the organization. Empty when the organization has none."""


class CreditBalancesDict(TypedDict):
    total_remaining_credits: NotRequired[float]
    balances: NotRequired[list[CreditBalanceDict]]
