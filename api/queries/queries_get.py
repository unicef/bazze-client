from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.query_executions import QueryExecutions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    pagination_token: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/queries".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[QueryExecutions]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueryExecutions.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[QueryExecutions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    pagination_token: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
) -> Response[QueryExecutions]:
    """Get query history by query status

     Get query history by specifying a query status.

    Args:
        pagination_token (Union[Unset, None, str]):
        pagesize (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryExecutions]
    """

    kwargs = _get_kwargs(
        client=client,
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
    pagination_token: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
) -> Optional[QueryExecutions]:
    """Get query history by query status

     Get query history by specifying a query status.

    Args:
        pagination_token (Union[Unset, None, str]):
        pagesize (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryExecutions]
    """

    return sync_detailed(
        client=client,
        pagination_token=pagination_token,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    pagination_token: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
) -> Response[QueryExecutions]:
    """Get query history by query status

     Get query history by specifying a query status.

    Args:
        pagination_token (Union[Unset, None, str]):
        pagesize (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryExecutions]
    """

    kwargs = _get_kwargs(
        client=client,
        pagination_token=pagination_token,
        pagesize=pagesize,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    pagination_token: Union[Unset, None, str] = UNSET,
    pagesize: Union[Unset, None, int] = UNSET,
) -> Optional[QueryExecutions]:
    """Get query history by query status

     Get query history by specifying a query status.

    Args:
        pagination_token (Union[Unset, None, str]):
        pagesize (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryExecutions]
    """

    return (
        await asyncio_detailed(
            client=client,
            pagination_token=pagination_token,
            pagesize=pagesize,
        )
    ).parsed
