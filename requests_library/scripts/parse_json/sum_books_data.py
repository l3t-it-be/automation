from pprint import pprint

from requests_library.requests_setup import get_web_data

params = {'page': 1, 'per_page': 6}

html_data = get_web_data(
    'http://31.130.149.237/json_extraction/api/books', params=params, json=True
)
pprint(html_data)

result = []

for book in html_data['data']:
    sum_data = book['id'] + book['price'] + book['year']
    result.append(sum_data)

print(sum(result))
