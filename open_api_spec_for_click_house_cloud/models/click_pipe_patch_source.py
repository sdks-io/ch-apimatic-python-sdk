from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_pipe_patch_kafka_source import ClickPipePatchKafkaSource, ClickPipePatchKafkaSourceDict
from .click_pipe_patch_kinesis_source import ClickPipePatchKinesisSource, ClickPipePatchKinesisSourceDict
from .click_pipe_patch_mongo_dbsource import ClickPipePatchMongoDbsource, ClickPipePatchMongoDbsourceDict
from .click_pipe_patch_my_sqlsource import ClickPipePatchMySqlsource, ClickPipePatchMySqlsourceDict
from .click_pipe_patch_object_storage_source import (
    ClickPipePatchObjectStorageSource,
    ClickPipePatchObjectStorageSourceDict,
)
from .click_pipe_patch_postgres_source import ClickPipePatchPostgresSource, ClickPipePatchPostgresSourceDict
from .click_pipe_patch_pub_sub_source import ClickPipePatchPubSubSource, ClickPipePatchPubSubSourceDict


class ClickPipePatchSource(SdkBaseModel):
    kafka: OptionalNullable[ClickPipePatchKafkaSource] = UNSET
    object_storage: OptionalNullable[ClickPipePatchObjectStorageSource] = Field(default=UNSET, alias="objectStorage")
    kinesis: OptionalNullable[ClickPipePatchKinesisSource] = UNSET
    pubsub: OptionalNullable[ClickPipePatchPubSubSource] = UNSET
    postgres: Optional[ClickPipePatchPostgresSource] = UNSET
    mysql: OptionalNullable[ClickPipePatchMySqlsource] = UNSET
    mongodb: OptionalNullable[ClickPipePatchMongoDbsource] = UNSET
    validate_samples: Optional[bool] = Field(default=UNSET, alias="validateSamples")
    """Validate data samples received from data source. It will validate the connection and data availability and
    correctness. If not enabled, only connection will be validated. This has no effect on Postgres or MySQL pipes, they
    always only validate the connection and table definitions. This is experimental and can be removed in the future."""


class ClickPipePatchSourceDict(TypedDict):
    kafka: NotRequired[ClickPipePatchKafkaSourceDict | None]
    object_storage: NotRequired[ClickPipePatchObjectStorageSourceDict | None]
    kinesis: NotRequired[ClickPipePatchKinesisSourceDict | None]
    pubsub: NotRequired[ClickPipePatchPubSubSourceDict | None]
    postgres: NotRequired[ClickPipePatchPostgresSourceDict]
    mysql: NotRequired[ClickPipePatchMySqlsourceDict | None]
    mongodb: NotRequired[ClickPipePatchMongoDbsourceDict | None]
    validate_samples: NotRequired[bool]
