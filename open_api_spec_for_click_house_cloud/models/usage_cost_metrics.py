from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsageCostMetrics(SdkBaseModel):
    storage_chc: Optional[float] = Field(default=UNSET, alias="storageCHC")
    """Cost of storage in ClickHouse Credits (CHCs). Applies to dataWarehouse entities."""

    backup_chc: Optional[float] = Field(default=UNSET, alias="backupCHC")
    """Cost of backup in ClickHouse Credits (CHCs). Applies to dataWarehouse entities."""

    compute_chc: Optional[float] = Field(default=UNSET, alias="computeCHC")
    """Cost of compute in ClickHouse Credits (CHCs). Applies to service and clickpipe entities."""

    data_transfer_chc: Optional[float] = Field(default=UNSET, alias="dataTransferCHC")
    """Cost of data transfer in ClickHouse Credits (CHCs). Applies to clickpipe entities."""

    initial_load_chc: Optional[float] = Field(default=UNSET, alias="initialLoadCHC")
    """Cost of initial load and resyncs in ClickHouse Credits (CHCs). Applies to clickpipe entities."""

    public_data_transfer_chc: Optional[float] = Field(default=UNSET, alias="publicDataTransferCHC")
    """Cost of data transfer in ClickHouse Credits (CHCs). Applies to service entities."""

    inter_region_tier1_data_transfer_chc: Optional[float] = Field(
        default=UNSET, alias="interRegionTier1DataTransferCHC"
    )
    """Cost of tier1 inter-region data transfer in ClickHouse Credits (CHCs). Applies to service entities."""

    inter_region_tier2_data_transfer_chc: Optional[float] = Field(
        default=UNSET, alias="interRegionTier2DataTransferCHC"
    )
    """Cost of tier2 inter-region data transfer in ClickHouse Credits (CHCs). Applies to service entities."""

    inter_region_tier3_data_transfer_chc: Optional[float] = Field(
        default=UNSET, alias="interRegionTier3DataTransferCHC"
    )
    """Cost of tier3 inter-region data transfer in ClickHouse Credits (CHCs). Applies to service entities."""

    inter_region_tier4_data_transfer_chc: Optional[float] = Field(
        default=UNSET, alias="interRegionTier4DataTransferCHC"
    )
    """Cost of tier4 inter-region data transfer in ClickHouse Credits (CHCs). Applies to service entities."""


class UsageCostMetricsDict(TypedDict):
    storage_chc: NotRequired[float]
    backup_chc: NotRequired[float]
    compute_chc: NotRequired[float]
    data_transfer_chc: NotRequired[float]
    initial_load_chc: NotRequired[float]
    public_data_transfer_chc: NotRequired[float]
    inter_region_tier1_data_transfer_chc: NotRequired[float]
    inter_region_tier2_data_transfer_chc: NotRequired[float]
    inter_region_tier3_data_transfer_chc: NotRequired[float]
    inter_region_tier4_data_transfer_chc: NotRequired[float]
