
# Click Stack Dashboard Response

*This model accepts additional fields of type Any.*

## Structure

`ClickStackDashboardResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Dashboard ID |
| `name` | `str` | Optional | Dashboard name |
| `tiles` | [`List[ClickStackTileOutput]`](../../doc/models/click-stack-tile-output.md) | Optional | List of tiles/charts in the dashboard |
| `tags` | `List[str]` | Optional | Tags for organizing and filtering dashboards |
| `filters` | [`List[ClickStackFilter]`](../../doc/models/click-stack-filter.md) | Optional | Dropdown filters added to the dashboard. Each one broadcasts its selected value as a condition, acts as a variable which can be referenced in tile queries, or both. |
| `saved_query` | `str` | Optional | Optional default dashboard query restored when loading the dashboard. |
| `saved_query_language` | [`SavedQueryLanguage`](../../doc/models/saved-query-language.md) | Optional | Query language used by savedQuery. |
| `saved_filter_values` | List[[ClickStackSqlSavedFilterValue](../../doc/models/click-stack-sql-saved-filter-value.md) \| [ClickStackVariableSavedFilterValue](../../doc/models/click-stack-variable-saved-filter-value.md)] \| None | Optional | Optional default dashboard filter values restored when loading the dashboard. |
| `containers` | [`List[ClickStackDashboardContainer]`](../../doc/models/click-stack-dashboard-container.md) | Optional | Optional grouping containers. Each tile may join a container via tile.containerId, and a tab inside it via tile.tabId. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.agg_fn_3 import AggFn3
from openapispecforclickhousecloud.models.click_stack_dashboard_response import ClickStackDashboardResponse
from openapispecforclickhousecloud.models.click_stack_filter import ClickStackFilter
from openapispecforclickhousecloud.models.click_stack_line_builder_chart_config import ClickStackLineBuilderChartConfig
from openapispecforclickhousecloud.models.click_stack_select_item import ClickStackSelectItem
from openapispecforclickhousecloud.models.click_stack_tile_output import ClickStackTileOutput
from openapispecforclickhousecloud.models.level import Level
from openapispecforclickhousecloud.models.saved_query_language import SavedQueryLanguage
from openapispecforclickhousecloud.models.source_metric_type import SourceMetricType
from openapispecforclickhousecloud.models.where_language_10 import WhereLanguage10
from openapispecforclickhousecloud.models.where_language_4 import WhereLanguage4

click_stack_dashboard_response = ClickStackDashboardResponse(
    id='65f5e4a3b9e77c001a567890',
    name='Service Overview',
    tiles=[
        ClickStackTileOutput(
            name='name6',
            x=0,
            y=72,
            w=168,
            h=16,
            id='id6',
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
            container_id='containerId2',
            tab_id='tabId2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackTileOutput(
            name='name6',
            x=0,
            y=72,
            w=168,
            h=16,
            id='id6',
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
            container_id='containerId2',
            tab_id='tabId2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    tags=[
        'production',
        'monitoring'
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
        )
    ],
    saved_query='service.name = \'api\'',
    saved_query_language=SavedQueryLanguage.SQL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

