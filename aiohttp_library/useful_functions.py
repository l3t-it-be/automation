import os

import aiofiles
from bs4 import BeautifulSoup

from aiohttp_library.aiohttp_setup import AsyncSessionManager

first_page_url = 'https://parsinger.ru/html/index1_page_1.html'


async def get_response_data(url, return_response=False, read=False):
    session_manager = AsyncSessionManager()
    retry_client = session_manager.create_client()

    try:
        async with retry_client.get(url) as response:
            if return_response:
                return response
            if response.ok:
                if read:
                    return await response.read()
                return BeautifulSoup(await response.text(), 'lxml')
            return None
    except Exception as e:
        print(f'Request failed: {e}')
        return None
    finally:
        await session_manager.close_session()


async def download_video(video_url, file_path, chunk_size=1024):
    session_manager = AsyncSessionManager()
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        retry_client = session_manager.create_client()
        async with retry_client.get(video_url) as response:
            if not response.ok:
                print(f'Failed to download video: HTTP {response.status}')
                return False

            async with aiofiles.open(file_path, 'wb') as file:
                async for chunk in response.content.iter_chunked(chunk_size):
                    await file.write(chunk)
            return True

    except Exception as e:
        print(f'Video download failed: {e}')
        return False
    finally:
        await session_manager.close_session()


async def get_first_page_data() -> BeautifulSoup | None:
    first_page_data = await get_response_data(first_page_url)
    return first_page_data


async def get_products_categories_url_titles() -> list | None:
    data = await get_first_page_data()
    if data:
        categories = [
            category.get('id') for category in data.select('.nav_menu div[id]')
        ]
        return categories
    else:
        print('The page is unavailable')
        return None


async def get_last_page_number() -> int | None:
    data = await get_first_page_data()
    if data:
        return int(data.select('.pagen a')[-1].text)
    else:
        print('The page is unavailable')
        return None


async def get_last_card_number() -> int | None:
    last_page_number = await get_last_page_number()
    last_page_url = (
        f'https://parsinger.ru/html/index1_page_{last_page_number}.html'
    )
    last_page_data = await get_response_data(last_page_url)
    if last_page_data:
        last_card_name = last_page_data.select('a.name_item')[-1].get('name')
        last_card_number = last_card_name.split('_')[1]
        return int(last_card_number)
    else:
        print('The page is unavailable')
        return None


async def get_sub_urls(url) -> list | None:
    page_data = await get_response_data(url)
    if page_data:
        urls = [a['href'] for a in page_data.select('a[href]')]
        return urls
    else:
        print('The page is unavailable')
        return None


def get_folder_size_and_count(filepath):
    count = sum(len(files) for root, dirs, files in os.walk(filepath))
    total_size = sum(
        os.path.getsize(os.path.join(root, file))
        for root, dirs, files in os.walk(filepath)
        for file in files
    )
    return count, total_size
