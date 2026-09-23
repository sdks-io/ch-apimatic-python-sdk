
# Ssl Min Protocol Version

Sets the minimum SSL/TLS protocol version allowed for client connections.

Find out more here: [https://postgresqlco.nf/doc/en/param/ssl_min_protocol_version/](https://postgresqlco.nf/doc/en/param/ssl_min_protocol_version/)

## Enumeration

`SslMinProtocolVersion`

## Fields

| Name |
|  --- |
| `TLSV1` |
| `ENUM_TLSV11` |
| `ENUM_TLSV12` |
| `ENUM_TLSV13` |

## Example

```python
from openapispecforclickhousecloud.models.ssl_min_protocol_version import SslMinProtocolVersion

ssl_min_protocol_version = SslMinProtocolVersion.ENUM_TLSV12
```

