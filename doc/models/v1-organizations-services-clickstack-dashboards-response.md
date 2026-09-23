
# V1 Organizations Services Clickstack Dashboards Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickstackDashboardsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[ClickStackDashboardResponse]`](../../doc/models/click-stack-dashboard-response.md) | Optional | - |
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
from openapispecforclickhousecloud.models.source_metric_type import SourceMetricType
from openapispecforclickhousecloud.models.v_1_organizations_services_clickstack_dashboards_response import V1OrganizationsServicesClickstackDashboardsResponse
from openapispecforclickhousecloud.models.where_language_10 import WhereLanguage10
from openapispecforclickhousecloud.models.where_language_4 import WhereLanguage4

v_1_organizations_services_clickstack_dashboards_response = V1OrganizationsServicesClickstackDashboardsResponse(
    status=200,
    request_id='0000087a-0000-0000-0000-000000000000',
    result=[
        ClickStackDashboardResponse(
            id='id6',
            name='name6',
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
                'tags1'
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
                )
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackDashboardResponse(
            id='id6',
            name='name6',
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
                'tags1'
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
                )
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackDashboardResponse(
            id='id6',
            name='name6',
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
                'tags1'
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
                )
            ],
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

