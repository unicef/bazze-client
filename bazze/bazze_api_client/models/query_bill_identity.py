from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..datatypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_bill_identity_price import QueryBillIdentityPrice


T = TypeVar("T", bound="QueryBillIdentity")


@attr.s(auto_attribs=True)
class QueryBillIdentity:
    """
    Attributes:
        api_user (Union[Unset, str]):  Example: test_user.
        price (Union[Unset, QueryBillIdentityPrice]):
    """

    api_user: Union[Unset, str] = UNSET
    price: Union[Unset, "QueryBillIdentityPrice"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_user = self.api_user
        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_user is not UNSET:
            field_dict["api_user"] = api_user
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_bill_identity_price import QueryBillIdentityPrice

        d = src_dict.copy()
        api_user = d.pop("api_user", UNSET)

        _price = d.pop("price", UNSET)
        price: Union[Unset, QueryBillIdentityPrice]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = QueryBillIdentityPrice.from_dict(_price)

        query_bill_identity = cls(
            api_user=api_user,
            price=price,
        )

        query_bill_identity.additional_properties = d
        return query_bill_identity

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
