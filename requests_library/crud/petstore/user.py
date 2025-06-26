from pprint import pprint

import requests

from requests_library.crud.petstore.settings import base_url, headers

username = 'john_smith'
create_user_data = [
    {
        'id': 4,
        'username': username,
        'firstName': 'John',
        'lastName': 'Smith',
        'email': 'john-smith@gmail.com',
        'password': '1234QWERTY',
        'phone': 'Secret',
        'userStatus': 2,
    }
]


def create_user(post_headers, user_data):
    url = base_url + '/user/createWithList'
    response = requests.post(url, headers=post_headers, json=user_data)

    print('Status code:', response.status_code)
    print('Response body:', response.json())


def get_user(get_headers):
    url = base_url + f'/user/{username}'
    response = requests.get(url, headers=get_headers)

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(response.json())


print('Create new user:\n')
create_user(headers, create_user_data)
print('\n--------------------------------------------------------------')

print('Get user info:\n')
get_user(headers)
