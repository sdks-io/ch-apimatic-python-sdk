from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.authentication5 import Authentication5OrStr
from .msk_iam_user import MskIamUser, MskIamUserDict


class ClickPipePatchKinesisSource(SdkBaseModel):
    authentication: OptionalNullable[Authentication5OrStr] = UNSET
    """Authentication method to use with the Kinesis stream."""

    iam_role: OptionalNullable[str] = Field(default=UNSET, alias="iamRole")
    """IAM role to use for authentication. Required if IAM_ROLE is used."""

    access_key: OptionalNullable[MskIamUser] = Field(default=UNSET, alias="accessKey")


class ClickPipePatchKinesisSourceDict(TypedDict):
    authentication: NotRequired[Authentication5OrStr | None]
    iam_role: NotRequired[str | None]
    access_key: NotRequired[MskIamUserDict | None]
