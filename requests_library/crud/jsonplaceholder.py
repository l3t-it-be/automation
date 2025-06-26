from pprint import pprint

import requests

base_url = 'https://jsonplaceholder.typicode.com'
headers = {'Content-Type': 'application/json; charset=UTF-8'}

post_id = 42
create_data = {'userId': 1, 'title': 'foo', 'body': 'bar'}
update_data = {'userId': 1, 'id': post_id, 'title': 'foo'}


def get_all_posts():
    url = base_url + '/posts'
    response = requests.get(url)

    print('Status code:', response.status_code)
    for post_num, post in enumerate(response.json(), start=1):
        print(f'{post_num}. {post['title']}')


def get_one_post(post_id):
    url = base_url + f'/posts/{post_id}'
    response = requests.get(url)

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(response.json())


def create_new_post(post_headers, data):
    url = base_url + '/posts'
    response = requests.post(url, headers=post_headers, json=data)

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(response.json())


def update_post(post_id, put_headers, data):
    url = base_url + f'/posts/{post_id}'
    response = requests.put(url, headers=put_headers, json=data)

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(response.json())


def partially_update_post(post_id, patch_headers, data):
    url = base_url + f'/posts/{post_id}'
    response = requests.patch(url, headers=patch_headers, json=data)

    print('Status code:', response.status_code)
    print('Response body:')
    pprint(response.json())


def delete_post(post_id):
    url = base_url + f'/posts/{post_id}'
    response = requests.delete(url)

    print('Status code:', response.status_code)


print('Get all posts:\n')
get_all_posts()
print('\n--------------------------------------------------------------')

print('Get one post:\n')
get_one_post(post_id)
print('\n--------------------------------------------------------------')

print('Create new post:\n')
create_new_post(headers, create_data)
print('\n--------------------------------------------------------------')

print('Update post:\n')
update_post(post_id, headers, update_data)
print('\n--------------------------------------------------------------')

print('Partially update post:\n')
partially_update_post(post_id, headers, update_data)
print('\n--------------------------------------------------------------')

print('Delete post:\n')
delete_post(post_id)
