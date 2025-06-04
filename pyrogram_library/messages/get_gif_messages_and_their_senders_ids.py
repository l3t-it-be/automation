import asyncio

from pyrogram.enums import MessagesFilter

from pyrogram_library.pyrogram_setup import app

group_url = 'parsinger_pyrogram'


async def main():
    async with app:
        chat = await app.get_chat(group_url)
        messages = [
            message
            async for message in app.search_messages(
                chat.id, filter=MessagesFilter.ANIMATION
            )
        ]
        users_ids = [message.from_user.id for message in messages]
        result = sum(
            [
                message.id * user_id
                for message, user_id in zip(messages, users_ids)
            ]
        )
        print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
