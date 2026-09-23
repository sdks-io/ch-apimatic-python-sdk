from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ServiceAccount(SdkBaseModel):
    service_account_file: str = Field(alias="serviceAccountFile")
    """Google Cloud service account JSON key file content, base64 encoded."""


class ServiceAccountDict(TypedDict):
    service_account_file: str
