
# V1 Organizations Services Query Api Endpoints Endpoint Id 409 Error Exception

## Structure

`V1OrganizationsServicesQueryApiEndpointsEndpointId409ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `str` | Required | Human-readable error message. |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |

## Example

```python
try:
    # make the API call
except V1OrganizationsServicesQueryApiEndpointsEndpointId409ErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

