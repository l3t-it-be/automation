import json

from bs4 import BeautifulSoup

from requests_library.requests_setup import get_web_data

html_data = get_web_data('https://parsinger.ru/table/6/index.html')
if html_data:
    html = BeautifulSoup(html_data, 'lxml')

    brands = [row.select('td')[0].text for row in html.select('tr')[1:]]
    release_years = [
        int(row.select('td')[1].text) for row in html.select('tr')[1:]
    ]
    engine_types = [row.select('td')[4].text for row in html.select('tr')[1:]]
    prices = [int(row.select('td')[-1].text) for row in html.select('tr')[1:]]

    cars = list(zip(brands, release_years, engine_types, prices))
    filtered_cars = []
    for car in cars:
        brand, release_year, engine_type, price = car
        if (
            price <= 4000000
            and release_year >= 2005
            and engine_type == 'Бензиновый'
        ):
            filtered_car = {
                'Марка Авто': brand,
                'Год выпуска': release_year,
                'Тип двигателя': engine_type,
                'Стоимость авто': price,
            }
            filtered_cars.append(filtered_car)

    sorted_cars = sorted(filtered_cars, key=lambda x: x['Стоимость авто'])
    result = json.dumps(sorted_cars, indent=4, ensure_ascii=False)
    print(result)
else:
    print('The page is unavailable')
