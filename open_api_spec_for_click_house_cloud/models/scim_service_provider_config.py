from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scim_authentication_scheme import ScimAuthenticationScheme, ScimAuthenticationSchemeDict
from .scim_boolean_feature import ScimBooleanFeature, ScimBooleanFeatureDict
from .scim_service_provider_config_bulk import ScimServiceProviderConfigBulk, ScimServiceProviderConfigBulkDict
from .scim_service_provider_config_filter import ScimServiceProviderConfigFilter, ScimServiceProviderConfigFilterDict
from .scim_service_provider_config_meta import ScimServiceProviderConfigMeta, ScimServiceProviderConfigMetaDict
from .scim_service_provider_config_patch import ScimServiceProviderConfigPatch, ScimServiceProviderConfigPatchDict


class ScimServiceProviderConfig(SdkBaseModel):
    schemas: list[str]
    """SCIM schema URIs."""

    documentation_uri: Optional[str] = Field(default=UNSET, alias="documentationUri")
    """URI of the service documentation."""

    patch: ScimServiceProviderConfigPatch
    bulk: ScimServiceProviderConfigBulk
    filter: ScimServiceProviderConfigFilter
    change_password: ScimBooleanFeature = Field(alias="changePassword")
    sort: ScimBooleanFeature
    etag: ScimBooleanFeature
    authentication_schemes: list[ScimAuthenticationScheme] = Field(alias="authenticationSchemes")
    """Supported authentication schemes."""

    meta: ScimServiceProviderConfigMeta


class ScimServiceProviderConfigDict(TypedDict):
    schemas: list[str]
    documentation_uri: NotRequired[str]
    patch: ScimServiceProviderConfigPatchDict
    bulk: ScimServiceProviderConfigBulkDict
    filter: ScimServiceProviderConfigFilterDict
    change_password: ScimBooleanFeatureDict
    sort: ScimBooleanFeatureDict
    etag: ScimBooleanFeatureDict
    authentication_schemes: list[ScimAuthenticationSchemeDict]
    meta: ScimServiceProviderConfigMetaDict
