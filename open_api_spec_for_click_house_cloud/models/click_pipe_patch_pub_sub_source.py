from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.authentication17 import Authentication17OrStr
from .service_account import ServiceAccount, ServiceAccountDict


class ClickPipePatchPubSubSource(SdkBaseModel):
    authentication: Authentication17OrStr | None
    """Authentication method to use with GCP Pub/Sub. SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview.
    ClickPipes uses the GCP service account returned in gcpWorkloadIdentity.principal by the operation with operationId
    clickPipesServiceContextGet; grant it access to the source resources."""

    ack_deadline: OptionalNullable[int] = Field(default=UNSET, alias="ackDeadline")
    """Acknowledgement deadline for messages, in seconds. Must be between 10 and 600."""

    service_account_key: OptionalNullable[ServiceAccount] = Field(default=UNSET, alias="serviceAccountKey")


class ClickPipePatchPubSubSourceDict(TypedDict):
    authentication: Authentication17OrStr | None
    ack_deadline: NotRequired[int | None]
    service_account_key: NotRequired[ServiceAccountDict | None]
