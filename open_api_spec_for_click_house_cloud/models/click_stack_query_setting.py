from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClickStackQuerySetting(SdkBaseModel):
    setting: str
    """ClickHouse setting name"""

    value: str
    """Setting value"""


class ClickStackQuerySettingDict(TypedDict):
    setting: str
    value: str
