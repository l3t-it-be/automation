import asyncio

from pyrogram_library.pyrogram_setup import app
from pyrogram_library.useful_functions import get_folder_size_and_count

group_url = 'parsinger_pyrogram'


async def main():
    async with app:
        chat = await app.get_chat(group_url)

        members_with_avatars = [
            (member.user.id, member.user.photo.big_file_id)
            async for member in app.get_chat_members(chat.id)
            if member.user.photo
        ]

        tasks = [
            download_avatar(user_id, avatar, len(members_with_avatars), index)
            for index, (user_id, avatar) in enumerate(
                members_with_avatars, start=1
            )
        ]
        await asyncio.gather(*tasks)

        image_count, folder_size = get_folder_size_and_count(
            'files/images/avatars'
        )
        print(f'Total amount of downloaded avatars: {image_count}')
        print(f'Total size of downloaded avatars: {folder_size} bites')


async def download_avatar(user_id, user_avatar, total_avatars, current_index):
    await app.download_media(
        user_avatar,
        file_name=f'files/images/avatars/{user_id}.png',
    )
    print(f'Downloaded avatars {current_index} / {total_avatars}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
