from requests_library.requests_setup import get_web_data

data = {}

json = get_web_data('https://parsinger.ru/4.6/1/res.json', json=True)
if json:
    for item in json:
        if item['categories'] in data:
            data[item['categories']] += (
                int(item['article']) * item['description']['rating']
            )
        else:
            data[item['categories']] = (
                int(item['article']) * item['description']['rating']
            )

    print(data)
else:
    print('The data is unavailable')
