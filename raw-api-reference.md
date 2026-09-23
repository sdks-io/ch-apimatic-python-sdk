# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [OpenApiSpecForClickHouseCloudClient](open_api_spec_for_click_house_cloud/client.py)

## ApiKeys

> Source: [ApiKeys](open_api_spec_for_click_house_cloud/apis/api_keys.py)

<details>
<summary><code>def openapi_key_create(organization_id: UUID, *, body: ApiKeyPostRequest | ApiKeyPostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsKeysResponse1, OpenapiKeyCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates new API key.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.api_keys.with_raw_response.openapi_key_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsKeysResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OpenapiKeyCreateErrorBody
```

**Async**

```python
result = await async_client.api_keys.with_raw_response.openapi_key_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsKeysResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OpenapiKeyCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that will own the key. |
| <code>body</code> | <code>[ApiKeyPostRequest](open_api_spec_for_click_house_cloud/models/api_key_post_request.py) \| [ApiKeyPostRequestDict](open_api_spec_for_click_house_cloud/models/api_key_post_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsKeysResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response1.py), [OpenapiKeyCreateErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsKeysResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OpenapiKeyCreateErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsKeys400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys400_error1.py)</code> |
| 500 | <code>[V1OrganizationsKeys500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def openapi_key_delete(organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsKeysResponse4, OpenapiKeyDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes API key. Only a key not used to authenticate the active request can be deleted.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.api_keys.with_raw_response.openapi_key_delete(organization_id, key_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsKeysResponse4
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OpenapiKeyDeleteErrorBody
```

**Async**

```python
result = await async_client.api_keys.with_raw_response.openapi_key_delete(organization_id, key_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsKeysResponse4
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OpenapiKeyDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the key. |
| <code>key_id</code> | <code>UUID</code> | ID of the key to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsKeysResponse4](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response4.py), [OpenapiKeyDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsKeysResponse4](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response4.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OpenapiKeyDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsKeys400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys400_error1.py)</code> |
| 500 | <code>[V1OrganizationsKeys500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def openapi_key_get(organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsKeysResponse2, OpenapiKeyGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single key details.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.api_keys.with_raw_response.openapi_key_get(organization_id, key_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsKeysResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OpenapiKeyGetErrorBody
```

**Async**

```python
result = await async_client.api_keys.with_raw_response.openapi_key_get(organization_id, key_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsKeysResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OpenapiKeyGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>key_id</code> | <code>UUID</code> | ID of the requested key. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsKeysResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response2.py), [OpenapiKeyGetErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsKeysResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response2.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OpenapiKeyGetErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsKeys400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys400_error1.py)</code> |
| 500 | <code>[V1OrganizationsKeys500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def openapi_key_get_list(organization_id: UUID, *, limit: int | None = 250, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsKeysResponse, OpenapiKeyGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of keys in the organization, ordered by creation date, oldest first. Results are capped at `limit` (default and maximum 250) per page. Every response carries `limit`, `totalCount` and `nextCursor`; pass `nextCursor` as the `cursor` query parameter to fetch the next page, repeating until it is null.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.api_keys.with_raw_response.openapi_key_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsKeysResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OpenapiKeyGetListErrorBody
```

**Async**

```python
result = await async_client.api_keys.with_raw_response.openapi_key_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsKeysResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OpenapiKeyGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>limit</code> | <code>int \| None</code> | Maximum number of results to return.<br>**Default**: <code>250</code> |
| <code>cursor</code> | <code>str \| None</code> | Opaque cursor from a previous response's `nextCursor`, marking where to resume the list.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsKeysResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response.py), [OpenapiKeyGetListErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsKeysResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OpenapiKeyGetListErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsKeys400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys400_error1.py)</code> |
| 500 | <code>[V1OrganizationsKeys500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def openapi_key_update(organization_id: UUID, key_id: UUID, *, body: ApiKeyPatchRequest | ApiKeyPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsKeysResponse2, OpenapiKeyUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates API key properties.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.api_keys.with_raw_response.openapi_key_update(organization_id, key_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsKeysResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OpenapiKeyUpdateErrorBody
```

**Async**

```python
result = await async_client.api_keys.with_raw_response.openapi_key_update(organization_id, key_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsKeysResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OpenapiKeyUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the key. |
| <code>key_id</code> | <code>UUID</code> | ID of the key to update. |
| <code>body</code> | <code>[ApiKeyPatchRequest](open_api_spec_for_click_house_cloud/models/api_key_patch_request.py) \| [ApiKeyPatchRequestDict](open_api_spec_for_click_house_cloud/models/api_key_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsKeysResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response2.py), [OpenapiKeyUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsKeysResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response2.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OpenapiKeyUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsKeys400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys400_error1.py)</code> |
| 500 | <code>[V1OrganizationsKeys500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## BackupApi

> Source: [BackupApi](open_api_spec_for_click_house_cloud/apis/backup_api.py)

<details>
<summary><code>def backup_bucket_create(organization_id: UUID, service_id: UUID, *, body: BackupBucketPostRequest | BackupBucketPostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesBackupBucketResponse, BackupBucketCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Create service backup bucket. Requires ADMIN auth key role.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.backup_api.with_raw_response.backup_bucket_create(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupBucketResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupBucketCreateErrorBody
```

**Async**

```python
result = await async_client.backup_api.with_raw_response.backup_bucket_create(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupBucketResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupBucketCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>body</code> | <code>[BackupBucketPostRequest](open_api_spec_for_click_house_cloud/models/unions/backup_bucket_post_request.py) \| [BackupBucketPostRequestDict](open_api_spec_for_click_house_cloud/models/unions/backup_bucket_post_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesBackupBucketResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response.py), [BackupBucketCreateErrorBody](open_api_spec_for_click_house_cloud/errors/backup_bucket_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesBackupBucketResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[BackupBucketCreateErrorBody](open_api_spec_for_click_house_cloud/errors/backup_bucket_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesBackupBucket400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesBackupBucket500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def backup_bucket_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesBackupBucketResponse3, BackupBucketDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Delete service backup bucket. Requires ADMIN auth key role.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.backup_api.with_raw_response.backup_bucket_delete(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupBucketResponse3
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupBucketDeleteErrorBody
```

**Async**

```python
result = await async_client.backup_api.with_raw_response.backup_bucket_delete(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupBucketResponse3
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupBucketDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesBackupBucketResponse3](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response3.py), [BackupBucketDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/backup_bucket_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesBackupBucketResponse3](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response3.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[BackupBucketDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/backup_bucket_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesBackupBucket400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesBackupBucket500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def backup_bucket_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesBackupBucketResponse, BackupBucketGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns the service backup bucket.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.backup_api.with_raw_response.backup_bucket_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupBucketResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupBucketGetErrorBody
```

**Async**

```python
result = await async_client.backup_api.with_raw_response.backup_bucket_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupBucketResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupBucketGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesBackupBucketResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response.py), [BackupBucketGetErrorBody](open_api_spec_for_click_house_cloud/errors/backup_bucket_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesBackupBucketResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[BackupBucketGetErrorBody](open_api_spec_for_click_house_cloud/errors/backup_bucket_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesBackupBucket400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesBackupBucket500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def backup_bucket_update(organization_id: UUID, service_id: UUID, *, body: BackupBucketPatchRequest | BackupBucketPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesBackupBucketResponse, BackupBucketUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Update service backup bucket. Requires ADMIN auth key role. The secrets of the specified bucket provider are always required

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.backup_api.with_raw_response.backup_bucket_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupBucketResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupBucketUpdateErrorBody
```

**Async**

```python
result = await async_client.backup_api.with_raw_response.backup_bucket_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupBucketResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupBucketUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>body</code> | <code>[BackupBucketPatchRequest](open_api_spec_for_click_house_cloud/models/unions/backup_bucket_patch_request.py) \| [BackupBucketPatchRequestDict](open_api_spec_for_click_house_cloud/models/unions/backup_bucket_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesBackupBucketResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response.py), [BackupBucketUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/backup_bucket_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesBackupBucketResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[BackupBucketUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/backup_bucket_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesBackupBucket400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesBackupBucket500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def backup_configuration_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesBackupConfigurationResponse, BackupConfigurationGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the service backup configuration.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.backup_api.with_raw_response.backup_configuration_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupConfigurationGetErrorBody
```

**Async**

```python
result = await async_client.backup_api.with_raw_response.backup_configuration_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupConfigurationGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesBackupConfigurationResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration_response.py), [BackupConfigurationGetErrorBody](open_api_spec_for_click_house_cloud/errors/backup_configuration_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesBackupConfigurationResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[BackupConfigurationGetErrorBody](open_api_spec_for_click_house_cloud/errors/backup_configuration_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesBackupConfiguration400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesBackupConfiguration500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def backup_configuration_update(organization_id: UUID, service_id: UUID, *, body: BackupConfigurationPatchRequest | BackupConfigurationPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesBackupConfigurationResponse, BackupConfigurationUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates service backup configuration. Requires ADMIN auth key role. Setting the properties with null value, will reset the properties to theirs default values.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.backup_api.with_raw_response.backup_configuration_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupConfigurationUpdateErrorBody
```

**Async**

```python
result = await async_client.backup_api.with_raw_response.backup_configuration_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupConfigurationUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>body</code> | <code>[BackupConfigurationPatchRequest](open_api_spec_for_click_house_cloud/models/backup_configuration_patch_request.py) \| [BackupConfigurationPatchRequestDict](open_api_spec_for_click_house_cloud/models/backup_configuration_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesBackupConfigurationResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration_response.py), [BackupConfigurationUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/backup_configuration_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesBackupConfigurationResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[BackupConfigurationUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/backup_configuration_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesBackupConfiguration400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesBackupConfiguration500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def backup_get(organization_id: UUID, service_id: UUID, backup_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesBackupsBackupIdResponse, BackupGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single backup info.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.backup_api.with_raw_response.backup_get(organization_id, service_id, backup_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupsBackupIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupGetErrorBody
```

**Async**

```python
result = await async_client.backup_api.with_raw_response.backup_get(organization_id, service_id, backup_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupsBackupIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the backup. |
| <code>service_id</code> | <code>UUID</code> | ID of the service the backup was created from. |
| <code>backup_id</code> | <code>UUID</code> | ID of the requested backup. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesBackupsBackupIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups_backup_id_response.py), [BackupGetErrorBody](open_api_spec_for_click_house_cloud/errors/backup_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesBackupsBackupIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups_backup_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[BackupGetErrorBody](open_api_spec_for_click_house_cloud/errors/backup_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesBackupsBackupId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups_backup_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesBackupsBackupId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups_backup_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def backup_get_list(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesBackupsResponse, BackupGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of all backups for the service. The most recent backups comes first in the list.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.backup_api.with_raw_response.backup_get_list(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupGetListErrorBody
```

**Async**

```python
result = await async_client.backup_api.with_raw_response.backup_get_list(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesBackupsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BackupGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the backup. |
| <code>service_id</code> | <code>UUID</code> | ID of the service the backup was created from. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesBackupsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups_response.py), [BackupGetListErrorBody](open_api_spec_for_click_house_cloud/errors/backup_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesBackupsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[BackupGetListErrorBody](open_api_spec_for_click_house_cloud/errors/backup_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesBackups400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesBackups500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Billing

> Source: [Billing](open_api_spec_for_click_house_cloud/apis/billing.py)

<details>
<summary><code>def active_balances_get(organization_id: UUID, *, limit: int | None = 100, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsActiveBalancesResponse, ActiveBalancesGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

DEPRECATED. Use the `/v1/organizations/{organizationId}/creditBalances` endpoint instead. <br /><br /> Returns the active prepaid credit balances for the organization, each with its own balance ID and remaining credits, along with the total remaining credits across all active balances. A balance is active when it has started, has not expired, and has credits remaining. Balances are ordered by expiration date, soonest first, and the returned page is capped at `limit` (default and maximum 100). When `totalCount` exceeds the number of returned balances, page with `limit`/`offset` to retrieve them all. `totalRemainingPrepaidCredits` always covers every active balance, not just the returned page.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.billing.with_raw_response.active_balances_get(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsActiveBalancesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ActiveBalancesGetErrorBody
```

**Async**

```python
result = await async_client.billing.with_raw_response.active_balances_get(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsActiveBalancesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ActiveBalancesGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>limit</code> | <code>int \| None</code> | Maximum number of results to return.<br>**Default**: <code>100</code> |
| <code>offset</code> | <code>int \| None</code> | Number of results to skip before returning.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsActiveBalancesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_active_balances_response.py), [ActiveBalancesGetErrorBody](open_api_spec_for_click_house_cloud/errors/active_balances_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsActiveBalancesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_active_balances_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ActiveBalancesGetErrorBody](open_api_spec_for_click_house_cloud/errors/active_balances_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsActiveBalances400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_active_balances400_error1.py)</code> |
| 500 | <code>[V1OrganizationsActiveBalances500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_active_balances500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def credit_balances_get(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsCreditBalancesResponse, CreditBalancesGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the active credit balances for the organization, each with its own balance ID, type and remaining credits, along with the total remaining credits across all of them. A balance is active when it has started, has not expired, and has credits remaining. Balances are ordered by expiration date, soonest first. The list is always present and is empty when the organization has no active balances.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.billing.with_raw_response.credit_balances_get(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsCreditBalancesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreditBalancesGetErrorBody
```

**Async**

```python
result = await async_client.billing.with_raw_response.credit_balances_get(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsCreditBalancesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreditBalancesGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsCreditBalancesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_credit_balances_response.py), [CreditBalancesGetErrorBody](open_api_spec_for_click_house_cloud/errors/credit_balances_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsCreditBalancesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_credit_balances_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[CreditBalancesGetErrorBody](open_api_spec_for_click_house_cloud/errors/credit_balances_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsCreditBalances400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_credit_balances400_error1.py)</code> |
| 500 | <code>[V1OrganizationsCreditBalances500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_credit_balances500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def usage_cost_get(organization_id: UUID, from_date: Date, to_date: Date, *, filter: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUsageCostResponse, UsageCostGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a grand total and a list of daily, per-entity organization usage cost records for the organization in the queried time period (maximum 31 days). All days in both the request and the response are evaluated based on the UTC timezone.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.billing.with_raw_response.usage_cost_get(organization_id, from_date, to_date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUsageCostResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UsageCostGetErrorBody
```

**Async**

```python
result = await async_client.billing.with_raw_response.usage_cost_get(organization_id, from_date, to_date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUsageCostResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UsageCostGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>from_date</code> | <code>Date</code> | Start date for the report, e.g. 2024-12-19. |
| <code>to_date</code> | <code>Date</code> | End date (inclusive) for the report, e.g. 2024-12-20. This date cannot be more than 30 days after from_date (for a maximum queried period of 31 days). |
| <code>filter</code> | <code>list&#91;str&#93; \| None</code> | Filter criteria to apply when retrieving the usage cost report. Currently, only filtering by resource tags is supported.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUsageCostResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_usage_cost_response.py), [UsageCostGetErrorBody](open_api_spec_for_click_house_cloud/errors/usage_cost_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUsageCostResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_usage_cost_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[UsageCostGetErrorBody](open_api_spec_for_click_house_cloud/errors/usage_cost_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUsageCost400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_usage_cost400_error1.py)</code> |
| 500 | <code>[V1OrganizationsUsageCost500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_usage_cost500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ClickPipes

> Source: [ClickPipes](open_api_spec_for_click_house_cloud/apis/click_pipes.py)

<details>
<summary><code>def click_pipe_cdc_scaling_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesCdcScalingResponse, ClickPipeCdcScalingGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get scaling settings for database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery).

The infrastructure is shared between all database ClickPipes in the service, both for initial load and CDC. For billing purposes, 2 CPU cores and 8 GB of RAM [correspond](https://clickhouse.com/docs/cloud/manage/billing/overview#clickpipes-for-postgres-cdc) to one compute unit.

**Note:** For Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob), see [Get ClickPipe](#tag/ClickPipes/operation/clickPipeGet).

**This endpoint becomes available once at least one database ClickPipe was provisioned.**

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_cdc_scaling_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesCdcScalingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeCdcScalingGetErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_cdc_scaling_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesCdcScalingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeCdcScalingGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the ClickPipe. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesCdcScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling_response.py), [ClickPipeCdcScalingGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_cdc_scaling_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesCdcScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeCdcScalingGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_cdc_scaling_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesCdcScaling400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesCdcScaling500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_cdc_scaling_update(organization_id: UUID, service_id: UUID, *, body: ClickPipesCdcScalingPatchRequest | ClickPipesCdcScalingPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesCdcScalingResponse, ClickPipeCdcScalingUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update scaling settings for database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery).

The infrastructure is shared between all database ClickPipes in the service, both for initial load and CDC. Scaling settings may take a few minutes to fully propagate.

For billing purposes, 2 CPU cores and 8 GB of RAM [correspond](https://clickhouse.com/docs/cloud/manage/billing/overview#clickpipes-for-postgres-cdc) to one compute unit. If your organization tier changes, database ClickPipes will be [rescaled](https://clickhouse.com/docs/cloud/manage/billing/overview#compute) appropriately.

**Note:** For Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob), see [Get ClickPipe](#tag/ClickPipes/operation/clickPipeGet).

**This endpoint becomes available once at least one database ClickPipe was provisioned.**

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_cdc_scaling_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesCdcScalingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeCdcScalingUpdateErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_cdc_scaling_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesCdcScalingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeCdcScalingUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the ClickPipe. |
| <code>body</code> | <code>[ClickPipesCdcScalingPatchRequest](open_api_spec_for_click_house_cloud/models/click_pipes_cdc_scaling_patch_request.py) \| [ClickPipesCdcScalingPatchRequestDict](open_api_spec_for_click_house_cloud/models/click_pipes_cdc_scaling_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesCdcScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling_response.py), [ClickPipeCdcScalingUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_cdc_scaling_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesCdcScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeCdcScalingUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_cdc_scaling_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesCdcScaling400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesCdcScaling500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_create(organization_id: UUID, service_id: UUID, *, body: ClickPipePostRequest | ClickPipePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesResponse1, ClickPipeCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new ClickPipe.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_create(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeCreateErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_create(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service to create the ClickPipe for. |
| <code>body</code> | <code>[ClickPipePostRequest](open_api_spec_for_click_house_cloud/models/click_pipe_post_request.py) \| [ClickPipePostRequestDict](open_api_spec_for_click_house_cloud/models/click_pipe_post_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_response1.py), [ClickPipeCreateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeCreateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipes400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipes500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_delete(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdResponse2, ClickPipeDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete the specified ClickPipe.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_delete(organization_id, service_id, click_pipe_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeDeleteErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_delete(organization_id, service_id, click_pipe_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the ClickPipe. |
| <code>click_pipe_id</code> | <code>UUID</code> | ID of the ClickPipe to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesClickPipeIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_response2.py), [ClickPipeDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesClickPipeIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_response2.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesClickPipeId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesClickPipeId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_get(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdResponse, ClickPipeGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the specified ClickPipe.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_get(organization_id, service_id, click_pipe_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeGetErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_get(organization_id, service_id, click_pipe_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the ClickPipe. |
| <code>click_pipe_id</code> | <code>UUID</code> | ID of the requested ClickPipe. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesClickPipeIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_response.py), [ClickPipeGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesClickPipeIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesClickPipeId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesClickPipeId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_get_list(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesResponse, ClickPipeGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of ClickPipes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_get_list(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeGetListErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_get_list(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the ClickPipe. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_response.py), [ClickPipeGetListErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeGetListErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipes400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipes500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_reverse_private_endpoint_create(organization_id: UUID, service_id: UUID, *, body: CreateReversePrivateEndpoint | CreateReversePrivateEndpointDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1, ClickPipeReversePrivateEndpointCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new reverse private endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_reverse_private_endpoint_create(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeReversePrivateEndpointCreateErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_reverse_private_endpoint_create(
    organization_id, service_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeReversePrivateEndpointCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the Reverse Private Endpoint. |
| <code>body</code> | <code>[CreateReversePrivateEndpoint](open_api_spec_for_click_house_cloud/models/create_reverse_private_endpoint.py) \| [CreateReversePrivateEndpointDict](open_api_spec_for_click_house_cloud/models/create_reverse_private_endpoint.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_response1.py), [ClickPipeReversePrivateEndpointCreateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeReversePrivateEndpointCreateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_reverse_private_endpoint_delete(organization_id: UUID, service_id: UUID, reverse_private_endpoint_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1, ClickPipeReversePrivateEndpointDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete the reverse private endpoint with the specified ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_reverse_private_endpoint_delete(
    organization_id, service_id, reverse_private_endpoint_id
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type
        # V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeReversePrivateEndpointDeleteErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_reverse_private_endpoint_delete(
    organization_id, service_id, reverse_private_endpoint_id
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type
        # V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeReversePrivateEndpointDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the Reverse Private Endpoint. |
| <code>reverse_private_endpoint_id</code> | <code>UUID</code> | ID of the reverse private endpoint to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response1.py), [ClickPipeReversePrivateEndpointDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeReversePrivateEndpointDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_reverse_private_endpoint_get(organization_id: UUID, service_id: UUID, reverse_private_endpoint_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse, ClickPipeReversePrivateEndpointGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the reverse private endpoint with the specified ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_reverse_private_endpoint_get(
    organization_id, service_id, reverse_private_endpoint_id
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type
        # V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeReversePrivateEndpointGetErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_reverse_private_endpoint_get(
    organization_id, service_id, reverse_private_endpoint_id
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type
        # V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeReversePrivateEndpointGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the Reverse Private Endpoint. |
| <code>reverse_private_endpoint_id</code> | <code>UUID</code> | ID of the reverse private endpoint to get. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response.py), [ClickPipeReversePrivateEndpointGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeReversePrivateEndpointGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_reverse_private_endpoint_get_list(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse, ClickPipeReversePrivateEndpointGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of reverse private endpoints for the specified service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_reverse_private_endpoint_get_list(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeReversePrivateEndpointGetListErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_reverse_private_endpoint_get_list(
    organization_id, service_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeReversePrivateEndpointGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the Reverse Private Endpoint. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_response.py), [ClickPipeReversePrivateEndpointGetListErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeReversePrivateEndpointGetListErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_reverse_private_endpoint_update(organization_id: UUID, service_id: UUID, reverse_private_endpoint_id: UUID, *, body: UpdateReversePrivateEndpoint | UpdateReversePrivateEndpointDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse, ClickPipeReversePrivateEndpointUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update mutable fields for an existing reverse private endpoint. customPrivateDnsMappings is a full replacement list. Use an empty array to clear mappings.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_reverse_private_endpoint_update(
    organization_id, service_id, reverse_private_endpoint_id
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type
        # V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeReversePrivateEndpointUpdateErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_reverse_private_endpoint_update(
    organization_id, service_id, reverse_private_endpoint_id
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type
        # V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeReversePrivateEndpointUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the Reverse Private Endpoint. |
| <code>reverse_private_endpoint_id</code> | <code>UUID</code> | ID of the reverse private endpoint to update. |
| <code>body</code> | <code>[UpdateReversePrivateEndpoint](open_api_spec_for_click_house_cloud/models/update_reverse_private_endpoint.py) \| [UpdateReversePrivateEndpointDict](open_api_spec_for_click_house_cloud/models/update_reverse_private_endpoint.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response.py), [ClickPipeReversePrivateEndpointUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeReversePrivateEndpointUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_scaling_update(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, body: ClickPipeScalingPatchRequest | ClickPipeScalingPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdScalingResponse, ClickPipeScalingUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Change scaling settings for the specified ClickPipe. This endpoint supports Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob).

**Note:** For database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery), use the [Update CDC ClickPipes scaling](#tag/ClickPipes/operation/clickPipeCdcScalingUpdate) endpoint instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_scaling_update(organization_id, service_id, click_pipe_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdScalingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeScalingUpdateErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_scaling_update(
    organization_id, service_id, click_pipe_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdScalingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeScalingUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the ClickPipe. |
| <code>click_pipe_id</code> | <code>UUID</code> | ID of the ClickPipe to update scaling settings. |
| <code>body</code> | <code>[ClickPipeScalingPatchRequest](open_api_spec_for_click_house_cloud/models/click_pipe_scaling_patch_request.py) \| [ClickPipeScalingPatchRequestDict](open_api_spec_for_click_house_cloud/models/click_pipe_scaling_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesClickPipeIdScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_scaling_response.py), [ClickPipeScalingUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_scaling_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesClickPipeIdScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_scaling_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeScalingUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_scaling_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesClickPipeIdScaling400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_scaling400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesClickPipeIdScaling500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_scaling500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_schema_discovery(organization_id: UUID, service_id: UUID, *, body: ClickPipeSchemaDiscoveryRequest | ClickPipeSchemaDiscoveryRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesSchemaDiscoveryResponse, ClickPipeSchemaDiscoveryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Infers the schema (field names and ClickHouse data types) of a ClickPipe source without creating a pipe. Supported for Kafka, Kinesis, Pub/Sub, and object storage sources. Object storage inference runs on the destination service, which must be running.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_schema_discovery(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesSchemaDiscoveryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeSchemaDiscoveryErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_schema_discovery(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesSchemaDiscoveryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeSchemaDiscoveryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service to run schema discovery against. |
| <code>body</code> | <code>[ClickPipeSchemaDiscoveryRequest](open_api_spec_for_click_house_cloud/models/click_pipe_schema_discovery_request.py) \| [ClickPipeSchemaDiscoveryRequestDict](open_api_spec_for_click_house_cloud/models/click_pipe_schema_discovery_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesSchemaDiscoveryResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_schema_discovery_response.py), [ClickPipeSchemaDiscoveryErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_schema_discovery_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesSchemaDiscoveryResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_schema_discovery_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeSchemaDiscoveryErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_schema_discovery_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesSchemaDiscovery400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_schema_discovery400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesSchemaDiscovery500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_schema_discovery500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_settings_get(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse, ClickPipeSettingsGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the advanced settings for the specified ClickPipe.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_settings_get(organization_id, service_id, click_pipe_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeSettingsGetErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_settings_get(
    organization_id, service_id, click_pipe_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeSettingsGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the ClickPipe. |
| <code>click_pipe_id</code> | <code>UUID</code> | ID of the ClickPipe to get settings for. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings_response.py), [ClickPipeSettingsGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_settings_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeSettingsGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_settings_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_settings_update(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, body: ClickPipeSettingsPutRequest | ClickPipeSettingsPutRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse, ClickPipeSettingsUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update the advanced settings for the specified ClickPipe. Send key-value pairs where values can be strings, numbers, or booleans.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_settings_update(organization_id, service_id, click_pipe_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeSettingsUpdateErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_settings_update(
    organization_id, service_id, click_pipe_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeSettingsUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the ClickPipe. |
| <code>click_pipe_id</code> | <code>UUID</code> | ID of the ClickPipe to update settings for. |
| <code>body</code> | <code>[ClickPipeSettingsPutRequest](open_api_spec_for_click_house_cloud/models/click_pipe_settings_put_request.py) \| [ClickPipeSettingsPutRequestDict](open_api_spec_for_click_house_cloud/models/click_pipe_settings_put_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings_response.py), [ClickPipeSettingsUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_settings_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeSettingsUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_settings_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_state_update(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, body: ClickPipeStatePatchRequest | ClickPipeStatePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdStateResponse, ClickPipeStateUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Start, stop or resync ClickPipe. Stopping a ClickPipe will stop the ingestion process from any state. Starting is allowed for ClickPipes in the "Stopped" state or with a "Failed" state. Resyncing is only for Postgres and MySQL pipes and can be done from any state.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_state_update(organization_id, service_id, click_pipe_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdStateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeStateUpdateErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_state_update(
    organization_id, service_id, click_pipe_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdStateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeStateUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service that owns the ClickPipe. |
| <code>click_pipe_id</code> | <code>UUID</code> | ID of the ClickPipe to update state. |
| <code>body</code> | <code>[ClickPipeStatePatchRequest](open_api_spec_for_click_house_cloud/models/click_pipe_state_patch_request.py) \| [ClickPipeStatePatchRequestDict](open_api_spec_for_click_house_cloud/models/click_pipe_state_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesClickPipeIdStateResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_state_response.py), [ClickPipeStateUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_state_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesClickPipeIdStateResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_state_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeStateUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_state_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesClickPipeIdState400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_state400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesClickPipeIdState500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_state500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipe_update(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, body: ClickPipePatchRequest | ClickPipePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesClickPipeIdResponse, ClickPipeUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update the specified ClickPipe. Source fields not present in the per-source update schemas are immutable after creation. For Kafka sources, values submitted for immutable fields (type, format, brokers, topics, consumerGroup, offset, schemaRegistry, exactlyOnce) are not applied, except schema registry credentials, which are rejected.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipe_update(organization_id, service_id, click_pipe_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeUpdateErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipe_update(organization_id, service_id, click_pipe_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesClickPipeIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipeUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service to create the ClickPipe for. |
| <code>click_pipe_id</code> | <code>UUID</code> | ID of the requested ClickPipe. |
| <code>body</code> | <code>[ClickPipePatchRequest](open_api_spec_for_click_house_cloud/models/click_pipe_patch_request.py) \| [ClickPipePatchRequestDict](open_api_spec_for_click_house_cloud/models/click_pipe_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesClickPipeIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_response.py), [ClickPipeUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesClickPipeIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipeUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesClickPipeId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesClickPipeId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_pipes_service_context_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickpipesContextResponse, ClickPipesServiceContextGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns service-level ClickPipes capabilities and Private Preview workload identity context, including the GCP service account to grant access to customer source resources.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_pipes.with_raw_response.click_pipes_service_context_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesContextResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipesServiceContextGetErrorBody
```

**Async**

```python
result = await async_client.click_pipes.with_raw_response.click_pipes_service_context_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickpipesContextResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickPipesServiceContextGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service to get ClickPipes context for. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickpipesContextResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_context_response.py), [ClickPipesServiceContextGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipes_service_context_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickpipesContextResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_context_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickPipesServiceContextGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipes_service_context_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickpipesContext400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_context400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickpipesContext500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_context500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ClickStack

> Source: [ClickStack](open_api_spec_for_click_house_cloud/apis/click_stack.py)

<details>
<summary><code>def click_stack_create_alert(organization_id: UUID, service_id: UUID, *, body: ClickStackCreateAlertRequest | ClickStackCreateAlertRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackAlertsResponse1, ClickStackCreateAlertErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Creates a new alert

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_create_alert(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackAlertsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackCreateAlertErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_create_alert(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackAlertsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackCreateAlertErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>body</code> | <code>[ClickStackCreateAlertRequest](open_api_spec_for_click_house_cloud/models/click_stack_create_alert_request.py) \| [ClickStackCreateAlertRequestDict](open_api_spec_for_click_house_cloud/models/click_stack_create_alert_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackAlertsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_response1.py), [ClickStackCreateAlertErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_alert_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackAlertsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackCreateAlertErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_alert_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackAlerts400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackAlerts500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_create_dashboard(organization_id: UUID, service_id: UUID, *, body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackDashboardsResponse1, ClickStackCreateDashboardErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Creates a new dashboard

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_create_dashboard(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackDashboardsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackCreateDashboardErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_create_dashboard(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackDashboardsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackCreateDashboardErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>body</code> | <code>[ClickStackCreateDashboardRequest](open_api_spec_for_click_house_cloud/models/click_stack_create_dashboard_request.py) \| [ClickStackCreateDashboardRequestDict](open_api_spec_for_click_house_cloud/models/click_stack_create_dashboard_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackDashboardsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_response1.py), [ClickStackCreateDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_dashboard_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackDashboardsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackCreateDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_dashboard_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackDashboards400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackDashboards500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_create_role(organization_id: UUID, service_id: UUID, *, body: ClickStackCreateRoleRequest | ClickStackCreateRoleRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackRolesResponse1, ClickStackCreateRoleErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Creates a new custom role for the team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_create_role(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackRolesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackCreateRoleErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_create_role(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackRolesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackCreateRoleErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>body</code> | <code>[ClickStackCreateRoleRequest](open_api_spec_for_click_house_cloud/models/click_stack_create_role_request.py) \| [ClickStackCreateRoleRequestDict](open_api_spec_for_click_house_cloud/models/click_stack_create_role_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackRolesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_response1.py), [ClickStackCreateRoleErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_role_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackRolesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackCreateRoleErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_role_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackRoles400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackRoles500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_create_saved_search(organization_id: UUID, service_id: UUID, *, body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackSavedSearchesResponse1, ClickStackCreateSavedSearchErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Creates a new saved search.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_create_saved_search(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSavedSearchesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackCreateSavedSearchErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_create_saved_search(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSavedSearchesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackCreateSavedSearchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>body</code> | <code>[ClickStackSavedSearchInput](open_api_spec_for_click_house_cloud/models/click_stack_saved_search_input.py) \| [ClickStackSavedSearchInputDict](open_api_spec_for_click_house_cloud/models/click_stack_saved_search_input.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackSavedSearchesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_response1.py), [ClickStackCreateSavedSearchErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_saved_search_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackSavedSearchesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackCreateSavedSearchErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_saved_search_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackSavedSearches400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackSavedSearches500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_create_source(organization_id: UUID, service_id: UUID, *, body: ClickStackSource | ClickStackSourceDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackSourcesResponse1, ClickStackCreateSourceErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Creates a new source.  The request body is a source object without the `id` field. If an `id` is sent anyway it is silently ignored (stripped before validation — the request is never rejected because of it). Granularity fields (`materializedViews[].minGranularity` and `metadataMaterializedViews.granularity`) accept the same short format the API returns (e.g. `5m`, `15s`, `1h`, `1d`).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_create_source(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSourcesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackCreateSourceErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_create_source(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSourcesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackCreateSourceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>body</code> | <code>[ClickStackSource](open_api_spec_for_click_house_cloud/models/unions/click_stack_source.py) \| [ClickStackSourceDict](open_api_spec_for_click_house_cloud/models/unions/click_stack_source.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackSourcesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_response1.py), [ClickStackCreateSourceErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_source_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackSourcesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackCreateSourceErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_source_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackSources400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackSources500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_create_webhook(organization_id: UUID, service_id: UUID, *, body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackWebhooksResponse1, ClickStackCreateWebhookErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Creates a new webhook for the authenticated team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_create_webhook(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackWebhooksResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackCreateWebhookErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_create_webhook(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackWebhooksResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackCreateWebhookErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>body</code> | <code>[ClickStackWebhookInput](open_api_spec_for_click_house_cloud/models/click_stack_webhook_input.py) \| [ClickStackWebhookInputDict](open_api_spec_for_click_house_cloud/models/click_stack_webhook_input.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackWebhooksResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_response1.py), [ClickStackCreateWebhookErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_webhook_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackWebhooksResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackCreateWebhookErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_webhook_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackWebhooks400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackWebhooks500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_delete_alert(organization_id: UUID, service_id: UUID, click_stack_alert_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2, ClickStackDeleteAlertErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Deletes an alert

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_delete_alert(
    organization_id, service_id, click_stack_alert_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackDeleteAlertErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_delete_alert(
    organization_id, service_id, click_stack_alert_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackDeleteAlertErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_alert_id</code> | <code>str</code> | ClickStack Alert ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id_response2.py), [ClickStackDeleteAlertErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_alert_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id_response2.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackDeleteAlertErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_alert_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_delete_dashboard(organization_id: UUID, service_id: UUID, click_stack_dashboard_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2, ClickStackDeleteDashboardErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Deletes a dashboard

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_delete_dashboard(
    organization_id, service_id, click_stack_dashboard_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackDeleteDashboardErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_delete_dashboard(
    organization_id, service_id, click_stack_dashboard_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackDeleteDashboardErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_dashboard_id</code> | <code>str</code> | ClickStack Dashboard ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response2.py), [ClickStackDeleteDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_dashboard_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response2.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackDeleteDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_dashboard_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_delete_role(organization_id: UUID, service_id: UUID, click_stack_role_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2, ClickStackDeleteRoleErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Deletes a custom role. Predefined roles, the team default user role, and roles assigned to users cannot be deleted.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_delete_role(organization_id, service_id, click_stack_role_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackDeleteRoleErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_delete_role(
    organization_id, service_id, click_stack_role_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackDeleteRoleErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_role_id</code> | <code>str</code> | id parameter |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id_response2.py), [ClickStackDeleteRoleErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_role_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id_response2.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackDeleteRoleErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_role_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_delete_saved_search(organization_id: UUID, service_id: UUID, click_stack_saved_search_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2, ClickStackDeleteSavedSearchErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Deletes a saved search and any alerts attached to it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_delete_saved_search(
    organization_id, service_id, click_stack_saved_search_id
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackDeleteSavedSearchErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_delete_saved_search(
    organization_id, service_id, click_stack_saved_search_id
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackDeleteSavedSearchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_saved_search_id</code> | <code>str</code> | Saved search ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response2.py), [ClickStackDeleteSavedSearchErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_saved_search_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response2.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackDeleteSavedSearchErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_saved_search_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_delete_source(organization_id: UUID, service_id: UUID, click_stack_source_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2, ClickStackDeleteSourceErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Deletes a source

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_delete_source(
    organization_id, service_id, click_stack_source_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackDeleteSourceErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_delete_source(
    organization_id, service_id, click_stack_source_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackDeleteSourceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_source_id</code> | <code>str</code> | Source ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id_response2.py), [ClickStackDeleteSourceErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_source_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id_response2.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackDeleteSourceErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_source_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_delete_webhook(organization_id: UUID, service_id: UUID, click_stack_webhook_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1, ClickStackDeleteWebhookErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Deletes a webhook. Blocked with a 409 while any alert still references it — reassign or remove those alerts first — so deletion never leaves an alert pointing at a missing webhook (which would silently drop notifications). Mirrors the internal webhook delete guard.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_delete_webhook(
    organization_id, service_id, click_stack_webhook_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackDeleteWebhookErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_delete_webhook(
    organization_id, service_id, click_stack_webhook_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackDeleteWebhookErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_webhook_id</code> | <code>str</code> | Webhook ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id_response1.py), [ClickStackDeleteWebhookErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_webhook_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackDeleteWebhookErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_webhook_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_get_alert(organization_id: UUID, service_id: UUID, click_stack_alert_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse, ClickStackGetAlertErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a specific alert by ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_get_alert(organization_id, service_id, click_stack_alert_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackGetAlertErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_get_alert(
    organization_id, service_id, click_stack_alert_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackGetAlertErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_alert_id</code> | <code>str</code> | ClickStack Alert ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id_response.py), [ClickStackGetAlertErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_alert_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackGetAlertErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_alert_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_get_dashboard(organization_id: UUID, service_id: UUID, click_stack_dashboard_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse, ClickStackGetDashboardErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a specific dashboard by ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_get_dashboard(
    organization_id, service_id, click_stack_dashboard_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackGetDashboardErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_get_dashboard(
    organization_id, service_id, click_stack_dashboard_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackGetDashboardErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_dashboard_id</code> | <code>str</code> | ClickStack Dashboard ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response.py), [ClickStackGetDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_dashboard_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackGetDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_dashboard_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_get_role(organization_id: UUID, service_id: UUID, click_stack_role_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse, ClickStackGetRoleErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a specific role by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_get_role(organization_id, service_id, click_stack_role_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackGetRoleErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_get_role(
    organization_id, service_id, click_stack_role_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackGetRoleErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_role_id</code> | <code>str</code> | id parameter |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id_response.py), [ClickStackGetRoleErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_role_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackGetRoleErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_role_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_get_saved_search(organization_id: UUID, service_id: UUID, click_stack_saved_search_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse, ClickStackGetSavedSearchErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a specific saved search by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_get_saved_search(
    organization_id, service_id, click_stack_saved_search_id
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackGetSavedSearchErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_get_saved_search(
    organization_id, service_id, click_stack_saved_search_id
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackGetSavedSearchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_saved_search_id</code> | <code>str</code> | Saved search ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response.py), [ClickStackGetSavedSearchErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_saved_search_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackGetSavedSearchErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_saved_search_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_get_source(organization_id: UUID, service_id: UUID, click_stack_source_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse, ClickStackGetSourceErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a specific source by ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_get_source(organization_id, service_id, click_stack_source_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackGetSourceErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_get_source(
    organization_id, service_id, click_stack_source_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackGetSourceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_source_id</code> | <code>str</code> | Source ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id_response.py), [ClickStackGetSourceErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_source_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackGetSourceErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_source_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_list_alerts(organization_id: UUID, service_id: UUID, *, limit: int | None = 1000, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackAlertsResponse, ClickStackListAlertsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves alerts for the authenticated team (paginated). Results are capped at `limit` (default and maximum 1000). When `totalCount` exceeds the number of returned items, page with `limit`/`offset` to retrieve them all.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_list_alerts(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackAlertsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackListAlertsErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_list_alerts(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackAlertsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackListAlertsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>limit</code> | <code>int \| None</code> | Maximum number of results to return.<br>**Default**: <code>1000</code> |
| <code>offset</code> | <code>int \| None</code> | Number of results to skip before returning.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackAlertsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_response.py), [ClickStackListAlertsErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_alerts_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackAlertsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackListAlertsErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_alerts_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackAlerts400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackAlerts500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_list_dashboards(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackDashboardsResponse, ClickStackListDashboardsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a list of all dashboards for the authenticated team

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_list_dashboards(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackDashboardsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackListDashboardsErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_list_dashboards(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackDashboardsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackListDashboardsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackDashboardsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_response.py), [ClickStackListDashboardsErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_dashboards_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackDashboardsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackListDashboardsErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_dashboards_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackDashboards400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackDashboards500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_list_roles(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackRolesResponse, ClickStackListRolesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves all roles for the authenticated team, including predefined roles.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_list_roles(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackRolesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackListRolesErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_list_roles(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackRolesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackListRolesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackRolesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_response.py), [ClickStackListRolesErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_roles_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackRolesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackListRolesErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_roles_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackRoles400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackRoles500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_list_saved_searches(organization_id: UUID, service_id: UUID, *, limit: int | None = 1000, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackSavedSearchesResponse, ClickStackListSavedSearchesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves saved searches for the authenticated team (paginated). Results are capped at `limit` (default and maximum 1000). When `totalCount` exceeds the number of returned items, page with `limit`/`offset` to retrieve them all.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_list_saved_searches(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSavedSearchesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackListSavedSearchesErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_list_saved_searches(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSavedSearchesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackListSavedSearchesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>limit</code> | <code>int \| None</code> | Maximum number of results to return.<br>**Default**: <code>1000</code> |
| <code>offset</code> | <code>int \| None</code> | Number of results to skip before returning.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackSavedSearchesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_response.py), [ClickStackListSavedSearchesErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_saved_searches_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackSavedSearchesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackListSavedSearchesErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_saved_searches_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackSavedSearches400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackSavedSearches500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_list_sources(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackSourcesResponse, ClickStackListSourcesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a list of all sources for the authenticated team

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_list_sources(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSourcesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackListSourcesErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_list_sources(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSourcesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackListSourcesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackSourcesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_response.py), [ClickStackListSourcesErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_sources_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackSourcesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackListSourcesErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_sources_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackSources400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackSources500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_list_webhooks(organization_id: UUID, service_id: UUID, *, limit: int | None = 1000, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackWebhooksResponse, ClickStackListWebhooksErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves webhooks for the authenticated team (paginated). Results are capped at `limit` (default and maximum 1000). When `totalCount` exceeds the number of returned items, page with `limit`/`offset` to retrieve them all.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_list_webhooks(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackWebhooksResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackListWebhooksErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_list_webhooks(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackWebhooksResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackListWebhooksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>limit</code> | <code>int \| None</code> | Maximum number of results to return.<br>**Default**: <code>1000</code> |
| <code>offset</code> | <code>int \| None</code> | Number of results to skip before returning.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackWebhooksResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_response.py), [ClickStackListWebhooksErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_webhooks_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackWebhooksResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackListWebhooksErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_webhooks_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackWebhooks400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackWebhooks500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_update_alert(organization_id: UUID, service_id: UUID, click_stack_alert_id: str, *, body: ClickStackUpdateAlertRequest | ClickStackUpdateAlertRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse, ClickStackUpdateAlertErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Updates an existing alert

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_update_alert(
    organization_id, service_id, click_stack_alert_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackUpdateAlertErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_update_alert(
    organization_id, service_id, click_stack_alert_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackUpdateAlertErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_alert_id</code> | <code>str</code> | ClickStack Alert ID |
| <code>body</code> | <code>[ClickStackUpdateAlertRequest](open_api_spec_for_click_house_cloud/models/click_stack_update_alert_request.py) \| [ClickStackUpdateAlertRequestDict](open_api_spec_for_click_house_cloud/models/click_stack_update_alert_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id_response.py), [ClickStackUpdateAlertErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_alert_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackUpdateAlertErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_alert_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_update_dashboard(organization_id: UUID, service_id: UUID, click_stack_dashboard_id: str, *, body: ClickStackUpdateDashboardRequest | ClickStackUpdateDashboardRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse, ClickStackUpdateDashboardErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Updates an existing dashboard.  **Concurrency:** This endpoint does not support optimistic concurrency control. Concurrent PUT requests for the same dashboard may silently overwrite each other, which can leave orphan tile-to-container references on layout-shape edits. Clients should serialize edits to a given dashboard.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_update_dashboard(
    organization_id, service_id, click_stack_dashboard_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackUpdateDashboardErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_update_dashboard(
    organization_id, service_id, click_stack_dashboard_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackUpdateDashboardErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_dashboard_id</code> | <code>str</code> | ClickStack Dashboard ID |
| <code>body</code> | <code>[ClickStackUpdateDashboardRequest](open_api_spec_for_click_house_cloud/models/click_stack_update_dashboard_request.py) \| [ClickStackUpdateDashboardRequestDict](open_api_spec_for_click_house_cloud/models/click_stack_update_dashboard_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response.py), [ClickStackUpdateDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_dashboard_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackUpdateDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_dashboard_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_update_role(organization_id: UUID, service_id: UUID, click_stack_role_id: str, *, body: ClickStackUpdateRoleRequest | ClickStackUpdateRoleRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse, ClickStackUpdateRoleErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Updates a custom role's permissions, name, and description. Predefined roles cannot be modified.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_update_role(organization_id, service_id, click_stack_role_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackUpdateRoleErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_update_role(
    organization_id, service_id, click_stack_role_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackUpdateRoleErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_role_id</code> | <code>str</code> | id parameter |
| <code>body</code> | <code>[ClickStackUpdateRoleRequest](open_api_spec_for_click_house_cloud/models/click_stack_update_role_request.py) \| [ClickStackUpdateRoleRequestDict](open_api_spec_for_click_house_cloud/models/click_stack_update_role_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id_response.py), [ClickStackUpdateRoleErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_role_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackUpdateRoleErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_role_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_update_saved_search(organization_id: UUID, service_id: UUID, click_stack_saved_search_id: str, *, body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse, ClickStackUpdateSavedSearchErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Updates an existing saved search. This is a full replace: send the full object. Every optional field (`select`, `where`, `whereLanguage`, `orderBy`, `tags`, `filters`) is always written and falls back to its default when omitted, so omitting a field resets it rather than preserving the stored value.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_update_saved_search(
    organization_id, service_id, click_stack_saved_search_id
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackUpdateSavedSearchErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_update_saved_search(
    organization_id, service_id, click_stack_saved_search_id
)
match result:
    case Success(payload=payload):
        # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse
        ...
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackUpdateSavedSearchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_saved_search_id</code> | <code>str</code> | Saved search ID |
| <code>body</code> | <code>[ClickStackSavedSearchInput](open_api_spec_for_click_house_cloud/models/click_stack_saved_search_input.py) \| [ClickStackSavedSearchInputDict](open_api_spec_for_click_house_cloud/models/click_stack_saved_search_input.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response.py), [ClickStackUpdateSavedSearchErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_saved_search_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackUpdateSavedSearchErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_saved_search_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_update_source(organization_id: UUID, service_id: UUID, click_stack_source_id: str, *, body: ClickStackSource | ClickStackSourceDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse, ClickStackUpdateSourceErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Updates an existing source. The full source object must be provided; this is a replace, not a patch.  The request body is a source object without the `id` field. If an `id` is sent anyway it is silently ignored (stripped before validation — never a 400); the path parameter alone identifies the source. Granularity fields (`materializedViews[].minGranularity` and `metadataMaterializedViews.granularity`) accept the same short format the API returns (e.g. `5m`, `15s`, `1h`, `1d`).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_update_source(
    organization_id, service_id, click_stack_source_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackUpdateSourceErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_update_source(
    organization_id, service_id, click_stack_source_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackUpdateSourceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_source_id</code> | <code>str</code> | Source ID |
| <code>body</code> | <code>[ClickStackSource](open_api_spec_for_click_house_cloud/models/unions/click_stack_source.py) \| [ClickStackSourceDict](open_api_spec_for_click_house_cloud/models/unions/click_stack_source.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id_response.py), [ClickStackUpdateSourceErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_source_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackUpdateSourceErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_source_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_update_webhook(organization_id: UUID, service_id: UUID, click_stack_webhook_id: str, *, body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse, ClickStackUpdateWebhookErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Replaces an existing webhook. Readable optional fields (`description`, `body`) are a full replace: omitting them clears them. The write-only fields `headers` and `queryParams` are never returned on read, so omitting them preserves the stored values; send an explicit empty object (`{}`) to clear them. Exception: if the destination (`url` or `service`) changes, omitted `headers`/ `queryParams` are cleared rather than preserved so stored secrets are never forwarded to a new destination.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_update_webhook(
    organization_id, service_id, click_stack_webhook_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackUpdateWebhookErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_update_webhook(
    organization_id, service_id, click_stack_webhook_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackUpdateWebhookErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>click_stack_webhook_id</code> | <code>str</code> | Webhook ID |
| <code>body</code> | <code>[ClickStackWebhookInput](open_api_spec_for_click_house_cloud/models/click_stack_webhook_input.py) \| [ClickStackWebhookInputDict](open_api_spec_for_click_house_cloud/models/click_stack_webhook_input.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id_response.py), [ClickStackUpdateWebhookErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_webhook_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackUpdateWebhookErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_webhook_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def click_stack_validate_dashboard(organization_id: UUID, service_id: UUID, *, body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickstackDashboardsValidateResponse, ClickStackValidateDashboardErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Validates a dashboard body against the same schema and tile rules used by POST /api/v2/dashboards. The dashboard is **never persisted**. Use this endpoint at plan time (e.g. from a Terraform provider) to check that a dashboard configuration is valid before applying it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.click_stack.with_raw_response.click_stack_validate_dashboard(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackDashboardsValidateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackValidateDashboardErrorBody
```

**Async**

```python
result = await async_client.click_stack.with_raw_response.click_stack_validate_dashboard(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickstackDashboardsValidateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ClickStackValidateDashboardErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the ClickStack service. |
| <code>body</code> | <code>[ClickStackCreateDashboardRequest](open_api_spec_for_click_house_cloud/models/click_stack_create_dashboard_request.py) \| [ClickStackCreateDashboardRequestDict](open_api_spec_for_click_house_cloud/models/click_stack_create_dashboard_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickstackDashboardsValidateResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_validate_response.py), [ClickStackValidateDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_validate_dashboard_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickstackDashboardsValidateResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_validate_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ClickStackValidateDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_validate_dashboard_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickstackDashboardsValidate400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_validate400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickstackDashboardsValidate500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_validate500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## OrganizationApi

> Source: [OrganizationApi](open_api_spec_for_click_house_cloud/apis/organization_api.py)

<details>
<summary><code>def activity_get(organization_id: UUID, activity_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsActivitiesResponse1, ActivityGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single organization activity by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.organization_api.with_raw_response.activity_get(organization_id, activity_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsActivitiesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ActivityGetErrorBody
```

**Async**

```python
result = await async_client.organization_api.with_raw_response.activity_get(organization_id, activity_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsActivitiesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ActivityGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>activity_id</code> | <code>str</code> | ID of the requested activity. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsActivitiesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_activities_response1.py), [ActivityGetErrorBody](open_api_spec_for_click_house_cloud/errors/activity_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsActivitiesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_activities_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ActivityGetErrorBody](open_api_spec_for_click_house_cloud/errors/activity_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsActivities400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_activities400_error1.py)</code> |
| 500 | <code>[V1OrganizationsActivities500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_activities500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def activity_get_list(organization_id: UUID, *, from_date: RFC3339DateTime | None = None, to_date: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsActivitiesResponse, ActivityGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of all organization activities.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.organization_api.with_raw_response.activity_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsActivitiesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ActivityGetListErrorBody
```

**Async**

```python
result = await async_client.organization_api.with_raw_response.activity_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsActivitiesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ActivityGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>from_date</code> | <code>RFC3339DateTime \| None</code> | A starting date for a search<br>**Default**: <code>None</code> |
| <code>to_date</code> | <code>RFC3339DateTime \| None</code> | An ending date for a search<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsActivitiesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_activities_response.py), [ActivityGetListErrorBody](open_api_spec_for_click_house_cloud/errors/activity_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsActivitiesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_activities_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ActivityGetListErrorBody](open_api_spec_for_click_house_cloud/errors/activity_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsActivities400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_activities400_error1.py)</code> |
| 500 | <code>[V1OrganizationsActivities500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_activities500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_byoc_infrastructure_create(organization_id: UUID, *, body: ByocInfrastructurePostRequest | ByocInfrastructurePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsByocInfrastructureResponse, OrganizationByocInfrastructureCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new BYOC Infrastructure in the organization. Returns the configuration of the newly created infrastructure

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.organization_api.with_raw_response.organization_byoc_infrastructure_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsByocInfrastructureResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationByocInfrastructureCreateErrorBody
```

**Async**

```python
result = await async_client.organization_api.with_raw_response.organization_byoc_infrastructure_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsByocInfrastructureResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationByocInfrastructureCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>body</code> | <code>[ByocInfrastructurePostRequest](open_api_spec_for_click_house_cloud/models/byoc_infrastructure_post_request.py) \| [ByocInfrastructurePostRequestDict](open_api_spec_for_click_house_cloud/models/byoc_infrastructure_post_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsByocInfrastructureResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure_response.py), [OrganizationByocInfrastructureCreateErrorBody](open_api_spec_for_click_house_cloud/errors/organization_byoc_infrastructure_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsByocInfrastructureResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationByocInfrastructureCreateErrorBody](open_api_spec_for_click_house_cloud/errors/organization_byoc_infrastructure_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsByocInfrastructure400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure400_error1.py)</code> |
| 500 | <code>[V1OrganizationsByocInfrastructure500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_byoc_infrastructure_delete(organization_id: UUID, byoc_infrastructure_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsByocInfrastructureResponse1, OrganizationByocInfrastructureDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a BYOC Infrastructure from the organization

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.organization_api.with_raw_response.organization_byoc_infrastructure_delete(
    organization_id, byoc_infrastructure_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsByocInfrastructureResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationByocInfrastructureDeleteErrorBody
```

**Async**

```python
result = await async_client.organization_api.with_raw_response.organization_byoc_infrastructure_delete(
    organization_id, byoc_infrastructure_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsByocInfrastructureResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationByocInfrastructureDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>byoc_infrastructure_id</code> | <code>UUID</code> | ID of the requested BYOC Infrastructure |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsByocInfrastructureResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure_response1.py), [OrganizationByocInfrastructureDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/organization_byoc_infrastructure_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsByocInfrastructureResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationByocInfrastructureDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/organization_byoc_infrastructure_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsByocInfrastructure400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure400_error1.py)</code> |
| 500 | <code>[V1OrganizationsByocInfrastructure500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_byoc_infrastructure_update(organization_id: UUID, byoc_infrastructure_id: UUID, *, body: ByocInfrastructurePatchRequest | ByocInfrastructurePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsByocInfrastructureResponse, OrganizationByocInfrastructureUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update configuration of the BYOC infrastructure. Returns the modified infrastructure

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.organization_api.with_raw_response.organization_byoc_infrastructure_update(
    organization_id, byoc_infrastructure_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsByocInfrastructureResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationByocInfrastructureUpdateErrorBody
```

**Async**

```python
result = await async_client.organization_api.with_raw_response.organization_byoc_infrastructure_update(
    organization_id, byoc_infrastructure_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsByocInfrastructureResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationByocInfrastructureUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>byoc_infrastructure_id</code> | <code>UUID</code> | ID of the requested BYOC Infrastructure |
| <code>body</code> | <code>[ByocInfrastructurePatchRequest](open_api_spec_for_click_house_cloud/models/byoc_infrastructure_patch_request.py) \| [ByocInfrastructurePatchRequestDict](open_api_spec_for_click_house_cloud/models/byoc_infrastructure_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsByocInfrastructureResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure_response.py), [OrganizationByocInfrastructureUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/organization_byoc_infrastructure_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsByocInfrastructureResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationByocInfrastructureUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/organization_byoc_infrastructure_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsByocInfrastructure400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure400_error1.py)</code> |
| 500 | <code>[V1OrganizationsByocInfrastructure500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_get(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsResponse1, OrganizationGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns details of a single organization. In order to get the details, the auth key must belong to the organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.organization_api.with_raw_response.organization_get(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationGetErrorBody
```

**Async**

```python
result = await async_client.organization_api.with_raw_response.organization_get(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_response1.py), [OrganizationGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1Organizations400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations400_error1.py)</code> |
| 500 | <code>[V1Organizations500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_get_list(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsResponse, OrganizationGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list with a single organization associated with the API key in the request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.organization_api.with_raw_response.organization_get_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationGetListErrorBody
```

**Async**

```python
result = await async_client.organization_api.with_raw_response.organization_get_list()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_response.py), [OrganizationGetListErrorBody](open_api_spec_for_click_house_cloud/errors/organization_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationGetListErrorBody](open_api_spec_for_click_house_cloud/errors/organization_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1Organizations400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations400_error1.py)</code> |
| 500 | <code>[V1Organizations500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_private_endpoint_config_get_list(organization_id: UUID, cloud_provider: str, region_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPrivateEndpointConfigResponse, OrganizationPrivateEndpointConfigGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated. Please follow [documentation](https://clickhouse.com/docs/manage/security/aws-privatelink#add-endpoint-id-to-services-allow-list) for the updated process.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.organization_api.with_raw_response.organization_private_endpoint_config_get_list(
    organization_id, cloud_provider, region_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPrivateEndpointConfigResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationPrivateEndpointConfigGetListErrorBody
```

**Async**

```python
result = await async_client.organization_api.with_raw_response.organization_private_endpoint_config_get_list(
    organization_id, cloud_provider, region_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPrivateEndpointConfigResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationPrivateEndpointConfigGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>cloud_provider</code> | <code>str</code> | Cloud provider identifier. One of aws, gcp, or azure. |
| <code>region_id</code> | <code>str</code> | Region identifier within specific cloud providers. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPrivateEndpointConfigResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_private_endpoint_config_response.py), [OrganizationPrivateEndpointConfigGetListErrorBody](open_api_spec_for_click_house_cloud/errors/organization_private_endpoint_config_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPrivateEndpointConfigResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_private_endpoint_config_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationPrivateEndpointConfigGetListErrorBody](open_api_spec_for_click_house_cloud/errors/organization_private_endpoint_config_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPrivateEndpointConfig400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_private_endpoint_config400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPrivateEndpointConfig500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_private_endpoint_config500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_quota_get(organization_id: UUID, quota_code: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsQuotasResponse1, OrganizationQuotaGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns a single organization quota identified by its quota code. Responds with a not found error when the quota code is unknown or the quota does not apply to the organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.organization_api.with_raw_response.organization_quota_get(organization_id, quota_code)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsQuotasResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationQuotaGetErrorBody
```

**Async**

```python
result = await async_client.organization_api.with_raw_response.organization_quota_get(organization_id, quota_code)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsQuotasResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationQuotaGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>quota_code</code> | <code>str</code> | Code of the requested quota. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsQuotasResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_quotas_response1.py), [OrganizationQuotaGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_quota_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsQuotasResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_quotas_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationQuotaGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_quota_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsQuotas400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_quotas400_error1.py)</code> |
| 500 | <code>[V1OrganizationsQuotas500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_quotas500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_quotas_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsQuotasResponse, OrganizationQuotasGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the resource quotas enforced for the organization together with their current usage where available. Quotas that do not apply to the organization are omitted. Quota values reflect the limits currently enforced, so they can be polled to detect changes, for example after a billing status change. The response contains one entry per quota code; quotas enforced per resource may additionally appear under resource-scoped endpoints in the future.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.organization_api.with_raw_response.organization_quotas_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsQuotasResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationQuotasGetListErrorBody
```

**Async**

```python
result = await async_client.organization_api.with_raw_response.organization_quotas_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsQuotasResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationQuotasGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsQuotasResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_quotas_response.py), [OrganizationQuotasGetListErrorBody](open_api_spec_for_click_house_cloud/errors/organization_quotas_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsQuotasResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_quotas_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationQuotasGetListErrorBody](open_api_spec_for_click_house_cloud/errors/organization_quotas_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsQuotas400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_quotas400_error1.py)</code> |
| 500 | <code>[V1OrganizationsQuotas500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_quotas500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_update(organization_id: UUID, *, body: OrganizationPatchRequest | OrganizationPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsResponse1, OrganizationUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates organization fields. Requires ADMIN auth key role.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.organization_api.with_raw_response.organization_update(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationUpdateErrorBody
```

**Async**

```python
result = await async_client.organization_api.with_raw_response.organization_update(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization to update. |
| <code>body</code> | <code>[OrganizationPatchRequest](open_api_spec_for_click_house_cloud/models/organization_patch_request.py) \| [OrganizationPatchRequestDict](open_api_spec_for_click_house_cloud/models/organization_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_response1.py), [OrganizationUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/organization_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/organization_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1Organizations400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations400_error1.py)</code> |
| 500 | <code>[V1Organizations500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Postgres

> Source: [Postgres](open_api_spec_for_click_house_cloud/apis/postgres.py)

<details>
<summary><code>def postgres_instance_config_get(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresConfigResponse, PostgresInstanceConfigGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns the configuration data for a Postgres service and its PgBouncer service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_instance_config_get(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresConfigResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstanceConfigGetErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_instance_config_get(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresConfigResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstanceConfigGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresConfigResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config_response.py), [PostgresInstanceConfigGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_config_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresConfigResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresInstanceConfigGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_config_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresConfig400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresConfig500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_instance_config_patch(organization_id: UUID, postgres_id: UUID, *, body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresConfigResponse1, PostgresInstanceConfigPatchErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Update the existing Postgres service and pgBouncer configuration.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_instance_config_patch(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresConfigResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstanceConfigPatchErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_instance_config_patch(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresConfigResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstanceConfigPatchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>body</code> | <code>[PostgresInstanceConfig](open_api_spec_for_click_house_cloud/models/postgres_instance_config.py) \| [PostgresInstanceConfigDict](open_api_spec_for_click_house_cloud/models/postgres_instance_config.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresConfigResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config_response1.py), [PostgresInstanceConfigPatchErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_config_patch_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresConfigResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresInstanceConfigPatchErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_config_patch_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresConfig400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresConfig500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_instance_config_post(organization_id: UUID, postgres_id: UUID, *, body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresConfigResponse1, PostgresInstanceConfigPostErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Replace the existing Postgres service and pgBouncer configuration.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_instance_config_post(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresConfigResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstanceConfigPostErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_instance_config_post(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresConfigResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstanceConfigPostErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>body</code> | <code>[PostgresInstanceConfig](open_api_spec_for_click_house_cloud/models/postgres_instance_config.py) \| [PostgresInstanceConfigDict](open_api_spec_for_click_house_cloud/models/postgres_instance_config.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresConfigResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config_response1.py), [PostgresInstanceConfigPostErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_config_post_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresConfigResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresInstanceConfigPostErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_config_post_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresConfig400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresConfig500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_instance_create_read_replica(organization_id: UUID, postgres_id: UUID, *, body: PostgresServiceReadReplicaRequest | PostgresServiceReadReplicaRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresReadReplicaResponse, PostgresInstanceCreateReadReplicaErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Initiate the process to create a new read replica for a Postgres service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_instance_create_read_replica(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresReadReplicaResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstanceCreateReadReplicaErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_instance_create_read_replica(
    organization_id, postgres_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresReadReplicaResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstanceCreateReadReplicaErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>body</code> | <code>[PostgresServiceReadReplicaRequest](open_api_spec_for_click_house_cloud/models/postgres_service_read_replica_request.py) \| [PostgresServiceReadReplicaRequestDict](open_api_spec_for_click_house_cloud/models/postgres_service_read_replica_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresReadReplicaResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_read_replica_response.py), [PostgresInstanceCreateReadReplicaErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_create_read_replica_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresReadReplicaResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_read_replica_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresInstanceCreateReadReplicaErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_create_read_replica_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresReadReplica400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_read_replica400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresReadReplica500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_read_replica500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_instance_metrics_get(organization_id: UUID, postgres_id: UUID, from_date: RFC3339DateTime, to_date: RFC3339DateTime, *, bucket_size_seconds: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresMetricsResponse, PostgresInstanceMetricsGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns bucketed time-series metrics for a PostgreSQL service over the requested window (CPU, memory, disk, network, connections, cache hit ratio, throughput, transactions, and more). Use this to chart or analyze how a service behaved over time.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_instance_metrics_get(
    organization_id, postgres_id, from_date, to_date
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresMetricsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstanceMetricsGetErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_instance_metrics_get(
    organization_id, postgres_id, from_date, to_date
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresMetricsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstanceMetricsGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the Postgres service. |
| <code>from_date</code> | <code>RFC3339DateTime</code> | Inclusive start of the time window (RFC 3339 date-time). |
| <code>to_date</code> | <code>RFC3339DateTime</code> | Exclusive end of the time window (RFC 3339 date-time). |
| <code>bucket_size_seconds</code> | <code>int \| None</code> | Time-series bucket size in seconds. When omitted, a bucket size is derived from the requested window. Requests are capped at 250 data points.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresMetricsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_metrics_response.py), [PostgresInstanceMetricsGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_metrics_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresMetricsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_metrics_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresInstanceMetricsGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_metrics_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresMetrics400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_metrics400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresMetrics500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_metrics500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_instance_restore(organization_id: UUID, postgres_id: UUID, *, body: PostgresServiceRestoreRequest | PostgresServiceRestoreRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresRestoredServiceResponse, PostgresInstanceRestoreErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Restore a Postgres database from continuous backup, optionally at a specific point in time.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_instance_restore(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresRestoredServiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstanceRestoreErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_instance_restore(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresRestoredServiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstanceRestoreErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>body</code> | <code>[PostgresServiceRestoreRequest](open_api_spec_for_click_house_cloud/models/postgres_service_restore_request.py) \| [PostgresServiceRestoreRequestDict](open_api_spec_for_click_house_cloud/models/postgres_service_restore_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresRestoredServiceResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_restored_service_response.py), [PostgresInstanceRestoreErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_restore_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresRestoredServiceResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_restored_service_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresInstanceRestoreErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_restore_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresRestoredService400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_restored_service400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresRestoredService500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_restored_service500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_logs_get_list(organization_id: UUID, postgres_id: UUID, from_date: RFC3339DateTime, to_date: RFC3339DateTime, *, body_contains: str | None = None, severity: str | None = None, sort_order: SortOrder1OrStr | None = SortOrder1.DESC, limit: int | None = 50, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresLogsResponse, PostgresLogsGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns PostgreSQL server log entries for a Postgres service within the given time window, most recent first by default (override with `sort_order`). Results are paginated with `limit`/`offset`; advance `offset` until a page returns fewer than `limit` entries to read the full window. The time range must not exceed 30 days, and `to_date` must be after `from_date`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_logs_get_list(organization_id, postgres_id, from_date, to_date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresLogsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresLogsGetListErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_logs_get_list(
    organization_id, postgres_id, from_date, to_date
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresLogsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresLogsGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>from_date</code> | <code>RFC3339DateTime</code> | Inclusive start of the time window (RFC 3339 date-time). |
| <code>to_date</code> | <code>RFC3339DateTime</code> | Inclusive end of the time window (RFC 3339 date-time). |
| <code>body_contains</code> | <code>str \| None</code> | Case-sensitive substring the log body must contain.<br>**Default**: <code>None</code> |
| <code>severity</code> | <code>str \| None</code> | Filter to log entries with this PostgreSQL severity (for example, ERROR, WARNING, LOG).<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>[SortOrder1OrStr](open_api_spec_for_click_house_cloud/models/enums/sort_order1.py) \| None</code> | Sort order. One of `asc` or `desc`.<br>**Default**: <code>SortOrder1.DESC</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of results to return.<br>**Default**: <code>50</code> |
| <code>offset</code> | <code>int \| None</code> | Number of results to skip before returning.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresLogsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_logs_response.py), [PostgresLogsGetListErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_logs_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresLogsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_logs_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresLogsGetListErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_logs_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresLogs400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_logs400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresLogs500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_logs500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_service_certs_get(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, PostgresServiceCertsGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Download CA certificates for a PostgreSQL service

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_service_certs_get(organization_id, postgres_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServiceCertsGetErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_service_certs_get(organization_id, postgres_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServiceCertsGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;None, [PostgresServiceCertsGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_certs_get_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[PostgresServiceCertsGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_certs_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresCaCertificates400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_ca_certificates400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresCaCertificates500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_ca_certificates500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_service_create(organization_id: UUID, *, body: PostgresServicePostRequest | PostgresServicePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresResponse, PostgresServiceCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Creates a new Postgres service in the organization and returns it. The service is started asynchronously.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_service_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServiceCreateErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_service_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServiceCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that will own the service. |
| <code>body</code> | <code>[PostgresServicePostRequest](open_api_spec_for_click_house_cloud/models/postgres_service_post_request.py) \| [PostgresServicePostRequestDict](open_api_spec_for_click_house_cloud/models/postgres_service_post_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response.py), [PostgresServiceCreateErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresServiceCreateErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgres400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgres500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_service_delete(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresResponse3, PostgresServiceDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Deletes a Postgres service that belongs to the organization

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_service_delete(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresResponse3
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServiceDeleteErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_service_delete(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresResponse3
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServiceDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresResponse3](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response3.py), [PostgresServiceDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresResponse3](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response3.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresServiceDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgres400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgres500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_service_get(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresResponse, PostgresServiceGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns a Postgres service that belongs to the organization

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_service_get(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServiceGetErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_service_get(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServiceGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response.py), [PostgresServiceGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresServiceGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgres400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgres500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_service_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresResponse1, PostgresServiceGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns a list of all Postgres services in the organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_service_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServiceGetListErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_service_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServiceGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the services. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response1.py), [PostgresServiceGetListErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresServiceGetListErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgres400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgres500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_service_patch(organization_id: UUID, postgres_id: UUID, *, body: PostgresServicePatchRequest | PostgresServicePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresResponse, PostgresServicePatchErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Update a Postgres service that belongs to the organization. **WARNING:** Changing the name also updates the host name and certificates for the service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_service_patch(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServicePatchErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_service_patch(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServicePatchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>body</code> | <code>[PostgresServicePatchRequest](open_api_spec_for_click_house_cloud/models/postgres_service_patch_request.py) \| [PostgresServicePatchRequestDict](open_api_spec_for_click_house_cloud/models/postgres_service_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response.py), [PostgresServicePatchErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_patch_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresServicePatchErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_patch_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgres400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgres500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_service_patch_state(organization_id: UUID, postgres_id: UUID, *, body: PostgresServiceSetState | PostgresServiceSetStateDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresStateResponse, PostgresServicePatchStateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Initiate a process for a Postgres service:
* restart: Initiates a service restart
* promote: Promotes a read replica to primary
* switchover: Switch a primary over to a standby

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_service_patch_state(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresStateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServicePatchStateErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_service_patch_state(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresStateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServicePatchStateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>body</code> | <code>[PostgresServiceSetState](open_api_spec_for_click_house_cloud/models/postgres_service_set_state.py) \| [PostgresServiceSetStateDict](open_api_spec_for_click_house_cloud/models/postgres_service_set_state.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresStateResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_state_response.py), [PostgresServicePatchStateErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_patch_state_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresStateResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_state_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresServicePatchStateErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_patch_state_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresState400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_state400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresState500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_state500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_service_set_password(organization_id: UUID, postgres_id: UUID, *, body: PostgresServiceSetPassword | PostgresServiceSetPasswordDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresPasswordResponse, PostgresServiceSetPasswordErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Sets a new password for a Postgres service's superuser account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.postgres_service_set_password(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresPasswordResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServiceSetPasswordErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.postgres_service_set_password(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresPasswordResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresServiceSetPasswordErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>body</code> | <code>[PostgresServiceSetPassword](open_api_spec_for_click_house_cloud/models/postgres_service_set_password.py) \| [PostgresServiceSetPasswordDict](open_api_spec_for_click_house_cloud/models/postgres_service_set_password.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresPasswordResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_password_response.py), [PostgresServiceSetPasswordErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_set_password_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresPasswordResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_password_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresServiceSetPasswordErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_set_password_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresPassword400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_password400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresPassword500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_password500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def slow_query_pattern_get(organization_id: UUID, postgres_id: UUID, query_id: str, db_name: str, db_user: str, db_operation: str, *, app: str | None = None, timestamp: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse, SlowQueryPatternGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns aggregate metrics for a single slow query pattern together with its most recent individual executions.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.slow_query_pattern_get(
    organization_id, postgres_id, query_id, db_name, db_user, db_operation
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SlowQueryPatternGetErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.slow_query_pattern_get(
    organization_id, postgres_id, query_id, db_name, db_user, db_operation
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SlowQueryPatternGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>query_id</code> | <code>str</code> | Stable identifier for the query pattern. |
| <code>db_name</code> | <code>str</code> | Database name filter. |
| <code>db_user</code> | <code>str</code> | Database user filter. |
| <code>db_operation</code> | <code>str</code> | Database operation filter (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY). |
| <code>app</code> | <code>str \| None</code> | Application name filter.<br>**Default**: <code>None</code> |
| <code>timestamp</code> | <code>RFC3339DateTime \| None</code> | Timestamp of a specific execution (RFC 3339).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns_query_id_response.py), [SlowQueryPatternGetErrorBody](open_api_spec_for_click_house_cloud/errors/slow_query_pattern_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns_query_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[SlowQueryPatternGetErrorBody](open_api_spec_for_click_house_cloud/errors/slow_query_pattern_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresSlowQueryPatternsQueryId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns_query_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresSlowQueryPatternsQueryId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns_query_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def slow_query_patterns_get_list(organization_id: UUID, postgres_id: UUID, from_date: RFC3339DateTime, to_date: RFC3339DateTime, *, db_name: str | None = None, db_user: str | None = None, db_operation: str | None = None, app: str | None = None, sort_by: SortByOrStr | None = SortBy.TOTAL_DURATION, sort_order: SortOrder1OrStr | None = SortOrder1.DESC, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsPostgresSlowQueryPatternsResponse, SlowQueryPatternsGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns aggregate metrics for the slowest query patterns observed on a Postgres service during the given time window. Use this to discover which queries dominate total execution time, CPU, I/O, or WAL generation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.postgres.with_raw_response.slow_query_patterns_get_list(
    organization_id, postgres_id, from_date, to_date
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresSlowQueryPatternsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SlowQueryPatternsGetListErrorBody
```

**Async**

```python
result = await async_client.postgres.with_raw_response.slow_query_patterns_get_list(
    organization_id, postgres_id, from_date, to_date
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsPostgresSlowQueryPatternsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SlowQueryPatternsGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>from_date</code> | <code>RFC3339DateTime</code> | Inclusive start of the time window (RFC 3339 date-time). |
| <code>to_date</code> | <code>RFC3339DateTime</code> | Exclusive end of the time window (RFC 3339 date-time). |
| <code>db_name</code> | <code>str \| None</code> | Database name filter.<br>**Default**: <code>None</code> |
| <code>db_user</code> | <code>str \| None</code> | Database user filter.<br>**Default**: <code>None</code> |
| <code>db_operation</code> | <code>str \| None</code> | Database operation filter (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY).<br>**Default**: <code>None</code> |
| <code>app</code> | <code>str \| None</code> | Application name filter.<br>**Default**: <code>None</code> |
| <code>sort_by</code> | <code>[SortByOrStr](open_api_spec_for_click_house_cloud/models/enums/sort_by.py) \| None</code> | Field to sort results by.<br>**Default**: <code>SortBy.TOTAL_DURATION</code> |
| <code>sort_order</code> | <code>[SortOrder1OrStr](open_api_spec_for_click_house_cloud/models/enums/sort_order1.py) \| None</code> | Sort order. One of `asc` or `desc`.<br>**Default**: <code>SortOrder1.DESC</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of results to return.<br>**Default**: <code>20</code> |
| <code>offset</code> | <code>int \| None</code> | Number of results to skip before returning.<br>**Default**: <code>0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsPostgresSlowQueryPatternsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns_response.py), [SlowQueryPatternsGetListErrorBody](open_api_spec_for_click_house_cloud/errors/slow_query_patterns_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsPostgresSlowQueryPatternsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[SlowQueryPatternsGetListErrorBody](open_api_spec_for_click_house_cloud/errors/slow_query_patterns_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresSlowQueryPatterns400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresSlowQueryPatterns500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Prometheus

> Source: [Prometheus](open_api_spec_for_click_house_cloud/apis/prometheus.py)

<details>
<summary><code>def instance_prometheus_get(organization_id: UUID, service_id: UUID, *, filtered_metrics: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[str, InstancePrometheusGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns prometheus metrics for a service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prometheus.with_raw_response.instance_prometheus_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstancePrometheusGetErrorBody
```

**Async**

```python
result = await async_client.prometheus.with_raw_response.instance_prometheus_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstancePrometheusGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>filtered_metrics</code> | <code>str \| None</code> | Return a filtered list of Prometheus metrics.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;str, [InstancePrometheusGetErrorBody](open_api_spec_for_click_house_cloud/errors/instance_prometheus_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>str</code> -- Successful response

**On `Failure`**: `error` is <code>[InstancePrometheusGetErrorBody](open_api_spec_for_click_house_cloud/errors/instance_prometheus_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesPrometheus400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_prometheus400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesPrometheus500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_prometheus500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_prometheus_discovery_get(organization_id: UUID, *, filtered_metrics: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[PrometheusDiscoveryTargetGroup], OrganizationPrometheusDiscoveryGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns one Prometheus scrape target per service in the organization, in the [HTTP service discovery](https://prometheus.io/docs/prometheus/latest/http_sd/) (`http_sd`) format. Only services the API key is authorized to view are included; services that are being deleted or have been deleted are omitted.

Point an https://prometheus.io/docs/prometheus/latest/configuration/configuration/#http_sd_config job at this endpoint to discover and scrape all services in the organization automatically. Prometheus refreshes the target list on every discovery poll, so newly created and deleted services are picked up without configuration changes.

Discovered targets scrape with `filtered_metrics=true` by default; pass `?filtered_metrics=false` to this endpoint to discover unfiltered targets. See the [Prometheus integration guide](https://clickhouse.com/docs/integrations/prometheus) for more on the exported metrics.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prometheus.with_raw_response.organization_prometheus_discovery_get(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PrometheusDiscoveryTargetGroup]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationPrometheusDiscoveryGetErrorBody
```

**Async**

```python
result = await async_client.prometheus.with_raw_response.organization_prometheus_discovery_get(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PrometheusDiscoveryTargetGroup]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationPrometheusDiscoveryGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>filtered_metrics</code> | <code>str \| None</code> | Whether discovered targets scrape a filtered list of metrics. Sets the filtered_metrics parameter on each discovered target. Defaults to true.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;list&#91;[PrometheusDiscoveryTargetGroup](open_api_spec_for_click_house_cloud/models/prometheus_discovery_target_group.py)&#93;, [OrganizationPrometheusDiscoveryGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_prometheus_discovery_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[PrometheusDiscoveryTargetGroup](open_api_spec_for_click_house_cloud/models/prometheus_discovery_target_group.py)&#93;</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationPrometheusDiscoveryGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_prometheus_discovery_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPrometheusDiscovery400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_prometheus_discovery400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPrometheusDiscovery500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_prometheus_discovery500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_prometheus_get(organization_id: UUID, *, filtered_metrics: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[str, OrganizationPrometheusGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated. Use the Prometheus service discovery endpoint (/v1/organizations/{organizationId}/prometheus/discovery) instead. This endpoint is not available for new organizations; contact ClickHouse support to request access. Returns Prometheus metrics for the services in an organization that the caller is authorized to view. Services the caller lacks view access to are omitted.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prometheus.with_raw_response.organization_prometheus_get(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationPrometheusGetErrorBody
```

**Async**

```python
result = await async_client.prometheus.with_raw_response.organization_prometheus_get(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationPrometheusGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>filtered_metrics</code> | <code>str \| None</code> | Return a filtered list of Prometheus metrics.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;str, [OrganizationPrometheusGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_prometheus_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>str</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationPrometheusGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_prometheus_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPrometheus400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_prometheus400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPrometheus500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_prometheus500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_instance_prometheus_get(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[str, PostgresInstancePrometheusGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns Prometheus metrics for a PostgreSQL service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prometheus.with_raw_response.postgres_instance_prometheus_get(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstancePrometheusGetErrorBody
```

**Async**

```python
result = await async_client.prometheus.with_raw_response.postgres_instance_prometheus_get(organization_id, postgres_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresInstancePrometheusGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the Postgres service. |
| <code>postgres_id</code> | <code>UUID</code> | ID of the requested Postgres service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;str, [PostgresInstancePrometheusGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_prometheus_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>str</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresInstancePrometheusGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_prometheus_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresPrometheus400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_prometheus400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresPrometheus500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_prometheus500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def postgres_org_prometheus_get(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[str, PostgresOrgPrometheusGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns Prometheus metrics for all PostgreSQL services in an organization. Maximum 100 services supported.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.prometheus.with_raw_response.postgres_org_prometheus_get(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresOrgPrometheusGetErrorBody
```

**Async**

```python
result = await async_client.prometheus.with_raw_response.postgres_org_prometheus_get(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PostgresOrgPrometheusGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;str, [PostgresOrgPrometheusGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_org_prometheus_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>str</code> -- Successful response

**On `Failure`**: `error` is <code>[PostgresOrgPrometheusGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_org_prometheus_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsPostgresPrometheus400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_prometheus400_error1.py)</code> |
| 500 | <code>[V1OrganizationsPostgresPrometheus500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_prometheus500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## QueryApiEndpoints

> Source: [QueryApiEndpoints](open_api_spec_for_click_house_cloud/apis/query_api_endpoints.py)

<details>
<summary><code>def query_api_endpoint_create(organization_id: UUID, service_id: UUID, *, body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsResponse, QueryApiEndpointCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates a Query API endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.query_api_endpoints.with_raw_response.query_api_endpoint_create(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesQueryApiEndpointsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryApiEndpointCreateErrorBody
```

**Async**

```python
result = await async_client.query_api_endpoints.with_raw_response.query_api_endpoint_create(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesQueryApiEndpointsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryApiEndpointCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>body</code> | <code>[PublicQueryApiEndpointRequest](open_api_spec_for_click_house_cloud/models/public_query_api_endpoint_request.py) \| [PublicQueryApiEndpointRequestDict](open_api_spec_for_click_house_cloud/models/public_query_api_endpoint_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesQueryApiEndpointsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_response.py), [QueryApiEndpointCreateErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesQueryApiEndpointsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_response.py)</code> -- The Query API endpoint was created.

**On `Failure`**: `error` is <code>[QueryApiEndpointCreateErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesQueryApiEndpoints400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints400_error1.py)</code> |
| 403 | <code>[V1OrganizationsServicesQueryApiEndpoints403Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints403_error1.py)</code> |
| 404 | <code>[V1OrganizationsServicesQueryApiEndpoints404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints404_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesQueryApiEndpoints500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_api_endpoint_delete(organization_id: UUID, service_id: UUID, endpoint_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse, QueryApiEndpointDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes a Query API endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.query_api_endpoints.with_raw_response.query_api_endpoint_delete(
    organization_id, service_id, endpoint_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryApiEndpointDeleteErrorBody
```

**Async**

```python
result = await async_client.query_api_endpoints.with_raw_response.query_api_endpoint_delete(
    organization_id, service_id, endpoint_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryApiEndpointDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>endpoint_id</code> | <code>UUID</code> | ID of the requested Query API endpoint. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id_response.py), [QueryApiEndpointDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id_response.py)</code> -- The Query API endpoint was deleted.

**On `Failure`**: `error` is <code>[QueryApiEndpointDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id400_error1.py)</code> |
| 403 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id403_error1.py)</code> |
| 404 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id404_error1.py)</code> |
| 409 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id409_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_api_endpoint_get(organization_id: UUID, service_id: UUID, endpoint_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1, QueryApiEndpointGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns a Query API endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.query_api_endpoints.with_raw_response.query_api_endpoint_get(organization_id, service_id, endpoint_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryApiEndpointGetErrorBody
```

**Async**

```python
result = await async_client.query_api_endpoints.with_raw_response.query_api_endpoint_get(
    organization_id, service_id, endpoint_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryApiEndpointGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>endpoint_id</code> | <code>UUID</code> | ID of the requested Query API endpoint. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id_response1.py), [QueryApiEndpointGetErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id_response1.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[QueryApiEndpointGetErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id400_error1.py)</code> |
| 403 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id403_error1.py)</code> |
| 404 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id404_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_api_endpoint_list(organization_id: UUID, service_id: UUID, *, cursor: str | None = None, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsResponse1, QueryApiEndpointListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns all active Query API endpoints for the service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.query_api_endpoints.with_raw_response.query_api_endpoint_list(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesQueryApiEndpointsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryApiEndpointListErrorBody
```

**Async**

```python
result = await async_client.query_api_endpoints.with_raw_response.query_api_endpoint_list(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesQueryApiEndpointsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryApiEndpointListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>cursor</code> | <code>str \| None</code> | Cursor returned in `pagination.nextCursor` from the previous page.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of records to return per page. Defaults to 100. Maximum is 100.<br>**Default**: <code>100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesQueryApiEndpointsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_response1.py), [QueryApiEndpointListErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesQueryApiEndpointsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_response1.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[QueryApiEndpointListErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesQueryApiEndpoints400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints400_error1.py)</code> |
| 403 | <code>[V1OrganizationsServicesQueryApiEndpoints403Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints403_error1.py)</code> |
| 404 | <code>[V1OrganizationsServicesQueryApiEndpoints404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints404_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesQueryApiEndpoints500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_api_endpoint_update(organization_id: UUID, service_id: UUID, endpoint_id: UUID, *, body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1, QueryApiEndpointUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Updates a Query API endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.query_api_endpoints.with_raw_response.query_api_endpoint_update(
    organization_id, service_id, endpoint_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryApiEndpointUpdateErrorBody
```

**Async**

```python
result = await async_client.query_api_endpoints.with_raw_response.query_api_endpoint_update(
    organization_id, service_id, endpoint_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryApiEndpointUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>endpoint_id</code> | <code>UUID</code> | ID of the requested Query API endpoint. |
| <code>body</code> | <code>[PublicQueryApiEndpointRequest](open_api_spec_for_click_house_cloud/models/public_query_api_endpoint_request.py) \| [PublicQueryApiEndpointRequestDict](open_api_spec_for_click_house_cloud/models/public_query_api_endpoint_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id_response1.py), [QueryApiEndpointUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id_response1.py)</code> -- The Query API endpoint was updated.

**On `Failure`**: `error` is <code>[QueryApiEndpointUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId400Error31](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id400_error31.py)</code> |
| 403 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id403_error1.py)</code> |
| 404 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id404_error1.py)</code> |
| 409 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id409_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## RoleManagement

> Source: [RoleManagement](open_api_spec_for_click_house_cloud/apis/role_management.py)

<details>
<summary><code>def organization_role_delete(organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsRolesResponse4, OrganizationRoleDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes an existing custom role. System roles cannot be deleted. This operation will remove the role and all its associated policies.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.role_management.with_raw_response.organization_role_delete(organization_id, role_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsRolesResponse4
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationRoleDeleteErrorBody
```

**Async**

```python
result = await async_client.role_management.with_raw_response.organization_role_delete(organization_id, role_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsRolesResponse4
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationRoleDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>role_id</code> | <code>UUID</code> | ID of the requested role. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsRolesResponse4](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response4.py), [OrganizationRoleDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/organization_role_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsRolesResponse4](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response4.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationRoleDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/organization_role_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsRoles400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles400_error1.py)</code> |
| 500 | <code>[V1OrganizationsRoles500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_role_get(organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsRolesResponse1, OrganizationRoleGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns details for a specific role.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.role_management.with_raw_response.organization_role_get(organization_id, role_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsRolesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationRoleGetErrorBody
```

**Async**

```python
result = await async_client.role_management.with_raw_response.organization_role_get(organization_id, role_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsRolesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationRoleGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>role_id</code> | <code>UUID</code> | ID of the requested role. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsRolesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response1.py), [OrganizationRoleGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_role_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsRolesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationRoleGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_role_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsRoles400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles400_error1.py)</code> |
| 500 | <code>[V1OrganizationsRoles500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_role_patch(organization_id: UUID, role_id: UUID, *, body: RoleUpdateRequest | RoleUpdateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsRolesResponse1, OrganizationRolePatchErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing custom role. System roles cannot be updated. All fields are optional - only provided fields will be updated.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.role_management.with_raw_response.organization_role_patch(organization_id, role_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsRolesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationRolePatchErrorBody
```

**Async**

```python
result = await async_client.role_management.with_raw_response.organization_role_patch(organization_id, role_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsRolesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationRolePatchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>role_id</code> | <code>UUID</code> | ID of the requested role. |
| <code>body</code> | <code>[RoleUpdateRequest](open_api_spec_for_click_house_cloud/models/role_update_request.py) \| [RoleUpdateRequestDict](open_api_spec_for_click_house_cloud/models/role_update_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsRolesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response1.py), [OrganizationRolePatchErrorBody](open_api_spec_for_click_house_cloud/errors/organization_role_patch_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsRolesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationRolePatchErrorBody](open_api_spec_for_click_house_cloud/errors/organization_role_patch_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsRoles400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles400_error1.py)</code> |
| 500 | <code>[V1OrganizationsRoles500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_role_post(organization_id: UUID, *, body: RoleCreateRequest | RoleCreateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsRolesResponse1, OrganizationRolePostErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new custom role for an organization with specified policies and actors.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.role_management.with_raw_response.organization_role_post(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsRolesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationRolePostErrorBody
```

**Async**

```python
result = await async_client.role_management.with_raw_response.organization_role_post(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsRolesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationRolePostErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>body</code> | <code>[RoleCreateRequest](open_api_spec_for_click_house_cloud/models/role_create_request.py) \| [RoleCreateRequestDict](open_api_spec_for_click_house_cloud/models/role_create_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsRolesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response1.py), [OrganizationRolePostErrorBody](open_api_spec_for_click_house_cloud/errors/organization_role_post_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsRolesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationRolePostErrorBody](open_api_spec_for_click_house_cloud/errors/organization_role_post_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsRoles400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles400_error1.py)</code> |
| 500 | <code>[V1OrganizationsRoles500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def organization_roles_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsRolesResponse, OrganizationRolesGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns all available roles (system + custom) for an organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.role_management.with_raw_response.organization_roles_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsRolesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationRolesGetListErrorBody
```

**Async**

```python
result = await async_client.role_management.with_raw_response.organization_roles_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsRolesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OrganizationRolesGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsRolesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response.py), [OrganizationRolesGetListErrorBody](open_api_spec_for_click_house_cloud/errors/organization_roles_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsRolesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[OrganizationRolesGetListErrorBody](open_api_spec_for_click_house_cloud/errors/organization_roles_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsRoles400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles400_error1.py)</code> |
| 500 | <code>[V1OrganizationsRoles500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ServiceApi

> Source: [ServiceApi](open_api_spec_for_click_house_cloud/apis/service_api.py)

<details>
<summary><code>def instance_create(organization_id: UUID, *, body: ServicePostRequest | ServicePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesResponse1, InstanceCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new service in the organization, and returns the current service state and a password to access the service. The service is started asynchronously.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceCreateErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that will own the service. |
| <code>body</code> | <code>[ServicePostRequest](open_api_spec_for_click_house_cloud/models/service_post_request.py) \| [ServicePostRequestDict](open_api_spec_for_click_house_cloud/models/service_post_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response1.py), [InstanceCreateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstanceCreateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServices400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServices500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesResponse4, InstanceDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes the service. The service must be in stopped state and is deleted asynchronously after this method call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_delete(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesResponse4
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceDeleteErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_delete(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesResponse4
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesResponse4](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response4.py), [InstanceDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/instance_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesResponse4](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response4.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstanceDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/instance_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServices400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServices500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesResponse2, InstanceGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a service that belongs to the organization

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceGetErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response2.py), [InstanceGetErrorBody](open_api_spec_for_click_house_cloud/errors/instance_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response2.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstanceGetErrorBody](open_api_spec_for_click_house_cloud/errors/instance_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServices400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServices500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_get_list(organization_id: UUID, *, filter: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesResponse, InstanceGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of all services in the organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceGetListErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>filter</code> | <code>list&#91;str&#93; \| None</code> | Filter criteria to apply when retrieving the resource. Currently, only filtering by resource tags is supported.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response.py), [InstanceGetListErrorBody](open_api_spec_for_click_house_cloud/errors/instance_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstanceGetListErrorBody](open_api_spec_for_click_house_cloud/errors/instance_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServices400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServices500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_password_update(organization_id: UUID, service_id: UUID, *, body: ServicePasswordPatchRequest | ServicePasswordPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesPasswordResponse, InstancePasswordUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sets a new password for the service

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_password_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesPasswordResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstancePasswordUpdateErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_password_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesPasswordResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstancePasswordUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service to update password. |
| <code>body</code> | <code>[ServicePasswordPatchRequest](open_api_spec_for_click_house_cloud/models/service_password_patch_request.py) \| [ServicePasswordPatchRequestDict](open_api_spec_for_click_house_cloud/models/service_password_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesPasswordResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_password_response.py), [InstancePasswordUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_password_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesPasswordResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_password_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstancePasswordUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_password_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesPassword400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_password400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesPassword500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_password500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_private_endpoint_config_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesPrivateEndpointConfigResponse, InstancePrivateEndpointConfigGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Information required to set up a private endpoint

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_private_endpoint_config_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesPrivateEndpointConfigResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstancePrivateEndpointConfigGetErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_private_endpoint_config_get(
    organization_id, service_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesPrivateEndpointConfigResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstancePrivateEndpointConfigGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesPrivateEndpointConfigResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint_config_response.py), [InstancePrivateEndpointConfigGetErrorBody](open_api_spec_for_click_house_cloud/errors/instance_private_endpoint_config_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesPrivateEndpointConfigResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint_config_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstancePrivateEndpointConfigGetErrorBody](open_api_spec_for_click_house_cloud/errors/instance_private_endpoint_config_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesPrivateEndpointConfig400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint_config400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesPrivateEndpointConfig500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint_config500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_private_endpoint_create(organization_id: UUID, service_id: UUID, *, body: ServicPrivateEndpointePostRequest | ServicPrivateEndpointePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesPrivateEndpointResponse, InstancePrivateEndpointCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new private endpoint. The private endpoint will be associated with this service and organization

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_private_endpoint_create(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesPrivateEndpointResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstancePrivateEndpointCreateErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_private_endpoint_create(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesPrivateEndpointResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstancePrivateEndpointCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>body</code> | <code>[ServicPrivateEndpointePostRequest](open_api_spec_for_click_house_cloud/models/servic_private_endpointe_post_request.py) \| [ServicPrivateEndpointePostRequestDict](open_api_spec_for_click_house_cloud/models/servic_private_endpointe_post_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesPrivateEndpointResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint_response.py), [InstancePrivateEndpointCreateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_private_endpoint_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesPrivateEndpointResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstancePrivateEndpointCreateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_private_endpoint_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesPrivateEndpoint400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesPrivateEndpoint500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_query_endpoint_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesServiceQueryEndpointResponse1, InstanceQueryEndpointDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes the service query endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_query_endpoint_delete(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesServiceQueryEndpointResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceQueryEndpointDeleteErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_query_endpoint_delete(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesServiceQueryEndpointResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceQueryEndpointDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesServiceQueryEndpointResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint_response1.py), [InstanceQueryEndpointDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/instance_query_endpoint_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesServiceQueryEndpointResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstanceQueryEndpointDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/instance_query_endpoint_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesServiceQueryEndpoint400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesServiceQueryEndpoint500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_query_endpoint_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesServiceQueryEndpointResponse, InstanceQueryEndpointGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the configuration for the service query endpoint that allows executing queries via API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_query_endpoint_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesServiceQueryEndpointResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceQueryEndpointGetErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_query_endpoint_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesServiceQueryEndpointResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceQueryEndpointGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesServiceQueryEndpointResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint_response.py), [InstanceQueryEndpointGetErrorBody](open_api_spec_for_click_house_cloud/errors/instance_query_endpoint_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesServiceQueryEndpointResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstanceQueryEndpointGetErrorBody](open_api_spec_for_click_house_cloud/errors/instance_query_endpoint_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesServiceQueryEndpoint400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesServiceQueryEndpoint500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_query_endpoint_upsert(organization_id: UUID, service_id: UUID, *, body: InstanceServiceQueryApiEndpointsPostRequest | InstanceServiceQueryApiEndpointsPostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesServiceQueryEndpointResponse, InstanceQueryEndpointUpsertErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create the service query endpoint that allows executing queries via API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_query_endpoint_upsert(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesServiceQueryEndpointResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceQueryEndpointUpsertErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_query_endpoint_upsert(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesServiceQueryEndpointResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceQueryEndpointUpsertErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>body</code> | <code>[InstanceServiceQueryApiEndpointsPostRequest](open_api_spec_for_click_house_cloud/models/instance_service_query_api_endpoints_post_request.py) \| [InstanceServiceQueryApiEndpointsPostRequestDict](open_api_spec_for_click_house_cloud/models/instance_service_query_api_endpoints_post_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesServiceQueryEndpointResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint_response.py), [InstanceQueryEndpointUpsertErrorBody](open_api_spec_for_click_house_cloud/errors/instance_query_endpoint_upsert_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesServiceQueryEndpointResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstanceQueryEndpointUpsertErrorBody](open_api_spec_for_click_house_cloud/errors/instance_query_endpoint_upsert_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesServiceQueryEndpoint400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesServiceQueryEndpoint500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_replica_scaling_update(organization_id: UUID, service_id: UUID, *, body: ServiceReplicaScalingPatchRequest | ServiceReplicaScalingPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesReplicaScalingResponse, InstanceReplicaScalingUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates minimum and maximum memory limits per replica and idle mode scaling behavior for the service. Supports both vertical autoscaling (fixed replica count, variable memory) and horizontal autoscaling (variable replica count, fixed memory). The memory settings are available only for "production" services and must be a multiple of 4 starting from 8GB. For vertical autoscaling, please contact support to enable adjustment of numReplicas. For horizontal autoscaling (autoscalingMode "horizontal" with minReplicas/maxReplicas), contact support to enable the feature for your organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_replica_scaling_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesReplicaScalingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceReplicaScalingUpdateErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_replica_scaling_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesReplicaScalingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceReplicaScalingUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service to update scaling parameters. |
| <code>body</code> | <code>[ServiceReplicaScalingPatchRequest](open_api_spec_for_click_house_cloud/models/service_replica_scaling_patch_request.py) \| [ServiceReplicaScalingPatchRequestDict](open_api_spec_for_click_house_cloud/models/service_replica_scaling_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesReplicaScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_replica_scaling_response.py), [InstanceReplicaScalingUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_replica_scaling_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesReplicaScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_replica_scaling_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstanceReplicaScalingUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_replica_scaling_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesReplicaScaling400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_replica_scaling400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesReplicaScaling500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_replica_scaling500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_scaling_update(organization_id: UUID, service_id: UUID, *, body: ServiceScalingPatchRequest | ServiceScalingPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesScalingResponse, InstanceScalingUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates minimum and maximum total memory limits and idle mode scaling behavior for the service. The memory settings are available only for "production" services and must be a multiple of 12 starting from 24GB. Please contact support to enable adjustment of numReplicas.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_scaling_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesScalingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceScalingUpdateErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_scaling_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesScalingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceScalingUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service to update scaling parameters. |
| <code>body</code> | <code>[ServiceScalingPatchRequest](open_api_spec_for_click_house_cloud/models/service_scaling_patch_request.py) \| [ServiceScalingPatchRequestDict](open_api_spec_for_click_house_cloud/models/service_scaling_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_response.py), [InstanceScalingUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_scaling_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstanceScalingUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_scaling_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesScaling400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesScaling500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_state_update(organization_id: UUID, service_id: UUID, *, body: ServiceStatePatchRequest | ServiceStatePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesStateResponse, InstanceStateUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Starts, stops, or wakes a service. The `start` and `stop` commands require the `control-plane:service:manage` permission on the service. The `awake` command requires only `control-plane:service:view` and applies to an idle service; it does not start a stopped service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_state_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesStateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceStateUpdateErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_state_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesStateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceStateUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service to update state. |
| <code>body</code> | <code>[ServiceStatePatchRequest](open_api_spec_for_click_house_cloud/models/service_state_patch_request.py) \| [ServiceStatePatchRequestDict](open_api_spec_for_click_house_cloud/models/service_state_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesStateResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_state_response.py), [InstanceStateUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_state_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesStateResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_state_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstanceStateUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_state_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesState400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_state400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesState500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_state500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def instance_update(organization_id: UUID, service_id: UUID, *, body: ServicePatchRequest | ServicePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesResponse2, InstanceUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates basic service details like service name or IP access list.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.instance_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceUpdateErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.instance_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InstanceUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service to update. |
| <code>body</code> | <code>[ServicePatchRequest](open_api_spec_for_click_house_cloud/models/service_patch_request.py) \| [ServicePatchRequestDict](open_api_spec_for_click_house_cloud/models/service_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response2.py), [InstanceUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response2.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InstanceUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServices400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServices500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def scaling_schedule_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesScalingScheduleResponse2, ScalingScheduleDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes the autoscaling schedule for a service. If a schedule entry is currently active, the base scaling config is restored to the instance before the schedule is removed. Returns 404 if no schedule exists. Requires the scheduled autoscaling feature to be enabled for the organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.scaling_schedule_delete(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesScalingScheduleResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScalingScheduleDeleteErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.scaling_schedule_delete(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesScalingScheduleResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScalingScheduleDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesScalingScheduleResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule_response2.py), [ScalingScheduleDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/scaling_schedule_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesScalingScheduleResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule_response2.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ScalingScheduleDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/scaling_schedule_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesScalingSchedule400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesScalingSchedule500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def scaling_schedule_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesScalingScheduleResponse, ScalingScheduleGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the autoscaling schedule for a service. Returns 404 if no schedule has been configured or if the schedule was cleared. Requires the scheduled autoscaling feature to be enabled for the organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.scaling_schedule_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesScalingScheduleResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScalingScheduleGetErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.scaling_schedule_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesScalingScheduleResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScalingScheduleGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesScalingScheduleResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule_response.py), [ScalingScheduleGetErrorBody](open_api_spec_for_click_house_cloud/errors/scaling_schedule_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesScalingScheduleResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ScalingScheduleGetErrorBody](open_api_spec_for_click_house_cloud/errors/scaling_schedule_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesScalingSchedule400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesScalingSchedule500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def scaling_schedule_upsert(organization_id: UUID, service_id: UUID, *, body: ScalingSchedulePostRequest | ScalingSchedulePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesScalingScheduleResponse, ScalingScheduleUpsertErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates or fully replaces the autoscaling schedule for a service. Pass an empty `entries` array to clear the schedule — a subsequent GET will return 404, and the response will contain an empty `baseConfig` (all fields absent). The base scaling config (applied when no entry is active) is managed separately via the `replicaScaling` endpoint. Requires the scheduled autoscaling feature to be enabled for the organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.scaling_schedule_upsert(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesScalingScheduleResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScalingScheduleUpsertErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.scaling_schedule_upsert(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesScalingScheduleResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScalingScheduleUpsertErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>body</code> | <code>[ScalingSchedulePostRequest](open_api_spec_for_click_house_cloud/models/scaling_schedule_post_request.py) \| [ScalingSchedulePostRequestDict](open_api_spec_for_click_house_cloud/models/scaling_schedule_post_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesScalingScheduleResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule_response.py), [ScalingScheduleUpsertErrorBody](open_api_spec_for_click_house_cloud/errors/scaling_schedule_upsert_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesScalingScheduleResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ScalingScheduleUpsertErrorBody](open_api_spec_for_click_house_cloud/errors/scaling_schedule_upsert_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesScalingSchedule400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesScalingSchedule500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def service_clickhouse_setting_delete(organization_id: UUID, service_id: UUID, setting_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickhouseSettingsSettingNameResponse1, ServiceClickhouseSettingDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Removes a previously-configured ClickHouse setting, reverting its effective value to the platform default. Settings under `spec.extraConfig.server.*` (e.g. `keep_alive_timeout`, `shared_merge_tree_disable_merges_and_mutations_assignment`) trigger a ClickHouse server rollout restart; other settings propagate to all replicas after a short delay. Deleting a setting that was never configured is a no-op (200 OK).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.service_clickhouse_setting_delete(
    organization_id, service_id, setting_name
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickhouseSettingsSettingNameResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ServiceClickhouseSettingDeleteErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.service_clickhouse_setting_delete(
    organization_id, service_id, setting_name
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickhouseSettingsSettingNameResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ServiceClickhouseSettingDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>setting_name</code> | <code>str</code> | Name of the setting to reset. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickhouseSettingsSettingNameResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name_response1.py), [ServiceClickhouseSettingDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_setting_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickhouseSettingsSettingNameResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ServiceClickhouseSettingDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_setting_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickhouseSettingsSettingName400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickhouseSettingsSettingName500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def service_clickhouse_setting_get(organization_id: UUID, service_id: UUID, setting_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickhouseSettingsSettingNameResponse, ServiceClickhouseSettingGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current value of a ClickHouse setting for the service. Use the [schema endpoint](#tag/Service/operation/serviceClickhouseSettingsSchemaGet) to discover which settings are configurable.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.service_clickhouse_setting_get(organization_id, service_id, setting_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickhouseSettingsSettingNameResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ServiceClickhouseSettingGetErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.service_clickhouse_setting_get(
    organization_id, service_id, setting_name
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickhouseSettingsSettingNameResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ServiceClickhouseSettingGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>setting_name</code> | <code>str</code> | Name of the setting to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickhouseSettingsSettingNameResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name_response.py), [ServiceClickhouseSettingGetErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_setting_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickhouseSettingsSettingNameResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ServiceClickhouseSettingGetErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_setting_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickhouseSettingsSettingName400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickhouseSettingsSettingName500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def service_clickhouse_settings_list_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickhouseSettingsResponse, ServiceClickhouseSettingsListGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the configured ClickHouse settings for the service. Only settings that have been explicitly set are included.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.service_clickhouse_settings_list_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickhouseSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ServiceClickhouseSettingsListGetErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.service_clickhouse_settings_list_get(
    organization_id, service_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickhouseSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ServiceClickhouseSettingsListGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickhouseSettingsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_response.py), [ServiceClickhouseSettingsListGetErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_settings_list_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickhouseSettingsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ServiceClickhouseSettingsListGetErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_settings_list_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickhouseSettings400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickhouseSettings500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def service_clickhouse_settings_schema_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickhouseSettingsSchemaResponse, ServiceClickhouseSettingsSchemaGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the schema of all configurable ClickHouse settings, including types, valid values, descriptions, and warnings.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.service_clickhouse_settings_schema_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickhouseSettingsSchemaResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ServiceClickhouseSettingsSchemaGetErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.service_clickhouse_settings_schema_get(
    organization_id, service_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickhouseSettingsSchemaResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ServiceClickhouseSettingsSchemaGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickhouseSettingsSchemaResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_schema_response.py), [ServiceClickhouseSettingsSchemaGetErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_settings_schema_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickhouseSettingsSchemaResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_schema_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ServiceClickhouseSettingsSchemaGetErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_settings_schema_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickhouseSettingsSchema400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_schema400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickhouseSettingsSchema500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_schema500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def service_clickhouse_settings_update(organization_id: UUID, service_id: UUID, *, body: ServiceClickhouseSettingsPatchRequest | ServiceClickhouseSettingsPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesClickhouseSettingsResponse1, ServiceClickhouseSettingsUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Updates one or more ClickHouse settings for the service. To reset a setting to its platform default, use the [DELETE single setting](#tag/Service/operation/serviceClickhouseSettingDelete) endpoint. Use the [schema endpoint](#tag/Service/operation/serviceClickhouseSettingsSchemaGet) to discover which settings are configurable.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.service_clickhouse_settings_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickhouseSettingsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ServiceClickhouseSettingsUpdateErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.service_clickhouse_settings_update(
    organization_id, service_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesClickhouseSettingsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ServiceClickhouseSettingsUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>body</code> | <code>[ServiceClickhouseSettingsPatchRequest](open_api_spec_for_click_house_cloud/models/service_clickhouse_settings_patch_request.py) \| [ServiceClickhouseSettingsPatchRequestDict](open_api_spec_for_click_house_cloud/models/service_clickhouse_settings_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesClickhouseSettingsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_response1.py), [ServiceClickhouseSettingsUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_settings_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesClickhouseSettingsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ServiceClickhouseSettingsUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_settings_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesClickhouseSettings400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesClickhouseSettings500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def service_profiles_list(organization_id: UUID, *, region_id: str | None = None, byoc_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServiceProfilesResponse, ServiceProfilesListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the custom instance profiles the organization can use in a region. Pass byoc_id to list the profiles configured for a BYOC infrastructure; the region is then taken from the infrastructure and region_id may be omitted. The list is empty when the organization tier does not include custom hardware profiles.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.service_profiles_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServiceProfilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ServiceProfilesListErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.service_profiles_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServiceProfilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ServiceProfilesListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization to list available profiles for. |
| <code>region_id</code> | <code>str \| None</code> | Region to list profiles for, e.g. us-east-1. Required unless byoc_id is set; when both are set it must match the BYOC infrastructure's region.<br>**Default**: <code>None</code> |
| <code>byoc_id</code> | <code>UUID \| None</code> | ID of the BYOC infrastructure to list profiles for. BYOC profiles are only returned when this is set.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServiceProfilesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_service_profiles_response.py), [ServiceProfilesListErrorBody](open_api_spec_for_click_house_cloud/errors/service_profiles_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServiceProfilesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_service_profiles_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[ServiceProfilesListErrorBody](open_api_spec_for_click_house_cloud/errors/service_profiles_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServiceProfiles400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_service_profiles400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServiceProfiles500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_service_profiles500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upgrade_window_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesUpgradeWindowResponse2, UpgradeWindowDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes the upgrade window for a service, restoring the default scheduling behaviour. The upgrade window can only be deleted on primary services. Deletion succeeds even if the organization has lost the scheduled upgrades entitlement, so a window can be cleared after entitlement loss.

Errors:
- 400: the service is a secondary service.
- 401: missing, invalid, or disabled API key.
- 403: caller lacks `control-plane:service:manage` on the service.
- 404: service does not exist, is not visible to the caller, or no upgrade window is configured.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.upgrade_window_delete(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesUpgradeWindowResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpgradeWindowDeleteErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.upgrade_window_delete(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesUpgradeWindowResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpgradeWindowDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesUpgradeWindowResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window_response2.py), [UpgradeWindowDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/upgrade_window_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesUpgradeWindowResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window_response2.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[UpgradeWindowDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/upgrade_window_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesUpgradeWindow400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesUpgradeWindow500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upgrade_window_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesUpgradeWindowResponse, UpgradeWindowGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the configured upgrade window for a service.

Errors:
- 401: missing, invalid, or disabled API key.
- 403: caller lacks `control-plane:service:view` on the service.
- 404: service does not exist, is not visible to the caller, or no upgrade window has been configured.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.upgrade_window_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesUpgradeWindowResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpgradeWindowGetErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.upgrade_window_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesUpgradeWindowResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpgradeWindowGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesUpgradeWindowResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window_response.py), [UpgradeWindowGetErrorBody](open_api_spec_for_click_house_cloud/errors/upgrade_window_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesUpgradeWindowResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[UpgradeWindowGetErrorBody](open_api_spec_for_click_house_cloud/errors/upgrade_window_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesUpgradeWindow400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesUpgradeWindow500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upgrade_window_update(organization_id: UUID, service_id: UUID, *, body: UpgradeWindowPutRequest | UpgradeWindowPutRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesUpgradeWindowResponse, UpgradeWindowUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates or fully replaces the upgrade window for a service. The upgrade window currently lasts 6 hours from `startHourUtc`. The upgrade window can only be set on primary services; secondary services inherit the primary service window.

Errors:
- 400: invalid field values (`weekday` not in 0–6, `startHourUtc` not in {0, 6, 12, 18}), or the service is a secondary service.
- 401: missing, invalid, or disabled API key.
- 403: caller lacks `control-plane:service:manage` on the service, or the organization does not have the scheduled upgrades feature enabled.
- 404: service does not exist or is not visible to the caller.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_api.with_raw_response.upgrade_window_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesUpgradeWindowResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpgradeWindowUpdateErrorBody
```

**Async**

```python
result = await async_client.service_api.with_raw_response.upgrade_window_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesUpgradeWindowResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpgradeWindowUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>body</code> | <code>[UpgradeWindowPutRequest](open_api_spec_for_click_house_cloud/models/upgrade_window_put_request.py) \| [UpgradeWindowPutRequestDict](open_api_spec_for_click_house_cloud/models/upgrade_window_put_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesUpgradeWindowResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window_response.py), [UpgradeWindowUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/upgrade_window_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesUpgradeWindowResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[UpgradeWindowUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/upgrade_window_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesUpgradeWindow400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesUpgradeWindow500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SnapshotApi

> Source: [SnapshotApi](open_api_spec_for_click_house_cloud/apis/snapshot_api.py)

<details>
<summary><code>def snapshot_configuration_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesSnapshotConfigurationResponse, SnapshotConfigurationGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns the service snapshot configuration.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.snapshot_api.with_raw_response.snapshot_configuration_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesSnapshotConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SnapshotConfigurationGetErrorBody
```

**Async**

```python
result = await async_client.snapshot_api.with_raw_response.snapshot_configuration_get(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesSnapshotConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SnapshotConfigurationGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesSnapshotConfigurationResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration_response.py), [SnapshotConfigurationGetErrorBody](open_api_spec_for_click_house_cloud/errors/snapshot_configuration_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesSnapshotConfigurationResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[SnapshotConfigurationGetErrorBody](open_api_spec_for_click_house_cloud/errors/snapshot_configuration_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesSnapshotConfiguration400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesSnapshotConfiguration500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def snapshot_configuration_update(organization_id: UUID, service_id: UUID, *, body: SnapshotConfigurationPatchRequest | SnapshotConfigurationPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesSnapshotConfigurationResponse, SnapshotConfigurationUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Updates the service snapshot configuration. Requires ADMIN auth key role. Enables or disables scheduled snapshots and sets the cadence; when enabled, gap and timeFrame (in minutes) must together be one of the supported (gap, timeFrame) pairs: (30, 1440), (60, 2880). Provide at least one of enabled, gap, timeFrame; omit a field to leave it unchanged (null is not accepted).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.snapshot_api.with_raw_response.snapshot_configuration_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesSnapshotConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SnapshotConfigurationUpdateErrorBody
```

**Async**

```python
result = await async_client.snapshot_api.with_raw_response.snapshot_configuration_update(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesSnapshotConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SnapshotConfigurationUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the service. |
| <code>service_id</code> | <code>UUID</code> | ID of the service. |
| <code>body</code> | <code>[SnapshotConfigurationPatchRequest](open_api_spec_for_click_house_cloud/models/snapshot_configuration_patch_request.py) \| [SnapshotConfigurationPatchRequestDict](open_api_spec_for_click_house_cloud/models/snapshot_configuration_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesSnapshotConfigurationResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration_response.py), [SnapshotConfigurationUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/snapshot_configuration_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesSnapshotConfigurationResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[SnapshotConfigurationUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/snapshot_configuration_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesSnapshotConfiguration400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesSnapshotConfiguration500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def snapshot_get(organization_id: UUID, service_id: UUID, snapshot_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesSnapshotsSnapshotIdResponse, SnapshotGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns a single snapshot info.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.snapshot_api.with_raw_response.snapshot_get(organization_id, service_id, snapshot_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesSnapshotsSnapshotIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SnapshotGetErrorBody
```

**Async**

```python
result = await async_client.snapshot_api.with_raw_response.snapshot_get(organization_id, service_id, snapshot_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesSnapshotsSnapshotIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SnapshotGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the snapshot. |
| <code>service_id</code> | <code>UUID</code> | ID of the service the snapshot was created from. |
| <code>snapshot_id</code> | <code>UUID</code> | ID of the requested snapshot. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesSnapshotsSnapshotIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots_snapshot_id_response.py), [SnapshotGetErrorBody](open_api_spec_for_click_house_cloud/errors/snapshot_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesSnapshotsSnapshotIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots_snapshot_id_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[SnapshotGetErrorBody](open_api_spec_for_click_house_cloud/errors/snapshot_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesSnapshotsSnapshotId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots_snapshot_id400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesSnapshotsSnapshotId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots_snapshot_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def snapshot_get_list(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsServicesSnapshotsResponse, SnapshotGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns a list of all snapshots for the service. The most recent snapshots come first in the list.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.snapshot_api.with_raw_response.snapshot_get_list(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesSnapshotsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SnapshotGetListErrorBody
```

**Async**

```python
result = await async_client.snapshot_api.with_raw_response.snapshot_get_list(organization_id, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsServicesSnapshotsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SnapshotGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that owns the snapshot. |
| <code>service_id</code> | <code>UUID</code> | ID of the service the snapshot was created from. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsServicesSnapshotsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots_response.py), [SnapshotGetListErrorBody](open_api_spec_for_click_house_cloud/errors/snapshot_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsServicesSnapshotsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[SnapshotGetListErrorBody](open_api_spec_for_click_house_cloud/errors/snapshot_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsServicesSnapshots400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots400_error1.py)</code> |
| 500 | <code>[V1OrganizationsServicesSnapshots500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## UdfApi

> Source: [UdfApi](open_api_spec_for_click_house_cloud/apis/udf_api.py)

<details>
<summary><code>def udf_attach(organization_id: UUID, function_name: str, service_id: UUID, *, body: V1OrganizationsUdfsAttachmentsServiceIdRequest | V1OrganizationsUdfsAttachmentsServiceIdRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUdfsAttachmentsServiceIdResponse, UdfAttachErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Attaches one UDF version to a service, replacing the current version when necessary. When version is omitted, the latest ready version is attached.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.udf_api.with_raw_response.udf_attach(organization_id, function_name, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsAttachmentsServiceIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfAttachErrorBody
```

**Async**

```python
result = await async_client.udf_api.with_raw_response.udf_attach(organization_id, function_name, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsAttachmentsServiceIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfAttachErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>function_name</code> | <code>str</code> | Name of the UDF. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>body</code> | <code>[V1OrganizationsUdfsAttachmentsServiceIdRequest](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_request.py) \| [V1OrganizationsUdfsAttachmentsServiceIdRequestDict](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUdfsAttachmentsServiceIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_response.py), [UdfAttachErrorBody](open_api_spec_for_click_house_cloud/errors/udf_attach_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUdfsAttachmentsServiceIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_response.py)</code> -- Current attachment state.

**On `Failure`**: `error` is <code>[UdfAttachErrorBody](open_api_spec_for_click_house_cloud/errors/udf_attach_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUdfsAttachmentsServiceId400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id400_error1.py)</code> |
| 404 | <code>[V1OrganizationsUdfsAttachmentsServiceId404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id404_error1.py)</code> |
| 409 | <code>[V1OrganizationsUdfsAttachmentsServiceId409Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id409_error1.py)</code> |
| 422 | <code>[V1OrganizationsUdfsAttachmentsServiceId422Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id422_error1.py)</code> |
| 424 | <code>[V1OrganizationsUdfsAttachmentsServiceId424Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id424_error1.py)</code> |
| 500 | <code>[V1OrganizationsUdfsAttachmentsServiceId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def udf_attachment_get(organization_id: UUID, function_name: str, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUdfsAttachmentsServiceIdResponse, UdfAttachmentGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current attachment of a UDF to one service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.udf_api.with_raw_response.udf_attachment_get(organization_id, function_name, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsAttachmentsServiceIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfAttachmentGetErrorBody
```

**Async**

```python
result = await async_client.udf_api.with_raw_response.udf_attachment_get(organization_id, function_name, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsAttachmentsServiceIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfAttachmentGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>function_name</code> | <code>str</code> | Name of the UDF. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUdfsAttachmentsServiceIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_response.py), [UdfAttachmentGetErrorBody](open_api_spec_for_click_house_cloud/errors/udf_attachment_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUdfsAttachmentsServiceIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_response.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[UdfAttachmentGetErrorBody](open_api_spec_for_click_house_cloud/errors/udf_attachment_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUdfsAttachmentsServiceId400Error21](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id400_error21.py)</code> |
| 404 | <code>[V1OrganizationsUdfsAttachmentsServiceId404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id404_error1.py)</code> |
| 500 | <code>[V1OrganizationsUdfsAttachmentsServiceId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def udf_attachment_list(organization_id: UUID, function_name: str, *, cursor: str | None = None, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUdfsAttachmentsResponse, UdfAttachmentListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current service attachments for a UDF, with at most one attachment per service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.udf_api.with_raw_response.udf_attachment_list(organization_id, function_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsAttachmentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfAttachmentListErrorBody
```

**Async**

```python
result = await async_client.udf_api.with_raw_response.udf_attachment_list(organization_id, function_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsAttachmentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfAttachmentListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>function_name</code> | <code>str</code> | Name of the UDF. |
| <code>cursor</code> | <code>str \| None</code> | Cursor returned in `pagination.nextCursor` from the previous page.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of records to return per page. Defaults to 100. Maximum is 100.<br>**Default**: <code>100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUdfsAttachmentsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_response.py), [UdfAttachmentListErrorBody](open_api_spec_for_click_house_cloud/errors/udf_attachment_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUdfsAttachmentsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_response.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[UdfAttachmentListErrorBody](open_api_spec_for_click_house_cloud/errors/udf_attachment_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUdfsAttachments400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments400_error1.py)</code> |
| 404 | <code>[V1OrganizationsUdfsAttachments404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments404_error1.py)</code> |
| 500 | <code>[V1OrganizationsUdfsAttachments500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def udf_create(organization_id: UUID, *, body: UdfCreateRequest2 | UdfCreateRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUdfsResponse, UdfCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates a new UDF. See [User-defined functions in Cloud](https://clickhouse.com/docs/products/cloud/features/sql-console-features/user-defined-functions).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.udf_api.with_raw_response.udf_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfCreateErrorBody
```

**Async**

```python
result = await async_client.udf_api.with_raw_response.udf_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>body</code> | <code>[UdfCreateRequest2](open_api_spec_for_click_house_cloud/models/unions/udf_create_request2.py) \| [UdfCreateRequest2Dict](open_api_spec_for_click_house_cloud/models/unions/udf_create_request2.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUdfsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response.py), [UdfCreateErrorBody](open_api_spec_for_click_house_cloud/errors/udf_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUdfsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response.py)</code> -- UDF created and building.

**On `Failure`**: `error` is <code>[UdfCreateErrorBody](open_api_spec_for_click_house_cloud/errors/udf_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUdfs400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs400_error1.py)</code> |
| 403 | <code>[V1OrganizationsUdfs403Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs403_error1.py)</code> |
| 409 | <code>[V1OrganizationsUdfs409Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs409_error1.py)</code> |
| 410 | <code>[V1OrganizationsUdfs410Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs410_error1.py)</code> |
| 500 | <code>[V1OrganizationsUdfs500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def udf_delete(organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUdfsResponse2, UdfDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes every version of a UDF and detaches it from all services. Removal from services completes asynchronously.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.udf_api.with_raw_response.udf_delete(organization_id, function_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfDeleteErrorBody
```

**Async**

```python
result = await async_client.udf_api.with_raw_response.udf_delete(organization_id, function_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>function_name</code> | <code>str</code> | Name of the UDF. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUdfsResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response2.py), [UdfDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/udf_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUdfsResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response2.py)</code> -- UDF deleted.

**On `Failure`**: `error` is <code>[UdfDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/udf_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUdfs400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs400_error1.py)</code> |
| 404 | <code>[V1OrganizationsUdfs404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs404_error1.py)</code> |
| 409 | <code>[V1OrganizationsUdfs409Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs409_error1.py)</code> |
| 500 | <code>[V1OrganizationsUdfs500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def udf_detach(organization_id: UUID, function_name: str, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUdfsAttachmentsServiceIdResponse2, UdfDetachErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Detaches a UDF from a service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.udf_api.with_raw_response.udf_detach(organization_id, function_name, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsAttachmentsServiceIdResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfDetachErrorBody
```

**Async**

```python
result = await async_client.udf_api.with_raw_response.udf_detach(organization_id, function_name, service_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsAttachmentsServiceIdResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfDetachErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>function_name</code> | <code>str</code> | Name of the UDF. |
| <code>service_id</code> | <code>UUID</code> | ID of the requested service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUdfsAttachmentsServiceIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_response2.py), [UdfDetachErrorBody](open_api_spec_for_click_house_cloud/errors/udf_detach_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUdfsAttachmentsServiceIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_response2.py)</code> -- UDF detached.

**On `Failure`**: `error` is <code>[UdfDetachErrorBody](open_api_spec_for_click_house_cloud/errors/udf_detach_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUdfsAttachmentsServiceId400Error21](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id400_error21.py)</code> |
| 404 | <code>[V1OrganizationsUdfsAttachmentsServiceId404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id404_error1.py)</code> |
| 409 | <code>[V1OrganizationsUdfsAttachmentsServiceId409Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id409_error1.py)</code> |
| 500 | <code>[V1OrganizationsUdfsAttachmentsServiceId500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def udf_get(organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUdfsResponse, UdfGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the latest version of a UDF.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.udf_api.with_raw_response.udf_get(organization_id, function_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfGetErrorBody
```

**Async**

```python
result = await async_client.udf_api.with_raw_response.udf_get(organization_id, function_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>function_name</code> | <code>str</code> | Name of the UDF. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUdfsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response.py), [UdfGetErrorBody](open_api_spec_for_click_house_cloud/errors/udf_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUdfsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[UdfGetErrorBody](open_api_spec_for_click_house_cloud/errors/udf_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUdfs400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs400_error1.py)</code> |
| 404 | <code>[V1OrganizationsUdfs404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs404_error1.py)</code> |
| 500 | <code>[V1OrganizationsUdfs500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def udf_list(organization_id: UUID, *, cursor: str | None = None, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUdfsResponse1, UdfListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the latest version of each UDF in the organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.udf_api.with_raw_response.udf_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfListErrorBody
```

**Async**

```python
result = await async_client.udf_api.with_raw_response.udf_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>cursor</code> | <code>str \| None</code> | Cursor returned in `pagination.nextCursor` from the previous page.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of records to return per page. Defaults to 100. Maximum is 100.<br>**Default**: <code>100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUdfsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response1.py), [UdfListErrorBody](open_api_spec_for_click_house_cloud/errors/udf_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUdfsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response1.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[UdfListErrorBody](open_api_spec_for_click_house_cloud/errors/udf_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUdfs400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs400_error1.py)</code> |
| 500 | <code>[V1OrganizationsUdfs500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def udf_upload_session_create(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUdfUploadsUrlResponse, UdfUploadSessionCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates an org-scoped presigned application/zip upload URL. Callers must use an upload ID for only one create or version attempt and request a new upload URL when retrying.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.udf_api.with_raw_response.udf_upload_session_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfUploadsUrlResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfUploadSessionCreateErrorBody
```

**Async**

```python
result = await async_client.udf_api.with_raw_response.udf_upload_session_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfUploadsUrlResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfUploadSessionCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUdfUploadsUrlResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udf_uploads_url_response.py), [UdfUploadSessionCreateErrorBody](open_api_spec_for_click_house_cloud/errors/udf_upload_session_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUdfUploadsUrlResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udf_uploads_url_response.py)</code> -- Upload URL created.

**On `Failure`**: `error` is <code>[UdfUploadSessionCreateErrorBody](open_api_spec_for_click_house_cloud/errors/udf_upload_session_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUdfUploadsUrl400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udf_uploads_url400_error1.py)</code> |
| 500 | <code>[V1OrganizationsUdfUploadsUrl500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udf_uploads_url500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def udf_version_create(organization_id: UUID, function_name: str, *, body: UdfVersionCreateRequest2 | UdfVersionCreateRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUdfsVersionsResponse, UdfVersionCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Consumes a source archive, assigns a version, and starts the UDF build. Optional configuration fields omitted from the request use the defaults documented in the request schema; values are not inherited from the previous version. Retry by requesting a new upload URL and re-uploading.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.udf_api.with_raw_response.udf_version_create(organization_id, function_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsVersionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfVersionCreateErrorBody
```

**Async**

```python
result = await async_client.udf_api.with_raw_response.udf_version_create(organization_id, function_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsVersionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfVersionCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>function_name</code> | <code>str</code> | Name of the UDF. |
| <code>body</code> | <code>[UdfVersionCreateRequest2](open_api_spec_for_click_house_cloud/models/unions/udf_version_create_request2.py) \| [UdfVersionCreateRequest2Dict](open_api_spec_for_click_house_cloud/models/unions/udf_version_create_request2.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUdfsVersionsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_response.py), [UdfVersionCreateErrorBody](open_api_spec_for_click_house_cloud/errors/udf_version_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUdfsVersionsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_response.py)</code> -- UDF version created and building.

**On `Failure`**: `error` is <code>[UdfVersionCreateErrorBody](open_api_spec_for_click_house_cloud/errors/udf_version_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUdfsVersions400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions400_error1.py)</code> |
| 403 | <code>[V1OrganizationsUdfsVersions403Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions403_error1.py)</code> |
| 404 | <code>[V1OrganizationsUdfsVersions404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions404_error1.py)</code> |
| 409 | <code>[V1OrganizationsUdfsVersions409Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions409_error1.py)</code> |
| 410 | <code>[V1OrganizationsUdfsVersions410Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions410_error1.py)</code> |
| 500 | <code>[V1OrganizationsUdfsVersions500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def udf_version_delete(organization_id: UUID, function_name: str, version: int, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUdfsVersionsVersionResponse, UdfVersionDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes a UDF version. The UDF must not be attached to any services.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.udf_api.with_raw_response.udf_version_delete(organization_id, function_name, version)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsVersionsVersionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfVersionDeleteErrorBody
```

**Async**

```python
result = await async_client.udf_api.with_raw_response.udf_version_delete(organization_id, function_name, version)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsVersionsVersionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfVersionDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>function_name</code> | <code>str</code> | Name of the UDF. |
| <code>version</code> | <code>int</code> | Version number of the UDF. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUdfsVersionsVersionResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_version_response.py), [UdfVersionDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/udf_version_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUdfsVersionsVersionResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_version_response.py)</code> -- UDF version deleted.

**On `Failure`**: `error` is <code>[UdfVersionDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/udf_version_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUdfsVersionsVersion400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_version400_error1.py)</code> |
| 404 | <code>[V1OrganizationsUdfsVersionsVersion404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_version404_error1.py)</code> |
| 409 | <code>[V1OrganizationsUdfsVersionsVersion409Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_version409_error1.py)</code> |
| 500 | <code>[V1OrganizationsUdfsVersionsVersion500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_version500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def udf_version_list(organization_id: UUID, function_name: str, *, cursor: str | None = None, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsUdfsVersionsResponse1, UdfVersionListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns all versions of a UDF.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.udf_api.with_raw_response.udf_version_list(organization_id, function_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsVersionsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfVersionListErrorBody
```

**Async**

```python
result = await async_client.udf_api.with_raw_response.udf_version_list(organization_id, function_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsUdfsVersionsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UdfVersionListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>function_name</code> | <code>str</code> | Name of the UDF. |
| <code>cursor</code> | <code>str \| None</code> | Cursor returned in `pagination.nextCursor` from the previous page.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of records to return per page. Defaults to 100. Maximum is 100.<br>**Default**: <code>100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsUdfsVersionsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_response1.py), [UdfVersionListErrorBody](open_api_spec_for_click_house_cloud/errors/udf_version_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsUdfsVersionsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_response1.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[UdfVersionListErrorBody](open_api_spec_for_click_house_cloud/errors/udf_version_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsUdfsVersions400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions400_error1.py)</code> |
| 404 | <code>[V1OrganizationsUdfsVersions404Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions404_error1.py)</code> |
| 500 | <code>[V1OrganizationsUdfsVersions500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## UserManagement

> Source: [UserManagement](open_api_spec_for_click_house_cloud/apis/user_management.py)

<details>
<summary><code>def invitation_create(organization_id: UUID, *, body: InvitationPostRequest | InvitationPostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsInvitationsResponse1, InvitationCreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates organization invitation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_management.with_raw_response.invitation_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsInvitationsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InvitationCreateErrorBody
```

**Async**

```python
result = await async_client.user_management.with_raw_response.invitation_create(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsInvitationsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InvitationCreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization to invite a user to. |
| <code>body</code> | <code>[InvitationPostRequest](open_api_spec_for_click_house_cloud/models/invitation_post_request.py) \| [InvitationPostRequestDict](open_api_spec_for_click_house_cloud/models/invitation_post_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsInvitationsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response1.py), [InvitationCreateErrorBody](open_api_spec_for_click_house_cloud/errors/invitation_create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsInvitationsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InvitationCreateErrorBody](open_api_spec_for_click_house_cloud/errors/invitation_create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsInvitations400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations400_error1.py)</code> |
| 500 | <code>[V1OrganizationsInvitations500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def invitation_delete(organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsInvitationsResponse3, InvitationDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a single organization invitation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_management.with_raw_response.invitation_delete(organization_id, invitation_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsInvitationsResponse3
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InvitationDeleteErrorBody
```

**Async**

```python
result = await async_client.user_management.with_raw_response.invitation_delete(organization_id, invitation_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsInvitationsResponse3
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InvitationDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization that has the invitation. |
| <code>invitation_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsInvitationsResponse3](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response3.py), [InvitationDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/invitation_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsInvitationsResponse3](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response3.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InvitationDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/invitation_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsInvitations400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations400_error1.py)</code> |
| 500 | <code>[V1OrganizationsInvitations500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def invitation_get(organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsInvitationsResponse1, InvitationGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns details for a single organization invitation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_management.with_raw_response.invitation_get(organization_id, invitation_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsInvitationsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InvitationGetErrorBody
```

**Async**

```python
result = await async_client.user_management.with_raw_response.invitation_get(organization_id, invitation_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsInvitationsResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InvitationGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>invitation_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsInvitationsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response1.py), [InvitationGetErrorBody](open_api_spec_for_click_house_cloud/errors/invitation_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsInvitationsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InvitationGetErrorBody](open_api_spec_for_click_house_cloud/errors/invitation_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsInvitations400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations400_error1.py)</code> |
| 500 | <code>[V1OrganizationsInvitations500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def invitation_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsInvitationsResponse, InvitationGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns list of all organization invitations.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_management.with_raw_response.invitation_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsInvitationsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InvitationGetListErrorBody
```

**Async**

```python
result = await async_client.user_management.with_raw_response.invitation_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsInvitationsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InvitationGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsInvitationsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response.py), [InvitationGetListErrorBody](open_api_spec_for_click_house_cloud/errors/invitation_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsInvitationsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[InvitationGetListErrorBody](open_api_spec_for_click_house_cloud/errors/invitation_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsInvitations400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations400_error1.py)</code> |
| 500 | <code>[V1OrganizationsInvitations500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def member_delete(organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsMembersResponse3, MemberDeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a user from the organization

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_management.with_raw_response.member_delete(organization_id, user_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsMembersResponse3
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type MemberDeleteErrorBody
```

**Async**

```python
result = await async_client.user_management.with_raw_response.member_delete(organization_id, user_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsMembersResponse3
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type MemberDeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>user_id</code> | <code>UUID</code> | ID of the requested user. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsMembersResponse3](open_api_spec_for_click_house_cloud/models/v1_organizations_members_response3.py), [MemberDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/member_delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsMembersResponse3](open_api_spec_for_click_house_cloud/models/v1_organizations_members_response3.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[MemberDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/member_delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsMembers400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_members400_error1.py)</code> |
| 500 | <code>[V1OrganizationsMembers500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_members500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def member_get(organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsMembersResponse1, MemberGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single organization member details.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_management.with_raw_response.member_get(organization_id, user_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsMembersResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type MemberGetErrorBody
```

**Async**

```python
result = await async_client.user_management.with_raw_response.member_get(organization_id, user_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsMembersResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type MemberGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization the member is part of. |
| <code>user_id</code> | <code>UUID</code> | ID of the requested user. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsMembersResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_members_response1.py), [MemberGetErrorBody](open_api_spec_for_click_house_cloud/errors/member_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsMembersResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_members_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[MemberGetErrorBody](open_api_spec_for_click_house_cloud/errors/member_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsMembers400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_members400_error1.py)</code> |
| 500 | <code>[V1OrganizationsMembers500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_members500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def member_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsMembersResponse, MemberGetListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of all members in the organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_management.with_raw_response.member_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsMembersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type MemberGetListErrorBody
```

**Async**

```python
result = await async_client.user_management.with_raw_response.member_get_list(organization_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsMembersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type MemberGetListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the requested organization. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsMembersResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_members_response.py), [MemberGetListErrorBody](open_api_spec_for_click_house_cloud/errors/member_get_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsMembersResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_members_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[MemberGetListErrorBody](open_api_spec_for_click_house_cloud/errors/member_get_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsMembers400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_members400_error1.py)</code> |
| 500 | <code>[V1OrganizationsMembers500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_members500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def member_update(organization_id: UUID, user_id: UUID, *, body: MemberPatchRequest | MemberPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1OrganizationsMembersResponse1, MemberUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates organization member role.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user_management.with_raw_response.member_update(organization_id, user_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsMembersResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type MemberUpdateErrorBody
```

**Async**

```python
result = await async_client.user_management.with_raw_response.member_update(organization_id, user_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1OrganizationsMembersResponse1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type MemberUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>organization_id</code> | <code>UUID</code> | ID of the organization the member is part of. |
| <code>user_id</code> | <code>UUID</code> | ID of the user to patch |
| <code>body</code> | <code>[MemberPatchRequest](open_api_spec_for_click_house_cloud/models/member_patch_request.py) \| [MemberPatchRequestDict](open_api_spec_for_click_house_cloud/models/member_patch_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](open_api_spec_for_click_house_cloud/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](open_api_spec_for_click_house_cloud/core/results.py)&#91;[V1OrganizationsMembersResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_members_response1.py), [MemberUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/member_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1OrganizationsMembersResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_members_response1.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[MemberUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/member_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[V1OrganizationsMembers400Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_members400_error1.py)</code> |
| 500 | <code>[V1OrganizationsMembers500Error1](open_api_spec_for_click_house_cloud/models/v1_organizations_members500_error1.py)</code> |
| anything unmapped | <code>[RawError](open_api_spec_for_click_house_cloud/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

