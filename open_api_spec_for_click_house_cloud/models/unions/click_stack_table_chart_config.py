from __future__ import annotations

from typing import TypeAlias

from ..click_stack_table_builder_chart_config import (
    ClickStackTableBuilderChartConfig,
    ClickStackTableBuilderChartConfigDict,
)
from ..click_stack_table_raw_sql_chart_config import (
    ClickStackTableRawSqlChartConfig,
    ClickStackTableRawSqlChartConfigDict,
)

ClickStackTableChartConfig: TypeAlias = ClickStackTableBuilderChartConfig | ClickStackTableRawSqlChartConfig

ClickStackTableChartConfigDict: TypeAlias = ClickStackTableBuilderChartConfigDict | ClickStackTableRawSqlChartConfigDict
