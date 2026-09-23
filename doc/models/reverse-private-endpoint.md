
# Reverse Private Endpoint

*This model accepts additional fields of type Any.*

## Structure

`ReversePrivateEndpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Reverse private endpoint description. Maximum length is 255 characters. |
| `mtype` | [`Type1`](../../doc/models/type-1.md) | Optional | Reverse private endpoint type. |
| `vpc_endpoint_service_name` | `str` | Optional | VPC endpoint service name. |
| `vpc_resource_configuration_id` | `str` | Optional | VPC resource configuration ID. Required for VPC_RESOURCE type. |
| `vpc_resource_share_arn` | `str` | Optional | VPC resource share ARN. Required for VPC_RESOURCE type. |
| `msk_cluster_arn` | `str` | Optional | MSK cluster ARN. Required for MSK_MULTI_VPC type. |
| `msk_authentication` | [`MskAuthentication`](../../doc/models/msk-authentication.md) | Optional | MSK cluster authentication type. Required for MSK_MULTI_VPC type. |
| `gcp_service_attachment` | `str` | Optional | Private Preview. GCP PSC service attachment URI. Required for GCP_PSC_SERVICE_ATTACHMENT type. Format: projects/{project}/regions/{region}/serviceAttachments/{name}. |
| `custom_private_dns_mappings` | [`List[CustomPrivateDnsMapping]`](../../doc/models/custom-private-dns-mapping.md) | Optional | Optional private DNS names for Reverse Private Endpoint. Can be used as data source destination address. Must be unique across the ClickHouse service.<br>Generally available for Google Private Service Connect (PSC). For AWS PrivateLink (VPC endpoint service and VPC resource), available in Private Preview; contact ClickHouse support to enable it for your service. Not supported for MSK multi-VPC.<br>Supports exact names and leading wildcard names such as *.example.com |
| `id` | `uuid\|str` | Optional | Reverse private endpoint ID. |
| `service_id` | `uuid\|str` | Optional | ClickHouse service ID reverse private endpoint is associated with. |
| `endpoint_id` | `str` | Optional | Reverse private endpoint endpoint ID. |
| `dns_names` | `List[str]` | Optional | Reverse private endpoint internal DNS names. |
| `private_dns_names` | `List[str]` | Optional | Reverse private endpoint private DNS names. |
| `status` | [`Status`](../../doc/models/status.md) | Optional | Reverse private endpoint status. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.custom_private_dns_mapping import CustomPrivateDnsMapping
from openapispecforclickhousecloud.models.msk_authentication import MskAuthentication
from openapispecforclickhousecloud.models.reverse_private_endpoint import ReversePrivateEndpoint
from openapispecforclickhousecloud.models.status import Status
from openapispecforclickhousecloud.models.type_1 import Type1

reverse_private_endpoint = ReversePrivateEndpoint(
    description='My reverse private endpoint',
    mtype=Type1.VPC_ENDPOINT_SERVICE,
    vpc_endpoint_service_name='com.amazonaws.vpce.us-east-1.vpce-svc-12345678901234567',
    vpc_resource_configuration_id='rcfg-12345678901234567',
    vpc_resource_share_arn='arn:aws:ram:us-east-1:123456789012:resource-share/share-12345678901234567',
    msk_cluster_arn='arn:aws:kafka:us-east-1:123456789012:cluster/my-cluster',
    msk_authentication=MskAuthentication.SASL_IAM,
    gcp_service_attachment='projects/my-project/regions/us-central1/serviceAttachments/my-service',
    custom_private_dns_mappings=[
        CustomPrivateDnsMapping(
            private_dns_name='my-service.example.com',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CustomPrivateDnsMapping(
            private_dns_name='*.example.com',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    id='12345678-1234-1234-1234-123456789012',
    service_id='12345678-1234-1234-1234-123456789012',
    endpoint_id='vpce-12345678901234567',
    dns_names=[
        'vpce-12345678901234567-abcdefg.execute-api.us-east-1.vpce.amazonaws.com'
    ],
    private_dns_names=[
        'vpce-12345678901234567-abcdefg.execute-api.us-east-1.vpce.amazonaws.com'
    ],
    status=Status.READY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

