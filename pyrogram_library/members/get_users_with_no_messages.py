import asyncio

from pyrogram_library.pyrogram_setup import app

group_url = 'parsinger_pyrogram'


async def main():
    async with app:
        chat = await app.get_chat(group_url)

        members_ids = [
            member.user.id async for member in app.get_chat_members(chat.id)
        ]
        messages = [message async for message in app.get_chat_history(chat.id)]

        users_ids_with_messages = [
            message.from_user.id for message in messages if message.from_user
        ]
        users_ids_without_messages = [
            user_id
            for user_id in members_ids
            if user_id not in users_ids_with_messages
        ]
        sum_ids = sum(users_ids_without_messages)

        print(
            f'Users with no messages: {users_ids_without_messages}\nSum ids: {sum_ids}'
        )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
