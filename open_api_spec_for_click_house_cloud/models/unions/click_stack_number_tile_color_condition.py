from __future__ import annotations

from typing import TypeAlias

from ..click_stack_between_color_condition import ClickStackBetweenColorCondition, ClickStackBetweenColorConditionDict
from ..click_stack_equality_color_condition import (
    ClickStackEqualityColorCondition,
    ClickStackEqualityColorConditionDict,
)
from ..click_stack_numeric_color_condition import ClickStackNumericColorCondition, ClickStackNumericColorConditionDict

ClickStackNumberTileColorCondition: TypeAlias = (
    ClickStackNumericColorCondition | ClickStackBetweenColorCondition | ClickStackEqualityColorCondition
)

ClickStackNumberTileColorConditionDict: TypeAlias = (
    ClickStackNumericColorConditionDict | ClickStackBetweenColorConditionDict | ClickStackEqualityColorConditionDict
)
