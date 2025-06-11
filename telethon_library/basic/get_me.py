import asyncio

from telethon_library.telethon_setup import app


async def main():
    async with app:
        me = await app.get_me()
        print('=== Account data ===')
        print(f'First name: {me.first_name}')
        print(
            f'Last name: {me.last_name}'
            if me.last_name
            else 'Last name: not specified'
        )
        print(
            f'Username: @{me.username}'
            if me.username
            else 'Username: not specified'
        )
        print(f'ID: {me.id}')
        print(f'Phone number: +{me.phone}')


if __name__ == '__main__':
    asyncio.run(main())
