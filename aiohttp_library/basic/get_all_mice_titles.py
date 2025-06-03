import asyncio

from aiohttp_library.useful_functions import (
    get_last_page_number,
    get_response_data,
)


async def main():
    last_page_number = await get_last_page_number()

    tasks = [
        get_mice_titles(page_num)
        for page_num in range(1, last_page_number + 1)
    ]
    all_mice_titles = await asyncio.gather(*tasks, return_exceptions=True)
    mice_titles_lst = [
        title for sub_lst in all_mice_titles if sub_lst for title in sub_lst
    ]

    print(mice_titles_lst)


async def get_mice_titles(page_num):
    url = f'https://parsinger.ru/html/index3_page_{page_num}.html'
    page_data = await get_response_data(url)
    if page_data:
        mice_titles = [
            mice_title.text.strip()
            for mice_title in page_data.select('.name_item')
        ]
        return mice_titles
    else:
        print(f'Page {url} не отвечает')
        return None


if __name__ == '__main__':
    asyncio.run(main())
