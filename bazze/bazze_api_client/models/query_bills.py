from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..datatypes import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_bill_identity import QueryBillIdentity
    from ..models.query_bill_location import QueryBillLocation
    from ..models.query_bills_pagination import QueryBillsPagination


T = TypeVar("T", bound="QueryBills")


@attr.s(auto_attribs=True)
class QueryBills:
    """
    Attributes:
        pagination (Union[Unset, QueryBillsPagination]):
        queries (Union[Unset, List[Union['QueryBillIdentity', 'QueryBillLocation']]]):
    """

    pagination: Union[Unset, "QueryBillsPagination"] = UNSET
    queries: Union[Unset, List[Union["QueryBillIdentity", "QueryBillLocation"]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.query_bill_location import QueryBillLocation

        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        queries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.queries, Unset):
            queries = []
            for queries_item_data in self.queries:
                queries_item: Dict[str, Any]

                if isinstance(queries_item_data, QueryBillLocation):
                    queries_item = queries_item_data.to_dict()

                else:
                    queries_item = queries_item_data.to_dict()

                queries.append(queries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if queries is not UNSET:
            field_dict["queries"] = queries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_bill_identity import QueryBillIdentity
        from ..models.query_bill_location import QueryBillLocation
        from ..models.query_bills_pagination import QueryBillsPagination

        d = src_dict.copy()
        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, QueryBillsPagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = QueryBillsPagination.from_dict(_pagination)

        queries = []
        _queries = d.pop("queries", UNSET)
        for queries_item_data in _queries or []:

            def _parse_queries_item(data: object) -> Union["QueryBillIdentity", "QueryBillLocation"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    queries_item_type_0 = QueryBillLocation.from_dict(data)

                    return queries_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                queries_item_type_1 = QueryBillIdentity.from_dict(data)

                return queries_item_type_1

            queries_item = _parse_queries_item(queries_item_data)

            queries.append(queries_item)

        query_bills = cls(
            pagination=pagination,
            queries=queries,
        )

        query_bills.additional_properties = d
        return query_bills

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
