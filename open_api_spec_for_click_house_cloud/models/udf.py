from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.runtime4 import Runtime4OrStr
from .enums.sandbox_type4 import SandboxType4OrStr
from .enums.sandbox_version4 import SandboxVersion4OrStr
from .enums.status4 import Status4OrStr
from .enums.type22 import Type22OrStr
from .udf_argument_output import UdfArgumentOutput, UdfArgumentOutputDict


class Udf(SdkBaseModel):
    function_name: str = Field(alias="functionName")
    """Name of the UDF. Unique within the organization."""

    version: int
    """Version number of the UDF."""

    status: Status4OrStr
    """Build state of this UDF version."""

    runtime: Runtime4OrStr
    """Runtime used to execute the UDF command."""

    type_: Type22OrStr = Field(alias="type")
    """Executable UDF type."""

    arguments: list[UdfArgumentOutput]
    """Arguments passed to the UDF command."""

    return_type: str = Field(alias="returnType")
    """ClickHouse data type of the returned value."""

    return_name: str = Field(alias="returnName")
    """Name of the returned value, or null when unnamed."""

    pool_size: int = Field(alias="poolSize")
    """Command pool size for executable_pool UDFs."""

    command_read_timeout: int = Field(alias="commandReadTimeout")
    """Command stdout read timeout in milliseconds."""

    command_write_timeout: int = Field(alias="commandWriteTimeout")
    """Command stdin write timeout in milliseconds."""

    max_command_execution_time: int = Field(alias="maxCommandExecutionTime")
    """Maximum command execution time in seconds for executable_pool UDFs."""

    memory_limit_mib: int = Field(alias="memoryLimitMib")
    """Maximum memory, in MiB, available to each UDF sandbox process. Null uses the sandbox default."""

    send_chunk_header: bool = Field(alias="sendChunkHeader")
    """Whether ClickHouse sends a row-count chunk header."""

    deterministic: bool
    """Whether ClickHouse may reuse cached query results for this UDF."""

    format: str
    """Input and output format used by the UDF command."""

    sandbox_type: SandboxType4OrStr = Field(alias="sandboxType")
    """Sandbox isolation level."""

    sandbox_version: SandboxVersion4OrStr = Field(alias="sandboxVersion")
    """Sandbox runtime version."""

    error: str
    """Build error, or null when no build error is present."""

    created_at: RFC3339DateTime = Field(alias="createdAt")
    """Creation timestamp."""

    updated_at: RFC3339DateTime = Field(alias="updatedAt")
    """Last-update timestamp."""


class UdfDict(TypedDict):
    function_name: str
    version: int
    status: Status4OrStr
    runtime: Runtime4OrStr
    type_: Type22OrStr
    arguments: list[UdfArgumentOutputDict]
    return_type: str
    return_name: str
    pool_size: int
    command_read_timeout: int
    command_write_timeout: int
    max_command_execution_time: int
    memory_limit_mib: int
    send_chunk_header: bool
    deterministic: bool
    format: str
    sandbox_type: SandboxType4OrStr
    sandbox_version: SandboxVersion4OrStr
    error: str
    created_at: RFC3339DateTime
    updated_at: RFC3339DateTime
