from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.format6 import Format6OrStr
from .enums.seek_type import SeekTypeOrStr


class ClickPipePostPubSubWorkloadIdentitySource(SdkBaseModel):
    format: Format6OrStr
    """Format of messages in the Pub/Sub topic. GCP Pub/Sub ClickPipes are in limited preview — contact support to
    enable this feature for your organization."""

    project_id: str = Field(alias="projectId")
    """GCP project ID that owns the Pub/Sub topic."""

    topic: str
    """Pub/Sub topic name (not the fully-qualified path)."""

    authentication: Literal["SERVICE_ACCOUNT_WORKLOAD_IDENTITY"] = "SERVICE_ACCOUNT_WORKLOAD_IDENTITY"
    """SERVICE_ACCOUNT_WORKLOAD_IDENTITY is in Private Preview. ClickPipes uses the GCP service account returned in
    gcpWorkloadIdentity.principal by the operation with operationId clickPipesServiceContextGet; grant it access to the
    source resources."""

    seek_type: SeekTypeOrStr = Field(alias="seekType")
    """Starting position strategy for consuming the subscription. The seekTimestamp companion is required only when
    seekType is "timestamp"; setting it for a mismatched seek type is rejected."""

    seek_timestamp: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="seekTimestamp")
    """RFC 3339 / ISO 8601 timestamp to seek to. Required when seekType is "timestamp"; must be omitted otherwise."""

    filter: OptionalNullable[str] = UNSET
    """Optional Pub/Sub subscription filter expression (CEL). Maximum 256 characters."""

    enable_ordering: OptionalNullable[bool] = Field(default=UNSET, alias="enableOrdering")
    """Whether to enable ordered delivery of messages (requires messages to be published with ordering keys)."""

    ack_deadline: OptionalNullable[int] = Field(default=UNSET, alias="ackDeadline")
    """Acknowledgement deadline for messages, in seconds. Must be between 10 and 600."""


class ClickPipePostPubSubWorkloadIdentitySourceDict(TypedDict):
    format: Format6OrStr
    project_id: str
    topic: str
    authentication: Literal["SERVICE_ACCOUNT_WORKLOAD_IDENTITY"]
    seek_type: SeekTypeOrStr
    seek_timestamp: NotRequired[RFC3339DateTime | None]
    filter: NotRequired[str | None]
    enable_ordering: NotRequired[bool | None]
    ack_deadline: NotRequired[int | None]
