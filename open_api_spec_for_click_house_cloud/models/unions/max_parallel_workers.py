from __future__ import annotations

from typing import TypeAlias

MaxParallelWorkers: TypeAlias = str | int
"""Maximum number of workers that can be used for parallel operations. Cannot exceed max_worker_processes."""

MaxParallelWorkersDict: TypeAlias = str | int
