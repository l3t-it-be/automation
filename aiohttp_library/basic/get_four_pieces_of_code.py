import asyncio

from aiohttp_library.useful_functions import get_response_data


async def main():
    start_page_data = await get_response_data(
        'https://parsinger.ru/asyncio/create_soup/1/index.html'
    )
    if start_page_data:
        urls = start_page_data.select('a[href]')

        tasks = [
            get_secret_code(
                'https://parsinger.ru/asyncio/create_soup/1/' + url['href']
            )
            for url in urls
        ]
        results = await asyncio.gather(*tasks)
        print(sum(results))
    else:
        print('Page is unavailable')


async def get_secret_code(url):
    data = await get_response_data(url)
    if data:
        code_part = int(data.select_one('p.text').text)
        print(f'Код найден на странице {url}: {code_part}')
        return code_part
    return 0


if __name__ == '__main__':
    asyncio.run(main())
