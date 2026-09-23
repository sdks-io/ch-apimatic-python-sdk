<!-- Generated file — do not edit; regenerated with the SDK. -->

# UdfApi — operations

Accessor: `client.udf_api` · Source: `open_api_spec_for_click_house_cloud/apis/udf_api.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.udf_api.udf_attach

- **Route**: `PUT /v1/organizations/{organizationId}/udfs/{functionName}/attachments/{serviceId}`
- **Auth**: `basic_auth`
- **Signature**: `def udf_attach(organization_id: UUID, function_name: str, service_id: UUID, *, body: V1OrganizationsUdfsAttachmentsServiceIdRequest | V1OrganizationsUdfsAttachmentsServiceIdRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `function_name`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `function_name` — path `functionName` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsUdfsAttachmentsServiceIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsUdfsAttachmentsServiceIdResponse, UdfAttachErrorBody]`
- **Error**: `UdfAttachErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUdfsAttachmentsServiceId400Error1` [400] · `V1OrganizationsUdfsAttachmentsServiceId404Error1` [404] · `V1OrganizationsUdfsAttachmentsServiceId409Error1` [409] · `V1OrganizationsUdfsAttachmentsServiceId422Error1` [422] · `V1OrganizationsUdfsAttachmentsServiceId424Error1` [424] · `V1OrganizationsUdfsAttachmentsServiceId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsUdfsAttachmentsServiceIdRequest` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_request.py` |
| `V1OrganizationsUdfsAttachmentsServiceIdRequestDict` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_request.py` |
| `V1OrganizationsUdfsAttachmentsServiceIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_response.py` |
| `UdfAttachErrorBody` | `open_api_spec_for_click_house_cloud/errors/udf_attach_error.py` |
| `V1OrganizationsUdfsAttachmentsServiceId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id400_error1.py` |
| `V1OrganizationsUdfsAttachmentsServiceId404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id404_error1.py` |
| `V1OrganizationsUdfsAttachmentsServiceId409Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id409_error1.py` |
| `V1OrganizationsUdfsAttachmentsServiceId422Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id422_error1.py` |
| `V1OrganizationsUdfsAttachmentsServiceId424Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id424_error1.py` |
| `V1OrganizationsUdfsAttachmentsServiceId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id500_error1.py` |

### client.udf_api.udf_attachment_get

- **Route**: `GET /v1/organizations/{organizationId}/udfs/{functionName}/attachments/{serviceId}`
- **Auth**: `basic_auth`
- **Signature**: `def udf_attachment_get(organization_id: UUID, function_name: str, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `function_name`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `function_name` — path `functionName` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsUdfsAttachmentsServiceIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsUdfsAttachmentsServiceIdResponse, UdfAttachmentGetErrorBody]`
- **Error**: `UdfAttachmentGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUdfsAttachmentsServiceId400Error21` [400] · `V1OrganizationsUdfsAttachmentsServiceId404Error1` [404] · `V1OrganizationsUdfsAttachmentsServiceId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsUdfsAttachmentsServiceIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_response.py` |
| `UdfAttachmentGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/udf_attachment_get_error.py` |
| `V1OrganizationsUdfsAttachmentsServiceId400Error21` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id400_error21.py` |
| `V1OrganizationsUdfsAttachmentsServiceId404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id404_error1.py` |
| `V1OrganizationsUdfsAttachmentsServiceId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id500_error1.py` |

### client.udf_api.udf_attachment_list

- **Route**: `GET /v1/organizations/{organizationId}/udfs/{functionName}/attachments`
- **Auth**: `basic_auth`
- **Signature**: `def udf_attachment_list(organization_id: UUID, function_name: str, *, cursor: str | None = None, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `function_name`
- **Params**: `organization_id` — path `organizationId` · `function_name` — path `functionName` · `cursor` — query · `limit` — query
- **Returns (parsed)**: `V1OrganizationsUdfsAttachmentsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsUdfsAttachmentsResponse, UdfAttachmentListErrorBody]`
- **Error**: `UdfAttachmentListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUdfsAttachments400Error1` [400] · `V1OrganizationsUdfsAttachments404Error1` [404] · `V1OrganizationsUdfsAttachments500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsUdfsAttachmentsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_response.py` |
| `UdfAttachmentListErrorBody` | `open_api_spec_for_click_house_cloud/errors/udf_attachment_list_error.py` |
| `V1OrganizationsUdfsAttachments400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments400_error1.py` |
| `V1OrganizationsUdfsAttachments404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments404_error1.py` |
| `V1OrganizationsUdfsAttachments500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments500_error1.py` |

### client.udf_api.udf_create

- **Route**: `POST /v1/organizations/{organizationId}/udfs`
- **Auth**: `basic_auth`
- **Signature**: `def udf_create(organization_id: UUID, *, body: UdfCreateRequest2 | UdfCreateRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsUdfsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsUdfsResponse, UdfCreateErrorBody]`
- **Error**: `UdfCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUdfs400Error1` [400] · `V1OrganizationsUdfs403Error1` [403] · `V1OrganizationsUdfs409Error1` [409] · `V1OrganizationsUdfs410Error1` [410] · `V1OrganizationsUdfs500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UdfCreateRequest2` | `open_api_spec_for_click_house_cloud/models/unions/udf_create_request2.py` |
| `UdfCreateRequest2Dict` | `open_api_spec_for_click_house_cloud/models/unions/udf_create_request2.py` |
| `V1OrganizationsUdfsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response.py` |
| `UdfCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/udf_create_error.py` |
| `V1OrganizationsUdfs400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs400_error1.py` |
| `V1OrganizationsUdfs403Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs403_error1.py` |
| `V1OrganizationsUdfs409Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs409_error1.py` |
| `V1OrganizationsUdfs410Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs410_error1.py` |
| `V1OrganizationsUdfs500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs500_error1.py` |

### client.udf_api.udf_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/udfs/{functionName}`
- **Auth**: `basic_auth`
- **Signature**: `def udf_delete(organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `function_name`
- **Params**: `organization_id` — path `organizationId` · `function_name` — path `functionName`
- **Returns (parsed)**: `V1OrganizationsUdfsResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsUdfsResponse2, UdfDeleteErrorBody]`
- **Error**: `UdfDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUdfs400Error1` [400] · `V1OrganizationsUdfs404Error1` [404] · `V1OrganizationsUdfs409Error1` [409] · `V1OrganizationsUdfs500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsUdfsResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response2.py` |
| `UdfDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/udf_delete_error.py` |
| `V1OrganizationsUdfs400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs400_error1.py` |
| `V1OrganizationsUdfs404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs404_error1.py` |
| `V1OrganizationsUdfs409Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs409_error1.py` |
| `V1OrganizationsUdfs500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs500_error1.py` |

### client.udf_api.udf_detach

- **Route**: `DELETE /v1/organizations/{organizationId}/udfs/{functionName}/attachments/{serviceId}`
- **Auth**: `basic_auth`
- **Signature**: `def udf_detach(organization_id: UUID, function_name: str, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `function_name`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `function_name` — path `functionName` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsUdfsAttachmentsServiceIdResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsUdfsAttachmentsServiceIdResponse2, UdfDetachErrorBody]`
- **Error**: `UdfDetachErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUdfsAttachmentsServiceId400Error21` [400] · `V1OrganizationsUdfsAttachmentsServiceId404Error1` [404] · `V1OrganizationsUdfsAttachmentsServiceId409Error1` [409] · `V1OrganizationsUdfsAttachmentsServiceId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsUdfsAttachmentsServiceIdResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id_response2.py` |
| `UdfDetachErrorBody` | `open_api_spec_for_click_house_cloud/errors/udf_detach_error.py` |
| `V1OrganizationsUdfsAttachmentsServiceId400Error21` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id400_error21.py` |
| `V1OrganizationsUdfsAttachmentsServiceId404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id404_error1.py` |
| `V1OrganizationsUdfsAttachmentsServiceId409Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id409_error1.py` |
| `V1OrganizationsUdfsAttachmentsServiceId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_attachments_service_id500_error1.py` |

### client.udf_api.udf_get

- **Route**: `GET /v1/organizations/{organizationId}/udfs/{functionName}`
- **Auth**: `basic_auth`
- **Signature**: `def udf_get(organization_id: UUID, function_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `function_name`
- **Params**: `organization_id` — path `organizationId` · `function_name` — path `functionName`
- **Returns (parsed)**: `V1OrganizationsUdfsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsUdfsResponse, UdfGetErrorBody]`
- **Error**: `UdfGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUdfs400Error1` [400] · `V1OrganizationsUdfs404Error1` [404] · `V1OrganizationsUdfs500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsUdfsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response.py` |
| `UdfGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/udf_get_error.py` |
| `V1OrganizationsUdfs400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs400_error1.py` |
| `V1OrganizationsUdfs404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs404_error1.py` |
| `V1OrganizationsUdfs500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs500_error1.py` |

### client.udf_api.udf_list

- **Route**: `GET /v1/organizations/{organizationId}/udfs`
- **Auth**: `basic_auth`
- **Signature**: `def udf_list(organization_id: UUID, *, cursor: str | None = None, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `cursor` — query · `limit` — query
- **Returns (parsed)**: `V1OrganizationsUdfsResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsUdfsResponse1, UdfListErrorBody]`
- **Error**: `UdfListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUdfs400Error1` [400] · `V1OrganizationsUdfs500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsUdfsResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_response1.py` |
| `UdfListErrorBody` | `open_api_spec_for_click_house_cloud/errors/udf_list_error.py` |
| `V1OrganizationsUdfs400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs400_error1.py` |
| `V1OrganizationsUdfs500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs500_error1.py` |

### client.udf_api.udf_upload_session_create

- **Route**: `POST /v1/organizations/{organizationId}/udfUploads/url`
- **Auth**: `basic_auth`
- **Signature**: `def udf_upload_session_create(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId`
- **Returns (parsed)**: `V1OrganizationsUdfUploadsUrlResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsUdfUploadsUrlResponse, UdfUploadSessionCreateErrorBody]`
- **Error**: `UdfUploadSessionCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUdfUploadsUrl400Error1` [400] · `V1OrganizationsUdfUploadsUrl500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsUdfUploadsUrlResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udf_uploads_url_response.py` |
| `UdfUploadSessionCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/udf_upload_session_create_error.py` |
| `V1OrganizationsUdfUploadsUrl400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udf_uploads_url400_error1.py` |
| `V1OrganizationsUdfUploadsUrl500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udf_uploads_url500_error1.py` |

### client.udf_api.udf_version_create

- **Route**: `POST /v1/organizations/{organizationId}/udfs/{functionName}/versions`
- **Auth**: `basic_auth`
- **Signature**: `def udf_version_create(organization_id: UUID, function_name: str, *, body: UdfVersionCreateRequest2 | UdfVersionCreateRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `function_name`
- **Params**: `organization_id` — path `organizationId` · `function_name` — path `functionName` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsUdfsVersionsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsUdfsVersionsResponse, UdfVersionCreateErrorBody]`
- **Error**: `UdfVersionCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUdfsVersions400Error1` [400] · `V1OrganizationsUdfsVersions403Error1` [403] · `V1OrganizationsUdfsVersions404Error1` [404] · `V1OrganizationsUdfsVersions409Error1` [409] · `V1OrganizationsUdfsVersions410Error1` [410] · `V1OrganizationsUdfsVersions500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UdfVersionCreateRequest2` | `open_api_spec_for_click_house_cloud/models/unions/udf_version_create_request2.py` |
| `UdfVersionCreateRequest2Dict` | `open_api_spec_for_click_house_cloud/models/unions/udf_version_create_request2.py` |
| `V1OrganizationsUdfsVersionsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_response.py` |
| `UdfVersionCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/udf_version_create_error.py` |
| `V1OrganizationsUdfsVersions400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions400_error1.py` |
| `V1OrganizationsUdfsVersions403Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions403_error1.py` |
| `V1OrganizationsUdfsVersions404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions404_error1.py` |
| `V1OrganizationsUdfsVersions409Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions409_error1.py` |
| `V1OrganizationsUdfsVersions410Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions410_error1.py` |
| `V1OrganizationsUdfsVersions500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions500_error1.py` |

### client.udf_api.udf_version_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/udfs/{functionName}/versions/{version}`
- **Auth**: `basic_auth`
- **Signature**: `def udf_version_delete(organization_id: UUID, function_name: str, version: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `function_name`, `version`
- **Params**: `organization_id` — path `organizationId` · `function_name` — path `functionName` · `version` — path
- **Returns (parsed)**: `V1OrganizationsUdfsVersionsVersionResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsUdfsVersionsVersionResponse, UdfVersionDeleteErrorBody]`
- **Error**: `UdfVersionDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUdfsVersionsVersion400Error1` [400] · `V1OrganizationsUdfsVersionsVersion404Error1` [404] · `V1OrganizationsUdfsVersionsVersion409Error1` [409] · `V1OrganizationsUdfsVersionsVersion500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsUdfsVersionsVersionResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_version_response.py` |
| `UdfVersionDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/udf_version_delete_error.py` |
| `V1OrganizationsUdfsVersionsVersion400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_version400_error1.py` |
| `V1OrganizationsUdfsVersionsVersion404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_version404_error1.py` |
| `V1OrganizationsUdfsVersionsVersion409Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_version409_error1.py` |
| `V1OrganizationsUdfsVersionsVersion500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_version500_error1.py` |

### client.udf_api.udf_version_list

- **Route**: `GET /v1/organizations/{organizationId}/udfs/{functionName}/versions`
- **Auth**: `basic_auth`
- **Signature**: `def udf_version_list(organization_id: UUID, function_name: str, *, cursor: str | None = None, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `function_name`
- **Params**: `organization_id` — path `organizationId` · `function_name` — path `functionName` · `cursor` — query · `limit` — query
- **Returns (parsed)**: `V1OrganizationsUdfsVersionsResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsUdfsVersionsResponse1, UdfVersionListErrorBody]`
- **Error**: `UdfVersionListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUdfsVersions400Error1` [400] · `V1OrganizationsUdfsVersions404Error1` [404] · `V1OrganizationsUdfsVersions500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsUdfsVersionsResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions_response1.py` |
| `UdfVersionListErrorBody` | `open_api_spec_for_click_house_cloud/errors/udf_version_list_error.py` |
| `V1OrganizationsUdfsVersions400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions400_error1.py` |
| `V1OrganizationsUdfsVersions404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions404_error1.py` |
| `V1OrganizationsUdfsVersions500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_udfs_versions500_error1.py` |

