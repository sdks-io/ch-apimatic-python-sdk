# Usermanagement

```python
usermanagement_api = client.usermanagement
```

## Class Name

`UsermanagementApi`

## Methods

* [Member Get List](../../doc/controllers/usermanagement.md#member-get-list)
* [Member Get](../../doc/controllers/usermanagement.md#member-get)
* [Member Update](../../doc/controllers/usermanagement.md#member-update)
* [Member Delete](../../doc/controllers/usermanagement.md#member-delete)
* [Invitation Get List](../../doc/controllers/usermanagement.md#invitation-get-list)
* [Invitation Create](../../doc/controllers/usermanagement.md#invitation-create)
* [Invitation Get](../../doc/controllers/usermanagement.md#invitation-get)
* [Invitation Delete](../../doc/controllers/usermanagement.md#invitation-delete)


# Member Get List

Returns a list of all members in the organization.

```python
def member_get_list(self,
                   organization_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsMembersResponse`](../../doc/models/v1-organizations-members-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = user_management_api.member_get_list(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsMembers400ErrorException`](../../doc/models/v1-organizations-members-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsMembers500ErrorException`](../../doc/models/v1-organizations-members-500-error-exception.md) |


# Member Get

Returns a single organization member details.

```python
def member_get(self,
              organization_id,
              user_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization the member is part of. |
| `user_id` | `uuid\|str` | Template, Required | ID of the requested user. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsMembersResponse1`](../../doc/models/v1-organizations-members-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

user_id = '000013ec-0000-0000-0000-000000000000'

result = user_management_api.member_get(
    organization_id,
    user_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsMembers400ErrorException`](../../doc/models/v1-organizations-members-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsMembers500ErrorException`](../../doc/models/v1-organizations-members-500-error-exception.md) |


# Member Update

Updates organization member role.

```python
def member_update(self,
                 organization_id,
                 user_id,
                 body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization the member is part of. |
| `user_id` | `uuid\|str` | Template, Required | ID of the user to patch |
| `body` | [`MemberPatchRequest`](../../doc/models/member-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsMembersResponse1`](../../doc/models/v1-organizations-members-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

user_id = '000013ec-0000-0000-0000-000000000000'

result = user_management_api.member_update(
    organization_id,
    user_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsMembers400ErrorException`](../../doc/models/v1-organizations-members-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsMembers500ErrorException`](../../doc/models/v1-organizations-members-500-error-exception.md) |


# Member Delete

Removes a user from the organization

```python
def member_delete(self,
                 organization_id,
                 user_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `user_id` | `uuid\|str` | Template, Required | ID of the requested user. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsMembersResponse3`](../../doc/models/v1-organizations-members-response-3.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

user_id = '000013ec-0000-0000-0000-000000000000'

result = user_management_api.member_delete(
    organization_id,
    user_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsMembers400ErrorException`](../../doc/models/v1-organizations-members-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsMembers500ErrorException`](../../doc/models/v1-organizations-members-500-error-exception.md) |


# Invitation Get List

Returns list of all organization invitations.

```python
def invitation_get_list(self,
                       organization_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsInvitationsResponse`](../../doc/models/v1-organizations-invitations-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = user_management_api.invitation_get_list(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsInvitations400ErrorException`](../../doc/models/v1-organizations-invitations-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsInvitations500ErrorException`](../../doc/models/v1-organizations-invitations-500-error-exception.md) |


# Invitation Create

Creates organization invitation.

```python
def invitation_create(self,
                     organization_id,
                     body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization to invite a user to. |
| `body` | [`InvitationPostRequest`](../../doc/models/invitation-post-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsInvitationsResponse1`](../../doc/models/v1-organizations-invitations-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = user_management_api.invitation_create(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsInvitations400ErrorException`](../../doc/models/v1-organizations-invitations-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsInvitations500ErrorException`](../../doc/models/v1-organizations-invitations-500-error-exception.md) |


# Invitation Get

Returns details for a single organization invitation.

```python
def invitation_get(self,
                  organization_id,
                  invitation_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `invitation_id` | `uuid\|str` | Template, Required | ID of the requested organization. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsInvitationsResponse1`](../../doc/models/v1-organizations-invitations-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

invitation_id = '0000032c-0000-0000-0000-000000000000'

result = user_management_api.invitation_get(
    organization_id,
    invitation_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsInvitations400ErrorException`](../../doc/models/v1-organizations-invitations-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsInvitations500ErrorException`](../../doc/models/v1-organizations-invitations-500-error-exception.md) |


# Invitation Delete

Deletes a single organization invitation.

```python
def invitation_delete(self,
                     organization_id,
                     invitation_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that has the invitation. |
| `invitation_id` | `uuid\|str` | Template, Required | ID of the requested organization. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsInvitationsResponse3`](../../doc/models/v1-organizations-invitations-response-3.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

invitation_id = '0000032c-0000-0000-0000-000000000000'

result = user_management_api.invitation_delete(
    organization_id,
    invitation_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsInvitations400ErrorException`](../../doc/models/v1-organizations-invitations-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsInvitations500ErrorException`](../../doc/models/v1-organizations-invitations-500-error-exception.md) |

