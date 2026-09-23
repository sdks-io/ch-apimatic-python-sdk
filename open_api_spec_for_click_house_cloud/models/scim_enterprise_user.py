from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scim_enterprise_manager import ScimEnterpriseManager, ScimEnterpriseManagerDict


class ScimEnterpriseUser(SdkBaseModel):
    employee_number: Optional[str] = Field(default=UNSET, alias="employeeNumber")
    """Numeric or alphanumeric identifier assigned to a person, typically based on order of hire or association with an
    organization."""

    cost_center: Optional[str] = Field(default=UNSET, alias="costCenter")
    """Identifies the name of a cost center."""

    organization: Optional[str] = UNSET
    """Identifies the name of an organization."""

    division: Optional[str] = UNSET
    """Identifies the name of a division."""

    department: Optional[str] = UNSET
    """Identifies the name of a department."""

    manager: Optional[ScimEnterpriseManager] = UNSET


class ScimEnterpriseUserDict(TypedDict):
    employee_number: NotRequired[str]
    cost_center: NotRequired[str]
    organization: NotRequired[str]
    division: NotRequired[str]
    department: NotRequired[str]
    manager: NotRequired[ScimEnterpriseManagerDict]
