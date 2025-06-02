import asyncio

from aiohttp_library.useful_functions import get_response_data


async def main():
    urls = [f'https://parsinger.ru/3.3/2/{i}.html' for i in range(1, 201)]
    tasks = [get_status_code(url) for url in urls]

    status_codes = await asyncio.gather(*tasks)
    print(f'Сумма статус-кодов: {sum(status_codes)}')


async def get_status_code(url):
    response = await get_response_data(url, return_response=True)
    return response.status


if __name__ == '__main__':
    asyncio.run(main())
