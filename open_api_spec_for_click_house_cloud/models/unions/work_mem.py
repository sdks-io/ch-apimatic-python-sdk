from __future__ import annotations

from typing import TypeAlias

WorkMem: TypeAlias = str | int
"""Sets the amount of memory Postgres will use for internal operations like sorting and hashing as part of executing a
query."""

WorkMemDict: TypeAlias = str | int
