from __future__ import annotations

from typing import TypeAlias

StatementTimeout: TypeAlias = str | int
"""Abort any statement that runs longer than the specified time. Use 0 to disable."""

StatementTimeoutDict: TypeAlias = str | int
