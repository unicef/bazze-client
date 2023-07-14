from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateRange")


@attr.s(auto_attribs=True)
class DateRange:
    """
    Attributes:
        from_date (Union[Unset, str]):  Example: 2021-06-11T23:59:59+00:00.
        to_date (Union[Unset, str]):  Example: 2021-06-09T23:59:59+00:00.
    """

    from_date: Union[Unset, str] = UNSET
    to_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_date = self.from_date
        to_date = self.to_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_date is not UNSET:
            field_dict["from_date"] = from_date
        if to_date is not UNSET:
            field_dict["to_date"] = to_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_date = d.pop("from_date", UNSET)

        to_date = d.pop("to_date", UNSET)

        date_range = cls(
            from_date=from_date,
            to_date=to_date,
        )

        date_range.additional_properties = d
        return date_range

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
