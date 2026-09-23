from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PostgresServicePasswordResource(SdkBaseModel):
    password: Optional[str] = UNSET
    """New Postgres superuser password. Provided only if there was no 'password' in the request."""


class PostgresServicePasswordResourceDict(TypedDict):
    password: NotRequired[str]
