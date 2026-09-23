
# V1 Organizations Services Backup Configuration Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsServicesBackupConfigurationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`BackupConfiguration`](../../doc/models/backup-configuration.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.backup_configuration import BackupConfiguration
from openapispecforclickhousecloud.models.v_1_organizations_services_backup_configuration_response import V1OrganizationsServicesBackupConfigurationResponse

v_1_organizations_services_backup_configuration_response = V1OrganizationsServicesBackupConfigurationResponse(
    status=200,
    request_id='00000634-0000-0000-0000-000000000000',
    result=BackupConfiguration(
        backup_period_in_hours=97.04,
        backup_retention_period_in_hours=142.88,
        backup_start_time='backupStartTime0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

