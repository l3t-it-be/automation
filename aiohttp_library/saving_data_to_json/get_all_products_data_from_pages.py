import asyncio
import json
import os

from aiohttp_library.useful_functions import (
    get_last_category_number,
    get_last_page_number,
    get_response_data,
)


async def main():
    last_category_number = await get_last_category_number()
    last_page_number = await get_last_page_number()

    tasks = [
        get_products_data_from_one_page(category_num, page_num)
        for category_num in range(1, last_category_number + 1)
        for page_num in range(1, last_page_number + 1)
    ]
    all_data = await asyncio.gather(*tasks)
    all_data = [data for lst in all_data for data in lst]

    os.makedirs('jsons', exist_ok=True)

    with open(
        'jsons/products_pages_data.json', 'w', encoding='utf-8'
    ) as json_file:
        json.dump(all_data, json_file, indent=4, ensure_ascii=False)


async def get_products_data_from_one_page(category_num, page_num):
    url = f'https://parsinger.ru/html/index{category_num}_page_{page_num}.html'

    page_data = await get_response_data(url)
    if page_data:
        names = [name.text.strip() for name in page_data.select('.name_item')]
        description_names = [
            [li.text.split(':')[0].strip() for li in description.select('li')]
            for description in page_data.select('.description')
        ]
        descriptions_values = [
            [li.text.split(':')[1].strip() for li in description.select('li')]
            for description in page_data.select('.description')
        ]
        prices = [price.text.strip() for price in page_data.select('.price')]
        data = [
            {
                'Наименование': name,
                **{
                    desc_name: desc_value
                    for desc_name, desc_value in zip(desc_names, desc_values)
                },
                'Цена': price,
            }
            for name, desc_names, desc_values, price in zip(
                names, description_names, descriptions_values, prices
            )
        ]
        return data
    else:
        print(f'Page {url} is unavailable')
        return None


if __name__ == '__main__':
    asyncio.run(main())
