from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UseTextIndexForImplicitColumn(str, Enum):
    """Controls whether lucene rendering uses ClickHouse text indices via hasAllTokens() against the implicit column.
    "auto" detects a covering index at query time, "enabled" forces text index usage, "disabled" forces a LIKE/hasToken
    fallback."""

    AUTO = "auto"
    ENABLED = "enabled"
    DISABLED = "disabled"

    __str__ = str.__str__


UseTextIndexForImplicitColumnOrStr: TypeAlias = Annotated[
    UseTextIndexForImplicitColumn | str, open_enum_validator(UseTextIndexForImplicitColumn)
]
