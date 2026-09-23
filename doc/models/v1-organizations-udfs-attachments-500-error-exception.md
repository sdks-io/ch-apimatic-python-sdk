
# V1 Organizations Udfs Attachments 500 Error Exception

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsUdfsAttachments500ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `str` | Required | Error message. |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except V1OrganizationsUdfsAttachments500ErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

