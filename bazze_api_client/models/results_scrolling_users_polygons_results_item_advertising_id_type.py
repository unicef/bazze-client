from enum import Enum


class ResultsScrollingUsersPolygonsResultsItemAdvertisingIdType(str, Enum):
    IDFA = "idfa"
    IDFV = "idfv"
    GAID = "gaid"

    def __str__(self) -> str:
        return str(self.value)
