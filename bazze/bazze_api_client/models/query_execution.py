from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
import sys 
sys.path.insert(0, '..')

##from datatypes import UNSET, Unset
from ..datatypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_execution_status import QueryExecutionStatus


T = TypeVar("T", bound="QueryExecution")


@attr.s(auto_attribs=True)
class QueryExecution:
    """
    Attributes:
        query_execution_id (str):  Example: 54445f05-0105-4a58-b32f-b99f3938f388.
        status (Union[Unset, QueryExecutionStatus]):
    """

    query_execution_id: str
    status: Union[Unset, "QueryExecutionStatus"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query_execution_id = self.query_execution_id
        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "QueryExecutionId": query_execution_id,
            }
        )
        if status is not UNSET:
            field_dict["Status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_execution_status import QueryExecutionStatus

        d = src_dict.copy()
        query_execution_id = d.pop("QueryExecutionId")

        _status = d.pop("Status", UNSET)
        status: Union[Unset, QueryExecutionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = QueryExecutionStatus.from_dict(_status)

        query_execution = cls(
            query_execution_id=query_execution_id,
            status=status,
        )

        query_execution.additional_properties = d
        return query_execution

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
