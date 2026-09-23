from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .enums.entity_type import EntityTypeOrStr
from .usage_cost_metrics import UsageCostMetrics, UsageCostMetricsDict


class UsageCostRecord(SdkBaseModel):
    data_warehouse_id: Optional[UUID] = Field(default=UNSET, alias="dataWarehouseId")
    """ID of the dataWarehouse this entity belongs to (or is)."""

    service_id: OptionalNullable[UUID] = Field(default=UNSET, alias="serviceId")
    """ID of the service this entity belongs to (or is). Set to null for dataWarehouse entities."""

    date: Optional[Date] = UNSET
    """Date of the usage. ISO-8601 date, based on the UTC timezone."""

    entity_type: Optional[EntityTypeOrStr] = Field(default=UNSET, alias="entityType")
    """Type of the entity."""

    entity_id: Optional[UUID] = Field(default=UNSET, alias="entityId")
    """Unique ID of the entity."""

    entity_name: Optional[str] = Field(default=UNSET, alias="entityName")
    """Name of the entity."""

    metrics: Optional[UsageCostMetrics] = UNSET
    total_chc: Optional[float] = Field(default=UNSET, alias="totalCHC")
    """Total cost of usage in ClickHouse Credits (CHCs) for this entity."""

    locked: Optional[bool] = UNSET
    """When true, the record is immutable. Unlocked records are subject to change until locked."""


class UsageCostRecordDict(TypedDict):
    data_warehouse_id: NotRequired[UUID]
    service_id: NotRequired[UUID | None]
    date: NotRequired[Date]
    entity_type: NotRequired[EntityTypeOrStr]
    entity_id: NotRequired[UUID]
    entity_name: NotRequired[str]
    metrics: NotRequired[UsageCostMetricsDict]
    total_chc: NotRequired[float]
    locked: NotRequired[bool]
