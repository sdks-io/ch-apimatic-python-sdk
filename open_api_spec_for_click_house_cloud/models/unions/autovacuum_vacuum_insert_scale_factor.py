from __future__ import annotations

from typing import TypeAlias

AutovacuumVacuumInsertScaleFactor: TypeAlias = str | float
"""Fraction of a table's rows that must be inserted before autovacuum runs. Helps vacuum insert-heavy, rarely-updated
tables."""

AutovacuumVacuumInsertScaleFactorDict: TypeAlias = str | float
