
# Msk Authentication

MSK cluster authentication type. Required for MSK_MULTI_VPC type.

## Enumeration

`MskAuthentication`

## Fields

| Name |
|  --- |
| `SASL_IAM` |
| `SASL_SCRAM` |

## Example

```python
from openapispecforclickhousecloud.models.msk_authentication import MskAuthentication

msk_authentication = MskAuthentication.SASL_IAM
```

