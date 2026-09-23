from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_pipe_kafka_offset import ClickPipeKafkaOffset, ClickPipeKafkaOffsetDict
from .click_pipe_kafka_schema_registry import ClickPipeKafkaSchemaRegistry, ClickPipeKafkaSchemaRegistryDict
from .enums.authentication2 import Authentication2OrStr
from .enums.format import FormatOrStr
from .enums.type3 import Type3OrStr


class ClickPipeKafkaSource(SdkBaseModel):
    type_: Optional[Type3OrStr] = Field(default=UNSET, alias="type")
    """Type of the Kafka source."""

    format: Optional[FormatOrStr] = UNSET
    """Format of the Kafka source."""

    brokers: Optional[str] = UNSET
    """Brokers of the Kafka source."""

    topics: Optional[str] = UNSET
    """Topics of the Kafka source."""

    consumer_group: OptionalNullable[str] = Field(default=UNSET, alias="consumerGroup")
    """Consumer group of the Kafka source. If not provided "clickpipes-<<ID>>" will be used."""

    authentication: Optional[Authentication2OrStr] = UNSET
    """Authentication method of the Kafka source. SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes
    uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with operationId
    clickPipesServiceContextGet; grant it access to the source resources. Supported authentication methods: kafka:
    PLAIN, SCRAM-SHA-256, SCRAM-SHA-512, MUTUAL_TLS, msk: SCRAM-SHA-512, IAM_ROLE, IAM_USER, MUTUAL_TLS, gcmk: PLAIN,
    MUTUAL_TLS, SERVICE_ACCOUNT_WORKLOAD_IDENTITY, confluent: PLAIN, MUTUAL_TLS, warpstream: PLAIN, azureeventhub:
    PLAIN, redpanda: SCRAM-SHA-256, SCRAM-SHA-512, MUTUAL_TLS, dokafka: SCRAM-SHA-256, MUTUAL_TLS"""

    iam_role: OptionalNullable[str] = Field(default=UNSET, alias="iamRole")
    """IAM role for the Kafka source. Use with IAM role authentication. Read more in ClickPipes documentation:
    https://clickhouse.com/docs/en/integrations/clickpipes/kafka#iam"""

    offset: OptionalNullable[ClickPipeKafkaOffset] = UNSET
    schema_registry: OptionalNullable[ClickPipeKafkaSchemaRegistry] = Field(default=UNSET, alias="schemaRegistry")
    ca_certificate: OptionalNullable[str] = Field(default=UNSET, alias="caCertificate")
    """PEM encoded CA certificates to validate the broker's certificate."""

    reverse_private_endpoint_ids: Optional[list[str]] = Field(default=UNSET, alias="reversePrivateEndpointIds")
    """Reverse private endpoint UUIDs used for a secure private connection to the Kafka source."""

    exactly_once: OptionalNullable[bool] = Field(default=UNSET, alias="exactlyOnce")
    """Enable exactly-once delivery. Guarantees every Kafka record is inserted exactly once across restarts and
    rebalances. Can only be set at pipe creation."""


class ClickPipeKafkaSourceDict(TypedDict):
    type_: NotRequired[Type3OrStr]
    format: NotRequired[FormatOrStr]
    brokers: NotRequired[str]
    topics: NotRequired[str]
    consumer_group: NotRequired[str | None]
    authentication: NotRequired[Authentication2OrStr]
    iam_role: NotRequired[str | None]
    offset: NotRequired[ClickPipeKafkaOffsetDict | None]
    schema_registry: NotRequired[ClickPipeKafkaSchemaRegistryDict | None]
    ca_certificate: NotRequired[str | None]
    reverse_private_endpoint_ids: NotRequired[list[str]]
    exactly_once: NotRequired[bool | None]
