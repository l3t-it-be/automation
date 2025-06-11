import asyncio

from telethon_library.telethon_setup import app

group_url = 't.me/Parsinger_Telethon_Test'
user_id = 6388067367


async def main():
    async with app:
        messages = app.iter_messages(group_url, from_user=user_id)
        async for message in messages:
            if message.message and message.message.isdigit():
                print(int(message.message))
                break


if __name__ == '__main__':
    asyncio.run(main())
