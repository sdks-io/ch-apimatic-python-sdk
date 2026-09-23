from __future__ import annotations

from typing import TypeAlias

MaxWalSize: TypeAlias = str | int
"""Maximum size WAL can grow between checkpoints. Larger values improve write performance but increase crash recovery
time."""

MaxWalSizeDict: TypeAlias = str | int
