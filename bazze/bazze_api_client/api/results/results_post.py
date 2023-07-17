from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.query_execution import QueryExecution
from ...models.results import Results
from ...datatypes import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: QueryExecution,
) -> Dict[str, Any]:
    url = "{}/results".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Results]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Results.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Results]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: QueryExecution,
) -> Response[Results]:
    """Get query results by QueryExecutionId

     ## Description
    Get query results by specifying the `QueryExecutionId``.

    ## Usage
    If the query is still running, you will get a response similar to:

    ```
    {
      \"QueryExecutionId\": \"54dc2e94-1104-4649-b9be-24dfda498186\",
      \"Status\": {
        \"State\": \"RUNNING\",
        \"SubmissionDateTime\": \"2020-08-27T19:31:59Z\"
      }
    }
    ```

    If the query has completed, the response will look like:

    ```
    {
      \"QueryExecutionId\": \"54dc2e94-1104-4649-b9be-24dfda498186\",
      \"csv\": \"https://bazze.link/82410f\",
      \"json\": \"https://bazze.link/f3162f\"
    }
    ```

    The short links can be shared and downloaded wherever the data is needed. For example, `wget
    https://bazze.link/82410f` would download the .csv file.

    Args:
        json_body (QueryExecution):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Results]
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


def sync(
    *,
    client: Client,
    json_body: QueryExecution,
) -> Optional[Results]:
    """Get query results by QueryExecutionId

     ## Description
    Get query results by specifying the `QueryExecutionId``.

    ## Usage
    If the query is still running, you will get a response similar to:

    ```
    {
      \"QueryExecutionId\": \"54dc2e94-1104-4649-b9be-24dfda498186\",
      \"Status\": {
        \"State\": \"RUNNING\",
        \"SubmissionDateTime\": \"2020-08-27T19:31:59Z\"
      }
    }
    ```

    If the query has completed, the response will look like:

    ```
    {
      \"QueryExecutionId\": \"54dc2e94-1104-4649-b9be-24dfda498186\",
      \"csv\": \"https://bazze.link/82410f\",
      \"json\": \"https://bazze.link/f3162f\"
    }
    ```

    The short links can be shared and downloaded wherever the data is needed. For example, `wget
    https://bazze.link/82410f` would download the .csv file.

    Args:
        json_body (QueryExecution):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Results]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: QueryExecution,
) -> Response[Results]:
    """Get query results by QueryExecutionId

     ## Description
    Get query results by specifying the `QueryExecutionId``.

    ## Usage
    If the query is still running, you will get a response similar to:

    ```
    {
      \"QueryExecutionId\": \"54dc2e94-1104-4649-b9be-24dfda498186\",
      \"Status\": {
        \"State\": \"RUNNING\",
        \"SubmissionDateTime\": \"2020-08-27T19:31:59Z\"
      }
    }
    ```

    If the query has completed, the response will look like:

    ```
    {
      \"QueryExecutionId\": \"54dc2e94-1104-4649-b9be-24dfda498186\",
      \"csv\": \"https://bazze.link/82410f\",
      \"json\": \"https://bazze.link/f3162f\"
    }
    ```

    The short links can be shared and downloaded wherever the data is needed. For example, `wget
    https://bazze.link/82410f` would download the .csv file.

    Args:
        json_body (QueryExecution):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Results]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: QueryExecution,
) -> Optional[Results]:
    """Get query results by QueryExecutionId

     ## Description
    Get query results by specifying the `QueryExecutionId``.

    ## Usage
    If the query is still running, you will get a response similar to:

    ```
    {
      \"QueryExecutionId\": \"54dc2e94-1104-4649-b9be-24dfda498186\",
      \"Status\": {
        \"State\": \"RUNNING\",
        \"SubmissionDateTime\": \"2020-08-27T19:31:59Z\"
      }
    }
    ```

    If the query has completed, the response will look like:

    ```
    {
      \"QueryExecutionId\": \"54dc2e94-1104-4649-b9be-24dfda498186\",
      \"csv\": \"https://bazze.link/82410f\",
      \"json\": \"https://bazze.link/f3162f\"
    }
    ```

    The short links can be shared and downloaded wherever the data is needed. For example, `wget
    https://bazze.link/82410f` would download the .csv file.

    Args:
        json_body (QueryExecution):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Results]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
