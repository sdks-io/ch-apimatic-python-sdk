from __future__ import annotations

from typing import TypeAlias

TransactionTimeout: TypeAlias = str | int
"""Terminate any statement that takes more than the specified time, even while active. Use 0 to disable."""

TransactionTimeoutDict: TypeAlias = str | int
