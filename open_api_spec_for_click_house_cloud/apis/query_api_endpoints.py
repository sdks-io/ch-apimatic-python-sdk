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
from ..errors.query_api_endpoint_create_error import (
    QueryApiEndpointCreateErrorBody,
    query_api_endpoint_create_error_mapper,
)
from ..errors.query_api_endpoint_delete_error import (
    QueryApiEndpointDeleteErrorBody,
    query_api_endpoint_delete_error_mapper,
)
from ..errors.query_api_endpoint_get_error import QueryApiEndpointGetErrorBody, query_api_endpoint_get_error_mapper
from ..errors.query_api_endpoint_list_error import QueryApiEndpointListErrorBody, query_api_endpoint_list_error_mapper
from ..errors.query_api_endpoint_update_error import (
    QueryApiEndpointUpdateErrorBody,
    query_api_endpoint_update_error_mapper,
)
from ..models.public_query_api_endpoint_request import PublicQueryApiEndpointRequest, PublicQueryApiEndpointRequestDict
from ..models.v1_organizations_services_query_api_endpoints_endpoint_id_response import (
    V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse,
)
from ..models.v1_organizations_services_query_api_endpoints_endpoint_id_response1 import (
    V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1,
)
from ..models.v1_organizations_services_query_api_endpoints_response import (
    V1OrganizationsServicesQueryApiEndpointsResponse,
)
from ..models.v1_organizations_services_query_api_endpoints_response1 import (
    V1OrganizationsServicesQueryApiEndpointsResponse1,
)
from ..server.server import Server


class QueryApiEndpoints:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = QueryApiEndpointsWithRawResponse(client, server, auth)

    def query_api_endpoint_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesQueryApiEndpointsResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The Query API endpoint was created.

        Raises:
            ApiError: The request cannot be processed due to a client error. The request is forbidden. Service not
                found. An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud
                support for assistance. ``error`` is ``V1OrganizationsServicesQueryApiEndpoints400Error1 |
                V1OrganizationsServicesQueryApiEndpoints403Error1 | V1OrganizationsServicesQueryApiEndpoints404Error1 |
                V1OrganizationsServicesQueryApiEndpoints500Error1 | RawError``."""
        return self._with_raw_response.query_api_endpoint_create(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def query_api_endpoint_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            endpoint_id: ID of the requested Query API endpoint.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The Query API endpoint was deleted.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. The request is forbidden. Query API endpoint not found. Query API endpoint can not be managed
                via this API. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesQueryApiEndpointsEndpointId400Error1
                | V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1 | RawError``."""
        return self._with_raw_response.query_api_endpoint_delete(
            organization_id, service_id, endpoint_id, request_options=request_options
        ).unwrap()

    def query_api_endpoint_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            endpoint_id: ID of the requested Query API endpoint.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. The request is forbidden. Query API endpoint not found. An internal server error has
                occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesQueryApiEndpointsEndpointId400Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1 | RawError``."""
        return self._with_raw_response.query_api_endpoint_get(
            organization_id, service_id, endpoint_id, request_options=request_options
        ).unwrap()

    def query_api_endpoint_list(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesQueryApiEndpointsResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns all active
        Query API endpoints for the service.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. The request is forbidden. Service not
                found. An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud
                support for assistance. ``error`` is ``V1OrganizationsServicesQueryApiEndpoints400Error1 |
                V1OrganizationsServicesQueryApiEndpoints403Error1 | V1OrganizationsServicesQueryApiEndpoints404Error1 |
                V1OrganizationsServicesQueryApiEndpoints500Error1 | RawError``."""
        return self._with_raw_response.query_api_endpoint_list(
            organization_id, service_id, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def query_api_endpoint_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        endpoint_id: UUID,
        *,
        body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Updates a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            endpoint_id: ID of the requested Query API endpoint.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The Query API endpoint was updated.

        Raises:
            ApiError: The request cannot be processed due to a client error. The request is forbidden. Query API
                endpoint not found. Query API endpoint can not be managed via this API. An internal server error has
                occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesQueryApiEndpointsEndpointId400Error31 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1 | RawError``."""
        return self._with_raw_response.query_api_endpoint_update(
            organization_id, service_id, endpoint_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> QueryApiEndpointsWithRawResponse:
        return self._with_raw_response


class AsyncQueryApiEndpoints:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncQueryApiEndpointsWithRawResponse(client, server, auth)

    async def query_api_endpoint_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesQueryApiEndpointsResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The Query API endpoint was created.

        Raises:
            ApiError: The request cannot be processed due to a client error. The request is forbidden. Service not
                found. An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud
                support for assistance. ``error`` is ``V1OrganizationsServicesQueryApiEndpoints400Error1 |
                V1OrganizationsServicesQueryApiEndpoints403Error1 | V1OrganizationsServicesQueryApiEndpoints404Error1 |
                V1OrganizationsServicesQueryApiEndpoints500Error1 | RawError``."""
        return (
            await self._with_raw_response.query_api_endpoint_create(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def query_api_endpoint_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            endpoint_id: ID of the requested Query API endpoint.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The Query API endpoint was deleted.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. The request is forbidden. Query API endpoint not found. Query API endpoint can not be managed
                via this API. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesQueryApiEndpointsEndpointId400Error1
                | V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1 | RawError``."""
        return (
            await self._with_raw_response.query_api_endpoint_delete(
                organization_id, service_id, endpoint_id, request_options=request_options
            )
        ).unwrap()

    async def query_api_endpoint_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            endpoint_id: ID of the requested Query API endpoint.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. The request is forbidden. Query API endpoint not found. An internal server error has
                occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesQueryApiEndpointsEndpointId400Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1 | RawError``."""
        return (
            await self._with_raw_response.query_api_endpoint_get(
                organization_id, service_id, endpoint_id, request_options=request_options
            )
        ).unwrap()

    async def query_api_endpoint_list(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesQueryApiEndpointsResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns all active
        Query API endpoints for the service.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. The request is forbidden. Service not
                found. An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud
                support for assistance. ``error`` is ``V1OrganizationsServicesQueryApiEndpoints400Error1 |
                V1OrganizationsServicesQueryApiEndpoints403Error1 | V1OrganizationsServicesQueryApiEndpoints404Error1 |
                V1OrganizationsServicesQueryApiEndpoints500Error1 | RawError``."""
        return (
            await self._with_raw_response.query_api_endpoint_list(
                organization_id, service_id, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def query_api_endpoint_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        endpoint_id: UUID,
        *,
        body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Updates a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            endpoint_id: ID of the requested Query API endpoint.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The Query API endpoint was updated.

        Raises:
            ApiError: The request cannot be processed due to a client error. The request is forbidden. Query API
                endpoint not found. Query API endpoint can not be managed via this API. An internal server error has
                occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesQueryApiEndpointsEndpointId400Error31 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1 |
                V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1 | RawError``."""
        return (
            await self._with_raw_response.query_api_endpoint_update(
                organization_id, service_id, endpoint_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncQueryApiEndpointsWithRawResponse:
        return self._with_raw_response


class QueryApiEndpointsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def query_api_endpoint_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsResponse, QueryApiEndpointCreateErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates a Query API
        endpoint.

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
                "/v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesQueryApiEndpointsResponse],
            error_mapper=query_api_endpoint_create_error_mapper,
            request_options=request_options,
        )

    def query_api_endpoint_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse, QueryApiEndpointDeleteErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            endpoint_id: ID of the requested Query API endpoint.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints/{endpointId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("endpointId", endpoint_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse],
            error_mapper=query_api_endpoint_delete_error_mapper,
            request_options=request_options,
        )

    def query_api_endpoint_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1, QueryApiEndpointGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            endpoint_id: ID of the requested Query API endpoint.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints/{endpointId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("endpointId", endpoint_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1],
            error_mapper=query_api_endpoint_get_error_mapper,
            request_options=request_options,
        )

    def query_api_endpoint_list(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsResponse1, QueryApiEndpointListErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns all active
        Query API endpoints for the service.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesQueryApiEndpointsResponse1],
            error_mapper=query_api_endpoint_list_error_mapper,
            request_options=request_options,
        )

    def query_api_endpoint_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        endpoint_id: UUID,
        *,
        body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1, QueryApiEndpointUpdateErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Updates a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            endpoint_id: ID of the requested Query API endpoint.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints/{endpointId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("endpointId", endpoint_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1],
            error_mapper=query_api_endpoint_update_error_mapper,
            request_options=request_options,
        )


class AsyncQueryApiEndpointsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def query_api_endpoint_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsResponse, QueryApiEndpointCreateErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates a Query API
        endpoint.

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
                "/v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesQueryApiEndpointsResponse],
            error_mapper=query_api_endpoint_create_error_mapper,
            request_options=request_options,
        )

    async def query_api_endpoint_delete(
        self,
        organization_id: UUID,
        service_id: UUID,
        endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse, QueryApiEndpointDeleteErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            endpoint_id: ID of the requested Query API endpoint.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints/{endpointId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("endpointId", endpoint_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse],
            error_mapper=query_api_endpoint_delete_error_mapper,
            request_options=request_options,
        )

    async def query_api_endpoint_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        endpoint_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1, QueryApiEndpointGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            endpoint_id: ID of the requested Query API endpoint.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints/{endpointId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("endpointId", endpoint_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1],
            error_mapper=query_api_endpoint_get_error_mapper,
            request_options=request_options,
        )

    async def query_api_endpoint_list(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsResponse1, QueryApiEndpointListErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns all active
        Query API endpoints for the service.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesQueryApiEndpointsResponse1],
            error_mapper=query_api_endpoint_list_error_mapper,
            request_options=request_options,
        )

    async def query_api_endpoint_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        endpoint_id: UUID,
        *,
        body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1, QueryApiEndpointUpdateErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Updates a Query API
        endpoint.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            endpoint_id: ID of the requested Query API endpoint.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints/{endpointId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("endpointId", endpoint_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1],
            error_mapper=query_api_endpoint_update_error_mapper,
            request_options=request_options,
        )
