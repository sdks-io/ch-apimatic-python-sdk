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
from ..errors.organization_role_delete_error import (
    OrganizationRoleDeleteErrorBody,
    organization_role_delete_error_mapper,
)
from ..errors.organization_role_get_error import OrganizationRoleGetErrorBody, organization_role_get_error_mapper
from ..errors.organization_role_patch_error import OrganizationRolePatchErrorBody, organization_role_patch_error_mapper
from ..errors.organization_role_post_error import OrganizationRolePostErrorBody, organization_role_post_error_mapper
from ..errors.organization_roles_get_list_error import (
    OrganizationRolesGetListErrorBody,
    organization_roles_get_list_error_mapper,
)
from ..models.role_create_request import RoleCreateRequest, RoleCreateRequestDict
from ..models.role_update_request import RoleUpdateRequest, RoleUpdateRequestDict
from ..models.v1_organizations_roles_response import V1OrganizationsRolesResponse
from ..models.v1_organizations_roles_response1 import V1OrganizationsRolesResponse1
from ..models.v1_organizations_roles_response4 import V1OrganizationsRolesResponse4
from ..server.server import Server


class RoleManagement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = RoleManagementWithRawResponse(client, server, auth)

    def organization_role_delete(
        self, organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsRolesResponse4:
        """Deletes an existing custom role. System roles cannot be deleted. This operation will remove the role and all
        its associated policies.

        Args:
            organization_id: ID of the requested organization.
            role_id: ID of the requested role.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsRoles400Error1 |
                V1OrganizationsRoles500Error1 | RawError``."""
        return self._with_raw_response.organization_role_delete(
            organization_id, role_id, request_options=request_options
        ).unwrap()

    def organization_role_get(
        self, organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsRolesResponse1:
        """Returns details for a specific role.

        Args:
            organization_id: ID of the requested organization.
            role_id: ID of the requested role.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsRoles400Error1 |
                V1OrganizationsRoles500Error1 | RawError``."""
        return self._with_raw_response.organization_role_get(
            organization_id, role_id, request_options=request_options
        ).unwrap()

    def organization_role_patch(
        self,
        organization_id: UUID,
        role_id: UUID,
        *,
        body: RoleUpdateRequest | RoleUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsRolesResponse1:
        """Updates an existing custom role. System roles cannot be updated. All fields are optional - only provided
        fields will be updated.

        Args:
            organization_id: ID of the requested organization.
            role_id: ID of the requested role.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsRoles400Error1 |
                V1OrganizationsRoles500Error1 | RawError``."""
        return self._with_raw_response.organization_role_patch(
            organization_id, role_id, body=body, request_options=request_options
        ).unwrap()

    def organization_role_post(
        self,
        organization_id: UUID,
        *,
        body: RoleCreateRequest | RoleCreateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsRolesResponse1:
        """Creates a new custom role for an organization with specified policies and actors.

        Args:
            organization_id: ID of the requested organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsRoles400Error1 |
                V1OrganizationsRoles500Error1 | RawError``."""
        return self._with_raw_response.organization_role_post(
            organization_id, body=body, request_options=request_options
        ).unwrap()

    def organization_roles_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsRolesResponse:
        """Returns all available roles (system + custom) for an organization.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsRoles400Error1 |
                V1OrganizationsRoles500Error1 | RawError``."""
        return self._with_raw_response.organization_roles_get_list(
            organization_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> RoleManagementWithRawResponse:
        return self._with_raw_response


class AsyncRoleManagement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncRoleManagementWithRawResponse(client, server, auth)

    async def organization_role_delete(
        self, organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsRolesResponse4:
        """Deletes an existing custom role. System roles cannot be deleted. This operation will remove the role and all
        its associated policies.

        Args:
            organization_id: ID of the requested organization.
            role_id: ID of the requested role.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsRoles400Error1 |
                V1OrganizationsRoles500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_role_delete(
                organization_id, role_id, request_options=request_options
            )
        ).unwrap()

    async def organization_role_get(
        self, organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsRolesResponse1:
        """Returns details for a specific role.

        Args:
            organization_id: ID of the requested organization.
            role_id: ID of the requested role.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsRoles400Error1 |
                V1OrganizationsRoles500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_role_get(
                organization_id, role_id, request_options=request_options
            )
        ).unwrap()

    async def organization_role_patch(
        self,
        organization_id: UUID,
        role_id: UUID,
        *,
        body: RoleUpdateRequest | RoleUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsRolesResponse1:
        """Updates an existing custom role. System roles cannot be updated. All fields are optional - only provided
        fields will be updated.

        Args:
            organization_id: ID of the requested organization.
            role_id: ID of the requested role.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsRoles400Error1 |
                V1OrganizationsRoles500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_role_patch(
                organization_id, role_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def organization_role_post(
        self,
        organization_id: UUID,
        *,
        body: RoleCreateRequest | RoleCreateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsRolesResponse1:
        """Creates a new custom role for an organization with specified policies and actors.

        Args:
            organization_id: ID of the requested organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsRoles400Error1 |
                V1OrganizationsRoles500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_role_post(
                organization_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def organization_roles_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsRolesResponse:
        """Returns all available roles (system + custom) for an organization.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsRoles400Error1 |
                V1OrganizationsRoles500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_roles_get_list(organization_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncRoleManagementWithRawResponse:
        return self._with_raw_response


class RoleManagementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def organization_role_delete(
        self, organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsRolesResponse4, OrganizationRoleDeleteErrorBody]:
        """Deletes an existing custom role. System roles cannot be deleted. This operation will remove the role and all
        its associated policies.

        Args:
            organization_id: ID of the requested organization.
            role_id: ID of the requested role.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/roles/{roleId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("roleId", role_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsRolesResponse4],
            error_mapper=organization_role_delete_error_mapper,
            request_options=request_options,
        )

    def organization_role_get(
        self, organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsRolesResponse1, OrganizationRoleGetErrorBody]:
        """Returns details for a specific role.

        Args:
            organization_id: ID of the requested organization.
            role_id: ID of the requested role.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/roles/{roleId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("roleId", role_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsRolesResponse1],
            error_mapper=organization_role_get_error_mapper,
            request_options=request_options,
        )

    def organization_role_patch(
        self,
        organization_id: UUID,
        role_id: UUID,
        *,
        body: RoleUpdateRequest | RoleUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsRolesResponse1, OrganizationRolePatchErrorBody]:
        """Updates an existing custom role. System roles cannot be updated. All fields are optional - only provided
        fields will be updated.

        Args:
            organization_id: ID of the requested organization.
            role_id: ID of the requested role.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/roles/{roleId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("roleId", role_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RoleUpdateRequest | RoleUpdateRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsRolesResponse1],
            error_mapper=organization_role_patch_error_mapper,
            request_options=request_options,
        )

    def organization_role_post(
        self,
        organization_id: UUID,
        *,
        body: RoleCreateRequest | RoleCreateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsRolesResponse1, OrganizationRolePostErrorBody]:
        """Creates a new custom role for an organization with specified policies and actors.

        Args:
            organization_id: ID of the requested organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/roles"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RoleCreateRequest | RoleCreateRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsRolesResponse1],
            error_mapper=organization_role_post_error_mapper,
            request_options=request_options,
        )

    def organization_roles_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsRolesResponse, OrganizationRolesGetListErrorBody]:
        """Returns all available roles (system + custom) for an organization.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/roles"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsRolesResponse],
            error_mapper=organization_roles_get_list_error_mapper,
            request_options=request_options,
        )


class AsyncRoleManagementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def organization_role_delete(
        self, organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsRolesResponse4, OrganizationRoleDeleteErrorBody]:
        """Deletes an existing custom role. System roles cannot be deleted. This operation will remove the role and all
        its associated policies.

        Args:
            organization_id: ID of the requested organization.
            role_id: ID of the requested role.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/roles/{roleId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("roleId", role_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsRolesResponse4],
            error_mapper=organization_role_delete_error_mapper,
            request_options=request_options,
        )

    async def organization_role_get(
        self, organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsRolesResponse1, OrganizationRoleGetErrorBody]:
        """Returns details for a specific role.

        Args:
            organization_id: ID of the requested organization.
            role_id: ID of the requested role.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/roles/{roleId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("roleId", role_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsRolesResponse1],
            error_mapper=organization_role_get_error_mapper,
            request_options=request_options,
        )

    async def organization_role_patch(
        self,
        organization_id: UUID,
        role_id: UUID,
        *,
        body: RoleUpdateRequest | RoleUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsRolesResponse1, OrganizationRolePatchErrorBody]:
        """Updates an existing custom role. System roles cannot be updated. All fields are optional - only provided
        fields will be updated.

        Args:
            organization_id: ID of the requested organization.
            role_id: ID of the requested role.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/roles/{roleId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("roleId", role_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RoleUpdateRequest | RoleUpdateRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsRolesResponse1],
            error_mapper=organization_role_patch_error_mapper,
            request_options=request_options,
        )

    async def organization_role_post(
        self,
        organization_id: UUID,
        *,
        body: RoleCreateRequest | RoleCreateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsRolesResponse1, OrganizationRolePostErrorBody]:
        """Creates a new custom role for an organization with specified policies and actors.

        Args:
            organization_id: ID of the requested organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/roles"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RoleCreateRequest | RoleCreateRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsRolesResponse1],
            error_mapper=organization_role_post_error_mapper,
            request_options=request_options,
        )

    async def organization_roles_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsRolesResponse, OrganizationRolesGetListErrorBody]:
        """Returns all available roles (system + custom) for an organization.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/roles"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsRolesResponse],
            error_mapper=organization_roles_get_list_error_mapper,
            request_options=request_options,
        )
