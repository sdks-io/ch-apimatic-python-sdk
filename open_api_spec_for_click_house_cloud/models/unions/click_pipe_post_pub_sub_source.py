from __future__ import annotations

from typing import TypeAlias

from ..click_pipe_post_pub_sub_service_account_source import (
    ClickPipePostPubSubServiceAccountSource,
    ClickPipePostPubSubServiceAccountSourceDict,
)
from ..click_pipe_post_pub_sub_workload_identity_source import (
    ClickPipePostPubSubWorkloadIdentitySource,
    ClickPipePostPubSubWorkloadIdentitySourceDict,
)

ClickPipePostPubSubSource: TypeAlias = (
    ClickPipePostPubSubServiceAccountSource | ClickPipePostPubSubWorkloadIdentitySource
)

ClickPipePostPubSubSourceDict: TypeAlias = (
    ClickPipePostPubSubServiceAccountSourceDict | ClickPipePostPubSubWorkloadIdentitySourceDict
)
