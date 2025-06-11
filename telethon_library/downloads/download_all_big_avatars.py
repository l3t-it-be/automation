import asyncio
import os

from telethon_library.telethon_setup import app
from telethon_library.useful_functions import get_folder_size_and_count

group_url = 't.me/Parsinger_Telethon_Test'


async def main():
    async with app:
        users = [user async for user in app.iter_participants(group_url)]
        users_with_avatars = [user for user in users if user.photo]
        total = len(users_with_avatars)
        print(f'{total} participants with avatars found.')

        os.makedirs('files/images/avatars', exist_ok=True)

        tasks = [
            download_avatar(idx, user, total)
            for idx, user in enumerate(users_with_avatars, start=1)
        ]
        await asyncio.gather(*tasks)

        image_count, folder_size = get_folder_size_and_count(
            'files/images/avatars'
        )
        print(f'Total amount of downloaded avatars: {image_count}')
        print(f'Total size of downloaded avatars: {folder_size} bites')


async def download_avatar(idx, user, total):
    await app.download_profile_photo(
        user, f'files/images/avatars/{user.id}.png', download_big=True
    )
    print(f'{idx} / {total} avatars downloaded')


if __name__ == '__main__':
    asyncio.run(main())
