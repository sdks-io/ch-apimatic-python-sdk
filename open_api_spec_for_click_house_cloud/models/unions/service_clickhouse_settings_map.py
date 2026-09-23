from __future__ import annotations

from typing import TypeAlias

ServiceClickhouseSettingsMap: TypeAlias = str | int
"""Setting value in its native JSON type. Use the settings schema endpoint for per-setting constraints."""

ServiceClickhouseSettingsMapDict: TypeAlias = str | int
