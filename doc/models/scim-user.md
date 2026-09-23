
# Scim User

*This model accepts additional fields of type Any.*

## Structure

`ScimUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schemas` | `List[str]` | Required | SCIM schemas URIs. Should include "urn:ietf:params:scim:schemas:core:2.0:User". |
| `id` | `str` | Required | Unique identifier for the SCIM resource. Returned by the server. |
| `external_id` | `str` | Optional | A String that is an identifier for the resource as defined by the provisioning client. |
| `user_name` | `str` | Required | Unique identifier for the User, typically used by the user to directly authenticate to the service provider. |
| `name` | [`ScimUserName`](../../doc/models/scim-user-name.md) | Required | - |
| `display_name` | `str` | Optional | The name of the User, suitable for display to end-users. |
| `nick_name` | `str` | Optional | The casual way to address the user in real life. |
| `profile_url` | `str` | Optional | A fully qualified URL pointing to a page representing the User's online profile. |
| `title` | `str` | Optional | The User's title, such as "Vice President". |
| `user_type` | `str` | Optional | Identifies the relationship between the organization and the user. |
| `preferred_language` | `str` | Optional | Indicates the User's preferred written or spoken language (e.g., "en-US"). |
| `locale` | `str` | Optional | Used to indicate the User's default location for localizing items such as currency, date time format, or numerical representations (e.g., "en-US"). |
| `timezone` | `str` | Optional | The User's time zone in the "Olson" time zone database format (e.g., "America/Los_Angeles"). |
| `active` | `bool` | Required | A Boolean value indicating the User's administrative status. |
| `emails` | [`List[ScimUserEmail]`](../../doc/models/scim-user-email.md) | Required | Email addresses for the user. |
| `phone_numbers` | [`List[ScimUserPhoneNumber]`](../../doc/models/scim-user-phone-number.md) | Optional | Phone numbers for the User. |
| `ims` | [`List[ScimUserIm]`](../../doc/models/scim-user-im.md) | Optional | Instant messaging addresses for the User. |
| `photos` | [`List[ScimUserPhoto]`](../../doc/models/scim-user-photo.md) | Optional | URLs of photos of the User. |
| `addresses` | [`List[ScimUserAddress]`](../../doc/models/scim-user-address.md) | Optional | Physical mailing addresses for the User. |
| `groups` | [`List[ScimUserGroup]`](../../doc/models/scim-user-group.md) | Optional | A list of groups to which the user belongs, either through direct membership, through nested groups, or dynamically calculated. |
| `entitlements` | [`List[ScimUserEntitlement]`](../../doc/models/scim-user-entitlement.md) | Optional | A list of entitlements for the user that represent a thing the user has. |
| `roles` | [`List[ScimUserRole]`](../../doc/models/scim-user-role.md) | Optional | A list of roles for the user that collectively represent who the user is, e.g. "Student", "Faculty". No vocabulary or syntax is specified; role value is a string or label representing a collection of entitlements. RFC 7643. |
| `x_509_certificates` | [`List[ScimX509Certificate]`](../../doc/models/scim-x509-certificate.md) | Optional | A list of certificates issued to the User. |
| `meta` | [`ScimUserMeta`](../../doc/models/scim-user-meta.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.scim_user import ScimUser
from openapispecforclickhousecloud.models.scim_user_email import ScimUserEmail
from openapispecforclickhousecloud.models.scim_user_meta import ScimUserMeta
from openapispecforclickhousecloud.models.scim_user_name import ScimUserName

scim_user = ScimUser(
    schemas=[
        'urn:ietf:params:scim:schemas:core:2.0:User'
    ],
    id='samlp|b7a3c2d1-4e5f-6a7b-8c9d-0e1f2a3b4c5d|user@example.com',
    user_name='user@example.com',
    name=ScimUserName(
        formatted='formatted2',
        family_name='familyName8',
        given_name='givenName4',
        middle_name='middleName8',
        honorific_prefix='honorificPrefix4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    active=False,
    emails=[
        ScimUserEmail(
            value='value8',
            mtype='type6',
            primary=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    meta=ScimUserMeta(
        resource_type='resourceType6',
        created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        last_modified=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        location='location6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    external_id='ext-user-001',
    display_name='displayName6',
    nick_name='nickName8',
    profile_url='profileUrl0',
    title='title2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

