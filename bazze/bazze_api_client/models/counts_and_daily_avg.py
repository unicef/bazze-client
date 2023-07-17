from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..datatypes import UNSET, Unset

T = TypeVar("T", bound="CountsAndDailyAvg")


@attr.s(auto_attribs=True)
class CountsAndDailyAvg:
    """
    Attributes:
        daily_avg_advertising_ids (Union[Unset, float]):  Example: 21.6288.
        daily_avg_ip_addresses (Union[Unset, float]):  Example: 24.1014.
        daily_avg_wifi_bssids (Union[Unset, float]):  Example: 2.6906.
        daily_avg_wifi_ssids (Union[Unset, float]):  Example: 2.275.
        total_records (Union[Unset, int]):  Example: 794357.
    """

    daily_avg_advertising_ids: Union[Unset, float] = UNSET
    daily_avg_ip_addresses: Union[Unset, float] = UNSET
    daily_avg_wifi_bssids: Union[Unset, float] = UNSET
    daily_avg_wifi_ssids: Union[Unset, float] = UNSET
    total_records: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        daily_avg_advertising_ids = self.daily_avg_advertising_ids
        daily_avg_ip_addresses = self.daily_avg_ip_addresses
        daily_avg_wifi_bssids = self.daily_avg_wifi_bssids
        daily_avg_wifi_ssids = self.daily_avg_wifi_ssids
        total_records = self.total_records

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily_avg_advertising_ids is not UNSET:
            field_dict["daily_avg_advertising_ids"] = daily_avg_advertising_ids
        if daily_avg_ip_addresses is not UNSET:
            field_dict["daily_avg_ip_addresses"] = daily_avg_ip_addresses
        if daily_avg_wifi_bssids is not UNSET:
            field_dict["daily_avg_wifi_bssids"] = daily_avg_wifi_bssids
        if daily_avg_wifi_ssids is not UNSET:
            field_dict["daily_avg_wifi_ssids"] = daily_avg_wifi_ssids
        if total_records is not UNSET:
            field_dict["total_records"] = total_records

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        daily_avg_advertising_ids = d.pop("daily_avg_advertising_ids", UNSET)

        daily_avg_ip_addresses = d.pop("daily_avg_ip_addresses", UNSET)

        daily_avg_wifi_bssids = d.pop("daily_avg_wifi_bssids", UNSET)

        daily_avg_wifi_ssids = d.pop("daily_avg_wifi_ssids", UNSET)

        total_records = d.pop("total_records", UNSET)

        counts_and_daily_avg = cls(
            daily_avg_advertising_ids=daily_avg_advertising_ids,
            daily_avg_ip_addresses=daily_avg_ip_addresses,
            daily_avg_wifi_bssids=daily_avg_wifi_bssids,
            daily_avg_wifi_ssids=daily_avg_wifi_ssids,
            total_records=total_records,
        )

        counts_and_daily_avg.additional_properties = d
        return counts_and_daily_avg

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
