from __future__ import annotations

from typing import TypeAlias

from ..click_stack_log_source import ClickStackLogSource, ClickStackLogSourceDict
from ..click_stack_metric_source import ClickStackMetricSource, ClickStackMetricSourceDict
from ..click_stack_promql_source import ClickStackPromqlSource, ClickStackPromqlSourceDict
from ..click_stack_session_source import ClickStackSessionSource, ClickStackSessionSourceDict
from ..click_stack_trace_source import ClickStackTraceSource, ClickStackTraceSourceDict

ClickStackSource: TypeAlias = (
    ClickStackLogSource
    | ClickStackTraceSource
    | ClickStackMetricSource
    | ClickStackSessionSource
    | ClickStackPromqlSource
)

ClickStackSourceDict: TypeAlias = (
    ClickStackLogSourceDict
    | ClickStackTraceSourceDict
    | ClickStackMetricSourceDict
    | ClickStackSessionSourceDict
    | ClickStackPromqlSourceDict
)
