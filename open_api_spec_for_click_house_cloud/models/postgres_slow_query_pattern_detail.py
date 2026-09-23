from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .postgres_query_execution import PostgresQueryExecution, PostgresQueryExecutionDict
from .postgres_slow_query_pattern import PostgresSlowQueryPattern, PostgresSlowQueryPatternDict


class PostgresSlowQueryPatternDetail(SdkBaseModel):
    aggregate: Optional[PostgresSlowQueryPattern] = UNSET
    recent_executions: list[PostgresQueryExecution] = Field(alias="recentExecutions")
    """Recent individual executions matching the pattern."""


class PostgresSlowQueryPatternDetailDict(TypedDict):
    aggregate: NotRequired[PostgresSlowQueryPatternDict]
    recent_executions: list[PostgresQueryExecutionDict]
