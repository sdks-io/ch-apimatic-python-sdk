from __future__ import annotations

from typing import TypeAlias

WalSenderTimeout: TypeAlias = str | int
"""Terminate replication connections that are inactive for longer than this time. Use 0 to disable."""

WalSenderTimeoutDict: TypeAlias = str | int
