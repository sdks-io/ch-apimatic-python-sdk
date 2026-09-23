from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.activity_get_error import ActivityGetErrorBody, activity_get_error_mapper
from ..errors.activity_get_list_error import ActivityGetListErrorBody, activity_get_list_error_mapper
from ..errors.organization_byoc_infrastructure_create_error import (
    OrganizationByocInfrastructureCreateErrorBody,
    organization_byoc_infrastructure_create_error_mapper,
)
from ..errors.organization_byoc_infrastructure_delete_error import (
    OrganizationByocInfrastructureDeleteErrorBody,
    organization_byoc_infrastructure_delete_error_mapper,
)
from ..errors.organization_byoc_infrastructure_update_error import (
    OrganizationByocInfrastructureUpdateErrorBody,
    organization_byoc_infrastructure_update_error_mapper,
)
from ..errors.organization_get_error import OrganizationGetErrorBody, organization_get_error_mapper
from ..errors.organization_get_list_error import OrganizationGetListErrorBody, organization_get_list_error_mapper
from ..errors.organization_private_endpoint_config_get_list_error import (
    OrganizationPrivateEndpointConfigGetListErrorBody,
    organization_private_endpoint_config_get_list_error_mapper,
)
from ..errors.organization_quota_get_error import OrganizationQuotaGetErrorBody, organization_quota_get_error_mapper
from ..errors.organization_quotas_get_list_error import (
    OrganizationQuotasGetListErrorBody,
    organization_quotas_get_list_error_mapper,
)
from ..errors.organization_update_error import OrganizationUpdateErrorBody, organization_update_error_mapper
from ..models.byoc_infrastructure_patch_request import (
    ByocInfrastructurePatchRequest,
    ByocInfrastructurePatchRequestDict,
)
from ..models.byoc_infrastructure_post_request import ByocInfrastructurePostRequest, ByocInfrastructurePostRequestDict
from ..models.organization_patch_request import OrganizationPatchRequest, OrganizationPatchRequestDict
from ..models.v1_organizations_activities_response import V1OrganizationsActivitiesResponse
from ..models.v1_organizations_activities_response1 import V1OrganizationsActivitiesResponse1
from ..models.v1_organizations_byoc_infrastructure_response import V1OrganizationsByocInfrastructureResponse
from ..models.v1_organizations_byoc_infrastructure_response1 import V1OrganizationsByocInfrastructureResponse1
from ..models.v1_organizations_private_endpoint_config_response import V1OrganizationsPrivateEndpointConfigResponse
from ..models.v1_organizations_quotas_response import V1OrganizationsQuotasResponse
from ..models.v1_organizations_quotas_response1 import V1OrganizationsQuotasResponse1
from ..models.v1_organizations_response import V1OrganizationsResponse
from ..models.v1_organizations_response1 import V1OrganizationsResponse1
from ..server.server import Server


class OrganizationApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OrganizationApiWithRawResponse(client, server, auth)

    def activity_get(
        self, organization_id: UUID, activity_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsActivitiesResponse1:
        """Returns a single organization activity by ID.

        Args:
            organization_id: ID of the requested organization.
            activity_id: ID of the requested activity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsActivities400Error1 |
                V1OrganizationsActivities500Error1 | RawError``."""
        return self._with_raw_response.activity_get(
            organization_id, activity_id, request_options=request_options
        ).unwrap()

    def activity_get_list(
        self,
        organization_id: UUID,
        *,
        from_date: RFC3339DateTime | None = None,
        to_date: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsActivitiesResponse:
        """Returns a list of all organization activities.

        Args:
            organization_id: ID of the requested organization.
            from_date: A starting date for a search
            to_date: An ending date for a search
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsActivities400Error1 |
                V1OrganizationsActivities500Error1 | RawError``."""
        return self._with_raw_response.activity_get_list(
            organization_id, from_date=from_date, to_date=to_date, request_options=request_options
        ).unwrap()

    def organization_byoc_infrastructure_create(
        self,
        organization_id: UUID,
        *,
        body: ByocInfrastructurePostRequest | ByocInfrastructurePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsByocInfrastructureResponse:
        """Create a new BYOC Infrastructure in the organization. Returns the configuration of the newly created
        infrastructure

        Args:
            organization_id: ID of the requested organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsByocInfrastructure400Error1 |
                V1OrganizationsByocInfrastructure500Error1 | RawError``."""
        return self._with_raw_response.organization_byoc_infrastructure_create(
            organization_id, body=body, request_options=request_options
        ).unwrap()

    def organization_byoc_infrastructure_delete(
        self,
        organization_id: UUID,
        byoc_infrastructure_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsByocInfrastructureResponse1:
        """Removes a BYOC Infrastructure from the organization

        Args:
            organization_id: ID of the requested organization.
            byoc_infrastructure_id: ID of the requested BYOC Infrastructure
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsByocInfrastructure400Error1 |
                V1OrganizationsByocInfrastructure500Error1 | RawError``."""
        return self._with_raw_response.organization_byoc_infrastructure_delete(
            organization_id, byoc_infrastructure_id, request_options=request_options
        ).unwrap()

    def organization_byoc_infrastructure_update(
        self,
        organization_id: UUID,
        byoc_infrastructure_id: UUID,
        *,
        body: ByocInfrastructurePatchRequest | ByocInfrastructurePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsByocInfrastructureResponse:
        """Update configuration of the BYOC infrastructure. Returns the modified infrastructure

        Args:
            organization_id: ID of the requested organization.
            byoc_infrastructure_id: ID of the requested BYOC Infrastructure
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsByocInfrastructure400Error1 |
                V1OrganizationsByocInfrastructure500Error1 | RawError``."""
        return self._with_raw_response.organization_byoc_infrastructure_update(
            organization_id, byoc_infrastructure_id, body=body, request_options=request_options
        ).unwrap()

    def organization_get(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsResponse1:
        """Returns details of a single organization. In order to get the details, the auth key must belong to the
        organization.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1Organizations400Error1 | V1Organizations500Error1 |
                RawError``."""
        return self._with_raw_response.organization_get(organization_id, request_options=request_options).unwrap()

    def organization_get_list(self, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsResponse:
        """Returns a list with a single organization associated with the API key in the request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1Organizations400Error1 | V1Organizations500Error1 |
                RawError``."""
        return self._with_raw_response.organization_get_list(request_options=request_options).unwrap()

    def organization_private_endpoint_config_get_list(
        self,
        organization_id: UUID,
        cloud_provider: str,
        region_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPrivateEndpointConfigResponse:
        """Deprecated. Please follow `documentation
        <https://clickhouse.com/docs/manage/security/aws-privatelink#add-endpoint-id-to-services-allow-list>`__ for the
        updated process.

        Args:
            organization_id: ID of the requested organization.
            cloud_provider: Cloud provider identifier. One of aws, gcp, or azure.
            region_id: Region identifier within specific cloud providers.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPrivateEndpointConfig400Error1 |
                V1OrganizationsPrivateEndpointConfig500Error1 | RawError``."""
        return self._with_raw_response.organization_private_endpoint_config_get_list(
            organization_id, cloud_provider, region_id, request_options=request_options
        ).unwrap()

    def organization_quota_get(
        self, organization_id: UUID, quota_code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsQuotasResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns a single
        organization quota identified by its quota code. Responds with a not found error when the quota code is unknown
        or the quota does not apply to the organization.

        Args:
            organization_id: ID of the requested organization.
            quota_code: Code of the requested quota.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsQuotas400Error1 |
                V1OrganizationsQuotas500Error1 | RawError``."""
        return self._with_raw_response.organization_quota_get(
            organization_id, quota_code, request_options=request_options
        ).unwrap()

    def organization_quotas_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsQuotasResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the
        resource quotas enforced for the organization together with their current usage where available. Quotas that do
        not apply to the organization are omitted. Quota values reflect the limits currently enforced, so they can be
        polled to detect changes, for example after a billing status change. The response contains one entry per quota
        code; quotas enforced per resource may additionally appear under resource-scoped endpoints in the future.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsQuotas400Error1 |
                V1OrganizationsQuotas500Error1 | RawError``."""
        return self._with_raw_response.organization_quotas_get_list(
            organization_id, request_options=request_options
        ).unwrap()

    def organization_update(
        self,
        organization_id: UUID,
        *,
        body: OrganizationPatchRequest | OrganizationPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsResponse1:
        """Updates organization fields. Requires ADMIN auth key role.

        Args:
            organization_id: ID of the organization to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1Organizations400Error1 | V1Organizations500Error1 |
                RawError``."""
        return self._with_raw_response.organization_update(
            organization_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> OrganizationApiWithRawResponse:
        return self._with_raw_response


class AsyncOrganizationApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOrganizationApiWithRawResponse(client, server, auth)

    async def activity_get(
        self, organization_id: UUID, activity_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsActivitiesResponse1:
        """Returns a single organization activity by ID.

        Args:
            organization_id: ID of the requested organization.
            activity_id: ID of the requested activity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsActivities400Error1 |
                V1OrganizationsActivities500Error1 | RawError``."""
        return (
            await self._with_raw_response.activity_get(organization_id, activity_id, request_options=request_options)
        ).unwrap()

    async def activity_get_list(
        self,
        organization_id: UUID,
        *,
        from_date: RFC3339DateTime | None = None,
        to_date: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsActivitiesResponse:
        """Returns a list of all organization activities.

        Args:
            organization_id: ID of the requested organization.
            from_date: A starting date for a search
            to_date: An ending date for a search
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsActivities400Error1 |
                V1OrganizationsActivities500Error1 | RawError``."""
        return (
            await self._with_raw_response.activity_get_list(
                organization_id, from_date=from_date, to_date=to_date, request_options=request_options
            )
        ).unwrap()

    async def organization_byoc_infrastructure_create(
        self,
        organization_id: UUID,
        *,
        body: ByocInfrastructurePostRequest | ByocInfrastructurePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsByocInfrastructureResponse:
        """Create a new BYOC Infrastructure in the organization. Returns the configuration of the newly created
        infrastructure

        Args:
            organization_id: ID of the requested organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsByocInfrastructure400Error1 |
                V1OrganizationsByocInfrastructure500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_byoc_infrastructure_create(
                organization_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def organization_byoc_infrastructure_delete(
        self,
        organization_id: UUID,
        byoc_infrastructure_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsByocInfrastructureResponse1:
        """Removes a BYOC Infrastructure from the organization

        Args:
            organization_id: ID of the requested organization.
            byoc_infrastructure_id: ID of the requested BYOC Infrastructure
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsByocInfrastructure400Error1 |
                V1OrganizationsByocInfrastructure500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_byoc_infrastructure_delete(
                organization_id, byoc_infrastructure_id, request_options=request_options
            )
        ).unwrap()

    async def organization_byoc_infrastructure_update(
        self,
        organization_id: UUID,
        byoc_infrastructure_id: UUID,
        *,
        body: ByocInfrastructurePatchRequest | ByocInfrastructurePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsByocInfrastructureResponse:
        """Update configuration of the BYOC infrastructure. Returns the modified infrastructure

        Args:
            organization_id: ID of the requested organization.
            byoc_infrastructure_id: ID of the requested BYOC Infrastructure
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsByocInfrastructure400Error1 |
                V1OrganizationsByocInfrastructure500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_byoc_infrastructure_update(
                organization_id, byoc_infrastructure_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def organization_get(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsResponse1:
        """Returns details of a single organization. In order to get the details, the auth key must belong to the
        organization.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1Organizations400Error1 | V1Organizations500Error1 |
                RawError``."""
        return (
            await self._with_raw_response.organization_get(organization_id, request_options=request_options)
        ).unwrap()

    async def organization_get_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsResponse:
        """Returns a list with a single organization associated with the API key in the request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1Organizations400Error1 | V1Organizations500Error1 |
                RawError``."""
        return (await self._with_raw_response.organization_get_list(request_options=request_options)).unwrap()

    async def organization_private_endpoint_config_get_list(
        self,
        organization_id: UUID,
        cloud_provider: str,
        region_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPrivateEndpointConfigResponse:
        """Deprecated. Please follow `documentation
        <https://clickhouse.com/docs/manage/security/aws-privatelink#add-endpoint-id-to-services-allow-list>`__ for the
        updated process.

        Args:
            organization_id: ID of the requested organization.
            cloud_provider: Cloud provider identifier. One of aws, gcp, or azure.
            region_id: Region identifier within specific cloud providers.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPrivateEndpointConfig400Error1 |
                V1OrganizationsPrivateEndpointConfig500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_private_endpoint_config_get_list(
                organization_id, cloud_provider, region_id, request_options=request_options
            )
        ).unwrap()

    async def organization_quota_get(
        self, organization_id: UUID, quota_code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsQuotasResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns a single
        organization quota identified by its quota code. Responds with a not found error when the quota code is unknown
        or the quota does not apply to the organization.

        Args:
            organization_id: ID of the requested organization.
            quota_code: Code of the requested quota.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsQuotas400Error1 |
                V1OrganizationsQuotas500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_quota_get(
                organization_id, quota_code, request_options=request_options
            )
        ).unwrap()

    async def organization_quotas_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsQuotasResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the
        resource quotas enforced for the organization together with their current usage where available. Quotas that do
        not apply to the organization are omitted. Quota values reflect the limits currently enforced, so they can be
        polled to detect changes, for example after a billing status change. The response contains one entry per quota
        code; quotas enforced per resource may additionally appear under resource-scoped endpoints in the future.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsQuotas400Error1 |
                V1OrganizationsQuotas500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_quotas_get_list(organization_id, request_options=request_options)
        ).unwrap()

    async def organization_update(
        self,
        organization_id: UUID,
        *,
        body: OrganizationPatchRequest | OrganizationPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsResponse1:
        """Updates organization fields. Requires ADMIN auth key role.

        Args:
            organization_id: ID of the organization to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1Organizations400Error1 | V1Organizations500Error1 |
                RawError``."""
        return (
            await self._with_raw_response.organization_update(
                organization_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncOrganizationApiWithRawResponse:
        return self._with_raw_response


class OrganizationApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def activity_get(
        self, organization_id: UUID, activity_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsActivitiesResponse1, ActivityGetErrorBody]:
        """Returns a single organization activity by ID.

        Args:
            organization_id: ID of the requested organization.
            activity_id: ID of the requested activity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/activities/{activityId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("activityId", activity_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsActivitiesResponse1],
            error_mapper=activity_get_error_mapper,
            request_options=request_options,
        )

    def activity_get_list(
        self,
        organization_id: UUID,
        *,
        from_date: RFC3339DateTime | None = None,
        to_date: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsActivitiesResponse, ActivityGetListErrorBody]:
        """Returns a list of all organization activities.

        Args:
            organization_id: ID of the requested organization.
            from_date: A starting date for a search
            to_date: An ending date for a search
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/activities"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[
                param[RFC3339DateTime | None]("from_date", from_date), param[RFC3339DateTime | None]("to_date", to_date)
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsActivitiesResponse],
            error_mapper=activity_get_list_error_mapper,
            request_options=request_options,
        )

    def organization_byoc_infrastructure_create(
        self,
        organization_id: UUID,
        *,
        body: ByocInfrastructurePostRequest | ByocInfrastructurePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsByocInfrastructureResponse, OrganizationByocInfrastructureCreateErrorBody]:
        """Create a new BYOC Infrastructure in the organization. Returns the configuration of the newly created
        infrastructure

        Args:
            organization_id: ID of the requested organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/byocInfrastructure"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ByocInfrastructurePostRequest | ByocInfrastructurePostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsByocInfrastructureResponse],
            error_mapper=organization_byoc_infrastructure_create_error_mapper,
            request_options=request_options,
        )

    def organization_byoc_infrastructure_delete(
        self,
        organization_id: UUID,
        byoc_infrastructure_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsByocInfrastructureResponse1, OrganizationByocInfrastructureDeleteErrorBody]:
        """Removes a BYOC Infrastructure from the organization

        Args:
            organization_id: ID of the requested organization.
            byoc_infrastructure_id: ID of the requested BYOC Infrastructure
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/byocInfrastructure/{byocInfrastructureId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("byocInfrastructureId", byoc_infrastructure_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsByocInfrastructureResponse1],
            error_mapper=organization_byoc_infrastructure_delete_error_mapper,
            request_options=request_options,
        )

    def organization_byoc_infrastructure_update(
        self,
        organization_id: UUID,
        byoc_infrastructure_id: UUID,
        *,
        body: ByocInfrastructurePatchRequest | ByocInfrastructurePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsByocInfrastructureResponse, OrganizationByocInfrastructureUpdateErrorBody]:
        """Update configuration of the BYOC infrastructure. Returns the modified infrastructure

        Args:
            organization_id: ID of the requested organization.
            byoc_infrastructure_id: ID of the requested BYOC Infrastructure
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/byocInfrastructure/{byocInfrastructureId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("byocInfrastructureId", byoc_infrastructure_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ByocInfrastructurePatchRequest | ByocInfrastructurePatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsByocInfrastructureResponse],
            error_mapper=organization_byoc_infrastructure_update_error_mapper,
            request_options=request_options,
        )

    def organization_get(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsResponse1, OrganizationGetErrorBody]:
        """Returns details of a single organization. In order to get the details, the auth key must belong to the
        organization.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsResponse1],
            error_mapper=organization_get_error_mapper,
            request_options=request_options,
        )

    def organization_get_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsResponse, OrganizationGetListErrorBody]:
        """Returns a list with a single organization associated with the API key in the request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations"),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsResponse],
            error_mapper=organization_get_list_error_mapper,
            request_options=request_options,
        )

    def organization_private_endpoint_config_get_list(
        self,
        organization_id: UUID,
        cloud_provider: str,
        region_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPrivateEndpointConfigResponse, OrganizationPrivateEndpointConfigGetListErrorBody]:
        """Deprecated. Please follow `documentation
        <https://clickhouse.com/docs/manage/security/aws-privatelink#add-endpoint-id-to-services-allow-list>`__ for the
        updated process.

        Args:
            organization_id: ID of the requested organization.
            cloud_provider: Cloud provider identifier. One of aws, gcp, or azure.
            region_id: Region identifier within specific cloud providers.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/privateEndpointConfig"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[str]("cloud_provider", cloud_provider), param[str]("region_id", region_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPrivateEndpointConfigResponse],
            error_mapper=organization_private_endpoint_config_get_list_error_mapper,
            request_options=request_options,
        )

    def organization_quota_get(
        self, organization_id: UUID, quota_code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsQuotasResponse1, OrganizationQuotaGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns a single
        organization quota identified by its quota code. Responds with a not found error when the quota code is unknown
        or the quota does not apply to the organization.

        Args:
            organization_id: ID of the requested organization.
            quota_code: Code of the requested quota.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/quotas/{quotaCode}"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("quotaCode", quota_code)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsQuotasResponse1],
            error_mapper=organization_quota_get_error_mapper,
            request_options=request_options,
        )

    def organization_quotas_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsQuotasResponse, OrganizationQuotasGetListErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the
        resource quotas enforced for the organization together with their current usage where available. Quotas that do
        not apply to the organization are omitted. Quota values reflect the limits currently enforced, so they can be
        polled to detect changes, for example after a billing status change. The response contains one entry per quota
        code; quotas enforced per resource may additionally appear under resource-scoped endpoints in the future.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/quotas"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsQuotasResponse],
            error_mapper=organization_quotas_get_list_error_mapper,
            request_options=request_options,
        )

    def organization_update(
        self,
        organization_id: UUID,
        *,
        body: OrganizationPatchRequest | OrganizationPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsResponse1, OrganizationUpdateErrorBody]:
        """Updates organization fields. Requires ADMIN auth key role.

        Args:
            organization_id: ID of the organization to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OrganizationPatchRequest | OrganizationPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsResponse1],
            error_mapper=organization_update_error_mapper,
            request_options=request_options,
        )


class AsyncOrganizationApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def activity_get(
        self, organization_id: UUID, activity_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsActivitiesResponse1, ActivityGetErrorBody]:
        """Returns a single organization activity by ID.

        Args:
            organization_id: ID of the requested organization.
            activity_id: ID of the requested activity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/activities/{activityId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("activityId", activity_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsActivitiesResponse1],
            error_mapper=activity_get_error_mapper,
            request_options=request_options,
        )

    async def activity_get_list(
        self,
        organization_id: UUID,
        *,
        from_date: RFC3339DateTime | None = None,
        to_date: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsActivitiesResponse, ActivityGetListErrorBody]:
        """Returns a list of all organization activities.

        Args:
            organization_id: ID of the requested organization.
            from_date: A starting date for a search
            to_date: An ending date for a search
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/activities"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[
                param[RFC3339DateTime | None]("from_date", from_date), param[RFC3339DateTime | None]("to_date", to_date)
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsActivitiesResponse],
            error_mapper=activity_get_list_error_mapper,
            request_options=request_options,
        )

    async def organization_byoc_infrastructure_create(
        self,
        organization_id: UUID,
        *,
        body: ByocInfrastructurePostRequest | ByocInfrastructurePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsByocInfrastructureResponse, OrganizationByocInfrastructureCreateErrorBody]:
        """Create a new BYOC Infrastructure in the organization. Returns the configuration of the newly created
        infrastructure

        Args:
            organization_id: ID of the requested organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/byocInfrastructure"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ByocInfrastructurePostRequest | ByocInfrastructurePostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsByocInfrastructureResponse],
            error_mapper=organization_byoc_infrastructure_create_error_mapper,
            request_options=request_options,
        )

    async def organization_byoc_infrastructure_delete(
        self,
        organization_id: UUID,
        byoc_infrastructure_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsByocInfrastructureResponse1, OrganizationByocInfrastructureDeleteErrorBody]:
        """Removes a BYOC Infrastructure from the organization

        Args:
            organization_id: ID of the requested organization.
            byoc_infrastructure_id: ID of the requested BYOC Infrastructure
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/byocInfrastructure/{byocInfrastructureId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("byocInfrastructureId", byoc_infrastructure_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsByocInfrastructureResponse1],
            error_mapper=organization_byoc_infrastructure_delete_error_mapper,
            request_options=request_options,
        )

    async def organization_byoc_infrastructure_update(
        self,
        organization_id: UUID,
        byoc_infrastructure_id: UUID,
        *,
        body: ByocInfrastructurePatchRequest | ByocInfrastructurePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsByocInfrastructureResponse, OrganizationByocInfrastructureUpdateErrorBody]:
        """Update configuration of the BYOC infrastructure. Returns the modified infrastructure

        Args:
            organization_id: ID of the requested organization.
            byoc_infrastructure_id: ID of the requested BYOC Infrastructure
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/byocInfrastructure/{byocInfrastructureId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("byocInfrastructureId", byoc_infrastructure_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ByocInfrastructurePatchRequest | ByocInfrastructurePatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsByocInfrastructureResponse],
            error_mapper=organization_byoc_infrastructure_update_error_mapper,
            request_options=request_options,
        )

    async def organization_get(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsResponse1, OrganizationGetErrorBody]:
        """Returns details of a single organization. In order to get the details, the auth key must belong to the
        organization.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsResponse1],
            error_mapper=organization_get_error_mapper,
            request_options=request_options,
        )

    async def organization_get_list(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsResponse, OrganizationGetListErrorBody]:
        """Returns a list with a single organization associated with the API key in the request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations"),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsResponse],
            error_mapper=organization_get_list_error_mapper,
            request_options=request_options,
        )

    async def organization_private_endpoint_config_get_list(
        self,
        organization_id: UUID,
        cloud_provider: str,
        region_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPrivateEndpointConfigResponse, OrganizationPrivateEndpointConfigGetListErrorBody]:
        """Deprecated. Please follow `documentation
        <https://clickhouse.com/docs/manage/security/aws-privatelink#add-endpoint-id-to-services-allow-list>`__ for the
        updated process.

        Args:
            organization_id: ID of the requested organization.
            cloud_provider: Cloud provider identifier. One of aws, gcp, or azure.
            region_id: Region identifier within specific cloud providers.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/privateEndpointConfig"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[str]("cloud_provider", cloud_provider), param[str]("region_id", region_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPrivateEndpointConfigResponse],
            error_mapper=organization_private_endpoint_config_get_list_error_mapper,
            request_options=request_options,
        )

    async def organization_quota_get(
        self, organization_id: UUID, quota_code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsQuotasResponse1, OrganizationQuotaGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns a single
        organization quota identified by its quota code. Responds with a not found error when the quota code is unknown
        or the quota does not apply to the organization.

        Args:
            organization_id: ID of the requested organization.
            quota_code: Code of the requested quota.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/quotas/{quotaCode}"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("quotaCode", quota_code)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsQuotasResponse1],
            error_mapper=organization_quota_get_error_mapper,
            request_options=request_options,
        )

    async def organization_quotas_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsQuotasResponse, OrganizationQuotasGetListErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the
        resource quotas enforced for the organization together with their current usage where available. Quotas that do
        not apply to the organization are omitted. Quota values reflect the limits currently enforced, so they can be
        polled to detect changes, for example after a billing status change. The response contains one entry per quota
        code; quotas enforced per resource may additionally appear under resource-scoped endpoints in the future.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/quotas"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsQuotasResponse],
            error_mapper=organization_quotas_get_list_error_mapper,
            request_options=request_options,
        )

    async def organization_update(
        self,
        organization_id: UUID,
        *,
        body: OrganizationPatchRequest | OrganizationPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsResponse1, OrganizationUpdateErrorBody]:
        """Updates organization fields. Requires ADMIN auth key role.

        Args:
            organization_id: ID of the organization to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OrganizationPatchRequest | OrganizationPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsResponse1],
            error_mapper=organization_update_error_mapper,
            request_options=request_options,
        )
