import requests

base_url = 'https://jsonplaceholder.typicode.com'


def get_all_posts():
    response = requests.get(f'{base_url}/posts')

    print('Status code:', response.status_code)
    for post_num, post in enumerate(response.json(), start=1):
        print(f'{post_num}. {post['title']}')


def get_one_post(post_id):
    response = requests.get(f'{base_url}/posts/{post_id}')

    print('Status code:', response.status_code)
    print('Response body:', response.json())


def create_new_post(post_headers, data):
    response = requests.post(
        f'{base_url}/posts', headers=post_headers, json=data
    )

    print('Status code:', response.status_code)
    print('Response body:', response.json())


def update_post(post_id, put_headers, data):
    response = requests.put(
        f'{base_url}/posts/{post_id}', headers=put_headers, json=data
    )

    print('Status code:', response.status_code)
    print('Response body:', response.json())


def partially_update_post(post_id, patch_headers, data):
    response = requests.patch(
        f'{base_url}/posts/{post_id}', headers=patch_headers, json=data
    )

    print('Status code:', response.status_code)
    print('Response body:', response.json())


def delete_post(post_id):
    response = requests.delete(f'{base_url}/posts/{post_id}')
    print('Status code:', response.status_code)


headers = {'Content-Type': 'application/json; charset=UTF-8'}
create_data = {'title': 'foo', 'body': 'bar', 'userId': 1}
update_data = {'id': 42, 'title': 'foo', 'userId': 1}

get_all_posts()
print('\n--------------------------------------------------------------\n')
get_one_post(42)
print('\n--------------------------------------------------------------\n')
create_new_post(headers, create_data)
print('\n--------------------------------------------------------------\n')
update_post(42, headers, update_data)
print('\n--------------------------------------------------------------\n')
partially_update_post(42, headers, update_data)
print('\n--------------------------------------------------------------\n')
delete_post(42)
