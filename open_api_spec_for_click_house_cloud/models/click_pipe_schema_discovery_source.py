from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .click_pipe_post_kafka_source import ClickPipePostKafkaSource, ClickPipePostKafkaSourceDict
from .click_pipe_post_kinesis_source import ClickPipePostKinesisSource, ClickPipePostKinesisSourceDict
from .click_pipe_post_object_storage_source import (
    ClickPipePostObjectStorageSource,
    ClickPipePostObjectStorageSourceDict,
)


class ClickPipeSchemaDiscoverySource(SdkBaseModel):
    kafka: OptionalNullable[ClickPipePostKafkaSource] = UNSET
    kinesis: OptionalNullable[ClickPipePostKinesisSource] = UNSET
    pubsub: OptionalNullable[Any] = UNSET
    object_storage: OptionalNullable[ClickPipePostObjectStorageSource] = Field(default=UNSET, alias="objectStorage")


class ClickPipeSchemaDiscoverySourceDict(TypedDict):
    kafka: NotRequired[ClickPipePostKafkaSourceDict | None]
    kinesis: NotRequired[ClickPipePostKinesisSourceDict | None]
    pubsub: NotRequired[Any | None]
    object_storage: NotRequired[ClickPipePostObjectStorageSourceDict | None]
