import asyncio
import csv
import os

from aiohttp_library.useful_functions import (
    get_products_categories_url_titles,
    get_last_card_number,
    get_response_data,
)


async def main():
    os.makedirs('csvs', exist_ok=True)

    # fmt: off
    csv_headers = ['Наименование', 'Артикул', 'Бренд', 'Модель',
                   'Наличие', 'Цена', 'Старая цена', 'Ссылка']
    # fmt: on

    with open(
        'csvs/products_cards_basic_data.csv',
        'w',
        encoding='utf-8-sig',
        newline='',
    ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(csv_headers)

    products_categories = await get_products_categories_url_titles()
    last_card_number = await get_last_card_number()

    tasks = [
        get_product_basic_data_from_card(product, product_num, card_num)
        for product_num, product in enumerate(products_categories, 1)
        for card_num in range(1, last_card_number + 1)
    ]
    all_data = await asyncio.gather(*tasks, return_exceptions=True)

    with open(
        'csvs/products_cards_basic_data.csv',
        'a',
        encoding='utf-8-sig',
        newline='',
    ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(all_data)


async def get_product_basic_data_from_card(product, product_num, card_num):

    url = f'https://parsinger.ru/html/{product}/{product_num}/{product_num}_{card_num}.html'

    page_data = await get_response_data(url)
    if page_data:
        title = page_data.select_one('#p_header').text.strip()
        article = page_data.select_one('.article').text.split()[1].strip()
        brand = page_data.select_one('#brand').text.split()[1].strip()
        model = page_data.select_one('#model').text.split()[1].strip()
        in_stock = page_data.select_one('#in_stock').text.split(':')[1].strip()
        current_price = page_data.select_one('#price').text.strip()
        old_price = page_data.select_one('#old_price').text.strip()

        # fmt: off
        data = (title, article, brand, model, in_stock,
                current_price, old_price, url)
        # fmt: on
        return data
    else:
        print(f'Page {url} is unavailable')
        return None


if __name__ == '__main__':
    asyncio.run(main())
