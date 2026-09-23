from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Format2(str, Enum):
    """Format of the Kinesis stream."""

    JSON_EACH_ROW = "JSONEachRow"
    AVRO = "Avro"
    AVRO_CONFLUENT = "AvroConfluent"
    PROTOBUF = "Protobuf"

    __str__ = str.__str__


Format2OrStr: TypeAlias = Annotated[Format2 | str, open_enum_validator(Format2)]
