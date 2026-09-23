from __future__ import annotations

from typing import TypeAlias

from ..udf_version_create_request import UdfVersionCreateRequest, UdfVersionCreateRequestDict
from ..udf_version_create_request1 import UdfVersionCreateRequest1, UdfVersionCreateRequest1Dict

UdfVersionCreateRequest2: TypeAlias = UdfVersionCreateRequest | UdfVersionCreateRequest1

UdfVersionCreateRequest2Dict: TypeAlias = UdfVersionCreateRequestDict | UdfVersionCreateRequest1Dict
