import asyncio

from telethon.tl.types import InputMessagesFilterPinned

from telethon_library.telethon_setup import app

group_url = 't.me/Parsinger_Telethon_Test'


async def main():
    async with app:
        messages = await app.get_messages(
            group_url, filter=InputMessagesFilterPinned
        )
        user_id = messages[0].from_id.user_id
        print(user_id)


if __name__ == '__main__':
    asyncio.run(main())
