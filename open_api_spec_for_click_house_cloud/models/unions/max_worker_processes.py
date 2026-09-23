from __future__ import annotations

from typing import TypeAlias

MaxWorkerProcesses: TypeAlias = str | int
"""Maximum number of background processes the system can support. Includes parallel query workers, logical replication,
and more."""

MaxWorkerProcessesDict: TypeAlias = str | int
