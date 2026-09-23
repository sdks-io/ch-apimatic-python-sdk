from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Format4(str, Enum):
    """Format of the files."""

    JSON_EACH_ROW = "JSONEachRow"
    JSONAS_OBJECT = "JSONAsObject"
    CSV = "CSV"
    CSV_WITH_NAMES = "CSVWithNames"
    TAB_SEPARATED = "TabSeparated"
    TAB_SEPARATED_WITH_NAMES = "TabSeparatedWithNames"
    PARQUET = "Parquet"
    AVRO = "Avro"

    __str__ = str.__str__


Format4OrStr: TypeAlias = Annotated[Format4 | str, open_enum_validator(Format4)]
