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
    dryrun: bool = False,
    vendors: str,
    advertising_id: str,
    email: str,
    email_hash: str,
    phone_number: str,
    social_media: str,
    ip_address: str,
    full_name: str,
    domain: str,
    first_name: str,
    last_name: str,
    location: str,
) -> Dict[str, Any]:
    url = "{}/identity".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["dryrun"] = dryrun

    params["vendors"] = vendors

    params["advertising_id"] = advertising_id

    params["email"] = email

    params["email_hash"] = email_hash

    params["phone_number"] = phone_number

    params["social_media"] = social_media

    params["ip_address"] = ip_address

    params["full_name"] = full_name

    params["domain"] = domain

    params["first_name"] = first_name

    params["last_name"] = last_name

    params["location"] = location

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
    dryrun: bool = False,
    vendors: str,
    advertising_id: str,
    email: str,
    email_hash: str,
    phone_number: str,
    social_media: str,
    ip_address: str,
    full_name: str,
    domain: str,
    first_name: str,
    last_name: str,
    location: str,
) -> Response[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get identity data by selector

     ## Description
    Get identity data by searching one or more selectors.

    Args:
        dryrun (bool):
        vendors (str):
        advertising_id (str):
        email (str):
        email_hash (str):
        phone_number (str):
        social_media (str):
        ip_address (str):
        full_name (str):
        domain (str):
        first_name (str):
        last_name (str):
        location (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['QueryExecution', 'ResultsScrollingRecords']]]
    """

    kwargs = _get_kwargs(
        client=client,
        dryrun=dryrun,
        vendors=vendors,
        advertising_id=advertising_id,
        email=email,
        email_hash=email_hash,
        phone_number=phone_number,
        social_media=social_media,
        ip_address=ip_address,
        full_name=full_name,
        domain=domain,
        first_name=first_name,
        last_name=last_name,
        location=location,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    dryrun: bool = False,
    vendors: str,
    advertising_id: str,
    email: str,
    email_hash: str,
    phone_number: str,
    social_media: str,
    ip_address: str,
    full_name: str,
    domain: str,
    first_name: str,
    last_name: str,
    location: str,
) -> Optional[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get identity data by selector

     ## Description
    Get identity data by searching one or more selectors.

    Args:
        dryrun (bool):
        vendors (str):
        advertising_id (str):
        email (str):
        email_hash (str):
        phone_number (str):
        social_media (str):
        ip_address (str):
        full_name (str):
        domain (str):
        first_name (str):
        last_name (str):
        location (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['QueryExecution', 'ResultsScrollingRecords']]]
    """

    return sync_detailed(
        client=client,
        dryrun=dryrun,
        vendors=vendors,
        advertising_id=advertising_id,
        email=email,
        email_hash=email_hash,
        phone_number=phone_number,
        social_media=social_media,
        ip_address=ip_address,
        full_name=full_name,
        domain=domain,
        first_name=first_name,
        last_name=last_name,
        location=location,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    dryrun: bool = False,
    vendors: str,
    advertising_id: str,
    email: str,
    email_hash: str,
    phone_number: str,
    social_media: str,
    ip_address: str,
    full_name: str,
    domain: str,
    first_name: str,
    last_name: str,
    location: str,
) -> Response[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get identity data by selector

     ## Description
    Get identity data by searching one or more selectors.

    Args:
        dryrun (bool):
        vendors (str):
        advertising_id (str):
        email (str):
        email_hash (str):
        phone_number (str):
        social_media (str):
        ip_address (str):
        full_name (str):
        domain (str):
        first_name (str):
        last_name (str):
        location (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['QueryExecution', 'ResultsScrollingRecords']]]
    """

    kwargs = _get_kwargs(
        client=client,
        dryrun=dryrun,
        vendors=vendors,
        advertising_id=advertising_id,
        email=email,
        email_hash=email_hash,
        phone_number=phone_number,
        social_media=social_media,
        ip_address=ip_address,
        full_name=full_name,
        domain=domain,
        first_name=first_name,
        last_name=last_name,
        location=location,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    dryrun: bool = False,
    vendors: str,
    advertising_id: str,
    email: str,
    email_hash: str,
    phone_number: str,
    social_media: str,
    ip_address: str,
    full_name: str,
    domain: str,
    first_name: str,
    last_name: str,
    location: str,
) -> Optional[Union[Any, Union["QueryExecution", "ResultsScrollingRecords"]]]:
    """Get identity data by selector

     ## Description
    Get identity data by searching one or more selectors.

    Args:
        dryrun (bool):
        vendors (str):
        advertising_id (str):
        email (str):
        email_hash (str):
        phone_number (str):
        social_media (str):
        ip_address (str):
        full_name (str):
        domain (str):
        first_name (str):
        last_name (str):
        location (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['QueryExecution', 'ResultsScrollingRecords']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            dryrun=dryrun,
            vendors=vendors,
            advertising_id=advertising_id,
            email=email,
            email_hash=email_hash,
            phone_number=phone_number,
            social_media=social_media,
            ip_address=ip_address,
            full_name=full_name,
            domain=domain,
            first_name=first_name,
            last_name=last_name,
            location=location,
        )
    ).parsed
