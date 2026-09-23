from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NumericUnit(str, Enum):
    """Numeric unit for data, data rate, or throughput formats."""

    BYTES_IEC = "bytes_iec"
    BYTES_SI = "bytes_si"
    BITS_IEC = "bits_iec"
    BITS_SI = "bits_si"
    KIBIBYTES = "kibibytes"
    KILOBYTES = "kilobytes"
    MEBIBYTES = "mebibytes"
    MEGABYTES = "megabytes"
    GIBIBYTES = "gibibytes"
    GIGABYTES = "gigabytes"
    TEBIBYTES = "tebibytes"
    TERABYTES = "terabytes"
    PEBIBYTES = "pebibytes"
    PETABYTES = "petabytes"
    PACKETS_SEC = "packets_sec"
    BYTES_SEC_IEC = "bytes_sec_iec"
    BYTES_SEC_SI = "bytes_sec_si"
    BITS_SEC_IEC = "bits_sec_iec"
    BITS_SEC_SI = "bits_sec_si"
    KIBIBYTES_SEC = "kibibytes_sec"
    KIBIBITS_SEC = "kibibits_sec"
    KILOBYTES_SEC = "kilobytes_sec"
    KILOBITS_SEC = "kilobits_sec"
    MEBIBYTES_SEC = "mebibytes_sec"
    MEBIBITS_SEC = "mebibits_sec"
    MEGABYTES_SEC = "megabytes_sec"
    MEGABITS_SEC = "megabits_sec"
    GIBIBYTES_SEC = "gibibytes_sec"
    GIBIBITS_SEC = "gibibits_sec"
    GIGABYTES_SEC = "gigabytes_sec"
    GIGABITS_SEC = "gigabits_sec"
    TEBIBYTES_SEC = "tebibytes_sec"
    TEBIBITS_SEC = "tebibits_sec"
    TERABYTES_SEC = "terabytes_sec"
    TERABITS_SEC = "terabits_sec"
    PEBIBYTES_SEC = "pebibytes_sec"
    PEBIBITS_SEC = "pebibits_sec"
    PETABYTES_SEC = "petabytes_sec"
    PETABITS_SEC = "petabits_sec"
    CPS = "cps"
    OPS = "ops"
    RPS = "rps"
    READS_SEC = "reads_sec"
    WPS = "wps"
    IOPS = "iops"
    CPM = "cpm"
    OPM = "opm"
    RPM_READS = "rpm_reads"
    WPM = "wpm"

    __str__ = str.__str__


NumericUnitOrStr: TypeAlias = Annotated[NumericUnit | str, open_enum_validator(NumericUnit)]
