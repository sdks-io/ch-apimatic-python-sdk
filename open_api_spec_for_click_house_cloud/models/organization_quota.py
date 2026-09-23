from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.quota_code import QuotaCodeOrStr
from .enums.scope import ScopeOrStr


class OrganizationQuota(SdkBaseModel):
    quota_code: QuotaCodeOrStr = Field(alias="quotaCode")
    """Stable identifier of the quota. Use it to request a single quota by code."""

    name: str
    """Human-readable name of the quota."""

    description: str
    """Explanation of the resource the quota limits and how the limit is applied."""

    scope: ScopeOrStr
    """Granularity at which the limit is applied. For example, ``replicas-per-warehouse`` is an organization-wide
    setting that limits each warehouse individually."""

    value: int
    """Limit currently applied to the organization, including any adjustments made for the organization. The value can
    change when the billing status of the organization changes."""

    usage: Optional[int] = UNSET
    """Current consumption of the quota. Omitted for quotas that do not report usage. Usage can exceed ``value`` when a
    limit was lowered after resources were created; existing resources are not affected."""

    adjustable: bool
    """Whether the limit can be raised for the organization by contacting ClickHouse support."""


class OrganizationQuotaDict(TypedDict):
    quota_code: QuotaCodeOrStr
    name: str
    description: str
    scope: ScopeOrStr
    value: int
    usage: NotRequired[int]
    adjustable: bool
