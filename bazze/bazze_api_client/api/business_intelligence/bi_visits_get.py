import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.bi_visits_get_geohash_length import BIVisitsGetGeohashLength
from ...datatypes import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    geohash_length: BIVisitsGetGeohashLength,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    advertising_id: str,
    ip_address: str,
    wifi_ssid: str,
    wifi_bssid: str,
    country: str,
) -> Dict[str, Any]:
    url = "{}/bi/visits".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["wait"] = wait

    params["dryrun"] = dryrun

    params["limit"] = limit

    json_geohash_length = geohash_length.value

    params["geohash_length"] = json_geohash_length

    json_from_date = from_date.isoformat()

    params["from_date"] = json_from_date

    json_to_date = to_date.isoformat()

    params["to_date"] = json_to_date

    params["advertising_id"] = advertising_id

    params["ip_address"] = ip_address

    params["wifi_ssid"] = wifi_ssid

    params["wifi_bssid"] = wifi_bssid

    params["country"] = country

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    geohash_length: BIVisitsGetGeohashLength,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    advertising_id: str,
    ip_address: str,
    wifi_ssid: str,
    wifi_bssid: str,
    country: str,
) -> Response[Any]:
    """Get user visit statistics by selector

     ## Description
    Get user visit statistics by searching one or more selectors. This is an AND type query, meaning
    that it will return statistics only if the user matches ALL of the criteria.

    **NOTE**: Due to performance limitations, this endpoint will return the statistics for the first
    2000 user ids that
    meet the filter criteria. Also, this endpoint can time out due to the long computation time. Please
    use asynchronous
    mode by setting `wait = false` and retrieve the results from the endpoint `/results`.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        geohash_length (BIVisitsGetGeohashLength):
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        advertising_id (str):
        ip_address (str):
        wifi_ssid (str):  Example: TP-LINK.
        wifi_bssid (str):
        country (str):  Example: RU.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        wait=wait,
        dryrun=dryrun,
        limit=limit,
        geohash_length=geohash_length,
        from_date=from_date,
        to_date=to_date,
        advertising_id=advertising_id,
        ip_address=ip_address,
        wifi_ssid=wifi_ssid,
        wifi_bssid=wifi_bssid,
        country=country,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    geohash_length: BIVisitsGetGeohashLength,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    advertising_id: str,
    ip_address: str,
    wifi_ssid: str,
    wifi_bssid: str,
    country: str,
) -> Response[Any]:
    """Get user visit statistics by selector

     ## Description
    Get user visit statistics by searching one or more selectors. This is an AND type query, meaning
    that it will return statistics only if the user matches ALL of the criteria.

    **NOTE**: Due to performance limitations, this endpoint will return the statistics for the first
    2000 user ids that
    meet the filter criteria. Also, this endpoint can time out due to the long computation time. Please
    use asynchronous
    mode by setting `wait = false` and retrieve the results from the endpoint `/results`.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        geohash_length (BIVisitsGetGeohashLength):
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        advertising_id (str):
        ip_address (str):
        wifi_ssid (str):  Example: TP-LINK.
        wifi_bssid (str):
        country (str):  Example: RU.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        wait=wait,
        dryrun=dryrun,
        limit=limit,
        geohash_length=geohash_length,
        from_date=from_date,
        to_date=to_date,
        advertising_id=advertising_id,
        ip_address=ip_address,
        wifi_ssid=wifi_ssid,
        wifi_bssid=wifi_bssid,
        country=country,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
