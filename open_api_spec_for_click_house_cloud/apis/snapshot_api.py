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
from ..errors.snapshot_configuration_get_error import (
    SnapshotConfigurationGetErrorBody,
    snapshot_configuration_get_error_mapper,
)
from ..errors.snapshot_configuration_update_error import (
    SnapshotConfigurationUpdateErrorBody,
    snapshot_configuration_update_error_mapper,
)
from ..errors.snapshot_get_error import SnapshotGetErrorBody, snapshot_get_error_mapper
from ..errors.snapshot_get_list_error import SnapshotGetListErrorBody, snapshot_get_list_error_mapper
from ..models.snapshot_configuration_patch_request import (
    SnapshotConfigurationPatchRequest,
    SnapshotConfigurationPatchRequestDict,
)
from ..models.v1_organizations_services_snapshot_configuration_response import (
    V1OrganizationsServicesSnapshotConfigurationResponse,
)
from ..models.v1_organizations_services_snapshots_response import V1OrganizationsServicesSnapshotsResponse
from ..models.v1_organizations_services_snapshots_snapshot_id_response import (
    V1OrganizationsServicesSnapshotsSnapshotIdResponse,
)
from ..server.server import Server


class SnapshotApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SnapshotApiWithRawResponse(client, server, auth)

    def snapshot_configuration_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesSnapshotConfigurationResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns the service snapshot configuration.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesSnapshotConfiguration400Error1 |
                V1OrganizationsServicesSnapshotConfiguration500Error1 | RawError``."""
        return self._with_raw_response.snapshot_configuration_get(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def snapshot_configuration_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: SnapshotConfigurationPatchRequest | SnapshotConfigurationPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesSnapshotConfigurationResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Updates the service snapshot configuration. Requires ADMIN auth key role. Enables or disables scheduled
        snapshots and sets the cadence; when enabled, gap and timeFrame (in minutes) must together be one of the
        supported (gap, timeFrame) pairs: (30, 1440), (60, 2880). Provide at least one of enabled, gap, timeFrame; omit
        a field to leave it unchanged (null is not accepted).

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
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesSnapshotConfiguration400Error1 |
                V1OrganizationsServicesSnapshotConfiguration500Error1 | RawError``."""
        return self._with_raw_response.snapshot_configuration_update(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def snapshot_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        snapshot_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesSnapshotsSnapshotIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a single snapshot info.

        Args:
            organization_id: ID of the organization that owns the snapshot.
            service_id: ID of the service the snapshot was created from.
            snapshot_id: ID of the requested snapshot.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesSnapshotsSnapshotId400Error1 |
                V1OrganizationsServicesSnapshotsSnapshotId500Error1 | RawError``."""
        return self._with_raw_response.snapshot_get(
            organization_id, service_id, snapshot_id, request_options=request_options
        ).unwrap()

    def snapshot_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesSnapshotsResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a list of all snapshots for the service. The most recent snapshots come first in the list.

        Args:
            organization_id: ID of the organization that owns the snapshot.
            service_id: ID of the service the snapshot was created from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesSnapshots400Error1 |
                V1OrganizationsServicesSnapshots500Error1 | RawError``."""
        return self._with_raw_response.snapshot_get_list(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SnapshotApiWithRawResponse:
        return self._with_raw_response


class AsyncSnapshotApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSnapshotApiWithRawResponse(client, server, auth)

    async def snapshot_configuration_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesSnapshotConfigurationResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns the service snapshot configuration.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesSnapshotConfiguration400Error1 |
                V1OrganizationsServicesSnapshotConfiguration500Error1 | RawError``."""
        return (
            await self._with_raw_response.snapshot_configuration_get(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def snapshot_configuration_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: SnapshotConfigurationPatchRequest | SnapshotConfigurationPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesSnapshotConfigurationResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Updates the service snapshot configuration. Requires ADMIN auth key role. Enables or disables scheduled
        snapshots and sets the cadence; when enabled, gap and timeFrame (in minutes) must together be one of the
        supported (gap, timeFrame) pairs: (30, 1440), (60, 2880). Provide at least one of enabled, gap, timeFrame; omit
        a field to leave it unchanged (null is not accepted).

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
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesSnapshotConfiguration400Error1 |
                V1OrganizationsServicesSnapshotConfiguration500Error1 | RawError``."""
        return (
            await self._with_raw_response.snapshot_configuration_update(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def snapshot_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        snapshot_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesSnapshotsSnapshotIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a single snapshot info.

        Args:
            organization_id: ID of the organization that owns the snapshot.
            service_id: ID of the service the snapshot was created from.
            snapshot_id: ID of the requested snapshot.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesSnapshotsSnapshotId400Error1 |
                V1OrganizationsServicesSnapshotsSnapshotId500Error1 | RawError``."""
        return (
            await self._with_raw_response.snapshot_get(
                organization_id, service_id, snapshot_id, request_options=request_options
            )
        ).unwrap()

    async def snapshot_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesSnapshotsResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a list of all snapshots for the service. The most recent snapshots come first in the list.

        Args:
            organization_id: ID of the organization that owns the snapshot.
            service_id: ID of the service the snapshot was created from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesSnapshots400Error1 |
                V1OrganizationsServicesSnapshots500Error1 | RawError``."""
        return (
            await self._with_raw_response.snapshot_get_list(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSnapshotApiWithRawResponse:
        return self._with_raw_response


class SnapshotApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def snapshot_configuration_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesSnapshotConfigurationResponse, SnapshotConfigurationGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns the service snapshot configuration.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/snapshotConfiguration"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesSnapshotConfigurationResponse],
            error_mapper=snapshot_configuration_get_error_mapper,
            request_options=request_options,
        )

    def snapshot_configuration_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: SnapshotConfigurationPatchRequest | SnapshotConfigurationPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesSnapshotConfigurationResponse, SnapshotConfigurationUpdateErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Updates the service snapshot configuration. Requires ADMIN auth key role. Enables or disables scheduled
        snapshots and sets the cadence; when enabled, gap and timeFrame (in minutes) must together be one of the
        supported (gap, timeFrame) pairs: (30, 1440), (60, 2880). Provide at least one of enabled, gap, timeFrame; omit
        a field to leave it unchanged (null is not accepted).

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
                "/v1/organizations/{organizationId}/services/{serviceId}/snapshotConfiguration"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SnapshotConfigurationPatchRequest | SnapshotConfigurationPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesSnapshotConfigurationResponse],
            error_mapper=snapshot_configuration_update_error_mapper,
            request_options=request_options,
        )

    def snapshot_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        snapshot_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesSnapshotsSnapshotIdResponse, SnapshotGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a single snapshot info.

        Args:
            organization_id: ID of the organization that owns the snapshot.
            service_id: ID of the service the snapshot was created from.
            snapshot_id: ID of the requested snapshot.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/snapshots/{snapshotId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("snapshotId", snapshot_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesSnapshotsSnapshotIdResponse],
            error_mapper=snapshot_get_error_mapper,
            request_options=request_options,
        )

    def snapshot_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesSnapshotsResponse, SnapshotGetListErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a list of all snapshots for the service. The most recent snapshots come first in the list.

        Args:
            organization_id: ID of the organization that owns the snapshot.
            service_id: ID of the service the snapshot was created from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/snapshots"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesSnapshotsResponse],
            error_mapper=snapshot_get_list_error_mapper,
            request_options=request_options,
        )


class AsyncSnapshotApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def snapshot_configuration_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesSnapshotConfigurationResponse, SnapshotConfigurationGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns the service snapshot configuration.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/snapshotConfiguration"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesSnapshotConfigurationResponse],
            error_mapper=snapshot_configuration_get_error_mapper,
            request_options=request_options,
        )

    async def snapshot_configuration_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: SnapshotConfigurationPatchRequest | SnapshotConfigurationPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesSnapshotConfigurationResponse, SnapshotConfigurationUpdateErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Updates the service snapshot configuration. Requires ADMIN auth key role. Enables or disables scheduled
        snapshots and sets the cadence; when enabled, gap and timeFrame (in minutes) must together be one of the
        supported (gap, timeFrame) pairs: (30, 1440), (60, 2880). Provide at least one of enabled, gap, timeFrame; omit
        a field to leave it unchanged (null is not accepted).

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
                "/v1/organizations/{organizationId}/services/{serviceId}/snapshotConfiguration"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SnapshotConfigurationPatchRequest | SnapshotConfigurationPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesSnapshotConfigurationResponse],
            error_mapper=snapshot_configuration_update_error_mapper,
            request_options=request_options,
        )

    async def snapshot_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        snapshot_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesSnapshotsSnapshotIdResponse, SnapshotGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a single snapshot info.

        Args:
            organization_id: ID of the organization that owns the snapshot.
            service_id: ID of the service the snapshot was created from.
            snapshot_id: ID of the requested snapshot.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/snapshots/{snapshotId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("snapshotId", snapshot_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesSnapshotsSnapshotIdResponse],
            error_mapper=snapshot_get_error_mapper,
            request_options=request_options,
        )

    async def snapshot_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesSnapshotsResponse, SnapshotGetListErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a list of all snapshots for the service. The most recent snapshots come first in the list.

        Args:
            organization_id: ID of the organization that owns the snapshot.
            service_id: ID of the service the snapshot was created from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/snapshots"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesSnapshotsResponse],
            error_mapper=snapshot_get_list_error_mapper,
            request_options=request_options,
        )
