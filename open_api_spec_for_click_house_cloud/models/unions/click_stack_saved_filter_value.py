from __future__ import annotations

from typing import TypeAlias

from ..click_stack_sql_saved_filter_value import ClickStackSqlSavedFilterValue, ClickStackSqlSavedFilterValueDict
from ..click_stack_variable_saved_filter_value import (
    ClickStackVariableSavedFilterValue,
    ClickStackVariableSavedFilterValueDict,
)

ClickStackSavedFilterValue: TypeAlias = ClickStackSqlSavedFilterValue | ClickStackVariableSavedFilterValue

ClickStackSavedFilterValueDict: TypeAlias = ClickStackSqlSavedFilterValueDict | ClickStackVariableSavedFilterValueDict
