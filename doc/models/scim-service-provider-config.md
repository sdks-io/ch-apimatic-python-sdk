
# Scim Service Provider Config

*This model accepts additional fields of type Any.*

## Structure

`ScimServiceProviderConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schemas` | `List[str]` | Required | SCIM schema URIs. |
| `documentation_uri` | `str` | Optional | URI of the service documentation. |
| `patch` | [`ScimServiceProviderConfigPatch`](../../doc/models/scim-service-provider-config-patch.md) | Required | - |
| `bulk` | [`ScimServiceProviderConfigBulk`](../../doc/models/scim-service-provider-config-bulk.md) | Required | - |
| `filter` | [`ScimServiceProviderConfigFilter`](../../doc/models/scim-service-provider-config-filter.md) | Required | - |
| `change_password` | [`ScimBooleanFeature`](../../doc/models/scim-boolean-feature.md) | Required | - |
| `sort` | [`ScimBooleanFeature`](../../doc/models/scim-boolean-feature.md) | Required | - |
| `etag` | [`ScimBooleanFeature`](../../doc/models/scim-boolean-feature.md) | Required | - |
| `authentication_schemes` | [`List[ScimAuthenticationScheme]`](../../doc/models/scim-authentication-scheme.md) | Required | Supported authentication schemes. |
| `meta` | [`ScimServiceProviderConfigMeta`](../../doc/models/scim-service-provider-config-meta.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_authentication_scheme import ScimAuthenticationScheme
from openapispecforclickhousecloud.models.scim_boolean_feature import ScimBooleanFeature
from openapispecforclickhousecloud.models.scim_service_provider_config import ScimServiceProviderConfig
from openapispecforclickhousecloud.models.scim_service_provider_config_bulk import ScimServiceProviderConfigBulk
from openapispecforclickhousecloud.models.scim_service_provider_config_filter import ScimServiceProviderConfigFilter
from openapispecforclickhousecloud.models.scim_service_provider_config_meta import ScimServiceProviderConfigMeta
from openapispecforclickhousecloud.models.scim_service_provider_config_patch import ScimServiceProviderConfigPatch

scim_service_provider_config = ScimServiceProviderConfig(
    schemas=[
        'schemas5',
        'schemas6'
    ],
    patch=ScimServiceProviderConfigPatch(
        supported=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    bulk=ScimServiceProviderConfigBulk(
        supported=False,
        max_operations=148,
        max_payload_size=104,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    filter=ScimServiceProviderConfigFilter(
        supported=False,
        max_results=200,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    change_password=ScimBooleanFeature(
        supported=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    sort=ScimBooleanFeature(
        supported=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    etag=ScimBooleanFeature(
        supported=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    authentication_schemes=[
        ScimAuthenticationScheme(
            mtype='type0',
            name='name0',
            description='description0',
            spec_uri='specUri4',
            primary=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    meta=ScimServiceProviderConfigMeta(
        resource_type='resourceType6',
        location='location6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    documentation_uri='documentationUri0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

