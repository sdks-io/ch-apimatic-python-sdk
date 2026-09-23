from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_credit_balances400_error1 import V1OrganizationsCreditBalances400Error1
from ..models.v1_organizations_credit_balances500_error1 import V1OrganizationsCreditBalances500Error1

CreditBalancesGetErrorBody: TypeAlias = (
    V1OrganizationsCreditBalances400Error1 | V1OrganizationsCreditBalances500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _CreditBalancesGetError:
    def map(self, response: HttpResponse) -> CreditBalancesGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsCreditBalances400Error1](response)
            case 500:
                return decode_json[V1OrganizationsCreditBalances500Error1](response)
            case _:
                return RawError(response)


credit_balances_get_error_mapper: Final[ErrorMapper[CreditBalancesGetErrorBody]] = _CreditBalancesGetError()
