import asyncio
import os

import aiofiles

from aiohttp_library.useful_functions import get_response_data


async def main():
    os.makedirs('files/images/160_pictures', exist_ok=True)

    tasks = [download_picture(num) for num in range(1, 161)]
    await asyncio.gather(*tasks, return_exceptions=True)


async def download_picture(num):
    url = f'https://parsinger.ru/img_download/img/ready/{num}.png'

    img_data = await get_response_data(url, read=True)
    if img_data:
        async with aiofiles.open(
            f'files/images/160_pictures/{num}.png', 'wb'
        ) as img_file:
            await img_file.write(img_data)
            print(f'Image number {num} is downloaded')
    else:
        print(f'Page {url} is unavailable')


if __name__ == '__main__':
    asyncio.run(main())
