import asyncio
import os

from telethon.tl.types import InputMessagesFilterPhotos

from telethon_library.telethon_setup import app
from telethon_library.useful_functions import get_folder_size_and_count

group_url = 't.me/Parsinger_Telethon_Test'


async def main():
    async with app:
        messages = [
            message
            async for message in app.iter_messages(
                group_url, filter=InputMessagesFilterPhotos
            )
        ]
        total_messages = len(messages)
        print(f'{total_messages} messages with pictures found.')

        os.makedirs('files/images/pictures', exist_ok=True)

        tasks = [
            download_picture(idx, message, total_messages)
            for idx, message in enumerate(messages, start=1)
        ]
        await asyncio.gather(*tasks)

        image_count, folder_size = get_folder_size_and_count(
            'files/images/pictures'
        )
        print(f'Total amount of downloaded pictures: {image_count}')
        print(f'Total size of downloaded pictures: {folder_size} bites')


async def download_picture(idx, message, total):
    await app.download_media(
        message, file=f'files/images/pictures/{message.id}'
    )
    print(f'{idx} / {total} pictures downloaded')


if __name__ == '__main__':
    asyncio.run(main())
