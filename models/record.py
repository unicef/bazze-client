import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.record_advertising_id_type import RecordAdvertisingIdType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@attr.s(auto_attribs=True)
class Record:
    """
    Attributes:
        advertising_id (Union[Unset, str]): User identifier for a mobile user. Example:
            496DC9DB-0E91-4C7B-9A40-9A454E759D76.
        advertising_id_type (Union[Unset, RecordAdvertisingIdType]): User identifier type for a mobile user. Example:
            idfa.
        altitude (Union[Unset, float]): Altitude of device in meters. Example: 36.199997.
        bazze_device_id (Union[Unset, str]): Hash of the user identifier of the record. Example:
            d72e6216b548ba30cf6987f25efce702c633344eb5722b539b4958f341bfe137.
        bazze_event_id (Union[Unset, str]): Hash of the full data record. Example:
            b93dbd393ae6859c7e5d3eaac6577d5bb18d8d770572671ac0f23e8dd68ed4a1.
        bazze_geohash (Union[Unset, str]): Geohash approximation of the data record location, at a 1km precision.
            Example: 69y7nvu9.
        bazze_mgrs (Union[Unset, str]): MGRS approximation of the record location, at a 1km precision. Example:
            21HUB7070.
        country (Union[Unset, str]):  Example: RU.
        horizontal_accuracy (Union[Unset, float]): Horizonal accuracy of the record location in meters. Example: 23.0.
        iot_signals (Union[Unset, str]): Only available for some data sources. Normally this field reflects an
            identifier for a bluetooth capable device.
        ip_address (Union[Unset, str]):  Example: 187.198.34.168.
        latitude (Union[Unset, float]):  Example: 25.54216121.
        longitude (Union[Unset, float]):  Example: -103.36121293.
        publisher_id (Union[Unset, str]): Publisher id of the mobile application. Example: 5e4bb75870a7d50001cd2368.
        timestamp (Union[Unset, datetime.datetime]): Event timestamp in ISO format. Example: 2019-07-27T19:31:59Z.
        user_agent (Union[Unset, str]): The browser user agent. Typical browsers include Chrome, Internet Explorer,
            Safari, Firefox. Example: Mozilla/5.0 (Linux; Android 9; G8341 Build/47.2.A.11.228; wv) AppleWebKit/537.36
            (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36.
        wifi_bssid (Union[Unset, str]):  Example: 50:4e:dc:41:18:a8.
        wifi_ssid (Union[Unset, str]):  Example: Tenda_4BADC0.
    """

    advertising_id: Union[Unset, str] = UNSET
    advertising_id_type: Union[Unset, RecordAdvertisingIdType] = UNSET
    altitude: Union[Unset, float] = UNSET
    bazze_device_id: Union[Unset, str] = UNSET
    bazze_event_id: Union[Unset, str] = UNSET
    bazze_geohash: Union[Unset, str] = UNSET
    bazze_mgrs: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    horizontal_accuracy: Union[Unset, float] = UNSET
    iot_signals: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    publisher_id: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    user_agent: Union[Unset, str] = UNSET
    wifi_bssid: Union[Unset, str] = UNSET
    wifi_ssid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        advertising_id = self.advertising_id
        advertising_id_type: Union[Unset, str] = UNSET
        if not isinstance(self.advertising_id_type, Unset):
            advertising_id_type = self.advertising_id_type.value

        altitude = self.altitude
        bazze_device_id = self.bazze_device_id
        bazze_event_id = self.bazze_event_id
        bazze_geohash = self.bazze_geohash
        bazze_mgrs = self.bazze_mgrs
        country = self.country
        horizontal_accuracy = self.horizontal_accuracy
        iot_signals = self.iot_signals
        ip_address = self.ip_address
        latitude = self.latitude
        longitude = self.longitude
        publisher_id = self.publisher_id
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        user_agent = self.user_agent
        wifi_bssid = self.wifi_bssid
        wifi_ssid = self.wifi_ssid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advertising_id is not UNSET:
            field_dict["advertising_id"] = advertising_id
        if advertising_id_type is not UNSET:
            field_dict["advertising_id_type"] = advertising_id_type
        if altitude is not UNSET:
            field_dict["altitude"] = altitude
        if bazze_device_id is not UNSET:
            field_dict["bazze_device_id"] = bazze_device_id
        if bazze_event_id is not UNSET:
            field_dict["bazze_event_id"] = bazze_event_id
        if bazze_geohash is not UNSET:
            field_dict["bazze_geohash"] = bazze_geohash
        if bazze_mgrs is not UNSET:
            field_dict["bazze_mgrs"] = bazze_mgrs
        if country is not UNSET:
            field_dict["country"] = country
        if horizontal_accuracy is not UNSET:
            field_dict["horizontal_accuracy"] = horizontal_accuracy
        if iot_signals is not UNSET:
            field_dict["iot_signals"] = iot_signals
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if publisher_id is not UNSET:
            field_dict["publisher_id"] = publisher_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if wifi_bssid is not UNSET:
            field_dict["wifi_bssid"] = wifi_bssid
        if wifi_ssid is not UNSET:
            field_dict["wifi_ssid"] = wifi_ssid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        advertising_id = d.pop("advertising_id", UNSET)

        _advertising_id_type = d.pop("advertising_id_type", UNSET)
        advertising_id_type: Union[Unset, RecordAdvertisingIdType]
        if isinstance(_advertising_id_type, Unset):
            advertising_id_type = UNSET
        else:
            advertising_id_type = RecordAdvertisingIdType(_advertising_id_type)

        altitude = d.pop("altitude", UNSET)

        bazze_device_id = d.pop("bazze_device_id", UNSET)

        bazze_event_id = d.pop("bazze_event_id", UNSET)

        bazze_geohash = d.pop("bazze_geohash", UNSET)

        bazze_mgrs = d.pop("bazze_mgrs", UNSET)

        country = d.pop("country", UNSET)

        horizontal_accuracy = d.pop("horizontal_accuracy", UNSET)

        iot_signals = d.pop("iot_signals", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        publisher_id = d.pop("publisher_id", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        user_agent = d.pop("user_agent", UNSET)

        wifi_bssid = d.pop("wifi_bssid", UNSET)

        wifi_ssid = d.pop("wifi_ssid", UNSET)

        record = cls(
            advertising_id=advertising_id,
            advertising_id_type=advertising_id_type,
            altitude=altitude,
            bazze_device_id=bazze_device_id,
            bazze_event_id=bazze_event_id,
            bazze_geohash=bazze_geohash,
            bazze_mgrs=bazze_mgrs,
            country=country,
            horizontal_accuracy=horizontal_accuracy,
            iot_signals=iot_signals,
            ip_address=ip_address,
            latitude=latitude,
            longitude=longitude,
            publisher_id=publisher_id,
            timestamp=timestamp,
            user_agent=user_agent,
            wifi_bssid=wifi_bssid,
            wifi_ssid=wifi_ssid,
        )

        record.additional_properties = d
        return record

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
