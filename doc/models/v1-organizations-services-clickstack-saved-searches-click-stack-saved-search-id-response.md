
# V1 Organizations Services Clickstack Saved Searches Click Stack Saved Search Id Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`ClickStackSavedSearch`](../../doc/models/click-stack-saved-search.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_saved_search import ClickStackSavedSearch
from openapispecforclickhousecloud.models.v_1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response import V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse
from openapispecforclickhousecloud.models.where_language_12 import WhereLanguage12

v_1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response = V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse(
    status=200,
    request_id='00000764-0000-0000-0000-000000000000',
    result=ClickStackSavedSearch(
        id='id6',
        name='name6',
        source_id='sourceId0',
        select='select6',
        where='where0',
        where_language=WhereLanguage12.LUCENE,
        order_by='orderBy8',
        tags=[
            'tags1'
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

