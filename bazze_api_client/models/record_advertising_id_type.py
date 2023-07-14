from enum import Enum


class RecordAdvertisingIdType(str, Enum):
    IDFA = "idfa"
    IDFV = "idfv"
    GAID = "gaid"

    def __str__(self) -> str:
        return str(self.value)
