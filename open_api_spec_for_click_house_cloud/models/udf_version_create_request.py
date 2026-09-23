from __future__ import annotations

from typing import Literal
from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.runtime import RuntimeOrStr
from .enums.sandbox_type import SandboxType, SandboxTypeOrStr
from .enums.sandbox_version import SandboxVersion, SandboxVersionOrStr
from .udf_argument import UdfArgument, UdfArgumentDict


class UdfVersionCreateRequest(SdkBaseModel):
    upload_id: UUID = Field(alias="uploadId")
    """Identifier of the uploaded source archive."""

    runtime: RuntimeOrStr
    arguments: list[UdfArgument]
    return_type: str = Field(alias="returnType")
    return_name: Optional[str] = Field(default=UNSET, alias="returnName")
    command_read_timeout: int = Field(default=10000, alias="commandReadTimeout")
    command_write_timeout: int = Field(default=10000, alias="commandWriteTimeout")
    memory_limit_mib: Optional[int] = Field(default=UNSET, alias="memoryLimitMib")
    send_chunk_header: bool = Field(default=False, alias="sendChunkHeader")
    deterministic: bool = False
    """Marks the UDF as deterministic so ClickHouse can reuse cached query results. Only set this when the UDF always
    returns the same result for the same arguments."""

    format: str = "TabSeparated"
    sandbox_type: SandboxTypeOrStr = Field(default=SandboxType.BASIC, alias="sandboxType")
    sandbox_version: SandboxVersionOrStr = Field(default=SandboxVersion.V2, alias="sandboxVersion")
    type_: Literal["executable"] = Field(default="executable", alias="type")
    pool_size: OptionalNullable[str] = Field(default=UNSET, alias="poolSize")
    """Always null — an executable UDF has no command pool."""

    max_command_execution_time: Optional[int] = Field(default=UNSET, alias="maxCommandExecutionTime")


class UdfVersionCreateRequestDict(TypedDict):
    upload_id: UUID
    runtime: RuntimeOrStr
    arguments: list[UdfArgumentDict]
    return_type: str
    return_name: NotRequired[str]
    command_read_timeout: NotRequired[int]
    command_write_timeout: NotRequired[int]
    memory_limit_mib: NotRequired[int]
    send_chunk_header: NotRequired[bool]
    deterministic: NotRequired[bool]
    format: NotRequired[str]
    sandbox_type: NotRequired[SandboxTypeOrStr]
    sandbox_version: NotRequired[SandboxVersionOrStr]
    type_: Literal["executable"]
    pool_size: NotRequired[str | None]
    max_command_execution_time: NotRequired[int]
