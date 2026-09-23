from __future__ import annotations

from typing import TypeAlias

MinWalSize: TypeAlias = str | int
"""Minimum size to shrink the WAL to. WAL files are recycled rather than removed when below this size."""

MinWalSizeDict: TypeAlias = str | int
