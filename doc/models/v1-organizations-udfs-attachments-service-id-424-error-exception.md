
# V1 Organizations Udfs Attachments Service Id 424 Error Exception

## Structure

`V1OrganizationsUdfsAttachmentsServiceId424ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `str` | Required | Human-readable error message. |
| `code` | [`Code`](../../doc/models/code.md) | Required | Reason the attachment could not be started. |
| `service_state` | [`ServiceState`](../../doc/models/service-state.md) | Required | Current state of the service. |
| `can_wake` | `bool` | Required | Whether the service can be woken before retrying the attachment. |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |

## Example

```python
try:
    # make the API call
except V1OrganizationsUdfsAttachmentsServiceId424ErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

