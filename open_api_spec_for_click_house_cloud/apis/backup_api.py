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
from ..errors.backup_bucket_create_error import BackupBucketCreateErrorBody, backup_bucket_create_error_mapper
from ..errors.backup_bucket_delete_error import BackupBucketDeleteErrorBody, backup_bucket_delete_error_mapper
from ..errors.backup_bucket_get_error import BackupBucketGetErrorBody, backup_bucket_get_error_mapper
from ..errors.backup_bucket_update_error import BackupBucketUpdateErrorBody, backup_bucket_update_error_mapper
from ..errors.backup_configuration_get_error import (
    BackupConfigurationGetErrorBody,
    backup_configuration_get_error_mapper,
)
from ..errors.backup_configuration_update_error import (
    BackupConfigurationUpdateErrorBody,
    backup_configuration_update_error_mapper,
)
from ..errors.backup_get_error import BackupGetErrorBody, backup_get_error_mapper
from ..errors.backup_get_list_error import BackupGetListErrorBody, backup_get_list_error_mapper
from ..models.backup_configuration_patch_request import (
    BackupConfigurationPatchRequest,
    BackupConfigurationPatchRequestDict,
)
from ..models.unions.backup_bucket_patch_request import BackupBucketPatchRequest, BackupBucketPatchRequestDict
from ..models.unions.backup_bucket_post_request import BackupBucketPostRequest, BackupBucketPostRequestDict
from ..models.v1_organizations_services_backup_bucket_response import V1OrganizationsServicesBackupBucketResponse
from ..models.v1_organizations_services_backup_bucket_response3 import V1OrganizationsServicesBackupBucketResponse3
from ..models.v1_organizations_services_backup_configuration_response import (
    V1OrganizationsServicesBackupConfigurationResponse,
)
from ..models.v1_organizations_services_backups_backup_id_response import V1OrganizationsServicesBackupsBackupIdResponse
from ..models.v1_organizations_services_backups_response import V1OrganizationsServicesBackupsResponse
from ..server.server import Server


class BackupApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BackupApiWithRawResponse(client, server, auth)

    def backup_bucket_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: BackupBucketPostRequest | BackupBucketPostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesBackupBucketResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Create service backup bucket. Requires ADMIN auth key role.

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
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupBucket400Error1 |
                V1OrganizationsServicesBackupBucket500Error1 | RawError``."""
        return self._with_raw_response.backup_bucket_create(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def backup_bucket_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesBackupBucketResponse3:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Delete service backup bucket. Requires ADMIN auth key role.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupBucket400Error1 |
                V1OrganizationsServicesBackupBucket500Error1 | RawError``."""
        return self._with_raw_response.backup_bucket_delete(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def backup_bucket_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesBackupBucketResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns the service backup bucket.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupBucket400Error1 |
                V1OrganizationsServicesBackupBucket500Error1 | RawError``."""
        return self._with_raw_response.backup_bucket_get(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def backup_bucket_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: BackupBucketPatchRequest | BackupBucketPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesBackupBucketResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Update service backup bucket. Requires ADMIN auth key role. The secrets of the specified bucket
        provider are always required

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
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupBucket400Error1 |
                V1OrganizationsServicesBackupBucket500Error1 | RawError``."""
        return self._with_raw_response.backup_bucket_update(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def backup_configuration_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesBackupConfigurationResponse:
        """Returns the service backup configuration.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupConfiguration400Error1 |
                V1OrganizationsServicesBackupConfiguration500Error1 | RawError``."""
        return self._with_raw_response.backup_configuration_get(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def backup_configuration_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: BackupConfigurationPatchRequest | BackupConfigurationPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesBackupConfigurationResponse:
        """Updates service backup configuration. Requires ADMIN auth key role. Setting the properties with null value,
        will reset the properties to theirs default values.

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
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupConfiguration400Error1 |
                V1OrganizationsServicesBackupConfiguration500Error1 | RawError``."""
        return self._with_raw_response.backup_configuration_update(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def backup_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        backup_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesBackupsBackupIdResponse:
        """Returns a single backup info.

        Args:
            organization_id: ID of the organization that owns the backup.
            service_id: ID of the service the backup was created from.
            backup_id: ID of the requested backup.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupsBackupId400Error1 |
                V1OrganizationsServicesBackupsBackupId500Error1 | RawError``."""
        return self._with_raw_response.backup_get(
            organization_id, service_id, backup_id, request_options=request_options
        ).unwrap()

    def backup_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesBackupsResponse:
        """Returns a list of all backups for the service. The most recent backups comes first in the list.

        Args:
            organization_id: ID of the organization that owns the backup.
            service_id: ID of the service the backup was created from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackups400Error1 |
                V1OrganizationsServicesBackups500Error1 | RawError``."""
        return self._with_raw_response.backup_get_list(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> BackupApiWithRawResponse:
        return self._with_raw_response


class AsyncBackupApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBackupApiWithRawResponse(client, server, auth)

    async def backup_bucket_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: BackupBucketPostRequest | BackupBucketPostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesBackupBucketResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Create service backup bucket. Requires ADMIN auth key role.

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
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupBucket400Error1 |
                V1OrganizationsServicesBackupBucket500Error1 | RawError``."""
        return (
            await self._with_raw_response.backup_bucket_create(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def backup_bucket_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesBackupBucketResponse3:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Delete service backup bucket. Requires ADMIN auth key role.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupBucket400Error1 |
                V1OrganizationsServicesBackupBucket500Error1 | RawError``."""
        return (
            await self._with_raw_response.backup_bucket_delete(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def backup_bucket_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesBackupBucketResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns the service backup bucket.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupBucket400Error1 |
                V1OrganizationsServicesBackupBucket500Error1 | RawError``."""
        return (
            await self._with_raw_response.backup_bucket_get(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def backup_bucket_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: BackupBucketPatchRequest | BackupBucketPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesBackupBucketResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Update service backup bucket. Requires ADMIN auth key role. The secrets of the specified bucket
        provider are always required

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
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupBucket400Error1 |
                V1OrganizationsServicesBackupBucket500Error1 | RawError``."""
        return (
            await self._with_raw_response.backup_bucket_update(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def backup_configuration_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesBackupConfigurationResponse:
        """Returns the service backup configuration.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupConfiguration400Error1 |
                V1OrganizationsServicesBackupConfiguration500Error1 | RawError``."""
        return (
            await self._with_raw_response.backup_configuration_get(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def backup_configuration_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: BackupConfigurationPatchRequest | BackupConfigurationPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesBackupConfigurationResponse:
        """Updates service backup configuration. Requires ADMIN auth key role. Setting the properties with null value,
        will reset the properties to theirs default values.

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
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupConfiguration400Error1 |
                V1OrganizationsServicesBackupConfiguration500Error1 | RawError``."""
        return (
            await self._with_raw_response.backup_configuration_update(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def backup_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        backup_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesBackupsBackupIdResponse:
        """Returns a single backup info.

        Args:
            organization_id: ID of the organization that owns the backup.
            service_id: ID of the service the backup was created from.
            backup_id: ID of the requested backup.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackupsBackupId400Error1 |
                V1OrganizationsServicesBackupsBackupId500Error1 | RawError``."""
        return (
            await self._with_raw_response.backup_get(
                organization_id, service_id, backup_id, request_options=request_options
            )
        ).unwrap()

    async def backup_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesBackupsResponse:
        """Returns a list of all backups for the service. The most recent backups comes first in the list.

        Args:
            organization_id: ID of the organization that owns the backup.
            service_id: ID of the service the backup was created from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesBackups400Error1 |
                V1OrganizationsServicesBackups500Error1 | RawError``."""
        return (
            await self._with_raw_response.backup_get_list(organization_id, service_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncBackupApiWithRawResponse:
        return self._with_raw_response


class BackupApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def backup_bucket_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: BackupBucketPostRequest | BackupBucketPostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesBackupBucketResponse, BackupBucketCreateErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Create service backup bucket. Requires ADMIN auth key role.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/backupBucket"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BackupBucketPostRequest | BackupBucketPostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupBucketResponse],
            error_mapper=backup_bucket_create_error_mapper,
            request_options=request_options,
        )

    def backup_bucket_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesBackupBucketResponse3, BackupBucketDeleteErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Delete service backup bucket. Requires ADMIN auth key role.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/backupBucket"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupBucketResponse3],
            error_mapper=backup_bucket_delete_error_mapper,
            request_options=request_options,
        )

    def backup_bucket_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesBackupBucketResponse, BackupBucketGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns the service backup bucket.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/backupBucket"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupBucketResponse],
            error_mapper=backup_bucket_get_error_mapper,
            request_options=request_options,
        )

    def backup_bucket_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: BackupBucketPatchRequest | BackupBucketPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesBackupBucketResponse, BackupBucketUpdateErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Update service backup bucket. Requires ADMIN auth key role. The secrets of the specified bucket
        provider are always required

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/backupBucket"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BackupBucketPatchRequest | BackupBucketPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupBucketResponse],
            error_mapper=backup_bucket_update_error_mapper,
            request_options=request_options,
        )

    def backup_configuration_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesBackupConfigurationResponse, BackupConfigurationGetErrorBody]:
        """Returns the service backup configuration.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/backupConfiguration"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupConfigurationResponse],
            error_mapper=backup_configuration_get_error_mapper,
            request_options=request_options,
        )

    def backup_configuration_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: BackupConfigurationPatchRequest | BackupConfigurationPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesBackupConfigurationResponse, BackupConfigurationUpdateErrorBody]:
        """Updates service backup configuration. Requires ADMIN auth key role. Setting the properties with null value,
        will reset the properties to theirs default values.

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
                "/v1/organizations/{organizationId}/services/{serviceId}/backupConfiguration"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BackupConfigurationPatchRequest | BackupConfigurationPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupConfigurationResponse],
            error_mapper=backup_configuration_update_error_mapper,
            request_options=request_options,
        )

    def backup_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        backup_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesBackupsBackupIdResponse, BackupGetErrorBody]:
        """Returns a single backup info.

        Args:
            organization_id: ID of the organization that owns the backup.
            service_id: ID of the service the backup was created from.
            backup_id: ID of the requested backup.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/backups/{backupId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("backupId", backup_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupsBackupIdResponse],
            error_mapper=backup_get_error_mapper,
            request_options=request_options,
        )

    def backup_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesBackupsResponse, BackupGetListErrorBody]:
        """Returns a list of all backups for the service. The most recent backups comes first in the list.

        Args:
            organization_id: ID of the organization that owns the backup.
            service_id: ID of the service the backup was created from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/backups"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupsResponse],
            error_mapper=backup_get_list_error_mapper,
            request_options=request_options,
        )


class AsyncBackupApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def backup_bucket_create(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: BackupBucketPostRequest | BackupBucketPostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesBackupBucketResponse, BackupBucketCreateErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Create service backup bucket. Requires ADMIN auth key role.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/backupBucket"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BackupBucketPostRequest | BackupBucketPostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupBucketResponse],
            error_mapper=backup_bucket_create_error_mapper,
            request_options=request_options,
        )

    async def backup_bucket_delete(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesBackupBucketResponse3, BackupBucketDeleteErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Delete service backup bucket. Requires ADMIN auth key role.

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/backupBucket"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupBucketResponse3],
            error_mapper=backup_bucket_delete_error_mapper,
            request_options=request_options,
        )

    async def backup_bucket_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesBackupBucketResponse, BackupBucketGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns the service backup bucket.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/backupBucket"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupBucketResponse],
            error_mapper=backup_bucket_get_error_mapper,
            request_options=request_options,
        )

    async def backup_bucket_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: BackupBucketPatchRequest | BackupBucketPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesBackupBucketResponse, BackupBucketUpdateErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Update service backup bucket. Requires ADMIN auth key role. The secrets of the specified bucket
        provider are always required

        Args:
            organization_id: ID of the requested organization.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/backupBucket"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BackupBucketPatchRequest | BackupBucketPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupBucketResponse],
            error_mapper=backup_bucket_update_error_mapper,
            request_options=request_options,
        )

    async def backup_configuration_get(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesBackupConfigurationResponse, BackupConfigurationGetErrorBody]:
        """Returns the service backup configuration.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/backupConfiguration"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupConfigurationResponse],
            error_mapper=backup_configuration_get_error_mapper,
            request_options=request_options,
        )

    async def backup_configuration_update(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: BackupConfigurationPatchRequest | BackupConfigurationPatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesBackupConfigurationResponse, BackupConfigurationUpdateErrorBody]:
        """Updates service backup configuration. Requires ADMIN auth key role. Setting the properties with null value,
        will reset the properties to theirs default values.

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
                "/v1/organizations/{organizationId}/services/{serviceId}/backupConfiguration"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BackupConfigurationPatchRequest | BackupConfigurationPatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupConfigurationResponse],
            error_mapper=backup_configuration_update_error_mapper,
            request_options=request_options,
        )

    async def backup_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        backup_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesBackupsBackupIdResponse, BackupGetErrorBody]:
        """Returns a single backup info.

        Args:
            organization_id: ID of the organization that owns the backup.
            service_id: ID of the service the backup was created from.
            backup_id: ID of the requested backup.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/backups/{backupId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[UUID]("backupId", backup_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupsBackupIdResponse],
            error_mapper=backup_get_error_mapper,
            request_options=request_options,
        )

    async def backup_get_list(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesBackupsResponse, BackupGetListErrorBody]:
        """Returns a list of all backups for the service. The most recent backups comes first in the list.

        Args:
            organization_id: ID of the organization that owns the backup.
            service_id: ID of the service the backup was created from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/backups"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesBackupsResponse],
            error_mapper=backup_get_list_error_mapper,
            request_options=request_options,
        )
