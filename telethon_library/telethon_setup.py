from telethon import TelegramClient

api_id = 12345678  # just an example
api_hash = '*********************'

app = TelegramClient(
    'my_session',
    api_id=api_id,
    api_hash=api_hash,
    system_version='5.14.3 x64',  # your version of Telegram app
)
