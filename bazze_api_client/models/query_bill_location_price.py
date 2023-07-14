from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryBillLocationPrice")


@attr.s(auto_attribs=True)
class QueryBillLocationPrice:
    """
    Attributes:
        dollars_per_km2_day (Union[Unset, str]):  Example: 0.019.
        dollars_per_selector_day (Union[Unset, str]):  Example: 0.035.
        location_search_cost (Union[Unset, str]):
        num_days (Union[Unset, str]):  Example: 5.
        num_km2 (Union[Unset, str]):
        num_selectors (Union[Unset, str]):  Example: 2.
        selector_search_cost (Union[Unset, str]):  Example: 0.7.
        tier (Union[Unset, str]):  Example: Small.
        total_search_cost (Union[Unset, str]):  Example: 0.7.
        type (Union[Unset, str]):  Example: location_data.
        version (Union[Unset, str]):  Example: 0.1.
    """

    dollars_per_km2_day: Union[Unset, str] = UNSET
    dollars_per_selector_day: Union[Unset, str] = UNSET
    location_search_cost: Union[Unset, str] = UNSET
    num_days: Union[Unset, str] = UNSET
    num_km2: Union[Unset, str] = UNSET
    num_selectors: Union[Unset, str] = UNSET
    selector_search_cost: Union[Unset, str] = UNSET
    tier: Union[Unset, str] = UNSET
    total_search_cost: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dollars_per_km2_day = self.dollars_per_km2_day
        dollars_per_selector_day = self.dollars_per_selector_day
        location_search_cost = self.location_search_cost
        num_days = self.num_days
        num_km2 = self.num_km2
        num_selectors = self.num_selectors
        selector_search_cost = self.selector_search_cost
        tier = self.tier
        total_search_cost = self.total_search_cost
        type = self.type
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dollars_per_km2_day is not UNSET:
            field_dict["dollars_per_km2_day"] = dollars_per_km2_day
        if dollars_per_selector_day is not UNSET:
            field_dict["dollars_per_selector_day"] = dollars_per_selector_day
        if location_search_cost is not UNSET:
            field_dict["location_search_cost"] = location_search_cost
        if num_days is not UNSET:
            field_dict["num_days"] = num_days
        if num_km2 is not UNSET:
            field_dict["num_km2"] = num_km2
        if num_selectors is not UNSET:
            field_dict["num_selectors"] = num_selectors
        if selector_search_cost is not UNSET:
            field_dict["selector_search_cost"] = selector_search_cost
        if tier is not UNSET:
            field_dict["tier"] = tier
        if total_search_cost is not UNSET:
            field_dict["total_search_cost"] = total_search_cost
        if type is not UNSET:
            field_dict["type"] = type
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dollars_per_km2_day = d.pop("dollars_per_km2_day", UNSET)

        dollars_per_selector_day = d.pop("dollars_per_selector_day", UNSET)

        location_search_cost = d.pop("location_search_cost", UNSET)

        num_days = d.pop("num_days", UNSET)

        num_km2 = d.pop("num_km2", UNSET)

        num_selectors = d.pop("num_selectors", UNSET)

        selector_search_cost = d.pop("selector_search_cost", UNSET)

        tier = d.pop("tier", UNSET)

        total_search_cost = d.pop("total_search_cost", UNSET)

        type = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        query_bill_location_price = cls(
            dollars_per_km2_day=dollars_per_km2_day,
            dollars_per_selector_day=dollars_per_selector_day,
            location_search_cost=location_search_cost,
            num_days=num_days,
            num_km2=num_km2,
            num_selectors=num_selectors,
            selector_search_cost=selector_search_cost,
            tier=tier,
            total_search_cost=total_search_cost,
            type=type,
            version=version,
        )

        query_bill_location_price.additional_properties = d
        return query_bill_location_price

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
