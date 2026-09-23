from __future__ import annotations

from typing import TypeAlias

AutovacuumAnalyzeScaleFactor: TypeAlias = str | float
"""Fraction of a table's rows that must change before autovacuum runs ANALYZE to refresh planner statistics."""

AutovacuumAnalyzeScaleFactorDict: TypeAlias = str | float
