import asyncio

from pyrogram_library.pyrogram_setup import app

group_url = 'parsinger_pyrogram'


async def main():
    async with app:
        chat = await app.get_chat(group_url)
        big_photo = chat.photo.big_file_id
        await app.download_media(
            big_photo, file_name='files/images/big_avatar.png'
        )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
