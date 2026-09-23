from __future__ import annotations

from typing import TypeAlias

WalKeepSize: TypeAlias = str | int
"""Minimum size of past WAL files kept in pg_wal for standby servers. Use 0 to disable."""

WalKeepSizeDict: TypeAlias = str | int
