import asyncio
import os

from pyrogram_library.pyrogram_setup import app
from pyrogram_library.useful_functions import get_folder_size_and_count

group_url = 'parsinger_pyrogram'


async def main():
    async with app:
        chat = await app.get_chat(group_url)

        os.makedirs('files/images/pictures_from_chat', exist_ok=True)

        messages = [
            message
            async for message in app.get_chat_history(chat.id)
            if message.photo
        ]

        tasks = [
            download_picture(num, message.photo, len(messages))
            for num, message in enumerate(messages, start=1)
        ]
        await asyncio.gather(*tasks)

        image_count, folder_size = get_folder_size_and_count(
            'files/images/pictures_from_chat'
        )
        print(f'Total amount of downloaded pictures: {image_count}')
        print(f'Total size of all downloaded pictures: {folder_size} bites')


async def download_picture(num, photo, total):
    await app.download_media(
        photo,
        file_name=f'files/images/pictures_from_chat/{num}.png',
    )
    print(f'Downloaded images {num} / {total}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
