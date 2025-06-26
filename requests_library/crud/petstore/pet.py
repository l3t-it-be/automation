from pprint import pprint

import requests

from requests_library.crud.petstore.settings import base_url, headers

status_params = {
    'available': {'status': 'available'},
    'pending': {'status': 'pending'},
    'sold': {'status': 'sold'},
}

tisha_id = 42

create_pet_data = {
    'id': tisha_id,
    'category': {'id': 1, 'name': 'Cats'},
    'name': 'Tisha',
    'photoUrls': ['https://ibb.co/MyrZCGRb'],
    'tags': [{'id': 1, 'name': 'best_cat'}],
    'status': 'available',
}

tisha_photo = {
    'file': ('Tisha.jpg', open('files/images/Tischa.jpg', 'rb'), 'image/jpeg')
}


def get_pets_by_status(get_headers, status):
    url = base_url + '/pet/findByStatus'
    response = requests.get(url, headers=get_headers, params=status)

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(response.json())


def add_pet(post_headers, pet_data):
    url = base_url + '/pet'
    response = requests.post(url, headers=post_headers, json=pet_data)

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(response.json())


def upload_pet_img(pet_id, post_headers, files):
    url = base_url + f'/pet/{pet_id}/uploadImage'
    response = requests.post(url, headers=post_headers, files=files)

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(response.json())


def get_pet_by_id(pet_id, get_headers):
    url = base_url + f'/pet/{pet_id}'
    response = requests.get(url, headers=get_headers)

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(response.json())


print('Get available pets:\n')
get_pets_by_status(headers, status_params['available'])
print('\n--------------------------------------------------------------')

print('Get pending pets:\n')
get_pets_by_status(headers, status_params['pending'])
print('\n--------------------------------------------------------------')

print('Get sold pets:\n')
get_pets_by_status(headers, status_params['sold'])
print('\n--------------------------------------------------------------')

print('Create new pet Tisha:\n')
add_pet(headers, create_pet_data)
print('\n--------------------------------------------------------------')

print('Get Tisha\'s data:\n')
get_pet_by_id(tisha_id, headers)
print('\n--------------------------------------------------------------')

print('Upload Tisha\'s photo:\n')
upload_pet_img(tisha_id, headers, tisha_photo)
