from __future__ import annotations

from typing import TypeAlias

from ..udf_create_request import UdfCreateRequest, UdfCreateRequestDict
from ..udf_create_request1 import UdfCreateRequest1, UdfCreateRequest1Dict

UdfCreateRequest2: TypeAlias = UdfCreateRequest | UdfCreateRequest1

UdfCreateRequest2Dict: TypeAlias = UdfCreateRequestDict | UdfCreateRequest1Dict
