import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.query_execution import QueryExecution
from ...models.results_scrolling_records import ResultsScrollingRecords
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    from_date: datetime.date,
    to_date: datetime.date,
    phone_number: str,
    imei: str,
    imsi: str,
    cellid: str,
) -> Dict[str, Any]:
    url = "{}/cdr".format(client.base_url)

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

    params["phone_number"] = phone_number

    params["imei"] = imei

    params["imsi"] = imsi

    params["cellid"] = cellid

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
    from_date: datetime.date,
    to_date: datetime.date,
    phone_number: str,
    imei: str,
    imsi: str,
    cellid: str,
) -> Response[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get call data records (CDR) by phone number, IMEI, or IMSI.

     ## Description
    Get call data records (CDR) by phone number, IMEI, or IMSI.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        from_date (datetime.date):  Example: 2022-08-01.
        to_date (datetime.date):  Example: 2022-08-16.
        phone_number (str):
        imei (str):
        imsi (str):
        cellid (str):

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
        from_date=from_date,
        to_date=to_date,
        phone_number=phone_number,
        imei=imei,
        imsi=imsi,
        cellid=cellid,
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
    from_date: datetime.date,
    to_date: datetime.date,
    phone_number: str,
    imei: str,
    imsi: str,
    cellid: str,
) -> Optional[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get call data records (CDR) by phone number, IMEI, or IMSI.

     ## Description
    Get call data records (CDR) by phone number, IMEI, or IMSI.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        from_date (datetime.date):  Example: 2022-08-01.
        to_date (datetime.date):  Example: 2022-08-16.
        phone_number (str):
        imei (str):
        imsi (str):
        cellid (str):

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
        from_date=from_date,
        to_date=to_date,
        phone_number=phone_number,
        imei=imei,
        imsi=imsi,
        cellid=cellid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    from_date: datetime.date,
    to_date: datetime.date,
    phone_number: str,
    imei: str,
    imsi: str,
    cellid: str,
) -> Response[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get call data records (CDR) by phone number, IMEI, or IMSI.

     ## Description
    Get call data records (CDR) by phone number, IMEI, or IMSI.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        from_date (datetime.date):  Example: 2022-08-01.
        to_date (datetime.date):  Example: 2022-08-16.
        phone_number (str):
        imei (str):
        imsi (str):
        cellid (str):

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
        from_date=from_date,
        to_date=to_date,
        phone_number=phone_number,
        imei=imei,
        imsi=imsi,
        cellid=cellid,
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
    from_date: datetime.date,
    to_date: datetime.date,
    phone_number: str,
    imei: str,
    imsi: str,
    cellid: str,
) -> Optional[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get call data records (CDR) by phone number, IMEI, or IMSI.

     ## Description
    Get call data records (CDR) by phone number, IMEI, or IMSI.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        from_date (datetime.date):  Example: 2022-08-01.
        to_date (datetime.date):  Example: 2022-08-16.
        phone_number (str):
        imei (str):
        imsi (str):
        cellid (str):

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
            from_date=from_date,
            to_date=to_date,
            phone_number=phone_number,
            imei=imei,
            imsi=imsi,
            cellid=cellid,
        )
    ).parsed
