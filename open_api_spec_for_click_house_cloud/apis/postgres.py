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
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.postgres_instance_config_get_error import (
    PostgresInstanceConfigGetErrorBody,
    postgres_instance_config_get_error_mapper,
)
from ..errors.postgres_instance_config_patch_error import (
    PostgresInstanceConfigPatchErrorBody,
    postgres_instance_config_patch_error_mapper,
)
from ..errors.postgres_instance_config_post_error import (
    PostgresInstanceConfigPostErrorBody,
    postgres_instance_config_post_error_mapper,
)
from ..errors.postgres_instance_create_read_replica_error import (
    PostgresInstanceCreateReadReplicaErrorBody,
    postgres_instance_create_read_replica_error_mapper,
)
from ..errors.postgres_instance_metrics_get_error import (
    PostgresInstanceMetricsGetErrorBody,
    postgres_instance_metrics_get_error_mapper,
)
from ..errors.postgres_instance_restore_error import (
    PostgresInstanceRestoreErrorBody,
    postgres_instance_restore_error_mapper,
)
from ..errors.postgres_logs_get_list_error import PostgresLogsGetListErrorBody, postgres_logs_get_list_error_mapper
from ..errors.postgres_service_certs_get_error import (
    PostgresServiceCertsGetErrorBody,
    postgres_service_certs_get_error_mapper,
)
from ..errors.postgres_service_create_error import PostgresServiceCreateErrorBody, postgres_service_create_error_mapper
from ..errors.postgres_service_delete_error import PostgresServiceDeleteErrorBody, postgres_service_delete_error_mapper
from ..errors.postgres_service_get_error import PostgresServiceGetErrorBody, postgres_service_get_error_mapper
from ..errors.postgres_service_get_list_error import (
    PostgresServiceGetListErrorBody,
    postgres_service_get_list_error_mapper,
)
from ..errors.postgres_service_patch_error import PostgresServicePatchErrorBody, postgres_service_patch_error_mapper
from ..errors.postgres_service_patch_state_error import (
    PostgresServicePatchStateErrorBody,
    postgres_service_patch_state_error_mapper,
)
from ..errors.postgres_service_set_password_error import (
    PostgresServiceSetPasswordErrorBody,
    postgres_service_set_password_error_mapper,
)
from ..errors.slow_query_pattern_get_error import SlowQueryPatternGetErrorBody, slow_query_pattern_get_error_mapper
from ..errors.slow_query_patterns_get_list_error import (
    SlowQueryPatternsGetListErrorBody,
    slow_query_patterns_get_list_error_mapper,
)
from ..models.enums.sort_by import SortBy, SortByOrStr
from ..models.enums.sort_order1 import SortOrder1, SortOrder1OrStr
from ..models.postgres_instance_config import PostgresInstanceConfig, PostgresInstanceConfigDict
from ..models.postgres_service_patch_request import PostgresServicePatchRequest, PostgresServicePatchRequestDict
from ..models.postgres_service_post_request import PostgresServicePostRequest, PostgresServicePostRequestDict
from ..models.postgres_service_read_replica_request import (
    PostgresServiceReadReplicaRequest,
    PostgresServiceReadReplicaRequestDict,
)
from ..models.postgres_service_restore_request import PostgresServiceRestoreRequest, PostgresServiceRestoreRequestDict
from ..models.postgres_service_set_password import PostgresServiceSetPassword, PostgresServiceSetPasswordDict
from ..models.postgres_service_set_state import PostgresServiceSetState, PostgresServiceSetStateDict
from ..models.v1_organizations_postgres_config_response import V1OrganizationsPostgresConfigResponse
from ..models.v1_organizations_postgres_config_response1 import V1OrganizationsPostgresConfigResponse1
from ..models.v1_organizations_postgres_logs_response import V1OrganizationsPostgresLogsResponse
from ..models.v1_organizations_postgres_metrics_response import V1OrganizationsPostgresMetricsResponse
from ..models.v1_organizations_postgres_password_response import V1OrganizationsPostgresPasswordResponse
from ..models.v1_organizations_postgres_read_replica_response import V1OrganizationsPostgresReadReplicaResponse
from ..models.v1_organizations_postgres_response import V1OrganizationsPostgresResponse
from ..models.v1_organizations_postgres_response1 import V1OrganizationsPostgresResponse1
from ..models.v1_organizations_postgres_response3 import V1OrganizationsPostgresResponse3
from ..models.v1_organizations_postgres_restored_service_response import V1OrganizationsPostgresRestoredServiceResponse
from ..models.v1_organizations_postgres_slow_query_patterns_query_id_response import (
    V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse,
)
from ..models.v1_organizations_postgres_slow_query_patterns_response import (
    V1OrganizationsPostgresSlowQueryPatternsResponse,
)
from ..models.v1_organizations_postgres_state_response import V1OrganizationsPostgresStateResponse
from ..server.server import Server


class Postgres:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PostgresWithRawResponse(client, server, auth)

    def postgres_instance_config_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsPostgresConfigResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns the configuration data for a Postgres service and its PgBouncer service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresConfig400Error1 |
                V1OrganizationsPostgresConfig500Error1 | RawError``."""
        return self._with_raw_response.postgres_instance_config_get(
            organization_id, postgres_id, request_options=request_options
        ).unwrap()

    def postgres_instance_config_patch(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresConfigResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Update the existing Postgres service and pgBouncer configuration.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresConfig400Error1 |
                V1OrganizationsPostgresConfig500Error1 | RawError``."""
        return self._with_raw_response.postgres_instance_config_patch(
            organization_id, postgres_id, body=body, request_options=request_options
        ).unwrap()

    def postgres_instance_config_post(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresConfigResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Replace the existing Postgres service and pgBouncer configuration.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresConfig400Error1 |
                V1OrganizationsPostgresConfig500Error1 | RawError``."""
        return self._with_raw_response.postgres_instance_config_post(
            organization_id, postgres_id, body=body, request_options=request_options
        ).unwrap()

    def postgres_instance_create_read_replica(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceReadReplicaRequest | PostgresServiceReadReplicaRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresReadReplicaResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Initiate the process to create a new read replica for a Postgres service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresReadReplica400Error1 |
                V1OrganizationsPostgresReadReplica500Error1 | RawError``."""
        return self._with_raw_response.postgres_instance_create_read_replica(
            organization_id, postgres_id, body=body, request_options=request_options
        ).unwrap()

    def postgres_instance_metrics_get(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        from_date: RFC3339DateTime,
        to_date: RFC3339DateTime,
        *,
        bucket_size_seconds: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresMetricsResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns bucketed time-series metrics for a PostgreSQL service over the requested window (CPU, memory,
        disk, network, connections, cache hit ratio, throughput, transactions, and more). Use this to chart or analyze
        how a service behaved over time.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the Postgres service.
            from_date: Inclusive start of the time window (RFC 3339 date-time).
            to_date: Exclusive end of the time window (RFC 3339 date-time).
            bucket_size_seconds: Time-series bucket size in seconds. When omitted, a bucket size is derived from the
                requested window. Requests are capped at 250 data points.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresMetrics400Error1 |
                V1OrganizationsPostgresMetrics500Error1 | RawError``."""
        return self._with_raw_response.postgres_instance_metrics_get(
            organization_id,
            postgres_id,
            from_date,
            to_date,
            bucket_size_seconds=bucket_size_seconds,
            request_options=request_options,
        ).unwrap()

    def postgres_instance_restore(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceRestoreRequest | PostgresServiceRestoreRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresRestoredServiceResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Restore a Postgres database from continuous backup, optionally at a specific point in time.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresRestoredService400Error1 |
                V1OrganizationsPostgresRestoredService500Error1 | RawError``."""
        return self._with_raw_response.postgres_instance_restore(
            organization_id, postgres_id, body=body, request_options=request_options
        ).unwrap()

    def postgres_logs_get_list(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        from_date: RFC3339DateTime,
        to_date: RFC3339DateTime,
        *,
        body_contains: str | None = None,
        severity: str | None = None,
        sort_order: SortOrder1OrStr | None = SortOrder1.DESC,
        limit: int | None = 50,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresLogsResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns PostgreSQL server log entries for a Postgres service within the given time window, most recent
        first by default (override with ``sort_order``). Results are paginated with ``limit``/``offset``; advance
        ``offset`` until a page returns fewer than ``limit`` entries to read the full window. The time range must not
        exceed 30 days, and ``to_date`` must be after ``from_date``.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            from_date: Inclusive start of the time window (RFC 3339 date-time).
            to_date: Inclusive end of the time window (RFC 3339 date-time).
            body_contains: Case-sensitive substring the log body must contain.
            severity: Filter to log entries with this PostgreSQL severity (for example, ERROR, WARNING, LOG).
            sort_order: Sort order. One of ``asc`` or ``desc``.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresLogs400Error1 |
                V1OrganizationsPostgresLogs500Error1 | RawError``."""
        return self._with_raw_response.postgres_logs_get_list(
            organization_id,
            postgres_id,
            from_date,
            to_date,
            body_contains=body_contains,
            severity=severity,
            sort_order=sort_order,
            limit=limit,
            offset=offset,
            request_options=request_options,
        ).unwrap()

    def postgres_service_certs_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Download CA certificates for a PostgreSQL service

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresCaCertificates400Error1 |
                V1OrganizationsPostgresCaCertificates500Error1 | RawError``."""
        return self._with_raw_response.postgres_service_certs_get(
            organization_id, postgres_id, request_options=request_options
        ).unwrap()

    def postgres_service_create(
        self,
        organization_id: UUID,
        *,
        body: PostgresServicePostRequest | PostgresServicePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Creates a new Postgres service in the organization and returns it. The service is started
        asynchronously.

        Args:
            organization_id: ID of the organization that will own the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgres400Error1 |
                V1OrganizationsPostgres500Error1 | RawError``."""
        return self._with_raw_response.postgres_service_create(
            organization_id, body=body, request_options=request_options
        ).unwrap()

    def postgres_service_delete(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsPostgresResponse3:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Deletes a Postgres service that belongs to the organization

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgres400Error1 |
                V1OrganizationsPostgres500Error1 | RawError``."""
        return self._with_raw_response.postgres_service_delete(
            organization_id, postgres_id, request_options=request_options
        ).unwrap()

    def postgres_service_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsPostgresResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a Postgres service that belongs to the organization

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgres400Error1 |
                V1OrganizationsPostgres500Error1 | RawError``."""
        return self._with_raw_response.postgres_service_get(
            organization_id, postgres_id, request_options=request_options
        ).unwrap()

    def postgres_service_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsPostgresResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a list of all Postgres services in the organization.

        Args:
            organization_id: ID of the organization that owns the services.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgres400Error1 |
                V1OrganizationsPostgres500Error1 | RawError``."""
        return self._with_raw_response.postgres_service_get_list(
            organization_id, request_options=request_options
        ).unwrap()

    def postgres_service_patch(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServicePatchRequest | PostgresServicePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Update a Postgres service that belongs to the organization. **WARNING:** Changing the name also updates
        the host name and certificates for the service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgres400Error1 |
                V1OrganizationsPostgres500Error1 | RawError``."""
        return self._with_raw_response.postgres_service_patch(
            organization_id, postgres_id, body=body, request_options=request_options
        ).unwrap()

    def postgres_service_patch_state(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceSetState | PostgresServiceSetStateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresStateResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Initiate a process for a Postgres service:
        * restart: Initiates a service restart
        * promote: Promotes a read replica to primary
        * switchover: Switch a primary over to a standby

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresState400Error1 |
                V1OrganizationsPostgresState500Error1 | RawError``."""
        return self._with_raw_response.postgres_service_patch_state(
            organization_id, postgres_id, body=body, request_options=request_options
        ).unwrap()

    def postgres_service_set_password(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceSetPassword | PostgresServiceSetPasswordDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresPasswordResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Sets a new password for a Postgres service's superuser account.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresPassword400Error1 |
                V1OrganizationsPostgresPassword500Error1 | RawError``."""
        return self._with_raw_response.postgres_service_set_password(
            organization_id, postgres_id, body=body, request_options=request_options
        ).unwrap()

    def slow_query_pattern_get(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        query_id: str,
        db_name: str,
        db_user: str,
        db_operation: str,
        *,
        app: str | None = None,
        timestamp: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns aggregate metrics for a single slow query pattern together with its most recent individual
        executions.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            query_id: Stable identifier for the query pattern.
            db_name: Database name filter.
            db_user: Database user filter.
            db_operation: Database operation filter (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY).
            app: Application name filter.
            timestamp: Timestamp of a specific execution (RFC 3339).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresSlowQueryPatternsQueryId400Error1 |
                V1OrganizationsPostgresSlowQueryPatternsQueryId500Error1 | RawError``."""
        return self._with_raw_response.slow_query_pattern_get(
            organization_id,
            postgres_id,
            query_id,
            db_name,
            db_user,
            db_operation,
            app=app,
            timestamp=timestamp,
            request_options=request_options,
        ).unwrap()

    def slow_query_patterns_get_list(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        from_date: RFC3339DateTime,
        to_date: RFC3339DateTime,
        *,
        db_name: str | None = None,
        db_user: str | None = None,
        db_operation: str | None = None,
        app: str | None = None,
        sort_by: SortByOrStr | None = SortBy.TOTAL_DURATION,
        sort_order: SortOrder1OrStr | None = SortOrder1.DESC,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresSlowQueryPatternsResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns aggregate metrics for the slowest query patterns observed on a Postgres service during the
        given time window. Use this to discover which queries dominate total execution time, CPU, I/O, or WAL
        generation.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            from_date: Inclusive start of the time window (RFC 3339 date-time).
            to_date: Exclusive end of the time window (RFC 3339 date-time).
            db_name: Database name filter.
            db_user: Database user filter.
            db_operation: Database operation filter (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY).
            app: Application name filter.
            sort_by: Field to sort results by.
            sort_order: Sort order. One of ``asc`` or ``desc``.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresSlowQueryPatterns400Error1 |
                V1OrganizationsPostgresSlowQueryPatterns500Error1 | RawError``."""
        return self._with_raw_response.slow_query_patterns_get_list(
            organization_id,
            postgres_id,
            from_date,
            to_date,
            db_name=db_name,
            db_user=db_user,
            db_operation=db_operation,
            app=app,
            sort_by=sort_by,
            sort_order=sort_order,
            limit=limit,
            offset=offset,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> PostgresWithRawResponse:
        return self._with_raw_response


class AsyncPostgres:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPostgresWithRawResponse(client, server, auth)

    async def postgres_instance_config_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsPostgresConfigResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns the configuration data for a Postgres service and its PgBouncer service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresConfig400Error1 |
                V1OrganizationsPostgresConfig500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_instance_config_get(
                organization_id, postgres_id, request_options=request_options
            )
        ).unwrap()

    async def postgres_instance_config_patch(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresConfigResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Update the existing Postgres service and pgBouncer configuration.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresConfig400Error1 |
                V1OrganizationsPostgresConfig500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_instance_config_patch(
                organization_id, postgres_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def postgres_instance_config_post(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresConfigResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Replace the existing Postgres service and pgBouncer configuration.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresConfig400Error1 |
                V1OrganizationsPostgresConfig500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_instance_config_post(
                organization_id, postgres_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def postgres_instance_create_read_replica(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceReadReplicaRequest | PostgresServiceReadReplicaRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresReadReplicaResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Initiate the process to create a new read replica for a Postgres service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresReadReplica400Error1 |
                V1OrganizationsPostgresReadReplica500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_instance_create_read_replica(
                organization_id, postgres_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def postgres_instance_metrics_get(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        from_date: RFC3339DateTime,
        to_date: RFC3339DateTime,
        *,
        bucket_size_seconds: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresMetricsResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns bucketed time-series metrics for a PostgreSQL service over the requested window (CPU, memory,
        disk, network, connections, cache hit ratio, throughput, transactions, and more). Use this to chart or analyze
        how a service behaved over time.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the Postgres service.
            from_date: Inclusive start of the time window (RFC 3339 date-time).
            to_date: Exclusive end of the time window (RFC 3339 date-time).
            bucket_size_seconds: Time-series bucket size in seconds. When omitted, a bucket size is derived from the
                requested window. Requests are capped at 250 data points.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresMetrics400Error1 |
                V1OrganizationsPostgresMetrics500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_instance_metrics_get(
                organization_id,
                postgres_id,
                from_date,
                to_date,
                bucket_size_seconds=bucket_size_seconds,
                request_options=request_options,
            )
        ).unwrap()

    async def postgres_instance_restore(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceRestoreRequest | PostgresServiceRestoreRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresRestoredServiceResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Restore a Postgres database from continuous backup, optionally at a specific point in time.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresRestoredService400Error1 |
                V1OrganizationsPostgresRestoredService500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_instance_restore(
                organization_id, postgres_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def postgres_logs_get_list(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        from_date: RFC3339DateTime,
        to_date: RFC3339DateTime,
        *,
        body_contains: str | None = None,
        severity: str | None = None,
        sort_order: SortOrder1OrStr | None = SortOrder1.DESC,
        limit: int | None = 50,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresLogsResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns PostgreSQL server log entries for a Postgres service within the given time window, most recent
        first by default (override with ``sort_order``). Results are paginated with ``limit``/``offset``; advance
        ``offset`` until a page returns fewer than ``limit`` entries to read the full window. The time range must not
        exceed 30 days, and ``to_date`` must be after ``from_date``.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            from_date: Inclusive start of the time window (RFC 3339 date-time).
            to_date: Inclusive end of the time window (RFC 3339 date-time).
            body_contains: Case-sensitive substring the log body must contain.
            severity: Filter to log entries with this PostgreSQL severity (for example, ERROR, WARNING, LOG).
            sort_order: Sort order. One of ``asc`` or ``desc``.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresLogs400Error1 |
                V1OrganizationsPostgresLogs500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_logs_get_list(
                organization_id,
                postgres_id,
                from_date,
                to_date,
                body_contains=body_contains,
                severity=severity,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
                request_options=request_options,
            )
        ).unwrap()

    async def postgres_service_certs_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Download CA certificates for a PostgreSQL service

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresCaCertificates400Error1 |
                V1OrganizationsPostgresCaCertificates500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_service_certs_get(
                organization_id, postgres_id, request_options=request_options
            )
        ).unwrap()

    async def postgres_service_create(
        self,
        organization_id: UUID,
        *,
        body: PostgresServicePostRequest | PostgresServicePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Creates a new Postgres service in the organization and returns it. The service is started
        asynchronously.

        Args:
            organization_id: ID of the organization that will own the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgres400Error1 |
                V1OrganizationsPostgres500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_service_create(
                organization_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def postgres_service_delete(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsPostgresResponse3:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Deletes a Postgres service that belongs to the organization

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgres400Error1 |
                V1OrganizationsPostgres500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_service_delete(
                organization_id, postgres_id, request_options=request_options
            )
        ).unwrap()

    async def postgres_service_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsPostgresResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a Postgres service that belongs to the organization

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgres400Error1 |
                V1OrganizationsPostgres500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_service_get(
                organization_id, postgres_id, request_options=request_options
            )
        ).unwrap()

    async def postgres_service_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsPostgresResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a list of all Postgres services in the organization.

        Args:
            organization_id: ID of the organization that owns the services.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgres400Error1 |
                V1OrganizationsPostgres500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_service_get_list(organization_id, request_options=request_options)
        ).unwrap()

    async def postgres_service_patch(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServicePatchRequest | PostgresServicePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Update a Postgres service that belongs to the organization. **WARNING:** Changing the name also updates
        the host name and certificates for the service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgres400Error1 |
                V1OrganizationsPostgres500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_service_patch(
                organization_id, postgres_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def postgres_service_patch_state(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceSetState | PostgresServiceSetStateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresStateResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Initiate a process for a Postgres service:
        * restart: Initiates a service restart
        * promote: Promotes a read replica to primary
        * switchover: Switch a primary over to a standby

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresState400Error1 |
                V1OrganizationsPostgresState500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_service_patch_state(
                organization_id, postgres_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def postgres_service_set_password(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceSetPassword | PostgresServiceSetPasswordDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresPasswordResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Sets a new password for a Postgres service's superuser account.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresPassword400Error1 |
                V1OrganizationsPostgresPassword500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_service_set_password(
                organization_id, postgres_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def slow_query_pattern_get(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        query_id: str,
        db_name: str,
        db_user: str,
        db_operation: str,
        *,
        app: str | None = None,
        timestamp: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns aggregate metrics for a single slow query pattern together with its most recent individual
        executions.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            query_id: Stable identifier for the query pattern.
            db_name: Database name filter.
            db_user: Database user filter.
            db_operation: Database operation filter (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY).
            app: Application name filter.
            timestamp: Timestamp of a specific execution (RFC 3339).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresSlowQueryPatternsQueryId400Error1 |
                V1OrganizationsPostgresSlowQueryPatternsQueryId500Error1 | RawError``."""
        return (
            await self._with_raw_response.slow_query_pattern_get(
                organization_id,
                postgres_id,
                query_id,
                db_name,
                db_user,
                db_operation,
                app=app,
                timestamp=timestamp,
                request_options=request_options,
            )
        ).unwrap()

    async def slow_query_patterns_get_list(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        from_date: RFC3339DateTime,
        to_date: RFC3339DateTime,
        *,
        db_name: str | None = None,
        db_user: str | None = None,
        db_operation: str | None = None,
        app: str | None = None,
        sort_by: SortByOrStr | None = SortBy.TOTAL_DURATION,
        sort_order: SortOrder1OrStr | None = SortOrder1.DESC,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsPostgresSlowQueryPatternsResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns aggregate metrics for the slowest query patterns observed on a Postgres service during the
        given time window. Use this to discover which queries dominate total execution time, CPU, I/O, or WAL
        generation.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            from_date: Inclusive start of the time window (RFC 3339 date-time).
            to_date: Exclusive end of the time window (RFC 3339 date-time).
            db_name: Database name filter.
            db_user: Database user filter.
            db_operation: Database operation filter (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY).
            app: Application name filter.
            sort_by: Field to sort results by.
            sort_order: Sort order. One of ``asc`` or ``desc``.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresSlowQueryPatterns400Error1 |
                V1OrganizationsPostgresSlowQueryPatterns500Error1 | RawError``."""
        return (
            await self._with_raw_response.slow_query_patterns_get_list(
                organization_id,
                postgres_id,
                from_date,
                to_date,
                db_name=db_name,
                db_user=db_user,
                db_operation=db_operation,
                app=app,
                sort_by=sort_by,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPostgresWithRawResponse:
        return self._with_raw_response


class PostgresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def postgres_instance_config_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsPostgresConfigResponse, PostgresInstanceConfigGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns the configuration data for a Postgres service and its PgBouncer service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/config"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresConfigResponse],
            error_mapper=postgres_instance_config_get_error_mapper,
            request_options=request_options,
        )

    def postgres_instance_config_patch(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresConfigResponse1, PostgresInstanceConfigPatchErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Update the existing Postgres service and pgBouncer configuration.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/config"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresInstanceConfig | PostgresInstanceConfigDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresConfigResponse1],
            error_mapper=postgres_instance_config_patch_error_mapper,
            request_options=request_options,
        )

    def postgres_instance_config_post(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresConfigResponse1, PostgresInstanceConfigPostErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Replace the existing Postgres service and pgBouncer configuration.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/config"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresInstanceConfig | PostgresInstanceConfigDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresConfigResponse1],
            error_mapper=postgres_instance_config_post_error_mapper,
            request_options=request_options,
        )

    def postgres_instance_create_read_replica(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceReadReplicaRequest | PostgresServiceReadReplicaRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresReadReplicaResponse, PostgresInstanceCreateReadReplicaErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Initiate the process to create a new read replica for a Postgres service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/readReplica"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresServiceReadReplicaRequest | PostgresServiceReadReplicaRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresReadReplicaResponse],
            error_mapper=postgres_instance_create_read_replica_error_mapper,
            request_options=request_options,
        )

    def postgres_instance_metrics_get(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        from_date: RFC3339DateTime,
        to_date: RFC3339DateTime,
        *,
        bucket_size_seconds: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresMetricsResponse, PostgresInstanceMetricsGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns bucketed time-series metrics for a PostgreSQL service over the requested window (CPU, memory,
        disk, network, connections, cache hit ratio, throughput, transactions, and more). Use this to chart or analyze
        how a service behaved over time.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the Postgres service.
            from_date: Inclusive start of the time window (RFC 3339 date-time).
            to_date: Exclusive end of the time window (RFC 3339 date-time).
            bucket_size_seconds: Time-series bucket size in seconds. When omitted, a bucket size is derived from the
                requested window. Requests are capped at 250 data points.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/metrics"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            query_params=[
                param[RFC3339DateTime]("from_date", from_date),
                param[RFC3339DateTime]("to_date", to_date),
                param[int | None]("bucket_size_seconds", bucket_size_seconds),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresMetricsResponse],
            error_mapper=postgres_instance_metrics_get_error_mapper,
            request_options=request_options,
        )

    def postgres_instance_restore(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceRestoreRequest | PostgresServiceRestoreRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresRestoredServiceResponse, PostgresInstanceRestoreErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Restore a Postgres database from continuous backup, optionally at a specific point in time.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/postgres/{postgresId}/restoredService"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresServiceRestoreRequest | PostgresServiceRestoreRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresRestoredServiceResponse],
            error_mapper=postgres_instance_restore_error_mapper,
            request_options=request_options,
        )

    def postgres_logs_get_list(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        from_date: RFC3339DateTime,
        to_date: RFC3339DateTime,
        *,
        body_contains: str | None = None,
        severity: str | None = None,
        sort_order: SortOrder1OrStr | None = SortOrder1.DESC,
        limit: int | None = 50,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresLogsResponse, PostgresLogsGetListErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns PostgreSQL server log entries for a Postgres service within the given time window, most recent
        first by default (override with ``sort_order``). Results are paginated with ``limit``/``offset``; advance
        ``offset`` until a page returns fewer than ``limit`` entries to read the full window. The time range must not
        exceed 30 days, and ``to_date`` must be after ``from_date``.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            from_date: Inclusive start of the time window (RFC 3339 date-time).
            to_date: Inclusive end of the time window (RFC 3339 date-time).
            body_contains: Case-sensitive substring the log body must contain.
            severity: Filter to log entries with this PostgreSQL severity (for example, ERROR, WARNING, LOG).
            sort_order: Sort order. One of ``asc`` or ``desc``.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/logs"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            query_params=[
                param[RFC3339DateTime]("from_date", from_date),
                param[RFC3339DateTime]("to_date", to_date),
                param[str | None]("body_contains", body_contains),
                param[str | None]("severity", severity),
                param[SortOrder1OrStr | None]("sort_order", sort_order),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresLogsResponse],
            error_mapper=postgres_logs_get_list_error_mapper,
            request_options=request_options,
        )

    def postgres_service_certs_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, PostgresServiceCertsGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Download CA certificates for a PostgreSQL service

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/postgres/{postgresId}/caCertificates"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=postgres_service_certs_get_error_mapper,
            request_options=request_options,
        )

    def postgres_service_create(
        self,
        organization_id: UUID,
        *,
        body: PostgresServicePostRequest | PostgresServicePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresResponse, PostgresServiceCreateErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Creates a new Postgres service in the organization and returns it. The service is started
        asynchronously.

        Args:
            organization_id: ID of the organization that will own the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresServicePostRequest | PostgresServicePostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresResponse],
            error_mapper=postgres_service_create_error_mapper,
            request_options=request_options,
        )

    def postgres_service_delete(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsPostgresResponse3, PostgresServiceDeleteErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Deletes a Postgres service that belongs to the organization

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresResponse3],
            error_mapper=postgres_service_delete_error_mapper,
            request_options=request_options,
        )

    def postgres_service_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsPostgresResponse, PostgresServiceGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a Postgres service that belongs to the organization

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresResponse],
            error_mapper=postgres_service_get_error_mapper,
            request_options=request_options,
        )

    def postgres_service_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsPostgresResponse1, PostgresServiceGetListErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a list of all Postgres services in the organization.

        Args:
            organization_id: ID of the organization that owns the services.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresResponse1],
            error_mapper=postgres_service_get_list_error_mapper,
            request_options=request_options,
        )

    def postgres_service_patch(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServicePatchRequest | PostgresServicePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresResponse, PostgresServicePatchErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Update a Postgres service that belongs to the organization. **WARNING:** Changing the name also updates
        the host name and certificates for the service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresServicePatchRequest | PostgresServicePatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresResponse],
            error_mapper=postgres_service_patch_error_mapper,
            request_options=request_options,
        )

    def postgres_service_patch_state(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceSetState | PostgresServiceSetStateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresStateResponse, PostgresServicePatchStateErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Initiate a process for a Postgres service:
        * restart: Initiates a service restart
        * promote: Promotes a read replica to primary
        * switchover: Switch a primary over to a standby

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/state"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresServiceSetState | PostgresServiceSetStateDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresStateResponse],
            error_mapper=postgres_service_patch_state_error_mapper,
            request_options=request_options,
        )

    def postgres_service_set_password(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceSetPassword | PostgresServiceSetPasswordDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresPasswordResponse, PostgresServiceSetPasswordErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Sets a new password for a Postgres service's superuser account.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/password"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresServiceSetPassword | PostgresServiceSetPasswordDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresPasswordResponse],
            error_mapper=postgres_service_set_password_error_mapper,
            request_options=request_options,
        )

    def slow_query_pattern_get(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        query_id: str,
        db_name: str,
        db_user: str,
        db_operation: str,
        *,
        app: str | None = None,
        timestamp: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse, SlowQueryPatternGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns aggregate metrics for a single slow query pattern together with its most recent individual
        executions.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            query_id: Stable identifier for the query pattern.
            db_name: Database name filter.
            db_user: Database user filter.
            db_operation: Database operation filter (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY).
            app: Application name filter.
            timestamp: Timestamp of a specific execution (RFC 3339).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/postgres/{postgresId}/slowQueryPatterns/{queryId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("postgresId", postgres_id),
                param[str]("queryId", query_id),
            ],
            query_params=[
                param[str]("db_name", db_name),
                param[str]("db_user", db_user),
                param[str]("db_operation", db_operation),
                param[str | None]("app", app),
                param[RFC3339DateTime | None]("timestamp", timestamp),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse],
            error_mapper=slow_query_pattern_get_error_mapper,
            request_options=request_options,
        )

    def slow_query_patterns_get_list(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        from_date: RFC3339DateTime,
        to_date: RFC3339DateTime,
        *,
        db_name: str | None = None,
        db_user: str | None = None,
        db_operation: str | None = None,
        app: str | None = None,
        sort_by: SortByOrStr | None = SortBy.TOTAL_DURATION,
        sort_order: SortOrder1OrStr | None = SortOrder1.DESC,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresSlowQueryPatternsResponse, SlowQueryPatternsGetListErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns aggregate metrics for the slowest query patterns observed on a Postgres service during the
        given time window. Use this to discover which queries dominate total execution time, CPU, I/O, or WAL
        generation.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            from_date: Inclusive start of the time window (RFC 3339 date-time).
            to_date: Exclusive end of the time window (RFC 3339 date-time).
            db_name: Database name filter.
            db_user: Database user filter.
            db_operation: Database operation filter (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY).
            app: Application name filter.
            sort_by: Field to sort results by.
            sort_order: Sort order. One of ``asc`` or ``desc``.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/postgres/{postgresId}/slowQueryPatterns"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            query_params=[
                param[RFC3339DateTime]("from_date", from_date),
                param[RFC3339DateTime]("to_date", to_date),
                param[str | None]("db_name", db_name),
                param[str | None]("db_user", db_user),
                param[str | None]("db_operation", db_operation),
                param[str | None]("app", app),
                param[SortByOrStr | None]("sort_by", sort_by),
                param[SortOrder1OrStr | None]("sort_order", sort_order),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresSlowQueryPatternsResponse],
            error_mapper=slow_query_patterns_get_list_error_mapper,
            request_options=request_options,
        )


class AsyncPostgresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def postgres_instance_config_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsPostgresConfigResponse, PostgresInstanceConfigGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns the configuration data for a Postgres service and its PgBouncer service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/config"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresConfigResponse],
            error_mapper=postgres_instance_config_get_error_mapper,
            request_options=request_options,
        )

    async def postgres_instance_config_patch(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresConfigResponse1, PostgresInstanceConfigPatchErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Update the existing Postgres service and pgBouncer configuration.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/config"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresInstanceConfig | PostgresInstanceConfigDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresConfigResponse1],
            error_mapper=postgres_instance_config_patch_error_mapper,
            request_options=request_options,
        )

    async def postgres_instance_config_post(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresConfigResponse1, PostgresInstanceConfigPostErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Replace the existing Postgres service and pgBouncer configuration.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/config"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresInstanceConfig | PostgresInstanceConfigDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresConfigResponse1],
            error_mapper=postgres_instance_config_post_error_mapper,
            request_options=request_options,
        )

    async def postgres_instance_create_read_replica(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceReadReplicaRequest | PostgresServiceReadReplicaRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresReadReplicaResponse, PostgresInstanceCreateReadReplicaErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Initiate the process to create a new read replica for a Postgres service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/readReplica"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresServiceReadReplicaRequest | PostgresServiceReadReplicaRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresReadReplicaResponse],
            error_mapper=postgres_instance_create_read_replica_error_mapper,
            request_options=request_options,
        )

    async def postgres_instance_metrics_get(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        from_date: RFC3339DateTime,
        to_date: RFC3339DateTime,
        *,
        bucket_size_seconds: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresMetricsResponse, PostgresInstanceMetricsGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns bucketed time-series metrics for a PostgreSQL service over the requested window (CPU, memory,
        disk, network, connections, cache hit ratio, throughput, transactions, and more). Use this to chart or analyze
        how a service behaved over time.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the Postgres service.
            from_date: Inclusive start of the time window (RFC 3339 date-time).
            to_date: Exclusive end of the time window (RFC 3339 date-time).
            bucket_size_seconds: Time-series bucket size in seconds. When omitted, a bucket size is derived from the
                requested window. Requests are capped at 250 data points.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/metrics"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            query_params=[
                param[RFC3339DateTime]("from_date", from_date),
                param[RFC3339DateTime]("to_date", to_date),
                param[int | None]("bucket_size_seconds", bucket_size_seconds),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresMetricsResponse],
            error_mapper=postgres_instance_metrics_get_error_mapper,
            request_options=request_options,
        )

    async def postgres_instance_restore(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceRestoreRequest | PostgresServiceRestoreRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresRestoredServiceResponse, PostgresInstanceRestoreErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Restore a Postgres database from continuous backup, optionally at a specific point in time.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/postgres/{postgresId}/restoredService"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresServiceRestoreRequest | PostgresServiceRestoreRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresRestoredServiceResponse],
            error_mapper=postgres_instance_restore_error_mapper,
            request_options=request_options,
        )

    async def postgres_logs_get_list(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        from_date: RFC3339DateTime,
        to_date: RFC3339DateTime,
        *,
        body_contains: str | None = None,
        severity: str | None = None,
        sort_order: SortOrder1OrStr | None = SortOrder1.DESC,
        limit: int | None = 50,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresLogsResponse, PostgresLogsGetListErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns PostgreSQL server log entries for a Postgres service within the given time window, most recent
        first by default (override with ``sort_order``). Results are paginated with ``limit``/``offset``; advance
        ``offset`` until a page returns fewer than ``limit`` entries to read the full window. The time range must not
        exceed 30 days, and ``to_date`` must be after ``from_date``.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            from_date: Inclusive start of the time window (RFC 3339 date-time).
            to_date: Inclusive end of the time window (RFC 3339 date-time).
            body_contains: Case-sensitive substring the log body must contain.
            severity: Filter to log entries with this PostgreSQL severity (for example, ERROR, WARNING, LOG).
            sort_order: Sort order. One of ``asc`` or ``desc``.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/logs"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            query_params=[
                param[RFC3339DateTime]("from_date", from_date),
                param[RFC3339DateTime]("to_date", to_date),
                param[str | None]("body_contains", body_contains),
                param[str | None]("severity", severity),
                param[SortOrder1OrStr | None]("sort_order", sort_order),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresLogsResponse],
            error_mapper=postgres_logs_get_list_error_mapper,
            request_options=request_options,
        )

    async def postgres_service_certs_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, PostgresServiceCertsGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Download CA certificates for a PostgreSQL service

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/postgres/{postgresId}/caCertificates"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=empty_response,
            error_mapper=postgres_service_certs_get_error_mapper,
            request_options=request_options,
        )

    async def postgres_service_create(
        self,
        organization_id: UUID,
        *,
        body: PostgresServicePostRequest | PostgresServicePostRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresResponse, PostgresServiceCreateErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Creates a new Postgres service in the organization and returns it. The service is started
        asynchronously.

        Args:
            organization_id: ID of the organization that will own the service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres"),
            path_params=[param[UUID]("organizationId", organization_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresServicePostRequest | PostgresServicePostRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresResponse],
            error_mapper=postgres_service_create_error_mapper,
            request_options=request_options,
        )

    async def postgres_service_delete(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsPostgresResponse3, PostgresServiceDeleteErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Deletes a Postgres service that belongs to the organization

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresResponse3],
            error_mapper=postgres_service_delete_error_mapper,
            request_options=request_options,
        )

    async def postgres_service_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsPostgresResponse, PostgresServiceGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a Postgres service that belongs to the organization

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresResponse],
            error_mapper=postgres_service_get_error_mapper,
            request_options=request_options,
        )

    async def postgres_service_get_list(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsPostgresResponse1, PostgresServiceGetListErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns a list of all Postgres services in the organization.

        Args:
            organization_id: ID of the organization that owns the services.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresResponse1],
            error_mapper=postgres_service_get_list_error_mapper,
            request_options=request_options,
        )

    async def postgres_service_patch(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServicePatchRequest | PostgresServicePatchRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresResponse, PostgresServicePatchErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Update a Postgres service that belongs to the organization. **WARNING:** Changing the name also updates
        the host name and certificates for the service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresServicePatchRequest | PostgresServicePatchRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresResponse],
            error_mapper=postgres_service_patch_error_mapper,
            request_options=request_options,
        )

    async def postgres_service_patch_state(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceSetState | PostgresServiceSetStateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresStateResponse, PostgresServicePatchStateErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Initiate a process for a Postgres service:
        * restart: Initiates a service restart
        * promote: Promotes a read replica to primary
        * switchover: Switch a primary over to a standby

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/state"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresServiceSetState | PostgresServiceSetStateDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresStateResponse],
            error_mapper=postgres_service_patch_state_error_mapper,
            request_options=request_options,
        )

    async def postgres_service_set_password(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        *,
        body: PostgresServiceSetPassword | PostgresServiceSetPasswordDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresPasswordResponse, PostgresServiceSetPasswordErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Sets a new password for a Postgres service's superuser account.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/password"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PostgresServiceSetPassword | PostgresServiceSetPasswordDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresPasswordResponse],
            error_mapper=postgres_service_set_password_error_mapper,
            request_options=request_options,
        )

    async def slow_query_pattern_get(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        query_id: str,
        db_name: str,
        db_user: str,
        db_operation: str,
        *,
        app: str | None = None,
        timestamp: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse, SlowQueryPatternGetErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns aggregate metrics for a single slow query pattern together with its most recent individual
        executions.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            query_id: Stable identifier for the query pattern.
            db_name: Database name filter.
            db_user: Database user filter.
            db_operation: Database operation filter (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY).
            app: Application name filter.
            timestamp: Timestamp of a specific execution (RFC 3339).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/postgres/{postgresId}/slowQueryPatterns/{queryId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("postgresId", postgres_id),
                param[str]("queryId", query_id),
            ],
            query_params=[
                param[str]("db_name", db_name),
                param[str]("db_user", db_user),
                param[str]("db_operation", db_operation),
                param[str | None]("app", app),
                param[RFC3339DateTime | None]("timestamp", timestamp),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse],
            error_mapper=slow_query_pattern_get_error_mapper,
            request_options=request_options,
        )

    async def slow_query_patterns_get_list(
        self,
        organization_id: UUID,
        postgres_id: UUID,
        from_date: RFC3339DateTime,
        to_date: RFC3339DateTime,
        *,
        db_name: str | None = None,
        db_user: str | None = None,
        db_operation: str | None = None,
        app: str | None = None,
        sort_by: SortByOrStr | None = SortBy.TOTAL_DURATION,
        sort_order: SortOrder1OrStr | None = SortOrder1.DESC,
        limit: int | None = 20,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsPostgresSlowQueryPatternsResponse, SlowQueryPatternsGetListErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> Returns aggregate metrics for the slowest query patterns observed on a Postgres service during the
        given time window. Use this to discover which queries dominate total execution time, CPU, I/O, or WAL
        generation.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            from_date: Inclusive start of the time window (RFC 3339 date-time).
            to_date: Exclusive end of the time window (RFC 3339 date-time).
            db_name: Database name filter.
            db_user: Database user filter.
            db_operation: Database operation filter (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY).
            app: Application name filter.
            sort_by: Field to sort results by.
            sort_order: Sort order. One of ``asc`` or ``desc``.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/postgres/{postgresId}/slowQueryPatterns"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            query_params=[
                param[RFC3339DateTime]("from_date", from_date),
                param[RFC3339DateTime]("to_date", to_date),
                param[str | None]("db_name", db_name),
                param[str | None]("db_user", db_user),
                param[str | None]("db_operation", db_operation),
                param[str | None]("app", app),
                param[SortByOrStr | None]("sort_by", sort_by),
                param[SortOrder1OrStr | None]("sort_order", sort_order),
                param[int | None]("limit", limit),
                param[int | None]("offset", offset),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsPostgresSlowQueryPatternsResponse],
            error_mapper=slow_query_patterns_get_list_error_mapper,
            request_options=request_options,
        )
