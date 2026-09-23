
# V1 Organizations Udfs Attachments Service Id 422 Error Exception

## Structure

`V1OrganizationsUdfsAttachmentsServiceId422ErrorException`

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
except V1OrganizationsUdfsAttachmentsServiceId422ErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

