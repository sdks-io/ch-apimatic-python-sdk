from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_postgres_slow_query_patterns_query_id400_error1 import (
    V1OrganizationsPostgresSlowQueryPatternsQueryId400Error1,
)
from ..models.v1_organizations_postgres_slow_query_patterns_query_id500_error1 import (
    V1OrganizationsPostgresSlowQueryPatternsQueryId500Error1,
)

SlowQueryPatternGetErrorBody: TypeAlias = (
    V1OrganizationsPostgresSlowQueryPatternsQueryId400Error1
    | V1OrganizationsPostgresSlowQueryPatternsQueryId500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _SlowQueryPatternGetError:
    def map(self, response: HttpResponse) -> SlowQueryPatternGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPostgresSlowQueryPatternsQueryId400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPostgresSlowQueryPatternsQueryId500Error1](response)
            case _:
                return RawError(response)


slow_query_pattern_get_error_mapper: Final[ErrorMapper[SlowQueryPatternGetErrorBody]] = _SlowQueryPatternGetError()
