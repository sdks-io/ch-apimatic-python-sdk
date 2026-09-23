
# V1 Organizations Udfs Attachments Service Id 400 Error 2 Exception

## Structure

`V1OrganizationsUdfsAttachmentsServiceId400Error2Exception`

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
except V1OrganizationsUdfsAttachmentsServiceId400Error2Exception as e:
    print(e)
except ApiException as e:
    print(e)
```

