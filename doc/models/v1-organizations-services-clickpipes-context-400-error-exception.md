
# V1 Organizations Services Clickpipes Context 400 Error Exception

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickpipesContext400ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `error` | `str` | Optional | Detailed error description. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except V1OrganizationsServicesClickpipesContext400ErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

