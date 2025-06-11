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

        os.makedirs('files/images/all_profile_photos', exist_ok=True)

        tasks = [
            download_avatars(idx, user, total)
            for idx, user in enumerate(users_with_avatars, start=1)
        ]
        await asyncio.gather(*tasks)

        image_count, folder_size = get_folder_size_and_count(
            'files/images/all_profile_photos'
        )
        print(f'Total amount of downloaded avatars: {image_count}')
        print(f'Total size of all downloaded avatars: {folder_size} bites')


async def download_avatars(idx, user, total):
    all_user_avatars = [photo async for photo in app.iter_profile_photos(user)]
    count = len(all_user_avatars)
    print(f'Participant with id {user.id} has {count} profile photos')

    for num, iter_photo in enumerate(all_user_avatars, start=1):
        await app.download_media(
            iter_photo,
            file=f'files/images/all_profile_photos/user_{user.id}/{num}',
        )
        print(f'{num} / {count} user {user.id} profile photos downloaded')

    print(f'{idx} / {total} profile photos downloaded')


if __name__ == '__main__':
    asyncio.run(main())
