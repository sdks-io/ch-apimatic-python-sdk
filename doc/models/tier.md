
# Tier

DEPRECATED for BASIC, SCALE and ENTERPRISE organization tiers. Use `minReplicaMemoryGb`, `maxReplicaMemoryGb`, and `numReplicas` instead. Tier of the service: 'development', 'production', 'dedicated_high_mem', 'dedicated_high_cpu', 'dedicated_standard', 'dedicated_standard_n2d_standard_4', 'dedicated_standard_n2d_standard_8', 'dedicated_standard_n2d_standard_32', 'dedicated_standard_n2d_standard_128', 'dedicated_standard_n2d_standard_32_16SSD', 'dedicated_standard_n2d_standard_64_24SSD'. Production services scale, Development are fixed size. Azure services don't support Development tier

## Enumeration

`Tier`

## Fields

| Name |
|  --- |
| `DEVELOPMENT` |
| `PRODUCTION` |
| `DEDICATED_HIGH_MEM` |
| `DEDICATED_HIGH_CPU` |
| `DEDICATED_STANDARD` |
| `DEDICATED_STANDARD_N2D_STANDARD_4` |
| `DEDICATED_STANDARD_N2D_STANDARD_8` |
| `DEDICATED_STANDARD_N2D_STANDARD_32` |
| `DEDICATED_STANDARD_N2D_STANDARD_128` |
| `DEDICATED_STANDARD_N2D_STANDARD_32_16SSD` |
| `DEDICATED_STANDARD_N2D_STANDARD_64_24SSD` |

## Example

```python
from openapispecforclickhousecloud.models.tier import Tier

tier = Tier.DEDICATED_STANDARD_N2D_STANDARD_64_24SSD
```

