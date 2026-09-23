<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — OpenAPI spec for ClickHouse Cloud (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | OpenAPI spec for ClickHouse Cloud |
| Root package | `open_api_spec_for_click_house_cloud` |
| Distribution name | `ch-apimatic-sdk` |
| Requires | Python 3.10 or later |
| API spec version | `1.0` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from open_api_spec_for_click_house_cloud import OpenApiSpecForClickHouseCloudClient
from open_api_spec_for_click_house_cloud.core import BasicAuthCredentials

client = OpenApiSpecForClickHouseCloudClient(
    basic_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD")
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with OpenApiSpecForClickHouseCloudClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run

from open_api_spec_for_click_house_cloud import AsyncOpenApiSpecForClickHouseCloudClient
from open_api_spec_for_click_house_cloud.core import BasicAuthCredentials


async def main() -> None:
    client = AsyncOpenApiSpecForClickHouseCloudClient(
        basic_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD")
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncOpenApiSpecForClickHouseCloudClient(...) as client:` closes the pool on exit.

`AsyncClient` (`open_api_spec_for_click_house_cloud/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `OpenApiSpecForClickHouseCloudClient` and `AsyncOpenApiSpecForClickHouseCloudClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.api_keys`). Every constructor argument is optional and keyword-only. Sources: `open_api_spec_for_click_house_cloud/client.py`, `open_api_spec_for_click_house_cloud/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `base_url` | `str \| None` | `str \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `basic_auth` | `BasicAuthCredentialsOrDict \| None` | `BasicAuthCredentialsOrDict \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `HttpClient` | `open_api_spec_for_click_house_cloud.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()` |
| `BasicAuthCredentialsOrDict` | `open_api_spec_for_click_house_cloud.core` | `BasicAuthCredentials` or a dict: `username: str` · `password: str` |
| `AsyncHttpClient` | `open_api_spec_for_click_house_cloud.core` | protocol — `async send(request: HttpRequest) -> HttpResponse` · `async aclose()` |

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.response`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `open_api_spec_for_click_house_cloud/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`open_api_spec_for_click_house_cloud/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse`.

Core runtime types (`open_api_spec_for_click_house_cloud/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `open_api_spec_for_click_house_cloud/errors/` or `RawError` | `error: E` · `status_code: int` · `response: HttpResponse` | `open_api_spec_for_click_house_cloud/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `response: HttpResponse` (on both) | `open_api_spec_for_click_house_cloud/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse` | `open_api_spec_for_click_house_cloud/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
from open_api_spec_for_click_house_cloud.core import ApiError, RawError
from open_api_spec_for_click_house_cloud.models import V1OrganizationsKeys400Error1

try:
    response = client.api_keys.openapi_key_create(organization_id)
except ApiError as e:
    # Case A — typed error: e.error is OpenapiKeyCreateErrorBody
    if isinstance(e.error, V1OrganizationsKeys400Error1):
        # Handle 400
        print(e.error)
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **157 operations**, **157 are Case A (typed)** and **0 are Case B (raw)**.

---

## Operations — by controller (14 pages, 157 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every *generated* type it names, with the module that declares it. A runtime type — a file alias, a date/time or byte converter — is not listed there.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout or extra headers; every signature ends with it | here (`open_api_spec_for_click_house_cloud/core/request_options.py`) |
| **Base URL `https://api.clickhouse.cloud`** — this SDK's only server; override it with `base_url="https://…"` | Servers & auth |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client.api_keys` | 5 | [map/operations/api_keys.md](map/operations/api_keys.md) |
| `client.backup_api` | 8 | [map/operations/backup_api.md](map/operations/backup_api.md) |
| `client.billing` | 3 | [map/operations/billing.md](map/operations/billing.md) |
| `client.click_pipes` | 18 | [map/operations/click_pipes.md](map/operations/click_pipes.md) |
| `client.click_stack` | 30 | [map/operations/click_stack.md](map/operations/click_stack.md) |
| `client.organization_api` | 11 | [map/operations/organization_api.md](map/operations/organization_api.md) |
| `client.postgres` | 17 | [map/operations/postgres.md](map/operations/postgres.md) |
| `client.prometheus` | 5 | [map/operations/prometheus.md](map/operations/prometheus.md) |
| `client.query_api_endpoints` | 5 | [map/operations/query_api_endpoints.md](map/operations/query_api_endpoints.md) |
| `client.role_management` | 5 | [map/operations/role_management.md](map/operations/role_management.md) |
| `client.service_api` | 26 | [map/operations/service_api.md](map/operations/service_api.md) |
| `client.snapshot_api` | 4 | [map/operations/snapshot_api.md](map/operations/snapshot_api.md) |
| `client.udf_api` | 12 | [map/operations/udf_api.md](map/operations/udf_api.md) |
| `client.user_management` | 8 | [map/operations/user_management.md](map/operations/user_management.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `open_api_spec_for_click_house_cloud/models/` declares one type plus its input companion, and every module under `open_api_spec_for_click_house_cloud/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`ActiveBalance` ↔ `active_balance.py`; an error alias drops its `Body` suffix: `ActiveBalancesGetErrorBody` ↔ `active_balances_get_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 819 | `open_api_spec_for_click_house_cloud/models/` |
| Enums (`Enum` over `str` / `int`) — Python member names + wire values | 143 | `open_api_spec_for_click_house_cloud/models/enums/` |
| Unions (plain) — `TypeAlias` over the arms | 60 | `open_api_spec_for_click_house_cloud/models/unions/` |
| Error aliases (one per Case A operation) | 157 | `open_api_spec_for_click_house_cloud/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`remaining_prepaid_credits` ↔ `"remainingPrepaidCredits"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model, enum and union also has an **input companion**, exported beside it from the same package (`ActiveBalance` ↔ `ActiveBalanceDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str` / `int`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`ActorType` ↔ `ActorTypeOrStr`) and additionally accepts a wire value this SDK version does not know. A union is a `TypeAlias` over its arms.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `open_api_spec_for_click_house_cloud` |
| Operation controllers | `open_api_spec_for_click_house_cloud.apis` |
| Models | `open_api_spec_for_click_house_cloud.models` |
| Enums | `open_api_spec_for_click_house_cloud.models.enums` |
| Unions | `open_api_spec_for_click_house_cloud.models.unions`, `open_api_spec_for_click_house_cloud.models` |
| Error aliases | `open_api_spec_for_click_house_cloud.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `open_api_spec_for_click_house_cloud.core` |

---

## Servers & auth

**Basic auth.** Pass `basic_auth={"username": …, "password": …}`, or a `BasicAuthCredentials`.

Operation blocks name their scheme in an **Auth** bullet; an operation whose spec declares no scheme carries no such bullet.

- `AND` — every scheme listed must be configured for the call to succeed.
- `OR` — any one of the schemes listed can be used; the first one you configured is the one sent, in the order listed.

A scheme you did not configure is skipped silently rather than raising, and the request is sent anyway — so an authentication failure can mean no credential was sent rather than a bad one.

**One environment, one server** (`open_api_spec_for_click_house_cloud/server/server_config.py`). The spec declares a single environment, so no `environment` keyword exists; the base URL and its override point:

| Base URL | Override point |
| --- | --- |
| `https://api.clickhouse.cloud` | `base_url="https://…"` |

