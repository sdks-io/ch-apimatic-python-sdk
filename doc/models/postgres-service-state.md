
# Postgres Service State

Current state of the service

## Enumeration

`PostgresServiceState`

## Fields

| Name |
|  --- |
| `CREATING` |
| `RESTARTING` |
| `RUNNING` |
| `REPLAYING_WAL` |
| `RESTORING_BACKUP` |
| `FINALIZING_RESTORE` |
| `UNAVAILABLE` |
| `STOPPED` |
| `DELETING` |

## Example

```python
from openapispecforclickhousecloud.models.postgres_service_state import PostgresServiceState

postgres_service_state = PostgresServiceState.STOPPED
```

