from __future__ import annotations

from typing import TypeAlias

IdleInTransactionSessionTimeout: TypeAlias = str | int
"""Terminate any session that has been idle within an open transaction for longer than the specified time. Use 0 to
disable."""

IdleInTransactionSessionTimeoutDict: TypeAlias = str | int
