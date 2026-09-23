# Role Management

```python
role_management_api = client.role_management
```

## Class Name

`RoleManagementApi`

## Methods

* [Organization Roles Get List](../../doc/controllers/role-management.md#organization-roles-get-list)
* [Organization Role Post](../../doc/controllers/role-management.md#organization-role-post)
* [Organization Role Get](../../doc/controllers/role-management.md#organization-role-get)
* [Organization Role Patch](../../doc/controllers/role-management.md#organization-role-patch)
* [Organization Role Delete](../../doc/controllers/role-management.md#organization-role-delete)


# Organization Roles Get List

Returns all available roles (system + custom) for an organization.

```python
def organization_roles_get_list(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsRolesResponse`](../../doc/models/v1-organizations-roles-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = role_management_api.organization_roles_get_list(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsRoles400ErrorException`](../../doc/models/v1-organizations-roles-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsRoles500ErrorException`](../../doc/models/v1-organizations-roles-500-error-exception.md) |


# Organization Role Post

Creates a new custom role for an organization with specified policies and actors.

```python
def organization_role_post(self,
                          organization_id,
                          body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `body` | [`RoleCreateRequest`](../../doc/models/role-create-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsRolesResponse1`](../../doc/models/v1-organizations-roles-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

body = RoleCreateRequest(
    name='name6',
    actors=[
        'actors9',
        'actors0',
        'actors1'
    ],
    policies=[
        RbacPolicyCreateRequest(
            allow_deny=AllowDeny.ALLOW,
            permissions=[
                'permissions5'
            ],
            resources=[
                'resources3',
                'resources2',
                'resources1'
            ]
        )
    ]
)

result = role_management_api.organization_role_post(
    organization_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsRoles400ErrorException`](../../doc/models/v1-organizations-roles-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsRoles500ErrorException`](../../doc/models/v1-organizations-roles-500-error-exception.md) |


# Organization Role Get

Returns details for a specific role.

```python
def organization_role_get(self,
                         organization_id,
                         role_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `role_id` | `uuid\|str` | Template, Required | ID of the requested role. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsRolesResponse1`](../../doc/models/v1-organizations-roles-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

role_id = '00000178-0000-0000-0000-000000000000'

result = role_management_api.organization_role_get(
    organization_id,
    role_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsRoles400ErrorException`](../../doc/models/v1-organizations-roles-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsRoles500ErrorException`](../../doc/models/v1-organizations-roles-500-error-exception.md) |


# Organization Role Patch

Updates an existing custom role. System roles cannot be updated. All fields are optional - only provided fields will be updated.

```python
def organization_role_patch(self,
                           organization_id,
                           role_id,
                           body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `role_id` | `uuid\|str` | Template, Required | ID of the requested role. |
| `body` | [`RoleUpdateRequest`](../../doc/models/role-update-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsRolesResponse1`](../../doc/models/v1-organizations-roles-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

role_id = '00000178-0000-0000-0000-000000000000'

result = role_management_api.organization_role_patch(
    organization_id,
    role_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsRoles400ErrorException`](../../doc/models/v1-organizations-roles-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsRoles500ErrorException`](../../doc/models/v1-organizations-roles-500-error-exception.md) |


# Organization Role Delete

Deletes an existing custom role. System roles cannot be deleted. This operation will remove the role and all its associated policies.

```python
def organization_role_delete(self,
                            organization_id,
                            role_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `role_id` | `uuid\|str` | Template, Required | ID of the requested role. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsRolesResponse4`](../../doc/models/v1-organizations-roles-response-4.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

role_id = '00000178-0000-0000-0000-000000000000'

result = role_management_api.organization_role_delete(
    organization_id,
    role_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsRoles400ErrorException`](../../doc/models/v1-organizations-roles-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsRoles500ErrorException`](../../doc/models/v1-organizations-roles-500-error-exception.md) |

