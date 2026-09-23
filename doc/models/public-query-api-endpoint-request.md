
# Public Query Api Endpoint Request

*This model accepts additional fields of type Any.*

## Structure

`PublicQueryApiEndpointRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Name of the Query API endpoint.<br><br>**Constraints**: *Minimum Length*: `1`, *Pattern*: `\S` |
| `sql` | `str` | Required | SQL executed by the endpoint.<br><br>**Constraints**: *Maximum Length*: `4194304`, *Pattern*: `\S` |
| `database` | `str` | Required | Database used by the Query API endpoint.<br><br>**Constraints**: *Pattern*: `\S` |
| `parameters` | `Dict[str, str]` | Optional | Default query parameters. |
| `api_key_ids` | `List[uuid\|str]` | Required | API key IDs allowed to call the endpoint.<br><br>**Constraints**: *Minimum Items*: `1` |
| `roles` | `List[str]` | Required | Database roles used by the endpoint.<br><br>**Constraints**: *Minimum Items*: `1`, *Minimum Length*: `1` |
| `allowed_origins` | `List[str]` | Optional | Origins allowed by the endpoint CORS policy. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.public_query_api_endpoint_request import PublicQueryApiEndpointRequest

public_query_api_endpoint_request = PublicQueryApiEndpointRequest(
    name='name0',
    sql='sql8',
    database='database0',
    api_key_ids=[
        '00000098-0000-0000-0000-000000000000'
    ],
    roles=[
        'roles4',
        'roles3',
        'roles2'
    ],
    parameters={
        'key0': 'parameters6',
        'key1': 'parameters7',
        'key2': 'parameters8'
    },
    allowed_origins=[
        'allowedOrigins4',
        'allowedOrigins5'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

