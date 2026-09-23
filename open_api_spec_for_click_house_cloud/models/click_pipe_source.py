from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .click_pipe_kafka_source import ClickPipeKafkaSource, ClickPipeKafkaSourceDict
from .click_pipe_kinesis_source import ClickPipeKinesisSource, ClickPipeKinesisSourceDict
from .click_pipe_mongo_dbsource import ClickPipeMongoDbsource, ClickPipeMongoDbsourceDict
from .click_pipe_my_sqlsource import ClickPipeMySqlsource, ClickPipeMySqlsourceDict
from .click_pipe_object_storage_source import ClickPipeObjectStorageSource, ClickPipeObjectStorageSourceDict
from .click_pipe_postgres_source import ClickPipePostgresSource, ClickPipePostgresSourceDict
from .click_pipe_pub_sub_source import ClickPipePubSubSource, ClickPipePubSubSourceDict


class ClickPipeSource(SdkBaseModel):
    kafka: OptionalNullable[ClickPipeKafkaSource] = UNSET
    object_storage: OptionalNullable[ClickPipeObjectStorageSource] = Field(default=UNSET, alias="objectStorage")
    kinesis: OptionalNullable[ClickPipeKinesisSource] = UNSET
    pubsub: OptionalNullable[ClickPipePubSubSource] = UNSET
    postgres: OptionalNullable[ClickPipePostgresSource] = UNSET
    mysql: OptionalNullable[ClickPipeMySqlsource] = UNSET
    bigquery: OptionalNullable[Any] = UNSET
    mongodb: OptionalNullable[ClickPipeMongoDbsource] = UNSET


class ClickPipeSourceDict(TypedDict):
    kafka: NotRequired[ClickPipeKafkaSourceDict | None]
    object_storage: NotRequired[ClickPipeObjectStorageSourceDict | None]
    kinesis: NotRequired[ClickPipeKinesisSourceDict | None]
    pubsub: NotRequired[ClickPipePubSubSourceDict | None]
    postgres: NotRequired[ClickPipePostgresSourceDict | None]
    mysql: NotRequired[ClickPipeMySqlsourceDict | None]
    bigquery: NotRequired[Any | None]
    mongodb: NotRequired[ClickPipeMongoDbsourceDict | None]
