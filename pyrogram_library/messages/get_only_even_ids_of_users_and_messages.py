import asyncio

from pyrogram_library.pyrogram_setup import app

group_url = 'parsinger_pyrogram'


async def main():
    async with app:
        chat = await app.get_chat(group_url)

        even_messages = [
            message
            async for message in app.get_chat_history(chat.id)
            if message.id % 2 == 0
            and message.from_user
            and message.from_user.id % 2 == 0
            and message.text
            and len(message.text.replace(' ', '')) % 2 == 0
        ]

        even_messages_products = [
            message.id
            * message.from_user.id
            * len(message.text.replace(' ', ''))
            for message in even_messages
        ]

        result = sum(even_messages_products)
        print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
