from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_pipe_mutate_mongo_dbsource import ClickPipeMutateMongoDbsource, ClickPipeMutateMongoDbsourceDict
from .click_pipe_mutate_my_sqlsource import ClickPipeMutateMySqlsource, ClickPipeMutateMySqlsourceDict
from .click_pipe_mutate_postgres_source import ClickPipeMutatePostgresSource, ClickPipeMutatePostgresSourceDict
from .click_pipe_post_kafka_source import ClickPipePostKafkaSource, ClickPipePostKafkaSourceDict
from .click_pipe_post_kinesis_source import ClickPipePostKinesisSource, ClickPipePostKinesisSourceDict
from .click_pipe_post_object_storage_source import (
    ClickPipePostObjectStorageSource,
    ClickPipePostObjectStorageSourceDict,
)


class ClickPipePostSource(SdkBaseModel):
    kafka: OptionalNullable[ClickPipePostKafkaSource] = UNSET
    object_storage: OptionalNullable[ClickPipePostObjectStorageSource] = Field(default=UNSET, alias="objectStorage")
    kinesis: OptionalNullable[ClickPipePostKinesisSource] = UNSET
    pubsub: OptionalNullable[Any] = UNSET
    postgres: Optional[ClickPipeMutatePostgresSource] = UNSET
    mysql: OptionalNullable[ClickPipeMutateMySqlsource] = UNSET
    bigquery: OptionalNullable[Any] = UNSET
    mongodb: OptionalNullable[ClickPipeMutateMongoDbsource] = UNSET
    validate_samples: Optional[bool] = Field(default=UNSET, alias="validateSamples")
    """Validate data samples received from data source. It will validate the connection and data availability and
    correctness. If not enabled, only connection will be validated. This has no effect on Postgres or MySQL pipes, they
    always only validate the connection and table definitions. This is experimental and can be removed in the future."""


class ClickPipePostSourceDict(TypedDict):
    kafka: NotRequired[ClickPipePostKafkaSourceDict | None]
    object_storage: NotRequired[ClickPipePostObjectStorageSourceDict | None]
    kinesis: NotRequired[ClickPipePostKinesisSourceDict | None]
    pubsub: NotRequired[Any | None]
    postgres: NotRequired[ClickPipeMutatePostgresSourceDict]
    mysql: NotRequired[ClickPipeMutateMySqlsourceDict | None]
    bigquery: NotRequired[Any | None]
    mongodb: NotRequired[ClickPipeMutateMongoDbsourceDict | None]
    validate_samples: NotRequired[bool]
