from __future__ import annotations

from typing import TypeAlias

AutovacuumVacuumCostLimit: TypeAlias = str | int
"""Cost-accounting limit shared across all autovacuum workers before they pause. Use -1 to inherit vacuum_cost_limit."""

AutovacuumVacuumCostLimitDict: TypeAlias = str | int
