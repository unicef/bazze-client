import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_bill_location_price import QueryBillLocationPrice


T = TypeVar("T", bound="QueryBillLocation")


@attr.s(auto_attribs=True)
class QueryBillLocation:
    """
    Attributes:
        api_user (Union[Unset, str]):  Example: test_user.
        price (Union[Unset, QueryBillLocationPrice]):
        query_id (Union[Unset, str]):  Example: 54445f05-0105-4a58-b32f-b99f3938f388.
        timestamp (Union[Unset, datetime.datetime]):  Example: 2022-06-02T15:39:20+00:00.
    """

    api_user: Union[Unset, str] = UNSET
    price: Union[Unset, "QueryBillLocationPrice"] = UNSET
    query_id: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_user = self.api_user
        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        query_id = self.query_id
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_user is not UNSET:
            field_dict["api_user"] = api_user
        if price is not UNSET:
            field_dict["price"] = price
        if query_id is not UNSET:
            field_dict["query_id"] = query_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_bill_location_price import QueryBillLocationPrice

        d = src_dict.copy()
        api_user = d.pop("api_user", UNSET)

        _price = d.pop("price", UNSET)
        price: Union[Unset, QueryBillLocationPrice]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = QueryBillLocationPrice.from_dict(_price)

        query_id = d.pop("query_id", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        query_bill_location = cls(
            api_user=api_user,
            price=price,
            query_id=query_id,
            timestamp=timestamp,
        )

        query_bill_location.additional_properties = d
        return query_bill_location

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
