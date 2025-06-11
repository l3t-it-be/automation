import asyncio

from telethon.tl.functions.users import GetFullUserRequest

from telethon_library.telethon_setup import app

# fmt: off
lst = ['vladimir_might', 'anna_starlet', 'oleg_bolds',
       'sveta_lightf', 'nikita_skyx', 'elena_bigger',
       'victor_7777778', 'daria_sweetinger', 'igorstoperz',
       'aleksey1235678', 'Alina_nemisi']
# fmt: on

group_url = 't.me/Parsinger_Telethon_Test'


async def main():
    async with app:
        participants = [
            p
            async for p in app.iter_participants(group_url)
            if p.username in lst
        ]
        full_users = await asyncio.gather(
            *[app(GetFullUserRequest(p)) for p in participants]
        )

        result = sum(
            int(p.full_user.about)
            for p in full_users
            if p.full_user
            and p.full_user.about
            and p.full_user.about.isdigit()
        )
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
