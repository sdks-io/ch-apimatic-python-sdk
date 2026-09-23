
# Public Query Api Endpoint

## Structure

`PublicQueryApiEndpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Required | Unique ID of the Query API endpoint. |
| `name` | `str` | Required | Name of the Query API endpoint. |
| `sql` | `str` | Required | SQL executed by the endpoint.<br><br>**Constraints**: *Maximum Length*: `4194304` |
| `database` | `str` | Required | Database used by the Query API endpoint. |
| `parameters` | `Dict[str, str]` | Required | Query parameters. |
| `api_key_ids` | `List[uuid\|str]` | Required | API key IDs allowed to call the endpoint. |
| `roles` | `List[str]` | Required | Database roles used by the endpoint. |
| `allowed_origins` | `List[str]` | Required | Origins allowed by the endpoint CORS policy. |
| `url` | `str` | Required | Public URL used to execute the endpoint. |
| `owner_type` | [`OwnerType`](../../doc/models/owner-type.md) | Required | Owner type of the Query API endpoint. Endpoints with a user owned query cannot be updated or deleted through this API. |

## Example

```python
from openapispecforclickhousecloud.models.owner_type import OwnerType
from openapispecforclickhousecloud.models.public_query_api_endpoint import PublicQueryApiEndpoint

public_query_api_endpoint = PublicQueryApiEndpoint(
    id='0000025e-0000-0000-0000-000000000000',
    name='name6',
    sql='sql4',
    database='database6',
    parameters={
        'key0': 'parameters2',
        'key1': 'parameters3'
    },
    api_key_ids=[
        '000002d8-0000-0000-0000-000000000000',
        '000002d7-0000-0000-0000-000000000000'
    ],
    roles=[
        'roles0'
    ],
    allowed_origins=[
        'allowedOrigins0'
    ],
    url='https://queries.clickhouse.cloud/run/00000000-0000-0000-0000-000000000000',
    owner_type=OwnerType.USER
)
```

