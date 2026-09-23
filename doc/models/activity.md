
# Activity

*This model accepts additional fields of type Any.*

## Structure

`Activity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Unique activity ID. |
| `created_at` | `datetime` | Optional | Timestamp of the activity. ISO-8601. |
| `mtype` | [`Type12`](../../doc/models/type-12.md) | Optional | Type of the activity. |
| `actor_type` | [`ActorType`](../../doc/models/actor-type.md) | Optional | Type of the actor: 'user', 'support', 'system', 'api'. |
| `actor_id` | `str` | Optional | Unique actor ID. |
| `actor_details` | `str` | Optional | Additional information about the actor. |
| `actor_ip_address` | `str` | Optional | IP address of the actor. Defined for 'user' and 'api' actor types. |
| `organization_id` | `str` | Optional | Scope of the activity: organization ID this activity is related to. |
| `service_id` | `str` | Optional | Scope of the activity: service ID this activity is related to. |
| `user_agent` | `str` | Optional | User agent of the actor |
| `target_key_id` | `str` | Optional | For 'openapi_key_update' activities: the ID of the API key that was updated. |
| `key_update_type` | [`KeyUpdateType`](../../doc/models/key-update-type.md) | Optional | For 'openapi_key_update' activities: the type of update that was performed. |
| `target_role_ids` | `List[str]` | Optional | For role and actor-role activities: IDs of the affected roles. |
| `target_role_names` | `List[str]` | Optional | For role and actor-role activities: names of the affected roles, when recorded. |
| `target_actor_ids` | `List[str]` | Optional | For 'organization_member_update_roles' and 'organization_member_remove_roles' activities: IDs of the affected actors (e.g. 'user/<id>'). |
| `target_resource_ids` | `List[str]` | Optional | For 'role_resources_delete' activities: IDs of the deleted resources the roles referenced. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.activity import Activity
from openapispecforclickhousecloud.models.actor_type import ActorType
from openapispecforclickhousecloud.models.type_12 import Type12

activity = Activity(
    id='id8',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    mtype=Type12.UDF_DETACH,
    actor_type=ActorType.SYSTEM,
    actor_id='actorId8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

