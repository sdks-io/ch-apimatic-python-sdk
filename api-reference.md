# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [OpenApiSpecForClickHouseCloudClient](open_api_spec_for_click_house_cloud/client.py)

## ApiKeys

> Source: [ApiKeys](open_api_spec_for_click_house_cloud/apis/api_keys.py)

<details>
<summary><code>def openapi_key_create(organization_id: UUID, *, body: ApiKeyPostRequest | ApiKeyPostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsKeysResponse1</code></summary>

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
try:
    response = client.api_keys.openapi_key_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsKeysResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OpenapiKeyCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.api_keys.openapi_key_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsKeysResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OpenapiKeyCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsKeysResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OpenapiKeyCreateErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_create_error.py)&#93;</code>

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
<summary><code>def openapi_key_delete(organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsKeysResponse4</code></summary>

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
try:
    response = client.api_keys.openapi_key_delete(organization_id, key_id)
    # TODO: Handle 'response' of type V1OrganizationsKeysResponse4
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OpenapiKeyDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.api_keys.openapi_key_delete(organization_id, key_id)
    # TODO: Handle 'response' of type V1OrganizationsKeysResponse4
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OpenapiKeyDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsKeysResponse4](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response4.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OpenapiKeyDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_delete_error.py)&#93;</code>

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
<summary><code>def openapi_key_get(organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsKeysResponse2</code></summary>

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
try:
    response = client.api_keys.openapi_key_get(organization_id, key_id)
    # TODO: Handle 'response' of type V1OrganizationsKeysResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OpenapiKeyGetErrorBody
```

**Async**

```python
try:
    response = await async_client.api_keys.openapi_key_get(organization_id, key_id)
    # TODO: Handle 'response' of type V1OrganizationsKeysResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OpenapiKeyGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsKeysResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response2.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OpenapiKeyGetErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_get_error.py)&#93;</code>

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
<summary><code>def openapi_key_get_list(organization_id: UUID, *, limit: int | None = 250, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsKeysResponse</code></summary>

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
try:
    response = client.api_keys.openapi_key_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsKeysResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OpenapiKeyGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.api_keys.openapi_key_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsKeysResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OpenapiKeyGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsKeysResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OpenapiKeyGetListErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_get_list_error.py)&#93;</code>

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
<summary><code>def openapi_key_update(organization_id: UUID, key_id: UUID, *, body: ApiKeyPatchRequest | ApiKeyPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsKeysResponse2</code></summary>

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
try:
    response = client.api_keys.openapi_key_update(organization_id, key_id)
    # TODO: Handle 'response' of type V1OrganizationsKeysResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OpenapiKeyUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.api_keys.openapi_key_update(organization_id, key_id)
    # TODO: Handle 'response' of type V1OrganizationsKeysResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OpenapiKeyUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsKeysResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response2.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OpenapiKeyUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/openapi_key_update_error.py)&#93;</code>

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
<summary><code>def backup_bucket_create(organization_id: UUID, service_id: UUID, *, body: BackupBucketPostRequest | BackupBucketPostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesBackupBucketResponse</code></summary>

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
try:
    response = client.backup_api.backup_bucket_create(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupBucketResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupBucketCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.backup_api.backup_bucket_create(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupBucketResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupBucketCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesBackupBucketResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[BackupBucketCreateErrorBody](open_api_spec_for_click_house_cloud/errors/backup_bucket_create_error.py)&#93;</code>

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
<summary><code>def backup_bucket_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesBackupBucketResponse3</code></summary>

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
try:
    response = client.backup_api.backup_bucket_delete(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupBucketResponse3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupBucketDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.backup_api.backup_bucket_delete(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupBucketResponse3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupBucketDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesBackupBucketResponse3](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response3.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[BackupBucketDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/backup_bucket_delete_error.py)&#93;</code>

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
<summary><code>def backup_bucket_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesBackupBucketResponse</code></summary>

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
try:
    response = client.backup_api.backup_bucket_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupBucketResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupBucketGetErrorBody
```

**Async**

```python
try:
    response = await async_client.backup_api.backup_bucket_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupBucketResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupBucketGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesBackupBucketResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[BackupBucketGetErrorBody](open_api_spec_for_click_house_cloud/errors/backup_bucket_get_error.py)&#93;</code>

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
<summary><code>def backup_bucket_update(organization_id: UUID, service_id: UUID, *, body: BackupBucketPatchRequest | BackupBucketPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesBackupBucketResponse</code></summary>

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
try:
    response = client.backup_api.backup_bucket_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupBucketResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupBucketUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.backup_api.backup_bucket_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupBucketResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupBucketUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesBackupBucketResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[BackupBucketUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/backup_bucket_update_error.py)&#93;</code>

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
<summary><code>def backup_configuration_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesBackupConfigurationResponse</code></summary>

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
try:
    response = client.backup_api.backup_configuration_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupConfigurationGetErrorBody
```

**Async**

```python
try:
    response = await async_client.backup_api.backup_configuration_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupConfigurationGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesBackupConfigurationResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[BackupConfigurationGetErrorBody](open_api_spec_for_click_house_cloud/errors/backup_configuration_get_error.py)&#93;</code>

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
<summary><code>def backup_configuration_update(organization_id: UUID, service_id: UUID, *, body: BackupConfigurationPatchRequest | BackupConfigurationPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesBackupConfigurationResponse</code></summary>

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
try:
    response = client.backup_api.backup_configuration_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupConfigurationUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.backup_api.backup_configuration_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupConfigurationUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesBackupConfigurationResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[BackupConfigurationUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/backup_configuration_update_error.py)&#93;</code>

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
<summary><code>def backup_get(organization_id: UUID, service_id: UUID, backup_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesBackupsBackupIdResponse</code></summary>

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
try:
    response = client.backup_api.backup_get(organization_id, service_id, backup_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupsBackupIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupGetErrorBody
```

**Async**

```python
try:
    response = await async_client.backup_api.backup_get(organization_id, service_id, backup_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupsBackupIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesBackupsBackupIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups_backup_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[BackupGetErrorBody](open_api_spec_for_click_house_cloud/errors/backup_get_error.py)&#93;</code>

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
<summary><code>def backup_get_list(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesBackupsResponse</code></summary>

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
try:
    response = client.backup_api.backup_get_list(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.backup_api.backup_get_list(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesBackupsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BackupGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesBackupsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[BackupGetListErrorBody](open_api_spec_for_click_house_cloud/errors/backup_get_list_error.py)&#93;</code>

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
<summary><code>def active_balances_get(organization_id: UUID, *, limit: int | None = 100, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsActiveBalancesResponse</code></summary>

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
try:
    response = client.billing.active_balances_get(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsActiveBalancesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActiveBalancesGetErrorBody
```

**Async**

```python
try:
    response = await async_client.billing.active_balances_get(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsActiveBalancesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActiveBalancesGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsActiveBalancesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_active_balances_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ActiveBalancesGetErrorBody](open_api_spec_for_click_house_cloud/errors/active_balances_get_error.py)&#93;</code>

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
<summary><code>def credit_balances_get(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsCreditBalancesResponse</code></summary>

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
try:
    response = client.billing.credit_balances_get(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsCreditBalancesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreditBalancesGetErrorBody
```

**Async**

```python
try:
    response = await async_client.billing.credit_balances_get(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsCreditBalancesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreditBalancesGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsCreditBalancesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_credit_balances_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[CreditBalancesGetErrorBody](open_api_spec_for_click_house_cloud/errors/credit_balances_get_error.py)&#93;</code>

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
<summary><code>def usage_cost_get(organization_id: UUID, from_date: Date, to_date: Date, *, filter: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUsageCostResponse</code></summary>

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
try:
    response = client.billing.usage_cost_get(organization_id, from_date, to_date)
    # TODO: Handle 'response' of type V1OrganizationsUsageCostResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UsageCostGetErrorBody
```

**Async**

```python
try:
    response = await async_client.billing.usage_cost_get(organization_id, from_date, to_date)
    # TODO: Handle 'response' of type V1OrganizationsUsageCostResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UsageCostGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUsageCostResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_usage_cost_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UsageCostGetErrorBody](open_api_spec_for_click_house_cloud/errors/usage_cost_get_error.py)&#93;</code>

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
<summary><code>def click_pipe_cdc_scaling_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesCdcScalingResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_cdc_scaling_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesCdcScalingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeCdcScalingGetErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_cdc_scaling_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesCdcScalingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeCdcScalingGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesCdcScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeCdcScalingGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_cdc_scaling_get_error.py)&#93;</code>

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
<summary><code>def click_pipe_cdc_scaling_update(organization_id: UUID, service_id: UUID, *, body: ClickPipesCdcScalingPatchRequest | ClickPipesCdcScalingPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesCdcScalingResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_cdc_scaling_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesCdcScalingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeCdcScalingUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_cdc_scaling_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesCdcScalingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeCdcScalingUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesCdcScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeCdcScalingUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_cdc_scaling_update_error.py)&#93;</code>

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
<summary><code>def click_pipe_create(organization_id: UUID, service_id: UUID, *, body: ClickPipePostRequest | ClickPipePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesResponse1</code></summary>

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
try:
    response = client.click_pipes.click_pipe_create(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_create(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeCreateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_create_error.py)&#93;</code>

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
<summary><code>def click_pipe_delete(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesClickPipeIdResponse2</code></summary>

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
try:
    response = client.click_pipes.click_pipe_delete(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_delete(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesClickPipeIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_response2.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_delete_error.py)&#93;</code>

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
<summary><code>def click_pipe_get(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesClickPipeIdResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_get(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeGetErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_get(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesClickPipeIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_get_error.py)&#93;</code>

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
<summary><code>def click_pipe_get_list(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_get_list(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_get_list(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeGetListErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_get_list_error.py)&#93;</code>

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
<summary><code>def click_pipe_reverse_private_endpoint_create(organization_id: UUID, service_id: UUID, *, body: CreateReversePrivateEndpoint | CreateReversePrivateEndpointDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1</code></summary>

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
try:
    response = client.click_pipes.click_pipe_reverse_private_endpoint_create(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeReversePrivateEndpointCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_reverse_private_endpoint_create(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeReversePrivateEndpointCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeReversePrivateEndpointCreateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_create_error.py)&#93;</code>

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
<summary><code>def click_pipe_reverse_private_endpoint_delete(organization_id: UUID, service_id: UUID, reverse_private_endpoint_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1</code></summary>

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
try:
    response = client.click_pipes.click_pipe_reverse_private_endpoint_delete(
        organization_id, service_id, reverse_private_endpoint_id
    )
    # TODO: Handle 'response' of type
    # V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeReversePrivateEndpointDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_reverse_private_endpoint_delete(
        organization_id, service_id, reverse_private_endpoint_id
    )
    # TODO: Handle 'response' of type
    # V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeReversePrivateEndpointDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeReversePrivateEndpointDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_delete_error.py)&#93;</code>

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
<summary><code>def click_pipe_reverse_private_endpoint_get(organization_id: UUID, service_id: UUID, reverse_private_endpoint_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_reverse_private_endpoint_get(
        organization_id, service_id, reverse_private_endpoint_id
    )
    # TODO: Handle 'response' of type
    # V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeReversePrivateEndpointGetErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_reverse_private_endpoint_get(
        organization_id, service_id, reverse_private_endpoint_id
    )
    # TODO: Handle 'response' of type
    # V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeReversePrivateEndpointGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeReversePrivateEndpointGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_get_error.py)&#93;</code>

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
<summary><code>def click_pipe_reverse_private_endpoint_get_list(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_reverse_private_endpoint_get_list(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeReversePrivateEndpointGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_reverse_private_endpoint_get_list(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeReversePrivateEndpointGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeReversePrivateEndpointGetListErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_get_list_error.py)&#93;</code>

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
<summary><code>def click_pipe_reverse_private_endpoint_update(organization_id: UUID, service_id: UUID, reverse_private_endpoint_id: UUID, *, body: UpdateReversePrivateEndpoint | UpdateReversePrivateEndpointDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_reverse_private_endpoint_update(
        organization_id, service_id, reverse_private_endpoint_id
    )
    # TODO: Handle 'response' of type
    # V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeReversePrivateEndpointUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_reverse_private_endpoint_update(
        organization_id, service_id, reverse_private_endpoint_id
    )
    # TODO: Handle 'response' of type
    # V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeReversePrivateEndpointUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeReversePrivateEndpointUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_update_error.py)&#93;</code>

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
<summary><code>def click_pipe_scaling_update(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, body: ClickPipeScalingPatchRequest | ClickPipeScalingPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesClickPipeIdScalingResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_scaling_update(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdScalingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeScalingUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_scaling_update(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdScalingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeScalingUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesClickPipeIdScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_scaling_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeScalingUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_scaling_update_error.py)&#93;</code>

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
<summary><code>def click_pipe_schema_discovery(organization_id: UUID, service_id: UUID, *, body: ClickPipeSchemaDiscoveryRequest | ClickPipeSchemaDiscoveryRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesSchemaDiscoveryResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_schema_discovery(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesSchemaDiscoveryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeSchemaDiscoveryErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_schema_discovery(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesSchemaDiscoveryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeSchemaDiscoveryErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesSchemaDiscoveryResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_schema_discovery_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeSchemaDiscoveryErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_schema_discovery_error.py)&#93;</code>

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
<summary><code>def click_pipe_settings_get(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_settings_get(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeSettingsGetErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_settings_get(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeSettingsGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeSettingsGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_settings_get_error.py)&#93;</code>

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
<summary><code>def click_pipe_settings_update(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, body: ClickPipeSettingsPutRequest | ClickPipeSettingsPutRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_settings_update(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeSettingsUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_settings_update(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeSettingsUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeSettingsUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_settings_update_error.py)&#93;</code>

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
<summary><code>def click_pipe_state_update(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, body: ClickPipeStatePatchRequest | ClickPipeStatePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesClickPipeIdStateResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_state_update(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdStateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeStateUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_state_update(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdStateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeStateUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesClickPipeIdStateResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_state_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeStateUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_state_update_error.py)&#93;</code>

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
<summary><code>def click_pipe_update(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, body: ClickPipePatchRequest | ClickPipePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesClickPipeIdResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipe_update(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipe_update(organization_id, service_id, click_pipe_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesClickPipeIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipeUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesClickPipeIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipeUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipe_update_error.py)&#93;</code>

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
<summary><code>def click_pipes_service_context_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickpipesContextResponse</code></summary>

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
try:
    response = client.click_pipes.click_pipes_service_context_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesContextResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipesServiceContextGetErrorBody
```

**Async**

```python
try:
    response = await async_client.click_pipes.click_pipes_service_context_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickpipesContextResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickPipesServiceContextGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickpipesContextResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_context_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickPipesServiceContextGetErrorBody](open_api_spec_for_click_house_cloud/errors/click_pipes_service_context_get_error.py)&#93;</code>

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
<summary><code>def click_stack_create_alert(organization_id: UUID, service_id: UUID, *, body: ClickStackCreateAlertRequest | ClickStackCreateAlertRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackAlertsResponse1</code></summary>

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
try:
    response = client.click_stack.click_stack_create_alert(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackAlertsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackCreateAlertErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_create_alert(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackAlertsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackCreateAlertErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackAlertsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackCreateAlertErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_alert_error.py)&#93;</code>

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
<summary><code>def click_stack_create_dashboard(organization_id: UUID, service_id: UUID, *, body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackDashboardsResponse1</code></summary>

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
try:
    response = client.click_stack.click_stack_create_dashboard(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackDashboardsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackCreateDashboardErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_create_dashboard(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackDashboardsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackCreateDashboardErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackDashboardsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackCreateDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_dashboard_error.py)&#93;</code>

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
<summary><code>def click_stack_create_role(organization_id: UUID, service_id: UUID, *, body: ClickStackCreateRoleRequest | ClickStackCreateRoleRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackRolesResponse1</code></summary>

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
try:
    response = client.click_stack.click_stack_create_role(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackRolesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackCreateRoleErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_create_role(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackRolesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackCreateRoleErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackRolesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackCreateRoleErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_role_error.py)&#93;</code>

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
<summary><code>def click_stack_create_saved_search(organization_id: UUID, service_id: UUID, *, body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackSavedSearchesResponse1</code></summary>

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
try:
    response = client.click_stack.click_stack_create_saved_search(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSavedSearchesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackCreateSavedSearchErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_create_saved_search(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSavedSearchesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackCreateSavedSearchErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackSavedSearchesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackCreateSavedSearchErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_saved_search_error.py)&#93;</code>

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
<summary><code>def click_stack_create_source(organization_id: UUID, service_id: UUID, *, body: ClickStackSource | ClickStackSourceDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackSourcesResponse1</code></summary>

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
try:
    response = client.click_stack.click_stack_create_source(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSourcesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackCreateSourceErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_create_source(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSourcesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackCreateSourceErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackSourcesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackCreateSourceErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_source_error.py)&#93;</code>

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
<summary><code>def click_stack_create_webhook(organization_id: UUID, service_id: UUID, *, body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackWebhooksResponse1</code></summary>

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
try:
    response = client.click_stack.click_stack_create_webhook(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackWebhooksResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackCreateWebhookErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_create_webhook(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackWebhooksResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackCreateWebhookErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackWebhooksResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackCreateWebhookErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_create_webhook_error.py)&#93;</code>

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
<summary><code>def click_stack_delete_alert(organization_id: UUID, service_id: UUID, click_stack_alert_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2</code></summary>

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
try:
    response = client.click_stack.click_stack_delete_alert(organization_id, service_id, click_stack_alert_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackDeleteAlertErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_delete_alert(
        organization_id, service_id, click_stack_alert_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackDeleteAlertErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id_response2.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackDeleteAlertErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_alert_error.py)&#93;</code>

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
<summary><code>def click_stack_delete_dashboard(organization_id: UUID, service_id: UUID, click_stack_dashboard_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2</code></summary>

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
try:
    response = client.click_stack.click_stack_delete_dashboard(organization_id, service_id, click_stack_dashboard_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackDeleteDashboardErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_delete_dashboard(
        organization_id, service_id, click_stack_dashboard_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackDeleteDashboardErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response2.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackDeleteDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_dashboard_error.py)&#93;</code>

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
<summary><code>def click_stack_delete_role(organization_id: UUID, service_id: UUID, click_stack_role_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2</code></summary>

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
try:
    response = client.click_stack.click_stack_delete_role(organization_id, service_id, click_stack_role_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackDeleteRoleErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_delete_role(organization_id, service_id, click_stack_role_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackDeleteRoleErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id_response2.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackDeleteRoleErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_role_error.py)&#93;</code>

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
<summary><code>def click_stack_delete_saved_search(organization_id: UUID, service_id: UUID, click_stack_saved_search_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2</code></summary>

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
try:
    response = client.click_stack.click_stack_delete_saved_search(
        organization_id, service_id, click_stack_saved_search_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackDeleteSavedSearchErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_delete_saved_search(
        organization_id, service_id, click_stack_saved_search_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackDeleteSavedSearchErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response2.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackDeleteSavedSearchErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_saved_search_error.py)&#93;</code>

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
<summary><code>def click_stack_delete_source(organization_id: UUID, service_id: UUID, click_stack_source_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2</code></summary>

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
try:
    response = client.click_stack.click_stack_delete_source(organization_id, service_id, click_stack_source_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackDeleteSourceErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_delete_source(
        organization_id, service_id, click_stack_source_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackDeleteSourceErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id_response2.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackDeleteSourceErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_source_error.py)&#93;</code>

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
<summary><code>def click_stack_delete_webhook(organization_id: UUID, service_id: UUID, click_stack_webhook_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1</code></summary>

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
try:
    response = client.click_stack.click_stack_delete_webhook(organization_id, service_id, click_stack_webhook_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackDeleteWebhookErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_delete_webhook(
        organization_id, service_id, click_stack_webhook_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackDeleteWebhookErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackDeleteWebhookErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_delete_webhook_error.py)&#93;</code>

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
<summary><code>def click_stack_get_alert(organization_id: UUID, service_id: UUID, click_stack_alert_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_get_alert(organization_id, service_id, click_stack_alert_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackGetAlertErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_get_alert(organization_id, service_id, click_stack_alert_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackGetAlertErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackGetAlertErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_alert_error.py)&#93;</code>

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
<summary><code>def click_stack_get_dashboard(organization_id: UUID, service_id: UUID, click_stack_dashboard_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_get_dashboard(organization_id, service_id, click_stack_dashboard_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackGetDashboardErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_get_dashboard(
        organization_id, service_id, click_stack_dashboard_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackGetDashboardErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackGetDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_dashboard_error.py)&#93;</code>

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
<summary><code>def click_stack_get_role(organization_id: UUID, service_id: UUID, click_stack_role_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_get_role(organization_id, service_id, click_stack_role_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackGetRoleErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_get_role(organization_id, service_id, click_stack_role_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackGetRoleErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackGetRoleErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_role_error.py)&#93;</code>

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
<summary><code>def click_stack_get_saved_search(organization_id: UUID, service_id: UUID, click_stack_saved_search_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_get_saved_search(organization_id, service_id, click_stack_saved_search_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackGetSavedSearchErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_get_saved_search(
        organization_id, service_id, click_stack_saved_search_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackGetSavedSearchErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackGetSavedSearchErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_saved_search_error.py)&#93;</code>

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
<summary><code>def click_stack_get_source(organization_id: UUID, service_id: UUID, click_stack_source_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_get_source(organization_id, service_id, click_stack_source_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackGetSourceErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_get_source(organization_id, service_id, click_stack_source_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackGetSourceErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackGetSourceErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_get_source_error.py)&#93;</code>

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
<summary><code>def click_stack_list_alerts(organization_id: UUID, service_id: UUID, *, limit: int | None = 1000, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackAlertsResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_list_alerts(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackAlertsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackListAlertsErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_list_alerts(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackAlertsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackListAlertsErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackAlertsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackListAlertsErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_alerts_error.py)&#93;</code>

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
<summary><code>def click_stack_list_dashboards(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackDashboardsResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_list_dashboards(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackDashboardsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackListDashboardsErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_list_dashboards(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackDashboardsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackListDashboardsErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackDashboardsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackListDashboardsErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_dashboards_error.py)&#93;</code>

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
<summary><code>def click_stack_list_roles(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackRolesResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_list_roles(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackRolesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackListRolesErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_list_roles(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackRolesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackListRolesErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackRolesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackListRolesErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_roles_error.py)&#93;</code>

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
<summary><code>def click_stack_list_saved_searches(organization_id: UUID, service_id: UUID, *, limit: int | None = 1000, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackSavedSearchesResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_list_saved_searches(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSavedSearchesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackListSavedSearchesErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_list_saved_searches(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSavedSearchesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackListSavedSearchesErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackSavedSearchesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackListSavedSearchesErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_saved_searches_error.py)&#93;</code>

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
<summary><code>def click_stack_list_sources(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackSourcesResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_list_sources(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSourcesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackListSourcesErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_list_sources(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSourcesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackListSourcesErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackSourcesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackListSourcesErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_sources_error.py)&#93;</code>

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
<summary><code>def click_stack_list_webhooks(organization_id: UUID, service_id: UUID, *, limit: int | None = 1000, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackWebhooksResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_list_webhooks(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackWebhooksResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackListWebhooksErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_list_webhooks(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackWebhooksResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackListWebhooksErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackWebhooksResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackListWebhooksErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_list_webhooks_error.py)&#93;</code>

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
<summary><code>def click_stack_update_alert(organization_id: UUID, service_id: UUID, click_stack_alert_id: str, *, body: ClickStackUpdateAlertRequest | ClickStackUpdateAlertRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_update_alert(organization_id, service_id, click_stack_alert_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackUpdateAlertErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_update_alert(
        organization_id, service_id, click_stack_alert_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackUpdateAlertErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackUpdateAlertErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_alert_error.py)&#93;</code>

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
<summary><code>def click_stack_update_dashboard(organization_id: UUID, service_id: UUID, click_stack_dashboard_id: str, *, body: ClickStackUpdateDashboardRequest | ClickStackUpdateDashboardRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_update_dashboard(organization_id, service_id, click_stack_dashboard_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackUpdateDashboardErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_update_dashboard(
        organization_id, service_id, click_stack_dashboard_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackUpdateDashboardErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackUpdateDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_dashboard_error.py)&#93;</code>

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
<summary><code>def click_stack_update_role(organization_id: UUID, service_id: UUID, click_stack_role_id: str, *, body: ClickStackUpdateRoleRequest | ClickStackUpdateRoleRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_update_role(organization_id, service_id, click_stack_role_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackUpdateRoleErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_update_role(organization_id, service_id, click_stack_role_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackUpdateRoleErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackUpdateRoleErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_role_error.py)&#93;</code>

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
<summary><code>def click_stack_update_saved_search(organization_id: UUID, service_id: UUID, click_stack_saved_search_id: str, *, body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_update_saved_search(
        organization_id, service_id, click_stack_saved_search_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackUpdateSavedSearchErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_update_saved_search(
        organization_id, service_id, click_stack_saved_search_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackUpdateSavedSearchErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackUpdateSavedSearchErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_saved_search_error.py)&#93;</code>

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
<summary><code>def click_stack_update_source(organization_id: UUID, service_id: UUID, click_stack_source_id: str, *, body: ClickStackSource | ClickStackSourceDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_update_source(organization_id, service_id, click_stack_source_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackUpdateSourceErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_update_source(
        organization_id, service_id, click_stack_source_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackUpdateSourceErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackUpdateSourceErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_source_error.py)&#93;</code>

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
<summary><code>def click_stack_update_webhook(organization_id: UUID, service_id: UUID, click_stack_webhook_id: str, *, body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_update_webhook(organization_id, service_id, click_stack_webhook_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackUpdateWebhookErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_update_webhook(
        organization_id, service_id, click_stack_webhook_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackUpdateWebhookErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackUpdateWebhookErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_update_webhook_error.py)&#93;</code>

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
<summary><code>def click_stack_validate_dashboard(organization_id: UUID, service_id: UUID, *, body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickstackDashboardsValidateResponse</code></summary>

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
try:
    response = client.click_stack.click_stack_validate_dashboard(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackDashboardsValidateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackValidateDashboardErrorBody
```

**Async**

```python
try:
    response = await async_client.click_stack.click_stack_validate_dashboard(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickstackDashboardsValidateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ClickStackValidateDashboardErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickstackDashboardsValidateResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_validate_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ClickStackValidateDashboardErrorBody](open_api_spec_for_click_house_cloud/errors/click_stack_validate_dashboard_error.py)&#93;</code>

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
<summary><code>def activity_get(organization_id: UUID, activity_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsActivitiesResponse1</code></summary>

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
try:
    response = client.organization_api.activity_get(organization_id, activity_id)
    # TODO: Handle 'response' of type V1OrganizationsActivitiesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivityGetErrorBody
```

**Async**

```python
try:
    response = await async_client.organization_api.activity_get(organization_id, activity_id)
    # TODO: Handle 'response' of type V1OrganizationsActivitiesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivityGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsActivitiesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_activities_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ActivityGetErrorBody](open_api_spec_for_click_house_cloud/errors/activity_get_error.py)&#93;</code>

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
<summary><code>def activity_get_list(organization_id: UUID, *, from_date: RFC3339DateTime | None = None, to_date: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsActivitiesResponse</code></summary>

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
try:
    response = client.organization_api.activity_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsActivitiesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivityGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.organization_api.activity_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsActivitiesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivityGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsActivitiesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_activities_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ActivityGetListErrorBody](open_api_spec_for_click_house_cloud/errors/activity_get_list_error.py)&#93;</code>

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
<summary><code>def organization_byoc_infrastructure_create(organization_id: UUID, *, body: ByocInfrastructurePostRequest | ByocInfrastructurePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsByocInfrastructureResponse</code></summary>

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
try:
    response = client.organization_api.organization_byoc_infrastructure_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsByocInfrastructureResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationByocInfrastructureCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.organization_api.organization_byoc_infrastructure_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsByocInfrastructureResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationByocInfrastructureCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsByocInfrastructureResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationByocInfrastructureCreateErrorBody](open_api_spec_for_click_house_cloud/errors/organization_byoc_infrastructure_create_error.py)&#93;</code>

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
<summary><code>def organization_byoc_infrastructure_delete(organization_id: UUID, byoc_infrastructure_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsByocInfrastructureResponse1</code></summary>

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
try:
    response = client.organization_api.organization_byoc_infrastructure_delete(organization_id, byoc_infrastructure_id)
    # TODO: Handle 'response' of type V1OrganizationsByocInfrastructureResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationByocInfrastructureDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.organization_api.organization_byoc_infrastructure_delete(
        organization_id, byoc_infrastructure_id
    )
    # TODO: Handle 'response' of type V1OrganizationsByocInfrastructureResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationByocInfrastructureDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsByocInfrastructureResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationByocInfrastructureDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/organization_byoc_infrastructure_delete_error.py)&#93;</code>

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
<summary><code>def organization_byoc_infrastructure_update(organization_id: UUID, byoc_infrastructure_id: UUID, *, body: ByocInfrastructurePatchRequest | ByocInfrastructurePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsByocInfrastructureResponse</code></summary>

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
try:
    response = client.organization_api.organization_byoc_infrastructure_update(organization_id, byoc_infrastructure_id)
    # TODO: Handle 'response' of type V1OrganizationsByocInfrastructureResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationByocInfrastructureUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.organization_api.organization_byoc_infrastructure_update(
        organization_id, byoc_infrastructure_id
    )
    # TODO: Handle 'response' of type V1OrganizationsByocInfrastructureResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationByocInfrastructureUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsByocInfrastructureResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationByocInfrastructureUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/organization_byoc_infrastructure_update_error.py)&#93;</code>

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
<summary><code>def organization_get(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsResponse1</code></summary>

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
try:
    response = client.organization_api.organization_get(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationGetErrorBody
```

**Async**

```python
try:
    response = await async_client.organization_api.organization_get(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_get_error.py)&#93;</code>

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
<summary><code>def organization_get_list(*, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsResponse</code></summary>

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
try:
    response = client.organization_api.organization_get_list()
    # TODO: Handle 'response' of type V1OrganizationsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.organization_api.organization_get_list()
    # TODO: Handle 'response' of type V1OrganizationsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationGetListErrorBody](open_api_spec_for_click_house_cloud/errors/organization_get_list_error.py)&#93;</code>

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
<summary><code>def organization_private_endpoint_config_get_list(organization_id: UUID, cloud_provider: str, region_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPrivateEndpointConfigResponse</code></summary>

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
try:
    response = client.organization_api.organization_private_endpoint_config_get_list(
        organization_id, cloud_provider, region_id
    )
    # TODO: Handle 'response' of type V1OrganizationsPrivateEndpointConfigResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationPrivateEndpointConfigGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.organization_api.organization_private_endpoint_config_get_list(
        organization_id, cloud_provider, region_id
    )
    # TODO: Handle 'response' of type V1OrganizationsPrivateEndpointConfigResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationPrivateEndpointConfigGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPrivateEndpointConfigResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_private_endpoint_config_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationPrivateEndpointConfigGetListErrorBody](open_api_spec_for_click_house_cloud/errors/organization_private_endpoint_config_get_list_error.py)&#93;</code>

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
<summary><code>def organization_quota_get(organization_id: UUID, quota_code: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsQuotasResponse1</code></summary>

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
try:
    response = client.organization_api.organization_quota_get(organization_id, quota_code)
    # TODO: Handle 'response' of type V1OrganizationsQuotasResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationQuotaGetErrorBody
```

**Async**

```python
try:
    response = await async_client.organization_api.organization_quota_get(organization_id, quota_code)
    # TODO: Handle 'response' of type V1OrganizationsQuotasResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationQuotaGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsQuotasResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_quotas_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationQuotaGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_quota_get_error.py)&#93;</code>

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
<summary><code>def organization_quotas_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsQuotasResponse</code></summary>

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
try:
    response = client.organization_api.organization_quotas_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsQuotasResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationQuotasGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.organization_api.organization_quotas_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsQuotasResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationQuotasGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsQuotasResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_quotas_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationQuotasGetListErrorBody](open_api_spec_for_click_house_cloud/errors/organization_quotas_get_list_error.py)&#93;</code>

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
<summary><code>def organization_update(organization_id: UUID, *, body: OrganizationPatchRequest | OrganizationPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsResponse1</code></summary>

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
try:
    response = client.organization_api.organization_update(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.organization_api.organization_update(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/organization_update_error.py)&#93;</code>

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
<summary><code>def postgres_instance_config_get(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresConfigResponse</code></summary>

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
try:
    response = client.postgres.postgres_instance_config_get(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresConfigResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstanceConfigGetErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_instance_config_get(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresConfigResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstanceConfigGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresConfigResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresInstanceConfigGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_config_get_error.py)&#93;</code>

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
<summary><code>def postgres_instance_config_patch(organization_id: UUID, postgres_id: UUID, *, body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresConfigResponse1</code></summary>

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
try:
    response = client.postgres.postgres_instance_config_patch(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresConfigResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstanceConfigPatchErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_instance_config_patch(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresConfigResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstanceConfigPatchErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresConfigResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresInstanceConfigPatchErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_config_patch_error.py)&#93;</code>

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
<summary><code>def postgres_instance_config_post(organization_id: UUID, postgres_id: UUID, *, body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresConfigResponse1</code></summary>

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
try:
    response = client.postgres.postgres_instance_config_post(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresConfigResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstanceConfigPostErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_instance_config_post(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresConfigResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstanceConfigPostErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresConfigResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresInstanceConfigPostErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_config_post_error.py)&#93;</code>

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
<summary><code>def postgres_instance_create_read_replica(organization_id: UUID, postgres_id: UUID, *, body: PostgresServiceReadReplicaRequest | PostgresServiceReadReplicaRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresReadReplicaResponse</code></summary>

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
try:
    response = client.postgres.postgres_instance_create_read_replica(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresReadReplicaResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstanceCreateReadReplicaErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_instance_create_read_replica(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresReadReplicaResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstanceCreateReadReplicaErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresReadReplicaResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_read_replica_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresInstanceCreateReadReplicaErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_create_read_replica_error.py)&#93;</code>

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
<summary><code>def postgres_instance_metrics_get(organization_id: UUID, postgres_id: UUID, from_date: RFC3339DateTime, to_date: RFC3339DateTime, *, bucket_size_seconds: int | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresMetricsResponse</code></summary>

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
try:
    response = client.postgres.postgres_instance_metrics_get(organization_id, postgres_id, from_date, to_date)
    # TODO: Handle 'response' of type V1OrganizationsPostgresMetricsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstanceMetricsGetErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_instance_metrics_get(
        organization_id, postgres_id, from_date, to_date
    )
    # TODO: Handle 'response' of type V1OrganizationsPostgresMetricsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstanceMetricsGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresMetricsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_metrics_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresInstanceMetricsGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_metrics_get_error.py)&#93;</code>

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
<summary><code>def postgres_instance_restore(organization_id: UUID, postgres_id: UUID, *, body: PostgresServiceRestoreRequest | PostgresServiceRestoreRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresRestoredServiceResponse</code></summary>

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
try:
    response = client.postgres.postgres_instance_restore(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresRestoredServiceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstanceRestoreErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_instance_restore(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresRestoredServiceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstanceRestoreErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresRestoredServiceResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_restored_service_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresInstanceRestoreErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_restore_error.py)&#93;</code>

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
<summary><code>def postgres_logs_get_list(organization_id: UUID, postgres_id: UUID, from_date: RFC3339DateTime, to_date: RFC3339DateTime, *, body_contains: str | None = None, severity: str | None = None, sort_order: SortOrder1OrStr | None = SortOrder1.DESC, limit: int | None = 50, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresLogsResponse</code></summary>

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
try:
    response = client.postgres.postgres_logs_get_list(organization_id, postgres_id, from_date, to_date)
    # TODO: Handle 'response' of type V1OrganizationsPostgresLogsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresLogsGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_logs_get_list(organization_id, postgres_id, from_date, to_date)
    # TODO: Handle 'response' of type V1OrganizationsPostgresLogsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresLogsGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresLogsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_logs_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresLogsGetListErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_logs_get_list_error.py)&#93;</code>

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
<summary><code>def postgres_service_certs_get(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.postgres.postgres_service_certs_get(organization_id, postgres_id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServiceCertsGetErrorBody
```

**Async**

```python
try:
    await async_client.postgres.postgres_service_certs_get(organization_id, postgres_id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServiceCertsGetErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresServiceCertsGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_certs_get_error.py)&#93;</code>

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
<summary><code>def postgres_service_create(organization_id: UUID, *, body: PostgresServicePostRequest | PostgresServicePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresResponse</code></summary>

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
try:
    response = client.postgres.postgres_service_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServiceCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_service_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServiceCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresServiceCreateErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_create_error.py)&#93;</code>

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
<summary><code>def postgres_service_delete(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresResponse3</code></summary>

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
try:
    response = client.postgres.postgres_service_delete(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresResponse3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServiceDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_service_delete(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresResponse3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServiceDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresResponse3](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response3.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresServiceDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_delete_error.py)&#93;</code>

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
<summary><code>def postgres_service_get(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresResponse</code></summary>

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
try:
    response = client.postgres.postgres_service_get(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServiceGetErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_service_get(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServiceGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresServiceGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_get_error.py)&#93;</code>

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
<summary><code>def postgres_service_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresResponse1</code></summary>

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
try:
    response = client.postgres.postgres_service_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServiceGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_service_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServiceGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresServiceGetListErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_get_list_error.py)&#93;</code>

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
<summary><code>def postgres_service_patch(organization_id: UUID, postgres_id: UUID, *, body: PostgresServicePatchRequest | PostgresServicePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresResponse</code></summary>

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
try:
    response = client.postgres.postgres_service_patch(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServicePatchErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_service_patch(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServicePatchErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresServicePatchErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_patch_error.py)&#93;</code>

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
<summary><code>def postgres_service_patch_state(organization_id: UUID, postgres_id: UUID, *, body: PostgresServiceSetState | PostgresServiceSetStateDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresStateResponse</code></summary>

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
try:
    response = client.postgres.postgres_service_patch_state(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresStateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServicePatchStateErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_service_patch_state(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresStateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServicePatchStateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresStateResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_state_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresServicePatchStateErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_patch_state_error.py)&#93;</code>

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
<summary><code>def postgres_service_set_password(organization_id: UUID, postgres_id: UUID, *, body: PostgresServiceSetPassword | PostgresServiceSetPasswordDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresPasswordResponse</code></summary>

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
try:
    response = client.postgres.postgres_service_set_password(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresPasswordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServiceSetPasswordErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.postgres_service_set_password(organization_id, postgres_id)
    # TODO: Handle 'response' of type V1OrganizationsPostgresPasswordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresServiceSetPasswordErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresPasswordResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_password_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresServiceSetPasswordErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_service_set_password_error.py)&#93;</code>

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
<summary><code>def slow_query_pattern_get(organization_id: UUID, postgres_id: UUID, query_id: str, db_name: str, db_user: str, db_operation: str, *, app: str | None = None, timestamp: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse</code></summary>

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
try:
    response = client.postgres.slow_query_pattern_get(
        organization_id, postgres_id, query_id, db_name, db_user, db_operation
    )
    # TODO: Handle 'response' of type V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SlowQueryPatternGetErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.slow_query_pattern_get(
        organization_id, postgres_id, query_id, db_name, db_user, db_operation
    )
    # TODO: Handle 'response' of type V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SlowQueryPatternGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns_query_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[SlowQueryPatternGetErrorBody](open_api_spec_for_click_house_cloud/errors/slow_query_pattern_get_error.py)&#93;</code>

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
<summary><code>def slow_query_patterns_get_list(organization_id: UUID, postgres_id: UUID, from_date: RFC3339DateTime, to_date: RFC3339DateTime, *, db_name: str | None = None, db_user: str | None = None, db_operation: str | None = None, app: str | None = None, sort_by: SortByOrStr | None = SortBy.TOTAL_DURATION, sort_order: SortOrder1OrStr | None = SortOrder1.DESC, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsPostgresSlowQueryPatternsResponse</code></summary>

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
try:
    response = client.postgres.slow_query_patterns_get_list(organization_id, postgres_id, from_date, to_date)
    # TODO: Handle 'response' of type V1OrganizationsPostgresSlowQueryPatternsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SlowQueryPatternsGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.postgres.slow_query_patterns_get_list(
        organization_id, postgres_id, from_date, to_date
    )
    # TODO: Handle 'response' of type V1OrganizationsPostgresSlowQueryPatternsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SlowQueryPatternsGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsPostgresSlowQueryPatternsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[SlowQueryPatternsGetListErrorBody](open_api_spec_for_click_house_cloud/errors/slow_query_patterns_get_list_error.py)&#93;</code>

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
<summary><code>def instance_prometheus_get(organization_id: UUID, service_id: UUID, *, filtered_metrics: str | None = None, request_options: RequestOptionsOrDict | None = None) -> str</code></summary>

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
try:
    response = client.prometheus.instance_prometheus_get(organization_id, service_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstancePrometheusGetErrorBody
```

**Async**

```python
try:
    response = await async_client.prometheus.instance_prometheus_get(organization_id, service_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstancePrometheusGetErrorBody
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

**OnSuccess**: <code>str</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstancePrometheusGetErrorBody](open_api_spec_for_click_house_cloud/errors/instance_prometheus_get_error.py)&#93;</code>

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
<summary><code>def organization_prometheus_discovery_get(organization_id: UUID, *, filtered_metrics: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[PrometheusDiscoveryTargetGroup]</code></summary>

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
try:
    response = client.prometheus.organization_prometheus_discovery_get(organization_id)
    # TODO: Handle 'response' of type list[PrometheusDiscoveryTargetGroup]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationPrometheusDiscoveryGetErrorBody
```

**Async**

```python
try:
    response = await async_client.prometheus.organization_prometheus_discovery_get(organization_id)
    # TODO: Handle 'response' of type list[PrometheusDiscoveryTargetGroup]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationPrometheusDiscoveryGetErrorBody
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

**OnSuccess**: <code>list&#91;[PrometheusDiscoveryTargetGroup](open_api_spec_for_click_house_cloud/models/prometheus_discovery_target_group.py)&#93;</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationPrometheusDiscoveryGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_prometheus_discovery_get_error.py)&#93;</code>

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
<summary><code>def organization_prometheus_get(organization_id: UUID, *, filtered_metrics: str | None = None, request_options: RequestOptionsOrDict | None = None) -> str</code></summary>

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
try:
    response = client.prometheus.organization_prometheus_get(organization_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationPrometheusGetErrorBody
```

**Async**

```python
try:
    response = await async_client.prometheus.organization_prometheus_get(organization_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationPrometheusGetErrorBody
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

**OnSuccess**: <code>str</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationPrometheusGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_prometheus_get_error.py)&#93;</code>

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
<summary><code>def postgres_instance_prometheus_get(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> str</code></summary>

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
try:
    response = client.prometheus.postgres_instance_prometheus_get(organization_id, postgres_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstancePrometheusGetErrorBody
```

**Async**

```python
try:
    response = await async_client.prometheus.postgres_instance_prometheus_get(organization_id, postgres_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresInstancePrometheusGetErrorBody
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

**OnSuccess**: <code>str</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresInstancePrometheusGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_instance_prometheus_get_error.py)&#93;</code>

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
<summary><code>def postgres_org_prometheus_get(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> str</code></summary>

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
try:
    response = client.prometheus.postgres_org_prometheus_get(organization_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresOrgPrometheusGetErrorBody
```

**Async**

```python
try:
    response = await async_client.prometheus.postgres_org_prometheus_get(organization_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PostgresOrgPrometheusGetErrorBody
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

**OnSuccess**: <code>str</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[PostgresOrgPrometheusGetErrorBody](open_api_spec_for_click_house_cloud/errors/postgres_org_prometheus_get_error.py)&#93;</code>

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
<summary><code>def query_api_endpoint_create(organization_id: UUID, service_id: UUID, *, body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesQueryApiEndpointsResponse</code></summary>

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
try:
    response = client.query_api_endpoints.query_api_endpoint_create(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesQueryApiEndpointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryApiEndpointCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.query_api_endpoints.query_api_endpoint_create(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesQueryApiEndpointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryApiEndpointCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesQueryApiEndpointsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_response.py)</code> -- The Query API endpoint was created.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[QueryApiEndpointCreateErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_create_error.py)&#93;</code>

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
<summary><code>def query_api_endpoint_delete(organization_id: UUID, service_id: UUID, endpoint_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse</code></summary>

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
try:
    response = client.query_api_endpoints.query_api_endpoint_delete(organization_id, service_id, endpoint_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryApiEndpointDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.query_api_endpoints.query_api_endpoint_delete(
        organization_id, service_id, endpoint_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryApiEndpointDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id_response.py)</code> -- The Query API endpoint was deleted.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[QueryApiEndpointDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_delete_error.py)&#93;</code>

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
<summary><code>def query_api_endpoint_get(organization_id: UUID, service_id: UUID, endpoint_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1</code></summary>

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
try:
    response = client.query_api_endpoints.query_api_endpoint_get(organization_id, service_id, endpoint_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryApiEndpointGetErrorBody
```

**Async**

```python
try:
    response = await async_client.query_api_endpoints.query_api_endpoint_get(organization_id, service_id, endpoint_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryApiEndpointGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id_response1.py)</code> -- Successful response.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[QueryApiEndpointGetErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_get_error.py)&#93;</code>

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
<summary><code>def query_api_endpoint_list(organization_id: UUID, service_id: UUID, *, cursor: str | None = None, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesQueryApiEndpointsResponse1</code></summary>

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
try:
    response = client.query_api_endpoints.query_api_endpoint_list(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesQueryApiEndpointsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryApiEndpointListErrorBody
```

**Async**

```python
try:
    response = await async_client.query_api_endpoints.query_api_endpoint_list(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesQueryApiEndpointsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryApiEndpointListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesQueryApiEndpointsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_response1.py)</code> -- Successful response.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[QueryApiEndpointListErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_list_error.py)&#93;</code>

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
<summary><code>def query_api_endpoint_update(organization_id: UUID, service_id: UUID, endpoint_id: UUID, *, body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1</code></summary>

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
try:
    response = client.query_api_endpoints.query_api_endpoint_update(organization_id, service_id, endpoint_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryApiEndpointUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.query_api_endpoints.query_api_endpoint_update(
        organization_id, service_id, endpoint_id
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryApiEndpointUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id_response1.py)</code> -- The Query API endpoint was updated.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[QueryApiEndpointUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/query_api_endpoint_update_error.py)&#93;</code>

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
<summary><code>def organization_role_delete(organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsRolesResponse4</code></summary>

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
try:
    response = client.role_management.organization_role_delete(organization_id, role_id)
    # TODO: Handle 'response' of type V1OrganizationsRolesResponse4
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationRoleDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.role_management.organization_role_delete(organization_id, role_id)
    # TODO: Handle 'response' of type V1OrganizationsRolesResponse4
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationRoleDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsRolesResponse4](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response4.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationRoleDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/organization_role_delete_error.py)&#93;</code>

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
<summary><code>def organization_role_get(organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsRolesResponse1</code></summary>

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
try:
    response = client.role_management.organization_role_get(organization_id, role_id)
    # TODO: Handle 'response' of type V1OrganizationsRolesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationRoleGetErrorBody
```

**Async**

```python
try:
    response = await async_client.role_management.organization_role_get(organization_id, role_id)
    # TODO: Handle 'response' of type V1OrganizationsRolesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationRoleGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsRolesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationRoleGetErrorBody](open_api_spec_for_click_house_cloud/errors/organization_role_get_error.py)&#93;</code>

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
<summary><code>def organization_role_patch(organization_id: UUID, role_id: UUID, *, body: RoleUpdateRequest | RoleUpdateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsRolesResponse1</code></summary>

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
try:
    response = client.role_management.organization_role_patch(organization_id, role_id)
    # TODO: Handle 'response' of type V1OrganizationsRolesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationRolePatchErrorBody
```

**Async**

```python
try:
    response = await async_client.role_management.organization_role_patch(organization_id, role_id)
    # TODO: Handle 'response' of type V1OrganizationsRolesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationRolePatchErrorBody
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

**OnSuccess**: <code>[V1OrganizationsRolesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationRolePatchErrorBody](open_api_spec_for_click_house_cloud/errors/organization_role_patch_error.py)&#93;</code>

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
<summary><code>def organization_role_post(organization_id: UUID, *, body: RoleCreateRequest | RoleCreateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsRolesResponse1</code></summary>

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
try:
    response = client.role_management.organization_role_post(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsRolesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationRolePostErrorBody
```

**Async**

```python
try:
    response = await async_client.role_management.organization_role_post(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsRolesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationRolePostErrorBody
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

**OnSuccess**: <code>[V1OrganizationsRolesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationRolePostErrorBody](open_api_spec_for_click_house_cloud/errors/organization_role_post_error.py)&#93;</code>

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
<summary><code>def organization_roles_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsRolesResponse</code></summary>

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
try:
    response = client.role_management.organization_roles_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsRolesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationRolesGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.role_management.organization_roles_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsRolesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OrganizationRolesGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsRolesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[OrganizationRolesGetListErrorBody](open_api_spec_for_click_house_cloud/errors/organization_roles_get_list_error.py)&#93;</code>

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
<summary><code>def instance_create(organization_id: UUID, *, body: ServicePostRequest | ServicePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesResponse1</code></summary>

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
try:
    response = client.service_api.instance_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstanceCreateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_create_error.py)&#93;</code>

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
<summary><code>def instance_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesResponse4</code></summary>

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
try:
    response = client.service_api.instance_delete(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesResponse4
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_delete(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesResponse4
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesResponse4](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response4.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstanceDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/instance_delete_error.py)&#93;</code>

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
<summary><code>def instance_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesResponse2</code></summary>

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
try:
    response = client.service_api.instance_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceGetErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response2.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstanceGetErrorBody](open_api_spec_for_click_house_cloud/errors/instance_get_error.py)&#93;</code>

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
<summary><code>def instance_get_list(organization_id: UUID, *, filter: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesResponse</code></summary>

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
try:
    response = client.service_api.instance_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstanceGetListErrorBody](open_api_spec_for_click_house_cloud/errors/instance_get_list_error.py)&#93;</code>

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
<summary><code>def instance_password_update(organization_id: UUID, service_id: UUID, *, body: ServicePasswordPatchRequest | ServicePasswordPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesPasswordResponse</code></summary>

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
try:
    response = client.service_api.instance_password_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesPasswordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstancePasswordUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_password_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesPasswordResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstancePasswordUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesPasswordResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_password_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstancePasswordUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_password_update_error.py)&#93;</code>

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
<summary><code>def instance_private_endpoint_config_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesPrivateEndpointConfigResponse</code></summary>

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
try:
    response = client.service_api.instance_private_endpoint_config_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesPrivateEndpointConfigResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstancePrivateEndpointConfigGetErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_private_endpoint_config_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesPrivateEndpointConfigResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstancePrivateEndpointConfigGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesPrivateEndpointConfigResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint_config_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstancePrivateEndpointConfigGetErrorBody](open_api_spec_for_click_house_cloud/errors/instance_private_endpoint_config_get_error.py)&#93;</code>

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
<summary><code>def instance_private_endpoint_create(organization_id: UUID, service_id: UUID, *, body: ServicPrivateEndpointePostRequest | ServicPrivateEndpointePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesPrivateEndpointResponse</code></summary>

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
try:
    response = client.service_api.instance_private_endpoint_create(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesPrivateEndpointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstancePrivateEndpointCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_private_endpoint_create(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesPrivateEndpointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstancePrivateEndpointCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesPrivateEndpointResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstancePrivateEndpointCreateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_private_endpoint_create_error.py)&#93;</code>

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
<summary><code>def instance_query_endpoint_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesServiceQueryEndpointResponse1</code></summary>

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
try:
    response = client.service_api.instance_query_endpoint_delete(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesServiceQueryEndpointResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceQueryEndpointDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_query_endpoint_delete(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesServiceQueryEndpointResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceQueryEndpointDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesServiceQueryEndpointResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstanceQueryEndpointDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/instance_query_endpoint_delete_error.py)&#93;</code>

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
<summary><code>def instance_query_endpoint_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesServiceQueryEndpointResponse</code></summary>

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
try:
    response = client.service_api.instance_query_endpoint_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesServiceQueryEndpointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceQueryEndpointGetErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_query_endpoint_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesServiceQueryEndpointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceQueryEndpointGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesServiceQueryEndpointResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstanceQueryEndpointGetErrorBody](open_api_spec_for_click_house_cloud/errors/instance_query_endpoint_get_error.py)&#93;</code>

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
<summary><code>def instance_query_endpoint_upsert(organization_id: UUID, service_id: UUID, *, body: InstanceServiceQueryApiEndpointsPostRequest | InstanceServiceQueryApiEndpointsPostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesServiceQueryEndpointResponse</code></summary>

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
try:
    response = client.service_api.instance_query_endpoint_upsert(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesServiceQueryEndpointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceQueryEndpointUpsertErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_query_endpoint_upsert(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesServiceQueryEndpointResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceQueryEndpointUpsertErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesServiceQueryEndpointResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstanceQueryEndpointUpsertErrorBody](open_api_spec_for_click_house_cloud/errors/instance_query_endpoint_upsert_error.py)&#93;</code>

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
<summary><code>def instance_replica_scaling_update(organization_id: UUID, service_id: UUID, *, body: ServiceReplicaScalingPatchRequest | ServiceReplicaScalingPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesReplicaScalingResponse</code></summary>

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
try:
    response = client.service_api.instance_replica_scaling_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesReplicaScalingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceReplicaScalingUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_replica_scaling_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesReplicaScalingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceReplicaScalingUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesReplicaScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_replica_scaling_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstanceReplicaScalingUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_replica_scaling_update_error.py)&#93;</code>

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
<summary><code>def instance_scaling_update(organization_id: UUID, service_id: UUID, *, body: ServiceScalingPatchRequest | ServiceScalingPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesScalingResponse</code></summary>

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
try:
    response = client.service_api.instance_scaling_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesScalingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceScalingUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_scaling_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesScalingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceScalingUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesScalingResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstanceScalingUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_scaling_update_error.py)&#93;</code>

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
<summary><code>def instance_state_update(organization_id: UUID, service_id: UUID, *, body: ServiceStatePatchRequest | ServiceStatePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesStateResponse</code></summary>

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
try:
    response = client.service_api.instance_state_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesStateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceStateUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_state_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesStateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceStateUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesStateResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_state_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstanceStateUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_state_update_error.py)&#93;</code>

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
<summary><code>def instance_update(organization_id: UUID, service_id: UUID, *, body: ServicePatchRequest | ServicePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesResponse2</code></summary>

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
try:
    response = client.service_api.instance_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.instance_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InstanceUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_response2.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InstanceUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/instance_update_error.py)&#93;</code>

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
<summary><code>def scaling_schedule_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesScalingScheduleResponse2</code></summary>

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
try:
    response = client.service_api.scaling_schedule_delete(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesScalingScheduleResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScalingScheduleDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.scaling_schedule_delete(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesScalingScheduleResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScalingScheduleDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesScalingScheduleResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule_response2.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ScalingScheduleDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/scaling_schedule_delete_error.py)&#93;</code>

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
<summary><code>def scaling_schedule_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesScalingScheduleResponse</code></summary>

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
try:
    response = client.service_api.scaling_schedule_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesScalingScheduleResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScalingScheduleGetErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.scaling_schedule_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesScalingScheduleResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScalingScheduleGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesScalingScheduleResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ScalingScheduleGetErrorBody](open_api_spec_for_click_house_cloud/errors/scaling_schedule_get_error.py)&#93;</code>

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
<summary><code>def scaling_schedule_upsert(organization_id: UUID, service_id: UUID, *, body: ScalingSchedulePostRequest | ScalingSchedulePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesScalingScheduleResponse</code></summary>

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
try:
    response = client.service_api.scaling_schedule_upsert(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesScalingScheduleResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScalingScheduleUpsertErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.scaling_schedule_upsert(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesScalingScheduleResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScalingScheduleUpsertErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesScalingScheduleResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ScalingScheduleUpsertErrorBody](open_api_spec_for_click_house_cloud/errors/scaling_schedule_upsert_error.py)&#93;</code>

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
<summary><code>def service_clickhouse_setting_delete(organization_id: UUID, service_id: UUID, setting_name: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickhouseSettingsSettingNameResponse1</code></summary>

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
try:
    response = client.service_api.service_clickhouse_setting_delete(organization_id, service_id, setting_name)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickhouseSettingsSettingNameResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ServiceClickhouseSettingDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.service_clickhouse_setting_delete(
        organization_id, service_id, setting_name
    )
    # TODO: Handle 'response' of type V1OrganizationsServicesClickhouseSettingsSettingNameResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ServiceClickhouseSettingDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickhouseSettingsSettingNameResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ServiceClickhouseSettingDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_setting_delete_error.py)&#93;</code>

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
<summary><code>def service_clickhouse_setting_get(organization_id: UUID, service_id: UUID, setting_name: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickhouseSettingsSettingNameResponse</code></summary>

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
try:
    response = client.service_api.service_clickhouse_setting_get(organization_id, service_id, setting_name)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickhouseSettingsSettingNameResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ServiceClickhouseSettingGetErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.service_clickhouse_setting_get(organization_id, service_id, setting_name)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickhouseSettingsSettingNameResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ServiceClickhouseSettingGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickhouseSettingsSettingNameResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ServiceClickhouseSettingGetErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_setting_get_error.py)&#93;</code>

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
<summary><code>def service_clickhouse_settings_list_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickhouseSettingsResponse</code></summary>

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
try:
    response = client.service_api.service_clickhouse_settings_list_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickhouseSettingsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ServiceClickhouseSettingsListGetErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.service_clickhouse_settings_list_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickhouseSettingsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ServiceClickhouseSettingsListGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickhouseSettingsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ServiceClickhouseSettingsListGetErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_settings_list_get_error.py)&#93;</code>

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
<summary><code>def service_clickhouse_settings_schema_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickhouseSettingsSchemaResponse</code></summary>

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
try:
    response = client.service_api.service_clickhouse_settings_schema_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickhouseSettingsSchemaResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ServiceClickhouseSettingsSchemaGetErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.service_clickhouse_settings_schema_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickhouseSettingsSchemaResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ServiceClickhouseSettingsSchemaGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickhouseSettingsSchemaResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_schema_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ServiceClickhouseSettingsSchemaGetErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_settings_schema_get_error.py)&#93;</code>

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
<summary><code>def service_clickhouse_settings_update(organization_id: UUID, service_id: UUID, *, body: ServiceClickhouseSettingsPatchRequest | ServiceClickhouseSettingsPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesClickhouseSettingsResponse1</code></summary>

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
try:
    response = client.service_api.service_clickhouse_settings_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickhouseSettingsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ServiceClickhouseSettingsUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.service_clickhouse_settings_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesClickhouseSettingsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ServiceClickhouseSettingsUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesClickhouseSettingsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ServiceClickhouseSettingsUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/service_clickhouse_settings_update_error.py)&#93;</code>

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
<summary><code>def service_profiles_list(organization_id: UUID, *, region_id: str | None = None, byoc_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServiceProfilesResponse</code></summary>

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
try:
    response = client.service_api.service_profiles_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsServiceProfilesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ServiceProfilesListErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.service_profiles_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsServiceProfilesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ServiceProfilesListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServiceProfilesResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_service_profiles_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[ServiceProfilesListErrorBody](open_api_spec_for_click_house_cloud/errors/service_profiles_list_error.py)&#93;</code>

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
<summary><code>def upgrade_window_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesUpgradeWindowResponse2</code></summary>

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
try:
    response = client.service_api.upgrade_window_delete(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesUpgradeWindowResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpgradeWindowDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.upgrade_window_delete(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesUpgradeWindowResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpgradeWindowDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesUpgradeWindowResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window_response2.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UpgradeWindowDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/upgrade_window_delete_error.py)&#93;</code>

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
<summary><code>def upgrade_window_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesUpgradeWindowResponse</code></summary>

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
try:
    response = client.service_api.upgrade_window_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesUpgradeWindowResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpgradeWindowGetErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.upgrade_window_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesUpgradeWindowResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpgradeWindowGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesUpgradeWindowResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UpgradeWindowGetErrorBody](open_api_spec_for_click_house_cloud/errors/upgrade_window_get_error.py)&#93;</code>

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
<summary><code>def upgrade_window_update(organization_id: UUID, service_id: UUID, *, body: UpgradeWindowPutRequest | UpgradeWindowPutRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesUpgradeWindowResponse</code></summary>

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
try:
    response = client.service_api.upgrade_window_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesUpgradeWindowResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpgradeWindowUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.service_api.upgrade_window_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesUpgradeWindowResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpgradeWindowUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesUpgradeWindowResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UpgradeWindowUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/upgrade_window_update_error.py)&#93;</code>

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
<summary><code>def snapshot_configuration_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesSnapshotConfigurationResponse</code></summary>

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
try:
    response = client.snapshot_api.snapshot_configuration_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesSnapshotConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SnapshotConfigurationGetErrorBody
```

**Async**

```python
try:
    response = await async_client.snapshot_api.snapshot_configuration_get(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesSnapshotConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SnapshotConfigurationGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesSnapshotConfigurationResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[SnapshotConfigurationGetErrorBody](open_api_spec_for_click_house_cloud/errors/snapshot_configuration_get_error.py)&#93;</code>

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
<summary><code>def snapshot_configuration_update(organization_id: UUID, service_id: UUID, *, body: SnapshotConfigurationPatchRequest | SnapshotConfigurationPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesSnapshotConfigurationResponse</code></summary>

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
try:
    response = client.snapshot_api.snapshot_configuration_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesSnapshotConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SnapshotConfigurationUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.snapshot_api.snapshot_configuration_update(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesSnapshotConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SnapshotConfigurationUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesSnapshotConfigurationResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[SnapshotConfigurationUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/snapshot_configuration_update_error.py)&#93;</code>

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
<summary><code>def snapshot_get(organization_id: UUID, service_id: UUID, snapshot_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesSnapshotsSnapshotIdResponse</code></summary>

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
try:
    response = client.snapshot_api.snapshot_get(organization_id, service_id, snapshot_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesSnapshotsSnapshotIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SnapshotGetErrorBody
```

**Async**

```python
try:
    response = await async_client.snapshot_api.snapshot_get(organization_id, service_id, snapshot_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesSnapshotsSnapshotIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SnapshotGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesSnapshotsSnapshotIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots_snapshot_id_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[SnapshotGetErrorBody](open_api_spec_for_click_house_cloud/errors/snapshot_get_error.py)&#93;</code>

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
<summary><code>def snapshot_get_list(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsServicesSnapshotsResponse</code></summary>

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
try:
    response = client.snapshot_api.snapshot_get_list(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesSnapshotsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SnapshotGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.snapshot_api.snapshot_get_list(organization_id, service_id)
    # TODO: Handle 'response' of type V1OrganizationsServicesSnapshotsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SnapshotGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsServicesSnapshotsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[SnapshotGetListErrorBody](open_api_spec_for_click_house_cloud/errors/snapshot_get_list_error.py)&#93;</code>

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
<summary><code>def udf_attach(organization_id: UUID, function_name: str, service_id: UUID, *, body: V1OrganizationsUdfsAttachmentsServiceIdRequest | V1OrganizationsUdfsAttachmentsServiceIdRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUdfsAttachmentsServiceIdResponse</code></summary>

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
try:
    response = client.udf_api.udf_attach(organization_id, function_name, service_id)
    # TODO: Handle 'response' of type V1OrganizationsUdfsAttachmentsServiceIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfAttachErrorBody
```

**Async**

```python
try:
    response = await async_client.udf_api.udf_attach(organization_id, function_name, service_id)
    # TODO: Handle 'response' of type V1OrganizationsUdfsAttachmentsServiceIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfAttachErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUdfsAttachmentsServiceIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_response.py)</code> -- Current attachment state.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UdfAttachErrorBody](open_api_spec_for_click_house_cloud/errors/udf_attach_error.py)&#93;</code>

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
<summary><code>def udf_attachment_get(organization_id: UUID, function_name: str, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUdfsAttachmentsServiceIdResponse</code></summary>

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
try:
    response = client.udf_api.udf_attachment_get(organization_id, function_name, service_id)
    # TODO: Handle 'response' of type V1OrganizationsUdfsAttachmentsServiceIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfAttachmentGetErrorBody
```

**Async**

```python
try:
    response = await async_client.udf_api.udf_attachment_get(organization_id, function_name, service_id)
    # TODO: Handle 'response' of type V1OrganizationsUdfsAttachmentsServiceIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfAttachmentGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUdfsAttachmentsServiceIdResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_response.py)</code> -- Successful response.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UdfAttachmentGetErrorBody](open_api_spec_for_click_house_cloud/errors/udf_attachment_get_error.py)&#93;</code>

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
<summary><code>def udf_attachment_list(organization_id: UUID, function_name: str, *, cursor: str | None = None, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUdfsAttachmentsResponse</code></summary>

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
try:
    response = client.udf_api.udf_attachment_list(organization_id, function_name)
    # TODO: Handle 'response' of type V1OrganizationsUdfsAttachmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfAttachmentListErrorBody
```

**Async**

```python
try:
    response = await async_client.udf_api.udf_attachment_list(organization_id, function_name)
    # TODO: Handle 'response' of type V1OrganizationsUdfsAttachmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfAttachmentListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUdfsAttachmentsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_response.py)</code> -- Successful response.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UdfAttachmentListErrorBody](open_api_spec_for_click_house_cloud/errors/udf_attachment_list_error.py)&#93;</code>

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
<summary><code>def udf_create(organization_id: UUID, *, body: UdfCreateRequest2 | UdfCreateRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUdfsResponse</code></summary>

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
try:
    response = client.udf_api.udf_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsUdfsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.udf_api.udf_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsUdfsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUdfsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response.py)</code> -- UDF created and building.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UdfCreateErrorBody](open_api_spec_for_click_house_cloud/errors/udf_create_error.py)&#93;</code>

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
<summary><code>def udf_delete(organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUdfsResponse2</code></summary>

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
try:
    response = client.udf_api.udf_delete(organization_id, function_name)
    # TODO: Handle 'response' of type V1OrganizationsUdfsResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.udf_api.udf_delete(organization_id, function_name)
    # TODO: Handle 'response' of type V1OrganizationsUdfsResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUdfsResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response2.py)</code> -- UDF deleted.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UdfDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/udf_delete_error.py)&#93;</code>

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
<summary><code>def udf_detach(organization_id: UUID, function_name: str, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUdfsAttachmentsServiceIdResponse2</code></summary>

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
try:
    response = client.udf_api.udf_detach(organization_id, function_name, service_id)
    # TODO: Handle 'response' of type V1OrganizationsUdfsAttachmentsServiceIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfDetachErrorBody
```

**Async**

```python
try:
    response = await async_client.udf_api.udf_detach(organization_id, function_name, service_id)
    # TODO: Handle 'response' of type V1OrganizationsUdfsAttachmentsServiceIdResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfDetachErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUdfsAttachmentsServiceIdResponse2](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_response2.py)</code> -- UDF detached.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UdfDetachErrorBody](open_api_spec_for_click_house_cloud/errors/udf_detach_error.py)&#93;</code>

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
<summary><code>def udf_get(organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUdfsResponse</code></summary>

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
try:
    response = client.udf_api.udf_get(organization_id, function_name)
    # TODO: Handle 'response' of type V1OrganizationsUdfsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfGetErrorBody
```

**Async**

```python
try:
    response = await async_client.udf_api.udf_get(organization_id, function_name)
    # TODO: Handle 'response' of type V1OrganizationsUdfsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUdfsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response.py)</code> -- Successful response.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UdfGetErrorBody](open_api_spec_for_click_house_cloud/errors/udf_get_error.py)&#93;</code>

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
<summary><code>def udf_list(organization_id: UUID, *, cursor: str | None = None, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUdfsResponse1</code></summary>

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
try:
    response = client.udf_api.udf_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsUdfsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfListErrorBody
```

**Async**

```python
try:
    response = await async_client.udf_api.udf_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsUdfsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUdfsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response1.py)</code> -- Successful response.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UdfListErrorBody](open_api_spec_for_click_house_cloud/errors/udf_list_error.py)&#93;</code>

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
<summary><code>def udf_upload_session_create(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUdfUploadsUrlResponse</code></summary>

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
try:
    response = client.udf_api.udf_upload_session_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsUdfUploadsUrlResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfUploadSessionCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.udf_api.udf_upload_session_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsUdfUploadsUrlResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfUploadSessionCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUdfUploadsUrlResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udf_uploads_url_response.py)</code> -- Upload URL created.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UdfUploadSessionCreateErrorBody](open_api_spec_for_click_house_cloud/errors/udf_upload_session_create_error.py)&#93;</code>

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
<summary><code>def udf_version_create(organization_id: UUID, function_name: str, *, body: UdfVersionCreateRequest2 | UdfVersionCreateRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUdfsVersionsResponse</code></summary>

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
try:
    response = client.udf_api.udf_version_create(organization_id, function_name)
    # TODO: Handle 'response' of type V1OrganizationsUdfsVersionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfVersionCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.udf_api.udf_version_create(organization_id, function_name)
    # TODO: Handle 'response' of type V1OrganizationsUdfsVersionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfVersionCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUdfsVersionsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_response.py)</code> -- UDF version created and building.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UdfVersionCreateErrorBody](open_api_spec_for_click_house_cloud/errors/udf_version_create_error.py)&#93;</code>

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
<summary><code>def udf_version_delete(organization_id: UUID, function_name: str, version: int, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUdfsVersionsVersionResponse</code></summary>

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
try:
    response = client.udf_api.udf_version_delete(organization_id, function_name, version)
    # TODO: Handle 'response' of type V1OrganizationsUdfsVersionsVersionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfVersionDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.udf_api.udf_version_delete(organization_id, function_name, version)
    # TODO: Handle 'response' of type V1OrganizationsUdfsVersionsVersionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfVersionDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUdfsVersionsVersionResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_version_response.py)</code> -- UDF version deleted.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UdfVersionDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/udf_version_delete_error.py)&#93;</code>

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
<summary><code>def udf_version_list(organization_id: UUID, function_name: str, *, cursor: str | None = None, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsUdfsVersionsResponse1</code></summary>

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
try:
    response = client.udf_api.udf_version_list(organization_id, function_name)
    # TODO: Handle 'response' of type V1OrganizationsUdfsVersionsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfVersionListErrorBody
```

**Async**

```python
try:
    response = await async_client.udf_api.udf_version_list(organization_id, function_name)
    # TODO: Handle 'response' of type V1OrganizationsUdfsVersionsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UdfVersionListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsUdfsVersionsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_response1.py)</code> -- Successful response.

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[UdfVersionListErrorBody](open_api_spec_for_click_house_cloud/errors/udf_version_list_error.py)&#93;</code>

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
<summary><code>def invitation_create(organization_id: UUID, *, body: InvitationPostRequest | InvitationPostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsInvitationsResponse1</code></summary>

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
try:
    response = client.user_management.invitation_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsInvitationsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InvitationCreateErrorBody
```

**Async**

```python
try:
    response = await async_client.user_management.invitation_create(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsInvitationsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InvitationCreateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsInvitationsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InvitationCreateErrorBody](open_api_spec_for_click_house_cloud/errors/invitation_create_error.py)&#93;</code>

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
<summary><code>def invitation_delete(organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsInvitationsResponse3</code></summary>

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
try:
    response = client.user_management.invitation_delete(organization_id, invitation_id)
    # TODO: Handle 'response' of type V1OrganizationsInvitationsResponse3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InvitationDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.user_management.invitation_delete(organization_id, invitation_id)
    # TODO: Handle 'response' of type V1OrganizationsInvitationsResponse3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InvitationDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsInvitationsResponse3](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response3.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InvitationDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/invitation_delete_error.py)&#93;</code>

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
<summary><code>def invitation_get(organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsInvitationsResponse1</code></summary>

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
try:
    response = client.user_management.invitation_get(organization_id, invitation_id)
    # TODO: Handle 'response' of type V1OrganizationsInvitationsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InvitationGetErrorBody
```

**Async**

```python
try:
    response = await async_client.user_management.invitation_get(organization_id, invitation_id)
    # TODO: Handle 'response' of type V1OrganizationsInvitationsResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InvitationGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsInvitationsResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InvitationGetErrorBody](open_api_spec_for_click_house_cloud/errors/invitation_get_error.py)&#93;</code>

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
<summary><code>def invitation_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsInvitationsResponse</code></summary>

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
try:
    response = client.user_management.invitation_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsInvitationsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InvitationGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.user_management.invitation_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsInvitationsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InvitationGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsInvitationsResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[InvitationGetListErrorBody](open_api_spec_for_click_house_cloud/errors/invitation_get_list_error.py)&#93;</code>

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
<summary><code>def member_delete(organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsMembersResponse3</code></summary>

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
try:
    response = client.user_management.member_delete(organization_id, user_id)
    # TODO: Handle 'response' of type V1OrganizationsMembersResponse3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MemberDeleteErrorBody
```

**Async**

```python
try:
    response = await async_client.user_management.member_delete(organization_id, user_id)
    # TODO: Handle 'response' of type V1OrganizationsMembersResponse3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MemberDeleteErrorBody
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

**OnSuccess**: <code>[V1OrganizationsMembersResponse3](open_api_spec_for_click_house_cloud/models/v1_organizations_members_response3.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[MemberDeleteErrorBody](open_api_spec_for_click_house_cloud/errors/member_delete_error.py)&#93;</code>

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
<summary><code>def member_get(organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsMembersResponse1</code></summary>

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
try:
    response = client.user_management.member_get(organization_id, user_id)
    # TODO: Handle 'response' of type V1OrganizationsMembersResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MemberGetErrorBody
```

**Async**

```python
try:
    response = await async_client.user_management.member_get(organization_id, user_id)
    # TODO: Handle 'response' of type V1OrganizationsMembersResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MemberGetErrorBody
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

**OnSuccess**: <code>[V1OrganizationsMembersResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_members_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[MemberGetErrorBody](open_api_spec_for_click_house_cloud/errors/member_get_error.py)&#93;</code>

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
<summary><code>def member_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsMembersResponse</code></summary>

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
try:
    response = client.user_management.member_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsMembersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MemberGetListErrorBody
```

**Async**

```python
try:
    response = await async_client.user_management.member_get_list(organization_id)
    # TODO: Handle 'response' of type V1OrganizationsMembersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MemberGetListErrorBody
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

**OnSuccess**: <code>[V1OrganizationsMembersResponse](open_api_spec_for_click_house_cloud/models/v1_organizations_members_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[MemberGetListErrorBody](open_api_spec_for_click_house_cloud/errors/member_get_list_error.py)&#93;</code>

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
<summary><code>def member_update(organization_id: UUID, user_id: UUID, *, body: MemberPatchRequest | MemberPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> V1OrganizationsMembersResponse1</code></summary>

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
try:
    response = client.user_management.member_update(organization_id, user_id)
    # TODO: Handle 'response' of type V1OrganizationsMembersResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MemberUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.user_management.member_update(organization_id, user_id)
    # TODO: Handle 'response' of type V1OrganizationsMembersResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MemberUpdateErrorBody
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

**OnSuccess**: <code>[V1OrganizationsMembersResponse1](open_api_spec_for_click_house_cloud/models/v1_organizations_members_response1.py)</code> -- Successful response

**OnError**: <code>[ApiError](open_api_spec_for_click_house_cloud/core/exceptions.py)&#91;[MemberUpdateErrorBody](open_api_spec_for_click_house_cloud/errors/member_update_error.py)&#93;</code>

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

