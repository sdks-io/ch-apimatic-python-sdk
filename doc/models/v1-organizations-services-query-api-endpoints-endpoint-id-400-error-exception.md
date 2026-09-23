
# V1 Organizations Services Query Api Endpoints Endpoint Id 400 Error Exception

## Structure

`V1OrganizationsServicesQueryApiEndpointsEndpointId400ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `str` | Required | Error message. |
| `issues` | [`List[Issue]`](../../doc/models/issue.md) | Optional | Validation issues that caused the request to be rejected. |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |

## Example

```python
try:
    # make the API call
except V1OrganizationsServicesQueryApiEndpointsEndpointId400ErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

