from __future__ import annotations

from typing import TypeAlias

RandomPageCost: TypeAlias = str | float
"""Sets the planner's estimate of the cost of a non-sequentially-fetched disk page. Lower values (1.1-1.5) are better
for SSDs."""

RandomPageCostDict: TypeAlias = str | float
