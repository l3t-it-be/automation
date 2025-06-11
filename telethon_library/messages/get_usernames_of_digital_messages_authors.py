import asyncio

from telethon_library.telethon_setup import app

group_url = 't.me/Parsinger_Telethon_Test'


async def main():
    async with app:
        messages = [
            message
            async for message in app.iter_messages(group_url)
            if message.message and message.message.isdigit()
        ]
        tasks = [get_username(message) for message in messages]
        results = await asyncio.gather(*tasks)
        usernames = [username for username in results if username is not None]
        print(usernames)


async def get_username(message):
    user_id = message.from_id.user_id
    entity = await app.get_entity(user_id)
    if entity.username:
        return entity.username
    else:
        return None


if __name__ == '__main__':
    asyncio.run(main())
