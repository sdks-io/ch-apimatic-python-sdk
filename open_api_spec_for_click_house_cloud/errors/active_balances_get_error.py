from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_active_balances400_error1 import V1OrganizationsActiveBalances400Error1
from ..models.v1_organizations_active_balances500_error1 import V1OrganizationsActiveBalances500Error1

ActiveBalancesGetErrorBody: TypeAlias = (
    V1OrganizationsActiveBalances400Error1 | V1OrganizationsActiveBalances500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _ActiveBalancesGetError:
    def map(self, response: HttpResponse) -> ActiveBalancesGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsActiveBalances400Error1](response)
            case 500:
                return decode_json[V1OrganizationsActiveBalances500Error1](response)
            case _:
                return RawError(response)


active_balances_get_error_mapper: Final[ErrorMapper[ActiveBalancesGetErrorBody]] = _ActiveBalancesGetError()
