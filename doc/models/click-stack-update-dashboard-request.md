
# Click Stack Update Dashboard Request

*This model accepts additional fields of type Any.*

## Structure

`ClickStackUpdateDashboardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Dashboard name. |
| `tiles` | [`List[ClickStackTileInput]`](../../doc/models/click-stack-tile-input.md) | Required | Full list of tiles for the dashboard. Existing tiles are matched by ID; tiles with an ID that does not match an existing tile will be assigned a new generated ID. |
| `tags` | `List[str]` | Optional | Tags for organizing and filtering dashboards. |
| `filters` | [`List[ClickStackFilter]`](../../doc/models/click-stack-filter.md) | Optional | Dropdown filters added to the dashboard. Each one broadcasts its selected value as a condition, acts as a variable which can be referenced in tile queries, or both. |
| `saved_query` | `str` | Optional | Optional default dashboard query to persist on the dashboard. |
| `saved_query_language` | [`SavedQueryLanguage`](../../doc/models/saved-query-language.md) | Optional | Query language used by savedQuery. |
| `saved_filter_values` | List[[ClickStackSqlSavedFilterValue](../../doc/models/click-stack-sql-saved-filter-value.md) \| [ClickStackVariableSavedFilterValue](../../doc/models/click-stack-variable-saved-filter-value.md)] \| None | Optional | Optional default dashboard filter values to persist on the dashboard. |
| `containers` | [`List[ClickStackDashboardContainer]`](../../doc/models/click-stack-dashboard-container.md) | Optional | Optional grouping containers. Each tile may join a container via tile.containerId, and a tab inside it via tile.tabId. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.agg_fn_3 import AggFn3
from openapispecforclickhousecloud.models.click_stack_filter import ClickStackFilter
from openapispecforclickhousecloud.models.click_stack_line_builder_chart_config import ClickStackLineBuilderChartConfig
from openapispecforclickhousecloud.models.click_stack_select_item import ClickStackSelectItem
from openapispecforclickhousecloud.models.click_stack_sql_saved_filter_value import ClickStackSqlSavedFilterValue
from openapispecforclickhousecloud.models.click_stack_tile_input import ClickStackTileInput
from openapispecforclickhousecloud.models.click_stack_update_dashboard_request import ClickStackUpdateDashboardRequest
from openapispecforclickhousecloud.models.level import Level
from openapispecforclickhousecloud.models.saved_query_language import SavedQueryLanguage
from openapispecforclickhousecloud.models.source_metric_type import SourceMetricType
from openapispecforclickhousecloud.models.type_18 import Type18
from openapispecforclickhousecloud.models.where_language_10 import WhereLanguage10
from openapispecforclickhousecloud.models.where_language_4 import WhereLanguage4

click_stack_update_dashboard_request = ClickStackUpdateDashboardRequest(
    name='Updated Dashboard Name',
    tiles=[
        ClickStackTileInput(
            name='Error Rate',
            x=0,
            y=0,
            w=6,
            h=3,
            config=ClickStackLineBuilderChartConfig(
                source_id='sourceId0',
                select=[
                    ClickStackSelectItem(
                        agg_fn=AggFn3.MAX,
                        value_expression='valueExpression0',
                        alias='alias4',
                        level=Level.P50,
                        where='where6',
                        where_language=WhereLanguage4.SQL,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                group_by='groupBy4',
                as_ratio=False,
                align_date_range_to_granularity=False,
                fill_nulls=False,
                fit_y_axis_to_data=False,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            container_id='service-health',
            tab_id='errors',
            id='65f5e4a3b9e77c001a901234',
            as_ratio=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    tags=[
        'production',
        'updated'
    ],
    filters=[
        ClickStackFilter(
            name='name0',
            expression='expression2',
            source_id='sourceId4',
            id='id0',
            source_metric_type=SourceMetricType.HISTOGRAM,
            where='where4',
            where_language=WhereLanguage10.SQL,
            applies_to_source_ids=[
                'appliesToSourceIds1',
                'appliesToSourceIds2',
                'appliesToSourceIds3'
            ],
            is_broadcast_enabled=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackFilter(
            name='name0',
            expression='expression2',
            source_id='sourceId4',
            id='id0',
            source_metric_type=SourceMetricType.HISTOGRAM,
            where='where4',
            where_language=WhereLanguage10.SQL,
            applies_to_source_ids=[
                'appliesToSourceIds1',
                'appliesToSourceIds2',
                'appliesToSourceIds3'
            ],
            is_broadcast_enabled=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackFilter(
            name='name0',
            expression='expression2',
            source_id='sourceId4',
            id='id0',
            source_metric_type=SourceMetricType.HISTOGRAM,
            where='where4',
            where_language=WhereLanguage10.SQL,
            applies_to_source_ids=[
                'appliesToSourceIds1',
                'appliesToSourceIds2',
                'appliesToSourceIds3'
            ],
            is_broadcast_enabled=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    saved_query='service.name = \'api\'',
    saved_query_language=SavedQueryLanguage.SQL,
    saved_filter_values=[
        ClickStackSqlSavedFilterValue(
            condition='condition4',
            mtype=Type18.SQL,
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

