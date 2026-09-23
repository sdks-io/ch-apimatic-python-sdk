from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_replica_scaling400_error1 import V1OrganizationsServicesReplicaScaling400Error1
from ..models.v1_organizations_services_replica_scaling500_error1 import V1OrganizationsServicesReplicaScaling500Error1

InstanceReplicaScalingUpdateErrorBody: TypeAlias = (
    V1OrganizationsServicesReplicaScaling400Error1 | V1OrganizationsServicesReplicaScaling500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _InstanceReplicaScalingUpdateError:
    def map(self, response: HttpResponse) -> InstanceReplicaScalingUpdateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesReplicaScaling400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesReplicaScaling500Error1](response)
            case _:
                return RawError(response)


instance_replica_scaling_update_error_mapper: Final[
    ErrorMapper[InstanceReplicaScalingUpdateErrorBody]
] = _InstanceReplicaScalingUpdateError()
