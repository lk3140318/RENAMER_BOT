from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "")

APP_ID = int(os.environ.get("APP_ID", "24335028"))

API_HASH = os.environ.get("API_HASH", "b204ec833fb451fb913fc8e683b232d0")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
