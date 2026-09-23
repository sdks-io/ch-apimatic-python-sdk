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
from ..errors.invitation_create_error import InvitationCreateErrorBody, invitation_create_error_mapper
from ..errors.invitation_delete_error import InvitationDeleteErrorBody, invitation_delete_error_mapper
from ..errors.invitation_get_error import InvitationGetErrorBody, invitation_get_error_mapper
from ..errors.invitation_get_list_error import InvitationGetListErrorBody, invitation_get_list_error_mapper
from ..errors.member_delete_error import MemberDeleteErrorBody, member_delete_error_mapper
from ..errors.member_get_error import MemberGetErrorBody, member_get_error_mapper
from ..errors.member_get_list_error import MemberGetListErrorBody, member_get_list_error_mapper
from ..errors.member_update_error import MemberUpdateErrorBody, member_update_error_mapper
from ..models.invitation_post_request import InvitationPostRequest, InvitationPostRequestDict
from ..models.member_patch_request import MemberPatchRequest, MemberPatchRequestDict
from ..models.v1_organizations_invitations_response import V1OrganizationsInvitationsResponse
from ..models.v1_organizations_invitations_response1 import V1OrganizationsInvitationsResponse1
from ..models.v1_organizations_invitations_response3 import V1OrganizationsInvitationsResponse3
from ..models.v1_organizations_members_response import V1OrganizationsMembersResponse
from ..models.v1_organizations_members_response1 import V1OrganizationsMembersResponse1
from ..models.v1_organizations_members_response3 import V1OrganizationsMembersResponse3
from ..server.server import Server


class UserManagement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UserManagementWithRawResponse(client, server, auth)

    def invitation_create(
        self,
        organization_id: UUID,
        *,
        body: InvitationPostRequest | InvitationPostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsInvitationsResponse1:
        """Creates organization invitation.

        Args:
            organization_id: ID of the organization to invite a user to.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsInvitations400Error1 |
                V1OrganizationsInvitations500Error1 | RawError``."""
        return self._with_raw_response.invitation_create(
            organization_id, body=body, request_options=request_options
        ).unwrap()

    def invitation_delete(
        self, organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsInvitationsResponse3:
        """Deletes a single organization invitation.

        Args:
            organization_id: ID of the organization that has the invitation.
            invitation_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsInvitations400Error1 |
                V1OrganizationsInvitations500Error1 | RawError``."""
        return self._with_raw_response.invitation_delete(
            organization_id, invitation_id, request_options=request_options
        ).unwrap()

    def invitation_get(
        self, organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsInvitationsResponse1:
        """Returns details for a single organization invitation.

        Args:
            organization_id: ID of the requested organization.
            invitation_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsInvitations400Error1 |
                V1OrganizationsInvitations500Error1 | RawError``."""
        return self._with_raw_response.invitation_get(
            organization_id, invitation_id, request_options=request_options
        ).unwrap()

    def invitation_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsInvitationsResponse:
        """Returns list of all organization invitations.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsInvitations400Error1 |
                V1OrganizationsInvitations500Error1 | RawError``."""
        return self._with_raw_response.invitation_get_list(organization_id, request_options=request_options).unwrap()

    def member_delete(
        self, organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsMembersResponse3:
        """Removes a user from the organization

        Args:
            organization_id: ID of the requested organization.
            user_id: ID of the requested user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsMembers400Error1 |
                V1OrganizationsMembers500Error1 | RawError``."""
        return self._with_raw_response.member_delete(organization_id, user_id, request_options=request_options).unwrap()

    def member_get(
        self, organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsMembersResponse1:
        """Returns a single organization member details.

        Args:
            organization_id: ID of the organization the member is part of.
            user_id: ID of the requested user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsMembers400Error1 |
                V1OrganizationsMembers500Error1 | RawError``."""
        return self._with_raw_response.member_get(organization_id, user_id, request_options=request_options).unwrap()

    def member_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsMembersResponse:
        """Returns a list of all members in the organization.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsMembers400Error1 |
                V1OrganizationsMembers500Error1 | RawError``."""
        return self._with_raw_response.member_get_list(organization_id, request_options=request_options).unwrap()

    def member_update(
        self,
        organization_id: UUID,
        user_id: UUID,
        *,
        body: MemberPatchRequest | MemberPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsMembersResponse1:
        """Updates organization member role.

        Args:
            organization_id: ID of the organization the member is part of.
            user_id: ID of the user to patch
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsMembers400Error1 |
                V1OrganizationsMembers500Error1 | RawError``."""
        return self._with_raw_response.member_update(
            organization_id, user_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> UserManagementWithRawResponse:
        return self._with_raw_response


class AsyncUserManagement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUserManagementWithRawResponse(client, server, auth)

    async def invitation_create(
        self,
        organization_id: UUID,
        *,
        body: InvitationPostRequest | InvitationPostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsInvitationsResponse1:
        """Creates organization invitation.

        Args:
            organization_id: ID of the organization to invite a user to.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsInvitations400Error1 |
                V1OrganizationsInvitations500Error1 | RawError``."""
        return (
            await self._with_raw_response.invitation_create(organization_id, body=body, request_options=request_options)
        ).unwrap()

    async def invitation_delete(
        self, organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsInvitationsResponse3:
        """Deletes a single organization invitation.

        Args:
            organization_id: ID of the organization that has the invitation.
            invitation_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsInvitations400Error1 |
                V1OrganizationsInvitations500Error1 | RawError``."""
        return (
            await self._with_raw_response.invitation_delete(
                organization_id, invitation_id, request_options=request_options
            )
        ).unwrap()

    async def invitation_get(
        self, organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsInvitationsResponse1:
        """Returns details for a single organization invitation.

        Args:
            organization_id: ID of the requested organization.
            invitation_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsInvitations400Error1 |
                V1OrganizationsInvitations500Error1 | RawError``."""
        return (
            await self._with_raw_response.invitation_get(
                organization_id, invitation_id, request_options=request_options
            )
        ).unwrap()

    async def invitation_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsInvitationsResponse:
        """Returns list of all organization invitations.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsInvitations400Error1 |
                V1OrganizationsInvitations500Error1 | RawError``."""
        return (
            await self._with_raw_response.invitation_get_list(organization_id, request_options=request_options)
        ).unwrap()

    async def member_delete(
        self, organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsMembersResponse3:
        """Removes a user from the organization

        Args:
            organization_id: ID of the requested organization.
            user_id: ID of the requested user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsMembers400Error1 |
                V1OrganizationsMembers500Error1 | RawError``."""
        return (
            await self._with_raw_response.member_delete(organization_id, user_id, request_options=request_options)
        ).unwrap()

    async def member_get(
        self, organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsMembersResponse1:
        """Returns a single organization member details.

        Args:
            organization_id: ID of the organization the member is part of.
            user_id: ID of the requested user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsMembers400Error1 |
                V1OrganizationsMembers500Error1 | RawError``."""
        return (
            await self._with_raw_response.member_get(organization_id, user_id, request_options=request_options)
        ).unwrap()

    async def member_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsMembersResponse:
        """Returns a list of all members in the organization.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsMembers400Error1 |
                V1OrganizationsMembers500Error1 | RawError``."""
        return (
            await self._with_raw_response.member_get_list(organization_id, request_options=request_options)
        ).unwrap()

    async def member_update(
        self,
        organization_id: UUID,
        user_id: UUID,
        *,
        body: MemberPatchRequest | MemberPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsMembersResponse1:
        """Updates organization member role.

        Args:
            organization_id: ID of the organization the member is part of.
            user_id: ID of the user to patch
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsMembers400Error1 |
                V1OrganizationsMembers500Error1 | RawError``."""
        return (
            await self._with_raw_response.member_update(
                organization_id, user_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUserManagementWithRawResponse:
        return self._with_raw_response


class UserManagementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def invitation_create(
        self,
        organization_id: UUID,
        *,
        body: InvitationPostRequest | InvitationPostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsInvitationsResponse1, InvitationCreateErrorBody]:
        """Creates organization invitation.

        Args:
            organization_id: ID of the organization to invite a user to.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/invitations"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InvitationPostRequest | InvitationPostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsInvitationsResponse1],
            error_mapper=invitation_create_error_mapper,
            request_options=request_options,
        )

    def invitation_delete(
        self, organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsInvitationsResponse3, InvitationDeleteErrorBody]:
        """Deletes a single organization invitation.

        Args:
            organization_id: ID of the organization that has the invitation.
            invitation_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/invitations/{invitationId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("invitationId", invitation_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsInvitationsResponse3],
            error_mapper=invitation_delete_error_mapper,
            request_options=request_options,
        )

    def invitation_get(
        self, organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsInvitationsResponse1, InvitationGetErrorBody]:
        """Returns details for a single organization invitation.

        Args:
            organization_id: ID of the requested organization.
            invitation_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/invitations/{invitationId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("invitationId", invitation_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsInvitationsResponse1],
            error_mapper=invitation_get_error_mapper,
            request_options=request_options,
        )

    def invitation_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsInvitationsResponse, InvitationGetListErrorBody]:
        """Returns list of all organization invitations.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/invitations"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsInvitationsResponse],
            error_mapper=invitation_get_list_error_mapper,
            request_options=request_options,
        )

    def member_delete(
        self, organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsMembersResponse3, MemberDeleteErrorBody]:
        """Removes a user from the organization

        Args:
            organization_id: ID of the requested organization.
            user_id: ID of the requested user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/members/{userId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("userId", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsMembersResponse3],
            error_mapper=member_delete_error_mapper,
            request_options=request_options,
        )

    def member_get(
        self, organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsMembersResponse1, MemberGetErrorBody]:
        """Returns a single organization member details.

        Args:
            organization_id: ID of the organization the member is part of.
            user_id: ID of the requested user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/members/{userId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("userId", user_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsMembersResponse1],
            error_mapper=member_get_error_mapper,
            request_options=request_options,
        )

    def member_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsMembersResponse, MemberGetListErrorBody]:
        """Returns a list of all members in the organization.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/members"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsMembersResponse],
            error_mapper=member_get_list_error_mapper,
            request_options=request_options,
        )

    def member_update(
        self,
        organization_id: UUID,
        user_id: UUID,
        *,
        body: MemberPatchRequest | MemberPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsMembersResponse1, MemberUpdateErrorBody]:
        """Updates organization member role.

        Args:
            organization_id: ID of the organization the member is part of.
            user_id: ID of the user to patch
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/members/{userId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("userId", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MemberPatchRequest | MemberPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsMembersResponse1],
            error_mapper=member_update_error_mapper,
            request_options=request_options,
        )


class AsyncUserManagementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def invitation_create(
        self,
        organization_id: UUID,
        *,
        body: InvitationPostRequest | InvitationPostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsInvitationsResponse1, InvitationCreateErrorBody]:
        """Creates organization invitation.

        Args:
            organization_id: ID of the organization to invite a user to.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/invitations"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[InvitationPostRequest | InvitationPostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsInvitationsResponse1],
            error_mapper=invitation_create_error_mapper,
            request_options=request_options,
        )

    async def invitation_delete(
        self, organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsInvitationsResponse3, InvitationDeleteErrorBody]:
        """Deletes a single organization invitation.

        Args:
            organization_id: ID of the organization that has the invitation.
            invitation_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/invitations/{invitationId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("invitationId", invitation_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsInvitationsResponse3],
            error_mapper=invitation_delete_error_mapper,
            request_options=request_options,
        )

    async def invitation_get(
        self, organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsInvitationsResponse1, InvitationGetErrorBody]:
        """Returns details for a single organization invitation.

        Args:
            organization_id: ID of the requested organization.
            invitation_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/invitations/{invitationId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("invitationId", invitation_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsInvitationsResponse1],
            error_mapper=invitation_get_error_mapper,
            request_options=request_options,
        )

    async def invitation_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsInvitationsResponse, InvitationGetListErrorBody]:
        """Returns list of all organization invitations.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/invitations"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsInvitationsResponse],
            error_mapper=invitation_get_list_error_mapper,
            request_options=request_options,
        )

    async def member_delete(
        self, organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsMembersResponse3, MemberDeleteErrorBody]:
        """Removes a user from the organization

        Args:
            organization_id: ID of the requested organization.
            user_id: ID of the requested user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/members/{userId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("userId", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsMembersResponse3],
            error_mapper=member_delete_error_mapper,
            request_options=request_options,
        )

    async def member_get(
        self, organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsMembersResponse1, MemberGetErrorBody]:
        """Returns a single organization member details.

        Args:
            organization_id: ID of the organization the member is part of.
            user_id: ID of the requested user.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/members/{userId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("userId", user_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsMembersResponse1],
            error_mapper=member_get_error_mapper,
            request_options=request_options,
        )

    async def member_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsMembersResponse, MemberGetListErrorBody]:
        """Returns a list of all members in the organization.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/members"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsMembersResponse],
            error_mapper=member_get_list_error_mapper,
            request_options=request_options,
        )

    async def member_update(
        self,
        organization_id: UUID,
        user_id: UUID,
        *,
        body: MemberPatchRequest | MemberPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsMembersResponse1, MemberUpdateErrorBody]:
        """Updates organization member role.

        Args:
            organization_id: ID of the organization the member is part of.
            user_id: ID of the user to patch
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/members/{userId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("userId", user_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MemberPatchRequest | MemberPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsMembersResponse1],
            error_mapper=member_update_error_mapper,
            request_options=request_options,
        )
