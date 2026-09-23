from __future__ import annotations

from typing import TypeAlias

from ..click_stack_on_click_dashboard import ClickStackOnClickDashboard, ClickStackOnClickDashboardDict
from ..click_stack_on_click_external import ClickStackOnClickExternal, ClickStackOnClickExternalDict
from ..click_stack_on_click_search import ClickStackOnClickSearch, ClickStackOnClickSearchDict

ClickStackOnClick: TypeAlias = ClickStackOnClickSearch | ClickStackOnClickDashboard | ClickStackOnClickExternal

ClickStackOnClickDict: TypeAlias = (
    ClickStackOnClickSearchDict | ClickStackOnClickDashboardDict | ClickStackOnClickExternalDict
)
