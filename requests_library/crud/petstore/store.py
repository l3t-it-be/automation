from pprint import pprint

import requests

from requests_library.crud.petstore.settings import base_url, headers


def get_store_inventory(get_headers):
    url = base_url + '/store/inventory'

    response = requests.get(url, headers=get_headers)
    available = response.json()['available']

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(response.json())
    print('Available:', available)


get_store_inventory(headers)
