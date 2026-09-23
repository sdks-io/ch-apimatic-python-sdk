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
from ..errors.openapi_key_create_error import OpenapiKeyCreateErrorBody, openapi_key_create_error_mapper
from ..errors.openapi_key_delete_error import OpenapiKeyDeleteErrorBody, openapi_key_delete_error_mapper
from ..errors.openapi_key_get_error import OpenapiKeyGetErrorBody, openapi_key_get_error_mapper
from ..errors.openapi_key_get_list_error import OpenapiKeyGetListErrorBody, openapi_key_get_list_error_mapper
from ..errors.openapi_key_update_error import OpenapiKeyUpdateErrorBody, openapi_key_update_error_mapper
from ..models.api_key_patch_request import ApiKeyPatchRequest, ApiKeyPatchRequestDict
from ..models.api_key_post_request import ApiKeyPostRequest, ApiKeyPostRequestDict
from ..models.v1_organizations_keys_response import V1OrganizationsKeysResponse
from ..models.v1_organizations_keys_response1 import V1OrganizationsKeysResponse1
from ..models.v1_organizations_keys_response2 import V1OrganizationsKeysResponse2
from ..models.v1_organizations_keys_response4 import V1OrganizationsKeysResponse4
from ..server.server import Server


class ApiKeys:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ApiKeysWithRawResponse(client, server, auth)

    def openapi_key_create(
        self,
        organization_id: UUID,
        *,
        body: ApiKeyPostRequest | ApiKeyPostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsKeysResponse1:
        """Creates new API key.

        Args:
            organization_id: ID of the organization that will own the key.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsKeys400Error1 | V1OrganizationsKeys500Error1
                | RawError``."""
        return self._with_raw_response.openapi_key_create(
            organization_id, body=body, request_options=request_options
        ).unwrap()

    def openapi_key_delete(
        self, organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsKeysResponse4:
        """Deletes API key. Only a key not used to authenticate the active request can be deleted.

        Args:
            organization_id: ID of the organization that owns the key.
            key_id: ID of the key to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsKeys400Error1 | V1OrganizationsKeys500Error1
                | RawError``."""
        return self._with_raw_response.openapi_key_delete(
            organization_id, key_id, request_options=request_options
        ).unwrap()

    def openapi_key_get(
        self, organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsKeysResponse2:
        """Returns a single key details.

        Args:
            organization_id: ID of the requested organization.
            key_id: ID of the requested key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsKeys400Error1 | V1OrganizationsKeys500Error1
                | RawError``."""
        return self._with_raw_response.openapi_key_get(
            organization_id, key_id, request_options=request_options
        ).unwrap()

    def openapi_key_get_list(
        self,
        organization_id: UUID,
        *,
        limit: int | None = 250,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsKeysResponse:
        """Returns a list of keys in the organization, ordered by creation date, oldest first. Results are capped at
        ``limit`` (default and maximum 250) per page. Every response carries ``limit``, ``totalCount`` and
        ``nextCursor``; pass ``nextCursor`` as the ``cursor`` query parameter to fetch the next page, repeating until it
        is null.

        Args:
            organization_id: ID of the requested organization.
            limit: Maximum number of results to return.
            cursor: Opaque cursor from a previous response's ``nextCursor``, marking where to resume the list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsKeys400Error1 | V1OrganizationsKeys500Error1
                | RawError``."""
        return self._with_raw_response.openapi_key_get_list(
            organization_id, limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def openapi_key_update(
        self,
        organization_id: UUID,
        key_id: UUID,
        *,
        body: ApiKeyPatchRequest | ApiKeyPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsKeysResponse2:
        """Updates API key properties.

        Args:
            organization_id: ID of the organization that owns the key.
            key_id: ID of the key to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsKeys400Error1 | V1OrganizationsKeys500Error1
                | RawError``."""
        return self._with_raw_response.openapi_key_update(
            organization_id, key_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ApiKeysWithRawResponse:
        return self._with_raw_response


class AsyncApiKeys:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApiKeysWithRawResponse(client, server, auth)

    async def openapi_key_create(
        self,
        organization_id: UUID,
        *,
        body: ApiKeyPostRequest | ApiKeyPostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsKeysResponse1:
        """Creates new API key.

        Args:
            organization_id: ID of the organization that will own the key.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsKeys400Error1 | V1OrganizationsKeys500Error1
                | RawError``."""
        return (
            await self._with_raw_response.openapi_key_create(
                organization_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def openapi_key_delete(
        self, organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsKeysResponse4:
        """Deletes API key. Only a key not used to authenticate the active request can be deleted.

        Args:
            organization_id: ID of the organization that owns the key.
            key_id: ID of the key to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsKeys400Error1 | V1OrganizationsKeys500Error1
                | RawError``."""
        return (
            await self._with_raw_response.openapi_key_delete(organization_id, key_id, request_options=request_options)
        ).unwrap()

    async def openapi_key_get(
        self, organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsKeysResponse2:
        """Returns a single key details.

        Args:
            organization_id: ID of the requested organization.
            key_id: ID of the requested key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsKeys400Error1 | V1OrganizationsKeys500Error1
                | RawError``."""
        return (
            await self._with_raw_response.openapi_key_get(organization_id, key_id, request_options=request_options)
        ).unwrap()

    async def openapi_key_get_list(
        self,
        organization_id: UUID,
        *,
        limit: int | None = 250,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsKeysResponse:
        """Returns a list of keys in the organization, ordered by creation date, oldest first. Results are capped at
        ``limit`` (default and maximum 250) per page. Every response carries ``limit``, ``totalCount`` and
        ``nextCursor``; pass ``nextCursor`` as the ``cursor`` query parameter to fetch the next page, repeating until it
        is null.

        Args:
            organization_id: ID of the requested organization.
            limit: Maximum number of results to return.
            cursor: Opaque cursor from a previous response's ``nextCursor``, marking where to resume the list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsKeys400Error1 | V1OrganizationsKeys500Error1
                | RawError``."""
        return (
            await self._with_raw_response.openapi_key_get_list(
                organization_id, limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def openapi_key_update(
        self,
        organization_id: UUID,
        key_id: UUID,
        *,
        body: ApiKeyPatchRequest | ApiKeyPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsKeysResponse2:
        """Updates API key properties.

        Args:
            organization_id: ID of the organization that owns the key.
            key_id: ID of the key to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsKeys400Error1 | V1OrganizationsKeys500Error1
                | RawError``."""
        return (
            await self._with_raw_response.openapi_key_update(
                organization_id, key_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApiKeysWithRawResponse:
        return self._with_raw_response


class ApiKeysWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def openapi_key_create(
        self,
        organization_id: UUID,
        *,
        body: ApiKeyPostRequest | ApiKeyPostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsKeysResponse1, OpenapiKeyCreateErrorBody]:
        """Creates new API key.

        Args:
            organization_id: ID of the organization that will own the key.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/keys"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApiKeyPostRequest | ApiKeyPostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsKeysResponse1],
            error_mapper=openapi_key_create_error_mapper,
            request_options=request_options,
        )

    def openapi_key_delete(
        self, organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsKeysResponse4, OpenapiKeyDeleteErrorBody]:
        """Deletes API key. Only a key not used to authenticate the active request can be deleted.

        Args:
            organization_id: ID of the organization that owns the key.
            key_id: ID of the key to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/keys/{keyId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("keyId", key_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsKeysResponse4],
            error_mapper=openapi_key_delete_error_mapper,
            request_options=request_options,
        )

    def openapi_key_get(
        self, organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsKeysResponse2, OpenapiKeyGetErrorBody]:
        """Returns a single key details.

        Args:
            organization_id: ID of the requested organization.
            key_id: ID of the requested key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/keys/{keyId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("keyId", key_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsKeysResponse2],
            error_mapper=openapi_key_get_error_mapper,
            request_options=request_options,
        )

    def openapi_key_get_list(
        self,
        organization_id: UUID,
        *,
        limit: int | None = 250,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsKeysResponse, OpenapiKeyGetListErrorBody]:
        """Returns a list of keys in the organization, ordered by creation date, oldest first. Results are capped at
        ``limit`` (default and maximum 250) per page. Every response carries ``limit``, ``totalCount`` and
        ``nextCursor``; pass ``nextCursor`` as the ``cursor`` query parameter to fetch the next page, repeating until it
        is null.

        Args:
            organization_id: ID of the requested organization.
            limit: Maximum number of results to return.
            cursor: Opaque cursor from a previous response's ``nextCursor``, marking where to resume the list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/keys"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsKeysResponse],
            error_mapper=openapi_key_get_list_error_mapper,
            request_options=request_options,
        )

    def openapi_key_update(
        self,
        organization_id: UUID,
        key_id: UUID,
        *,
        body: ApiKeyPatchRequest | ApiKeyPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsKeysResponse2, OpenapiKeyUpdateErrorBody]:
        """Updates API key properties.

        Args:
            organization_id: ID of the organization that owns the key.
            key_id: ID of the key to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/keys/{keyId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("keyId", key_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApiKeyPatchRequest | ApiKeyPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsKeysResponse2],
            error_mapper=openapi_key_update_error_mapper,
            request_options=request_options,
        )


class AsyncApiKeysWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def openapi_key_create(
        self,
        organization_id: UUID,
        *,
        body: ApiKeyPostRequest | ApiKeyPostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsKeysResponse1, OpenapiKeyCreateErrorBody]:
        """Creates new API key.

        Args:
            organization_id: ID of the organization that will own the key.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/keys"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApiKeyPostRequest | ApiKeyPostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsKeysResponse1],
            error_mapper=openapi_key_create_error_mapper,
            request_options=request_options,
        )

    async def openapi_key_delete(
        self, organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsKeysResponse4, OpenapiKeyDeleteErrorBody]:
        """Deletes API key. Only a key not used to authenticate the active request can be deleted.

        Args:
            organization_id: ID of the organization that owns the key.
            key_id: ID of the key to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/keys/{keyId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("keyId", key_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsKeysResponse4],
            error_mapper=openapi_key_delete_error_mapper,
            request_options=request_options,
        )

    async def openapi_key_get(
        self, organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsKeysResponse2, OpenapiKeyGetErrorBody]:
        """Returns a single key details.

        Args:
            organization_id: ID of the requested organization.
            key_id: ID of the requested key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/keys/{keyId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("keyId", key_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsKeysResponse2],
            error_mapper=openapi_key_get_error_mapper,
            request_options=request_options,
        )

    async def openapi_key_get_list(
        self,
        organization_id: UUID,
        *,
        limit: int | None = 250,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsKeysResponse, OpenapiKeyGetListErrorBody]:
        """Returns a list of keys in the organization, ordered by creation date, oldest first. Results are capped at
        ``limit`` (default and maximum 250) per page. Every response carries ``limit``, ``totalCount`` and
        ``nextCursor``; pass ``nextCursor`` as the ``cursor`` query parameter to fetch the next page, repeating until it
        is null.

        Args:
            organization_id: ID of the requested organization.
            limit: Maximum number of results to return.
            cursor: Opaque cursor from a previous response's ``nextCursor``, marking where to resume the list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/keys"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsKeysResponse],
            error_mapper=openapi_key_get_list_error_mapper,
            request_options=request_options,
        )

    async def openapi_key_update(
        self,
        organization_id: UUID,
        key_id: UUID,
        *,
        body: ApiKeyPatchRequest | ApiKeyPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsKeysResponse2, OpenapiKeyUpdateErrorBody]:
        """Updates API key properties.

        Args:
            organization_id: ID of the organization that owns the key.
            key_id: ID of the key to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/keys/{keyId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("keyId", key_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ApiKeyPatchRequest | ApiKeyPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsKeysResponse2],
            error_mapper=openapi_key_update_error_mapper,
            request_options=request_options,
        )
