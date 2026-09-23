from __future__ import annotations

from typing import TypeAlias

from ..click_stack_markdown_chart_series import ClickStackMarkdownChartSeries, ClickStackMarkdownChartSeriesDict
from ..click_stack_number_chart_series import ClickStackNumberChartSeries, ClickStackNumberChartSeriesDict
from ..click_stack_search_chart_series import ClickStackSearchChartSeries, ClickStackSearchChartSeriesDict
from ..click_stack_table_chart_series import ClickStackTableChartSeries, ClickStackTableChartSeriesDict
from ..click_stack_time_chart_series import ClickStackTimeChartSeries, ClickStackTimeChartSeriesDict

ClickStackDashboardChartSeries: TypeAlias = (
    ClickStackTimeChartSeries
    | ClickStackTableChartSeries
    | ClickStackNumberChartSeries
    | ClickStackSearchChartSeries
    | ClickStackMarkdownChartSeries
)

ClickStackDashboardChartSeriesDict: TypeAlias = (
    ClickStackTimeChartSeriesDict
    | ClickStackTableChartSeriesDict
    | ClickStackNumberChartSeriesDict
    | ClickStackSearchChartSeriesDict
    | ClickStackMarkdownChartSeriesDict
)
