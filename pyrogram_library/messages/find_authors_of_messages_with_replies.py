import asyncio

from pyrogram_library.pyrogram_setup import app

group_url = 'parsinger_pyrogram'


async def main():
    async with app:
        chat = await app.get_chat(group_url)

        messages = [message async for message in app.get_chat_history(chat.id)]
        parent_message_ids = set(
            message.reply_to_message_id
            for message in messages
            if message.reply_to_message_id
        )

        parent_message_authors = set(
            message.from_user.id
            for message in messages
            if message.id in parent_message_ids and message.from_user
        )
        sum_user_ids = sum(parent_message_authors)
        print(
            f'Message authors ids: {", ".join(map(str, parent_message_authors))}\n'
            f'Sum ids: {sum_user_ids}'
        )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
