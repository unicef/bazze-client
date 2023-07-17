from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.subscribe import Subscribe
from ...datatypes import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Subscribe,
) -> Dict[str, Any]:
    url = "{}/unsubscribe".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
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
    json_body: Subscribe,
) -> Response[Any]:
    """Unsubscribe from a webhook

     ### Unsubscribing from an https url

    This endpoint allows you to unsubscribe from a previously confirmed https endpoint. Note that if you
    try to unsubscribe from a url that has NOT been confirmed you will get an error message. If you need
    to re-send the SubscriptionConfirmation just submit the `callbackUrl` again to the /subscribe
    endpoint.

    To disable a webhook subscription:

    - Submit a POST request to /v1/unsubscribe with the `callbackUrl` as the only key in the body.
    - If it is successful, you receive a 200 response code.

    Args:
        json_body (Subscribe):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Subscribe,
) -> Response[Any]:
    """Unsubscribe from a webhook

     ### Unsubscribing from an https url

    This endpoint allows you to unsubscribe from a previously confirmed https endpoint. Note that if you
    try to unsubscribe from a url that has NOT been confirmed you will get an error message. If you need
    to re-send the SubscriptionConfirmation just submit the `callbackUrl` again to the /subscribe
    endpoint.

    To disable a webhook subscription:

    - Submit a POST request to /v1/unsubscribe with the `callbackUrl` as the only key in the body.
    - If it is successful, you receive a 200 response code.

    Args:
        json_body (Subscribe):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
