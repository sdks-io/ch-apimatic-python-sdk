from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.strategy import StrategyOrStr


class ClickPipeKafkaOffset(SdkBaseModel):
    strategy: Optional[StrategyOrStr] = UNSET
    """Offset strategy."""

    timestamp: OptionalNullable[str] = UNSET
    """A minute precision UTC timestamp to start from. Required for "from_timestamp" strategy."""


class ClickPipeKafkaOffsetDict(TypedDict):
    strategy: NotRequired[StrategyOrStr]
    timestamp: NotRequired[str | None]
