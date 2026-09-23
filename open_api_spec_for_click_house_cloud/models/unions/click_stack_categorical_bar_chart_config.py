from __future__ import annotations

from typing import TypeAlias

from ..click_stack_categorical_bar_builder_chart_config import (
    ClickStackCategoricalBarBuilderChartConfig,
    ClickStackCategoricalBarBuilderChartConfigDict,
)
from ..click_stack_categorical_bar_raw_sql_chart_config import (
    ClickStackCategoricalBarRawSqlChartConfig,
    ClickStackCategoricalBarRawSqlChartConfigDict,
)

ClickStackCategoricalBarChartConfig: TypeAlias = (
    ClickStackCategoricalBarBuilderChartConfig | ClickStackCategoricalBarRawSqlChartConfig
)

ClickStackCategoricalBarChartConfigDict: TypeAlias = (
    ClickStackCategoricalBarBuilderChartConfigDict | ClickStackCategoricalBarRawSqlChartConfigDict
)
