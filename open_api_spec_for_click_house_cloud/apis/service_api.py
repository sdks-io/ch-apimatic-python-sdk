from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.instance_create_error import InstanceCreateErrorBody, instance_create_error_mapper
from ..errors.instance_delete_error import InstanceDeleteErrorBody, instance_delete_error_mapper
from ..errors.instance_get_error import InstanceGetErrorBody, instance_get_error_mapper
from ..errors.instance_get_list_error import InstanceGetListErrorBody, instance_get_list_error_mapper
from ..errors.instance_password_update_error import (
    InstancePasswordUpdateErrorBody,
    instance_password_update_error_mapper,
)
from ..errors.instance_private_endpoint_config_get_error import (
    InstancePrivateEndpointConfigGetErrorBody,
    instance_private_endpoint_config_get_error_mapper,
)
from ..errors.instance_private_endpoint_create_error import (
    InstancePrivateEndpointCreateErrorBody,
    instance_private_endpoint_create_error_mapper,
)
from ..errors.instance_query_endpoint_delete_error import (
    InstanceQueryEndpointDeleteErrorBody,
    instance_query_endpoint_delete_error_mapper,
)
from ..errors.instance_query_endpoint_get_error import (
    InstanceQueryEndpointGetErrorBody,
    instance_query_endpoint_get_error_mapper,
)
from ..errors.instance_query_endpoint_upsert_error import (
    InstanceQueryEndpointUpsertErrorBody,
    instance_query_endpoint_upsert_error_mapper,
)
from ..errors.instance_replica_scaling_update_error import (
    InstanceReplicaScalingUpdateErrorBody,
    instance_replica_scaling_update_error_mapper,
)
from ..errors.instance_scaling_update_error import InstanceScalingUpdateErrorBody, instance_scaling_update_error_mapper
from ..errors.instance_state_update_error import InstanceStateUpdateErrorBody, instance_state_update_error_mapper
from ..errors.instance_update_error import InstanceUpdateErrorBody, instance_update_error_mapper
from ..errors.scaling_schedule_delete_error import ScalingScheduleDeleteErrorBody, scaling_schedule_delete_error_mapper
from ..errors.scaling_schedule_get_error import ScalingScheduleGetErrorBody, scaling_schedule_get_error_mapper
from ..errors.scaling_schedule_upsert_error import ScalingScheduleUpsertErrorBody, scaling_schedule_upsert_error_mapper
from ..errors.service_clickhouse_setting_delete_error import (
    ServiceClickhouseSettingDeleteErrorBody,
    service_clickhouse_setting_delete_error_mapper,
)
from ..errors.service_clickhouse_setting_get_error import (
    ServiceClickhouseSettingGetErrorBody,
    service_clickhouse_setting_get_error_mapper,
)
from ..errors.service_clickhouse_settings_list_get_error import (
    ServiceClickhouseSettingsListGetErrorBody,
    service_clickhouse_settings_list_get_error_mapper,
)
from ..errors.service_clickhouse_settings_schema_get_error import (
    ServiceClickhouseSettingsSchemaGetErrorBody,
    service_clickhouse_settings_schema_get_error_mapper,
)
from ..errors.service_clickhouse_settings_update_error import (
    ServiceClickhouseSettingsUpdateErrorBody,
    service_clickhouse_settings_update_error_mapper,
)
from ..errors.service_profiles_list_error import ServiceProfilesListErrorBody, service_profiles_list_error_mapper
from ..errors.upgrade_window_delete_error import UpgradeWindowDeleteErrorBody, upgrade_window_delete_error_mapper
from ..errors.upgrade_window_get_error import UpgradeWindowGetErrorBody, upgrade_window_get_error_mapper
from ..errors.upgrade_window_update_error import UpgradeWindowUpdateErrorBody, upgrade_window_update_error_mapper
from ..models.instance_service_query_api_endpoints_post_request import (
    InstanceServiceQueryApiEndpointsPostRequest,
    InstanceServiceQueryApiEndpointsPostRequestDict,
)
from ..models.scaling_schedule_post_request import ScalingSchedulePostRequest, ScalingSchedulePostRequestDict
from ..models.servic_private_endpointe_post_request import (
    ServicPrivateEndpointePostRequest,
    ServicPrivateEndpointePostRequestDict,
)
from ..models.service_clickhouse_settings_patch_request import (
    ServiceClickhouseSettingsPatchRequest,
    ServiceClickhouseSettingsPatchRequestDict,
)
from ..models.service_password_patch_request import ServicePasswordPatchRequest, ServicePasswordPatchRequestDict
from ..models.service_patch_request import ServicePatchRequest, ServicePatchRequestDict
from ..models.service_post_request import ServicePostRequest, ServicePostRequestDict
from ..models.service_replica_scaling_patch_request import (
    ServiceReplicaScalingPatchRequest,
    ServiceReplicaScalingPatchRequestDict,
)
from ..models.service_scaling_patch_request import ServiceScalingPatchRequest, ServiceScalingPatchRequestDict
from ..models.service_state_patch_request import ServiceStatePatchRequest, ServiceStatePatchRequestDict
from ..models.upgrade_window_put_request import UpgradeWindowPutRequest, UpgradeWindowPutRequestDict
from ..models.v1_organizations_service_profiles_response import V1OrganizationsServiceProfilesResponse
from ..models.v1_organizations_services_clickhouse_settings_response import (
    V1OrganizationsServicesClickhouseSettingsResponse,
)
from ..models.v1_organizations_services_clickhouse_settings_response1 import (
    V1OrganizationsServicesClickhouseSettingsResponse1,
)
from ..models.v1_organizations_services_clickhouse_settings_schema_response import (
    V1OrganizationsServicesClickhouseSettingsSchemaResponse,
)
from ..models.v1_organizations_services_clickhouse_settings_setting_name_response import (
    V1OrganizationsServicesClickhouseSettingsSettingNameResponse,
)
from ..models.v1_organizations_services_clickhouse_settings_setting_name_response1 import (
    V1OrganizationsServicesClickhouseSettingsSettingNameResponse1,
)
from ..models.v1_organizations_services_password_response import V1OrganizationsServicesPasswordResponse
from ..models.v1_organizations_services_private_endpoint_config_response import (
    V1OrganizationsServicesPrivateEndpointConfigResponse,
)
from ..models.v1_organizations_services_private_endpoint_response import V1OrganizationsServicesPrivateEndpointResponse
from ..models.v1_organizations_services_replica_scaling_response import V1OrganizationsServicesReplicaScalingResponse
from ..models.v1_organizations_services_response import V1OrganizationsServicesResponse
from ..models.v1_organizations_services_response1 import V1OrganizationsServicesResponse1
from ..models.v1_organizations_services_response2 import V1OrganizationsServicesResponse2
from ..models.v1_organizations_services_response4 import V1OrganizationsServicesResponse4
from ..models.v1_organizations_services_scaling_response import V1OrganizationsServicesScalingResponse
from ..models.v1_organizations_services_scaling_schedule_response import V1OrganizationsServicesScalingScheduleResponse
from ..models.v1_organizations_services_scaling_schedule_response2 import (
    V1OrganizationsServicesScalingScheduleResponse2,
)
from ..models.v1_organizations_services_service_query_endpoint_response import (
    V1OrganizationsServicesServiceQueryEndpointResponse,
)
from ..models.v1_organizations_services_service_query_endpoint_response1 import (
    V1OrganizationsServicesServiceQueryEndpointResponse1,
)
from ..models.v1_organizations_services_state_response import V1OrganizationsServicesStateResponse
from ..models.v1_organizations_services_upgrade_window_response import V1OrganizationsServicesUpgradeWindowResponse
from ..models.v1_organizations_services_upgrade_window_response2 import V1OrganizationsServicesUpgradeWindowResponse2
from ..server.server import Server


class ServiceApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ServiceApiWithRawResponse(client, server, auth)

    def instance_create(
        self,
        organization_id: UUID,
        *,
        body: ServicePostRequest | ServicePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesResponse1:
        """Creates a new service in the organization, and returns the current service state and a password to access the
        service. The service is started asynchronously.

        Args:
            organization_id: ID of the organization that will own the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServices400Error1 |
                V1OrganizationsServices500Error1 | RawError``."""
        return self._with_raw_response.instance_create(
            organization_id, body=body, request_options=request_options
        ).unwrap()

    def instance_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesResponse4:
        """Deletes the service. The service must be in stopped state and is deleted asynchronously after this method
        call.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServices400Error1 |
                V1OrganizationsServices500Error1 | RawError``."""
        return self._with_raw_response.instance_delete(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def instance_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesResponse2:
        """Returns a service that belongs to the organization

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServices400Error1 |
                V1OrganizationsServices500Error1 | RawError``."""
        return self._with_raw_response.instance_get(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def instance_get_list(
        self,
        organization_id: UUID,
        *,
        filter: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesResponse:
        """Returns a list of all services in the organization.

        Args:
            organization_id: ID of the requested organization.
            filter: Filter criteria to apply when retrieving the resource. Currently, only filtering by resource tags is
                supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServices400Error1 |
                V1OrganizationsServices500Error1 | RawError``."""
        return self._with_raw_response.instance_get_list(
            organization_id, filter=filter, request_options=request_options
        ).unwrap()

    def instance_password_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServicePasswordPatchRequest | ServicePasswordPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesPasswordResponse:
        """Sets a new password for the service

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update password.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesPassword400Error1 |
                V1OrganizationsServicesPassword500Error1 | RawError``."""
        return self._with_raw_response.instance_password_update(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def instance_private_endpoint_config_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesPrivateEndpointConfigResponse:
        """Information required to set up a private endpoint

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesPrivateEndpointConfig400Error1 |
                V1OrganizationsServicesPrivateEndpointConfig500Error1 | RawError``."""
        return self._with_raw_response.instance_private_endpoint_config_get(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def instance_private_endpoint_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServicPrivateEndpointePostRequest | ServicPrivateEndpointePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesPrivateEndpointResponse:
        """Create a new private endpoint. The private endpoint will be associated with this service and organization

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesPrivateEndpoint400Error1 |
                V1OrganizationsServicesPrivateEndpoint500Error1 | RawError``."""
        return self._with_raw_response.instance_private_endpoint_create(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def instance_query_endpoint_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesServiceQueryEndpointResponse1:
        """Removes the service query endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesServiceQueryEndpoint400Error1 |
                V1OrganizationsServicesServiceQueryEndpoint500Error1 | RawError``."""
        return self._with_raw_response.instance_query_endpoint_delete(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def instance_query_endpoint_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesServiceQueryEndpointResponse:
        """Get the configuration for the service query endpoint that allows executing queries via API.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesServiceQueryEndpoint400Error1 |
                V1OrganizationsServicesServiceQueryEndpoint500Error1 | RawError``."""
        return self._with_raw_response.instance_query_endpoint_get(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def instance_query_endpoint_upsert(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: (
            InstanceServiceQueryApiEndpointsPostRequest | InstanceServiceQueryApiEndpointsPostRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesServiceQueryEndpointResponse:
        """Create the service query endpoint that allows executing queries via API.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesServiceQueryEndpoint400Error1 |
                V1OrganizationsServicesServiceQueryEndpoint500Error1 | RawError``."""
        return self._with_raw_response.instance_query_endpoint_upsert(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def instance_replica_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceReplicaScalingPatchRequest | ServiceReplicaScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesReplicaScalingResponse:
        """Updates minimum and maximum memory limits per replica and idle mode scaling behavior for the service.
        Supports both vertical autoscaling (fixed replica count, variable memory) and horizontal autoscaling (variable
        replica count, fixed memory). The memory settings are available only for "production" services and must be a
        multiple of 4 starting from 8GB. For vertical autoscaling, please contact support to enable adjustment of
        numReplicas. For horizontal autoscaling (autoscalingMode "horizontal" with minReplicas/maxReplicas), contact
        support to enable the feature for your organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update scaling parameters.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesReplicaScaling400Error1 |
                V1OrganizationsServicesReplicaScaling500Error1 | RawError``."""
        return self._with_raw_response.instance_replica_scaling_update(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def instance_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceScalingPatchRequest | ServiceScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesScalingResponse:
        """Updates minimum and maximum total memory limits and idle mode scaling behavior for the service. The memory
        settings are available only for "production" services and must be a multiple of 12 starting from 24GB. Please
        contact support to enable adjustment of numReplicas.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update scaling parameters.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesScaling400Error1 |
                V1OrganizationsServicesScaling500Error1 | RawError``."""
        return self._with_raw_response.instance_scaling_update(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def instance_state_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceStatePatchRequest | ServiceStatePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesStateResponse:
        """Starts, stops, or wakes a service. The ``start`` and ``stop`` commands require the
        ``control-plane:service:manage`` permission on the service. The ``awake`` command requires only
        ``control-plane:service:view`` and applies to an idle service; it does not start a stopped service.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update state.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesState400Error1 |
                V1OrganizationsServicesState500Error1 | RawError``."""
        return self._with_raw_response.instance_state_update(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def instance_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServicePatchRequest | ServicePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesResponse2:
        """Updates basic service details like service name or IP access list.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServices400Error1 |
                V1OrganizationsServices500Error1 | RawError``."""
        return self._with_raw_response.instance_update(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def scaling_schedule_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesScalingScheduleResponse2:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes the
        autoscaling schedule for a service. If a schedule entry is currently active, the base scaling config is restored
        to the instance before the schedule is removed. Returns 404 if no schedule exists. Requires the scheduled
        autoscaling feature to be enabled for the organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesScalingSchedule400Error1 |
                V1OrganizationsServicesScalingSchedule500Error1 | RawError``."""
        return self._with_raw_response.scaling_schedule_delete(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def scaling_schedule_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesScalingScheduleResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the
        autoscaling schedule for a service. Returns 404 if no schedule has been configured or if the schedule was
        cleared. Requires the scheduled autoscaling feature to be enabled for the organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesScalingSchedule400Error1 |
                V1OrganizationsServicesScalingSchedule500Error1 | RawError``."""
        return self._with_raw_response.scaling_schedule_get(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def scaling_schedule_upsert(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ScalingSchedulePostRequest | ScalingSchedulePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesScalingScheduleResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates or fully
        replaces the autoscaling schedule for a service. Pass an empty ``entries`` array to clear the schedule — a
        subsequent GET will return 404, and the response will contain an empty ``baseConfig`` (all fields absent). The
        base scaling config (applied when no entry is active) is managed separately via the ``replicaScaling`` endpoint.
        Requires the scheduled autoscaling feature to be enabled for the organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesScalingSchedule400Error1 |
                V1OrganizationsServicesScalingSchedule500Error1 | RawError``."""
        return self._with_raw_response.scaling_schedule_upsert(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def service_clickhouse_setting_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        setting_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickhouseSettingsSettingNameResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Removes a
        previously-configured ClickHouse setting, reverting its effective value to the platform default. Settings under
        ``spec.extraConfig.server.*`` (e.g. ``keep_alive_timeout``,
        ``shared_merge_tree_disable_merges_and_mutations_assignment``) trigger a ClickHouse server rollout restart;
        other settings propagate to all replicas after a short delay. Deleting a setting that was never configured is a
        no-op (200 OK).

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            setting_name: Name of the setting to reset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickhouseSettingsSettingName400Error1 |
                V1OrganizationsServicesClickhouseSettingsSettingName500Error1 | RawError``."""
        return self._with_raw_response.service_clickhouse_setting_delete(
            organization_id, service_id, setting_name, request_options=request_options
        ).unwrap()

    def service_clickhouse_setting_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        setting_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickhouseSettingsSettingNameResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current
        value of a ClickHouse setting for the service. Use the `schema endpoint
        <#tag/Service/operation/serviceClickhouseSettingsSchemaGet>`__ to discover which settings are configurable.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            setting_name: Name of the setting to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickhouseSettingsSettingName400Error1 |
                V1OrganizationsServicesClickhouseSettingsSettingName500Error1 | RawError``."""
        return self._with_raw_response.service_clickhouse_setting_get(
            organization_id, service_id, setting_name, request_options=request_options
        ).unwrap()

    def service_clickhouse_settings_list_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickhouseSettingsResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the
        configured ClickHouse settings for the service. Only settings that have been explicitly set are included.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickhouseSettings400Error1 |
                V1OrganizationsServicesClickhouseSettings500Error1 | RawError``."""
        return self._with_raw_response.service_clickhouse_settings_list_get(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def service_clickhouse_settings_schema_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickhouseSettingsSchemaResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the schema
        of all configurable ClickHouse settings, including types, valid values, descriptions, and warnings.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickhouseSettingsSchema400Error1 |
                V1OrganizationsServicesClickhouseSettingsSchema500Error1 | RawError``."""
        return self._with_raw_response.service_clickhouse_settings_schema_get(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def service_clickhouse_settings_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceClickhouseSettingsPatchRequest | ServiceClickhouseSettingsPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickhouseSettingsResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Updates one or more
        ClickHouse settings for the service. To reset a setting to its platform default, use the `DELETE single setting
        <#tag/Service/operation/serviceClickhouseSettingDelete>`__ endpoint. Use the `schema endpoint
        <#tag/Service/operation/serviceClickhouseSettingsSchemaGet>`__ to discover which settings are configurable.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickhouseSettings400Error1 |
                V1OrganizationsServicesClickhouseSettings500Error1 | RawError``."""
        return self._with_raw_response.service_clickhouse_settings_update(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def service_profiles_list(
        self,
        organization_id: UUID,
        *,
        region_id: str | None = None,
        byoc_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServiceProfilesResponse:
        """Returns the custom instance profiles the organization can use in a region. Pass byoc_id to list the profiles
        configured for a BYOC infrastructure; the region is then taken from the infrastructure and region_id may be
        omitted. The list is empty when the organization tier does not include custom hardware profiles.

        Args:
            organization_id: ID of the organization to list available profiles for.
            region_id: Region to list profiles for, e.g. us-east-1. Required unless byoc_id is set; when both are set it
                must match the BYOC infrastructure's region.
            byoc_id: ID of the BYOC infrastructure to list profiles for. BYOC profiles are only returned when this is
                set.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServiceProfiles400Error1 |
                V1OrganizationsServiceProfiles500Error1 | RawError``."""
        return self._with_raw_response.service_profiles_list(
            organization_id, region_id=region_id, byoc_id=byoc_id, request_options=request_options
        ).unwrap()

    def upgrade_window_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesUpgradeWindowResponse2:
        """Deletes the upgrade window for a service, restoring the default scheduling behaviour. The upgrade window can
        only be deleted on primary services. Deletion succeeds even if the organization has lost the scheduled upgrades
        entitlement, so a window can be cleared after entitlement loss.

        Errors:
        - 400: the service is a secondary service.
        - 401: missing, invalid, or disabled API key.
        - 403: caller lacks ``control-plane:service:manage`` on the service.
        - 404: service does not exist, is not visible to the caller, or no upgrade window is configured.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesUpgradeWindow400Error1 |
                V1OrganizationsServicesUpgradeWindow500Error1 | RawError``."""
        return self._with_raw_response.upgrade_window_delete(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def upgrade_window_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesUpgradeWindowResponse:
        """Returns the configured upgrade window for a service.

        Errors:
        - 401: missing, invalid, or disabled API key.
        - 403: caller lacks ``control-plane:service:view`` on the service.
        - 404: service does not exist, is not visible to the caller, or no upgrade window has been configured.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesUpgradeWindow400Error1 |
                V1OrganizationsServicesUpgradeWindow500Error1 | RawError``."""
        return self._with_raw_response.upgrade_window_get(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def upgrade_window_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: UpgradeWindowPutRequest | UpgradeWindowPutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesUpgradeWindowResponse:
        """Creates or fully replaces the upgrade window for a service. The upgrade window currently lasts 6 hours from
        ``startHourUtc``. The upgrade window can only be set on primary services; secondary services inherit the primary
        service window.

        Errors:
        - 400: invalid field values (``weekday`` not in 0–6, ``startHourUtc`` not in {0, 6, 12, 18}), or the service is
            a secondary service.
        - 401: missing, invalid, or disabled API key.
        - 403: caller lacks ``control-plane:service:manage`` on the service, or the organization does not have the
            scheduled upgrades feature enabled.
        - 404: service does not exist or is not visible to the caller.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesUpgradeWindow400Error1 |
                V1OrganizationsServicesUpgradeWindow500Error1 | RawError``."""
        return self._with_raw_response.upgrade_window_update(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ServiceApiWithRawResponse:
        return self._with_raw_response


class AsyncServiceApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncServiceApiWithRawResponse(client, server, auth)

    async def instance_create(
        self,
        organization_id: UUID,
        *,
        body: ServicePostRequest | ServicePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesResponse1:
        """Creates a new service in the organization, and returns the current service state and a password to access the
        service. The service is started asynchronously.

        Args:
            organization_id: ID of the organization that will own the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServices400Error1 |
                V1OrganizationsServices500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_create(organization_id, body=body, request_options=request_options)
        ).unwrap()

    async def instance_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesResponse4:
        """Deletes the service. The service must be in stopped state and is deleted asynchronously after this method
        call.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServices400Error1 |
                V1OrganizationsServices500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_delete(organization_id, service_id, request_options=request_options)
        ).unwrap()

    async def instance_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesResponse2:
        """Returns a service that belongs to the organization

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServices400Error1 |
                V1OrganizationsServices500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_get(organization_id, service_id, request_options=request_options)
        ).unwrap()

    async def instance_get_list(
        self,
        organization_id: UUID,
        *,
        filter: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesResponse:
        """Returns a list of all services in the organization.

        Args:
            organization_id: ID of the requested organization.
            filter: Filter criteria to apply when retrieving the resource. Currently, only filtering by resource tags is
                supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServices400Error1 |
                V1OrganizationsServices500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_get_list(
                organization_id, filter=filter, request_options=request_options
            )
        ).unwrap()

    async def instance_password_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServicePasswordPatchRequest | ServicePasswordPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesPasswordResponse:
        """Sets a new password for the service

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update password.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesPassword400Error1 |
                V1OrganizationsServicesPassword500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_password_update(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def instance_private_endpoint_config_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesPrivateEndpointConfigResponse:
        """Information required to set up a private endpoint

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesPrivateEndpointConfig400Error1 |
                V1OrganizationsServicesPrivateEndpointConfig500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_private_endpoint_config_get(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def instance_private_endpoint_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServicPrivateEndpointePostRequest | ServicPrivateEndpointePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesPrivateEndpointResponse:
        """Create a new private endpoint. The private endpoint will be associated with this service and organization

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesPrivateEndpoint400Error1 |
                V1OrganizationsServicesPrivateEndpoint500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_private_endpoint_create(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def instance_query_endpoint_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesServiceQueryEndpointResponse1:
        """Removes the service query endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesServiceQueryEndpoint400Error1 |
                V1OrganizationsServicesServiceQueryEndpoint500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_query_endpoint_delete(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def instance_query_endpoint_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesServiceQueryEndpointResponse:
        """Get the configuration for the service query endpoint that allows executing queries via API.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesServiceQueryEndpoint400Error1 |
                V1OrganizationsServicesServiceQueryEndpoint500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_query_endpoint_get(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def instance_query_endpoint_upsert(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: (
            InstanceServiceQueryApiEndpointsPostRequest | InstanceServiceQueryApiEndpointsPostRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesServiceQueryEndpointResponse:
        """Create the service query endpoint that allows executing queries via API.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesServiceQueryEndpoint400Error1 |
                V1OrganizationsServicesServiceQueryEndpoint500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_query_endpoint_upsert(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def instance_replica_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceReplicaScalingPatchRequest | ServiceReplicaScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesReplicaScalingResponse:
        """Updates minimum and maximum memory limits per replica and idle mode scaling behavior for the service.
        Supports both vertical autoscaling (fixed replica count, variable memory) and horizontal autoscaling (variable
        replica count, fixed memory). The memory settings are available only for "production" services and must be a
        multiple of 4 starting from 8GB. For vertical autoscaling, please contact support to enable adjustment of
        numReplicas. For horizontal autoscaling (autoscalingMode "horizontal" with minReplicas/maxReplicas), contact
        support to enable the feature for your organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update scaling parameters.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesReplicaScaling400Error1 |
                V1OrganizationsServicesReplicaScaling500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_replica_scaling_update(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def instance_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceScalingPatchRequest | ServiceScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesScalingResponse:
        """Updates minimum and maximum total memory limits and idle mode scaling behavior for the service. The memory
        settings are available only for "production" services and must be a multiple of 12 starting from 24GB. Please
        contact support to enable adjustment of numReplicas.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update scaling parameters.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesScaling400Error1 |
                V1OrganizationsServicesScaling500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_scaling_update(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def instance_state_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceStatePatchRequest | ServiceStatePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesStateResponse:
        """Starts, stops, or wakes a service. The ``start`` and ``stop`` commands require the
        ``control-plane:service:manage`` permission on the service. The ``awake`` command requires only
        ``control-plane:service:view`` and applies to an idle service; it does not start a stopped service.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update state.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesState400Error1 |
                V1OrganizationsServicesState500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_state_update(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def instance_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServicePatchRequest | ServicePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesResponse2:
        """Updates basic service details like service name or IP access list.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServices400Error1 |
                V1OrganizationsServices500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_update(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def scaling_schedule_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesScalingScheduleResponse2:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes the
        autoscaling schedule for a service. If a schedule entry is currently active, the base scaling config is restored
        to the instance before the schedule is removed. Returns 404 if no schedule exists. Requires the scheduled
        autoscaling feature to be enabled for the organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesScalingSchedule400Error1 |
                V1OrganizationsServicesScalingSchedule500Error1 | RawError``."""
        return (
            await self._with_raw_response.scaling_schedule_delete(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def scaling_schedule_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesScalingScheduleResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the
        autoscaling schedule for a service. Returns 404 if no schedule has been configured or if the schedule was
        cleared. Requires the scheduled autoscaling feature to be enabled for the organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesScalingSchedule400Error1 |
                V1OrganizationsServicesScalingSchedule500Error1 | RawError``."""
        return (
            await self._with_raw_response.scaling_schedule_get(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def scaling_schedule_upsert(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ScalingSchedulePostRequest | ScalingSchedulePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesScalingScheduleResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates or fully
        replaces the autoscaling schedule for a service. Pass an empty ``entries`` array to clear the schedule — a
        subsequent GET will return 404, and the response will contain an empty ``baseConfig`` (all fields absent). The
        base scaling config (applied when no entry is active) is managed separately via the ``replicaScaling`` endpoint.
        Requires the scheduled autoscaling feature to be enabled for the organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesScalingSchedule400Error1 |
                V1OrganizationsServicesScalingSchedule500Error1 | RawError``."""
        return (
            await self._with_raw_response.scaling_schedule_upsert(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def service_clickhouse_setting_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        setting_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickhouseSettingsSettingNameResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Removes a
        previously-configured ClickHouse setting, reverting its effective value to the platform default. Settings under
        ``spec.extraConfig.server.*`` (e.g. ``keep_alive_timeout``,
        ``shared_merge_tree_disable_merges_and_mutations_assignment``) trigger a ClickHouse server rollout restart;
        other settings propagate to all replicas after a short delay. Deleting a setting that was never configured is a
        no-op (200 OK).

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            setting_name: Name of the setting to reset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickhouseSettingsSettingName400Error1 |
                V1OrganizationsServicesClickhouseSettingsSettingName500Error1 | RawError``."""
        return (
            await self._with_raw_response.service_clickhouse_setting_delete(
                organization_id, service_id, setting_name, request_options=request_options
            )
        ).unwrap()

    async def service_clickhouse_setting_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        setting_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickhouseSettingsSettingNameResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current
        value of a ClickHouse setting for the service. Use the `schema endpoint
        <#tag/Service/operation/serviceClickhouseSettingsSchemaGet>`__ to discover which settings are configurable.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            setting_name: Name of the setting to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickhouseSettingsSettingName400Error1 |
                V1OrganizationsServicesClickhouseSettingsSettingName500Error1 | RawError``."""
        return (
            await self._with_raw_response.service_clickhouse_setting_get(
                organization_id, service_id, setting_name, request_options=request_options
            )
        ).unwrap()

    async def service_clickhouse_settings_list_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickhouseSettingsResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the
        configured ClickHouse settings for the service. Only settings that have been explicitly set are included.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickhouseSettings400Error1 |
                V1OrganizationsServicesClickhouseSettings500Error1 | RawError``."""
        return (
            await self._with_raw_response.service_clickhouse_settings_list_get(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def service_clickhouse_settings_schema_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickhouseSettingsSchemaResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the schema
        of all configurable ClickHouse settings, including types, valid values, descriptions, and warnings.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickhouseSettingsSchema400Error1 |
                V1OrganizationsServicesClickhouseSettingsSchema500Error1 | RawError``."""
        return (
            await self._with_raw_response.service_clickhouse_settings_schema_get(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def service_clickhouse_settings_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceClickhouseSettingsPatchRequest | ServiceClickhouseSettingsPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickhouseSettingsResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Updates one or more
        ClickHouse settings for the service. To reset a setting to its platform default, use the `DELETE single setting
        <#tag/Service/operation/serviceClickhouseSettingDelete>`__ endpoint. Use the `schema endpoint
        <#tag/Service/operation/serviceClickhouseSettingsSchemaGet>`__ to discover which settings are configurable.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickhouseSettings400Error1 |
                V1OrganizationsServicesClickhouseSettings500Error1 | RawError``."""
        return (
            await self._with_raw_response.service_clickhouse_settings_update(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def service_profiles_list(
        self,
        organization_id: UUID,
        *,
        region_id: str | None = None,
        byoc_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServiceProfilesResponse:
        """Returns the custom instance profiles the organization can use in a region. Pass byoc_id to list the profiles
        configured for a BYOC infrastructure; the region is then taken from the infrastructure and region_id may be
        omitted. The list is empty when the organization tier does not include custom hardware profiles.

        Args:
            organization_id: ID of the organization to list available profiles for.
            region_id: Region to list profiles for, e.g. us-east-1. Required unless byoc_id is set; when both are set it
                must match the BYOC infrastructure's region.
            byoc_id: ID of the BYOC infrastructure to list profiles for. BYOC profiles are only returned when this is
                set.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServiceProfiles400Error1 |
                V1OrganizationsServiceProfiles500Error1 | RawError``."""
        return (
            await self._with_raw_response.service_profiles_list(
                organization_id, region_id=region_id, byoc_id=byoc_id, request_options=request_options
            )
        ).unwrap()

    async def upgrade_window_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesUpgradeWindowResponse2:
        """Deletes the upgrade window for a service, restoring the default scheduling behaviour. The upgrade window can
        only be deleted on primary services. Deletion succeeds even if the organization has lost the scheduled upgrades
        entitlement, so a window can be cleared after entitlement loss.

        Errors:
        - 400: the service is a secondary service.
        - 401: missing, invalid, or disabled API key.
        - 403: caller lacks ``control-plane:service:manage`` on the service.
        - 404: service does not exist, is not visible to the caller, or no upgrade window is configured.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesUpgradeWindow400Error1 |
                V1OrganizationsServicesUpgradeWindow500Error1 | RawError``."""
        return (
            await self._with_raw_response.upgrade_window_delete(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def upgrade_window_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesUpgradeWindowResponse:
        """Returns the configured upgrade window for a service.

        Errors:
        - 401: missing, invalid, or disabled API key.
        - 403: caller lacks ``control-plane:service:view`` on the service.
        - 404: service does not exist, is not visible to the caller, or no upgrade window has been configured.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesUpgradeWindow400Error1 |
                V1OrganizationsServicesUpgradeWindow500Error1 | RawError``."""
        return (
            await self._with_raw_response.upgrade_window_get(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def upgrade_window_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: UpgradeWindowPutRequest | UpgradeWindowPutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesUpgradeWindowResponse:
        """Creates or fully replaces the upgrade window for a service. The upgrade window currently lasts 6 hours from
        ``startHourUtc``. The upgrade window can only be set on primary services; secondary services inherit the primary
        service window.

        Errors:
        - 400: invalid field values (``weekday`` not in 0–6, ``startHourUtc`` not in {0, 6, 12, 18}), or the service is
            a secondary service.
        - 401: missing, invalid, or disabled API key.
        - 403: caller lacks ``control-plane:service:manage`` on the service, or the organization does not have the
            scheduled upgrades feature enabled.
        - 404: service does not exist or is not visible to the caller.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesUpgradeWindow400Error1 |
                V1OrganizationsServicesUpgradeWindow500Error1 | RawError``."""
        return (
            await self._with_raw_response.upgrade_window_update(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncServiceApiWithRawResponse:
        return self._with_raw_response


class ServiceApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def instance_create(
        self,
        organization_id: UUID,
        *,
        body: ServicePostRequest | ServicePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesResponse1, InstanceCreateErrorBody]:
        """Creates a new service in the organization, and returns the current service state and a password to access the
        service. The service is started asynchronously.

        Args:
            organization_id: ID of the organization that will own the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/services"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServicePostRequest | ServicePostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesResponse1],
            error_mapper=instance_create_error_mapper,
            request_options=request_options,
        )

    def instance_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesResponse4, InstanceDeleteErrorBody]:
        """Deletes the service. The service must be in stopped state and is deleted asynchronously after this method
        call.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesResponse4],
            error_mapper=instance_delete_error_mapper,
            request_options=request_options,
        )

    def instance_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesResponse2, InstanceGetErrorBody]:
        """Returns a service that belongs to the organization

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesResponse2],
            error_mapper=instance_get_error_mapper,
            request_options=request_options,
        )

    def instance_get_list(
        self,
        organization_id: UUID,
        *,
        filter: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesResponse, InstanceGetListErrorBody]:
        """Returns a list of all services in the organization.

        Args:
            organization_id: ID of the requested organization.
            filter: Filter criteria to apply when retrieving the resource. Currently, only filtering by resource tags is
                supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[list[str] | None]("filter", filter)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesResponse],
            error_mapper=instance_get_list_error_mapper,
            request_options=request_options,
        )

    def instance_password_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServicePasswordPatchRequest | ServicePasswordPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesPasswordResponse, InstancePasswordUpdateErrorBody]:
        """Sets a new password for the service

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update password.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/password"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServicePasswordPatchRequest | ServicePasswordPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesPasswordResponse],
            error_mapper=instance_password_update_error_mapper,
            request_options=request_options,
        )

    def instance_private_endpoint_config_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesPrivateEndpointConfigResponse, InstancePrivateEndpointConfigGetErrorBody]:
        """Information required to set up a private endpoint

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/privateEndpointConfig"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesPrivateEndpointConfigResponse],
            error_mapper=instance_private_endpoint_config_get_error_mapper,
            request_options=request_options,
        )

    def instance_private_endpoint_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServicPrivateEndpointePostRequest | ServicPrivateEndpointePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesPrivateEndpointResponse, InstancePrivateEndpointCreateErrorBody]:
        """Create a new private endpoint. The private endpoint will be associated with this service and organization

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/privateEndpoint"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServicPrivateEndpointePostRequest | ServicPrivateEndpointePostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesPrivateEndpointResponse],
            error_mapper=instance_private_endpoint_create_error_mapper,
            request_options=request_options,
        )

    def instance_query_endpoint_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesServiceQueryEndpointResponse1, InstanceQueryEndpointDeleteErrorBody]:
        """Removes the service query endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/serviceQueryEndpoint"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesServiceQueryEndpointResponse1],
            error_mapper=instance_query_endpoint_delete_error_mapper,
            request_options=request_options,
        )

    def instance_query_endpoint_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesServiceQueryEndpointResponse, InstanceQueryEndpointGetErrorBody]:
        """Get the configuration for the service query endpoint that allows executing queries via API.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/serviceQueryEndpoint"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesServiceQueryEndpointResponse],
            error_mapper=instance_query_endpoint_get_error_mapper,
            request_options=request_options,
        )

    def instance_query_endpoint_upsert(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: (
            InstanceServiceQueryApiEndpointsPostRequest | InstanceServiceQueryApiEndpointsPostRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesServiceQueryEndpointResponse, InstanceQueryEndpointUpsertErrorBody]:
        """Create the service query endpoint that allows executing queries via API.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/serviceQueryEndpoint"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                InstanceServiceQueryApiEndpointsPostRequest | InstanceServiceQueryApiEndpointsPostRequestDict | None
            ](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesServiceQueryEndpointResponse],
            error_mapper=instance_query_endpoint_upsert_error_mapper,
            request_options=request_options,
        )

    def instance_replica_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceReplicaScalingPatchRequest | ServiceReplicaScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesReplicaScalingResponse, InstanceReplicaScalingUpdateErrorBody]:
        """Updates minimum and maximum memory limits per replica and idle mode scaling behavior for the service.
        Supports both vertical autoscaling (fixed replica count, variable memory) and horizontal autoscaling (variable
        replica count, fixed memory). The memory settings are available only for "production" services and must be a
        multiple of 4 starting from 8GB. For vertical autoscaling, please contact support to enable adjustment of
        numReplicas. For horizontal autoscaling (autoscalingMode "horizontal" with minReplicas/maxReplicas), contact
        support to enable the feature for your organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update scaling parameters.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/replicaScaling"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServiceReplicaScalingPatchRequest | ServiceReplicaScalingPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesReplicaScalingResponse],
            error_mapper=instance_replica_scaling_update_error_mapper,
            request_options=request_options,
        )

    def instance_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceScalingPatchRequest | ServiceScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesScalingResponse, InstanceScalingUpdateErrorBody]:
        """Updates minimum and maximum total memory limits and idle mode scaling behavior for the service. The memory
        settings are available only for "production" services and must be a multiple of 12 starting from 24GB. Please
        contact support to enable adjustment of numReplicas.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update scaling parameters.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/scaling"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServiceScalingPatchRequest | ServiceScalingPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesScalingResponse],
            error_mapper=instance_scaling_update_error_mapper,
            request_options=request_options,
        )

    def instance_state_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceStatePatchRequest | ServiceStatePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesStateResponse, InstanceStateUpdateErrorBody]:
        """Starts, stops, or wakes a service. The ``start`` and ``stop`` commands require the
        ``control-plane:service:manage`` permission on the service. The ``awake`` command requires only
        ``control-plane:service:view`` and applies to an idle service; it does not start a stopped service.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update state.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/state"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServiceStatePatchRequest | ServiceStatePatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesStateResponse],
            error_mapper=instance_state_update_error_mapper,
            request_options=request_options,
        )

    def instance_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServicePatchRequest | ServicePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesResponse2, InstanceUpdateErrorBody]:
        """Updates basic service details like service name or IP access list.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServicePatchRequest | ServicePatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesResponse2],
            error_mapper=instance_update_error_mapper,
            request_options=request_options,
        )

    def scaling_schedule_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesScalingScheduleResponse2, ScalingScheduleDeleteErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes the
        autoscaling schedule for a service. If a schedule entry is currently active, the base scaling config is restored
        to the instance before the schedule is removed. Returns 404 if no schedule exists. Requires the scheduled
        autoscaling feature to be enabled for the organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/scalingSchedule"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesScalingScheduleResponse2],
            error_mapper=scaling_schedule_delete_error_mapper,
            request_options=request_options,
        )

    def scaling_schedule_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesScalingScheduleResponse, ScalingScheduleGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the
        autoscaling schedule for a service. Returns 404 if no schedule has been configured or if the schedule was
        cleared. Requires the scheduled autoscaling feature to be enabled for the organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/scalingSchedule"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesScalingScheduleResponse],
            error_mapper=scaling_schedule_get_error_mapper,
            request_options=request_options,
        )

    def scaling_schedule_upsert(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ScalingSchedulePostRequest | ScalingSchedulePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesScalingScheduleResponse, ScalingScheduleUpsertErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates or fully
        replaces the autoscaling schedule for a service. Pass an empty ``entries`` array to clear the schedule — a
        subsequent GET will return 404, and the response will contain an empty ``baseConfig`` (all fields absent). The
        base scaling config (applied when no entry is active) is managed separately via the ``replicaScaling`` endpoint.
        Requires the scheduled autoscaling feature to be enabled for the organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/scalingSchedule"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScalingSchedulePostRequest | ScalingSchedulePostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesScalingScheduleResponse],
            error_mapper=scaling_schedule_upsert_error_mapper,
            request_options=request_options,
        )

    def service_clickhouse_setting_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        setting_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickhouseSettingsSettingNameResponse1, ServiceClickhouseSettingDeleteErrorBody
    ]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Removes a
        previously-configured ClickHouse setting, reverting its effective value to the platform default. Settings under
        ``spec.extraConfig.server.*`` (e.g. ``keep_alive_timeout``,
        ``shared_merge_tree_disable_merges_and_mutations_assignment``) trigger a ClickHouse server rollout restart;
        other settings propagate to all replicas after a short delay. Deleting a setting that was never configured is a
        no-op (200 OK).

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            setting_name: Name of the setting to reset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings/{settingName}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("settingName", setting_name),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickhouseSettingsSettingNameResponse1],
            error_mapper=service_clickhouse_setting_delete_error_mapper,
            request_options=request_options,
        )

    def service_clickhouse_setting_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        setting_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickhouseSettingsSettingNameResponse, ServiceClickhouseSettingGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current
        value of a ClickHouse setting for the service. Use the `schema endpoint
        <#tag/Service/operation/serviceClickhouseSettingsSchemaGet>`__ to discover which settings are configurable.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            setting_name: Name of the setting to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings/{settingName}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("settingName", setting_name),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickhouseSettingsSettingNameResponse],
            error_mapper=service_clickhouse_setting_get_error_mapper,
            request_options=request_options,
        )

    def service_clickhouse_settings_list_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickhouseSettingsResponse, ServiceClickhouseSettingsListGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the
        configured ClickHouse settings for the service. Only settings that have been explicitly set are included.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickhouseSettingsResponse],
            error_mapper=service_clickhouse_settings_list_get_error_mapper,
            request_options=request_options,
        )

    def service_clickhouse_settings_schema_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        V1OrganizationsServicesClickhouseSettingsSchemaResponse, ServiceClickhouseSettingsSchemaGetErrorBody
    ]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the schema
        of all configurable ClickHouse settings, including types, valid values, descriptions, and warnings.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings/schema"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickhouseSettingsSchemaResponse],
            error_mapper=service_clickhouse_settings_schema_get_error_mapper,
            request_options=request_options,
        )

    def service_clickhouse_settings_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceClickhouseSettingsPatchRequest | ServiceClickhouseSettingsPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickhouseSettingsResponse1, ServiceClickhouseSettingsUpdateErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Updates one or more
        ClickHouse settings for the service. To reset a setting to its platform default, use the `DELETE single setting
        <#tag/Service/operation/serviceClickhouseSettingDelete>`__ endpoint. Use the `schema endpoint
        <#tag/Service/operation/serviceClickhouseSettingsSchemaGet>`__ to discover which settings are configurable.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServiceClickhouseSettingsPatchRequest | ServiceClickhouseSettingsPatchRequestDict | None](
                body
            ),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickhouseSettingsResponse1],
            error_mapper=service_clickhouse_settings_update_error_mapper,
            request_options=request_options,
        )

    def service_profiles_list(
        self,
        organization_id: UUID,
        *,
        region_id: str | None = None,
        byoc_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServiceProfilesResponse, ServiceProfilesListErrorBody]:
        """Returns the custom instance profiles the organization can use in a region. Pass byoc_id to list the profiles
        configured for a BYOC infrastructure; the region is then taken from the infrastructure and region_id may be
        omitted. The list is empty when the organization tier does not include custom hardware profiles.

        Args:
            organization_id: ID of the organization to list available profiles for.
            region_id: Region to list profiles for, e.g. us-east-1. Required unless byoc_id is set; when both are set it
                must match the BYOC infrastructure's region.
            byoc_id: ID of the BYOC infrastructure to list profiles for. BYOC profiles are only returned when this is
                set.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/serviceProfiles"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[str | None]("region_id", region_id), param[UUID | None]("byoc_id", byoc_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServiceProfilesResponse],
            error_mapper=service_profiles_list_error_mapper,
            request_options=request_options,
        )

    def upgrade_window_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesUpgradeWindowResponse2, UpgradeWindowDeleteErrorBody]:
        """Deletes the upgrade window for a service, restoring the default scheduling behaviour. The upgrade window can
        only be deleted on primary services. Deletion succeeds even if the organization has lost the scheduled upgrades
        entitlement, so a window can be cleared after entitlement loss.

        Errors:
        - 400: the service is a secondary service.
        - 401: missing, invalid, or disabled API key.
        - 403: caller lacks ``control-plane:service:manage`` on the service.
        - 404: service does not exist, is not visible to the caller, or no upgrade window is configured.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/upgradeWindow"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesUpgradeWindowResponse2],
            error_mapper=upgrade_window_delete_error_mapper,
            request_options=request_options,
        )

    def upgrade_window_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesUpgradeWindowResponse, UpgradeWindowGetErrorBody]:
        """Returns the configured upgrade window for a service.

        Errors:
        - 401: missing, invalid, or disabled API key.
        - 403: caller lacks ``control-plane:service:view`` on the service.
        - 404: service does not exist, is not visible to the caller, or no upgrade window has been configured.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/upgradeWindow"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesUpgradeWindowResponse],
            error_mapper=upgrade_window_get_error_mapper,
            request_options=request_options,
        )

    def upgrade_window_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: UpgradeWindowPutRequest | UpgradeWindowPutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesUpgradeWindowResponse, UpgradeWindowUpdateErrorBody]:
        """Creates or fully replaces the upgrade window for a service. The upgrade window currently lasts 6 hours from
        ``startHourUtc``. The upgrade window can only be set on primary services; secondary services inherit the primary
        service window.

        Errors:
        - 400: invalid field values (``weekday`` not in 0–6, ``startHourUtc`` not in {0, 6, 12, 18}), or the service is
            a secondary service.
        - 401: missing, invalid, or disabled API key.
        - 403: caller lacks ``control-plane:service:manage`` on the service, or the organization does not have the
            scheduled upgrades feature enabled.
        - 404: service does not exist or is not visible to the caller.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/upgradeWindow"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpgradeWindowPutRequest | UpgradeWindowPutRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesUpgradeWindowResponse],
            error_mapper=upgrade_window_update_error_mapper,
            request_options=request_options,
        )


class AsyncServiceApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def instance_create(
        self,
        organization_id: UUID,
        *,
        body: ServicePostRequest | ServicePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesResponse1, InstanceCreateErrorBody]:
        """Creates a new service in the organization, and returns the current service state and a password to access the
        service. The service is started asynchronously.

        Args:
            organization_id: ID of the organization that will own the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/services"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServicePostRequest | ServicePostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesResponse1],
            error_mapper=instance_create_error_mapper,
            request_options=request_options,
        )

    async def instance_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesResponse4, InstanceDeleteErrorBody]:
        """Deletes the service. The service must be in stopped state and is deleted asynchronously after this method
        call.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesResponse4],
            error_mapper=instance_delete_error_mapper,
            request_options=request_options,
        )

    async def instance_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesResponse2, InstanceGetErrorBody]:
        """Returns a service that belongs to the organization

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesResponse2],
            error_mapper=instance_get_error_mapper,
            request_options=request_options,
        )

    async def instance_get_list(
        self,
        organization_id: UUID,
        *,
        filter: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesResponse, InstanceGetListErrorBody]:
        """Returns a list of all services in the organization.

        Args:
            organization_id: ID of the requested organization.
            filter: Filter criteria to apply when retrieving the resource. Currently, only filtering by resource tags is
                supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[list[str] | None]("filter", filter)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesResponse],
            error_mapper=instance_get_list_error_mapper,
            request_options=request_options,
        )

    async def instance_password_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServicePasswordPatchRequest | ServicePasswordPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesPasswordResponse, InstancePasswordUpdateErrorBody]:
        """Sets a new password for the service

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update password.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/password"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServicePasswordPatchRequest | ServicePasswordPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesPasswordResponse],
            error_mapper=instance_password_update_error_mapper,
            request_options=request_options,
        )

    async def instance_private_endpoint_config_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesPrivateEndpointConfigResponse, InstancePrivateEndpointConfigGetErrorBody]:
        """Information required to set up a private endpoint

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/privateEndpointConfig"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesPrivateEndpointConfigResponse],
            error_mapper=instance_private_endpoint_config_get_error_mapper,
            request_options=request_options,
        )

    async def instance_private_endpoint_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServicPrivateEndpointePostRequest | ServicPrivateEndpointePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesPrivateEndpointResponse, InstancePrivateEndpointCreateErrorBody]:
        """Create a new private endpoint. The private endpoint will be associated with this service and organization

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/privateEndpoint"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServicPrivateEndpointePostRequest | ServicPrivateEndpointePostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesPrivateEndpointResponse],
            error_mapper=instance_private_endpoint_create_error_mapper,
            request_options=request_options,
        )

    async def instance_query_endpoint_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesServiceQueryEndpointResponse1, InstanceQueryEndpointDeleteErrorBody]:
        """Removes the service query endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/serviceQueryEndpoint"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesServiceQueryEndpointResponse1],
            error_mapper=instance_query_endpoint_delete_error_mapper,
            request_options=request_options,
        )

    async def instance_query_endpoint_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesServiceQueryEndpointResponse, InstanceQueryEndpointGetErrorBody]:
        """Get the configuration for the service query endpoint that allows executing queries via API.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/serviceQueryEndpoint"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesServiceQueryEndpointResponse],
            error_mapper=instance_query_endpoint_get_error_mapper,
            request_options=request_options,
        )

    async def instance_query_endpoint_upsert(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: (
            InstanceServiceQueryApiEndpointsPostRequest | InstanceServiceQueryApiEndpointsPostRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesServiceQueryEndpointResponse, InstanceQueryEndpointUpsertErrorBody]:
        """Create the service query endpoint that allows executing queries via API.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/serviceQueryEndpoint"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                InstanceServiceQueryApiEndpointsPostRequest | InstanceServiceQueryApiEndpointsPostRequestDict | None
            ](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesServiceQueryEndpointResponse],
            error_mapper=instance_query_endpoint_upsert_error_mapper,
            request_options=request_options,
        )

    async def instance_replica_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceReplicaScalingPatchRequest | ServiceReplicaScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesReplicaScalingResponse, InstanceReplicaScalingUpdateErrorBody]:
        """Updates minimum and maximum memory limits per replica and idle mode scaling behavior for the service.
        Supports both vertical autoscaling (fixed replica count, variable memory) and horizontal autoscaling (variable
        replica count, fixed memory). The memory settings are available only for "production" services and must be a
        multiple of 4 starting from 8GB. For vertical autoscaling, please contact support to enable adjustment of
        numReplicas. For horizontal autoscaling (autoscalingMode "horizontal" with minReplicas/maxReplicas), contact
        support to enable the feature for your organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update scaling parameters.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/replicaScaling"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServiceReplicaScalingPatchRequest | ServiceReplicaScalingPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesReplicaScalingResponse],
            error_mapper=instance_replica_scaling_update_error_mapper,
            request_options=request_options,
        )

    async def instance_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceScalingPatchRequest | ServiceScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesScalingResponse, InstanceScalingUpdateErrorBody]:
        """Updates minimum and maximum total memory limits and idle mode scaling behavior for the service. The memory
        settings are available only for "production" services and must be a multiple of 12 starting from 24GB. Please
        contact support to enable adjustment of numReplicas.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update scaling parameters.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/scaling"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServiceScalingPatchRequest | ServiceScalingPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesScalingResponse],
            error_mapper=instance_scaling_update_error_mapper,
            request_options=request_options,
        )

    async def instance_state_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceStatePatchRequest | ServiceStatePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesStateResponse, InstanceStateUpdateErrorBody]:
        """Starts, stops, or wakes a service. The ``start`` and ``stop`` commands require the
        ``control-plane:service:manage`` permission on the service. The ``awake`` command requires only
        ``control-plane:service:view`` and applies to an idle service; it does not start a stopped service.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update state.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/state"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServiceStatePatchRequest | ServiceStatePatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesStateResponse],
            error_mapper=instance_state_update_error_mapper,
            request_options=request_options,
        )

    async def instance_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServicePatchRequest | ServicePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesResponse2, InstanceUpdateErrorBody]:
        """Updates basic service details like service name or IP access list.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServicePatchRequest | ServicePatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesResponse2],
            error_mapper=instance_update_error_mapper,
            request_options=request_options,
        )

    async def scaling_schedule_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesScalingScheduleResponse2, ScalingScheduleDeleteErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes the
        autoscaling schedule for a service. If a schedule entry is currently active, the base scaling config is restored
        to the instance before the schedule is removed. Returns 404 if no schedule exists. Requires the scheduled
        autoscaling feature to be enabled for the organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/scalingSchedule"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesScalingScheduleResponse2],
            error_mapper=scaling_schedule_delete_error_mapper,
            request_options=request_options,
        )

    async def scaling_schedule_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesScalingScheduleResponse, ScalingScheduleGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the
        autoscaling schedule for a service. Returns 404 if no schedule has been configured or if the schedule was
        cleared. Requires the scheduled autoscaling feature to be enabled for the organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/scalingSchedule"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesScalingScheduleResponse],
            error_mapper=scaling_schedule_get_error_mapper,
            request_options=request_options,
        )

    async def scaling_schedule_upsert(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ScalingSchedulePostRequest | ScalingSchedulePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesScalingScheduleResponse, ScalingScheduleUpsertErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates or fully
        replaces the autoscaling schedule for a service. Pass an empty ``entries`` array to clear the schedule — a
        subsequent GET will return 404, and the response will contain an empty ``baseConfig`` (all fields absent). The
        base scaling config (applied when no entry is active) is managed separately via the ``replicaScaling`` endpoint.
        Requires the scheduled autoscaling feature to be enabled for the organization.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/scalingSchedule"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScalingSchedulePostRequest | ScalingSchedulePostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesScalingScheduleResponse],
            error_mapper=scaling_schedule_upsert_error_mapper,
            request_options=request_options,
        )

    async def service_clickhouse_setting_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        setting_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickhouseSettingsSettingNameResponse1, ServiceClickhouseSettingDeleteErrorBody
    ]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Removes a
        previously-configured ClickHouse setting, reverting its effective value to the platform default. Settings under
        ``spec.extraConfig.server.*`` (e.g. ``keep_alive_timeout``,
        ``shared_merge_tree_disable_merges_and_mutations_assignment``) trigger a ClickHouse server rollout restart;
        other settings propagate to all replicas after a short delay. Deleting a setting that was never configured is a
        no-op (200 OK).

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            setting_name: Name of the setting to reset.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings/{settingName}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("settingName", setting_name),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickhouseSettingsSettingNameResponse1],
            error_mapper=service_clickhouse_setting_delete_error_mapper,
            request_options=request_options,
        )

    async def service_clickhouse_setting_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        setting_name: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickhouseSettingsSettingNameResponse, ServiceClickhouseSettingGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current
        value of a ClickHouse setting for the service. Use the `schema endpoint
        <#tag/Service/operation/serviceClickhouseSettingsSchemaGet>`__ to discover which settings are configurable.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            setting_name: Name of the setting to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings/{settingName}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("settingName", setting_name),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickhouseSettingsSettingNameResponse],
            error_mapper=service_clickhouse_setting_get_error_mapper,
            request_options=request_options,
        )

    async def service_clickhouse_settings_list_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickhouseSettingsResponse, ServiceClickhouseSettingsListGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the
        configured ClickHouse settings for the service. Only settings that have been explicitly set are included.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickhouseSettingsResponse],
            error_mapper=service_clickhouse_settings_list_get_error_mapper,
            request_options=request_options,
        )

    async def service_clickhouse_settings_schema_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        V1OrganizationsServicesClickhouseSettingsSchemaResponse, ServiceClickhouseSettingsSchemaGetErrorBody
    ]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the schema
        of all configurable ClickHouse settings, including types, valid values, descriptions, and warnings.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings/schema"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickhouseSettingsSchemaResponse],
            error_mapper=service_clickhouse_settings_schema_get_error_mapper,
            request_options=request_options,
        )

    async def service_clickhouse_settings_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ServiceClickhouseSettingsPatchRequest | ServiceClickhouseSettingsPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickhouseSettingsResponse1, ServiceClickhouseSettingsUpdateErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Updates one or more
        ClickHouse settings for the service. To reset a setting to its platform default, use the `DELETE single setting
        <#tag/Service/operation/serviceClickhouseSettingDelete>`__ endpoint. Use the `schema endpoint
        <#tag/Service/operation/serviceClickhouseSettingsSchemaGet>`__ to discover which settings are configurable.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ServiceClickhouseSettingsPatchRequest | ServiceClickhouseSettingsPatchRequestDict | None](
                body
            ),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickhouseSettingsResponse1],
            error_mapper=service_clickhouse_settings_update_error_mapper,
            request_options=request_options,
        )

    async def service_profiles_list(
        self,
        organization_id: UUID,
        *,
        region_id: str | None = None,
        byoc_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServiceProfilesResponse, ServiceProfilesListErrorBody]:
        """Returns the custom instance profiles the organization can use in a region. Pass byoc_id to list the profiles
        configured for a BYOC infrastructure; the region is then taken from the infrastructure and region_id may be
        omitted. The list is empty when the organization tier does not include custom hardware profiles.

        Args:
            organization_id: ID of the organization to list available profiles for.
            region_id: Region to list profiles for, e.g. us-east-1. Required unless byoc_id is set; when both are set it
                must match the BYOC infrastructure's region.
            byoc_id: ID of the BYOC infrastructure to list profiles for. BYOC profiles are only returned when this is
                set.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/serviceProfiles"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[str | None]("region_id", region_id), param[UUID | None]("byoc_id", byoc_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServiceProfilesResponse],
            error_mapper=service_profiles_list_error_mapper,
            request_options=request_options,
        )

    async def upgrade_window_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesUpgradeWindowResponse2, UpgradeWindowDeleteErrorBody]:
        """Deletes the upgrade window for a service, restoring the default scheduling behaviour. The upgrade window can
        only be deleted on primary services. Deletion succeeds even if the organization has lost the scheduled upgrades
        entitlement, so a window can be cleared after entitlement loss.

        Errors:
        - 400: the service is a secondary service.
        - 401: missing, invalid, or disabled API key.
        - 403: caller lacks ``control-plane:service:manage`` on the service.
        - 404: service does not exist, is not visible to the caller, or no upgrade window is configured.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/upgradeWindow"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesUpgradeWindowResponse2],
            error_mapper=upgrade_window_delete_error_mapper,
            request_options=request_options,
        )

    async def upgrade_window_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesUpgradeWindowResponse, UpgradeWindowGetErrorBody]:
        """Returns the configured upgrade window for a service.

        Errors:
        - 401: missing, invalid, or disabled API key.
        - 403: caller lacks ``control-plane:service:view`` on the service.
        - 404: service does not exist, is not visible to the caller, or no upgrade window has been configured.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/upgradeWindow"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesUpgradeWindowResponse],
            error_mapper=upgrade_window_get_error_mapper,
            request_options=request_options,
        )

    async def upgrade_window_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: UpgradeWindowPutRequest | UpgradeWindowPutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesUpgradeWindowResponse, UpgradeWindowUpdateErrorBody]:
        """Creates or fully replaces the upgrade window for a service. The upgrade window currently lasts 6 hours from
        ``startHourUtc``. The upgrade window can only be set on primary services; secondary services inherit the primary
        service window.

        Errors:
        - 400: invalid field values (``weekday`` not in 0–6, ``startHourUtc`` not in {0, 6, 12, 18}), or the service is
            a secondary service.
        - 401: missing, invalid, or disabled API key.
        - 403: caller lacks ``control-plane:service:manage`` on the service, or the organization does not have the
            scheduled upgrades feature enabled.
        - 404: service does not exist or is not visible to the caller.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/upgradeWindow"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpgradeWindowPutRequest | UpgradeWindowPutRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesUpgradeWindowResponse],
            error_mapper=upgrade_window_update_error_mapper,
            request_options=request_options,
        )
