from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.table_engine4 import TableEngine4OrStr


class ClickPipeBigQueryPipeTableMapping(SdkBaseModel):
    source_dataset_name: str = Field(alias="sourceDatasetName")
    """Source BigQuery dataset name."""

    source_table: str = Field(alias="sourceTable")
    """Source table name."""

    target_table: str = Field(alias="targetTable")
    """Target ClickHouse table name."""

    excluded_columns: Optional[list[str]] = Field(default=UNSET, alias="excludedColumns")
    """Columns to exclude from the target table."""

    use_custom_sorting_key: Optional[bool] = Field(default=UNSET, alias="useCustomSortingKey")
    """Whether to use a custom sorting key for the target table."""

    sorting_keys: Optional[list[str]] = Field(default=UNSET, alias="sortingKeys")
    """Ordered list of columns to use as sorting key for the target table."""

    table_engine: Optional[TableEngine4OrStr] = Field(default=UNSET, alias="tableEngine")
    """Table engine to use for the target table."""


class ClickPipeBigQueryPipeTableMappingDict(TypedDict):
    source_dataset_name: str
    source_table: str
    target_table: str
    excluded_columns: NotRequired[list[str]]
    use_custom_sorting_key: NotRequired[bool]
    sorting_keys: NotRequired[list[str]]
    table_engine: NotRequired[TableEngine4OrStr]
