from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Selectors")


@attr.s(auto_attribs=True)
class Selectors:
    """
    Attributes:
        advertising_id (Union[Unset, List[str]]):
        bazze_gps_country (Union[Unset, List[str]]):
        country (Union[Unset, List[str]]):
        ip_address (Union[Unset, List[str]]):
        wifi_bssid (Union[Unset, List[str]]):
        wifi_ssid (Union[Unset, List[str]]):
    """

    advertising_id: Union[Unset, List[str]] = UNSET
    bazze_gps_country: Union[Unset, List[str]] = UNSET
    country: Union[Unset, List[str]] = UNSET
    ip_address: Union[Unset, List[str]] = UNSET
    wifi_bssid: Union[Unset, List[str]] = UNSET
    wifi_ssid: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        advertising_id: Union[Unset, List[str]] = UNSET
        if not isinstance(self.advertising_id, Unset):
            advertising_id = self.advertising_id

        bazze_gps_country: Union[Unset, List[str]] = UNSET
        if not isinstance(self.bazze_gps_country, Unset):
            bazze_gps_country = self.bazze_gps_country

        country: Union[Unset, List[str]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country

        ip_address: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ip_address, Unset):
            ip_address = self.ip_address

        wifi_bssid: Union[Unset, List[str]] = UNSET
        if not isinstance(self.wifi_bssid, Unset):
            wifi_bssid = self.wifi_bssid

        wifi_ssid: Union[Unset, List[str]] = UNSET
        if not isinstance(self.wifi_ssid, Unset):
            wifi_ssid = self.wifi_ssid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advertising_id is not UNSET:
            field_dict["advertising_id"] = advertising_id
        if bazze_gps_country is not UNSET:
            field_dict["bazze_gps_country"] = bazze_gps_country
        if country is not UNSET:
            field_dict["country"] = country
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if wifi_bssid is not UNSET:
            field_dict["wifi_bssid"] = wifi_bssid
        if wifi_ssid is not UNSET:
            field_dict["wifi_ssid"] = wifi_ssid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        advertising_id = cast(List[str], d.pop("advertising_id", UNSET))

        bazze_gps_country = cast(List[str], d.pop("bazze_gps_country", UNSET))

        country = cast(List[str], d.pop("country", UNSET))

        ip_address = cast(List[str], d.pop("ip_address", UNSET))

        wifi_bssid = cast(List[str], d.pop("wifi_bssid", UNSET))

        wifi_ssid = cast(List[str], d.pop("wifi_ssid", UNSET))

        selectors = cls(
            advertising_id=advertising_id,
            bazze_gps_country=bazze_gps_country,
            country=country,
            ip_address=ip_address,
            wifi_bssid=wifi_bssid,
            wifi_ssid=wifi_ssid,
        )

        selectors.additional_properties = d
        return selectors

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
