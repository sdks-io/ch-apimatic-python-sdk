
# Postgres Configuration

Postgres [runtime configuration](https://www.postgresql.org/docs/current/runtime-config.html) configuration.

## Structure

`PostgresConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_connections` | str \| int \| None | Optional | This is a container for one-of cases. |
| `default_transaction_isolation` | [`DefaultTransactionIsolation`](../../doc/models/default-transaction-isolation.md) | Optional | Sets the default transaction isolation level for new transactions.<br><br>Find out more here: [https://postgresqlco.nf/doc/en/param/default_transaction_isolation/](https://postgresqlco.nf/doc/en/param/default_transaction_isolation/)<br><br>Find out more here: [https://postgresqlco.nf/doc/en/param/default_transaction_isolation/](https://postgresqlco.nf/doc/en/param/default_transaction_isolation/) |
| `ssl_min_protocol_version` | [`SslMinProtocolVersion`](../../doc/models/ssl-min-protocol-version.md) | Optional | Sets the minimum SSL/TLS protocol version allowed for client connections.<br><br>Find out more here: [https://postgresqlco.nf/doc/en/param/ssl_min_protocol_version/](https://postgresqlco.nf/doc/en/param/ssl_min_protocol_version/)<br><br>Find out more here: [https://postgresqlco.nf/doc/en/param/ssl_min_protocol_version/](https://postgresqlco.nf/doc/en/param/ssl_min_protocol_version/) |
| `maintenance_work_mem` | str \| int \| None | Optional | This is a container for one-of cases. |
| `work_mem` | str \| int \| None | Optional | This is a container for one-of cases. |
| `effective_cache_size` | str \| int \| None | Optional | This is a container for one-of cases. |
| `random_page_cost` | str \| float \| None | Optional | This is a container for one-of cases. |
| `effective_io_concurrency` | str \| int \| None | Optional | This is a container for one-of cases. |
| `max_worker_processes` | str \| int \| None | Optional | This is a container for one-of cases. |
| `max_parallel_workers` | str \| int \| None | Optional | This is a container for one-of cases. |
| `max_parallel_workers_per_gather` | str \| int \| None | Optional | This is a container for one-of cases. |
| `max_parallel_maintenance_workers` | str \| int \| None | Optional | This is a container for one-of cases. |
| `statement_timeout` | str \| int \| None | Optional | This is a container for one-of cases. |
| `lock_timeout` | str \| int \| None | Optional | This is a container for one-of cases. |
| `idle_session_timeout` | str \| int \| None | Optional | This is a container for one-of cases. |
| `idle_in_transaction_session_timeout` | str \| int \| None | Optional | This is a container for one-of cases. |
| `transaction_timeout` | str \| int \| None | Optional | This is a container for one-of cases. |
| `wal_sender_timeout` | str \| int \| None | Optional | This is a container for one-of cases. |
| `wal_keep_size` | str \| int \| None | Optional | This is a container for one-of cases. |
| `min_wal_size` | str \| int \| None | Optional | This is a container for one-of cases. |
| `max_wal_size` | str \| int \| None | Optional | This is a container for one-of cases. |
| `max_slot_wal_keep_size` | str \| int \| None | Optional | This is a container for one-of cases. |
| `wal_compression` | [`WalCompression`](../../doc/models/wal-compression.md) | Optional | Compress full-page writes in WAL. Reduces I/O at the cost of CPU. Options vary by PostgreSQL version.<br><br>Find out more here: [https://postgresqlco.nf/doc/en/param/wal_compression/](https://postgresqlco.nf/doc/en/param/wal_compression/)<br><br>Find out more here: [https://postgresqlco.nf/doc/en/param/wal_compression/](https://postgresqlco.nf/doc/en/param/wal_compression/) |
| `autovacuum_max_workers` | str \| int \| None | Optional | This is a container for one-of cases. |
| `autovacuum_naptime` | str \| int \| None | Optional | This is a container for one-of cases. |
| `autovacuum_work_mem` | str \| int \| None | Optional | This is a container for one-of cases. |
| `autovacuum_vacuum_scale_factor` | str \| float \| None | Optional | This is a container for one-of cases. |
| `autovacuum_analyze_scale_factor` | str \| float \| None | Optional | This is a container for one-of cases. |
| `autovacuum_vacuum_insert_scale_factor` | str \| float \| None | Optional | This is a container for one-of cases. |
| `autovacuum_vacuum_cost_limit` | str \| int \| None | Optional | This is a container for one-of cases. |
| `autovacuum_vacuum_cost_delay` | str \| int \| None | Optional | This is a container for one-of cases. |

## Example

```python
from openapispecforclickhousecloud.models.postgres_configuration import PostgresConfiguration

postgres_configuration = PostgresConfiguration(
    max_connections=100
)
```

