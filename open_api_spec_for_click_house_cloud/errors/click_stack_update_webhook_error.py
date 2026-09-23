from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickstack_webhooks_click_stack_webhook_id400_error1 import (
    V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1,
)
from ..models.v1_organizations_services_clickstack_webhooks_click_stack_webhook_id500_error1 import (
    V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1,
)

ClickStackUpdateWebhookErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1
    | V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackUpdateWebhookError:
    def map(self, response: HttpResponse) -> ClickStackUpdateWebhookErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1](response)
            case _:
                return RawError(response)


click_stack_update_webhook_error_mapper: Final[
    ErrorMapper[ClickStackUpdateWebhookErrorBody]
] = _ClickStackUpdateWebhookError()
