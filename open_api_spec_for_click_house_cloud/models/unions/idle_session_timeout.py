from __future__ import annotations

from typing import TypeAlias

IdleSessionTimeout: TypeAlias = str | int
"""Terminate any session that has been idle for longer than the specified time. Use 0 to disable."""

IdleSessionTimeoutDict: TypeAlias = str | int
