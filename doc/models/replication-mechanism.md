
# Replication Mechanism

MySQL replication mechanism: "GTID" (Global Transaction Identifier) or "FILE_POS" (binary log file and position). Defaults to "GTID" if not specified. MariaDB supports "GTID" only. For "FILE_POS" on MySQL, contact support.

## Enumeration

`ReplicationMechanism`

## Fields

| Name |
|  --- |
| `GTID` |
| `FILE_POS` |

## Example

```python
from openapispecforclickhousecloud.models.replication_mechanism import ReplicationMechanism

replication_mechanism = ReplicationMechanism.GTID
```

