from __future__ import annotations

from uuid import UUID

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.active_balances_get_error import ActiveBalancesGetErrorBody, active_balances_get_error_mapper
from ..errors.credit_balances_get_error import CreditBalancesGetErrorBody, credit_balances_get_error_mapper
from ..errors.usage_cost_get_error import UsageCostGetErrorBody, usage_cost_get_error_mapper
from ..models.v1_organizations_active_balances_response import V1OrganizationsActiveBalancesResponse
from ..models.v1_organizations_credit_balances_response import V1OrganizationsCreditBalancesResponse
from ..models.v1_organizations_usage_cost_response import V1OrganizationsUsageCostResponse
from ..server.server import Server


class Billing:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BillingWithRawResponse(client, server, auth)

    def active_balances_get(
        self,
        organization_id: UUID,
        *,
        limit: int | None = 100,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsActiveBalancesResponse:
        """DEPRECATED. Use the ``/v1/organizations/{organizationId}/creditBalances`` endpoint instead. <br /><br />
        Returns the active prepaid credit balances for the organization, each with its own balance ID and remaining
        credits, along with the total remaining credits across all active balances. A balance is active when it has
        started, has not expired, and has credits remaining. Balances are ordered by expiration date, soonest first, and
        the returned page is capped at ``limit`` (default and maximum 100). When ``totalCount`` exceeds the number of
        returned balances, page with ``limit``/``offset`` to retrieve them all. ``totalRemainingPrepaidCredits`` always
        covers every active balance, not just the returned page.

        Args:
            organization_id: ID of the requested organization.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsActiveBalances400Error1 |
                V1OrganizationsActiveBalances500Error1 | RawError``."""
        return self._with_raw_response.active_balances_get(
            organization_id, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def credit_balances_get(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsCreditBalancesResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the active
        credit balances for the organization, each with its own balance ID, type and remaining credits, along with the
        total remaining credits across all of them. A balance is active when it has started, has not expired, and has
        credits remaining. Balances are ordered by expiration date, soonest first. The list is always present and is
        empty when the organization has no active balances.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsCreditBalances400Error1 |
                V1OrganizationsCreditBalances500Error1 | RawError``."""
        return self._with_raw_response.credit_balances_get(organization_id, request_options=request_options).unwrap()

    def usage_cost_get(
        self,
        organization_id: UUID,
        from_date: Date,
        to_date: Date,
        *,
        filter: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUsageCostResponse:
        """Returns a grand total and a list of daily, per-entity organization usage cost records for the organization in
        the queried time period (maximum 31 days). All days in both the request and the response are evaluated based on
        the UTC timezone.

        Args:
            organization_id: ID of the requested organization.
            from_date: Start date for the report, e.g. 2024-12-19.
            to_date: End date (inclusive) for the report, e.g. 2024-12-20. This date cannot be more than 30 days after
                from_date (for a maximum queried period of 31 days).
            filter: Filter criteria to apply when retrieving the usage cost report. Currently, only filtering by
                resource tags is supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsUsageCost400Error1 |
                V1OrganizationsUsageCost500Error1 | RawError``."""
        return self._with_raw_response.usage_cost_get(
            organization_id, from_date, to_date, filter=filter, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> BillingWithRawResponse:
        return self._with_raw_response


class AsyncBilling:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBillingWithRawResponse(client, server, auth)

    async def active_balances_get(
        self,
        organization_id: UUID,
        *,
        limit: int | None = 100,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsActiveBalancesResponse:
        """DEPRECATED. Use the ``/v1/organizations/{organizationId}/creditBalances`` endpoint instead. <br /><br />
        Returns the active prepaid credit balances for the organization, each with its own balance ID and remaining
        credits, along with the total remaining credits across all active balances. A balance is active when it has
        started, has not expired, and has credits remaining. Balances are ordered by expiration date, soonest first, and
        the returned page is capped at ``limit`` (default and maximum 100). When ``totalCount`` exceeds the number of
        returned balances, page with ``limit``/``offset`` to retrieve them all. ``totalRemainingPrepaidCredits`` always
        covers every active balance, not just the returned page.

        Args:
            organization_id: ID of the requested organization.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsActiveBalances400Error1 |
                V1OrganizationsActiveBalances500Error1 | RawError``."""
        return (
            await self._with_raw_response.active_balances_get(
                organization_id, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def credit_balances_get(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsCreditBalancesResponse:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the active
        credit balances for the organization, each with its own balance ID, type and remaining credits, along with the
        total remaining credits across all of them. A balance is active when it has started, has not expired, and has
        credits remaining. Balances are ordered by expiration date, soonest first. The list is always present and is
        empty when the organization has no active balances.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsCreditBalances400Error1 |
                V1OrganizationsCreditBalances500Error1 | RawError``."""
        return (
            await self._with_raw_response.credit_balances_get(organization_id, request_options=request_options)
        ).unwrap()

    async def usage_cost_get(
        self,
        organization_id: UUID,
        from_date: Date,
        to_date: Date,
        *,
        filter: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsUsageCostResponse:
        """Returns a grand total and a list of daily, per-entity organization usage cost records for the organization in
        the queried time period (maximum 31 days). All days in both the request and the response are evaluated based on
        the UTC timezone.

        Args:
            organization_id: ID of the requested organization.
            from_date: Start date for the report, e.g. 2024-12-19.
            to_date: End date (inclusive) for the report, e.g. 2024-12-20. This date cannot be more than 30 days after
                from_date (for a maximum queried period of 31 days).
            filter: Filter criteria to apply when retrieving the usage cost report. Currently, only filtering by
                resource tags is supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsUsageCost400Error1 |
                V1OrganizationsUsageCost500Error1 | RawError``."""
        return (
            await self._with_raw_response.usage_cost_get(
                organization_id, from_date, to_date, filter=filter, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncBillingWithRawResponse:
        return self._with_raw_response


class BillingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def active_balances_get(
        self,
        organization_id: UUID,
        *,
        limit: int | None = 100,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsActiveBalancesResponse, ActiveBalancesGetErrorBody]:
        """DEPRECATED. Use the ``/v1/organizations/{organizationId}/creditBalances`` endpoint instead. <br /><br />
        Returns the active prepaid credit balances for the organization, each with its own balance ID and remaining
        credits, along with the total remaining credits across all active balances. A balance is active when it has
        started, has not expired, and has credits remaining. Balances are ordered by expiration date, soonest first, and
        the returned page is capped at ``limit`` (default and maximum 100). When ``totalCount`` exceeds the number of
        returned balances, page with ``limit``/``offset`` to retrieve them all. ``totalRemainingPrepaidCredits`` always
        covers every active balance, not just the returned page.

        Args:
            organization_id: ID of the requested organization.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/activeBalances"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsActiveBalancesResponse],
            error_mapper=active_balances_get_error_mapper,
            request_options=request_options,
        )

    def credit_balances_get(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsCreditBalancesResponse, CreditBalancesGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the active
        credit balances for the organization, each with its own balance ID, type and remaining credits, along with the
        total remaining credits across all of them. A balance is active when it has started, has not expired, and has
        credits remaining. Balances are ordered by expiration date, soonest first. The list is always present and is
        empty when the organization has no active balances.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/creditBalances"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsCreditBalancesResponse],
            error_mapper=credit_balances_get_error_mapper,
            request_options=request_options,
        )

    def usage_cost_get(
        self,
        organization_id: UUID,
        from_date: Date,
        to_date: Date,
        *,
        filter: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUsageCostResponse, UsageCostGetErrorBody]:
        """Returns a grand total and a list of daily, per-entity organization usage cost records for the organization in
        the queried time period (maximum 31 days). All days in both the request and the response are evaluated based on
        the UTC timezone.

        Args:
            organization_id: ID of the requested organization.
            from_date: Start date for the report, e.g. 2024-12-19.
            to_date: End date (inclusive) for the report, e.g. 2024-12-20. This date cannot be more than 30 days after
                from_date (for a maximum queried period of 31 days).
            filter: Filter criteria to apply when retrieving the usage cost report. Currently, only filtering by
                resource tags is supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/usageCost"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[
                param[Date]("from_date", from_date),
                param[Date]("to_date", to_date),
                param[list[str] | None]("filter", filter),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUsageCostResponse],
            error_mapper=usage_cost_get_error_mapper,
            request_options=request_options,
        )


class AsyncBillingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def active_balances_get(
        self,
        organization_id: UUID,
        *,
        limit: int | None = 100,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsActiveBalancesResponse, ActiveBalancesGetErrorBody]:
        """DEPRECATED. Use the ``/v1/organizations/{organizationId}/creditBalances`` endpoint instead. <br /><br />
        Returns the active prepaid credit balances for the organization, each with its own balance ID and remaining
        credits, along with the total remaining credits across all active balances. A balance is active when it has
        started, has not expired, and has credits remaining. Balances are ordered by expiration date, soonest first, and
        the returned page is capped at ``limit`` (default and maximum 100). When ``totalCount`` exceeds the number of
        returned balances, page with ``limit``/``offset`` to retrieve them all. ``totalRemainingPrepaidCredits`` always
        covers every active balance, not just the returned page.

        Args:
            organization_id: ID of the requested organization.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/activeBalances"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsActiveBalancesResponse],
            error_mapper=active_balances_get_error_mapper,
            request_options=request_options,
        )

    async def credit_balances_get(
        self, organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsCreditBalancesResponse, CreditBalancesGetErrorBody]:
        """**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the active
        credit balances for the organization, each with its own balance ID, type and remaining credits, along with the
        total remaining credits across all of them. A balance is active when it has started, has not expired, and has
        credits remaining. Balances are ordered by expiration date, soonest first. The list is always present and is
        empty when the organization has no active balances.

        Args:
            organization_id: ID of the requested organization.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/creditBalances"),
            path_params=[param[UUID]("organizationId", organization_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsCreditBalancesResponse],
            error_mapper=credit_balances_get_error_mapper,
            request_options=request_options,
        )

    async def usage_cost_get(
        self,
        organization_id: UUID,
        from_date: Date,
        to_date: Date,
        *,
        filter: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsUsageCostResponse, UsageCostGetErrorBody]:
        """Returns a grand total and a list of daily, per-entity organization usage cost records for the organization in
        the queried time period (maximum 31 days). All days in both the request and the response are evaluated based on
        the UTC timezone.

        Args:
            organization_id: ID of the requested organization.
            from_date: Start date for the report, e.g. 2024-12-19.
            to_date: End date (inclusive) for the report, e.g. 2024-12-20. This date cannot be more than 30 days after
                from_date (for a maximum queried period of 31 days).
            filter: Filter criteria to apply when retrieving the usage cost report. Currently, only filtering by
                resource tags is supported.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/organizations/{organizationId}/usageCost"),
            path_params=[param[UUID]("organizationId", organization_id)],
            query_params=[
                param[Date]("from_date", from_date),
                param[Date]("to_date", to_date),
                param[list[str] | None]("filter", filter),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsUsageCostResponse],
            error_mapper=usage_cost_get_error_mapper,
            request_options=request_options,
        )
