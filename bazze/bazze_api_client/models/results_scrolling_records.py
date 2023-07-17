from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..datatypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record import Record


T = TypeVar("T", bound="ResultsScrollingRecords")


@attr.s(auto_attribs=True)
class ResultsScrollingRecords:
    """
    Attributes:
        query_execution_id (str):  Example: 472bf5f-ca6f-4897-b936-fb980694d095.
        results (List['Record']):
        next_token (Union[Unset, str]):  Example:
            AUB1qOPL1oO2n7lcC3CiANqHsPRIcPwUhK5yFlcVs+Sq20SUJ7DJqbvbF3N9TikGKCLWqRn4IrwZSmVc6K7MCvB/9ooRt5bDnw==.
    """

    query_execution_id: str
    results: List["Record"]
    next_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query_execution_id = self.query_execution_id
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()

            results.append(results_item)

        next_token = self.next_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "QueryExecutionId": query_execution_id,
                "results": results,
            }
        )
        if next_token is not UNSET:
            field_dict["NextToken"] = next_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record import Record

        d = src_dict.copy()
        query_execution_id = d.pop("QueryExecutionId")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = Record.from_dict(results_item_data)

            results.append(results_item)

        next_token = d.pop("NextToken", UNSET)

        results_scrolling_records = cls(
            query_execution_id=query_execution_id,
            results=results,
            next_token=next_token,
        )

        results_scrolling_records.additional_properties = d
        return results_scrolling_records

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
