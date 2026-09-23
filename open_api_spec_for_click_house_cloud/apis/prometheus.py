from __future__ import annotations

from uuid import UUID

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    text_decoder,
)
from ..errors.instance_prometheus_get_error import InstancePrometheusGetErrorBody, instance_prometheus_get_error_mapper
from ..errors.organization_prometheus_discovery_get_error import (
    OrganizationPrometheusDiscoveryGetErrorBody,
    organization_prometheus_discovery_get_error_mapper,
)
from ..errors.organization_prometheus_get_error import (
    OrganizationPrometheusGetErrorBody,
    organization_prometheus_get_error_mapper,
)
from ..errors.postgres_instance_prometheus_get_error import (
    PostgresInstancePrometheusGetErrorBody,
    postgres_instance_prometheus_get_error_mapper,
)
from ..errors.postgres_org_prometheus_get_error import (
    PostgresOrgPrometheusGetErrorBody,
    postgres_org_prometheus_get_error_mapper,
)
from ..models.prometheus_discovery_target_group import PrometheusDiscoveryTargetGroup
from ..server.server import Server


class Prometheus:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PrometheusWithRawResponse(client, server, auth)

    def instance_prometheus_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        filtered_metrics: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> str:
        """Returns prometheus metrics for a service.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the requested service.
            filtered_metrics: Return a filtered list of Prometheus metrics.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesPrometheus400Error1 |
                V1OrganizationsServicesPrometheus500Error1 | RawError``."""
        return self._with_raw_response.instance_prometheus_get(
            organization_id, service_id, filtered_metrics=filtered_metrics, request_options=request_options
        ).unwrap()

    def organization_prometheus_discovery_get(
        self,
        organization_id: UUID,
        *,
        filtered_metrics: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PrometheusDiscoveryTargetGroup]:
        """Returns one Prometheus scrape target per service in the organization, in the `HTTP service discovery
        <https://prometheus.io/docs/prometheus/latest/http_sd/>`__ (``http_sd``) format. Only services the API key is
        authorized to view are included; services that are being deleted or have been deleted are omitted.

        Point an https://prometheus.io/docs/prometheus/latest/configuration/configuration/#http_sd_config job at this
        endpoint to discover and scrape all services in the organization automatically. Prometheus refreshes the target
        list on every discovery poll, so newly created and deleted services are picked up without configuration changes.

        Discovered targets scrape with ``filtered_metrics=true`` by default; pass ``?filtered_metrics=false`` to this
        endpoint to discover unfiltered targets. See the `Prometheus integration guide
        <https://clickhouse.com/docs/integrations/prometheus>`__ for more on the exported metrics.

        Args:
            organization_id: ID of the requested organization.
            filtered_metrics: Whether discovered targets scrape a filtered list of metrics. Sets the filtered_metrics
                parameter on each discovered target. Defaults to true.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPrometheusDiscovery400Error1 |
                V1OrganizationsPrometheusDiscovery500Error1 | RawError``."""
        return self._with_raw_response.organization_prometheus_discovery_get(
            organization_id, filtered_metrics=filtered_metrics, request_options=request_options
        ).unwrap()

    def organization_prometheus_get(
        self,
        organization_id: UUID,
        *,
        filtered_metrics: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> str:
        """Deprecated. Use the Prometheus service discovery endpoint
        (/v1/organizations/{organizationId}/prometheus/discovery) instead. This endpoint is not available for new
        organizations; contact ClickHouse support to request access. Returns Prometheus metrics for the services in an
        organization that the caller is authorized to view. Services the caller lacks view access to are omitted.

        Args:
            organization_id: ID of the requested organization.
            filtered_metrics: Return a filtered list of Prometheus metrics.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPrometheus400Error1 |
                V1OrganizationsPrometheus500Error1 | RawError``."""
        return self._with_raw_response.organization_prometheus_get(
            organization_id, filtered_metrics=filtered_metrics, request_options=request_options
        ).unwrap()

    def postgres_instance_prometheus_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> str:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns Prometheus
        metrics for a PostgreSQL service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresPrometheus400Error1 |
                V1OrganizationsPostgresPrometheus500Error1 | RawError``."""
        return self._with_raw_response.postgres_instance_prometheus_get(
            organization_id, postgres_id, request_options=request_options
        ).unwrap()

    def postgres_org_prometheus_get(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> str:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns Prometheus
        metrics for all PostgreSQL services in an organization. Maximum 100 services supported.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresPrometheus400Error1 |
                V1OrganizationsPostgresPrometheus500Error1 | RawError``."""
        return self._with_raw_response.postgres_org_prometheus_get(
            organization_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PrometheusWithRawResponse:
        return self._with_raw_response


class AsyncPrometheus:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPrometheusWithRawResponse(client, server, auth)

    async def instance_prometheus_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        filtered_metrics: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> str:
        """Returns prometheus metrics for a service.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the requested service.
            filtered_metrics: Return a filtered list of Prometheus metrics.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesPrometheus400Error1 |
                V1OrganizationsServicesPrometheus500Error1 | RawError``."""
        return (
            await self._with_raw_response.instance_prometheus_get(
                organization_id, service_id, filtered_metrics=filtered_metrics, request_options=request_options
            )
        ).unwrap()

    async def organization_prometheus_discovery_get(
        self,
        organization_id: UUID,
        *,
        filtered_metrics: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[PrometheusDiscoveryTargetGroup]:
        """Returns one Prometheus scrape target per service in the organization, in the `HTTP service discovery
        <https://prometheus.io/docs/prometheus/latest/http_sd/>`__ (``http_sd``) format. Only services the API key is
        authorized to view are included; services that are being deleted or have been deleted are omitted.

        Point an https://prometheus.io/docs/prometheus/latest/configuration/configuration/#http_sd_config job at this
        endpoint to discover and scrape all services in the organization automatically. Prometheus refreshes the target
        list on every discovery poll, so newly created and deleted services are picked up without configuration changes.

        Discovered targets scrape with ``filtered_metrics=true`` by default; pass ``?filtered_metrics=false`` to this
        endpoint to discover unfiltered targets. See the `Prometheus integration guide
        <https://clickhouse.com/docs/integrations/prometheus>`__ for more on the exported metrics.

        Args:
            organization_id: ID of the requested organization.
            filtered_metrics: Whether discovered targets scrape a filtered list of metrics. Sets the filtered_metrics
                parameter on each discovered target. Defaults to true.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPrometheusDiscovery400Error1 |
                V1OrganizationsPrometheusDiscovery500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_prometheus_discovery_get(
                organization_id, filtered_metrics=filtered_metrics, request_options=request_options
            )
        ).unwrap()

    async def organization_prometheus_get(
        self,
        organization_id: UUID,
        *,
        filtered_metrics: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> str:
        """Deprecated. Use the Prometheus service discovery endpoint
        (/v1/organizations/{organizationId}/prometheus/discovery) instead. This endpoint is not available for new
        organizations; contact ClickHouse support to request access. Returns Prometheus metrics for the services in an
        organization that the caller is authorized to view. Services the caller lacks view access to are omitted.

        Args:
            organization_id: ID of the requested organization.
            filtered_metrics: Return a filtered list of Prometheus metrics.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPrometheus400Error1 |
                V1OrganizationsPrometheus500Error1 | RawError``."""
        return (
            await self._with_raw_response.organization_prometheus_get(
                organization_id, filtered_metrics=filtered_metrics, request_options=request_options
            )
        ).unwrap()

    async def postgres_instance_prometheus_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> str:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns Prometheus
        metrics for a PostgreSQL service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresPrometheus400Error1 |
                V1OrganizationsPostgresPrometheus500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_instance_prometheus_get(
                organization_id, postgres_id, request_options=request_options
            )
        ).unwrap()

    async def postgres_org_prometheus_get(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> str:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns Prometheus
        metrics for all PostgreSQL services in an organization. Maximum 100 services supported.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsPostgresPrometheus400Error1 |
                V1OrganizationsPostgresPrometheus500Error1 | RawError``."""
        return (
            await self._with_raw_response.postgres_org_prometheus_get(organization_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPrometheusWithRawResponse:
        return self._with_raw_response


class PrometheusWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def instance_prometheus_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        filtered_metrics: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[str, InstancePrometheusGetErrorBody]:
        """Returns prometheus metrics for a service.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the requested service.
            filtered_metrics: Return a filtered list of Prometheus metrics.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/prometheus"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            query_params=[param[str | None]("filtered_metrics", filtered_metrics)],
            auth_scheme=self._auth.basic_auth,
            decoder=text_decoder[str],
            error_mapper=instance_prometheus_get_error_mapper,
            request_options=request_options,
        )

    def organization_prometheus_discovery_get(
        self,
        organization_id: UUID,
        *,
        filtered_metrics: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PrometheusDiscoveryTargetGroup], OrganizationPrometheusDiscoveryGetErrorBody]:
        """Returns one Prometheus scrape target per service in the organization, in the `HTTP service discovery
        <https://prometheus.io/docs/prometheus/latest/http_sd/>`__ (``http_sd``) format. Only services the API key is
        authorized to view are included; services that are being deleted or have been deleted are omitted.

        Point an https://prometheus.io/docs/prometheus/latest/configuration/configuration/#http_sd_config job at this
        endpoint to discover and scrape all services in the organization automatically. Prometheus refreshes the target
        list on every discovery poll, so newly created and deleted services are picked up without configuration changes.

        Discovered targets scrape with ``filtered_metrics=true`` by default; pass ``?filtered_metrics=false`` to this
        endpoint to discover unfiltered targets. See the `Prometheus integration guide
        <https://clickhouse.com/docs/integrations/prometheus>`__ for more on the exported metrics.

        Args:
            organization_id: ID of the requested organization.
            filtered_metrics: Whether discovered targets scrape a filtered list of metrics. Sets the filtered_metrics
                parameter on each discovered target. Defaults to true.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/prometheus/discovery"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[str | None]("filtered_metrics", filtered_metrics)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[PrometheusDiscoveryTargetGroup]],
            error_mapper=organization_prometheus_discovery_get_error_mapper,
            request_options=request_options,
        )

    def organization_prometheus_get(
        self,
        organization_id: UUID,
        *,
        filtered_metrics: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[str, OrganizationPrometheusGetErrorBody]:
        """Deprecated. Use the Prometheus service discovery endpoint
        (/v1/organizations/{organizationId}/prometheus/discovery) instead. This endpoint is not available for new
        organizations; contact ClickHouse support to request access. Returns Prometheus metrics for the services in an
        organization that the caller is authorized to view. Services the caller lacks view access to are omitted.

        Args:
            organization_id: ID of the requested organization.
            filtered_metrics: Return a filtered list of Prometheus metrics.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/prometheus"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[str | None]("filtered_metrics", filtered_metrics)],
            auth_scheme=self._auth.basic_auth,
            decoder=text_decoder[str],
            error_mapper=organization_prometheus_get_error_mapper,
            request_options=request_options,
        )

    def postgres_instance_prometheus_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[str, PostgresInstancePrometheusGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns Prometheus
        metrics for a PostgreSQL service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/prometheus"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=text_decoder[str],
            error_mapper=postgres_instance_prometheus_get_error_mapper,
            request_options=request_options,
        )

    def postgres_org_prometheus_get(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[str, PostgresOrgPrometheusGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns Prometheus
        metrics for all PostgreSQL services in an organization. Maximum 100 services supported.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/prometheus"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=text_decoder[str],
            error_mapper=postgres_org_prometheus_get_error_mapper,
            request_options=request_options,
        )


class AsyncPrometheusWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def instance_prometheus_get(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        filtered_metrics: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[str, InstancePrometheusGetErrorBody]:
        """Returns prometheus metrics for a service.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the requested service.
            filtered_metrics: Return a filtered list of Prometheus metrics.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/services/{serviceId}/prometheus"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            query_params=[param[str | None]("filtered_metrics", filtered_metrics)],
            auth_scheme=self._auth.basic_auth,
            decoder=text_decoder[str],
            error_mapper=instance_prometheus_get_error_mapper,
            request_options=request_options,
        )

    async def organization_prometheus_discovery_get(
        self,
        organization_id: UUID,
        *,
        filtered_metrics: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[PrometheusDiscoveryTargetGroup], OrganizationPrometheusDiscoveryGetErrorBody]:
        """Returns one Prometheus scrape target per service in the organization, in the `HTTP service discovery
        <https://prometheus.io/docs/prometheus/latest/http_sd/>`__ (``http_sd``) format. Only services the API key is
        authorized to view are included; services that are being deleted or have been deleted are omitted.

        Point an https://prometheus.io/docs/prometheus/latest/configuration/configuration/#http_sd_config job at this
        endpoint to discover and scrape all services in the organization automatically. Prometheus refreshes the target
        list on every discovery poll, so newly created and deleted services are picked up without configuration changes.

        Discovered targets scrape with ``filtered_metrics=true`` by default; pass ``?filtered_metrics=false`` to this
        endpoint to discover unfiltered targets. See the `Prometheus integration guide
        <https://clickhouse.com/docs/integrations/prometheus>`__ for more on the exported metrics.

        Args:
            organization_id: ID of the requested organization.
            filtered_metrics: Whether discovered targets scrape a filtered list of metrics. Sets the filtered_metrics
                parameter on each discovered target. Defaults to true.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/prometheus/discovery"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[str | None]("filtered_metrics", filtered_metrics)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[list[PrometheusDiscoveryTargetGroup]],
            error_mapper=organization_prometheus_discovery_get_error_mapper,
            request_options=request_options,
        )

    async def organization_prometheus_get(
        self,
        organization_id: UUID,
        *,
        filtered_metrics: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[str, OrganizationPrometheusGetErrorBody]:
        """Deprecated. Use the Prometheus service discovery endpoint
        (/v1/organizations/{organizationId}/prometheus/discovery) instead. This endpoint is not available for new
        organizations; contact ClickHouse support to request access. Returns Prometheus metrics for the services in an
        organization that the caller is authorized to view. Services the caller lacks view access to are omitted.

        Args:
            organization_id: ID of the requested organization.
            filtered_metrics: Return a filtered list of Prometheus metrics.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/prometheus"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[str | None]("filtered_metrics", filtered_metrics)],
            auth_scheme=self._auth.basic_auth,
            decoder=text_decoder[str],
            error_mapper=organization_prometheus_get_error_mapper,
            request_options=request_options,
        )

    async def postgres_instance_prometheus_get(
        self, organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[str, PostgresInstancePrometheusGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns Prometheus
        metrics for a PostgreSQL service.

        Args:
            organization_id: ID of the organization that owns the Postgres service.
            postgres_id: ID of the requested Postgres service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/{postgresId}/prometheus"),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("postgresId", postgres_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=text_decoder[str],
            error_mapper=postgres_instance_prometheus_get_error_mapper,
            request_options=request_options,
        )

    async def postgres_org_prometheus_get(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[str, PostgresOrgPrometheusGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns Prometheus
        metrics for all PostgreSQL services in an organization. Maximum 100 services supported.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/postgres/prometheus"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=text_decoder[str],
            error_mapper=postgres_org_prometheus_get_error_mapper,
            request_options=request_options,
        )
