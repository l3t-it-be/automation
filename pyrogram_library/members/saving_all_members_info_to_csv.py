import asyncio
import csv
import os

from pyrogram_library.pyrogram_setup import app

group_url = 'parsinger_pyrogram'


async def main():
    # fmt: off
    csv_headers = ['ID', 'Username', 'First Name', 'Last Name',
                   'Phone Number', 'Last Online Date', 'Joined Date',
                   'Is Bot', 'Is Self', 'Is Contact', 'Is Verified',
                   'Is Restricted', 'Is Scam', 'Is Fake', 'Is Support',
                   'Is Premium']
    # fmt: on

    os.makedirs('files/csvs', exist_ok=True)

    with open(
        'files/csvs/parsinger_members_info.csv',
        'w',
        encoding='utf-8-sig',
        newline='',
    ) as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(csv_headers)

    async with app:
        chat = await app.get_chat(group_url)
        members = [member async for member in app.get_chat_members(chat.id)]
        tasks = [get_member_info(member) for member in members]

        all_data = await asyncio.gather(*tasks, return_exceptions=True)
        all_data = [data for data in all_data if isinstance(data, list)]

        with open(
            'files/csvs/parsinger_members_info.csv',
            'a',
            encoding='utf-8-sig',
            newline='',
        ) as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerows(all_data)


async def get_member_info(member):
    try:
        user = member.user

        user_id = user.id
        username = f'@{user.username}' if user.username else 'None'
        first_name = user.first_name if user.first_name else 'None'
        last_name = user.last_name if user.last_name else 'None'
        phone_number = user.phone_number if user.phone_number else 'None'
        last_online_date = (
            user.last_online_date if user.last_online_date else 'None'
        )
        joined_date = (
            member.joined_date if hasattr(member, 'joined_date') else 'None'
        )
        is_bot = user.is_bot
        is_self = user.is_self
        is_contact = user.is_contact
        is_verified = user.is_verified
        is_restricted = user.is_restricted
        is_scam = user.is_scam
        is_fake = user.is_fake
        is_support = user.is_support
        is_premium = user.is_premium

        # fmt: off
        user_data = [user_id, username, first_name, last_name, phone_number,
                     last_online_date, joined_date, is_bot, is_self, is_contact,
                     is_verified, is_restricted, is_scam, is_fake, is_support,
                     is_premium]
        # fmt: on
        return user_data
    except Exception as e:
        print(f'Error processing member {member.user.id}: {e}')
        return None


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
