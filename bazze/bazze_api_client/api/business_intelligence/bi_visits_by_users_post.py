import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.bi_visits_by_users_post_geohash_length import BIVisitsByUsersPostGeohashLength
from ...models.record import Record
from ...datatypes import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    json_body: List["Record"],
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    geohash_length: BIVisitsByUsersPostGeohashLength,
) -> Dict[str, Any]:
    url = "{}/bi/visits/users".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["wait"] = wait

    params["dryrun"] = dryrun

    params["limit"] = limit

    json_from_date = from_date.isoformat()

    params["from_date"] = json_from_date

    json_to_date = to_date.isoformat()

    params["to_date"] = json_to_date

    json_geohash_length = geohash_length.value

    params["geohash_length"] = json_geohash_length

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = []
    for componentsschemas_records_item_data in json_body:
        componentsschemas_records_item = componentsschemas_records_item_data.to_dict()

        json_json_body.append(componentsschemas_records_item)

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: List["Record"],
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    geohash_length: BIVisitsByUsersPostGeohashLength,
) -> Response[Any]:
    """Get user visit statistics by user id

     ## Description
    Get user visit statistics by specifying one or more advertising_ids in a JSON object. Number of
    advertising_ids is limited to 2000.

    NOTE: Due to performance limitations, this endpoint will return the statistics for the first 2000
    user ids that meet the
    filter criteria. Also, this endpoint can time out due to the long computation time. Please use
    asynchronous mode by setting
    `wait = false` and retrieve the results from the endpoint `/results`.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        geohash_length (BIVisitsByUsersPostGeohashLength):
        json_body (List['Record']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        wait=wait,
        dryrun=dryrun,
        limit=limit,
        from_date=from_date,
        to_date=to_date,
        geohash_length=geohash_length,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    json_body: List["Record"],
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    geohash_length: BIVisitsByUsersPostGeohashLength,
) -> Response[Any]:
    """Get user visit statistics by user id

     ## Description
    Get user visit statistics by specifying one or more advertising_ids in a JSON object. Number of
    advertising_ids is limited to 2000.

    NOTE: Due to performance limitations, this endpoint will return the statistics for the first 2000
    user ids that meet the
    filter criteria. Also, this endpoint can time out due to the long computation time. Please use
    asynchronous mode by setting
    `wait = false` and retrieve the results from the endpoint `/results`.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        geohash_length (BIVisitsByUsersPostGeohashLength):
        json_body (List['Record']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        wait=wait,
        dryrun=dryrun,
        limit=limit,
        from_date=from_date,
        to_date=to_date,
        geohash_length=geohash_length,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
