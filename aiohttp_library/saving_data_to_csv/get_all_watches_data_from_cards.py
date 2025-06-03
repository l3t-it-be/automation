import asyncio
import csv
import os

from aiohttp_library.useful_functions import (
    get_last_card_number,
    get_response_data,
)


async def main():
    os.makedirs('csvs', exist_ok=True)

    # fmt: off
    csv_headers = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип',
                   'Технология экрана', 'Материал корпуса', 'Материал браслета',
                   'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',
                   'Ссылка на карточку с товаром']
    # fmt: on

    with open(
        'csvs/watches_cards_data.csv',
        'w',
        encoding='utf-8-sig',
        newline='',
    ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(csv_headers)

    last_card_number = await get_last_card_number()
    tasks = [
        get_watch_data_from_card(card_number)
        for card_number in range(1, last_card_number + 1)
    ]
    all_data = await asyncio.gather(*tasks, return_exceptions=True)

    with open(
        'csvs/watches_cards_data.csv', 'a', encoding='utf-8-sig', newline=''
    ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(all_data)


async def get_watch_data_from_card(card_number):
    url = f'https://parsinger.ru/html/watch/1/1_{card_number}.html'

    page_data = await get_response_data(url)
    if page_data:
        title = page_data.select_one('#p_header').text.strip()
        article = page_data.select_one('.article').text.split()[1].strip()
        descriptions = [
            li.text.split(':')[1].strip()
            for li in page_data.select('#description li')
        ]
        in_stock = page_data.select_one('#in_stock').text.split(':')[1].strip()
        current_price = page_data.select_one('#price').text.strip()
        old_price = page_data.select_one('#old_price').text.strip()

        # fmt: off
        data = (title, article, *descriptions, in_stock,
                current_price, old_price, url)
        # fmt: on
        return data
    else:
        print(f'Page {url} is unavailable')
        return None


if __name__ == '__main__':
    asyncio.run(main())
