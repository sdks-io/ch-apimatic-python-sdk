from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PgHaType(str, Enum):
    """Type of high availability: “none” for no replication, “async” for asynchronous replication to a single standby,
    and “sync” for synchronous replication to two standbys."""

    NONE = "none"
    ASYNC = "async"
    SYNC = "sync"

    __str__ = str.__str__


PgHaTypeOrStr: TypeAlias = Annotated[PgHaType | str, open_enum_validator(PgHaType)]
