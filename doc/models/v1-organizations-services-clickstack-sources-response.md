
# V1 Organizations Services Clickstack Sources Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesClickstackSourcesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | List[[ClickStackLogSource](../../doc/models/click-stack-log-source.md) \| [ClickStackTraceSource](../../doc/models/click-stack-trace-source.md) \| [ClickStackMetricSource](../../doc/models/click-stack-metric-source.md) \| [ClickStackSessionSource](../../doc/models/click-stack-session-source.md) \| [ClickStackPromqlSource](../../doc/models/click-stack-promql-source.md)] \| None | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_filter_settings_column import ClickStackFilterSettingsColumn
from openapispecforclickhousecloud.models.click_stack_log_source import ClickStackLogSource
from openapispecforclickhousecloud.models.click_stack_query_setting import ClickStackQuerySetting
from openapispecforclickhousecloud.models.click_stack_source_filter_settings import ClickStackSourceFilterSettings
from openapispecforclickhousecloud.models.click_stack_source_from import ClickStackSourceFrom
from openapispecforclickhousecloud.models.v_1_organizations_services_clickstack_sources_response import V1OrganizationsServicesClickstackSourcesResponse

v_1_organizations_services_clickstack_sources_response = V1OrganizationsServicesClickstackSourcesResponse(
    status=200,
    request_id='00000f38-0000-0000-0000-000000000000',
    result=[
        ClickStackLogSource(
            name='name4',
            connection='connection2',
            mfrom=ClickStackSourceFrom(
                database_name='databaseName2',
                table_name='tableName2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            default_table_select_expression='defaultTableSelectExpression0',
            timestamp_value_expression='timestampValueExpression4',
            id='id4',
            section='section8',
            disabled=False,
            query_settings=[
                ClickStackQuerySetting(
                    setting='setting6',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ClickStackQuerySetting(
                    setting='setting6',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ClickStackQuerySetting(
                    setting='setting6',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            filter_settings=ClickStackSourceFilterSettings(
                database_name='databaseName4',
                table_name='tableName4',
                columns=[
                    ClickStackFilterSettingsColumn(
                        name='name0',
                        label='label0',
                        value_expression='valueExpression8',
                        allow_all=False,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackLogSource(
            name='name4',
            connection='connection2',
            mfrom=ClickStackSourceFrom(
                database_name='databaseName2',
                table_name='tableName2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            default_table_select_expression='defaultTableSelectExpression0',
            timestamp_value_expression='timestampValueExpression4',
            id='id4',
            section='section8',
            disabled=False,
            query_settings=[
                ClickStackQuerySetting(
                    setting='setting6',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ClickStackQuerySetting(
                    setting='setting6',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ClickStackQuerySetting(
                    setting='setting6',
                    value='value0',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            filter_settings=ClickStackSourceFilterSettings(
                database_name='databaseName4',
                table_name='tableName4',
                columns=[
                    ClickStackFilterSettingsColumn(
                        name='name0',
                        label='label0',
                        value_expression='valueExpression8',
                        allow_all=False,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
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

