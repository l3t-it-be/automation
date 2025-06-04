import asyncio

from pyrogram_library.pyrogram_setup import app

group_url = 'parsinger_pyrogram'


async def main():
    async with app:
        chat = await app.get_chat(group_url)

        messages = [
            message
            async for message in app.get_chat_history(chat.id)
            if message.from_user and message.from_user.last_online_date
        ]
        user_ids = [message.from_user.id for message in messages]
        last_online_dates = [
            message.from_user.last_online_date for message in messages
        ]

        latest_user_id = None
        last_online_date = None

        for user_id, last_online in zip(user_ids, last_online_dates):
            if last_online_date is None or last_online < last_online_date:
                last_online_date = last_online
                latest_user_id = user_id

        print(f'Last online: user with ID {latest_user_id} {last_online_date}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
