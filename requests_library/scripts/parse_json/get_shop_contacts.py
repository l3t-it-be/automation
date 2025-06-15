from pprint import pprint

from requests_library.requests_setup import get_web_data

html_data = get_web_data(
    'http://31.130.149.237/json_extraction/contacts', json=True
)
pprint(html_data)

lng = html_data['stores'][1]['coordinates']['lng']
print(lng)
