import asyncio
import csv
import os

from aiohttp_library.useful_functions import (
    get_last_category_number,
    get_last_page_number,
    get_products_data_from_one_page,
)


async def main():
    last_category_number = await get_last_category_number()
    last_page_number = await get_last_page_number()

    urls = [
        f'https://parsinger.ru/html/index{category_num}_page_{page_num}.html'
        for category_num in range(1, last_category_number + 1)
        for page_num in range(1, last_page_number + 1)
    ]

    tasks = [get_products_data_from_one_page(url) for url in urls]
    all_data = await asyncio.gather(*tasks)
    all_data = [data for lst in all_data for data in lst]

    os.makedirs('csvs', exist_ok=True)

    with open(
        'csvs/all_categories_pages_data.csv',
        'a',
        encoding='utf-8-sig',
        newline='',
    ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(all_data)


if __name__ == '__main__':
    asyncio.run(main())
