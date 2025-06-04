import asyncio

from pyrogram_library.pyrogram_setup import app

group_url = 'parsinger_pyrogram'


async def main():
    async with app:
        chat = await app.get_chat(group_url)
        chat_description = chat.description

        numbers = []
        for char in chat_description:
            if char.isdigit() and int(char) > 0 and int(char) % 2 == 0:
                numbers.append(char)

        print(''.join(numbers))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
