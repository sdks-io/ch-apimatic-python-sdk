from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scim_user_address import ScimUserAddress, ScimUserAddressDict
from .scim_user_email import ScimUserEmail, ScimUserEmailDict
from .scim_user_entitlement import ScimUserEntitlement, ScimUserEntitlementDict
from .scim_user_group import ScimUserGroup, ScimUserGroupDict
from .scim_user_im import ScimUserIm, ScimUserImDict
from .scim_user_meta import ScimUserMeta, ScimUserMetaDict
from .scim_user_name import ScimUserName, ScimUserNameDict
from .scim_user_phone_number import ScimUserPhoneNumber, ScimUserPhoneNumberDict
from .scim_user_photo import ScimUserPhoto, ScimUserPhotoDict
from .scim_user_role import ScimUserRole, ScimUserRoleDict
from .scim_x509_certificate import ScimX509Certificate, ScimX509CertificateDict


class ScimUser(SdkBaseModel):
    schemas: list[str]
    """SCIM schemas URIs. Should include "urn:ietf:params:scim:schemas:core:2.0:User"."""

    id: str
    """Unique identifier for the SCIM resource. Returned by the server."""

    external_id: Optional[str] = Field(default=UNSET, alias="externalId")
    """A String that is an identifier for the resource as defined by the provisioning client."""

    user_name: str = Field(alias="userName")
    """Unique identifier for the User, typically used by the user to directly authenticate to the service provider."""

    name: ScimUserName
    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    """The name of the User, suitable for display to end-users."""

    nick_name: Optional[str] = Field(default=UNSET, alias="nickName")
    """The casual way to address the user in real life."""

    profile_url: Optional[str] = Field(default=UNSET, alias="profileUrl")
    """A fully qualified URL pointing to a page representing the User's online profile."""

    title: Optional[str] = UNSET
    """The User's title, such as "Vice President"."""

    user_type: Optional[str] = Field(default=UNSET, alias="userType")
    """Identifies the relationship between the organization and the user."""

    preferred_language: Optional[str] = Field(default=UNSET, alias="preferredLanguage")
    """Indicates the User's preferred written or spoken language (e.g., "en-US")."""

    locale: Optional[str] = UNSET
    """Used to indicate the User's default location for localizing items such as currency, date time format, or
    numerical representations (e.g., "en-US")."""

    timezone: Optional[str] = UNSET
    """The User's time zone in the "Olson" time zone database format (e.g., "America/Los_Angeles")."""

    active: bool
    """A Boolean value indicating the User's administrative status."""

    emails: list[ScimUserEmail]
    """Email addresses for the user."""

    phone_numbers: Optional[list[ScimUserPhoneNumber]] = Field(default=UNSET, alias="phoneNumbers")
    """Phone numbers for the User."""

    ims: Optional[list[ScimUserIm]] = UNSET
    """Instant messaging addresses for the User."""

    photos: Optional[list[ScimUserPhoto]] = UNSET
    """URLs of photos of the User."""

    addresses: Optional[list[ScimUserAddress]] = UNSET
    """Physical mailing addresses for the User."""

    groups: Optional[list[ScimUserGroup]] = UNSET
    """A list of groups to which the user belongs, either through direct membership, through nested groups, or
    dynamically calculated."""

    entitlements: Optional[list[ScimUserEntitlement]] = UNSET
    """A list of entitlements for the user that represent a thing the user has."""

    roles: Optional[list[ScimUserRole]] = UNSET
    """A list of roles for the user that collectively represent who the user is, e.g. "Student", "Faculty". No
    vocabulary or syntax is specified; role value is a string or label representing a collection of entitlements. RFC
    7643."""

    x509_certificates: Optional[list[ScimX509Certificate]] = Field(default=UNSET, alias="x509Certificates")
    """A list of certificates issued to the User."""

    meta: ScimUserMeta


class ScimUserDict(TypedDict):
    schemas: list[str]
    id: str
    external_id: NotRequired[str]
    user_name: str
    name: ScimUserNameDict
    display_name: NotRequired[str]
    nick_name: NotRequired[str]
    profile_url: NotRequired[str]
    title: NotRequired[str]
    user_type: NotRequired[str]
    preferred_language: NotRequired[str]
    locale: NotRequired[str]
    timezone: NotRequired[str]
    active: bool
    emails: list[ScimUserEmailDict]
    phone_numbers: NotRequired[list[ScimUserPhoneNumberDict]]
    ims: NotRequired[list[ScimUserImDict]]
    photos: NotRequired[list[ScimUserPhotoDict]]
    addresses: NotRequired[list[ScimUserAddressDict]]
    groups: NotRequired[list[ScimUserGroupDict]]
    entitlements: NotRequired[list[ScimUserEntitlementDict]]
    roles: NotRequired[list[ScimUserRoleDict]]
    x509_certificates: NotRequired[list[ScimX509CertificateDict]]
    meta: ScimUserMetaDict
