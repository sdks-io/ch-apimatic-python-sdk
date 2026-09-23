from __future__ import annotations

from typing import TypeAlias

from ..click_stack_event_patterns_chart_config import (
    ClickStackEventPatternsChartConfig,
    ClickStackEventPatternsChartConfigDict,
)
from ..click_stack_heatmap_chart_config import ClickStackHeatmapChartConfig, ClickStackHeatmapChartConfigDict
from ..click_stack_markdown_chart_config import ClickStackMarkdownChartConfig, ClickStackMarkdownChartConfigDict
from ..click_stack_search_chart_config import ClickStackSearchChartConfig, ClickStackSearchChartConfigDict
from .click_stack_bar_chart_config import ClickStackBarChartConfig, ClickStackBarChartConfigDict
from .click_stack_categorical_bar_chart_config import (
    ClickStackCategoricalBarChartConfig,
    ClickStackCategoricalBarChartConfigDict,
)
from .click_stack_line_chart_config import ClickStackLineChartConfig, ClickStackLineChartConfigDict
from .click_stack_number_chart_config import ClickStackNumberChartConfig, ClickStackNumberChartConfigDict
from .click_stack_pie_chart_config import ClickStackPieChartConfig, ClickStackPieChartConfigDict
from .click_stack_table_chart_config import ClickStackTableChartConfig, ClickStackTableChartConfigDict

ClickStackTileConfig: TypeAlias = (
    ClickStackLineChartConfig
    | ClickStackBarChartConfig
    | ClickStackTableChartConfig
    | ClickStackNumberChartConfig
    | ClickStackPieChartConfig
    | ClickStackCategoricalBarChartConfig
    | ClickStackHeatmapChartConfig
    | ClickStackSearchChartConfig
    | ClickStackEventPatternsChartConfig
    | ClickStackMarkdownChartConfig
)

ClickStackTileConfigDict: TypeAlias = (
    ClickStackLineChartConfigDict
    | ClickStackBarChartConfigDict
    | ClickStackTableChartConfigDict
    | ClickStackNumberChartConfigDict
    | ClickStackPieChartConfigDict
    | ClickStackCategoricalBarChartConfigDict
    | ClickStackHeatmapChartConfigDict
    | ClickStackSearchChartConfigDict
    | ClickStackEventPatternsChartConfigDict
    | ClickStackMarkdownChartConfigDict
)
