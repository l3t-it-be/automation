import requests

from requests_library.requests_setup import get_web_data

base_url = 'https://httpbin.org/cookies'

with requests.Session() as session:
    response = get_web_data(base_url, session=session, json=True)
    print(response)

    params = {'freeform': '123'}
    url = base_url + '/set'
    response = get_web_data(
        url,
        allow_redirects=True,
        params=params,
        session=session,
        json=True,
    )
    print(response)

    response = get_web_data(base_url, session=session, json=True)
    print(response)
