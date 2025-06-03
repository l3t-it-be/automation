import asyncio

from aiohttp_library.useful_functions import (
    get_last_card_number,
    get_response_data,
)


async def main():
    last_card_number = await get_last_card_number()

    tasks = [
        get_mice_article(card_number)
        for card_number in range(1, last_card_number + 1)
    ]
    articles = await asyncio.gather(*tasks, return_exceptions=True)
    print(sum(articles))


async def get_mice_article(card_number):
    url = f'https://parsinger.ru/html/mouse/3/3_{card_number}.html'

    page_data = await get_response_data(url)
    if page_data:
        article = page_data.select_one('.article').text.split()[1].strip()
        return int(article)
    else:
        print(f'Page {url} is unavailable')
        return None


if __name__ == '__main__':
    asyncio.run(main())
