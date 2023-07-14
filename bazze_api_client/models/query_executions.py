from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_execution import QueryExecution


T = TypeVar("T", bound="QueryExecutions")


@attr.s(auto_attribs=True)
class QueryExecutions:
    """
    Attributes:
        next_token (Union[Unset, str]):  Example: AWBKGKBqYFG9GYKeeHpK9IRHaOcMNIn3fevS1gNkK48Ic8ziMPQomqGP07djwWTVA/MWcw
            5O/VLv4WDPNACH9J+hA9qfI7G1Oc7lXDcS+CygMwzxSJA7WFA5fFOtO9Osjmqvc8CrjEm4bcM0dUMktpAHvbL8ty87/w==.
        query_executions (Union[Unset, List['QueryExecution']]):
    """

    next_token: Union[Unset, str] = UNSET
    query_executions: Union[Unset, List["QueryExecution"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_token = self.next_token
        query_executions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.query_executions, Unset):
            query_executions = []
            for query_executions_item_data in self.query_executions:
                query_executions_item = query_executions_item_data.to_dict()

                query_executions.append(query_executions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_token is not UNSET:
            field_dict["next_token"] = next_token
        if query_executions is not UNSET:
            field_dict["query_executions"] = query_executions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_execution import QueryExecution

        d = src_dict.copy()
        next_token = d.pop("next_token", UNSET)

        query_executions = []
        _query_executions = d.pop("query_executions", UNSET)
        for query_executions_item_data in _query_executions or []:
            query_executions_item = QueryExecution.from_dict(query_executions_item_data)

            query_executions.append(query_executions_item)

        query_executions = cls(
            next_token=next_token,
            query_executions=query_executions,
        )

        query_executions.additional_properties = d
        return query_executions

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
