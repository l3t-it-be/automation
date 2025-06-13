import json

import requests

token = '****************************'
chat_id = 7283010367

base_url = 'https://hh.ru/search/vacancy'
params = {
    'text': '',
    'excluded_text': '',
    'professional_role': '124',
    'area': ['48', '40', '113', '5', '16', '1001', '97', '28', '9'],
    'salary': '',
    'currency_code': 'RUR',
    'experience': 'doesNotMatter',
    'work_format': 'REMOTE',
    'order_by': 'relevance',
    'search_period': '3',
    'items_on_page': '20',
    'L_save_area': 'true',
    'hhtmFrom': 'vacancy_search_filter',
}


url = requests.Request('GET', base_url, params=params).prepare().url


headers = {'Content-Type': 'application/json'}
data = {'chat_id': chat_id, 'text': url}

requests.post(
    f'https://api.telegram.org/bot{token}/sendMessage',
    headers=headers,
    data=json.dumps(data),
)
