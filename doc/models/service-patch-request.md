
# Service Patch Request

*This model accepts additional fields of type Any.*

## Structure

`ServicePatchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the service. Alphanumerical string with whitespaces up to 50 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `ip_access_list` | [`IpAccessListPatch`](../../doc/models/ip-access-list-patch.md) | Optional | - |
| `private_endpoint_ids` | [`InstancePrivateEndpointsPatch`](../../doc/models/instance-private-endpoints-patch.md) | Optional | - |
| `release_channel` | [`ReleaseChannel`](../../doc/models/release-channel.md) | Optional | Select fast if you want to get new ClickHouse releases as soon as they are available. You'll get new features faster, but with a higher risk of bugs. Select slow if you would like to defer releases to give yourself more time to test. This feature is only available for production services. default is the regular release channel. |
| `endpoints` | [`List[ServiceEndpointChange]`](../../doc/models/service-endpoint-change.md) | Optional | List of service endpoints to change |
| `transparent_data_encryption_key_id` | `str` | Optional | The id of the key to rotate |
| `tags` | [`InstanceTagsPatch`](../../doc/models/instance-tags-patch.md) | Optional | - |
| `enable_core_dumps` | `bool` | Optional | If true, the underlying infra is enabled for collecting core dumps. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.instance_private_endpoints_patch import InstancePrivateEndpointsPatch
from openapispecforclickhousecloud.models.ip_access_list_entry import IpAccessListEntry
from openapispecforclickhousecloud.models.ip_access_list_patch import IpAccessListPatch
from openapispecforclickhousecloud.models.protocol_1 import Protocol1
from openapispecforclickhousecloud.models.release_channel import ReleaseChannel
from openapispecforclickhousecloud.models.service_endpoint_change import ServiceEndpointChange
from openapispecforclickhousecloud.models.service_patch_request import ServicePatchRequest

service_patch_request = ServicePatchRequest(
    name='name0',
    ip_access_list=IpAccessListPatch(
        add=[
            IpAccessListEntry(
                source='source8',
                description='description4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            IpAccessListEntry(
                source='source8',
                description='description4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        remove=[
            IpAccessListEntry(
                source='source6',
                description='description0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    private_endpoint_ids=InstancePrivateEndpointsPatch(
        add=[
            'add6'
        ],
        remove=[
            'remove9',
            'remove0',
            'remove1'
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    release_channel=ReleaseChannel.FAST,
    endpoints=[
        ServiceEndpointChange(
            protocol=Protocol1.MYSQL,
            enabled=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

