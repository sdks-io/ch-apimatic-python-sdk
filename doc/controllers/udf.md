# UDF

```python
udf_api = client.udf
```

## Class Name

`UdfApi`

## Methods

* [Udf Attach](../../doc/controllers/udf.md#udf-attach)
* [Udf Attachment Get](../../doc/controllers/udf.md#udf-attachment-get)
* [Udf Detach](../../doc/controllers/udf.md#udf-detach)
* [Udf Attachment List](../../doc/controllers/udf.md#udf-attachment-list)
* [Udf Create](../../doc/controllers/udf.md#udf-create)
* [Udf List](../../doc/controllers/udf.md#udf-list)
* [Udf Delete](../../doc/controllers/udf.md#udf-delete)
* [Udf Get](../../doc/controllers/udf.md#udf-get)
* [Udf Upload Session Create](../../doc/controllers/udf.md#udf-upload-session-create)
* [Udf Version Create](../../doc/controllers/udf.md#udf-version-create)
* [Udf Version List](../../doc/controllers/udf.md#udf-version-list)
* [Udf Version Delete](../../doc/controllers/udf.md#udf-version-delete)


# Udf Attach

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Attaches one UDF version to a service, replacing the current version when necessary. When version is omitted, the latest ready version is attached.

```python
def udf_attach(self,
              organization_id,
              function_name,
              service_id,
              body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `function_name` | `str` | Template, Required | Name of the UDF.<br><br>**Constraints**: *Pattern*: `^[A-Za-z][A-Za-z0-9_]*$` |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |
| `body` | [`V1OrganizationsUdfsAttachmentsServiceIdRequest`](../../doc/models/v1-organizations-udfs-attachments-service-id-request.md) | Body, Optional | - |

## Response Type

**200**: Current attachment state.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUdfsAttachmentsServiceIdResponse`](../../doc/models/v1-organizations-udfs-attachments-service-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

function_name = 'functionName2'

service_id = '00000060-0000-0000-0000-000000000000'

body = V1OrganizationsUdfsAttachmentsServiceIdRequest(
    version=1
)

result = udf_api.udf_attach(
    organization_id,
    function_name,
    service_id,
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
| 400 | The service does not support UDFs. | [`V1OrganizationsUdfsAttachmentsServiceId400ErrorException`](../../doc/models/v1-organizations-udfs-attachments-service-id-400-error-exception.md) |
| 404 | UDF, version, or service not found. | [`V1OrganizationsUdfsAttachmentsServiceId404ErrorException`](../../doc/models/v1-organizations-udfs-attachments-service-id-404-error-exception.md) |
| 409 | The requested version is not ready or another attachment transition is in progress. | [`V1OrganizationsUdfsAttachmentsServiceId409ErrorException`](../../doc/models/v1-organizations-udfs-attachments-service-id-409-error-exception.md) |
| 422 | Service UDF attachment limit exceeded. | [`V1OrganizationsUdfsAttachmentsServiceId422ErrorException`](../../doc/models/v1-organizations-udfs-attachments-service-id-422-error-exception.md) |
| 424 | The service must be running before the UDF can be attached. | [`V1OrganizationsUdfsAttachmentsServiceId424ErrorException`](../../doc/models/v1-organizations-udfs-attachments-service-id-424-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUdfsAttachmentsServiceId500ErrorException`](../../doc/models/v1-organizations-udfs-attachments-service-id-500-error-exception.md) |


# Udf Attachment Get

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current attachment of a UDF to one service.

```python
def udf_attachment_get(self,
                      organization_id,
                      function_name,
                      service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `function_name` | `str` | Template, Required | Name of the UDF.<br><br>**Constraints**: *Pattern*: `^[A-Za-z][A-Za-z0-9_]*$` |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |

## Response Type

**200**: Successful response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUdfsAttachmentsServiceIdResponse`](../../doc/models/v1-organizations-udfs-attachments-service-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

function_name = 'functionName2'

service_id = '00000060-0000-0000-0000-000000000000'

result = udf_api.udf_attachment_get(
    organization_id,
    function_name,
    service_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsUdfsAttachmentsServiceId400Error2Exception`](../../doc/models/v1-organizations-udfs-attachments-service-id-400-error-2-exception.md) |
| 404 | UDF not found or not attached to this service. | [`V1OrganizationsUdfsAttachmentsServiceId404ErrorException`](../../doc/models/v1-organizations-udfs-attachments-service-id-404-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUdfsAttachmentsServiceId500ErrorException`](../../doc/models/v1-organizations-udfs-attachments-service-id-500-error-exception.md) |


# Udf Detach

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Detaches a UDF from a service.

```python
def udf_detach(self,
              organization_id,
              function_name,
              service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `function_name` | `str` | Template, Required | Name of the UDF.<br><br>**Constraints**: *Pattern*: `^[A-Za-z][A-Za-z0-9_]*$` |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |

## Response Type

**200**: UDF detached.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUdfsAttachmentsServiceIdResponse2`](../../doc/models/v1-organizations-udfs-attachments-service-id-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

function_name = 'functionName2'

service_id = '00000060-0000-0000-0000-000000000000'

result = udf_api.udf_detach(
    organization_id,
    function_name,
    service_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsUdfsAttachmentsServiceId400Error2Exception`](../../doc/models/v1-organizations-udfs-attachments-service-id-400-error-2-exception.md) |
| 404 | UDF not found. | [`V1OrganizationsUdfsAttachmentsServiceId404ErrorException`](../../doc/models/v1-organizations-udfs-attachments-service-id-404-error-exception.md) |
| 409 | An attachment transition is already in progress. | [`V1OrganizationsUdfsAttachmentsServiceId409ErrorException`](../../doc/models/v1-organizations-udfs-attachments-service-id-409-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUdfsAttachmentsServiceId500ErrorException`](../../doc/models/v1-organizations-udfs-attachments-service-id-500-error-exception.md) |


# Udf Attachment List

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current service attachments for a UDF, with at most one attachment per service.

```python
def udf_attachment_list(self,
                       organization_id,
                       function_name,
                       cursor=None,
                       limit=100)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `function_name` | `str` | Template, Required | Name of the UDF.<br><br>**Constraints**: *Pattern*: `^[A-Za-z][A-Za-z0-9_]*$` |
| `cursor` | `str` | Query, Optional | Cursor returned in `pagination.nextCursor` from the previous page. |
| `limit` | `int` | Query, Optional | Maximum number of records to return per page. Defaults to 100. Maximum is 100.<br><br>**Default**: `100`<br><br>**Constraints**: `>= 1`, `<= 100` |

## Response Type

**200**: Successful response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUdfsAttachmentsResponse`](../../doc/models/v1-organizations-udfs-attachments-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

function_name = 'functionName2'

limit = 100

result = udf_api.udf_attachment_list(
    organization_id,
    function_name,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsUdfsAttachments400ErrorException`](../../doc/models/v1-organizations-udfs-attachments-400-error-exception.md) |
| 404 | UDF not found. | [`V1OrganizationsUdfsAttachments404ErrorException`](../../doc/models/v1-organizations-udfs-attachments-404-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUdfsAttachments500ErrorException`](../../doc/models/v1-organizations-udfs-attachments-500-error-exception.md) |


# Udf Create

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates a new UDF. See [User-defined functions in Cloud](https://clickhouse.com/docs/products/cloud/features/sql-console-features/user-defined-functions).

```python
def udf_create(self,
              organization_id,
              body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `body` | [UdfCreateRequest](../../doc/models/udf-create-request.md) \| [UdfCreateRequest1](../../doc/models/udf-create-request-1.md) \| None | Body, Optional | - |

## Response Type

**201**: UDF created and building.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUdfsResponse`](../../doc/models/v1-organizations-udfs-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

body = UdfCreateRequest(
    upload_id='000017c4-0000-0000-0000-000000000000',
    runtime=Runtime.ENUM_PYTHON311,
    arguments=[
        UdfArgument(
            name='name8',
            mtype='type2'
        )
    ],
    return_type='returnType2',
    function_name='functionName2',
    command_read_timeout=10000,
    command_write_timeout=10000,
    send_chunk_header=False,
    deterministic=False,
    format='TabSeparated',
    sandbox_type=SandboxType.BASIC,
    sandbox_version=SandboxVersion.V2
)

result = udf_api.udf_create(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsUdfs400ErrorException`](../../doc/models/v1-organizations-udfs-400-error-exception.md) |
| 403 | Requested UDF features are not enabled. | [`V1OrganizationsUdfs403ErrorException`](../../doc/models/v1-organizations-udfs-403-error-exception.md) |
| 409 | The function name already exists. | [`V1OrganizationsUdfs409ErrorException`](../../doc/models/v1-organizations-udfs-409-error-exception.md) |
| 410 | The source archive is unavailable. | [`V1OrganizationsUdfs410ErrorException`](../../doc/models/v1-organizations-udfs-410-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUdfs500ErrorException`](../../doc/models/v1-organizations-udfs-500-error-exception.md) |


# Udf List

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the latest version of each UDF in the organization.

```python
def udf_list(self,
            organization_id,
            cursor=None,
            limit=100)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `cursor` | `str` | Query, Optional | Cursor returned in `pagination.nextCursor` from the previous page. |
| `limit` | `int` | Query, Optional | Maximum number of records to return per page. Defaults to 100. Maximum is 100.<br><br>**Default**: `100`<br><br>**Constraints**: `>= 1`, `<= 100` |

## Response Type

**200**: Successful response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUdfsResponse1`](../../doc/models/v1-organizations-udfs-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

limit = 100

result = udf_api.udf_list(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsUdfs400ErrorException`](../../doc/models/v1-organizations-udfs-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUdfs500ErrorException`](../../doc/models/v1-organizations-udfs-500-error-exception.md) |


# Udf Delete

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes every version of a UDF and detaches it from all services. Removal from services completes asynchronously.

```python
def udf_delete(self,
              organization_id,
              function_name)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `function_name` | `str` | Template, Required | Name of the UDF.<br><br>**Constraints**: *Pattern*: `^[A-Za-z][A-Za-z0-9_]*$` |

## Response Type

**200**: UDF deleted.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUdfsResponse2`](../../doc/models/v1-organizations-udfs-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

function_name = 'functionName2'

result = udf_api.udf_delete(
    organization_id,
    function_name
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsUdfs400ErrorException`](../../doc/models/v1-organizations-udfs-400-error-exception.md) |
| 404 | UDF not found. | [`V1OrganizationsUdfs404ErrorException`](../../doc/models/v1-organizations-udfs-404-error-exception.md) |
| 409 | A UDF version is still building. | [`V1OrganizationsUdfs409ErrorException`](../../doc/models/v1-organizations-udfs-409-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUdfs500ErrorException`](../../doc/models/v1-organizations-udfs-500-error-exception.md) |


# Udf Get

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the latest version of a UDF.

```python
def udf_get(self,
           organization_id,
           function_name)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `function_name` | `str` | Template, Required | Name of the UDF.<br><br>**Constraints**: *Pattern*: `^[A-Za-z][A-Za-z0-9_]*$` |

## Response Type

**200**: Successful response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUdfsResponse`](../../doc/models/v1-organizations-udfs-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

function_name = 'functionName2'

result = udf_api.udf_get(
    organization_id,
    function_name
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsUdfs400ErrorException`](../../doc/models/v1-organizations-udfs-400-error-exception.md) |
| 404 | UDF not found. | [`V1OrganizationsUdfs404ErrorException`](../../doc/models/v1-organizations-udfs-404-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUdfs500ErrorException`](../../doc/models/v1-organizations-udfs-500-error-exception.md) |


# Udf Upload Session Create

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates an org-scoped presigned application/zip upload URL. Callers must use an upload ID for only one create or version attempt and request a new upload URL when retrying.

```python
def udf_upload_session_create(self,
                             organization_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |

## Response Type

**201**: Upload URL created.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUdfUploadsUrlResponse`](../../doc/models/v1-organizations-udf-uploads-url-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = udf_api.udf_upload_session_create(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsUdfUploadsUrl400ErrorException`](../../doc/models/v1-organizations-udf-uploads-url-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUdfUploadsUrl500ErrorException`](../../doc/models/v1-organizations-udf-uploads-url-500-error-exception.md) |


# Udf Version Create

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Consumes a source archive, assigns a version, and starts the UDF build. Optional configuration fields omitted from the request use the defaults documented in the request schema; values are not inherited from the previous version. Retry by requesting a new upload URL and re-uploading.

```python
def udf_version_create(self,
                      organization_id,
                      function_name,
                      body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `function_name` | `str` | Template, Required | Name of the UDF.<br><br>**Constraints**: *Pattern*: `^[A-Za-z][A-Za-z0-9_]*$` |
| `body` | [UdfVersionCreateRequest](../../doc/models/udf-version-create-request.md) \| [UdfVersionCreateRequest1](../../doc/models/udf-version-create-request-1.md) \| None | Body, Optional | - |

## Response Type

**201**: UDF version created and building.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUdfsVersionsResponse`](../../doc/models/v1-organizations-udfs-versions-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

function_name = 'functionName2'

body = UdfVersionCreateRequest(
    upload_id='0000139a-0000-0000-0000-000000000000',
    runtime=Runtime.ENUM_PYTHON311,
    arguments=[
        UdfArgument(
            name='name8',
            mtype='type2'
        )
    ],
    return_type='returnType6',
    command_read_timeout=10000,
    command_write_timeout=10000,
    send_chunk_header=False,
    deterministic=False,
    format='TabSeparated',
    sandbox_type=SandboxType.BASIC,
    sandbox_version=SandboxVersion.V2
)

result = udf_api.udf_version_create(
    organization_id,
    function_name,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsUdfsVersions400ErrorException`](../../doc/models/v1-organizations-udfs-versions-400-error-exception.md) |
| 403 | Requested UDF features are not enabled. | [`V1OrganizationsUdfsVersions403ErrorException`](../../doc/models/v1-organizations-udfs-versions-403-error-exception.md) |
| 404 | UDF not found. | [`V1OrganizationsUdfsVersions404ErrorException`](../../doc/models/v1-organizations-udfs-versions-404-error-exception.md) |
| 409 | A concurrent request conflicted with this request. | [`V1OrganizationsUdfsVersions409ErrorException`](../../doc/models/v1-organizations-udfs-versions-409-error-exception.md) |
| 410 | The source archive is unavailable. | [`V1OrganizationsUdfsVersions410ErrorException`](../../doc/models/v1-organizations-udfs-versions-410-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUdfsVersions500ErrorException`](../../doc/models/v1-organizations-udfs-versions-500-error-exception.md) |


# Udf Version List

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns all versions of a UDF.

```python
def udf_version_list(self,
                    organization_id,
                    function_name,
                    cursor=None,
                    limit=100)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `function_name` | `str` | Template, Required | Name of the UDF.<br><br>**Constraints**: *Pattern*: `^[A-Za-z][A-Za-z0-9_]*$` |
| `cursor` | `str` | Query, Optional | Cursor returned in `pagination.nextCursor` from the previous page. |
| `limit` | `int` | Query, Optional | Maximum number of records to return per page. Defaults to 100. Maximum is 100.<br><br>**Default**: `100`<br><br>**Constraints**: `>= 1`, `<= 100` |

## Response Type

**200**: Successful response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUdfsVersionsResponse1`](../../doc/models/v1-organizations-udfs-versions-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

function_name = 'functionName2'

limit = 100

result = udf_api.udf_version_list(
    organization_id,
    function_name,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsUdfsVersions400ErrorException`](../../doc/models/v1-organizations-udfs-versions-400-error-exception.md) |
| 404 | UDF not found. | [`V1OrganizationsUdfsVersions404ErrorException`](../../doc/models/v1-organizations-udfs-versions-404-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUdfsVersions500ErrorException`](../../doc/models/v1-organizations-udfs-versions-500-error-exception.md) |


# Udf Version Delete

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes a UDF version. The UDF must not be attached to any services.

```python
def udf_version_delete(self,
                      organization_id,
                      function_name,
                      version)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `function_name` | `str` | Template, Required | Name of the UDF.<br><br>**Constraints**: *Pattern*: `^[A-Za-z][A-Za-z0-9_]*$` |
| `version` | `int` | Template, Required | Version number of the UDF.<br><br>**Constraints**: `>= 1` |

## Response Type

**200**: UDF version deleted.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUdfsVersionsVersionResponse`](../../doc/models/v1-organizations-udfs-versions-version-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

function_name = 'functionName2'

version = 1

result = udf_api.udf_version_delete(
    organization_id,
    function_name,
    version
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsUdfsVersionsVersion400ErrorException`](../../doc/models/v1-organizations-udfs-versions-version-400-error-exception.md) |
| 404 | UDF or version not found. | [`V1OrganizationsUdfsVersionsVersion404ErrorException`](../../doc/models/v1-organizations-udfs-versions-version-404-error-exception.md) |
| 409 | The UDF version is the latest version, is attached to a service, or is still building. | [`V1OrganizationsUdfsVersionsVersion409ErrorException`](../../doc/models/v1-organizations-udfs-versions-version-409-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUdfsVersionsVersion500ErrorException`](../../doc/models/v1-organizations-udfs-versions-version-500-error-exception.md) |

