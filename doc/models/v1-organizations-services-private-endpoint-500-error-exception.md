
# V1 Organizations Services Private Endpoint 500 Error Exception

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesPrivateEndpoint500ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Optional | HTTP status code. |
| `error` | `str` | Optional | Detailed error description. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except V1OrganizationsServicesPrivateEndpoint500ErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

