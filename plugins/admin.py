from pyrogram import Client as Clinton
from pyrogram import filters
from config import Config
from database.access import clinton
from database.adduser import AddUser

@Clinton.on_message(filters.private & filters.command('total'))
async def sts(c, m):
    if m.from_user.id != Config.OWNER_ID:
        return 
    total_users = await clinton.total_users_count()
    await m.reply_text(text=f"Total user(s) {total_users}", quote=True)

@Clinton.on_message(filters.private & filters.text)
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    