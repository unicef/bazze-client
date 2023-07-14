from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryBillsPagination")


@attr.s(auto_attribs=True)
class QueryBillsPagination:
    """
    Attributes:
        next_token (Union[Unset, str]):  Example: AWBKGKBqYFG9GYKeeHpK9IRHaOcMNIn3fevS1gNkK48Ic8ziMPQomqGP07djwWTVA/MWcw
            5O/VLv4WDPNACH9J+hA9qfI7G1Oc7lXDcS+CygMwzxSJA7WFA5fFOtO9Osjmqvc8CrjEm4bcM0dUMktpAHvbL8ty87/w==.
    """

    next_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_token = self.next_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_token is not UNSET:
            field_dict["next_token"] = next_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        next_token = d.pop("next_token", UNSET)

        query_bills_pagination = cls(
            next_token=next_token,
        )

        query_bills_pagination.additional_properties = d
        return query_bills_pagination

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
