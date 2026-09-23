from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ComplianceType(str, Enum):
    """Type of regulatory compliance for service."""

    HIPAA = "hipaa"
    PCI = "pci"

    __str__ = str.__str__


ComplianceTypeOrStr: TypeAlias = Annotated[ComplianceType | str, open_enum_validator(ComplianceType)]
