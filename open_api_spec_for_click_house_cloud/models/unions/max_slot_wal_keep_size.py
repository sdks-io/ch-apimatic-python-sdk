from __future__ import annotations

from typing import TypeAlias

MaxSlotWalKeepSize: TypeAlias = str | int
"""Specifies the maximum size of WAL files that replication slots are allowed to retain. Use -1 for unlimited."""

MaxSlotWalKeepSizeDict: TypeAlias = str | int
