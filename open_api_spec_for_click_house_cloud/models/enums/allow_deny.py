from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AllowDeny(str, Enum):
    """Whether this policy allows or denies access"""

    ALLOW = "ALLOW"
    DENY = "DENY"

    __str__ = str.__str__


AllowDenyOrStr: TypeAlias = Annotated[AllowDeny | str, open_enum_validator(AllowDeny)]
