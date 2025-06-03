import asyncio
import json
import os

from aiohttp_library.useful_functions import (
    get_last_page_number,
    get_products_data_from_one_page,
)


async def main():
    # fmt: off
    hdd_keys = ['Наименование', 'Бренд', 'Форм-фактор',
                'Ёмкость', 'Объем буферной памяти', 'Цена']
    # fmt: on

    last_page_number = await get_last_page_number()

    urls = [
        f'https://parsinger.ru/html/index4_page_{page_num}.html'
        for page_num in range(1, last_page_number + 1)
    ]
    tasks = [get_products_data_from_one_page(url) for url in urls]

    all_data = await asyncio.gather(*tasks, return_exceptions=True)
    all_data = [data for lst in all_data for data in lst]
    result = [
        {key: value for key, value in zip(hdd_keys, data)} for data in all_data
    ]

    os.makedirs('jsons', exist_ok=True)

    with open('jsons/hdd_pages_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    asyncio.run(main())
