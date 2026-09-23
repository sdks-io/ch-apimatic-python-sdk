from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.path import Path, PathDict


class Issue(SdkBaseModel):
    path: list[Path]
    """Path to the invalid field."""

    code: str
    """Validation issue code."""

    message: str
    """Human-readable description of the issue."""


class IssueDict(TypedDict):
    path: list[PathDict]
    code: str
    message: str
