
# Backup Configuration

*This model accepts additional fields of type Any.*

## Structure

`BackupConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `backup_period_in_hours` | `float` | Optional | The interval in hours between each backup. |
| `backup_retention_period_in_hours` | `float` | Optional | The minimum duration in hours for which the backups are available. Must be a whole number of days between 24 (1 day) and 1080 (45 days) — i.e. a multiple of 24. |
| `backup_start_time` | `str` | Optional | The time in HH:MM format for the backups to be performed (evaluated in UTC timezone). When defined the backup period resets to every 24 hours. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.backup_configuration import BackupConfiguration

backup_configuration = BackupConfiguration(
    backup_period_in_hours=23.12,
    backup_retention_period_in_hours=187.04,
    backup_start_time='backupStartTime2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

