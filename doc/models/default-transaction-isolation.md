
# Default Transaction Isolation

Sets the default transaction isolation level for new transactions.

Find out more here: [https://postgresqlco.nf/doc/en/param/default_transaction_isolation/](https://postgresqlco.nf/doc/en/param/default_transaction_isolation/)

## Enumeration

`DefaultTransactionIsolation`

## Fields

| Name |
|  --- |
| `ENUM_READ_COMMITTED` |
| `ENUM_REPEATABLE_READ` |
| `SERIALIZABLE` |

## Example

```python
from openapispecforclickhousecloud.models.default_transaction_isolation import DefaultTransactionIsolation

default_transaction_isolation = DefaultTransactionIsolation.ENUM_READ_COMMITTED
```

