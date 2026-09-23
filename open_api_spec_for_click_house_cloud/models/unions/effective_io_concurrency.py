from __future__ import annotations

from typing import TypeAlias

EffectiveIoConcurrency: TypeAlias = str | int
"""Number of concurrent disk I/O operations the planner expects. Higher values (100-200) benefit SSDs."""

EffectiveIoConcurrencyDict: TypeAlias = str | int
