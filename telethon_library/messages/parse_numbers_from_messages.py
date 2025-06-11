import asyncio

from telethon_library.telethon_setup import app

group_url = 't.me/Parsinger_Telethon_Test'


async def main():
    async with app:
        all_messages = app.iter_messages(group_url)

        numbers = [
            int(message.text)
            async for message in all_messages
            if message.message and message.message.isdigit()
        ]
        print(sum(numbers))


if __name__ == '__main__':
    asyncio.run(main())
