import asyncio
import json
import os

from aiohttp_library.useful_functions import (
    get_products_categories_url_titles,
    get_last_card_number,
    get_product_data_from_card,
)


async def main():
    product_categories = await get_products_categories_url_titles()
    last_card_number = await get_last_card_number()

    tasks = [
        get_product_data_from_card(category, category_number, card_number)
        for category_number, category in enumerate(product_categories, 1)
        for card_number in range(1, last_card_number + 1)
    ]
    all_data = await asyncio.gather(*tasks)

    os.makedirs('jsons', exist_ok=True)

    with open(
        'jsons/products_cards_data.json', 'w', encoding='utf-8'
    ) as json_file:
        json.dump(all_data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    asyncio.run(main())
