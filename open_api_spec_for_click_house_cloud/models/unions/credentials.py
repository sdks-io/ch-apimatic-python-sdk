from __future__ import annotations

from typing import TypeAlias

from ..azure_event_hub import AzureEventHub, AzureEventHubDict
from ..msk_iam_user import MskIamUser, MskIamUserDict
from ..mutual_tls import MutualTls, MutualTlsDict
from ..plain import Plain, PlainDict

Credentials: TypeAlias = Plain | MskIamUser | AzureEventHub | MutualTls
"""Credentials for Kafka source. Choose one that is supported by the authentication method."""

CredentialsDict: TypeAlias = PlainDict | MskIamUserDict | AzureEventHubDict | MutualTlsDict
