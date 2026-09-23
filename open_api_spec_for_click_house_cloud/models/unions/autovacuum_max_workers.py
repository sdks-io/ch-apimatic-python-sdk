from __future__ import annotations

from typing import TypeAlias

AutovacuumMaxWorkers: TypeAlias = str | int
"""Maximum number of autovacuum worker processes that can run at the same time. Workers share a single cost-limit
budget, so raising this alone may not speed up vacuuming."""

AutovacuumMaxWorkersDict: TypeAlias = str | int
