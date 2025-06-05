from typing import Any

import requests
from fake_useragent import UserAgent
from requests.auth import HTTPBasicAuth

ua = UserAgent()


# fmt: off
def get_web_data(url: str, session=None, json=False, params=None, auth=None,
                 cookies=None, allow_redirects=False, stream=False,
                 iter_content=False, chunk_size=1024, return_response=False,
                 check_status=True, timeout=(10, 20)) -> Any:
# fmt: on
    response = None

    headers = {'User-Agent': ua.random, 'Connection': 'keep-alive'}

    if isinstance(auth, tuple) and len(auth) == 2:
        auth = HTTPBasicAuth(*auth)

    request_params = {
        'headers': headers,
        'params': params,
        'auth': auth,
        'cookies': cookies,
        'allow_redirects': allow_redirects,
        'stream': stream,
        'timeout': timeout,
    }

    try:
        if session:
            response = session.get(url, **request_params)
        else:
            response = requests.get(url, **request_params)

        if check_status:
            response.raise_for_status()

        if return_response:
            return response

        if json:
            return response.json()
        else:
            if stream:
                if iter_content:
                    return response.iter_content(chunk_size=chunk_size)
                else:
                    return response.content
            else:
                response.encoding = 'utf-8'
                return response.text

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP ошибка: {http_err} для URL: {url}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Ошибка соединения: {conn_err} для URL: {url}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Ошибка тайм-аута: {timeout_err} для URL: {url}')
    except requests.exceptions.RequestException as req_err:
        print(f'Ошибка запроса: {req_err} для URL: {url}')

    return response
