import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.query_execution import QueryExecution
from ...models.results_scrolling_records import ResultsScrollingRecords
from ...datatypes import UNSET, Response



def _get_kwargs(
    *,
    client: Client,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    horizontal_accuracy: float,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    advertising_id: str,
    ip_address: str,
    wifi_ssid: str,
    wifi_bssid: str,
    country: str,
    bazze_gps_country: str,
) -> Dict[str, Any]:
    url = "{}/records".format(client.base_url)

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
    
    # optional parameters 
    
    if horizontal_accuracy != '':
        params["horizontal_accuracy"] = horizontal_accuracy

    if country != '':
        params["country"] = country
    
    if bazze_gps_country != '':
        params["bazze_gps_country"] = bazze_gps_country
    
    if advertising_id != '':
        params["advertising_id"] = advertising_id

    if ip_address != '':    
        params["ip_address"] = ip_address

    if wifi_ssid != '':
        params["wifi_ssid"] = wifi_ssid

    if wifi_bssid != '':
        params["wifi_bssid"] = wifi_bssid



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["QueryExecution", "ResultsScrollingRecords"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ResultsScrollingRecords.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = QueryExecution.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
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
    horizontal_accuracy: float,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    advertising_id: str,
    ip_address: str,
    wifi_ssid: str,
    wifi_bssid: str,
    country: str,
    bazze_gps_country: str,
) -> Response[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get records by selector

     ## Description
    Get records by searching one or more selectors. This is an AND type query, meaning that it will
    return
    a record only if it matches ALL of the criteria.

    **NOTE**: Each query return is limited to 20 million records. Records will be selected randomly from
    the dataset.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        horizontal_accuracy (float):  Example: 50.
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        advertising_id (str):
        ip_address (str):
        wifi_ssid (str):  Example: TP-LINK.
        wifi_bssid (str):
        country (str):  Example: RU.
        bazze_gps_country (str):  Example: RU.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['QueryExecution', 'ResultsScrollingRecords']]]
    """

    kwargs = _get_kwargs(
        client=client,
        wait=wait,
        dryrun=dryrun,
        limit=limit,
        horizontal_accuracy=horizontal_accuracy,
        from_date=from_date,
        to_date=to_date,
        advertising_id=advertising_id,
        ip_address=ip_address,
        wifi_ssid=wifi_ssid,
        wifi_bssid=wifi_bssid,
        country=country,
        bazze_gps_country=bazze_gps_country,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    horizontal_accuracy: float,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    advertising_id: str,
    ip_address: str,
    wifi_ssid: str,
    wifi_bssid: str,
    country: str,
    bazze_gps_country: str,
) -> Optional[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get records by selector

     ## Description
    Get records by searching one or more selectors. This is an AND type query, meaning that it will
    return
    a record only if it matches ALL of the criteria.

    **NOTE**: Each query return is limited to 20 million records. Records will be selected randomly from
    the dataset.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        horizontal_accuracy (float):  Example: 50.
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        advertising_id (str):
        ip_address (str):
        wifi_ssid (str):  Example: TP-LINK.
        wifi_bssid (str):
        country (str):  Example: RU.
        bazze_gps_country (str):  Example: RU.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['QueryExecution', 'ResultsScrollingRecords']]]
    """

    return sync_detailed(
        client=client,
        wait=wait,
        dryrun=dryrun,
        limit=limit,
        horizontal_accuracy=horizontal_accuracy,
        from_date=from_date,
        to_date=to_date,
        advertising_id=advertising_id,
        ip_address=ip_address,
        wifi_ssid=wifi_ssid,
        wifi_bssid=wifi_bssid,
        country=country,
        bazze_gps_country=bazze_gps_country,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    horizontal_accuracy: float,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    advertising_id: str,
    ip_address: str,
    wifi_ssid: str,
    wifi_bssid: str,
    country: str,
    bazze_gps_country: str,
) -> Response[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get records by selector

     ## Description
    Get records by searching one or more selectors. This is an AND type query, meaning that it will
    return
    a record only if it matches ALL of the criteria.

    **NOTE**: Each query return is limited to 20 million records. Records will be selected randomly from
    the dataset.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        horizontal_accuracy (float):  Example: 50.
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        advertising_id (str):
        ip_address (str):
        wifi_ssid (str):  Example: TP-LINK.
        wifi_bssid (str):
        country (str):  Example: RU.
        bazze_gps_country (str):  Example: RU.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['QueryExecution', 'ResultsScrollingRecords']]]
    """

    kwargs = _get_kwargs(
        client=client,
        wait=wait,
        dryrun=dryrun,
        limit=limit,
        horizontal_accuracy=horizontal_accuracy,
        from_date=from_date,
        to_date=to_date,
        advertising_id=advertising_id,
        ip_address=ip_address,
        wifi_ssid=wifi_ssid,
        wifi_bssid=wifi_bssid,
        country=country,
        bazze_gps_country=bazze_gps_country,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    horizontal_accuracy: float,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    advertising_id: str,
    ip_address: str,
    wifi_ssid: str,
    wifi_bssid: str,
    country: str,
    bazze_gps_country: str,
) -> Optional[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get records by selector

     ## Description
    Get records by searching one or more selectors. This is an AND type query, meaning that it will
    return
    a record only if it matches ALL of the criteria.

    **NOTE**: Each query return is limited to 20 million records. Records will be selected randomly from
    the dataset.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        horizontal_accuracy (float):  Example: 50.
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        advertising_id (str):
        ip_address (str):
        wifi_ssid (str):  Example: TP-LINK.
        wifi_bssid (str):
        country (str):  Example: RU.
        bazze_gps_country (str):  Example: RU.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['QueryExecution', 'ResultsScrollingRecords']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            wait=wait,
            dryrun=dryrun,
            limit=limit,
            horizontal_accuracy=horizontal_accuracy,
            from_date=from_date,
            to_date=to_date,
            advertising_id=advertising_id,
            ip_address=ip_address,
            wifi_ssid=wifi_ssid,
            wifi_bssid=wifi_bssid,
            country=country,
            bazze_gps_country=bazze_gps_country,
        )
    ).parsed

