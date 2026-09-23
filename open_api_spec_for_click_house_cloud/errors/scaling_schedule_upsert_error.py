from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_scaling_schedule400_error1 import (
    V1OrganizationsServicesScalingSchedule400Error1,
)
from ..models.v1_organizations_services_scaling_schedule500_error1 import (
    V1OrganizationsServicesScalingSchedule500Error1,
)

ScalingScheduleUpsertErrorBody: TypeAlias = (
    V1OrganizationsServicesScalingSchedule400Error1 | V1OrganizationsServicesScalingSchedule500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _ScalingScheduleUpsertError:
    def map(self, response: HttpResponse) -> ScalingScheduleUpsertErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesScalingSchedule400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesScalingSchedule500Error1](response)
            case _:
                return RawError(response)


scaling_schedule_upsert_error_mapper: Final[ErrorMapper[ScalingScheduleUpsertErrorBody]] = _ScalingScheduleUpsertError()
