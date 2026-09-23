
# Api Key Hash Data

*This model accepts additional fields of type Any.*

## Structure

`ApiKeyHashData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key_id_hash` | `str` | Optional | Hash of the key ID. |
| `key_id_suffix` | `str` | Optional | Last 4 digits of the key ID. Algorithm: echo -n "yourpassword" \| sha256sum \| tr -d '-' \| xxd -r -p \| base64 |
| `key_secret_hash` | `str` | Optional | Hash of the key secret. Algorithm: echo -n "yourpassword" \| sha256sum \| tr -d '-' \| xxd -r -p \| base64 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.api_key_hash_data import ApiKeyHashData

api_key_hash_data = ApiKeyHashData(
    key_id_hash='keyIdHash6',
    key_id_suffix='keyIdSuffix8',
    key_secret_hash='keySecretHash0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

