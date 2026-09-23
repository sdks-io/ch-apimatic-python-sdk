from __future__ import annotations

from typing import TypeAlias

from ..click_stack_on_click_target_id_variant import (
    ClickStackOnClickTargetIdVariant,
    ClickStackOnClickTargetIdVariantDict,
)
from ..click_stack_on_click_target_template_variant import (
    ClickStackOnClickTargetTemplateVariant,
    ClickStackOnClickTargetTemplateVariantDict,
)

ClickStackOnClickTarget: TypeAlias = ClickStackOnClickTargetIdVariant | ClickStackOnClickTargetTemplateVariant

ClickStackOnClickTargetDict: TypeAlias = (
    ClickStackOnClickTargetIdVariantDict | ClickStackOnClickTargetTemplateVariantDict
)
