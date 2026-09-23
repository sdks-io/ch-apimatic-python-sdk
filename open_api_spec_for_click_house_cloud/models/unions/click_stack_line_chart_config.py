from __future__ import annotations

from typing import TypeAlias

from ..click_stack_line_builder_chart_config import (
    ClickStackLineBuilderChartConfig,
    ClickStackLineBuilderChartConfigDict,
)
from ..click_stack_line_raw_sql_chart_config import ClickStackLineRawSqlChartConfig, ClickStackLineRawSqlChartConfigDict

ClickStackLineChartConfig: TypeAlias = ClickStackLineBuilderChartConfig | ClickStackLineRawSqlChartConfig

ClickStackLineChartConfigDict: TypeAlias = ClickStackLineBuilderChartConfigDict | ClickStackLineRawSqlChartConfigDict
