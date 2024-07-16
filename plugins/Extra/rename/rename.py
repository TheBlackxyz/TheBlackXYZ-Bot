# Credit @TheBlackXYZ.
# Please Don't remove credit.
# TheBlackXYZBotz Forever !
# Thanks You For Help Us In This Amazing Creativity 
# Thanks You For Giving Me Credit @TheBlackXYZBotz
# For Any ERROR Please Contact Me -> Telegram ->@TheBlackXYZBotz & Insta @TheBlackXYZ
# Please Love & Support 💗💗🙏


from asyncio import sleep
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
from info import RENAME_MODE
import humanize
import random

@Client.on_message(filters.private & filters.command("rename"))
async def rename_start(client, message):
    if RENAME_MODE == False:
        return 
    msg = await client.ask(message.chat.id, "**Now send me your file/video/audio to rename.**")
    if not msg.media:
        return await message.reply("**Please send me supported media.**")
    if msg.media in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.DOCUMENT, enums.MessageMediaType.AUDIO]:
        file = getattr(msg, msg.media.value)
        filename = file.file_name
        filesize = humanize.naturalsize(file.file_size) 
        fileid = file.file_id
        try:
            text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                       [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
            await msg.reply_text(text=text, reply_to_message_id=msg.id, reply_markup=InlineKeyboardMarkup(buttons))
           # await sleep(FLOOD)
        except FloodWait as e:
            await sleep(e.value)
            text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                       [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
            await msg.reply_text(text=text, reply_to_message_id=msg.id, reply_markup=InlineKeyboardMarkup(buttons))
        except Exception as e:
            print(e)
      
