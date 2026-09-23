
# Scim User Name

*This model accepts additional fields of type Any.*

## Structure

`ScimUserName`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `formatted` | `str` | Optional | The full name, including all middle names, titles, and suffixes. |
| `family_name` | `str` | Optional | The family name of the User. |
| `given_name` | `str` | Optional | The given name of the User. |
| `middle_name` | `str` | Optional | The middle name(s) of the User. |
| `honorific_prefix` | `str` | Optional | The honorific prefix(es) of the User, or title in some cultures. |
| `honorific_suffix` | `str` | Optional | The honorific suffix(es) of the User. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_user_name import ScimUserName

scim_user_name = ScimUserName(
    formatted='formatted4',
    family_name='familyName0',
    given_name='givenName6',
    middle_name='middleName0',
    honorific_prefix='honorificPrefix6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

