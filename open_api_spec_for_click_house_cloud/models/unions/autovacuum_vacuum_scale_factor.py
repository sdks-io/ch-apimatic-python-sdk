from __future__ import annotations

from typing import TypeAlias

AutovacuumVacuumScaleFactor: TypeAlias = str | float
"""Fraction of a table's rows that must change before autovacuum runs. Lower values vacuum large tables more
frequently."""

AutovacuumVacuumScaleFactorDict: TypeAlias = str | float
