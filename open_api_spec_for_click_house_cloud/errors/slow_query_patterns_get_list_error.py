from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_postgres_slow_query_patterns400_error1 import (
    V1OrganizationsPostgresSlowQueryPatterns400Error1,
)
from ..models.v1_organizations_postgres_slow_query_patterns500_error1 import (
    V1OrganizationsPostgresSlowQueryPatterns500Error1,
)

SlowQueryPatternsGetListErrorBody: TypeAlias = (
    V1OrganizationsPostgresSlowQueryPatterns400Error1 | V1OrganizationsPostgresSlowQueryPatterns500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _SlowQueryPatternsGetListError:
    def map(self, response: HttpResponse) -> SlowQueryPatternsGetListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPostgresSlowQueryPatterns400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPostgresSlowQueryPatterns500Error1](response)
            case _:
                return RawError(response)


slow_query_patterns_get_list_error_mapper: Final[
    ErrorMapper[SlowQueryPatternsGetListErrorBody]
] = _SlowQueryPatternsGetListError()
