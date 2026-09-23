from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickstack_webhooks400_error1 import (
    V1OrganizationsServicesClickstackWebhooks400Error1,
)
from ..models.v1_organizations_services_clickstack_webhooks500_error1 import (
    V1OrganizationsServicesClickstackWebhooks500Error1,
)

ClickStackCreateWebhookErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackWebhooks400Error1 | V1OrganizationsServicesClickstackWebhooks500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackCreateWebhookError:
    def map(self, response: HttpResponse) -> ClickStackCreateWebhookErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackWebhooks400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickstackWebhooks500Error1](response)
            case _:
                return RawError(response)


click_stack_create_webhook_error_mapper: Final[
    ErrorMapper[ClickStackCreateWebhookErrorBody]
] = _ClickStackCreateWebhookError()
