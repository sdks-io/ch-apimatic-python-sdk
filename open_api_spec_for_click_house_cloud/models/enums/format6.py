from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Format6(str, Enum):
    """Format of messages in the Pub/Sub topic. GCP Pub/Sub ClickPipes are in limited preview — contact support to
    enable this feature for your organization."""

    JSON_EACH_ROW = "JSONEachRow"
    AVRO = "Avro"
    PROTOBUF = "Protobuf"

    __str__ = str.__str__


Format6OrStr: TypeAlias = Annotated[Format6 | str, open_enum_validator(Format6)]
