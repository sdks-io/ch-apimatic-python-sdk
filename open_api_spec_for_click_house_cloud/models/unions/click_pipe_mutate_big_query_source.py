from __future__ import annotations

from typing import TypeAlias

from ..click_pipe_post_big_query_service_account_source import (
    ClickPipePostBigQueryServiceAccountSource,
    ClickPipePostBigQueryServiceAccountSourceDict,
)
from ..click_pipe_post_big_query_workload_identity_source import (
    ClickPipePostBigQueryWorkloadIdentitySource,
    ClickPipePostBigQueryWorkloadIdentitySourceDict,
)

ClickPipeMutateBigQuerySource: TypeAlias = (
    ClickPipePostBigQueryServiceAccountSource | ClickPipePostBigQueryWorkloadIdentitySource
)

ClickPipeMutateBigQuerySourceDict: TypeAlias = (
    ClickPipePostBigQueryServiceAccountSourceDict | ClickPipePostBigQueryWorkloadIdentitySourceDict
)
