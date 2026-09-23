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
from ..errors.click_stack_create_alert_error import (
    ClickStackCreateAlertErrorBody,
    click_stack_create_alert_error_mapper,
)
from ..errors.click_stack_create_dashboard_error import (
    ClickStackCreateDashboardErrorBody,
    click_stack_create_dashboard_error_mapper,
)
from ..errors.click_stack_create_role_error import ClickStackCreateRoleErrorBody, click_stack_create_role_error_mapper
from ..errors.click_stack_create_saved_search_error import (
    ClickStackCreateSavedSearchErrorBody,
    click_stack_create_saved_search_error_mapper,
)
from ..errors.click_stack_create_source_error import (
    ClickStackCreateSourceErrorBody,
    click_stack_create_source_error_mapper,
)
from ..errors.click_stack_create_webhook_error import (
    ClickStackCreateWebhookErrorBody,
    click_stack_create_webhook_error_mapper,
)
from ..errors.click_stack_delete_alert_error import (
    ClickStackDeleteAlertErrorBody,
    click_stack_delete_alert_error_mapper,
)
from ..errors.click_stack_delete_dashboard_error import (
    ClickStackDeleteDashboardErrorBody,
    click_stack_delete_dashboard_error_mapper,
)
from ..errors.click_stack_delete_role_error import ClickStackDeleteRoleErrorBody, click_stack_delete_role_error_mapper
from ..errors.click_stack_delete_saved_search_error import (
    ClickStackDeleteSavedSearchErrorBody,
    click_stack_delete_saved_search_error_mapper,
)
from ..errors.click_stack_delete_source_error import (
    ClickStackDeleteSourceErrorBody,
    click_stack_delete_source_error_mapper,
)
from ..errors.click_stack_delete_webhook_error import (
    ClickStackDeleteWebhookErrorBody,
    click_stack_delete_webhook_error_mapper,
)
from ..errors.click_stack_get_alert_error import ClickStackGetAlertErrorBody, click_stack_get_alert_error_mapper
from ..errors.click_stack_get_dashboard_error import (
    ClickStackGetDashboardErrorBody,
    click_stack_get_dashboard_error_mapper,
)
from ..errors.click_stack_get_role_error import ClickStackGetRoleErrorBody, click_stack_get_role_error_mapper
from ..errors.click_stack_get_saved_search_error import (
    ClickStackGetSavedSearchErrorBody,
    click_stack_get_saved_search_error_mapper,
)
from ..errors.click_stack_get_source_error import ClickStackGetSourceErrorBody, click_stack_get_source_error_mapper
from ..errors.click_stack_list_alerts_error import ClickStackListAlertsErrorBody, click_stack_list_alerts_error_mapper
from ..errors.click_stack_list_dashboards_error import (
    ClickStackListDashboardsErrorBody,
    click_stack_list_dashboards_error_mapper,
)
from ..errors.click_stack_list_roles_error import ClickStackListRolesErrorBody, click_stack_list_roles_error_mapper
from ..errors.click_stack_list_saved_searches_error import (
    ClickStackListSavedSearchesErrorBody,
    click_stack_list_saved_searches_error_mapper,
)
from ..errors.click_stack_list_sources_error import (
    ClickStackListSourcesErrorBody,
    click_stack_list_sources_error_mapper,
)
from ..errors.click_stack_list_webhooks_error import (
    ClickStackListWebhooksErrorBody,
    click_stack_list_webhooks_error_mapper,
)
from ..errors.click_stack_update_alert_error import (
    ClickStackUpdateAlertErrorBody,
    click_stack_update_alert_error_mapper,
)
from ..errors.click_stack_update_dashboard_error import (
    ClickStackUpdateDashboardErrorBody,
    click_stack_update_dashboard_error_mapper,
)
from ..errors.click_stack_update_role_error import ClickStackUpdateRoleErrorBody, click_stack_update_role_error_mapper
from ..errors.click_stack_update_saved_search_error import (
    ClickStackUpdateSavedSearchErrorBody,
    click_stack_update_saved_search_error_mapper,
)
from ..errors.click_stack_update_source_error import (
    ClickStackUpdateSourceErrorBody,
    click_stack_update_source_error_mapper,
)
from ..errors.click_stack_update_webhook_error import (
    ClickStackUpdateWebhookErrorBody,
    click_stack_update_webhook_error_mapper,
)
from ..errors.click_stack_validate_dashboard_error import (
    ClickStackValidateDashboardErrorBody,
    click_stack_validate_dashboard_error_mapper,
)
from ..models.click_stack_create_alert_request import ClickStackCreateAlertRequest, ClickStackCreateAlertRequestDict
from ..models.click_stack_create_dashboard_request import (
    ClickStackCreateDashboardRequest,
    ClickStackCreateDashboardRequestDict,
)
from ..models.click_stack_create_role_request import ClickStackCreateRoleRequest, ClickStackCreateRoleRequestDict
from ..models.click_stack_saved_search_input import ClickStackSavedSearchInput, ClickStackSavedSearchInputDict
from ..models.click_stack_update_alert_request import ClickStackUpdateAlertRequest, ClickStackUpdateAlertRequestDict
from ..models.click_stack_update_dashboard_request import (
    ClickStackUpdateDashboardRequest,
    ClickStackUpdateDashboardRequestDict,
)
from ..models.click_stack_update_role_request import ClickStackUpdateRoleRequest, ClickStackUpdateRoleRequestDict
from ..models.click_stack_webhook_input import ClickStackWebhookInput, ClickStackWebhookInputDict
from ..models.unions.click_stack_source import ClickStackSource, ClickStackSourceDict
from ..models.v1_organizations_services_clickstack_alerts_click_stack_alert_id_response import (
    V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse,
)
from ..models.v1_organizations_services_clickstack_alerts_click_stack_alert_id_response2 import (
    V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2,
)
from ..models.v1_organizations_services_clickstack_alerts_response import (
    V1OrganizationsServicesClickstackAlertsResponse,
)
from ..models.v1_organizations_services_clickstack_alerts_response1 import (
    V1OrganizationsServicesClickstackAlertsResponse1,
)
from ..models.v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response import (
    V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse,
)
from ..models.v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response2 import (
    V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2,
)
from ..models.v1_organizations_services_clickstack_dashboards_response import (
    V1OrganizationsServicesClickstackDashboardsResponse,
)
from ..models.v1_organizations_services_clickstack_dashboards_response1 import (
    V1OrganizationsServicesClickstackDashboardsResponse1,
)
from ..models.v1_organizations_services_clickstack_dashboards_validate_response import (
    V1OrganizationsServicesClickstackDashboardsValidateResponse,
)
from ..models.v1_organizations_services_clickstack_roles_click_stack_role_id_response import (
    V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse,
)
from ..models.v1_organizations_services_clickstack_roles_click_stack_role_id_response2 import (
    V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2,
)
from ..models.v1_organizations_services_clickstack_roles_response import V1OrganizationsServicesClickstackRolesResponse
from ..models.v1_organizations_services_clickstack_roles_response1 import (
    V1OrganizationsServicesClickstackRolesResponse1,
)
from ..models.v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response import (
    V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse,
)
from ..models.v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response2 import (
    V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2,
)
from ..models.v1_organizations_services_clickstack_saved_searches_response import (
    V1OrganizationsServicesClickstackSavedSearchesResponse,
)
from ..models.v1_organizations_services_clickstack_saved_searches_response1 import (
    V1OrganizationsServicesClickstackSavedSearchesResponse1,
)
from ..models.v1_organizations_services_clickstack_sources_click_stack_source_id_response import (
    V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse,
)
from ..models.v1_organizations_services_clickstack_sources_click_stack_source_id_response2 import (
    V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2,
)
from ..models.v1_organizations_services_clickstack_sources_response import (
    V1OrganizationsServicesClickstackSourcesResponse,
)
from ..models.v1_organizations_services_clickstack_sources_response1 import (
    V1OrganizationsServicesClickstackSourcesResponse1,
)
from ..models.v1_organizations_services_clickstack_webhooks_click_stack_webhook_id_response import (
    V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse,
)
from ..models.v1_organizations_services_clickstack_webhooks_click_stack_webhook_id_response1 import (
    V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1,
)
from ..models.v1_organizations_services_clickstack_webhooks_response import (
    V1OrganizationsServicesClickstackWebhooksResponse,
)
from ..models.v1_organizations_services_clickstack_webhooks_response1 import (
    V1OrganizationsServicesClickstackWebhooksResponse1,
)
from ..server.server import Server


class ClickStack:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ClickStackWithRawResponse(client, server, auth)

    def click_stack_create_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateAlertRequest | ClickStackCreateAlertRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackAlertsResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new alert

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackAlerts400Error1 |
                V1OrganizationsServicesClickstackAlerts500Error1 | RawError``."""
        return self._with_raw_response.click_stack_create_alert(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def click_stack_create_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackDashboardsResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new dashboard

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackDashboards400Error1 |
                V1OrganizationsServicesClickstackDashboards500Error1 | RawError``."""
        return self._with_raw_response.click_stack_create_dashboard(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def click_stack_create_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateRoleRequest | ClickStackCreateRoleRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackRolesResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new custom role for the team.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackRoles400Error1 |
                V1OrganizationsServicesClickstackRoles500Error1 | RawError``."""
        return self._with_raw_response.click_stack_create_role(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def click_stack_create_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSavedSearchesResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new saved search.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackSavedSearches400Error1 |
                V1OrganizationsServicesClickstackSavedSearches500Error1 | RawError``."""
        return self._with_raw_response.click_stack_create_saved_search(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def click_stack_create_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackSource | ClickStackSourceDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSourcesResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new source. The request body is a source object without the ``id`` field. If an
        ``id`` is sent anyway it is silently ignored (stripped before validation — the request is never rejected because
        of it). Granularity fields (``materializedViews[].minGranularity`` and
        ``metadataMaterializedViews.granularity``) accept the same short format the API returns (e.g. ``5m``, ``15s``,
        ``1h``, ``1d``).

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackSources400Error1 |
                V1OrganizationsServicesClickstackSources500Error1 | RawError``."""
        return self._with_raw_response.click_stack_create_source(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def click_stack_create_webhook(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackWebhooksResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new webhook for the authenticated team.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackWebhooks400Error1 |
                V1OrganizationsServicesClickstackWebhooks500Error1 | RawError``."""
        return self._with_raw_response.click_stack_create_webhook(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    def click_stack_delete_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_alert_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes an alert

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_alert_id: ClickStack Alert ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1 |
                V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_delete_alert(
            organization_id, service_id, click_stack_alert_id, request_options=request_options
        ).unwrap()

    def click_stack_delete_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_dashboard_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a dashboard

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_dashboard_id: ClickStack Dashboard ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1 |
                V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_delete_dashboard(
            organization_id, service_id, click_stack_dashboard_id, request_options=request_options
        ).unwrap()

    def click_stack_delete_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_role_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a custom role. Predefined roles, the team default user role, and roles assigned to
        users cannot be deleted.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_role_id: id parameter
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1 |
                V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_delete_role(
            organization_id, service_id, click_stack_role_id, request_options=request_options
        ).unwrap()

    def click_stack_delete_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_saved_search_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a saved search and any alerts attached to it.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_saved_search_id: Saved search ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1 |
                V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_delete_saved_search(
            organization_id, service_id, click_stack_saved_search_id, request_options=request_options
        ).unwrap()

    def click_stack_delete_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_source_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a source

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_source_id: Source ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1 |
                V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_delete_source(
            organization_id, service_id, click_stack_source_id, request_options=request_options
        ).unwrap()

    def click_stack_delete_webhook(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_webhook_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a webhook. Blocked with a 409 while any alert still references it — reassign or
        remove those alerts first — so deletion never leaves an alert pointing at a missing webhook (which would
        silently drop notifications). Mirrors the internal webhook delete guard.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_webhook_id: Webhook ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1 |
                V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_delete_webhook(
            organization_id, service_id, click_stack_webhook_id, request_options=request_options
        ).unwrap()

    def click_stack_get_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_alert_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific alert by ID

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_alert_id: ClickStack Alert ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1 |
                V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_get_alert(
            organization_id, service_id, click_stack_alert_id, request_options=request_options
        ).unwrap()

    def click_stack_get_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_dashboard_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific dashboard by ID

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_dashboard_id: ClickStack Dashboard ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1 |
                V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_get_dashboard(
            organization_id, service_id, click_stack_dashboard_id, request_options=request_options
        ).unwrap()

    def click_stack_get_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_role_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific role by ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_role_id: id parameter
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1 |
                V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_get_role(
            organization_id, service_id, click_stack_role_id, request_options=request_options
        ).unwrap()

    def click_stack_get_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_saved_search_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific saved search by ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_saved_search_id: Saved search ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1 |
                V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_get_saved_search(
            organization_id, service_id, click_stack_saved_search_id, request_options=request_options
        ).unwrap()

    def click_stack_get_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_source_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific source by ID

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_source_id: Source ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1 |
                V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_get_source(
            organization_id, service_id, click_stack_source_id, request_options=request_options
        ).unwrap()

    def click_stack_list_alerts(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        limit: int | None = 1000,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackAlertsResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves alerts for the authenticated team (paginated). Results are capped at ``limit``
        (default and maximum 1000). When ``totalCount`` exceeds the number of returned items, page with
        ``limit``/``offset`` to retrieve them all.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackAlerts400Error1 |
                V1OrganizationsServicesClickstackAlerts500Error1 | RawError``."""
        return self._with_raw_response.click_stack_list_alerts(
            organization_id, service_id, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def click_stack_list_dashboards(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickstackDashboardsResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a list of all dashboards for the authenticated team

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackDashboards400Error1 |
                V1OrganizationsServicesClickstackDashboards500Error1 | RawError``."""
        return self._with_raw_response.click_stack_list_dashboards(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def click_stack_list_roles(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickstackRolesResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves all roles for the authenticated team, including predefined roles.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackRoles400Error1 |
                V1OrganizationsServicesClickstackRoles500Error1 | RawError``."""
        return self._with_raw_response.click_stack_list_roles(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def click_stack_list_saved_searches(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        limit: int | None = 1000,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSavedSearchesResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves saved searches for the authenticated team (paginated). Results are capped at
        ``limit`` (default and maximum 1000). When ``totalCount`` exceeds the number of returned items, page with
        ``limit``/``offset`` to retrieve them all.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackSavedSearches400Error1 |
                V1OrganizationsServicesClickstackSavedSearches500Error1 | RawError``."""
        return self._with_raw_response.click_stack_list_saved_searches(
            organization_id, service_id, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def click_stack_list_sources(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickstackSourcesResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a list of all sources for the authenticated team

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackSources400Error1 |
                V1OrganizationsServicesClickstackSources500Error1 | RawError``."""
        return self._with_raw_response.click_stack_list_sources(
            organization_id, service_id, request_options=request_options
        ).unwrap()

    def click_stack_list_webhooks(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        limit: int | None = 1000,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackWebhooksResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves webhooks for the authenticated team (paginated). Results are capped at ``limit``
        (default and maximum 1000). When ``totalCount`` exceeds the number of returned items, page with
        ``limit``/``offset`` to retrieve them all.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackWebhooks400Error1 |
                V1OrganizationsServicesClickstackWebhooks500Error1 | RawError``."""
        return self._with_raw_response.click_stack_list_webhooks(
            organization_id, service_id, limit=limit, offset=offset, request_options=request_options
        ).unwrap()

    def click_stack_update_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_alert_id: str,
        *,
        body: ClickStackUpdateAlertRequest | ClickStackUpdateAlertRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing alert

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_alert_id: ClickStack Alert ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1 |
                V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_update_alert(
            organization_id, service_id, click_stack_alert_id, body=body, request_options=request_options
        ).unwrap()

    def click_stack_update_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_dashboard_id: str,
        *,
        body: ClickStackUpdateDashboardRequest | ClickStackUpdateDashboardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing dashboard. **Concurrency:** This endpoint does not support optimistic
        concurrency control. Concurrent PUT requests for the same dashboard may silently overwrite each other, which can
        leave orphan tile-to-container references on layout-shape edits. Clients should serialize edits to a given
        dashboard.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_dashboard_id: ClickStack Dashboard ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1 |
                V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_update_dashboard(
            organization_id, service_id, click_stack_dashboard_id, body=body, request_options=request_options
        ).unwrap()

    def click_stack_update_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_role_id: str,
        *,
        body: ClickStackUpdateRoleRequest | ClickStackUpdateRoleRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates a custom role's permissions, name, and description. Predefined roles cannot be
        modified.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_role_id: id parameter
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1 |
                V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_update_role(
            organization_id, service_id, click_stack_role_id, body=body, request_options=request_options
        ).unwrap()

    def click_stack_update_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_saved_search_id: str,
        *,
        body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing saved search. This is a full replace: send the full object. Every
        optional field (``select``, ``where``, ``whereLanguage``, ``orderBy``, ``tags``, ``filters``) is always written
        and falls back to its default when omitted, so omitting a field resets it rather than preserving the stored
        value.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_saved_search_id: Saved search ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1 |
                V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_update_saved_search(
            organization_id, service_id, click_stack_saved_search_id, body=body, request_options=request_options
        ).unwrap()

    def click_stack_update_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_source_id: str,
        *,
        body: ClickStackSource | ClickStackSourceDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing source. The full source object must be provided; this is a replace, not
        a patch. The request body is a source object without the ``id`` field. If an ``id`` is sent anyway it is
        silently ignored (stripped before validation — never a 400); the path parameter alone identifies the source.
        Granularity fields (``materializedViews[].minGranularity`` and ``metadataMaterializedViews.granularity``) accept
        the same short format the API returns (e.g. ``5m``, ``15s``, ``1h``, ``1d``).

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_source_id: Source ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1 |
                V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_update_source(
            organization_id, service_id, click_stack_source_id, body=body, request_options=request_options
        ).unwrap()

    def click_stack_update_webhook(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_webhook_id: str,
        *,
        body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Replaces an existing webhook. Readable optional fields (``description``, ``body``) are a
        full replace: omitting them clears them. The write-only fields ``headers`` and ``queryParams`` are never
        returned on read, so omitting them preserves the stored values; send an explicit empty object (``{}``) to clear
        them. Exception: if the destination (``url`` or ``service``) changes, omitted ``headers``/ ``queryParams`` are
        cleared rather than preserved so stored secrets are never forwarded to a new destination.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_webhook_id: Webhook ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1 |
                V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1 | RawError``."""
        return self._with_raw_response.click_stack_update_webhook(
            organization_id, service_id, click_stack_webhook_id, body=body, request_options=request_options
        ).unwrap()

    def click_stack_validate_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackDashboardsValidateResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Validates a dashboard body against the same schema and tile rules used by POST
        /api/v2/dashboards. The dashboard is **never persisted**. Use this endpoint at plan time (e.g. from a Terraform
        provider) to check that a dashboard configuration is valid before applying it.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackDashboardsValidate400Error1 |
                V1OrganizationsServicesClickstackDashboardsValidate500Error1 | RawError``."""
        return self._with_raw_response.click_stack_validate_dashboard(
            organization_id, service_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ClickStackWithRawResponse:
        return self._with_raw_response


class AsyncClickStack:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncClickStackWithRawResponse(client, server, auth)

    async def click_stack_create_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateAlertRequest | ClickStackCreateAlertRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackAlertsResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new alert

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackAlerts400Error1 |
                V1OrganizationsServicesClickstackAlerts500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_create_alert(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_stack_create_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackDashboardsResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new dashboard

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackDashboards400Error1 |
                V1OrganizationsServicesClickstackDashboards500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_create_dashboard(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_stack_create_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateRoleRequest | ClickStackCreateRoleRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackRolesResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new custom role for the team.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackRoles400Error1 |
                V1OrganizationsServicesClickstackRoles500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_create_role(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_stack_create_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSavedSearchesResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new saved search.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackSavedSearches400Error1 |
                V1OrganizationsServicesClickstackSavedSearches500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_create_saved_search(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_stack_create_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackSource | ClickStackSourceDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSourcesResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new source. The request body is a source object without the ``id`` field. If an
        ``id`` is sent anyway it is silently ignored (stripped before validation — the request is never rejected because
        of it). Granularity fields (``materializedViews[].minGranularity`` and
        ``metadataMaterializedViews.granularity``) accept the same short format the API returns (e.g. ``5m``, ``15s``,
        ``1h``, ``1d``).

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackSources400Error1 |
                V1OrganizationsServicesClickstackSources500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_create_source(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_stack_create_webhook(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackWebhooksResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new webhook for the authenticated team.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackWebhooks400Error1 |
                V1OrganizationsServicesClickstackWebhooks500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_create_webhook(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_stack_delete_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_alert_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes an alert

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_alert_id: ClickStack Alert ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1 |
                V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_delete_alert(
                organization_id, service_id, click_stack_alert_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_delete_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_dashboard_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a dashboard

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_dashboard_id: ClickStack Dashboard ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1 |
                V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_delete_dashboard(
                organization_id, service_id, click_stack_dashboard_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_delete_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_role_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a custom role. Predefined roles, the team default user role, and roles assigned to
        users cannot be deleted.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_role_id: id parameter
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1 |
                V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_delete_role(
                organization_id, service_id, click_stack_role_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_delete_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_saved_search_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a saved search and any alerts attached to it.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_saved_search_id: Saved search ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1 |
                V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_delete_saved_search(
                organization_id, service_id, click_stack_saved_search_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_delete_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_source_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a source

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_source_id: Source ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1 |
                V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_delete_source(
                organization_id, service_id, click_stack_source_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_delete_webhook(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_webhook_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a webhook. Blocked with a 409 while any alert still references it — reassign or
        remove those alerts first — so deletion never leaves an alert pointing at a missing webhook (which would
        silently drop notifications). Mirrors the internal webhook delete guard.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_webhook_id: Webhook ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1 |
                V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_delete_webhook(
                organization_id, service_id, click_stack_webhook_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_get_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_alert_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific alert by ID

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_alert_id: ClickStack Alert ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1 |
                V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_get_alert(
                organization_id, service_id, click_stack_alert_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_get_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_dashboard_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific dashboard by ID

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_dashboard_id: ClickStack Dashboard ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1 |
                V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_get_dashboard(
                organization_id, service_id, click_stack_dashboard_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_get_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_role_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific role by ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_role_id: id parameter
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1 |
                V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_get_role(
                organization_id, service_id, click_stack_role_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_get_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_saved_search_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific saved search by ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_saved_search_id: Saved search ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1 |
                V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_get_saved_search(
                organization_id, service_id, click_stack_saved_search_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_get_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_source_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific source by ID

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_source_id: Source ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1 |
                V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_get_source(
                organization_id, service_id, click_stack_source_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_list_alerts(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        limit: int | None = 1000,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackAlertsResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves alerts for the authenticated team (paginated). Results are capped at ``limit``
        (default and maximum 1000). When ``totalCount`` exceeds the number of returned items, page with
        ``limit``/``offset`` to retrieve them all.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackAlerts400Error1 |
                V1OrganizationsServicesClickstackAlerts500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_list_alerts(
                organization_id, service_id, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def click_stack_list_dashboards(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickstackDashboardsResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a list of all dashboards for the authenticated team

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackDashboards400Error1 |
                V1OrganizationsServicesClickstackDashboards500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_list_dashboards(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_list_roles(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickstackRolesResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves all roles for the authenticated team, including predefined roles.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackRoles400Error1 |
                V1OrganizationsServicesClickstackRoles500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_list_roles(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_list_saved_searches(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        limit: int | None = 1000,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSavedSearchesResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves saved searches for the authenticated team (paginated). Results are capped at
        ``limit`` (default and maximum 1000). When ``totalCount`` exceeds the number of returned items, page with
        ``limit``/``offset`` to retrieve them all.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackSavedSearches400Error1 |
                V1OrganizationsServicesClickstackSavedSearches500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_list_saved_searches(
                organization_id, service_id, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def click_stack_list_sources(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1OrganizationsServicesClickstackSourcesResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a list of all sources for the authenticated team

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackSources400Error1 |
                V1OrganizationsServicesClickstackSources500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_list_sources(
                organization_id, service_id, request_options=request_options
            )
        ).unwrap()

    async def click_stack_list_webhooks(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        limit: int | None = 1000,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackWebhooksResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves webhooks for the authenticated team (paginated). Results are capped at ``limit``
        (default and maximum 1000). When ``totalCount`` exceeds the number of returned items, page with
        ``limit``/``offset`` to retrieve them all.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is ``V1OrganizationsServicesClickstackWebhooks400Error1 |
                V1OrganizationsServicesClickstackWebhooks500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_list_webhooks(
                organization_id, service_id, limit=limit, offset=offset, request_options=request_options
            )
        ).unwrap()

    async def click_stack_update_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_alert_id: str,
        *,
        body: ClickStackUpdateAlertRequest | ClickStackUpdateAlertRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing alert

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_alert_id: ClickStack Alert ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1 |
                V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_update_alert(
                organization_id, service_id, click_stack_alert_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_stack_update_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_dashboard_id: str,
        *,
        body: ClickStackUpdateDashboardRequest | ClickStackUpdateDashboardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing dashboard. **Concurrency:** This endpoint does not support optimistic
        concurrency control. Concurrent PUT requests for the same dashboard may silently overwrite each other, which can
        leave orphan tile-to-container references on layout-shape edits. Clients should serialize edits to a given
        dashboard.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_dashboard_id: ClickStack Dashboard ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1 |
                V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_update_dashboard(
                organization_id, service_id, click_stack_dashboard_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_stack_update_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_role_id: str,
        *,
        body: ClickStackUpdateRoleRequest | ClickStackUpdateRoleRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates a custom role's permissions, name, and description. Predefined roles cannot be
        modified.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_role_id: id parameter
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1 |
                V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_update_role(
                organization_id, service_id, click_stack_role_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_stack_update_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_saved_search_id: str,
        *,
        body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing saved search. This is a full replace: send the full object. Every
        optional field (``select``, ``where``, ``whereLanguage``, ``orderBy``, ``tags``, ``filters``) is always written
        and falls back to its default when omitted, so omitting a field resets it rather than preserving the stored
        value.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_saved_search_id: Saved search ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1 |
                V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_update_saved_search(
                organization_id, service_id, click_stack_saved_search_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_stack_update_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_source_id: str,
        *,
        body: ClickStackSource | ClickStackSourceDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing source. The full source object must be provided; this is a replace, not
        a patch. The request body is a source object without the ``id`` field. If an ``id`` is sent anyway it is
        silently ignored (stripped before validation — never a 400); the path parameter alone identifies the source.
        Granularity fields (``materializedViews[].minGranularity`` and ``metadataMaterializedViews.granularity``) accept
        the same short format the API returns (e.g. ``5m``, ``15s``, ``1h``, ``1d``).

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_source_id: Source ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1 |
                V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_update_source(
                organization_id, service_id, click_stack_source_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_stack_update_webhook(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_webhook_id: str,
        *,
        body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Replaces an existing webhook. Readable optional fields (``description``, ``body``) are a
        full replace: omitting them clears them. The write-only fields ``headers`` and ``queryParams`` are never
        returned on read, so omitting them preserves the stored values; send an explicit empty object (``{}``) to clear
        them. Exception: if the destination (``url`` or ``service``) changes, omitted ``headers``/ ``queryParams`` are
        cleared rather than preserved so stored secrets are never forwarded to a new destination.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_webhook_id: Webhook ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1 |
                V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_update_webhook(
                organization_id, service_id, click_stack_webhook_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def click_stack_validate_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1OrganizationsServicesClickstackDashboardsValidateResponse:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Validates a dashboard body against the same schema and tile rules used by POST
        /api/v2/dashboards. The dashboard is **never persisted**. Use this endpoint at plan time (e.g. from a Terraform
        provider) to check that a dashboard configuration is valid before applying it.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: The request cannot be processed due to a client error. Please verify your request parameters and
                try again. An internal server error has occurred. If this issue persists, please contact ClickHouse
                Cloud support for assistance. ``error`` is
                ``V1OrganizationsServicesClickstackDashboardsValidate400Error1 |
                V1OrganizationsServicesClickstackDashboardsValidate500Error1 | RawError``."""
        return (
            await self._with_raw_response.click_stack_validate_dashboard(
                organization_id, service_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncClickStackWithRawResponse:
        return self._with_raw_response


class ClickStackWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def click_stack_create_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateAlertRequest | ClickStackCreateAlertRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackAlertsResponse1, ClickStackCreateAlertErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new alert

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackCreateAlertRequest | ClickStackCreateAlertRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackAlertsResponse1],
            error_mapper=click_stack_create_alert_error_mapper,
            request_options=request_options,
        )

    def click_stack_create_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackDashboardsResponse1, ClickStackCreateDashboardErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new dashboard

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackDashboardsResponse1],
            error_mapper=click_stack_create_dashboard_error_mapper,
            request_options=request_options,
        )

    def click_stack_create_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateRoleRequest | ClickStackCreateRoleRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackRolesResponse1, ClickStackCreateRoleErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new custom role for the team.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackCreateRoleRequest | ClickStackCreateRoleRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackRolesResponse1],
            error_mapper=click_stack_create_role_error_mapper,
            request_options=request_options,
        )

    def click_stack_create_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackSavedSearchesResponse1, ClickStackCreateSavedSearchErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new saved search.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSavedSearchesResponse1],
            error_mapper=click_stack_create_saved_search_error_mapper,
            request_options=request_options,
        )

    def click_stack_create_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackSource | ClickStackSourceDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackSourcesResponse1, ClickStackCreateSourceErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new source. The request body is a source object without the ``id`` field. If an
        ``id`` is sent anyway it is silently ignored (stripped before validation — the request is never rejected because
        of it). Granularity fields (``materializedViews[].minGranularity`` and
        ``metadataMaterializedViews.granularity``) accept the same short format the API returns (e.g. ``5m``, ``15s``,
        ``1h``, ``1d``).

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackSource | ClickStackSourceDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSourcesResponse1],
            error_mapper=click_stack_create_source_error_mapper,
            request_options=request_options,
        )

    def click_stack_create_webhook(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackWebhooksResponse1, ClickStackCreateWebhookErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new webhook for the authenticated team.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/webhooks"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackWebhookInput | ClickStackWebhookInputDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackWebhooksResponse1],
            error_mapper=click_stack_create_webhook_error_mapper,
            request_options=request_options,
        )

    def click_stack_delete_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_alert_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2, ClickStackDeleteAlertErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes an alert

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_alert_id: ClickStack Alert ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts/{clickStackAlertId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackAlertId", click_stack_alert_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2],
            error_mapper=click_stack_delete_alert_error_mapper,
            request_options=request_options,
        )

    def click_stack_delete_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_dashboard_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2, ClickStackDeleteDashboardErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a dashboard

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_dashboard_id: ClickStack Dashboard ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards/{clickStackDashboardId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackDashboardId", click_stack_dashboard_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2],
            error_mapper=click_stack_delete_dashboard_error_mapper,
            request_options=request_options,
        )

    def click_stack_delete_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_role_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2, ClickStackDeleteRoleErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a custom role. Predefined roles, the team default user role, and roles assigned to
        users cannot be deleted.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_role_id: id parameter
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles/{clickStackRoleId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackRoleId", click_stack_role_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2],
            error_mapper=click_stack_delete_role_error_mapper,
            request_options=request_options,
        )

    def click_stack_delete_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_saved_search_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2,
        ClickStackDeleteSavedSearchErrorBody,
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a saved search and any alerts attached to it.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_saved_search_id: Saved search ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches/{clickStackSavedSearchId}",
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackSavedSearchId", click_stack_saved_search_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2],
            error_mapper=click_stack_delete_saved_search_error_mapper,
            request_options=request_options,
        )

    def click_stack_delete_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_source_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2, ClickStackDeleteSourceErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a source

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_source_id: Source ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources/{clickStackSourceId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackSourceId", click_stack_source_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2],
            error_mapper=click_stack_delete_source_error_mapper,
            request_options=request_options,
        )

    def click_stack_delete_webhook(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_webhook_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1, ClickStackDeleteWebhookErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a webhook. Blocked with a 409 while any alert still references it — reassign or
        remove those alerts first — so deletion never leaves an alert pointing at a missing webhook (which would
        silently drop notifications). Mirrors the internal webhook delete guard.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_webhook_id: Webhook ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/webhooks/{clickStackWebhookId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackWebhookId", click_stack_webhook_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1],
            error_mapper=click_stack_delete_webhook_error_mapper,
            request_options=request_options,
        )

    def click_stack_get_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_alert_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse, ClickStackGetAlertErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific alert by ID

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_alert_id: ClickStack Alert ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts/{clickStackAlertId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackAlertId", click_stack_alert_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse],
            error_mapper=click_stack_get_alert_error_mapper,
            request_options=request_options,
        )

    def click_stack_get_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_dashboard_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse, ClickStackGetDashboardErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific dashboard by ID

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_dashboard_id: ClickStack Dashboard ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards/{clickStackDashboardId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackDashboardId", click_stack_dashboard_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse],
            error_mapper=click_stack_get_dashboard_error_mapper,
            request_options=request_options,
        )

    def click_stack_get_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_role_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse, ClickStackGetRoleErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific role by ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_role_id: id parameter
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles/{clickStackRoleId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackRoleId", click_stack_role_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse],
            error_mapper=click_stack_get_role_error_mapper,
            request_options=request_options,
        )

    def click_stack_get_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_saved_search_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse, ClickStackGetSavedSearchErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific saved search by ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_saved_search_id: Saved search ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches/{clickStackSavedSearchId}",
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackSavedSearchId", click_stack_saved_search_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse],
            error_mapper=click_stack_get_saved_search_error_mapper,
            request_options=request_options,
        )

    def click_stack_get_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_source_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse, ClickStackGetSourceErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific source by ID

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_source_id: Source ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources/{clickStackSourceId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackSourceId", click_stack_source_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse],
            error_mapper=click_stack_get_source_error_mapper,
            request_options=request_options,
        )

    def click_stack_list_alerts(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        limit: int | None = 1000,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackAlertsResponse, ClickStackListAlertsErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves alerts for the authenticated team (paginated). Results are capped at ``limit``
        (default and maximum 1000). When ``totalCount`` exceeds the number of returned items, page with
        ``limit``/``offset`` to retrieve them all.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackAlertsResponse],
            error_mapper=click_stack_list_alerts_error_mapper,
            request_options=request_options,
        )

    def click_stack_list_dashboards(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickstackDashboardsResponse, ClickStackListDashboardsErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a list of all dashboards for the authenticated team

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackDashboardsResponse],
            error_mapper=click_stack_list_dashboards_error_mapper,
            request_options=request_options,
        )

    def click_stack_list_roles(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickstackRolesResponse, ClickStackListRolesErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves all roles for the authenticated team, including predefined roles.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackRolesResponse],
            error_mapper=click_stack_list_roles_error_mapper,
            request_options=request_options,
        )

    def click_stack_list_saved_searches(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        limit: int | None = 1000,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackSavedSearchesResponse, ClickStackListSavedSearchesErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves saved searches for the authenticated team (paginated). Results are capped at
        ``limit`` (default and maximum 1000). When ``totalCount`` exceeds the number of returned items, page with
        ``limit``/``offset`` to retrieve them all.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSavedSearchesResponse],
            error_mapper=click_stack_list_saved_searches_error_mapper,
            request_options=request_options,
        )

    def click_stack_list_sources(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickstackSourcesResponse, ClickStackListSourcesErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a list of all sources for the authenticated team

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSourcesResponse],
            error_mapper=click_stack_list_sources_error_mapper,
            request_options=request_options,
        )

    def click_stack_list_webhooks(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        limit: int | None = 1000,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackWebhooksResponse, ClickStackListWebhooksErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves webhooks for the authenticated team (paginated). Results are capped at ``limit``
        (default and maximum 1000). When ``totalCount`` exceeds the number of returned items, page with
        ``limit``/``offset`` to retrieve them all.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/webhooks"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackWebhooksResponse],
            error_mapper=click_stack_list_webhooks_error_mapper,
            request_options=request_options,
        )

    def click_stack_update_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_alert_id: str,
        *,
        body: ClickStackUpdateAlertRequest | ClickStackUpdateAlertRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse, ClickStackUpdateAlertErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing alert

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_alert_id: ClickStack Alert ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts/{clickStackAlertId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackAlertId", click_stack_alert_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackUpdateAlertRequest | ClickStackUpdateAlertRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse],
            error_mapper=click_stack_update_alert_error_mapper,
            request_options=request_options,
        )

    def click_stack_update_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_dashboard_id: str,
        *,
        body: ClickStackUpdateDashboardRequest | ClickStackUpdateDashboardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse, ClickStackUpdateDashboardErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing dashboard. **Concurrency:** This endpoint does not support optimistic
        concurrency control. Concurrent PUT requests for the same dashboard may silently overwrite each other, which can
        leave orphan tile-to-container references on layout-shape edits. Clients should serialize edits to a given
        dashboard.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_dashboard_id: ClickStack Dashboard ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards/{clickStackDashboardId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackDashboardId", click_stack_dashboard_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackUpdateDashboardRequest | ClickStackUpdateDashboardRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse],
            error_mapper=click_stack_update_dashboard_error_mapper,
            request_options=request_options,
        )

    def click_stack_update_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_role_id: str,
        *,
        body: ClickStackUpdateRoleRequest | ClickStackUpdateRoleRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse, ClickStackUpdateRoleErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates a custom role's permissions, name, and description. Predefined roles cannot be
        modified.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_role_id: id parameter
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles/{clickStackRoleId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackRoleId", click_stack_role_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackUpdateRoleRequest | ClickStackUpdateRoleRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse],
            error_mapper=click_stack_update_role_error_mapper,
            request_options=request_options,
        )

    def click_stack_update_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_saved_search_id: str,
        *,
        body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse,
        ClickStackUpdateSavedSearchErrorBody,
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing saved search. This is a full replace: send the full object. Every
        optional field (``select``, ``where``, ``whereLanguage``, ``orderBy``, ``tags``, ``filters``) is always written
        and falls back to its default when omitted, so omitting a field resets it rather than preserving the stored
        value.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_saved_search_id: Saved search ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches/{clickStackSavedSearchId}",
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackSavedSearchId", click_stack_saved_search_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse],
            error_mapper=click_stack_update_saved_search_error_mapper,
            request_options=request_options,
        )

    def click_stack_update_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_source_id: str,
        *,
        body: ClickStackSource | ClickStackSourceDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse, ClickStackUpdateSourceErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing source. The full source object must be provided; this is a replace, not
        a patch. The request body is a source object without the ``id`` field. If an ``id`` is sent anyway it is
        silently ignored (stripped before validation — never a 400); the path parameter alone identifies the source.
        Granularity fields (``materializedViews[].minGranularity`` and ``metadataMaterializedViews.granularity``) accept
        the same short format the API returns (e.g. ``5m``, ``15s``, ``1h``, ``1d``).

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_source_id: Source ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources/{clickStackSourceId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackSourceId", click_stack_source_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackSource | ClickStackSourceDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse],
            error_mapper=click_stack_update_source_error_mapper,
            request_options=request_options,
        )

    def click_stack_update_webhook(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_webhook_id: str,
        *,
        body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse, ClickStackUpdateWebhookErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Replaces an existing webhook. Readable optional fields (``description``, ``body``) are a
        full replace: omitting them clears them. The write-only fields ``headers`` and ``queryParams`` are never
        returned on read, so omitting them preserves the stored values; send an explicit empty object (``{}``) to clear
        them. Exception: if the destination (``url`` or ``service``) changes, omitted ``headers``/ ``queryParams`` are
        cleared rather than preserved so stored secrets are never forwarded to a new destination.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_webhook_id: Webhook ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/webhooks/{clickStackWebhookId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackWebhookId", click_stack_webhook_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackWebhookInput | ClickStackWebhookInputDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse],
            error_mapper=click_stack_update_webhook_error_mapper,
            request_options=request_options,
        )

    def click_stack_validate_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackDashboardsValidateResponse, ClickStackValidateDashboardErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Validates a dashboard body against the same schema and tile rules used by POST
        /api/v2/dashboards. The dashboard is **never persisted**. Use this endpoint at plan time (e.g. from a Terraform
        provider) to check that a dashboard configuration is valid before applying it.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards/validate"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackDashboardsValidateResponse],
            error_mapper=click_stack_validate_dashboard_error_mapper,
            request_options=request_options,
        )


class AsyncClickStackWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def click_stack_create_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateAlertRequest | ClickStackCreateAlertRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackAlertsResponse1, ClickStackCreateAlertErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new alert

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackCreateAlertRequest | ClickStackCreateAlertRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackAlertsResponse1],
            error_mapper=click_stack_create_alert_error_mapper,
            request_options=request_options,
        )

    async def click_stack_create_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackDashboardsResponse1, ClickStackCreateDashboardErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new dashboard

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackDashboardsResponse1],
            error_mapper=click_stack_create_dashboard_error_mapper,
            request_options=request_options,
        )

    async def click_stack_create_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateRoleRequest | ClickStackCreateRoleRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackRolesResponse1, ClickStackCreateRoleErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new custom role for the team.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackCreateRoleRequest | ClickStackCreateRoleRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackRolesResponse1],
            error_mapper=click_stack_create_role_error_mapper,
            request_options=request_options,
        )

    async def click_stack_create_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackSavedSearchesResponse1, ClickStackCreateSavedSearchErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new saved search.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSavedSearchesResponse1],
            error_mapper=click_stack_create_saved_search_error_mapper,
            request_options=request_options,
        )

    async def click_stack_create_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackSource | ClickStackSourceDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackSourcesResponse1, ClickStackCreateSourceErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new source. The request body is a source object without the ``id`` field. If an
        ``id`` is sent anyway it is silently ignored (stripped before validation — the request is never rejected because
        of it). Granularity fields (``materializedViews[].minGranularity`` and
        ``metadataMaterializedViews.granularity``) accept the same short format the API returns (e.g. ``5m``, ``15s``,
        ``1h``, ``1d``).

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackSource | ClickStackSourceDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSourcesResponse1],
            error_mapper=click_stack_create_source_error_mapper,
            request_options=request_options,
        )

    async def click_stack_create_webhook(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackWebhooksResponse1, ClickStackCreateWebhookErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Creates a new webhook for the authenticated team.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/webhooks"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackWebhookInput | ClickStackWebhookInputDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackWebhooksResponse1],
            error_mapper=click_stack_create_webhook_error_mapper,
            request_options=request_options,
        )

    async def click_stack_delete_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_alert_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2, ClickStackDeleteAlertErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes an alert

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_alert_id: ClickStack Alert ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts/{clickStackAlertId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackAlertId", click_stack_alert_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2],
            error_mapper=click_stack_delete_alert_error_mapper,
            request_options=request_options,
        )

    async def click_stack_delete_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_dashboard_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2, ClickStackDeleteDashboardErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a dashboard

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_dashboard_id: ClickStack Dashboard ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards/{clickStackDashboardId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackDashboardId", click_stack_dashboard_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2],
            error_mapper=click_stack_delete_dashboard_error_mapper,
            request_options=request_options,
        )

    async def click_stack_delete_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_role_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2, ClickStackDeleteRoleErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a custom role. Predefined roles, the team default user role, and roles assigned to
        users cannot be deleted.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_role_id: id parameter
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles/{clickStackRoleId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackRoleId", click_stack_role_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2],
            error_mapper=click_stack_delete_role_error_mapper,
            request_options=request_options,
        )

    async def click_stack_delete_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_saved_search_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2,
        ClickStackDeleteSavedSearchErrorBody,
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a saved search and any alerts attached to it.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_saved_search_id: Saved search ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches/{clickStackSavedSearchId}",
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackSavedSearchId", click_stack_saved_search_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2],
            error_mapper=click_stack_delete_saved_search_error_mapper,
            request_options=request_options,
        )

    async def click_stack_delete_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_source_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2, ClickStackDeleteSourceErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a source

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_source_id: Source ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources/{clickStackSourceId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackSourceId", click_stack_source_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2],
            error_mapper=click_stack_delete_source_error_mapper,
            request_options=request_options,
        )

    async def click_stack_delete_webhook(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_webhook_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1, ClickStackDeleteWebhookErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Deletes a webhook. Blocked with a 409 while any alert still references it — reassign or
        remove those alerts first — so deletion never leaves an alert pointing at a missing webhook (which would
        silently drop notifications). Mirrors the internal webhook delete guard.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_webhook_id: Webhook ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/webhooks/{clickStackWebhookId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackWebhookId", click_stack_webhook_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1],
            error_mapper=click_stack_delete_webhook_error_mapper,
            request_options=request_options,
        )

    async def click_stack_get_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_alert_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse, ClickStackGetAlertErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific alert by ID

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_alert_id: ClickStack Alert ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts/{clickStackAlertId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackAlertId", click_stack_alert_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse],
            error_mapper=click_stack_get_alert_error_mapper,
            request_options=request_options,
        )

    async def click_stack_get_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_dashboard_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse, ClickStackGetDashboardErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific dashboard by ID

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_dashboard_id: ClickStack Dashboard ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards/{clickStackDashboardId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackDashboardId", click_stack_dashboard_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse],
            error_mapper=click_stack_get_dashboard_error_mapper,
            request_options=request_options,
        )

    async def click_stack_get_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_role_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse, ClickStackGetRoleErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific role by ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_role_id: id parameter
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles/{clickStackRoleId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackRoleId", click_stack_role_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse],
            error_mapper=click_stack_get_role_error_mapper,
            request_options=request_options,
        )

    async def click_stack_get_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_saved_search_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse, ClickStackGetSavedSearchErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific saved search by ID.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_saved_search_id: Saved search ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches/{clickStackSavedSearchId}",
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackSavedSearchId", click_stack_saved_search_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse],
            error_mapper=click_stack_get_saved_search_error_mapper,
            request_options=request_options,
        )

    async def click_stack_get_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_source_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse, ClickStackGetSourceErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a specific source by ID

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_source_id: Source ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources/{clickStackSourceId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackSourceId", click_stack_source_id),
            ],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse],
            error_mapper=click_stack_get_source_error_mapper,
            request_options=request_options,
        )

    async def click_stack_list_alerts(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        limit: int | None = 1000,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackAlertsResponse, ClickStackListAlertsErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves alerts for the authenticated team (paginated). Results are capped at ``limit``
        (default and maximum 1000). When ``totalCount`` exceeds the number of returned items, page with
        ``limit``/``offset`` to retrieve them all.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackAlertsResponse],
            error_mapper=click_stack_list_alerts_error_mapper,
            request_options=request_options,
        )

    async def click_stack_list_dashboards(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickstackDashboardsResponse, ClickStackListDashboardsErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a list of all dashboards for the authenticated team

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackDashboardsResponse],
            error_mapper=click_stack_list_dashboards_error_mapper,
            request_options=request_options,
        )

    async def click_stack_list_roles(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickstackRolesResponse, ClickStackListRolesErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves all roles for the authenticated team, including predefined roles.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackRolesResponse],
            error_mapper=click_stack_list_roles_error_mapper,
            request_options=request_options,
        )

    async def click_stack_list_saved_searches(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        limit: int | None = 1000,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackSavedSearchesResponse, ClickStackListSavedSearchesErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves saved searches for the authenticated team (paginated). Results are capped at
        ``limit`` (default and maximum 1000). When ``totalCount`` exceeds the number of returned items, page with
        ``limit``/``offset`` to retrieve them all.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSavedSearchesResponse],
            error_mapper=click_stack_list_saved_searches_error_mapper,
            request_options=request_options,
        )

    async def click_stack_list_sources(
        self, organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1OrganizationsServicesClickstackSourcesResponse, ClickStackListSourcesErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves a list of all sources for the authenticated team

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSourcesResponse],
            error_mapper=click_stack_list_sources_error_mapper,
            request_options=request_options,
        )

    async def click_stack_list_webhooks(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        limit: int | None = 1000,
        offset: int | None = 0,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackWebhooksResponse, ClickStackListWebhooksErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Retrieves webhooks for the authenticated team (paginated). Results are capped at ``limit``
        (default and maximum 1000). When ``totalCount`` exceeds the number of returned items, page with
        ``limit``/``offset`` to retrieve them all.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            limit: Maximum number of results to return.
            offset: Number of results to skip before returning.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/webhooks"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            query_params=[param[int | None]("limit", limit), param[int | None]("offset", offset)],
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackWebhooksResponse],
            error_mapper=click_stack_list_webhooks_error_mapper,
            request_options=request_options,
        )

    async def click_stack_update_alert(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_alert_id: str,
        *,
        body: ClickStackUpdateAlertRequest | ClickStackUpdateAlertRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse, ClickStackUpdateAlertErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing alert

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_alert_id: ClickStack Alert ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts/{clickStackAlertId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackAlertId", click_stack_alert_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackUpdateAlertRequest | ClickStackUpdateAlertRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse],
            error_mapper=click_stack_update_alert_error_mapper,
            request_options=request_options,
        )

    async def click_stack_update_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_dashboard_id: str,
        *,
        body: ClickStackUpdateDashboardRequest | ClickStackUpdateDashboardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse, ClickStackUpdateDashboardErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing dashboard. **Concurrency:** This endpoint does not support optimistic
        concurrency control. Concurrent PUT requests for the same dashboard may silently overwrite each other, which can
        leave orphan tile-to-container references on layout-shape edits. Clients should serialize edits to a given
        dashboard.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_dashboard_id: ClickStack Dashboard ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards/{clickStackDashboardId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackDashboardId", click_stack_dashboard_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackUpdateDashboardRequest | ClickStackUpdateDashboardRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse],
            error_mapper=click_stack_update_dashboard_error_mapper,
            request_options=request_options,
        )

    async def click_stack_update_role(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_role_id: str,
        *,
        body: ClickStackUpdateRoleRequest | ClickStackUpdateRoleRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse, ClickStackUpdateRoleErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates a custom role's permissions, name, and description. Predefined roles cannot be
        modified.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_role_id: id parameter
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles/{clickStackRoleId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackRoleId", click_stack_role_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackUpdateRoleRequest | ClickStackUpdateRoleRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse],
            error_mapper=click_stack_update_role_error_mapper,
            request_options=request_options,
        )

    async def click_stack_update_saved_search(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_saved_search_id: str,
        *,
        body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse,
        ClickStackUpdateSavedSearchErrorBody,
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing saved search. This is a full replace: send the full object. Every
        optional field (``select``, ``where``, ``whereLanguage``, ``orderBy``, ``tags``, ``filters``) is always written
        and falls back to its default when omitted, so omitting a field resets it rather than preserving the stored
        value.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_saved_search_id: Saved search ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches/{clickStackSavedSearchId}",
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackSavedSearchId", click_stack_saved_search_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse],
            error_mapper=click_stack_update_saved_search_error_mapper,
            request_options=request_options,
        )

    async def click_stack_update_source(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_source_id: str,
        *,
        body: ClickStackSource | ClickStackSourceDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse, ClickStackUpdateSourceErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Updates an existing source. The full source object must be provided; this is a replace, not
        a patch. The request body is a source object without the ``id`` field. If an ``id`` is sent anyway it is
        silently ignored (stripped before validation — never a 400); the path parameter alone identifies the source.
        Granularity fields (``materializedViews[].minGranularity`` and ``metadataMaterializedViews.granularity``) accept
        the same short format the API returns (e.g. ``5m``, ``15s``, ``1h``, ``1d``).

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_source_id: Source ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources/{clickStackSourceId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackSourceId", click_stack_source_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackSource | ClickStackSourceDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse],
            error_mapper=click_stack_update_source_error_mapper,
            request_options=request_options,
        )

    async def click_stack_update_webhook(
        self,
        organization_id: UUID,
        service_id: UUID,
        click_stack_webhook_id: str,
        *,
        body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse, ClickStackUpdateWebhookErrorBody
    ]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Replaces an existing webhook. Readable optional fields (``description``, ``body``) are a
        full replace: omitting them clears them. The write-only fields ``headers`` and ``queryParams`` are never
        returned on read, so omitting them preserves the stored values; send an explicit empty object (``{}``) to clear
        them. Exception: if the destination (``url`` or ``service``) changes, omitted ``headers``/ ``queryParams`` are
        cleared rather than preserved so stored secrets are never forwarded to a new destination.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            click_stack_webhook_id: Webhook ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/webhooks/{clickStackWebhookId}"
            ),
            path_params=[
                param[UUID]("organizationId", organization_id),
                param[UUID]("serviceId", service_id),
                param[str]("clickStackWebhookId", click_stack_webhook_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackWebhookInput | ClickStackWebhookInputDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse],
            error_mapper=click_stack_update_webhook_error_mapper,
            request_options=request_options,
        )

    async def click_stack_validate_dashboard(
        self,
        organization_id: UUID,
        service_id: UUID,
        *,
        body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1OrganizationsServicesClickstackDashboardsValidateResponse, ClickStackValidateDashboardErrorBody]:
        """**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br
        /><br /> ClickStack: Validates a dashboard body against the same schema and tile rules used by POST
        /api/v2/dashboards. The dashboard is **never persisted**. Use this endpoint at plan time (e.g. from a Terraform
        provider) to check that a dashboard configuration is valid before applying it.

        Args:
            organization_id: ID of the organization that owns the service.
            service_id: ID of the ClickStack service.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default(
                "/v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards/validate"
            ),
            path_params=[param[UUID]("organizationId", organization_id), param[UUID]("serviceId", service_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None](body),
            auth_scheme=self._auth.basic_auth,
            decoder=json_decoder[V1OrganizationsServicesClickstackDashboardsValidateResponse],
            error_mapper=click_stack_validate_dashboard_error_mapper,
            request_options=request_options,
        )
