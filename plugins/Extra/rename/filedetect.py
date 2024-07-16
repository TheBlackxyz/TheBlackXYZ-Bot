# Credit @TheBlackXYZ.
# Please Don't remove credit.
# TheBlackXYZBotz Forever !
# Thanks You For Help Us In This Amazing Creativity 
# Thanks You For Giving Me Credit @TheBlackXYZBotz
# For Any ERROR Please Contact Me -> Telegram ->@TheBlackXYZBotz & Insta @TheBlackXYZ
# Please Love & Support 💗💗🙏

from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    try:
        if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply):
            new_name = message.text
            await message.delete()
            media = await client.get_messages(message.chat.id, message.reply_to_message.id)
            file = media.reply_to_message.document or media.reply_to_message.video or media.reply_to_message.audio
            filename = file.file_name
            types = file.mime_type.split("/")
            mime = types[0]
            mg_id = media.reply_to_message.id
            try:
                if ".mp4" or ".mkv" in new_name:
                    if ".mp4" in new_name:
                        new_name = new_name.replace(".mp4", "")  # Remove the dot from new_name
                    if ".mkv" in new_name:
                        new_name = new_name.replace(".mkv", "")
                else:
                    new_name = new_name
                if "." in new_name:
                    new_name = new_name.replace(".", "")  
             #   print(new_name)
                await message.reply_to_message.delete()
                if mime == "video":
                    markup = InlineKeyboardMarkup([[
                        InlineKeyboardButton("📁 Document", callback_data="upload_document"),
                        InlineKeyboardButton("🎥 Video", callback_data="upload_video")]])
                elif mime == "audio":
                    markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                        "📁 Document", callback_data="upload_document"), InlineKeyboardButton("🎵 audio", callback_data="upload_audio")]])
                else:
                    markup = InlineKeyboardMarkup(
                        [[InlineKeyboardButton("📁 Document", callback_data="upload_document")]])
                await message.reply_text(f"**Select the output file type**\n**🎞New Name** :- ```{out_filename}```", reply_to_message_id=mg_id, reply_markup=markup)

            except:
                try:
                    out = filename.split(".")
                    out_name = out[-1]
                    out_filename = new_name + "." + out_name
                #    print(f"out name: {out_filename}")
                except:
                    await message.reply_to_message.delete()
                    await message.reply_text("**Error** :  No  Extension in File, Not Supporting", reply_to_message_id=mg_id)
                    return
                await message.reply_to_message.delete()
                if mime == "video":
                    markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                        "📁 Document", callback_data="upload_document"), InlineKeyboardButton("🎥 Video", callback_data="upload_video")]])
                elif mime == "audio":
                    markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                        "📁 Document", callback_data="upload_document"), InlineKeyboardButton("🎵 audio", callback_data="upload_audio")]])
                else:
                    markup = InlineKeyboardMarkup(
                        [[InlineKeyboardButton("📁 Document", callback_data="upload_document")]])
                await message.reply_text(f"**Select the output file type**\n**🎞New Name ->** :- {out_filename}",
                                        reply_to_message_id=mg_id, reply_markup=markup)
    except Exception as e:
        print(f"error: {e}")
