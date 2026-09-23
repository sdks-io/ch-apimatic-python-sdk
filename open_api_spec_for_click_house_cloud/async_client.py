from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.api_keys import AsyncApiKeys
from .apis.backup_api import AsyncBackupApi
from .apis.billing import AsyncBilling
from .apis.click_pipes import AsyncClickPipes
from .apis.click_stack import AsyncClickStack
from .apis.organization_api import AsyncOrganizationApi
from .apis.postgres import AsyncPostgres
from .apis.prometheus import AsyncPrometheus
from .apis.query_api_endpoints import AsyncQueryApiEndpoints
from .apis.role_management import AsyncRoleManagement
from .apis.service_api import AsyncServiceApi
from .apis.snapshot_api import AsyncSnapshotApi
from .apis.udf_api import AsyncUdfApi
from .apis.user_management import AsyncUserManagement
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseOpenApiSpecForClickHouseCloudClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    no_auth,
    param,
)


class AsyncOpenApiSpecForClickHouseCloudClient(BaseOpenApiSpecForClickHouseCloudClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        basic_auth: BasicAuthCredentialsOrDict | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "OpenApiSpecForClickHouseCloudClient/1.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            basic_auth=BasicAuthScheme(BasicAuthCredentials.coerce(basic_auth)) if basic_auth is not None else no_auth
        )

    @cached_property
    def api_keys(self) -> AsyncApiKeys:
        return AsyncApiKeys(self._raw_client, self._server, self._auth)

    @cached_property
    def backup_api(self) -> AsyncBackupApi:
        return AsyncBackupApi(self._raw_client, self._server, self._auth)

    @cached_property
    def billing(self) -> AsyncBilling:
        return AsyncBilling(self._raw_client, self._server, self._auth)

    @cached_property
    def click_pipes(self) -> AsyncClickPipes:
        return AsyncClickPipes(self._raw_client, self._server, self._auth)

    @cached_property
    def click_stack(self) -> AsyncClickStack:
        return AsyncClickStack(self._raw_client, self._server, self._auth)

    @cached_property
    def organization_api(self) -> AsyncOrganizationApi:
        return AsyncOrganizationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def postgres(self) -> AsyncPostgres:
        return AsyncPostgres(self._raw_client, self._server, self._auth)

    @cached_property
    def prometheus(self) -> AsyncPrometheus:
        return AsyncPrometheus(self._raw_client, self._server, self._auth)

    @cached_property
    def query_api_endpoints(self) -> AsyncQueryApiEndpoints:
        return AsyncQueryApiEndpoints(self._raw_client, self._server, self._auth)

    @cached_property
    def role_management(self) -> AsyncRoleManagement:
        return AsyncRoleManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def service_api(self) -> AsyncServiceApi:
        return AsyncServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def snapshot_api(self) -> AsyncSnapshotApi:
        return AsyncSnapshotApi(self._raw_client, self._server, self._auth)

    @cached_property
    def udf_api(self) -> AsyncUdfApi:
        return AsyncUdfApi(self._raw_client, self._server, self._auth)

    @cached_property
    def user_management(self) -> AsyncUserManagement:
        return AsyncUserManagement(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncOpenApiSpecForClickHouseCloudClient
