from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.query_execution_scrolling import QueryExecutionScrolling
from ...datatypes import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: QueryExecutionScrolling,
) -> Dict[str, Any]:
    url = "{}/scrollResults".format(client.base_url)

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
    json_body: QueryExecutionScrolling,
) -> Response[Any]:
    """Get scrolling results by QueryExecutionId and NextToken

     Get scrolling results by `QueryExecutionId` and `NextToken`. This endpoint will return the query
    status if the query is still running or has failed.

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
      \"NextToken\": \"AUNcbIyhWBlqUOGqE3Y6NAEDhYSIK4ybNiKgmS30dWJlMzRFhO+ZL72BkWq+j16+nOhqeNkIFjGV8PVpL
    F72iZnpBUX2DFg/aA==\",
      \"QueryExecutionId\": \"54dc2e94-1104-4649-b9be-24dfda498186\",
      \"results\": [
        {
          \"advertising_id\": \"6D505F8D-D38D-40F5-8B81-CA29D15E02A4\",
          \"advertising_id_type\": \"idfa\",
          \"altitude\": \"249.20001\",
          \"bazze_device_id\": \"7336ea934441fdffe4123acf6dbd368fc4c67d2ce06644a97dc2d4a0fa07bdf8\",
          \"bazze_event_id\": \"c85e0aae825c068fdb087efe7e030ab4dc32e9636a47b9d458547da4a0848414\",
          \"bazze_geohash\": \"srxw99gx\",
          \"bazze_mgrs\": \"34TEN7099\",
          \"country\": \"RS\",
          \"horizontal_accuracy\": \"28.7\",
          \"iot_signals\": \"\",
          \"ip_address\": \"\",
          \"latitude\": \"43.341064\",
          \"longitude\": \"21.86794\",
          \"publisher_id\": \"151e0297a27d4140ad9c5d4e4bafd290\",
          \"timestamp\": \"2020-07-02 08:31:12.000\",
          \"user_agent\": \"Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Pro Build/PPR1.180610.011; wv)
    AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36\",
          \"wifi_bssid\": \"\",
          \"wifi_ssid\": \"<unknown ssid>\"
        }
      ]
    }
    ```

    This endpoint allows you to scroll 1000 records at a time. To scroll the data, you can poll this
    endpoint using the `NextToken` as the \"bookmark\" to pick up where you left off.

    Args:
        json_body (QueryExecutionScrolling):

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
    json_body: QueryExecutionScrolling,
) -> Response[Any]:
    """Get scrolling results by QueryExecutionId and NextToken

     Get scrolling results by `QueryExecutionId` and `NextToken`. This endpoint will return the query
    status if the query is still running or has failed.

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
      \"NextToken\": \"AUNcbIyhWBlqUOGqE3Y6NAEDhYSIK4ybNiKgmS30dWJlMzRFhO+ZL72BkWq+j16+nOhqeNkIFjGV8PVpL
    F72iZnpBUX2DFg/aA==\",
      \"QueryExecutionId\": \"54dc2e94-1104-4649-b9be-24dfda498186\",
      \"results\": [
        {
          \"advertising_id\": \"6D505F8D-D38D-40F5-8B81-CA29D15E02A4\",
          \"advertising_id_type\": \"idfa\",
          \"altitude\": \"249.20001\",
          \"bazze_device_id\": \"7336ea934441fdffe4123acf6dbd368fc4c67d2ce06644a97dc2d4a0fa07bdf8\",
          \"bazze_event_id\": \"c85e0aae825c068fdb087efe7e030ab4dc32e9636a47b9d458547da4a0848414\",
          \"bazze_geohash\": \"srxw99gx\",
          \"bazze_mgrs\": \"34TEN7099\",
          \"country\": \"RS\",
          \"horizontal_accuracy\": \"28.7\",
          \"iot_signals\": \"\",
          \"ip_address\": \"\",
          \"latitude\": \"43.341064\",
          \"longitude\": \"21.86794\",
          \"publisher_id\": \"151e0297a27d4140ad9c5d4e4bafd290\",
          \"timestamp\": \"2020-07-02 08:31:12.000\",
          \"user_agent\": \"Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Pro Build/PPR1.180610.011; wv)
    AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36\",
          \"wifi_bssid\": \"\",
          \"wifi_ssid\": \"<unknown ssid>\"
        }
      ]
    }
    ```

    This endpoint allows you to scroll 1000 records at a time. To scroll the data, you can poll this
    endpoint using the `NextToken` as the \"bookmark\" to pick up where you left off.

    Args:
        json_body (QueryExecutionScrolling):

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
