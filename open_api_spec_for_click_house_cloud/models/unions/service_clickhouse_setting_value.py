from __future__ import annotations

from typing import TypeAlias

ServiceClickhouseSettingValue: TypeAlias = str | int
"""Setting value in its native JSON type. Use the settings schema endpoint for per-setting constraints."""

ServiceClickhouseSettingValueDict: TypeAlias = str | int
