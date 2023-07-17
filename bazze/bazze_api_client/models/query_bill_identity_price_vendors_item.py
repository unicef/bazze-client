from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..datatypes import UNSET, Unset

T = TypeVar("T", bound="QueryBillIdentityPriceVendorsItem")


@attr.s(auto_attribs=True)
class QueryBillIdentityPriceVendorsItem:
    """
    Attributes:
        search_cost (Union[Unset, str]):  Example: $1.00.
        totalhits (Union[Unset, int]):  Example: 3.
        vendor_id (Union[Unset, str]):  Example: bobstay.
    """

    search_cost: Union[Unset, str] = UNSET
    totalhits: Union[Unset, int] = UNSET
    vendor_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        search_cost = self.search_cost
        totalhits = self.totalhits
        vendor_id = self.vendor_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_cost is not UNSET:
            field_dict["search_cost"] = search_cost
        if totalhits is not UNSET:
            field_dict["totalhits"] = totalhits
        if vendor_id is not UNSET:
            field_dict["vendor_id"] = vendor_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        search_cost = d.pop("search_cost", UNSET)

        totalhits = d.pop("totalhits", UNSET)

        vendor_id = d.pop("vendor_id", UNSET)

        query_bill_identity_price_vendors_item = cls(
            search_cost=search_cost,
            totalhits=totalhits,
            vendor_id=vendor_id,
        )

        query_bill_identity_price_vendors_item.additional_properties = d
        return query_bill_identity_price_vendors_item

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
