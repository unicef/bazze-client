import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.counts_and_daily_avg import CountsAndDailyAvg
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    geohash: str,
) -> Dict[str, Any]:
    url = "{}/stats/counts_by_geohash".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_from_date = from_date.isoformat()

    params["from_date"] = json_from_date

    json_to_date = to_date.isoformat()

    params["to_date"] = json_to_date

    params["geohash"] = geohash

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, CountsAndDailyAvg]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CountsAndDailyAvg.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, CountsAndDailyAvg]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    geohash: str,
) -> Response[Union[Any, CountsAndDailyAvg]]:
    """Get statistics by date and geohash

    Args:
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        geohash (str):  Example: 9g8d8v.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CountsAndDailyAvg]]
    """

    kwargs = _get_kwargs(
        client=client,
        from_date=from_date,
        to_date=to_date,
        geohash=geohash,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    geohash: str,
) -> Optional[Union[Any, CountsAndDailyAvg]]:
    """Get statistics by date and geohash

    Args:
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        geohash (str):  Example: 9g8d8v.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CountsAndDailyAvg]]
    """

    return sync_detailed(
        client=client,
        from_date=from_date,
        to_date=to_date,
        geohash=geohash,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    geohash: str,
) -> Response[Union[Any, CountsAndDailyAvg]]:
    """Get statistics by date and geohash

    Args:
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        geohash (str):  Example: 9g8d8v.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CountsAndDailyAvg]]
    """

    kwargs = _get_kwargs(
        client=client,
        from_date=from_date,
        to_date=to_date,
        geohash=geohash,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    geohash: str,
) -> Optional[Union[Any, CountsAndDailyAvg]]:
    """Get statistics by date and geohash

    Args:
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        geohash (str):  Example: 9g8d8v.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CountsAndDailyAvg]]
    """

    return (
        await asyncio_detailed(
            client=client,
            from_date=from_date,
            to_date=to_date,
            geohash=geohash,
        )
    ).parsed
