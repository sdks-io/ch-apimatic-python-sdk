
# Click Stack Log Source Metadata Materialized Views

*This model accepts additional fields of type Any.*

## Structure

`ClickStackLogSourceMetadataMaterializedViews`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key_rollup_table` | `str` | Optional | ClickHouse table name for the key rollup (field discovery). |
| `kv_rollup_table` | `str` | Optional | ClickHouse table name for the key-value rollup (value autocomplete). |
| `granularity` | `str` | Optional | The time granularity of the rollup tables. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_stack_log_source_metadata_materialized_views import ClickStackLogSourceMetadataMaterializedViews

click_stack_log_source_metadata_materialized_views = ClickStackLogSourceMetadataMaterializedViews(
    key_rollup_table='otel_logs_key_rollup_15m',
    kv_rollup_table='otel_logs_kv_rollup_15m',
    granularity='15m',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

