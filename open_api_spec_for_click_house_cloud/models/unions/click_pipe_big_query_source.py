from __future__ import annotations

from typing import TypeAlias

from ..click_pipe_big_query_service_account_source import (
    ClickPipeBigQueryServiceAccountSource,
    ClickPipeBigQueryServiceAccountSourceDict,
)
from ..click_pipe_big_query_workload_identity_source import (
    ClickPipeBigQueryWorkloadIdentitySource,
    ClickPipeBigQueryWorkloadIdentitySourceDict,
)

ClickPipeBigQuerySource: TypeAlias = ClickPipeBigQueryServiceAccountSource | ClickPipeBigQueryWorkloadIdentitySource

ClickPipeBigQuerySourceDict: TypeAlias = (
    ClickPipeBigQueryServiceAccountSourceDict | ClickPipeBigQueryWorkloadIdentitySourceDict
)
