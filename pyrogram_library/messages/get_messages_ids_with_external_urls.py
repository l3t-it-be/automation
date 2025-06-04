import asyncio

from pyrogram.enums import MessagesFilter

from pyrogram_library.pyrogram_setup import app

group_url = 'parsinger_pyrogram'


async def main():
    async with app:
        chat = await app.get_chat(group_url)
        messages_ids = [
            message.id
            async for message in app.search_messages(
                chat.id, filter=MessagesFilter.URL
            )
            if message.text and 'http' in message.text
        ]

        print(
            f'Ids of messages with external urls: {messages_ids}\n'
            f'Sum of these ids: {sum(messages_ids)}'
        )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
