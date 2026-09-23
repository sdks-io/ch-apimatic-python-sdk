from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.api_keys import ApiKeys
from .apis.backup_api import BackupApi
from .apis.billing import Billing
from .apis.click_pipes import ClickPipes
from .apis.click_stack import ClickStack
from .apis.organization_api import OrganizationApi
from .apis.postgres import Postgres
from .apis.prometheus import Prometheus
from .apis.query_api_endpoints import QueryApiEndpoints
from .apis.role_management import RoleManagement
from .apis.service_api import ServiceApi
from .apis.snapshot_api import SnapshotApi
from .apis.udf_api import UdfApi
from .apis.user_management import UserManagement
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseOpenApiSpecForClickHouseCloudClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    HttpClient,
    HttpxClient,
    RawClient,
    no_auth,
    param,
)


class OpenApiSpecForClickHouseCloudClient(BaseOpenApiSpecForClickHouseCloudClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        basic_auth: BasicAuthCredentialsOrDict | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "OpenApiSpecForClickHouseCloudClient/1.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            basic_auth=BasicAuthScheme(BasicAuthCredentials.coerce(basic_auth)) if basic_auth is not None else no_auth
        )

    @cached_property
    def api_keys(self) -> ApiKeys:
        return ApiKeys(self._raw_client, self._server, self._auth)

    @cached_property
    def backup_api(self) -> BackupApi:
        return BackupApi(self._raw_client, self._server, self._auth)

    @cached_property
    def billing(self) -> Billing:
        return Billing(self._raw_client, self._server, self._auth)

    @cached_property
    def click_pipes(self) -> ClickPipes:
        return ClickPipes(self._raw_client, self._server, self._auth)

    @cached_property
    def click_stack(self) -> ClickStack:
        return ClickStack(self._raw_client, self._server, self._auth)

    @cached_property
    def organization_api(self) -> OrganizationApi:
        return OrganizationApi(self._raw_client, self._server, self._auth)

    @cached_property
    def postgres(self) -> Postgres:
        return Postgres(self._raw_client, self._server, self._auth)

    @cached_property
    def prometheus(self) -> Prometheus:
        return Prometheus(self._raw_client, self._server, self._auth)

    @cached_property
    def query_api_endpoints(self) -> QueryApiEndpoints:
        return QueryApiEndpoints(self._raw_client, self._server, self._auth)

    @cached_property
    def role_management(self) -> RoleManagement:
        return RoleManagement(self._raw_client, self._server, self._auth)

    @cached_property
    def service_api(self) -> ServiceApi:
        return ServiceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def snapshot_api(self) -> SnapshotApi:
        return SnapshotApi(self._raw_client, self._server, self._auth)

    @cached_property
    def udf_api(self) -> UdfApi:
        return UdfApi(self._raw_client, self._server, self._auth)

    @cached_property
    def user_management(self) -> UserManagement:
        return UserManagement(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = OpenApiSpecForClickHouseCloudClient
