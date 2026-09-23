from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.authentication2 import Authentication2OrStr
from .unions.credentials import Credentials, CredentialsDict


class ClickPipePatchKafkaSource(SdkBaseModel):
    authentication: OptionalNullable[Authentication2OrStr] = UNSET
    """Authentication method of the Kafka source. SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes
    uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with operationId
    clickPipesServiceContextGet; grant it access to the source resources. Supported authentication methods: kafka:
    PLAIN, SCRAM-SHA-256, SCRAM-SHA-512, MUTUAL_TLS, msk: SCRAM-SHA-512, IAM_ROLE, IAM_USER, MUTUAL_TLS, gcmk: PLAIN,
    MUTUAL_TLS, SERVICE_ACCOUNT_WORKLOAD_IDENTITY, confluent: PLAIN, MUTUAL_TLS, warpstream: PLAIN, azureeventhub:
    PLAIN, redpanda: SCRAM-SHA-256, SCRAM-SHA-512, MUTUAL_TLS, dokafka: SCRAM-SHA-256, MUTUAL_TLS"""

    iam_role: OptionalNullable[str] = Field(default=UNSET, alias="iamRole")
    """IAM role for the Kafka source. Use with IAM role authentication. Read more in ClickPipes documentation:
    https://clickhouse.com/docs/en/integrations/clickpipes/kafka#iam"""

    ca_certificate: OptionalNullable[str] = Field(default=UNSET, alias="caCertificate")
    """PEM encoded CA certificates to validate the broker's certificate."""

    reverse_private_endpoint_ids: Optional[list[str]] = Field(default=UNSET, alias="reversePrivateEndpointIds")
    """Reverse private endpoint UUIDs used for a secure private connection to the Kafka source."""

    credentials: Optional[Credentials] = UNSET
    """Credentials for Kafka source. Choose one that is supported by the authentication method."""


class ClickPipePatchKafkaSourceDict(TypedDict):
    authentication: NotRequired[Authentication2OrStr | None]
    iam_role: NotRequired[str | None]
    ca_certificate: NotRequired[str | None]
    reverse_private_endpoint_ids: NotRequired[list[str]]
    credentials: NotRequired[CredentialsDict]
