from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Subscribe")


@attr.s(auto_attribs=True)
class Subscribe:
    """
    Attributes:
        callback_url (str):  Example: https://o86biqzuuk.execute-api.us-west-2.amazonaws.com/api.
    """

    callback_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        callback_url = self.callback_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "callbackUrl": callback_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        callback_url = d.pop("callbackUrl")

        subscribe = cls(
            callback_url=callback_url,
        )

        subscribe.additional_properties = d
        return subscribe

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
