from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.authentication5 import Authentication5OrStr
from .enums.format2 import Format2OrStr
from .enums.iterator_type import IteratorTypeOrStr
from .msk_iam_user import MskIamUser, MskIamUserDict


class ClickPipePostKinesisSource(SdkBaseModel):
    format: Optional[Format2OrStr] = UNSET
    """Format of the Kinesis stream."""

    stream_name: Optional[str] = Field(default=UNSET, alias="streamName")
    """Name of the Kinesis stream."""

    region: Optional[str] = UNSET
    """AWS region of the Kinesis stream."""

    use_enhanced_fan_out: OptionalNullable[bool] = Field(default=UNSET, alias="useEnhancedFanOut")
    """Use enhanced fan-out for the Kinesis stream."""

    iterator_type: Optional[IteratorTypeOrStr] = Field(default=UNSET, alias="iteratorType")
    """Type of iterator to use when reading from the Kinesis stream. If AT_TIMESTAMP is used, the timestamp field must
    be provided."""

    timestamp: OptionalNullable[int] = UNSET
    """UNIX timestamp to start reading from the Kinesis stream. Required if iteratorType is AT_TIMESTAMP."""

    authentication: Optional[Authentication5OrStr] = UNSET
    """Authentication method to use with the Kinesis stream."""

    iam_role: OptionalNullable[str] = Field(default=UNSET, alias="iamRole")
    """IAM role to use for authentication. Required if IAM_ROLE is used."""

    access_key: OptionalNullable[MskIamUser] = Field(default=UNSET, alias="accessKey")
    protobuf_schema: Optional[str] = Field(default=UNSET, alias="protobufSchema")
    """Base64-encoded .proto source or serialized FileDescriptorSet. Required with Protobuf format and not supported
    with other formats."""


class ClickPipePostKinesisSourceDict(TypedDict):
    format: NotRequired[Format2OrStr]
    stream_name: NotRequired[str]
    region: NotRequired[str]
    use_enhanced_fan_out: NotRequired[bool | None]
    iterator_type: NotRequired[IteratorTypeOrStr]
    timestamp: NotRequired[int | None]
    authentication: NotRequired[Authentication5OrStr]
    iam_role: NotRequired[str | None]
    access_key: NotRequired[MskIamUserDict | None]
    protobuf_schema: NotRequired[str]
