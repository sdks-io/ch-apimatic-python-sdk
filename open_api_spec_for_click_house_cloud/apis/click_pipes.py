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
from ..errors.click_pipe_cdc_scaling_get_error import (
    ClickPipeCdcScalingGetErrorBody,
    click_pipe_cdc_scaling_get_error_mapper,
)
from ..errors.click_pipe_cdc_scaling_update_error import (
    ClickPipeCdcScalingUpdateErrorBody,
    click_pipe_cdc_scaling_update_error_mapper,
)
from ..errors.click_pipe_create_error import ClickPipeCreateErrorBody, click_pipe_create_error_mapper
from ..errors.click_pipe_delete_error import ClickPipeDeleteErrorBody, click_pipe_delete_error_mapper
from ..errors.click_pipe_get_error import ClickPipeGetErrorBody, click_pipe_get_error_mapper
from ..errors.click_pipe_get_list_error import ClickPipeGetListErrorBody, click_pipe_get_list_error_mapper
from ..errors.click_pipe_reverse_private_endpoint_create_error import (
    ClickPipeReversePrivateEndpointCreateErrorBody,
    click_pipe_reverse_private_endpoint_create_error_mapper,
)
from ..errors.click_pipe_reverse_private_endpoint_delete_error import (
    ClickPipeReversePrivateEndpointDeleteErrorBody,
    click_pipe_reverse_private_endpoint_delete_error_mapper,
)
from ..errors.click_pipe_reverse_private_endpoint_get_error import (
    ClickPipeReversePrivateEndpointGetErrorBody,
    click_pipe_reverse_private_endpoint_get_error_mapper,
)
from ..errors.click_pipe_reverse_private_endpoint_get_list_error import (
    ClickPipeReversePrivateEndpointGetListErrorBody,
    click_pipe_reverse_private_endpoint_get_list_error_mapper,
)
from ..errors.click_pipe_reverse_private_endpoint_update_error import (
    ClickPipeReversePrivateEndpointUpdateErrorBody,
    click_pipe_reverse_private_endpoint_update_error_mapper,
)
from ..errors.click_pipe_scaling_update_error import (
    ClickPipeScalingUpdateErrorBody,
    click_pipe_scaling_update_error_mapper,
)
from ..errors.click_pipe_schema_discovery_error import (
    ClickPipeSchemaDiscoveryErrorBody,
    click_pipe_schema_discovery_error_mapper,
)
from ..errors.click_pipe_settings_get_error import ClickPipeSettingsGetErrorBody, click_pipe_settings_get_error_mapper
from ..errors.click_pipe_settings_update_error import (
    ClickPipeSettingsUpdateErrorBody,
    click_pipe_settings_update_error_mapper,
)
from ..errors.click_pipe_state_update_error import ClickPipeStateUpdateErrorBody, click_pipe_state_update_error_mapper
from ..errors.click_pipe_update_error import ClickPipeUpdateErrorBody, click_pipe_update_error_mapper
from ..errors.click_pipes_service_context_get_error import (
    ClickPipesServiceContextGetErrorBody,
    click_pipes_service_context_get_error_mapper,
)
from ..models.click_pipe_patch_request import ClickPipePatchRequest, ClickPipePatchRequestDict
from ..models.click_pipe_post_request import ClickPipePostRequest, ClickPipePostRequestDict
from ..models.click_pipe_scaling_patch_request import ClickPipeScalingPatchRequest, ClickPipeScalingPatchRequestDict
from ..models.click_pipe_schema_discovery_request import (
    ClickPipeSchemaDiscoveryRequest,
    ClickPipeSchemaDiscoveryRequestDict,
)
from ..models.click_pipe_settings_put_request import ClickPipeSettingsPutRequest, ClickPipeSettingsPutRequestDict
from ..models.click_pipe_state_patch_request import ClickPipeStatePatchRequest, ClickPipeStatePatchRequestDict
from ..models.click_pipes_cdc_scaling_patch_request import (
    ClickPipesCdcScalingPatchRequest,
    ClickPipesCdcScalingPatchRequestDict,
)
from ..models.create_reverse_private_endpoint import CreateReversePrivateEndpoint, CreateReversePrivateEndpointDict
from ..models.update_reverse_private_endpoint import UpdateReversePrivateEndpoint, UpdateReversePrivateEndpointDict
from ..models.v1_organizations_services_clickpipes_cdc_scaling_response import (
    V1OrganizationsServicesClickpipesCdcScalingResponse,
)
from ..models.v1_organizations_services_clickpipes_click_pipe_id_response import (
    V1OrganizationsServicesClickpipesClickPipeIdResponse,
)
from ..models.v1_organizations_services_clickpipes_click_pipe_id_response2 import (
    V1OrganizationsServicesClickpipesClickPipeIdResponse2,
)
from ..models.v1_organizations_services_clickpipes_click_pipe_id_scaling_response import (
    V1OrganizationsServicesClickpipesClickPipeIdScalingResponse,
)
from ..models.v1_organizations_services_clickpipes_click_pipe_id_settings_response import (
    V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse,
)
from ..models.v1_organizations_services_clickpipes_click_pipe_id_state_response import (
    V1OrganizationsServicesClickpipesClickPipeIdStateResponse,
)
from ..models.v1_organizations_services_clickpipes_context_response import (
    V1OrganizationsServicesClickpipesContextResponse,
)
from ..models.v1_organizations_services_clickpipes_response import V1OrganizationsServicesClickpipesResponse
from ..models.v1_organizations_services_clickpipes_response1 import V1OrganizationsServicesClickpipesResponse1
from ..models.v1_organizations_services_clickpipes_reverse_private_endpoints_response import (
    V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse,
)
from ..models.v1_organizations_services_clickpipes_reverse_private_endpoints_response1 import (
    V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1,
)
from ..models.v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response import (
    V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse,
)
from ..models.v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response1 import (
    V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1,
)
from ..models.v1_organizations_services_clickpipes_schema_discovery_response import (
    V1OrganizationsServicesClickpipesSchemaDiscoveryResponse,
)
from ..server.server import Server


class ClickPipes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ClickPipesWithRawResponse(client, server, auth)

    def click_pipe_cdc_scaling_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickpipesCdcScalingResponse:
        """Get scaling settings for database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery).

        The infrastructure is shared between all database ClickPipes in the service, both for initial load and CDC. For
        billing purposes, 2 CPU cores and 8 GB of RAM `correspond
        <https://clickhouse.com/docs/cloud/manage/billing/overview#clickpipes-for-postgres-cdc>`__ to one compute unit.

        **Note:** For Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob), see `Get ClickPipe
        <#tag/ClickPipes/operation/clickPipeGet>`__.

        **This endpoint becomes available once at least one database ClickPipe was provisioned.**

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesCdcScaling400Error1 |
                V1OrganizationsServicesClickpipesCdcScaling500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_cdc_scaling_get(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def click_pipe_cdc_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickPipesCdcScalingPatchRequest | ClickPipesCdcScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesCdcScalingResponse:
        """Update scaling settings for database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery).

        The infrastructure is shared between all database ClickPipes in the service, both for initial load and CDC.
        Scaling settings may take a few minutes to fully propagate.

        For billing purposes, 2 CPU cores and 8 GB of RAM `correspond
        <https://clickhouse.com/docs/cloud/manage/billing/overview#clickpipes-for-postgres-cdc>`__ to one compute unit.
        If your organization tier changes, database ClickPipes will be `rescaled
        <https://clickhouse.com/docs/cloud/manage/billing/overview#compute>`__ appropriately.

        **Note:** For Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob), see `Get ClickPipe
        <#tag/ClickPipes/operation/clickPipeGet>`__.

        **This endpoint becomes available once at least one database ClickPipe was provisioned.**

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesCdcScaling400Error1 |
                V1OrganizationsServicesClickpipesCdcScaling500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_cdc_scaling_update(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def click_pipe_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickPipePostRequest | ClickPipePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesResponse1:
        """Create a new ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to create the ClickPipe for.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipes400Error1 |
                V1OrganizationsServicesClickpipes500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_create(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def click_pipe_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdResponse2:
        """Delete the specified ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesClickPipeId400Error1 |
                V1OrganizationsServicesClickpipesClickPipeId500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_delete(
            organization_id, service_id, click_pipe_id, request_options=request_options
        ).unwrap()

    def click_pipe_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdResponse:
        """Returns the specified ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the requested ClickPipe.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesClickPipeId400Error1 |
                V1OrganizationsServicesClickpipesClickPipeId500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_get(
            organization_id, service_id, click_pipe_id, request_options=request_options
        ).unwrap()

    def click_pipe_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickpipesResponse:
        """Returns a list of ClickPipes.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipes400Error1 |
                V1OrganizationsServicesClickpipes500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_get_list(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def click_pipe_reverse_private_endpoint_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: CreateReversePrivateEndpoint | CreateReversePrivateEndpointDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1:
        """Create a new reverse private endpoint.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1 |
                V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_reverse_private_endpoint_create(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def click_pipe_reverse_private_endpoint_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        reverse_private_endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1:
        """Delete the reverse private endpoint with the specified ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            reverse_private_endpoint_id: ID of the reverse private endpoint to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1 |
                V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1 |
                RawError``."""
        return self._with_raw_response.click_pipe_reverse_private_endpoint_delete(
            organization_id, service_id, reverse_private_endpoint_id, request_options=request_options
        ).unwrap()

    def click_pipe_reverse_private_endpoint_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        reverse_private_endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse:
        """Returns the reverse private endpoint with the specified ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            reverse_private_endpoint_id: ID of the reverse private endpoint to get.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1 |
                V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1 |
                RawError``."""
        return self._with_raw_response.click_pipe_reverse_private_endpoint_get(
            organization_id, service_id, reverse_private_endpoint_id, request_options=request_options
        ).unwrap()

    def click_pipe_reverse_private_endpoint_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse:
        """Returns a list of reverse private endpoints for the specified service.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1 |
                V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_reverse_private_endpoint_get_list(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def click_pipe_reverse_private_endpoint_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        reverse_private_endpoint_id: UUID,
        *,
        body: UpdateReversePrivateEndpoint | UpdateReversePrivateEndpointDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse:
        """Update mutable fields for an existing reverse private endpoint. customPrivateDnsMappings is a full
        replacement list. Use an empty array to clear mappings.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            reverse_private_endpoint_id: ID of the reverse private endpoint to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1 |
                V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1 |
                RawError``."""
        return self._with_raw_response.click_pipe_reverse_private_endpoint_update(
            organization_id, service_id, reverse_private_endpoint_id, body=body, request_options=request_options
        ).unwrap()

    def click_pipe_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipeScalingPatchRequest | ClickPipeScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdScalingResponse:
        """Change scaling settings for the specified ClickPipe. This endpoint supports Kafka, Kinesis, and object
        storage pipes (S3, GCS, Azure Blob).

        **Note:** For database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery), use the `Update CDC ClickPipes scaling
        <#tag/ClickPipes/operation/clickPipeCdcScalingUpdate>`__ endpoint instead.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to update scaling settings.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesClickPipeIdScaling400Error1 |
                V1OrganizationsServicesClickpipesClickPipeIdScaling500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_scaling_update(
            organization_id, service_id, click_pipe_id, body=body, request_options=request_options
        ).unwrap()

    def click_pipe_schema_discovery(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickPipeSchemaDiscoveryRequest | ClickPipeSchemaDiscoveryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesSchemaDiscoveryResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Infers the schema (field names and ClickHouse data types) of a ClickPipe source without creating a
        pipe. Supported for Kafka, Kinesis, Pub/Sub, and object storage sources. Object storage inference runs on the
        destination service, which must be running.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to run schema discovery against.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesSchemaDiscovery400Error1 |
                V1OrganizationsServicesClickpipesSchemaDiscovery500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_schema_discovery(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def click_pipe_settings_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse:
        """Returns the advanced settings for the specified ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to get settings for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1 |
                V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_settings_get(
            organization_id, service_id, click_pipe_id, request_options=request_options
        ).unwrap()

    def click_pipe_settings_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipeSettingsPutRequest | ClickPipeSettingsPutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse:
        """Update the advanced settings for the specified ClickPipe. Send key-value pairs where values can be strings,
        numbers, or booleans.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to update settings for.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1 |
                V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_settings_update(
            organization_id, service_id, click_pipe_id, body=body, request_options=request_options
        ).unwrap()

    def click_pipe_state_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipeStatePatchRequest | ClickPipeStatePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdStateResponse:
        """Start, stop or resync ClickPipe. Stopping a ClickPipe will stop the ingestion process from any state.
        Starting is allowed for ClickPipes in the "Stopped" state or with a "Failed" state. Resyncing is only for
        Postgres and MySQL pipes and can be done from any state.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to update state.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesClickPipeIdState400Error1
                | V1OrganizationsServicesClickpipesClickPipeIdState500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_state_update(
            organization_id, service_id, click_pipe_id, body=body, request_options=request_options
        ).unwrap()

    def click_pipe_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipePatchRequest | ClickPipePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdResponse:
        """Update the specified ClickPipe. Source fields not present in the per-source update schemas are immutable
        after creation. For Kafka sources, values submitted for immutable fields (type, format, brokers, topics,
        consumerGroup, offset, schemaRegistry, exactlyOnce) are not applied, except schema registry credentials, which
        are rejected.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to create the ClickPipe for.
            click_pipe_id: ID of the requested ClickPipe.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesClickPipeId400Error1 |
                V1OrganizationsServicesClickpipesClickPipeId500Error1 | RawError``."""
        return self._with_raw_response.click_pipe_update(
            organization_id, service_id, click_pipe_id, body=body, request_options=request_options
        ).unwrap()

    def click_pipes_service_context_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickpipesContextResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns service-level ClickPipes capabilities and Private Preview workload identity context, including
        the GCP service account to grant access to customer source resources.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to get ClickPipes context for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesContext400Error1 |
                V1OrganizationsServicesClickpipesContext500Error1 | RawError``."""
        return self._with_raw_response.click_pipes_service_context_get(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ClickPipesWithRawResponse:
        return self._with_raw_response


class AsyncClickPipes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncClickPipesWithRawResponse(client, server, auth)

    async def click_pipe_cdc_scaling_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickpipesCdcScalingResponse:
        """Get scaling settings for database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery).

        The infrastructure is shared between all database ClickPipes in the service, both for initial load and CDC. For
        billing purposes, 2 CPU cores and 8 GB of RAM `correspond
        <https://clickhouse.com/docs/cloud/manage/billing/overview#clickpipes-for-postgres-cdc>`__ to one compute unit.

        **Note:** For Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob), see `Get ClickPipe
        <#tag/ClickPipes/operation/clickPipeGet>`__.

        **This endpoint becomes available once at least one database ClickPipe was provisioned.**

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesCdcScaling400Error1 |
                V1OrganizationsServicesClickpipesCdcScaling500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_cdc_scaling_get(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_cdc_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickPipesCdcScalingPatchRequest | ClickPipesCdcScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesCdcScalingResponse:
        """Update scaling settings for database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery).

        The infrastructure is shared between all database ClickPipes in the service, both for initial load and CDC.
        Scaling settings may take a few minutes to fully propagate.

        For billing purposes, 2 CPU cores and 8 GB of RAM `correspond
        <https://clickhouse.com/docs/cloud/manage/billing/overview#clickpipes-for-postgres-cdc>`__ to one compute unit.
        If your organization tier changes, database ClickPipes will be `rescaled
        <https://clickhouse.com/docs/cloud/manage/billing/overview#compute>`__ appropriately.

        **Note:** For Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob), see `Get ClickPipe
        <#tag/ClickPipes/operation/clickPipeGet>`__.

        **This endpoint becomes available once at least one database ClickPipe was provisioned.**

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesCdcScaling400Error1 |
                V1OrganizationsServicesClickpipesCdcScaling500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_cdc_scaling_update(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickPipePostRequest | ClickPipePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesResponse1:
        """Create a new ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to create the ClickPipe for.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipes400Error1 |
                V1OrganizationsServicesClickpipes500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_create(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdResponse2:
        """Delete the specified ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesClickPipeId400Error1 |
                V1OrganizationsServicesClickpipesClickPipeId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_delete(
                organization_id, service_id, click_pipe_id, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdResponse:
        """Returns the specified ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the requested ClickPipe.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesClickPipeId400Error1 |
                V1OrganizationsServicesClickpipesClickPipeId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_get(
                organization_id, service_id, click_pipe_id, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickpipesResponse:
        """Returns a list of ClickPipes.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipes400Error1 |
                V1OrganizationsServicesClickpipes500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_get_list(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_reverse_private_endpoint_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: CreateReversePrivateEndpoint | CreateReversePrivateEndpointDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1:
        """Create a new reverse private endpoint.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1 |
                V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_reverse_private_endpoint_create(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_reverse_private_endpoint_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        reverse_private_endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1:
        """Delete the reverse private endpoint with the specified ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            reverse_private_endpoint_id: ID of the reverse private endpoint to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1 |
                V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1 |
                RawError``."""
        return (
            await self._with_raw_response.click_pipe_reverse_private_endpoint_delete(
                organization_id, service_id, reverse_private_endpoint_id, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_reverse_private_endpoint_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        reverse_private_endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse:
        """Returns the reverse private endpoint with the specified ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            reverse_private_endpoint_id: ID of the reverse private endpoint to get.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1 |
                V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1 |
                RawError``."""
        return (
            await self._with_raw_response.click_pipe_reverse_private_endpoint_get(
                organization_id, service_id, reverse_private_endpoint_id, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_reverse_private_endpoint_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse:
        """Returns a list of reverse private endpoints for the specified service.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1 |
                V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_reverse_private_endpoint_get_list(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_reverse_private_endpoint_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        reverse_private_endpoint_id: UUID,
        *,
        body: UpdateReversePrivateEndpoint | UpdateReversePrivateEndpointDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse:
        """Update mutable fields for an existing reverse private endpoint. customPrivateDnsMappings is a full
        replacement list. Use an empty array to clear mappings.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            reverse_private_endpoint_id: ID of the reverse private endpoint to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1 |
                V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1 |
                RawError``."""
        return (
            await self._with_raw_response.click_pipe_reverse_private_endpoint_update(
                organization_id, service_id, reverse_private_endpoint_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipeScalingPatchRequest | ClickPipeScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdScalingResponse:
        """Change scaling settings for the specified ClickPipe. This endpoint supports Kafka, Kinesis, and object
        storage pipes (S3, GCS, Azure Blob).

        **Note:** For database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery), use the `Update CDC ClickPipes scaling
        <#tag/ClickPipes/operation/clickPipeCdcScalingUpdate>`__ endpoint instead.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to update scaling settings.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesClickPipeIdScaling400Error1 |
                V1OrganizationsServicesClickpipesClickPipeIdScaling500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_scaling_update(
                organization_id, service_id, click_pipe_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_schema_discovery(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickPipeSchemaDiscoveryRequest | ClickPipeSchemaDiscoveryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesSchemaDiscoveryResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Infers the schema (field names and ClickHouse data types) of a ClickPipe source without creating a
        pipe. Supported for Kafka, Kinesis, Pub/Sub, and object storage sources. Object storage inference runs on the
        destination service, which must be running.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to run schema discovery against.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesSchemaDiscovery400Error1 |
                V1OrganizationsServicesClickpipesSchemaDiscovery500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_schema_discovery(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_settings_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse:
        """Returns the advanced settings for the specified ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to get settings for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1 |
                V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_settings_get(
                organization_id, service_id, click_pipe_id, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_settings_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipeSettingsPutRequest | ClickPipeSettingsPutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse:
        """Update the advanced settings for the specified ClickPipe. Send key-value pairs where values can be strings,
        numbers, or booleans.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to update settings for.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1 |
                V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_settings_update(
                organization_id, service_id, click_pipe_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_state_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipeStatePatchRequest | ClickPipeStatePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdStateResponse:
        """Start, stop or resync ClickPipe. Stopping a ClickPipe will stop the ingestion process from any state.
        Starting is allowed for ClickPipes in the "Stopped" state or with a "Failed" state. Resyncing is only for
        Postgres and MySQL pipes and can be done from any state.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to update state.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesClickPipeIdState400Error1
                | V1OrganizationsServicesClickpipesClickPipeIdState500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_state_update(
                organization_id, service_id, click_pipe_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_pipe_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipePatchRequest | ClickPipePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickpipesClickPipeIdResponse:
        """Update the specified ClickPipe. Source fields not present in the per-source update schemas are immutable
        after creation. For Kafka sources, values submitted for immutable fields (type, format, brokers, topics,
        consumerGroup, offset, schemaRegistry, exactlyOnce) are not applied, except schema registry credentials, which
        are rejected.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to create the ClickPipe for.
            click_pipe_id: ID of the requested ClickPipe.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesClickPipeId400Error1 |
                V1OrganizationsServicesClickpipesClickPipeId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipe_update(
                organization_id, service_id, click_pipe_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_pipes_service_context_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickpipesContextResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns service-level ClickPipes capabilities and Private Preview workload identity context, including
        the GCP service account to grant access to customer source resources.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to get ClickPipes context for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickpipesContext400Error1 |
                V1OrganizationsServicesClickpipesContext500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_pipes_service_context_get(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncClickPipesWithRawResponse:
        return self._with_raw_response


class ClickPipesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def click_pipe_cdc_scaling_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickpipesCdcScalingResponse, ClickPipeCdcScalingGetErrorBody]:
        """Get scaling settings for database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery).

        The infrastructure is shared between all database ClickPipes in the service, both for initial load and CDC. For
        billing purposes, 2 CPU cores and 8 GB of RAM `correspond
        <https://clickhouse.com/docs/cloud/manage/billing/overview#clickpipes-for-postgres-cdc>`__ to one compute unit.

        **Note:** For Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob), see `Get ClickPipe
        <#tag/ClickPipes/operation/clickPipeGet>`__.

        **This endpoint becomes available once at least one database ClickPipe was provisioned.**

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesCdcScaling"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesCdcScalingResponse],
            error_mapper=click_pipe_cdc_scaling_get_error_mapper,
            request_options=request_options,
        )

    def click_pipe_cdc_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickPipesCdcScalingPatchRequest | ClickPipesCdcScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesCdcScalingResponse, ClickPipeCdcScalingUpdateErrorBody]:
        """Update scaling settings for database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery).

        The infrastructure is shared between all database ClickPipes in the service, both for initial load and CDC.
        Scaling settings may take a few minutes to fully propagate.

        For billing purposes, 2 CPU cores and 8 GB of RAM `correspond
        <https://clickhouse.com/docs/cloud/manage/billing/overview#clickpipes-for-postgres-cdc>`__ to one compute unit.
        If your organization tier changes, database ClickPipes will be `rescaled
        <https://clickhouse.com/docs/cloud/manage/billing/overview#compute>`__ appropriately.

        **Note:** For Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob), see `Get ClickPipe
        <#tag/ClickPipes/operation/clickPipeGet>`__.

        **This endpoint becomes available once at least one database ClickPipe was provisioned.**

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesCdcScaling"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipesCdcScalingPatchRequest | ClickPipesCdcScalingPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesCdcScalingResponse],
            error_mapper=click_pipe_cdc_scaling_update_error_mapper,
            request_options=request_options,
        )

    def click_pipe_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickPipePostRequest | ClickPipePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesResponse1, ClickPipeCreateErrorBody]:
        """Create a new ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to create the ClickPipe for.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/clickpipes"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipePostRequest | ClickPipePostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesResponse1],
            error_mapper=click_pipe_create_error_mapper,
            request_options=request_options,
        )

    def click_pipe_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdResponse2, ClickPipeDeleteErrorBody]:
        """Delete the specified ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdResponse2],
            error_mapper=click_pipe_delete_error_mapper,
            request_options=request_options,
        )

    def click_pipe_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdResponse, ClickPipeGetErrorBody]:
        """Returns the specified ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the requested ClickPipe.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdResponse],
            error_mapper=click_pipe_get_error_mapper,
            request_options=request_options,
        )

    def click_pipe_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickpipesResponse, ClickPipeGetListErrorBody]:
        """Returns a list of ClickPipes.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/clickpipes"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesResponse],
            error_mapper=click_pipe_get_list_error_mapper,
            request_options=request_options,
        )

    def click_pipe_reverse_private_endpoint_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: CreateReversePrivateEndpoint | CreateReversePrivateEndpointDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1,
        ClickPipeReversePrivateEndpointCreateErrorBody,
    ]:
        """Create a new reverse private endpoint.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateReversePrivateEndpoint | CreateReversePrivateEndpointDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1],
            error_mapper=click_pipe_reverse_private_endpoint_create_error_mapper,
            request_options=request_options,
        )

    def click_pipe_reverse_private_endpoint_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        reverse_private_endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1,
        ClickPipeReversePrivateEndpointDeleteErrorBody,
    ]:
        """Delete the reverse private endpoint with the specified ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            reverse_private_endpoint_id: ID of the reverse private endpoint to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints/{reversePrivateEndpointId}",
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("reversePrivateEndpointId", reverse_private_endpoint_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[
                V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1
            ],
            error_mapper=click_pipe_reverse_private_endpoint_delete_error_mapper,
            request_options=request_options,
        )

    def click_pipe_reverse_private_endpoint_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        reverse_private_endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse,
        ClickPipeReversePrivateEndpointGetErrorBody,
    ]:
        """Returns the reverse private endpoint with the specified ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            reverse_private_endpoint_id: ID of the reverse private endpoint to get.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints/{reversePrivateEndpointId}",
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("reversePrivateEndpointId", reverse_private_endpoint_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[
                V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse
            ],
            error_mapper=click_pipe_reverse_private_endpoint_get_error_mapper,
            request_options=request_options,
        )

    def click_pipe_reverse_private_endpoint_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse,
        ClickPipeReversePrivateEndpointGetListErrorBody,
    ]:
        """Returns a list of reverse private endpoints for the specified service.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse],
            error_mapper=click_pipe_reverse_private_endpoint_get_list_error_mapper,
            request_options=request_options,
        )

    def click_pipe_reverse_private_endpoint_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        reverse_private_endpoint_id: UUID,
        *,
        body: UpdateReversePrivateEndpoint | UpdateReversePrivateEndpointDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse,
        ClickPipeReversePrivateEndpointUpdateErrorBody,
    ]:
        """Update mutable fields for an existing reverse private endpoint. customPrivateDnsMappings is a full
        replacement list. Use an empty array to clear mappings.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            reverse_private_endpoint_id: ID of the reverse private endpoint to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints/{reversePrivateEndpointId}",
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("reversePrivateEndpointId", reverse_private_endpoint_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateReversePrivateEndpoint | UpdateReversePrivateEndpointDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[
                V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse
            ],
            error_mapper=click_pipe_reverse_private_endpoint_update_error_mapper,
            request_options=request_options,
        )

    def click_pipe_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipeScalingPatchRequest | ClickPipeScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdScalingResponse, ClickPipeScalingUpdateErrorBody]:
        """Change scaling settings for the specified ClickPipe. This endpoint supports Kafka, Kinesis, and object
        storage pipes (S3, GCS, Azure Blob).

        **Note:** For database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery), use the `Update CDC ClickPipes scaling
        <#tag/ClickPipes/operation/clickPipeCdcScalingUpdate>`__ endpoint instead.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to update scaling settings.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}/scaling"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipeScalingPatchRequest | ClickPipeScalingPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdScalingResponse],
            error_mapper=click_pipe_scaling_update_error_mapper,
            request_options=request_options,
        )

    def click_pipe_schema_discovery(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickPipeSchemaDiscoveryRequest | ClickPipeSchemaDiscoveryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesSchemaDiscoveryResponse, ClickPipeSchemaDiscoveryErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Infers the schema (field names and ClickHouse data types) of a ClickPipe source without creating a
        pipe. Supported for Kafka, Kinesis, Pub/Sub, and object storage sources. Object storage inference runs on the
        destination service, which must be running.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to run schema discovery against.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/schemaDiscovery"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipeSchemaDiscoveryRequest | ClickPipeSchemaDiscoveryRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesSchemaDiscoveryResponse],
            error_mapper=click_pipe_schema_discovery_error_mapper,
            request_options=request_options,
        )

    def click_pipe_settings_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse, ClickPipeSettingsGetErrorBody]:
        """Returns the advanced settings for the specified ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to get settings for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}/settings"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse],
            error_mapper=click_pipe_settings_get_error_mapper,
            request_options=request_options,
        )

    def click_pipe_settings_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipeSettingsPutRequest | ClickPipeSettingsPutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse, ClickPipeSettingsUpdateErrorBody]:
        """Update the advanced settings for the specified ClickPipe. Send key-value pairs where values can be strings,
        numbers, or booleans.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to update settings for.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}/settings"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipeSettingsPutRequest | ClickPipeSettingsPutRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse],
            error_mapper=click_pipe_settings_update_error_mapper,
            request_options=request_options,
        )

    def click_pipe_state_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipeStatePatchRequest | ClickPipeStatePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdStateResponse, ClickPipeStateUpdateErrorBody]:
        """Start, stop or resync ClickPipe. Stopping a ClickPipe will stop the ingestion process from any state.
        Starting is allowed for ClickPipes in the "Stopped" state or with a "Failed" state. Resyncing is only for
        Postgres and MySQL pipes and can be done from any state.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to update state.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}/state"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipeStatePatchRequest | ClickPipeStatePatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdStateResponse],
            error_mapper=click_pipe_state_update_error_mapper,
            request_options=request_options,
        )

    def click_pipe_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipePatchRequest | ClickPipePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdResponse, ClickPipeUpdateErrorBody]:
        """Update the specified ClickPipe. Source fields not present in the per-source update schemas are immutable
        after creation. For Kafka sources, values submitted for immutable fields (type, format, brokers, topics,
        consumerGroup, offset, schemaRegistry, exactlyOnce) are not applied, except schema registry credentials, which
        are rejected.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to create the ClickPipe for.
            click_pipe_id: ID of the requested ClickPipe.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipePatchRequest | ClickPipePatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdResponse],
            error_mapper=click_pipe_update_error_mapper,
            request_options=request_options,
        )

    def click_pipes_service_context_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickpipesContextResponse, ClickPipesServiceContextGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns service-level ClickPipes capabilities and Private Preview workload identity context, including
        the GCP service account to grant access to customer source resources.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to get ClickPipes context for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/context"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesContextResponse],
            error_mapper=click_pipes_service_context_get_error_mapper,
            request_options=request_options,
        )


class AsyncClickPipesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def click_pipe_cdc_scaling_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickpipesCdcScalingResponse, ClickPipeCdcScalingGetErrorBody]:
        """Get scaling settings for database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery).

        The infrastructure is shared between all database ClickPipes in the service, both for initial load and CDC. For
        billing purposes, 2 CPU cores and 8 GB of RAM `correspond
        <https://clickhouse.com/docs/cloud/manage/billing/overview#clickpipes-for-postgres-cdc>`__ to one compute unit.

        **Note:** For Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob), see `Get ClickPipe
        <#tag/ClickPipes/operation/clickPipeGet>`__.

        **This endpoint becomes available once at least one database ClickPipe was provisioned.**

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesCdcScaling"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesCdcScalingResponse],
            error_mapper=click_pipe_cdc_scaling_get_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_cdc_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickPipesCdcScalingPatchRequest | ClickPipesCdcScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesCdcScalingResponse, ClickPipeCdcScalingUpdateErrorBody]:
        """Update scaling settings for database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery).

        The infrastructure is shared between all database ClickPipes in the service, both for initial load and CDC.
        Scaling settings may take a few minutes to fully propagate.

        For billing purposes, 2 CPU cores and 8 GB of RAM `correspond
        <https://clickhouse.com/docs/cloud/manage/billing/overview#clickpipes-for-postgres-cdc>`__ to one compute unit.
        If your organization tier changes, database ClickPipes will be `rescaled
        <https://clickhouse.com/docs/cloud/manage/billing/overview#compute>`__ appropriately.

        **Note:** For Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob), see `Get ClickPipe
        <#tag/ClickPipes/operation/clickPipeGet>`__.

        **This endpoint becomes available once at least one database ClickPipe was provisioned.**

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesCdcScaling"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipesCdcScalingPatchRequest | ClickPipesCdcScalingPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesCdcScalingResponse],
            error_mapper=click_pipe_cdc_scaling_update_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickPipePostRequest | ClickPipePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesResponse1, ClickPipeCreateErrorBody]:
        """Create a new ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to create the ClickPipe for.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/clickpipes"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipePostRequest | ClickPipePostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesResponse1],
            error_mapper=click_pipe_create_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdResponse2, ClickPipeDeleteErrorBody]:
        """Delete the specified ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdResponse2],
            error_mapper=click_pipe_delete_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdResponse, ClickPipeGetErrorBody]:
        """Returns the specified ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the requested ClickPipe.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdResponse],
            error_mapper=click_pipe_get_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickpipesResponse, ClickPipeGetListErrorBody]:
        """Returns a list of ClickPipes.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/clickpipes"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesResponse],
            error_mapper=click_pipe_get_list_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_reverse_private_endpoint_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: CreateReversePrivateEndpoint | CreateReversePrivateEndpointDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1,
        ClickPipeReversePrivateEndpointCreateErrorBody,
    ]:
        """Create a new reverse private endpoint.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateReversePrivateEndpoint | CreateReversePrivateEndpointDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1],
            error_mapper=click_pipe_reverse_private_endpoint_create_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_reverse_private_endpoint_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        reverse_private_endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1,
        ClickPipeReversePrivateEndpointDeleteErrorBody,
    ]:
        """Delete the reverse private endpoint with the specified ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            reverse_private_endpoint_id: ID of the reverse private endpoint to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints/{reversePrivateEndpointId}",
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("reversePrivateEndpointId", reverse_private_endpoint_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[
                V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1
            ],
            error_mapper=click_pipe_reverse_private_endpoint_delete_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_reverse_private_endpoint_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        reverse_private_endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse,
        ClickPipeReversePrivateEndpointGetErrorBody,
    ]:
        """Returns the reverse private endpoint with the specified ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            reverse_private_endpoint_id: ID of the reverse private endpoint to get.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints/{reversePrivateEndpointId}",
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("reversePrivateEndpointId", reverse_private_endpoint_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[
                V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse
            ],
            error_mapper=click_pipe_reverse_private_endpoint_get_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_reverse_private_endpoint_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse,
        ClickPipeReversePrivateEndpointGetListErrorBody,
    ]:
        """Returns a list of reverse private endpoints for the specified service.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse],
            error_mapper=click_pipe_reverse_private_endpoint_get_list_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_reverse_private_endpoint_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        reverse_private_endpoint_id: UUID,
        *,
        body: UpdateReversePrivateEndpoint | UpdateReversePrivateEndpointDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse,
        ClickPipeReversePrivateEndpointUpdateErrorBody,
    ]:
        """Update mutable fields for an existing reverse private endpoint. customPrivateDnsMappings is a full
        replacement list. Use an empty array to clear mappings.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the Reverse Private Endpoint.
            reverse_private_endpoint_id: ID of the reverse private endpoint to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints/{reversePrivateEndpointId}",
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("reversePrivateEndpointId", reverse_private_endpoint_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateReversePrivateEndpoint | UpdateReversePrivateEndpointDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[
                V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse
            ],
            error_mapper=click_pipe_reverse_private_endpoint_update_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_scaling_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipeScalingPatchRequest | ClickPipeScalingPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdScalingResponse, ClickPipeScalingUpdateErrorBody]:
        """Change scaling settings for the specified ClickPipe. This endpoint supports Kafka, Kinesis, and object
        storage pipes (S3, GCS, Azure Blob).

        **Note:** For database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery), use the `Update CDC ClickPipes scaling
        <#tag/ClickPipes/operation/clickPipeCdcScalingUpdate>`__ endpoint instead.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to update scaling settings.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}/scaling"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipeScalingPatchRequest | ClickPipeScalingPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdScalingResponse],
            error_mapper=click_pipe_scaling_update_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_schema_discovery(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickPipeSchemaDiscoveryRequest | ClickPipeSchemaDiscoveryRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesSchemaDiscoveryResponse, ClickPipeSchemaDiscoveryErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Infers the schema (field names and ClickHouse data types) of a ClickPipe source without creating a
        pipe. Supported for Kafka, Kinesis, Pub/Sub, and object storage sources. Object storage inference runs on the
        destination service, which must be running.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to run schema discovery against.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/schemaDiscovery"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipeSchemaDiscoveryRequest | ClickPipeSchemaDiscoveryRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesSchemaDiscoveryResponse],
            error_mapper=click_pipe_schema_discovery_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_settings_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse, ClickPipeSettingsGetErrorBody]:
        """Returns the advanced settings for the specified ClickPipe.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to get settings for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}/settings"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse],
            error_mapper=click_pipe_settings_get_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_settings_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipeSettingsPutRequest | ClickPipeSettingsPutRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse, ClickPipeSettingsUpdateErrorBody]:
        """Update the advanced settings for the specified ClickPipe. Send key-value pairs where values can be strings,
        numbers, or booleans.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to update settings for.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}/settings"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipeSettingsPutRequest | ClickPipeSettingsPutRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse],
            error_mapper=click_pipe_settings_update_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_state_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipeStatePatchRequest | ClickPipeStatePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdStateResponse, ClickPipeStateUpdateErrorBody]:
        """Start, stop or resync ClickPipe. Stopping a ClickPipe will stop the ingestion process from any state.
        Starting is allowed for ClickPipes in the "Stopped" state or with a "Failed" state. Resyncing is only for
        Postgres and MySQL pipes and can be done from any state.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service that owns the ClickPipe.
            click_pipe_id: ID of the ClickPipe to update state.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}/state"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipeStatePatchRequest | ClickPipeStatePatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdStateResponse],
            error_mapper=click_pipe_state_update_error_mapper,
            request_options=request_options,
        )

    async def click_pipe_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_pipe_id: UUID,
        *,
        body: ClickPipePatchRequest | ClickPipePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdResponse, ClickPipeUpdateErrorBody]:
        """Update the specified ClickPipe. Source fields not present in the per-source update schemas are immutable
        after creation. For Kafka sources, values submitted for immutable fields (type, format, brokers, topics,
        consumerGroup, offset, schemaRegistry, exactlyOnce) are not applied, except schema registry credentials, which
        are rejected.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to create the ClickPipe for.
            click_pipe_id: ID of the requested ClickPipe.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("clickPipeId", click_pipe_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickPipePatchRequest | ClickPipePatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesClickPipeIdResponse],
            error_mapper=click_pipe_update_error_mapper,
            request_options=request_options,
        )

    async def click_pipes_service_context_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickpipesContextResponse, ClickPipesServiceContextGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns service-level ClickPipes capabilities and Private Preview workload identity context, including
        the GCP service account to grant access to customer source resources.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service to get ClickPipes context for.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickpipes/context"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickpipesContextResponse],
            error_mapper=click_pipes_service_context_get_error_mapper,
            request_options=request_options,
        )
