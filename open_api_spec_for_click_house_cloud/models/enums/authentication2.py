from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Authentication2(str, Enum):
    """Authentication method of the Kafka source. SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes
    uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with operationId
    clickPipesServiceContextGet; grant it access to the source resources. Supported authentication methods: kafka:
    PLAIN, SCRAM-SHA-256, SCRAM-SHA-512, MUTUAL_TLS, msk: SCRAM-SHA-512, IAM_ROLE, IAM_USER, MUTUAL_TLS, gcmk: PLAIN,
    MUTUAL_TLS, SERVICE_ACCOUNT_WORKLOAD_IDENTITY, confluent: PLAIN, MUTUAL_TLS, warpstream: PLAIN, azureeventhub:
    PLAIN, redpanda: SCRAM-SHA-256, SCRAM-SHA-512, MUTUAL_TLS, dokafka: SCRAM-SHA-256, MUTUAL_TLS"""

    PLAIN = "PLAIN"
    SCRAM_SHA_256 = "SCRAM-SHA-256"
    SCRAM_SHA_512 = "SCRAM-SHA-512"
    IAM_ROLE = "IAM_ROLE"
    IAM_USER = "IAM_USER"
    MUTUAL_TLS = "MUTUAL_TLS"
    SERVICE_ACCOUNT_WORKLOAD_IDENTITY = "SERVICE_ACCOUNT_WORKLOAD_IDENTITY"

    __str__ = str.__str__


Authentication2OrStr: TypeAlias = Annotated[Authentication2 | str, open_enum_validator(Authentication2)]
