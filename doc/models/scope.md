
# Scope

Granularity at which the limit is applied. For example, `replicas-per-warehouse` is an organization-wide setting that limits each warehouse individually.

## Enumeration

`Scope`

## Fields

| Name |
|  --- |
| `ORGANIZATION` |
| `WAREHOUSE` |

## Example

```python
from openapispecforclickhousecloud.models.scope import Scope

scope = Scope.ORGANIZATION
```

