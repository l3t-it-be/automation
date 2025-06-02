from bs4 import BeautifulSoup

from aiohttp_library.aiohttp_setup import AsyncSessionManager

first_page_url = 'https://parsinger.ru/html/index1_page_1.html'


async def get_response_data(url, return_response=False):
    session_manager = AsyncSessionManager()
    retry_client = session_manager.create_client()

    try:
        async with retry_client.get(url) as response:
            if return_response:
                return response
            if response.ok:
                return BeautifulSoup(await response.text(), 'lxml')
            return None
    except Exception as e:
        print(f'Request failed: {e}')
        return None
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
