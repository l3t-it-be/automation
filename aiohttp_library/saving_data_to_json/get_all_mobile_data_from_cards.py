import asyncio
import json
import os

from aiohttp_library.useful_functions import (
    get_last_card_number,
    get_product_data_from_card,
)


async def main():
    last_card_number = await get_last_card_number()

    tasks = [
        get_product_data_from_card('mobile', 2, card_number)
        for card_number in range(1, last_card_number + 1)
    ]
    all_data = await asyncio.gather(*tasks)

    os.makedirs('jsons', exist_ok=True)

    with open(
        'jsons/mobile_cards_data.json', 'w', encoding='utf-8'
    ) as json_file:
        json.dump(all_data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    asyncio.run(main())
