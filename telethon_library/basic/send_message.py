import asyncio

from telethon_library.telethon_setup import app


async def main():
    async with app:
        await app.send_message(
            '@l3t_it_be', 'Hello, Kate! You\'re breathtaking!'
        )


if __name__ == '__main__':
    asyncio.run(main())
