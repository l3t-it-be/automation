import asyncio
import csv
import os

from aiohttp_library.useful_functions import (
    get_last_page_number,
    get_products_data_from_one_page,
)


async def main():
    os.makedirs('csvs', exist_ok=True)

    # fmt: off
    csv_headers = ['Наименование', 'Бренд', 'Форм-фактор',
                   'Ёмкость', 'Объем буферной памяти','Цена']
    # fmt: on

    with open(
        'csvs/hdd_pages_data.csv', 'w', encoding='utf-8-sig', newline=''
    ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(csv_headers)

    last_page_number = await get_last_page_number()
    urls = [
        f'https://parsinger.ru/html/index4_page_{page_num}.html'
        for page_num in range(1, last_page_number + 1)
    ]

    tasks = [get_products_data_from_one_page(url) for url in urls]
    all_data = await asyncio.gather(*tasks, return_exceptions=True)
    all_data = [data for lst in all_data for data in lst]

    with open(
        'csvs/hdd_pages_data.csv',
        'a',
        encoding='utf-8-sig',
        newline='',
    ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(all_data)


if __name__ == '__main__':
    asyncio.run(main())
