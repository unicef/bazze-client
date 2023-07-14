from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.results_scrolling_users_polygons_results_item_advertising_id_type import (
    ResultsScrollingUsersPolygonsResultsItemAdvertisingIdType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResultsScrollingUsersPolygonsResultsItem")


@attr.s(auto_attribs=True)
class ResultsScrollingUsersPolygonsResultsItem:
    """
    Attributes:
        advertising_id (Union[Unset, str]):  Example: 24EA7CE0-D052-4A64-B708-46D424F19931.
        advertising_id_type (Union[Unset, ResultsScrollingUsersPolygonsResultsItemAdvertisingIdType]): User identifier
            type for a mobile user. Example: idfa.
        features (Union[Unset, str]): The specific polygons that the user shows up in. Example: [feature_0, feature_1].
        num_features (Union[Unset, str]): Number of polygons that the user shows up in. Example: 2.
    """

    advertising_id: Union[Unset, str] = UNSET
    advertising_id_type: Union[Unset, ResultsScrollingUsersPolygonsResultsItemAdvertisingIdType] = UNSET
    features: Union[Unset, str] = UNSET
    num_features: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        advertising_id = self.advertising_id
        advertising_id_type: Union[Unset, str] = UNSET
        if not isinstance(self.advertising_id_type, Unset):
            advertising_id_type = self.advertising_id_type.value

        features = self.features
        num_features = self.num_features

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advertising_id is not UNSET:
            field_dict["advertising_id"] = advertising_id
        if advertising_id_type is not UNSET:
            field_dict["advertising_id_type"] = advertising_id_type
        if features is not UNSET:
            field_dict["features"] = features
        if num_features is not UNSET:
            field_dict["num_features"] = num_features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        advertising_id = d.pop("advertising_id", UNSET)

        _advertising_id_type = d.pop("advertising_id_type", UNSET)
        advertising_id_type: Union[Unset, ResultsScrollingUsersPolygonsResultsItemAdvertisingIdType]
        if isinstance(_advertising_id_type, Unset):
            advertising_id_type = UNSET
        else:
            advertising_id_type = ResultsScrollingUsersPolygonsResultsItemAdvertisingIdType(_advertising_id_type)

        features = d.pop("features", UNSET)

        num_features = d.pop("num_features", UNSET)

        results_scrolling_users_polygons_results_item = cls(
            advertising_id=advertising_id,
            advertising_id_type=advertising_id_type,
            features=features,
            num_features=num_features,
        )

        results_scrolling_users_polygons_results_item.additional_properties = d
        return results_scrolling_users_polygons_results_item

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
