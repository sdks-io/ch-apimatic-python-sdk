from __future__ import annotations

from typing import TypeAlias

AutovacuumVacuumCostDelay: TypeAlias = str | int
"""Time autovacuum sleeps when the cost limit is reached. Lower values speed up vacuuming at the cost of more I/O."""

AutovacuumVacuumCostDelayDict: TypeAlias = str | int
