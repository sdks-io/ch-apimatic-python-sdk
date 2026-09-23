from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type3(str, Enum):
    """Type of the Kafka source."""

    KAFKA = "kafka"
    REDPANDA = "redpanda"
    MSK = "msk"
    GCMK = "gcmk"
    CONFLUENT = "confluent"
    WARPSTREAM = "warpstream"
    AZUREEVENTHUB = "azureeventhub"
    DOKAFKA = "dokafka"

    __str__ = str.__str__


Type3OrStr: TypeAlias = Annotated[Type3 | str, open_enum_validator(Type3)]
