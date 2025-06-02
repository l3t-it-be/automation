import asyncio

from aiohttp_library.useful_functions import (
    get_products_categories_url_titles,
    get_last_card_number,
    get_response_data,
)


async def main():
    products_categories = await get_products_categories_url_titles()
    last_card_number = await get_last_card_number()

    tasks = [
        get_discount_cost(category, category_num, card_number)
        for category_num, category in enumerate(products_categories, 1)
        for card_number in range(1, last_card_number + 1)
    ]
    discount_costs = await asyncio.gather(*tasks, return_exceptions=True)
    print(sum(discount_costs))


async def get_discount_cost(category, category_num, card_num):
    url = f'https://parsinger.ru/html/{category}/{category_num}/{category_num}_{card_num}.html'

    data = await get_response_data(url)
    if data:
        old_price = data.select_one('#old_price').text.split()[0].strip()
        current_price = data.select_one('#price').text.split()[0].strip()
        amount = data.select_one('#in_stock').text.split(':')[1].strip()
        cost = (int(old_price) - int(current_price)) * int(amount)
        return cost
    else:
        print(f'Page {url} is unavailable')
        return None


if __name__ == '__main__':
    asyncio.run(main())
