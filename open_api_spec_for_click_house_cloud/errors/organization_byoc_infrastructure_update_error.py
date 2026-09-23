from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_byoc_infrastructure400_error1 import V1OrganizationsByocInfrastructure400Error1
from ..models.v1_organizations_byoc_infrastructure500_error1 import V1OrganizationsByocInfrastructure500Error1

OrganizationByocInfrastructureUpdateErrorBody: TypeAlias = (
    V1OrganizationsByocInfrastructure400Error1 | V1OrganizationsByocInfrastructure500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _OrganizationByocInfrastructureUpdateError:
    def map(self, response: HttpResponse) -> OrganizationByocInfrastructureUpdateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsByocInfrastructure400Error1](response)
            case 500:
                return decode_json[V1OrganizationsByocInfrastructure500Error1](response)
            case _:
                return RawError(response)


organization_byoc_infrastructure_update_error_mapper: Final[
    ErrorMapper[OrganizationByocInfrastructureUpdateErrorBody]
] = _OrganizationByocInfrastructureUpdateError()
