from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Format(str, Enum):
    """Format of the Kafka source."""

    JSON_EACH_ROW = "JSONEachRow"
    AVRO = "Avro"
    AVRO_CONFLUENT = "AvroConfluent"
    PROTOBUF = "Protobuf"

    __str__ = str.__str__


FormatOrStr: TypeAlias = Annotated[Format | str, open_enum_validator(Format)]
