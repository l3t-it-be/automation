import asyncio
import os

import aiofiles

from aiohttp_library.useful_functions import (
    get_sub_urls,
    get_response_data,
    get_folder_size_and_count,
)


async def main():
    os.makedirs('files/images/449_pictures', exist_ok=True)

    base_url = 'https://parsinger.ru/asyncio/aiofile/2/'
    urls = await get_sub_urls(base_url + 'index.html')

    tasks = [download_unique_pictures(base_url, url) for url in urls]
    await asyncio.gather(*tasks, return_exceptions=True)

    image_count, folder_size = get_folder_size_and_count(
        'files/images/449_pictures'
    )
    print(
        f'Total amount of downloaded images: {image_count}\n'
        f'Total size of downloaded images: {folder_size} bites'
    )


async def download_unique_pictures(base_url, url):
    full_url = base_url + url

    page_data = await get_response_data(full_url)
    if page_data:
        links = page_data.select('.img_box img')
        files_links = set(link.get('src') for link in links)

        for link in files_links:
            file_name = link.rsplit('/', 1)[1]
            img_data = await get_response_data(link, read=True)
            if img_data:
                async with aiofiles.open(
                    f'files/images/449_pictures/{file_name}',
                    'wb',
                ) as img_file:
                    await img_file.write(img_data)
                    print(f'Image {file_name} downloaded')
            else:
                print(f'Image link {link} is unavailable')
        else:
            print(f'Page {full_url} is unavailable')


if __name__ == '__main__':
    asyncio.run(main())
