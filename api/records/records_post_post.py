import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.query_execution import QueryExecution
from ...models.results_scrolling_records import ResultsScrollingRecords
from ...models.selectors import Selectors
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Selectors,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    horizontal_accuracy: float,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
) -> Dict[str, Any]:
    url = "{}/records/multiple".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["wait"] = wait

    params["dryrun"] = dryrun

    params["limit"] = limit

    params["horizontal_accuracy"] = horizontal_accuracy

    json_from_date = from_date.isoformat()

    params["from_date"] = json_from_date

    json_to_date = to_date.isoformat()

    params["to_date"] = json_to_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: Selectors,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    horizontal_accuracy: float,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
) -> Response[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get records by multiple selectors

     ## Description
    Get records by searching numerous selector values and using a JSON object. It will return records
    that have matching values for each specified selector, similar to an IN...AND query.

    **NOTE**: Each query return is limited to 20 million records. Records will be selected randomly from
    the dataset. The JSON body cannot exceed 10 MB, AWS's API Gateway payload limit, which is roughly
    equivalent to 3500 advertising IDs OR 6500 IP addresses.CIDR search is not supported in this
    endpoint.
    Please use our /records GET endpoint for CIDR.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        horizontal_accuracy (float):  Example: 50.
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        json_body (Selectors):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['QueryExecution', 'ResultsScrollingRecords']]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        wait=wait,
        dryrun=dryrun,
        limit=limit,
        horizontal_accuracy=horizontal_accuracy,
        from_date=from_date,
        to_date=to_date,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: Selectors,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    horizontal_accuracy: float,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
) -> Optional[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get records by multiple selectors

     ## Description
    Get records by searching numerous selector values and using a JSON object. It will return records
    that have matching values for each specified selector, similar to an IN...AND query.

    **NOTE**: Each query return is limited to 20 million records. Records will be selected randomly from
    the dataset. The JSON body cannot exceed 10 MB, AWS's API Gateway payload limit, which is roughly
    equivalent to 3500 advertising IDs OR 6500 IP addresses.CIDR search is not supported in this
    endpoint.
    Please use our /records GET endpoint for CIDR.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        horizontal_accuracy (float):  Example: 50.
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        json_body (Selectors):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['QueryExecution', 'ResultsScrollingRecords']]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        wait=wait,
        dryrun=dryrun,
        limit=limit,
        horizontal_accuracy=horizontal_accuracy,
        from_date=from_date,
        to_date=to_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Selectors,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    horizontal_accuracy: float,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
) -> Response[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get records by multiple selectors

     ## Description
    Get records by searching numerous selector values and using a JSON object. It will return records
    that have matching values for each specified selector, similar to an IN...AND query.

    **NOTE**: Each query return is limited to 20 million records. Records will be selected randomly from
    the dataset. The JSON body cannot exceed 10 MB, AWS's API Gateway payload limit, which is roughly
    equivalent to 3500 advertising IDs OR 6500 IP addresses.CIDR search is not supported in this
    endpoint.
    Please use our /records GET endpoint for CIDR.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        horizontal_accuracy (float):  Example: 50.
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        json_body (Selectors):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['QueryExecution', 'ResultsScrollingRecords']]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        wait=wait,
        dryrun=dryrun,
        limit=limit,
        horizontal_accuracy=horizontal_accuracy,
        from_date=from_date,
        to_date=to_date,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: Selectors,
    wait: bool = False,
    dryrun: bool = False,
    limit: str,
    horizontal_accuracy: float,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
) -> Optional[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get records by multiple selectors

     ## Description
    Get records by searching numerous selector values and using a JSON object. It will return records
    that have matching values for each specified selector, similar to an IN...AND query.

    **NOTE**: Each query return is limited to 20 million records. Records will be selected randomly from
    the dataset. The JSON body cannot exceed 10 MB, AWS's API Gateway payload limit, which is roughly
    equivalent to 3500 advertising IDs OR 6500 IP addresses.CIDR search is not supported in this
    endpoint.
    Please use our /records GET endpoint for CIDR.

    Args:
        wait (bool):
        dryrun (bool):
        limit (str):  Example: 10.
        horizontal_accuracy (float):  Example: 50.
        from_date (datetime.datetime):  Example: 2021-06-01.
        to_date (datetime.datetime):  Example: 2021-06-05.
        json_body (Selectors):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['QueryExecution', 'ResultsScrollingRecords']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            wait=wait,
            dryrun=dryrun,
            limit=limit,
            horizontal_accuracy=horizontal_accuracy,
            from_date=from_date,
            to_date=to_date,
        )
    ).parsed
