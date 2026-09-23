
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](../doc/logging-configuration.md) | The SDK logging configuration for API calls |
| basic_auth_credentials | [`BasicAuthCredentials`](auth/basic-authentication.md) | The credential object for Basic Authentication |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
import logging

from openapispecforclickhousecloud.configuration import Environment
from openapispecforclickhousecloud.http.auth.basic_auth import BasicAuthCredentials
from openapispecforclickhousecloud.logging.configuration.api_logging_configuration import LoggingConfiguration
from openapispecforclickhousecloud.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from openapispecforclickhousecloud.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
from openapispecforclickhousecloud.openapispecforclickhousecloud_client import OpenapispecforclickhousecloudClient

client = OpenapispecforclickhousecloudClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION,
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

## Environment-Based Client Initialization

```python
from openapispecforclickhousecloud.openapispecforclickhousecloud_client import OpenapispecforclickhousecloudClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = OpenapispecforclickhousecloudClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## OpenAPI spec for ClickHouse Cloud Client

The gateway for the SDK. This class acts as a factory for the Apis and also holds the configuration of the SDK.

## Apis

| Name | Description |
|  --- | --- |
| organization | Gets OrganizationApi |
| user_management | Gets UserManagementApi |
| billing | Gets BillingApi |
| role_management | Gets RoleManagementApi |
| service | Gets ServiceApi |
| backup | Gets BackupApi |
| snapshot | Gets SnapshotApi |
| api_keys | Gets ApiKeysApi |
| prometheus | Gets PrometheusApi |
| click_pipes | Gets ClickPipesApi |
| click_stack | Gets ClickStackApi |
| postgres | Gets PostgresApi |
| udf | Gets UdfApi |
| query_api_endpoints | Gets QueryApiEndpointsApi |

