from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type7(str, Enum):
    """Type of the Postgres source. Defaults to "postgres" if not specified."""

    POSTGRES = "postgres"
    SUPABASE = "supabase"
    NEON = "neon"
    ALLOYDB = "alloydb"
    PLANETSCALE = "planetscale"
    RDSPOSTGRES = "rdspostgres"
    AURORAPOSTGRES = "aurorapostgres"
    CLOUDSQLPOSTGRES = "cloudsqlpostgres"
    AZUREPOSTGRES = "azurepostgres"
    CRUNCHYBRIDGE = "crunchybridge"
    TIGERDATA = "tigerdata"

    __str__ = str.__str__


Type7OrStr: TypeAlias = Annotated[Type7 | str, open_enum_validator(Type7)]
