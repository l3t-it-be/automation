from requests_library.requests_setup import get_web_data

data = {}

json = get_web_data(
    'https://parsinger.ru/downloads/get_json/res.json', json=True
)
if json:
    for item in json:
        if item['categories'] in data:
            data[item['categories']] += int(item['count'])
        else:
            data[item['categories']] = int(item['count'])

    print(data)
else:
    print('The data is unavailable')
