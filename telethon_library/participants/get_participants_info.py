import asyncio

from telethon_library.telethon_setup import app

group_url = 't.me/Parsinger_Telethon_Test'


async def main():
    async with app:
        participants_info = []

        async for p in app.iter_participants(group_url):
            first_name = p.first_name
            last_name = p.last_name or 'not specified'
            phone = p.phone or 'hidden'

            info = f'{p.id} {first_name} {last_name} {phone}'
            participants_info.append(info)

        print(participants_info)


if __name__ == '__main__':
    asyncio.run(main())
