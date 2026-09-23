from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class PostgresLogEntry(SdkBaseModel):
    timestamp: RFC3339DateTime
    """Time the entry was logged (RFC 3339)."""

    severity: str
    """PostgreSQL severity of the entry (for example, LOG, WARNING, ERROR, FATAL, PANIC)."""

    body: str
    """Raw log entry body as emitted by PostgreSQL. Structured bodies are returned as a JSON-encoded string."""


class PostgresLogEntryDict(TypedDict):
    timestamp: RFC3339DateTime
    severity: str
    body: str
