from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class KeyUpdateType(str, Enum):
    """For 'openapi_key_update' activities: the type of update that was performed."""

    CREATED = "created"
    DELETED = "deleted"
    NAME_CHANGED = "name-changed"
    ROLE_CHANGED = "role-changed"
    STATE_CHANGED = "state-changed"
    DATE_CHANGED = "date-changed"
    IP_ACCESS_LIST_CHANGED = "ip-access-list-changed"
    ORG_ROLE_CHANGED = "org-role-changed"
    DEFAULT_SERVICE_ROLE_CHANGED = "default-service-role-changed"
    SERVICE_ROLE_CHANGED = "service-role-changed"
    ROLES_V2_CHANGED = "roles-v2-changed"

    __str__ = str.__str__


KeyUpdateTypeOrStr: TypeAlias = Annotated[KeyUpdateType | str, open_enum_validator(KeyUpdateType)]
