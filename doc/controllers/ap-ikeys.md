# AP Ikeys

```python
ap_ikeys_api = client.ap_ikeys
```

## Class Name

`ApIkeysApi`

## Methods

* [Openapi Key Get List](../../doc/controllers/ap-ikeys.md#openapi-key-get-list)
* [Openapi Key Create](../../doc/controllers/ap-ikeys.md#openapi-key-create)
* [Openapi Key Get](../../doc/controllers/ap-ikeys.md#openapi-key-get)
* [Openapi Key Update](../../doc/controllers/ap-ikeys.md#openapi-key-update)
* [Openapi Key Delete](../../doc/controllers/ap-ikeys.md#openapi-key-delete)


# Openapi Key Get List

Returns a list of keys in the organization, ordered by creation date, oldest first. Results are capped at `limit` (default and maximum 250) per page. Every response carries `limit`, `totalCount` and `nextCursor`; pass `nextCursor` as the `cursor` query parameter to fetch the next page, repeating until it is null.

```python
def openapi_key_get_list(self,
                        organization_id,
                        limit=250,
                        cursor=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `limit` | `int` | Query, Optional | Maximum number of results to return.<br><br>**Default**: `250`<br><br>**Constraints**: `>= 1`, `<= 250` |
| `cursor` | `str` | Query, Optional | Opaque cursor from a previous response's `nextCursor`, marking where to resume the list. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsKeysResponse`](../../doc/models/v1-organizations-keys-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

limit = 250

result = api_keys_api.openapi_key_get_list(
    organization_id,
    limit=limit
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsKeys400ErrorException`](../../doc/models/v1-organizations-keys-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsKeys500ErrorException`](../../doc/models/v1-organizations-keys-500-error-exception.md) |


# Openapi Key Create

Creates new API key.

```python
def openapi_key_create(self,
                      organization_id,
                      body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that will own the key. |
| `body` | [`ApiKeyPostRequest`](../../doc/models/api-key-post-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsKeysResponse1`](../../doc/models/v1-organizations-keys-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = api_keys_api.openapi_key_create(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsKeys400ErrorException`](../../doc/models/v1-organizations-keys-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsKeys500ErrorException`](../../doc/models/v1-organizations-keys-500-error-exception.md) |


# Openapi Key Get

Returns a single key details.

```python
def openapi_key_get(self,
                   organization_id,
                   key_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `key_id` | `uuid\|str` | Template, Required | ID of the requested key. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsKeysResponse2`](../../doc/models/v1-organizations-keys-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

key_id = '00001b3a-0000-0000-0000-000000000000'

result = api_keys_api.openapi_key_get(
    organization_id,
    key_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsKeys400ErrorException`](../../doc/models/v1-organizations-keys-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsKeys500ErrorException`](../../doc/models/v1-organizations-keys-500-error-exception.md) |


# Openapi Key Update

Updates API key properties.

```python
def openapi_key_update(self,
                      organization_id,
                      key_id,
                      body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the key. |
| `key_id` | `uuid\|str` | Template, Required | ID of the key to update. |
| `body` | [`ApiKeyPatchRequest`](../../doc/models/api-key-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsKeysResponse2`](../../doc/models/v1-organizations-keys-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

key_id = '00001b3a-0000-0000-0000-000000000000'

result = api_keys_api.openapi_key_update(
    organization_id,
    key_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsKeys400ErrorException`](../../doc/models/v1-organizations-keys-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsKeys500ErrorException`](../../doc/models/v1-organizations-keys-500-error-exception.md) |


# Openapi Key Delete

Deletes API key. Only a key not used to authenticate the active request can be deleted.

```python
def openapi_key_delete(self,
                      organization_id,
                      key_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the key. |
| `key_id` | `uuid\|str` | Template, Required | ID of the key to delete. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsKeysResponse4`](../../doc/models/v1-organizations-keys-response-4.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

key_id = '00001b3a-0000-0000-0000-000000000000'

result = api_keys_api.openapi_key_delete(
    organization_id,
    key_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsKeys400ErrorException`](../../doc/models/v1-organizations-keys-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsKeys500ErrorException`](../../doc/models/v1-organizations-keys-500-error-exception.md) |

