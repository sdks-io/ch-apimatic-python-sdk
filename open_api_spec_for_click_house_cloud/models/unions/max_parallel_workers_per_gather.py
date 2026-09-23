from __future__ import annotations

from typing import TypeAlias

MaxParallelWorkersPerGather: TypeAlias = str | int
"""Maximum number of parallel workers per executor node for parallel queries. Use 0 to disable parallel queries."""

MaxParallelWorkersPerGatherDict: TypeAlias = str | int
