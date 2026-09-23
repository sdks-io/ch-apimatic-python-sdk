from __future__ import annotations

from typing import TypeAlias

AutovacuumNaptime: TypeAlias = str | int
"""Minimum delay between autovacuum runs. Lower values make autovacuum check for work more frequently."""

AutovacuumNaptimeDict: TypeAlias = str | int
