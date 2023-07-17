from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..datatypes import UNSET, Unset

T = TypeVar("T", bound="QueryExecutionScrolling")


@attr.s(auto_attribs=True)
class QueryExecutionScrolling:
    """
    Attributes:
        query_execution_id (str):  Example: 54445f05-0105-4a58-b32f-b99f3938f388.
        max_results (Union[Unset, int]):  Example: 1000.
        next_token (Union[Unset, str]):  Example:
            AUB1qOPL1oO2n7lcC3CiANqHsPRIcPwUhK5yFlcVs+Sq20SUJ7DJqbvbF3N9TikGKCLWqRn4IrwZSmVc6K7MCvB/9ooRt5bDnw==.
    """

    query_execution_id: str
    max_results: Union[Unset, int] = UNSET
    next_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query_execution_id = self.query_execution_id
        max_results = self.max_results
        next_token = self.next_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "QueryExecutionId": query_execution_id,
            }
        )
        if max_results is not UNSET:
            field_dict["MaxResults"] = max_results
        if next_token is not UNSET:
            field_dict["NextToken"] = next_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query_execution_id = d.pop("QueryExecutionId")

        max_results = d.pop("MaxResults", UNSET)

        next_token = d.pop("NextToken", UNSET)

        query_execution_scrolling = cls(
            query_execution_id=query_execution_id,
            max_results=max_results,
            next_token=next_token,
        )

        query_execution_scrolling.additional_properties = d
        return query_execution_scrolling

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
