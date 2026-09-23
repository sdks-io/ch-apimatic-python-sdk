from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReplicationMechanism(str, Enum):
    """MySQL replication mechanism: "GTID" (Global Transaction Identifier) or "FILE_POS" (binary log file and position).
    Defaults to "GTID" if not specified. MariaDB supports "GTID" only. For "FILE_POS" on MySQL, contact support."""

    GTID = "GTID"
    FILE_POS = "FILE_POS"

    __str__ = str.__str__


ReplicationMechanismOrStr: TypeAlias = Annotated[ReplicationMechanism | str, open_enum_validator(ReplicationMechanism)]
