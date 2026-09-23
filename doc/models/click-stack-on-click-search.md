
# Click Stack on Click Search

*This model accepts additional fields of type Any.*

## Structure

`ClickStackOnClickSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required, Constant | OnClick variant discriminator. Must be "search" for search link-outs.<br><br>**Value**: `"search"` |
| `target` | [ClickStackOnClickTargetIdVariant](../../doc/models/click-stack-on-click-target-id-variant.md) \| [ClickStackOnClickTargetTemplateVariant](../../doc/models/click-stack-on-click-target-template-variant.md) | Required | - |
| `where_template` | `str` | Optional | Optional WHERE clause template applied to the destination search. |
| `where_language` | [`WhereLanguage5`](../../doc/models/where-language-5.md) | Optional | Language of the rendered whereTemplate. |
| `filters` | [`List[ClickStackOnClickFilterTemplate]`](../../doc/models/click-stack-on-click-filter-template.md) | Optional | Optional dashboard filter templates rendered against the clicked row. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_on_click_filter_template import ClickStackOnClickFilterTemplate
from openapispecforclickhousecloud.models.click_stack_on_click_search import ClickStackOnClickSearch
from openapispecforclickhousecloud.models.click_stack_on_click_target_id_variant import ClickStackOnClickTargetIdVariant
from openapispecforclickhousecloud.models.where_language_5 import WhereLanguage5

click_stack_on_click_search = ClickStackOnClickSearch(
    target=ClickStackOnClickTargetIdVariant(
        id='65f5e4a3b9e77c001a567890',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    where_template='ServiceName = \'{{ServiceName}}\'',
    where_language=WhereLanguage5.SQL,
    filters=[
        ClickStackOnClickFilterTemplate(
            expression='expression2',
            template='template4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackOnClickFilterTemplate(
            expression='expression2',
            template='template4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackOnClickFilterTemplate(
            expression='expression2',
            template='template4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

