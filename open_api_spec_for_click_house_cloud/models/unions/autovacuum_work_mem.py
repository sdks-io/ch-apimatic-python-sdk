from __future__ import annotations

from typing import TypeAlias

AutovacuumWorkMem: TypeAlias = str | int
"""Maximum memory each autovacuum worker uses to track dead tuples. Higher values reduce repeated index-vacuum passes on
large tables. Use -1 to fall back to maintenance_work_mem."""

AutovacuumWorkMemDict: TypeAlias = str | int
