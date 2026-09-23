from __future__ import annotations

from typing import TypeAlias

MaxParallelMaintenanceWorkers: TypeAlias = str | int
"""Maximum number of parallel workers for maintenance operations like CREATE INDEX and VACUUM."""

MaxParallelMaintenanceWorkersDict: TypeAlias = str | int
