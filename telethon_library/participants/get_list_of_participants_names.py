import asyncio

from telethon_library.telethon_setup import app

group_url = 't.me/Parsinger_Telethon_Test'


async def main():
    async with app:
        participants = app.iter_participants(group_url)

        names_list = [
            (
                f'{p.first_name} {p.last_name}'
                if p.last_name
                else f'{p.first_name} not specified'
            )
            async for p in participants
        ]

        print(names_list)


if __name__ == '__main__':
    asyncio.run(main())
