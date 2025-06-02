import asyncio

from aiohttp_library.useful_functions import get_response_data


async def main():
    tasks = [check_availability(page_num) for page_num in range(1, 101)]
    result = await asyncio.gather(*tasks)
    available_pages = sorted(num for num in result if num)

    print(
        f'First available page: {available_pages[0]}.html\n'
        f'Last available page: {available_pages[-1]}.html'
    )


async def check_availability(page_num):
    url = f'https://parsinger.ru/3.3/4/{page_num}.html'

    async with await get_response_data(url, return_response=True) as response:
        if response.ok:
            return page_num
        return None


if __name__ == '__main__':
    asyncio.run(main())
