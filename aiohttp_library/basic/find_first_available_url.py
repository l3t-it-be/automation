import asyncio

from aiohttp_library.useful_functions import get_response_data


async def main():
    urls = [f'https://parsinger.ru/3.3/1/{i}.html' for i in range(1, 201)]
    tasks = [check_availability(url) for url in urls]

    result = await asyncio.gather(*tasks)
    for task in result:
        if task:
            url, number = task
            print(f'Available page: {url}\nNumber on page: {number}')
            break


async def check_availability(url):
    data = await get_response_data(url)
    if data:
        number = data.select_one('body').text.strip()
        return url, number
    return None


if __name__ == '__main__':
    asyncio.run(main())
