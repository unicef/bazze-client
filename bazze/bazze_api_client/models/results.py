from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..datatypes import UNSET, Unset

T = TypeVar("T", bound="Results")


@attr.s(auto_attribs=True)
class Results:
    """
    Attributes:
        csv (Union[Unset, str]):  Example: https://bazze.link/154f.
        json (Union[Unset, str]):  Example: https://bazze.link/ffcf.
    """

    csv: Union[Unset, str] = UNSET
    json: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        csv = self.csv
        json = self.json

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if csv is not UNSET:
            field_dict["csv"] = csv
        if json is not UNSET:
            field_dict["json"] = json

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        csv = d.pop("csv", UNSET)

        json = d.pop("json", UNSET)

        results = cls(
            csv=csv,
            json=json,
        )

        results.additional_properties = d
        return results

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
