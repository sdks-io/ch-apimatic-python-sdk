from __future__ import annotations

from typing import TypeAlias

from ..click_stack_number_builder_chart_config import (
    ClickStackNumberBuilderChartConfig,
    ClickStackNumberBuilderChartConfigDict,
)
from ..click_stack_number_raw_sql_chart_config import (
    ClickStackNumberRawSqlChartConfig,
    ClickStackNumberRawSqlChartConfigDict,
)

ClickStackNumberChartConfig: TypeAlias = ClickStackNumberBuilderChartConfig | ClickStackNumberRawSqlChartConfig

ClickStackNumberChartConfigDict: TypeAlias = (
    ClickStackNumberBuilderChartConfigDict | ClickStackNumberRawSqlChartConfigDict
)
