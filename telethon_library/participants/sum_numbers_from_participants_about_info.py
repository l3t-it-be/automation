import asyncio

from telethon.tl.functions.users import GetFullUserRequest

from telethon_library.telethon_setup import app

# fmt: off
lst = [7478070952, 6388067367, 6903264582,
       6508314190, 6785254031, 6774119671,
       6807753588, 6496620987, 6788724315,
       6810623013, 6816260703, 6581321535]
# fmt: on

group_url = 't.me/Parsinger_Telethon_Test'


async def main():
    async with app:
        participants = [
            p async for p in app.iter_participants(group_url) if p.id in lst
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
