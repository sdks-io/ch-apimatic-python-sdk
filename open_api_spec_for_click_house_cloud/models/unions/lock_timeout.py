from __future__ import annotations

from typing import TypeAlias

LockTimeout: TypeAlias = str | int
"""Abort any statement that waits longer than the specified time while attempting to acquire a lock. Use 0 to
disable."""

LockTimeoutDict: TypeAlias = str | int
