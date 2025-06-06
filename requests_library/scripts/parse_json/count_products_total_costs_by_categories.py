from requests_library.requests_setup import get_web_data

count = {}

json = get_web_data(
    'https://parsinger.ru/downloads/get_json/res.json', json=True
)
if json:
    for item in json:
        if item['categories'] in count:
            count[item['categories']] += int(item['count']) * int(
                item['price'].split()[0].strip()
            )
        else:
            count[item['categories']] = int(item['count']) * int(
                item['price'].split()[0].strip()
            )

    print(count)
else:
    print('The data is unavailable')
