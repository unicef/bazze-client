import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..datatypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_bill_identity_price_vendors_item import QueryBillIdentityPriceVendorsItem


T = TypeVar("T", bound="QueryBillIdentityPrice")


@attr.s(auto_attribs=True)
class QueryBillIdentityPrice:
    """
    Attributes:
        query_id (Union[Unset, str]):  Example: 54445f05-0105-4a58-b32f-b99f3938f388.
        timestamp (Union[Unset, datetime.datetime]):  Example: 2022-06-02T15:39:20+00:00.
        type (Union[Unset, str]):  Example: identity_data.
        vendors (Union[Unset, List['QueryBillIdentityPriceVendorsItem']]):
    """

    query_id: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, str] = UNSET
    vendors: Union[Unset, List["QueryBillIdentityPriceVendorsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query_id = self.query_id
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        type = self.type
        vendors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vendors, Unset):
            vendors = []
            for vendors_item_data in self.vendors:
                vendors_item = vendors_item_data.to_dict()

                vendors.append(vendors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query_id is not UNSET:
            field_dict["query_id"] = query_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if type is not UNSET:
            field_dict["type"] = type
        if vendors is not UNSET:
            field_dict["vendors"] = vendors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_bill_identity_price_vendors_item import QueryBillIdentityPriceVendorsItem

        d = src_dict.copy()
        query_id = d.pop("query_id", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        type = d.pop("type", UNSET)

        vendors = []
        _vendors = d.pop("vendors", UNSET)
        for vendors_item_data in _vendors or []:
            vendors_item = QueryBillIdentityPriceVendorsItem.from_dict(vendors_item_data)

            vendors.append(vendors_item)

        query_bill_identity_price = cls(
            query_id=query_id,
            timestamp=timestamp,
            type=type,
            vendors=vendors,
        )

        query_bill_identity_price.additional_properties = d
        return query_bill_identity_price

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
