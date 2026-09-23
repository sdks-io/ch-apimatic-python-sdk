from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PostgresServiceState(str, Enum):
    """Current state of the service"""

    CREATING = "creating"
    RESTARTING = "restarting"
    RUNNING = "running"
    REPLAYING_WAL = "replaying_wal"
    RESTORING_BACKUP = "restoring_backup"
    FINALIZING_RESTORE = "finalizing_restore"
    UNAVAILABLE = "unavailable"
    STOPPED = "stopped"
    DELETING = "deleting"

    __str__ = str.__str__


PostgresServiceStateOrStr: TypeAlias = Annotated[PostgresServiceState | str, open_enum_validator(PostgresServiceState)]
