import telethon
from telethon import TelegramClient, events, sync

api_id = fffffff # Your api_id
api_hash = 'ffffff'  # Your api_hash

client = TelegramClient('session_name', api_id, api_hash)
client.start()
