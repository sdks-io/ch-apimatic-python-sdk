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
from ..errors.udf_attach_error import UdfAttachErrorBody, udf_attach_error_mapper
from ..errors.udf_attachment_get_error import UdfAttachmentGetErrorBody, udf_attachment_get_error_mapper
from ..errors.udf_attachment_list_error import UdfAttachmentListErrorBody, udf_attachment_list_error_mapper
from ..errors.udf_create_error import UdfCreateErrorBody, udf_create_error_mapper
from ..errors.udf_delete_error import UdfDeleteErrorBody, udf_delete_error_mapper
from ..errors.udf_detach_error import UdfDetachErrorBody, udf_detach_error_mapper
from ..errors.udf_get_error import UdfGetErrorBody, udf_get_error_mapper
from ..errors.udf_list_error import UdfListErrorBody, udf_list_error_mapper
from ..errors.udf_upload_session_create_error import (
    UdfUploadSessionCreateErrorBody,
    udf_upload_session_create_error_mapper,
)
from ..errors.udf_version_create_error import UdfVersionCreateErrorBody, udf_version_create_error_mapper
from ..errors.udf_version_delete_error import UdfVersionDeleteErrorBody, udf_version_delete_error_mapper
from ..errors.udf_version_list_error import UdfVersionListErrorBody, udf_version_list_error_mapper
from ..models.unions.udf_create_request2 import UdfCreateRequest2, UdfCreateRequest2Dict
from ..models.unions.udf_version_create_request2 import UdfVersionCreateRequest2, UdfVersionCreateRequest2Dict
from ..models.v1_organizations_udf_uploads_url_response import V1OrganizationsUdfUploadsUrlResponse
from ..models.v1_organizations_udfs_attachments_response import V1OrganizationsUdfsAttachmentsResponse
from ..models.v1_organizations_udfs_attachments_service_id_request import (
    V1OrganizationsUdfsAttachmentsServiceIdRequest,
    V1OrganizationsUdfsAttachmentsServiceIdRequestDict,
)
from ..models.v1_organizations_udfs_attachments_service_id_response import (
    V1OrganizationsUdfsAttachmentsServiceIdResponse,
)
from ..models.v1_organizations_udfs_attachments_service_id_response2 import (
    V1OrganizationsUdfsAttachmentsServiceIdResponse2,
)
from ..models.v1_organizations_udfs_response import V1OrganizationsUdfsResponse
from ..models.v1_organizations_udfs_response1 import V1OrganizationsUdfsResponse1
from ..models.v1_organizations_udfs_response2 import V1OrganizationsUdfsResponse2
from ..models.v1_organizations_udfs_versions_response import V1OrganizationsUdfsVersionsResponse
from ..models.v1_organizations_udfs_versions_response1 import V1OrganizationsUdfsVersionsResponse1
from ..models.v1_organizations_udfs_versions_version_response import V1OrganizationsUdfsVersionsVersionResponse
from ..server.server import Server


class UdfApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UdfApiWithRawResponse(client, server, auth)

    def udf_attach(
        self,
        organization_id: UUID,
        function_name: str,
        service_id: UUID,
        *,
        body: (
            V1OrganizationsUdfsAttachmentsServiceIdRequest | V1OrganizationsUdfsAttachmentsServiceIdRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsAttachmentsServiceIdResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Attaches one UDF
        version to a service, replacing the current version when necessary. When version is omitted, the latest ready
        version is attached.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Current attachment state.

        Raises:
            ApiError: The service does not support UDFs. UDF, version, or service not found. The requested version is
                not ready or another attachment transition is in progress. Service UDF attachment limit exceeded. The
                service must be running before the UDF can be attached. An internal server error has occurred. If this
                issue persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsUdfsAttachmentsServiceId400Error1 | V1OrganizationsUdfsAttachmentsServiceId404Error1 |
                V1OrganizationsUdfsAttachmentsServiceId409Error1 | V1OrganizationsUdfsAttachmentsServiceId422Error1 |
                V1OrganizationsUdfsAttachmentsServiceId424Error1 | V1OrganizationsUdfsAttachmentsServiceId500Error1 |
                RawError``."""
        return self._with_raw_response.udf_attach(
            organization_id, function_name, service_id, body=body, request_options=request_options
        ).unwrap()

    def udf_attachment_get(
        self,
        organization_id: UUID,
        function_name: str,
        service_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsAttachmentsServiceIdResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current
        attachment of a UDF to one service.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF not found or not attached to this service. An internal server error has occurred. If this
                issue persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsUdfsAttachmentsServiceId400Error21 | V1OrganizationsUdfsAttachmentsServiceId404Error1 |
                V1OrganizationsUdfsAttachmentsServiceId500Error1 | RawError``."""
        return self._with_raw_response.udf_attachment_get(
            organization_id, function_name, service_id, request_options=request_options
        ).unwrap()

    def udf_attachment_list(
        self,
        organization_id: UUID,
        function_name: str,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsAttachmentsResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current
        service attachments for a UDF, with at most one attachment per service.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF not found. An internal server error has occurred. If this issue persists, please contact
                ClickHouse Cloud support for assistance. ``error`` is ``V1OrganizationsUdfsAttachments400Error1 |
                V1OrganizationsUdfsAttachments404Error1 | V1OrganizationsUdfsAttachments500Error1 | RawError``."""
        return self._with_raw_response.udf_attachment_list(
            organization_id, function_name, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def udf_create(
        self,
        organization_id: UUID,
        *,
        body: UdfCreateRequest2 | UdfCreateRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates a new UDF.
        See `User-defined functions in Cloud
        <https://clickhouse.com/docs/products/cloud/features/sql-console-features/user-defined-functions>`__.

        Args:
            organization_id: ID of the requested organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            UDF created and building.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. Requested UDF features are not enabled. The function name already exists. The source archive
                is unavailable. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsUdfs400Error1 | V1OrganizationsUdfs403Error1
                | V1OrganizationsUdfs409Error1 | V1OrganizationsUdfs410Error1 | V1OrganizationsUdfs500Error1 |
                RawError``."""
        return self._with_raw_response.udf_create(organization_id, body=body, request_options=request_options).unwrap()

    def udf_delete(
        self, organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsUdfsResponse2:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes every
        version of a UDF and detaches it from all services. Removal from services completes asynchronously.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            UDF deleted.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF not found. A UDF version is still building. An internal server error has occurred. If
                this issue persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsUdfs400Error1 | V1OrganizationsUdfs404Error1 | V1OrganizationsUdfs409Error1 |
                V1OrganizationsUdfs500Error1 | RawError``."""
        return self._with_raw_response.udf_delete(
            organization_id, function_name, request_options=request_options
        ).unwrap()

    def udf_detach(
        self,
        organization_id: UUID,
        function_name: str,
        service_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsAttachmentsServiceIdResponse2:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Detaches a UDF from
        a service.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            UDF detached.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF not found. An attachment transition is already in progress. An internal server error has
                occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsUdfsAttachmentsServiceId400Error21 | V1OrganizationsUdfsAttachmentsServiceId404Error1 |
                V1OrganizationsUdfsAttachmentsServiceId409Error1 | V1OrganizationsUdfsAttachmentsServiceId500Error1 |
                RawError``."""
        return self._with_raw_response.udf_detach(
            organization_id, function_name, service_id, request_options=request_options
        ).unwrap()

    def udf_get(
        self, organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsUdfsResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the latest
        version of a UDF.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF not found. An internal server error has occurred. If this issue persists, please contact
                ClickHouse Cloud support for assistance. ``error`` is ``V1OrganizationsUdfs400Error1 |
                V1OrganizationsUdfs404Error1 | V1OrganizationsUdfs500Error1 | RawError``."""
        return self._with_raw_response.udf_get(organization_id, function_name, request_options=request_options).unwrap()

    def udf_list(
        self,
        organization_id: UUID,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the latest
        version of each UDF in the organization.

        Args:
            organization_id: ID of the requested organization.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsUdfs400Error1 | V1OrganizationsUdfs500Error1
                | RawError``."""
        return self._with_raw_response.udf_list(
            organization_id, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def udf_upload_session_create(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsUdfUploadsUrlResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates an
        org-scoped presigned application/zip upload URL. Callers must use an upload ID for only one create or version
        attempt and request a new upload URL when retrying.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Upload URL created.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsUdfUploadsUrl400Error1 |
                V1OrganizationsUdfUploadsUrl500Error1 | RawError``."""
        return self._with_raw_response.udf_upload_session_create(
            organization_id, request_options=request_options
        ).unwrap()

    def udf_version_create(
        self,
        organization_id: UUID,
        function_name: str,
        *,
        body: UdfVersionCreateRequest2 | UdfVersionCreateRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsVersionsResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Consumes a source
        archive, assigns a version, and starts the UDF build. Optional configuration fields omitted from the request use
        the defaults documented in the request schema; values are not inherited from the previous version. Retry by
        requesting a new upload URL and re-uploading.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            UDF version created and building.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. Requested UDF features are not enabled. UDF not found. A concurrent request conflicted with
                this request. The source archive is unavailable. An internal server error has occurred. If this issue
                persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsUdfsVersions400Error1 | V1OrganizationsUdfsVersions403Error1 |
                V1OrganizationsUdfsVersions404Error1 | V1OrganizationsUdfsVersions409Error1 |
                V1OrganizationsUdfsVersions410Error1 | V1OrganizationsUdfsVersions500Error1 | RawError``."""
        return self._with_raw_response.udf_version_create(
            organization_id, function_name, body=body, request_options=request_options
        ).unwrap()

    def udf_version_delete(
        self,
        organization_id: UUID,
        function_name: str,
        version: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsVersionsVersionResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes a UDF
        version. The UDF must not be attached to any services.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            version: Version number of the UDF.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            UDF version deleted.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF or version not found. The UDF version is the latest version, is attached to a service, or
                is still building. An internal server error has occurred. If this issue persists, please contact
                ClickHouse Cloud support for assistance. ``error`` is ``V1OrganizationsUdfsVersionsVersion400Error1 |
                V1OrganizationsUdfsVersionsVersion404Error1 | V1OrganizationsUdfsVersionsVersion409Error1 |
                V1OrganizationsUdfsVersionsVersion500Error1 | RawError``."""
        return self._with_raw_response.udf_version_delete(
            organization_id, function_name, version, request_options=request_options
        ).unwrap()

    def udf_version_list(
        self,
        organization_id: UUID,
        function_name: str,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsVersionsResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns all
        versions of a UDF.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF not found. An internal server error has occurred. If this issue persists, please contact
                ClickHouse Cloud support for assistance. ``error`` is ``V1OrganizationsUdfsVersions400Error1 |
                V1OrganizationsUdfsVersions404Error1 | V1OrganizationsUdfsVersions500Error1 | RawError``."""
        return self._with_raw_response.udf_version_list(
            organization_id, function_name, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> UdfApiWithRawResponse:
        return self._with_raw_response


class AsyncUdfApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUdfApiWithRawResponse(client, server, auth)

    async def udf_attach(
        self,
        organization_id: UUID,
        function_name: str,
        service_id: UUID,
        *,
        body: (
            V1OrganizationsUdfsAttachmentsServiceIdRequest | V1OrganizationsUdfsAttachmentsServiceIdRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsAttachmentsServiceIdResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Attaches one UDF
        version to a service, replacing the current version when necessary. When version is omitted, the latest ready
        version is attached.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Current attachment state.

        Raises:
            ApiError: The service does not support UDFs. UDF, version, or service not found. The requested version is
                not ready or another attachment transition is in progress. Service UDF attachment limit exceeded. The
                service must be running before the UDF can be attached. An internal server error has occurred. If this
                issue persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsUdfsAttachmentsServiceId400Error1 | V1OrganizationsUdfsAttachmentsServiceId404Error1 |
                V1OrganizationsUdfsAttachmentsServiceId409Error1 | V1OrganizationsUdfsAttachmentsServiceId422Error1 |
                V1OrganizationsUdfsAttachmentsServiceId424Error1 | V1OrganizationsUdfsAttachmentsServiceId500Error1 |
                RawError``."""
        return (
            await self._with_raw_response.udf_attach(
                organization_id, function_name, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def udf_attachment_get(
        self,
        organization_id: UUID,
        function_name: str,
        service_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsAttachmentsServiceIdResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current
        attachment of a UDF to one service.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF not found or not attached to this service. An internal server error has occurred. If this
                issue persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsUdfsAttachmentsServiceId400Error21 | V1OrganizationsUdfsAttachmentsServiceId404Error1 |
                V1OrganizationsUdfsAttachmentsServiceId500Error1 | RawError``."""
        return (
            await self._with_raw_response.udf_attachment_get(
                organization_id, function_name, service_id, request_options=request_options
            )
        ).unwrap()

    async def udf_attachment_list(
        self,
        organization_id: UUID,
        function_name: str,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsAttachmentsResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current
        service attachments for a UDF, with at most one attachment per service.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF not found. An internal server error has occurred. If this issue persists, please contact
                ClickHouse Cloud support for assistance. ``error`` is ``V1OrganizationsUdfsAttachments400Error1 |
                V1OrganizationsUdfsAttachments404Error1 | V1OrganizationsUdfsAttachments500Error1 | RawError``."""
        return (
            await self._with_raw_response.udf_attachment_list(
                organization_id, function_name, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def udf_create(
        self,
        organization_id: UUID,
        *,
        body: UdfCreateRequest2 | UdfCreateRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates a new UDF.
        See `User-defined functions in Cloud
        <https://clickhouse.com/docs/products/cloud/features/sql-console-features/user-defined-functions>`__.

        Args:
            organization_id: ID of the requested organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            UDF created and building.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. Requested UDF features are not enabled. The function name already exists. The source archive
                is unavailable. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsUdfs400Error1 | V1OrganizationsUdfs403Error1
                | V1OrganizationsUdfs409Error1 | V1OrganizationsUdfs410Error1 | V1OrganizationsUdfs500Error1 |
                RawError``."""
        return (
            await self._with_raw_response.udf_create(organization_id, body=body, request_options=request_options)
        ).unwrap()

    async def udf_delete(
        self, organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsUdfsResponse2:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes every
        version of a UDF and detaches it from all services. Removal from services completes asynchronously.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            UDF deleted.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF not found. A UDF version is still building. An internal server error has occurred. If
                this issue persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsUdfs400Error1 | V1OrganizationsUdfs404Error1 | V1OrganizationsUdfs409Error1 |
                V1OrganizationsUdfs500Error1 | RawError``."""
        return (
            await self._with_raw_response.udf_delete(organization_id, function_name, request_options=request_options)
        ).unwrap()

    async def udf_detach(
        self,
        organization_id: UUID,
        function_name: str,
        service_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsAttachmentsServiceIdResponse2:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Detaches a UDF from
        a service.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            UDF detached.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF not found. An attachment transition is already in progress. An internal server error has
                occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsUdfsAttachmentsServiceId400Error21 | V1OrganizationsUdfsAttachmentsServiceId404Error1 |
                V1OrganizationsUdfsAttachmentsServiceId409Error1 | V1OrganizationsUdfsAttachmentsServiceId500Error1 |
                RawError``."""
        return (
            await self._with_raw_response.udf_detach(
                organization_id, function_name, service_id, request_options=request_options
            )
        ).unwrap()

    async def udf_get(
        self, organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsUdfsResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the latest
        version of a UDF.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF not found. An internal server error has occurred. If this issue persists, please contact
                ClickHouse Cloud support for assistance. ``error`` is ``V1OrganizationsUdfs400Error1 |
                V1OrganizationsUdfs404Error1 | V1OrganizationsUdfs500Error1 | RawError``."""
        return (
            await self._with_raw_response.udf_get(organization_id, function_name, request_options=request_options)
        ).unwrap()

    async def udf_list(
        self,
        organization_id: UUID,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the latest
        version of each UDF in the organization.

        Args:
            organization_id: ID of the requested organization.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsUdfs400Error1 | V1OrganizationsUdfs500Error1
                | RawError``."""
        return (
            await self._with_raw_response.udf_list(
                organization_id, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def udf_upload_session_create(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsUdfUploadsUrlResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates an
        org-scoped presigned application/zip upload URL. Callers must use an upload ID for only one create or version
        attempt and request a new upload URL when retrying.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Upload URL created.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsUdfUploadsUrl400Error1 |
                V1OrganizationsUdfUploadsUrl500Error1 | RawError``."""
        return (
            await self._with_raw_response.udf_upload_session_create(organization_id, request_options=request_options)
        ).unwrap()

    async def udf_version_create(
        self,
        organization_id: UUID,
        function_name: str,
        *,
        body: UdfVersionCreateRequest2 | UdfVersionCreateRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsVersionsResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Consumes a source
        archive, assigns a version, and starts the UDF build. Optional configuration fields omitted from the request use
        the defaults documented in the request schema; values are not inherited from the previous version. Retry by
        requesting a new upload URL and re-uploading.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            UDF version created and building.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. Requested UDF features are not enabled. UDF not found. A concurrent request conflicted with
                this request. The source archive is unavailable. An internal server error has occurred. If this issue
                persists, please contact ClickHouse Cloud support for assistance. ``error`` is
                ``V1OrganizationsUdfsVersions400Error1 | V1OrganizationsUdfsVersions403Error1 |
                V1OrganizationsUdfsVersions404Error1 | V1OrganizationsUdfsVersions409Error1 |
                V1OrganizationsUdfsVersions410Error1 | V1OrganizationsUdfsVersions500Error1 | RawError``."""
        return (
            await self._with_raw_response.udf_version_create(
                organization_id, function_name, body=body, request_options=request_options
            )
        ).unwrap()

    async def udf_version_delete(
        self,
        organization_id: UUID,
        function_name: str,
        version: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsVersionsVersionResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes a UDF
        version. The UDF must not be attached to any services.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            version: Version number of the UDF.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            UDF version deleted.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF or version not found. The UDF version is the latest version, is attached to a service, or
                is still building. An internal server error has occurred. If this issue persists, please contact
                ClickHouse Cloud support for assistance. ``error`` is ``V1OrganizationsUdfsVersionsVersion400Error1 |
                V1OrganizationsUdfsVersionsVersion404Error1 | V1OrganizationsUdfsVersionsVersion409Error1 |
                V1OrganizationsUdfsVersionsVersion500Error1 | RawError``."""
        return (
            await self._with_raw_response.udf_version_delete(
                organization_id, function_name, version, request_options=request_options
            )
        ).unwrap()

    async def udf_version_list(
        self,
        organization_id: UUID,
        function_name: str,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUdfsVersionsResponse1:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns all
        versions of a UDF.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. UDF not found. An internal server error has occurred. If this issue persists, please contact
                ClickHouse Cloud support for assistance. ``error`` is ``V1OrganizationsUdfsVersions400Error1 |
                V1OrganizationsUdfsVersions404Error1 | V1OrganizationsUdfsVersions500Error1 | RawError``."""
        return (
            await self._with_raw_response.udf_version_list(
                organization_id, function_name, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUdfApiWithRawResponse:
        return self._with_raw_response


class UdfApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def udf_attach(
        self,
        organization_id: UUID,
        function_name: str,
        service_id: UUID,
        *,
        body: (
            V1OrganizationsUdfsAttachmentsServiceIdRequest | V1OrganizationsUdfsAttachmentsServiceIdRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsAttachmentsServiceIdResponse, UdfAttachErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Attaches one UDF
        version to a service, replacing the current version when necessary. When version is omitted, the latest ready
        version is attached.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/udfs/{functionName}/attachments/{serviceId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[str]("functionName", function_name),
                param[UUID]("serviceId", service_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                (
                    V1OrganizationsUdfsAttachmentsServiceIdRequest
                    | V1OrganizationsUdfsAttachmentsServiceIdRequestDict
                    | None
                )
            ](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsAttachmentsServiceIdResponse],
            error_mapper=udf_attach_error_mapper,
            request_options=request_options,
        )

    def udf_attachment_get(
        self,
        organization_id: UUID,
        function_name: str,
        service_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsAttachmentsServiceIdResponse, UdfAttachmentGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current
        attachment of a UDF to one service.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/udfs/{functionName}/attachments/{serviceId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[str]("functionName", function_name),
                param[UUID]("serviceId", service_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsAttachmentsServiceIdResponse],
            error_mapper=udf_attachment_get_error_mapper,
            request_options=request_options,
        )

    def udf_attachment_list(
        self,
        organization_id: UUID,
        function_name: str,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsAttachmentsResponse, UdfAttachmentListErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current
        service attachments for a UDF, with at most one attachment per service.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs/{functionName}/attachments"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("functionName", function_name)],
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsAttachmentsResponse],
            error_mapper=udf_attachment_list_error_mapper,
            request_options=request_options,
        )

    def udf_create(
        self,
        organization_id: UUID,
        *,
        body: UdfCreateRequest2 | UdfCreateRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsResponse, UdfCreateErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates a new UDF.
        See `User-defined functions in Cloud
        <https://clickhouse.com/docs/products/cloud/features/sql-console-features/user-defined-functions>`__.

        Args:
            organization_id: ID of the requested organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UdfCreateRequest2 | UdfCreateRequest2Dict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsResponse],
            error_mapper=udf_create_error_mapper,
            request_options=request_options,
        )

    def udf_delete(
        self, organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsUdfsResponse2, UdfDeleteErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes every
        version of a UDF and detaches it from all services. Removal from services completes asynchronously.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs/{functionName}"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("functionName", function_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsResponse2],
            error_mapper=udf_delete_error_mapper,
            request_options=request_options,
        )

    def udf_detach(
        self,
        organization_id: UUID,
        function_name: str,
        service_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsAttachmentsServiceIdResponse2, UdfDetachErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Detaches a UDF from
        a service.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/udfs/{functionName}/attachments/{serviceId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[str]("functionName", function_name),
                param[UUID]("serviceId", service_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsAttachmentsServiceIdResponse2],
            error_mapper=udf_detach_error_mapper,
            request_options=request_options,
        )

    def udf_get(
        self, organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsUdfsResponse, UdfGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the latest
        version of a UDF.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs/{functionName}"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("functionName", function_name)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsResponse],
            error_mapper=udf_get_error_mapper,
            request_options=request_options,
        )

    def udf_list(
        self,
        organization_id: UUID,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsResponse1, UdfListErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the latest
        version of each UDF in the organization.

        Args:
            organization_id: ID of the requested organization.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsResponse1],
            error_mapper=udf_list_error_mapper,
            request_options=request_options,
        )

    def udf_upload_session_create(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsUdfUploadsUrlResponse, UdfUploadSessionCreateErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates an
        org-scoped presigned application/zip upload URL. Callers must use an upload ID for only one create or version
        attempt and request a new upload URL when retrying.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfUploads/url"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfUploadsUrlResponse],
            error_mapper=udf_upload_session_create_error_mapper,
            request_options=request_options,
        )

    def udf_version_create(
        self,
        organization_id: UUID,
        function_name: str,
        *,
        body: UdfVersionCreateRequest2 | UdfVersionCreateRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsVersionsResponse, UdfVersionCreateErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Consumes a source
        archive, assigns a version, and starts the UDF build. Optional configuration fields omitted from the request use
        the defaults documented in the request schema; values are not inherited from the previous version. Retry by
        requesting a new upload URL and re-uploading.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs/{functionName}/versions"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("functionName", function_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UdfVersionCreateRequest2 | UdfVersionCreateRequest2Dict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsVersionsResponse],
            error_mapper=udf_version_create_error_mapper,
            request_options=request_options,
        )

    def udf_version_delete(
        self,
        organization_id: UUID,
        function_name: str,
        version: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsVersionsVersionResponse, UdfVersionDeleteErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes a UDF
        version. The UDF must not be attached to any services.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            version: Version number of the UDF.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/udfs/{functionName}/versions/{version}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[str]("functionName", function_name),
                param[int]("version", version),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsVersionsVersionResponse],
            error_mapper=udf_version_delete_error_mapper,
            request_options=request_options,
        )

    def udf_version_list(
        self,
        organization_id: UUID,
        function_name: str,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsVersionsResponse1, UdfVersionListErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns all
        versions of a UDF.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs/{functionName}/versions"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("functionName", function_name)],
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsVersionsResponse1],
            error_mapper=udf_version_list_error_mapper,
            request_options=request_options,
        )


class AsyncUdfApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def udf_attach(
        self,
        organization_id: UUID,
        function_name: str,
        service_id: UUID,
        *,
        body: (
            V1OrganizationsUdfsAttachmentsServiceIdRequest | V1OrganizationsUdfsAttachmentsServiceIdRequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsAttachmentsServiceIdResponse, UdfAttachErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Attaches one UDF
        version to a service, replacing the current version when necessary. When version is omitted, the latest ready
        version is attached.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            service_id: ID of the requested service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/udfs/{functionName}/attachments/{serviceId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[str]("functionName", function_name),
                param[UUID]("serviceId", service_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                (
                    V1OrganizationsUdfsAttachmentsServiceIdRequest
                    | V1OrganizationsUdfsAttachmentsServiceIdRequestDict
                    | None
                )
            ](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsAttachmentsServiceIdResponse],
            error_mapper=udf_attach_error_mapper,
            request_options=request_options,
        )

    async def udf_attachment_get(
        self,
        organization_id: UUID,
        function_name: str,
        service_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsAttachmentsServiceIdResponse, UdfAttachmentGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current
        attachment of a UDF to one service.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/udfs/{functionName}/attachments/{serviceId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[str]("functionName", function_name),
                param[UUID]("serviceId", service_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsAttachmentsServiceIdResponse],
            error_mapper=udf_attachment_get_error_mapper,
            request_options=request_options,
        )

    async def udf_attachment_list(
        self,
        organization_id: UUID,
        function_name: str,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsAttachmentsResponse, UdfAttachmentListErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current
        service attachments for a UDF, with at most one attachment per service.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs/{functionName}/attachments"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("functionName", function_name)],
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsAttachmentsResponse],
            error_mapper=udf_attachment_list_error_mapper,
            request_options=request_options,
        )

    async def udf_create(
        self,
        organization_id: UUID,
        *,
        body: UdfCreateRequest2 | UdfCreateRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsResponse, UdfCreateErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates a new UDF.
        See `User-defined functions in Cloud
        <https://clickhouse.com/docs/products/cloud/features/sql-console-features/user-defined-functions>`__.

        Args:
            organization_id: ID of the requested organization.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UdfCreateRequest2 | UdfCreateRequest2Dict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsResponse],
            error_mapper=udf_create_error_mapper,
            request_options=request_options,
        )

    async def udf_delete(
        self, organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsUdfsResponse2, UdfDeleteErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes every
        version of a UDF and detaches it from all services. Removal from services completes asynchronously.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs/{functionName}"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("functionName", function_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsResponse2],
            error_mapper=udf_delete_error_mapper,
            request_options=request_options,
        )

    async def udf_detach(
        self,
        organization_id: UUID,
        function_name: str,
        service_id: UUID,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsAttachmentsServiceIdResponse2, UdfDetachErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Detaches a UDF from
        a service.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            service_id: ID of the requested service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/udfs/{functionName}/attachments/{serviceId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[str]("functionName", function_name),
                param[UUID]("serviceId", service_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsAttachmentsServiceIdResponse2],
            error_mapper=udf_detach_error_mapper,
            request_options=request_options,
        )

    async def udf_get(
        self, organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsUdfsResponse, UdfGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the latest
        version of a UDF.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs/{functionName}"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("functionName", function_name)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsResponse],
            error_mapper=udf_get_error_mapper,
            request_options=request_options,
        )

    async def udf_list(
        self,
        organization_id: UUID,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsResponse1, UdfListErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the latest
        version of each UDF in the organization.

        Args:
            organization_id: ID of the requested organization.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsResponse1],
            error_mapper=udf_list_error_mapper,
            request_options=request_options,
        )

    async def udf_upload_session_create(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsUdfUploadsUrlResponse, UdfUploadSessionCreateErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates an
        org-scoped presigned application/zip upload URL. Callers must use an upload ID for only one create or version
        attempt and request a new upload URL when retrying.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfUploads/url"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfUploadsUrlResponse],
            error_mapper=udf_upload_session_create_error_mapper,
            request_options=request_options,
        )

    async def udf_version_create(
        self,
        organization_id: UUID,
        function_name: str,
        *,
        body: UdfVersionCreateRequest2 | UdfVersionCreateRequest2Dict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsVersionsResponse, UdfVersionCreateErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Consumes a source
        archive, assigns a version, and starts the UDF build. Optional configuration fields omitted from the request use
        the defaults documented in the request schema; values are not inherited from the previous version. Retry by
        requesting a new upload URL and re-uploading.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs/{functionName}/versions"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("functionName", function_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UdfVersionCreateRequest2 | UdfVersionCreateRequest2Dict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsVersionsResponse],
            error_mapper=udf_version_create_error_mapper,
            request_options=request_options,
        )

    async def udf_version_delete(
        self,
        organization_id: UUID,
        function_name: str,
        version: int,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsVersionsVersionResponse, UdfVersionDeleteErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes a UDF
        version. The UDF must not be attached to any services.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            version: Version number of the UDF.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/udfs/{functionName}/versions/{version}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[str]("functionName", function_name),
                param[int]("version", version),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsVersionsVersionResponse],
            error_mapper=udf_version_delete_error_mapper,
            request_options=request_options,
        )

    async def udf_version_list(
        self,
        organization_id: UUID,
        function_name: str,
        *,
        cursor: str | None = None,
        limit: int | None = 100,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUdfsVersionsResponse1, UdfVersionListErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns all
        versions of a UDF.

        Args:
            organization_id: ID of the requested organization.
            function_name: Name of the UDF.
            cursor: Cursor returned in ``pagination.nextCursor`` from the previous page.
            limit: Maximum number of records to return per page. Defaults to 100. Maximum is 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/udfs/{functionName}/versions"),
            path_params=[param[UUID]("organizationId", organization_id), param[str]("functionName", function_name)],
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUdfsVersionsResponse1],
            error_mapper=udf_version_list_error_mapper,
            request_options=request_options,
        )
