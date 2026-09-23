from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.type21 import Type21OrStr


class CreditBalance(SdkBaseModel):
    id: Optional[UUID] = UNSET
    """Unique ID of the balance."""

    type_: Optional[Type21OrStr] = Field(default=UNSET, alias="type")
    """Type of the balance."""

    remaining_credits: Optional[float] = Field(default=UNSET, alias="remainingCredits")
    """Remaining credits available on this balance, in ClickHouse Credits (CHCs)."""

    total_amount: Optional[float] = Field(default=UNSET, alias="totalAmount")
    """Total credits granted on this balance, in ClickHouse Credits (CHCs)."""

    amount_spent: Optional[float] = Field(default=UNSET, alias="amountSpent")
    """Credits spent from this balance, in ClickHouse Credits (CHCs)."""

    start_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="startDate")
    """Date the balance became active. ISO-8601, based on the UTC timezone."""

    expiration_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expirationDate")
    """Date the balance expires. ISO-8601, based on the UTC timezone."""


class CreditBalanceDict(TypedDict):
    id: NotRequired[UUID]
    type_: NotRequired[Type21OrStr]
    remaining_credits: NotRequired[float]
    total_amount: NotRequired[float]
    amount_spent: NotRequired[float]
    start_date: NotRequired[RFC3339DateTime]
    expiration_date: NotRequired[RFC3339DateTime]
