from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReleaseChannel(str, Enum):
    """Select fast if you want to get new ClickHouse releases as soon as they are available. You'll get new features
    faster, but with a higher risk of bugs. Select slow if you would like to defer releases to give yourself more time
    to test. This feature is only available for production services. default is the regular release channel."""

    SLOW = "slow"
    DEFAULT = "default"
    FAST = "fast"

    __str__ = str.__str__


ReleaseChannelOrStr: TypeAlias = Annotated[ReleaseChannel | str, open_enum_validator(ReleaseChannel)]
