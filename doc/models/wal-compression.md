
# Wal Compression

Compress full-page writes in WAL. Reduces I/O at the cost of CPU. Options vary by PostgreSQL version.

Find out more here: [https://postgresqlco.nf/doc/en/param/wal_compression/](https://postgresqlco.nf/doc/en/param/wal_compression/)

## Enumeration

`WalCompression`

## Fields

| Name |
|  --- |
| `OFF` |
| `ON` |
| `LZ4` |
| `ZSTD` |

## Example

```python
from openapispecforclickhousecloud.models.wal_compression import WalCompression

wal_compression = WalCompression.LZ4
```

