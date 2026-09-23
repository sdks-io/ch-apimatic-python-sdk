
# Click Pipe Big Query Service Account Source

*This model accepts additional fields of type Any.*

## Structure

`ClickPipeBigQueryServiceAccountSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `snapshot_staging_path` | `str` | Required | GCS bucket path for staging snapshot data (e.g., gs://my-bucket/staging/). Data will be automatically cleaned up after initial load. |
| `settings` | [`ClickPipeBigQueryPipeSettings`](../../doc/models/click-pipe-big-query-pipe-settings.md) | Required | - |
| `table_mappings` | [`List[ClickPipeBigQueryPipeTableMapping]`](../../doc/models/click-pipe-big-query-pipe-table-mapping.md) | Required | Table mappings for BigQuery pipe. |
| `authentication` | `str` | Required, Constant | Authenticated with a Google Cloud service account JSON key.<br><br>**Value**: `"SERVICE_ACCOUNT"` |
| `project_id` | `str` | Optional | GCP project ID that owns the BigQuery resources. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.click_pipe_big_query_pipe_settings import ClickPipeBigQueryPipeSettings
from openapispecforclickhousecloud.models.click_pipe_big_query_pipe_table_mapping import ClickPipeBigQueryPipeTableMapping
from openapispecforclickhousecloud.models.click_pipe_big_query_service_account_source import ClickPipeBigQueryServiceAccountSource
from openapispecforclickhousecloud.models.table_engine_4 import TableEngine4

click_pipe_big_query_service_account_source = ClickPipeBigQueryServiceAccountSource(
    snapshot_staging_path='snapshotStagingPath6',
    settings=ClickPipeBigQueryPipeSettings(
        allow_nullable_columns=False,
        initial_load_parallelism=117.34,
        snapshot_num_rows_per_partition=43.84,
        snapshot_number_of_parallel_tables=15.52,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    table_mappings=[
        ClickPipeBigQueryPipeTableMapping(
            source_dataset_name='sourceDatasetName6',
            source_table='sourceTable2',
            target_table='targetTable0',
            excluded_columns=[
                'excludedColumns6'
            ],
            use_custom_sorting_key=False,
            sorting_keys=[
                'sortingKeys5',
                'sortingKeys6',
                'sortingKeys7'
            ],
            table_engine=TableEngine4.REPLACINGMERGETREE,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    project_id='my-gcp-project',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

