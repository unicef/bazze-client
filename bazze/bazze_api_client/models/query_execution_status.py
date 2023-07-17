import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..datatypes import UNSET, Unset

T = TypeVar("T", bound="QueryExecutionStatus")


@attr.s(auto_attribs=True)
class QueryExecutionStatus:
    """
    Attributes:
        completion_date_time (Union[Unset, datetime.datetime]):  Example: 2022-06-14T18:38:48.500000+02:00.
        message (Union[Unset, str]):  Example: Query failed due to a transient error. Please try again. Contact bazze if
            the error persists.
        state (Union[Unset, str]):  Example: FAILED.
        submission_date_time (Union[Unset, datetime.datetime]):  Example: 2022-06-14T18:38:54.954000+02:00.
    """

    completion_date_time: Union[Unset, datetime.datetime] = UNSET
    message: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    submission_date_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completion_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.completion_date_time, Unset):
            completion_date_time = self.completion_date_time.isoformat()

        message = self.message
        state = self.state
        submission_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.submission_date_time, Unset):
            submission_date_time = self.submission_date_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completion_date_time is not UNSET:
            field_dict["CompletionDateTime"] = completion_date_time
        if message is not UNSET:
            field_dict["Message"] = message
        if state is not UNSET:
            field_dict["State"] = state
        if submission_date_time is not UNSET:
            field_dict["SubmissionDateTime"] = submission_date_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _completion_date_time = d.pop("CompletionDateTime", UNSET)
        completion_date_time: Union[Unset, datetime.datetime]
        if isinstance(_completion_date_time, Unset):
            completion_date_time = UNSET
        else:
            completion_date_time = isoparse(_completion_date_time)

        message = d.pop("Message", UNSET)

        state = d.pop("State", UNSET)

        _submission_date_time = d.pop("SubmissionDateTime", UNSET)
        submission_date_time: Union[Unset, datetime.datetime]
        if isinstance(_submission_date_time, Unset):
            submission_date_time = UNSET
        else:
            submission_date_time = isoparse(_submission_date_time)

        query_execution_status = cls(
            completion_date_time=completion_date_time,
            message=message,
            state=state,
            submission_date_time=submission_date_time,
        )

        query_execution_status.additional_properties = d
        return query_execution_status

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
