import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.query_bills import QueryBills
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    date: datetime.date,
    pagination_token: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/billing".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_date = date.isoformat()
    params["date"] = json_date

    params["pagination_token"] = pagination_token

    params["pagesize"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[QueryBills]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueryBills.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[QueryBills]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    date: datetime.date,
    pagination_token: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
) -> Response[QueryBills]:
    """Get query history and billing details by date

     Get query history and billing details by specifying a date.

    Args:
        date (datetime.date):  Example: 2021-06-05.
        pagination_token (Union[Unset, None, str]):
        pagesize (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryBills]
    """

    kwargs = _get_kwargs(
        client=client,
        date=date,
        pagination_token=pagination_token,
        pagesize=pagesize,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    date: datetime.date,
    pagination_token: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
) -> Optional[QueryBills]:
    """Get query history and billing details by date

     Get query history and billing details by specifying a date.

    Args:
        date (datetime.date):  Example: 2021-06-05.
        pagination_token (Union[Unset, None, str]):
        pagesize (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryBills]
    """

    return sync_detailed(
        client=client,
        date=date,
        pagination_token=pagination_token,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    date: datetime.date,
    pagination_token: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
) -> Response[QueryBills]:
    """Get query history and billing details by date

     Get query history and billing details by specifying a date.

    Args:
        date (datetime.date):  Example: 2021-06-05.
        pagination_token (Union[Unset, None, str]):
        pagesize (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryBills]
    """

    kwargs = _get_kwargs(
        client=client,
        date=date,
        pagination_token=pagination_token,
        pagesize=pagesize,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    date: datetime.date,
    pagination_token: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
) -> Optional[QueryBills]:
    """Get query history and billing details by date

     Get query history and billing details by specifying a date.

    Args:
        date (datetime.date):  Example: 2021-06-05.
        pagination_token (Union[Unset, None, str]):
        pagesize (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryBills]
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            pagination_token=pagination_token,
            pagesize=pagesize,
        )
    ).parsed
