from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class QuotaCode(str, Enum):
    """Stable identifier of the quota. Use it to request a single quota by code."""

    SERVICES_PER_ORGANIZATION = "services-per-organization"
    POSTGRES_SERVICES_PER_ORGANIZATION = "postgres-services-per-organization"
    REPLICAS_PER_WAREHOUSE = "replicas-per-warehouse"
    API_KEYS_PER_ORGANIZATION = "api-keys-per-organization"

    __str__ = str.__str__


QuotaCodeOrStr: TypeAlias = Annotated[QuotaCode | str, open_enum_validator(QuotaCode)]
