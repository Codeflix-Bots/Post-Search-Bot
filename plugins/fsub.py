from info import *
from utils import *
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions

@Client.on_message(filters.group & filters.command("fsub"))
async def f_sub_cmd(bot, message):
    m=await message.reply("ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...")
    try:
       group     = await get_group(message.chat.id)
       user_id   = group["user_id"] 
       user_name = group["user_name"]
       verified  = group["verified"]
    except :
       return await bot.leave_chat(message.chat.id)  
    if message.from_user.id!=user_id:
       return await m.edit(f"Only {user_name} can use this command 😁")
    if bool(verified)==False:
       return await m.edit("ᴛʜɪꜱ ᴄʜᴀᴛ ɪꜱ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ 🚫\nᴜꜱᴇ /verify")
    try:
       f_sub = int(message.command[-1])
    except:
       return await m.edit("ɪɴᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ 🚫\nᴜꜱᴇ `/fsub` ᴄʜᴀɴɴᴇʟ ɪᴅ")      
    try:
       chat   = await bot.get_chat(f_sub)
       group  = await bot.get_chat(message.chat.id)
       c_link = chat.invite_link
       g_link = group.invite_link       
    except Exception as e:
       text = f"🚫  ᴇʀʀᴏʀ  - `{str(e)}`\n\nᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ɪ ᴀᴍ ᴀᴅᴍɪɴ ɪɴ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ"
       return await m.edit(text)
    await update_group(message.chat.id, {"f_sub":f_sub})
    await m.edit(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴀᴛᴛᴀᴄʜᴇᴅ ꜰᴏʀᴄᴇꜱᴜʙ ᴛᴏ [{chat.title}]({c_link})!", disable_web_page_preview=True)
    text = f"#NewFsub\n\nUser: {message.from_user.mention}\nGroup: [{group.title}]({g_link})\nChannel: [{chat.title}]({c_link})"
    await bot.send_message(chat_id=LOG_CHANNEL, text=text)


@Client.on_message(filters.group & filters.command("nofsub"))
async def nf_sub_cmd(bot, message):
    m=await message.reply("ᴅɪꜱᴀᴛᴛᴀᴄʜɪɴɢ...")
    try:
       group     = await get_group(message.chat.id)
       user_id   = group["user_id"] 
       user_name = group["user_name"]
       verified  = group["verified"]
       f_sub     = group["f_sub"]
    except :
       return await bot.leave_chat(message.chat.id)  
    if message.from_user.id!=user_id:
       return await m.edit(f"Only {user_name} can use this command 😁")
    if bool(verified)==False:
       return await m.edit("ᴛʜɪꜱ ᴄʜᴀᴛ ɪꜱ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ 🚫\nᴜꜱᴇ /verify")
    if bool(f_sub)==False:
       return await m.edit("ᴛʜɪꜱ ᴄʜᴀᴛ ᴅᴏᴇꜱ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴʏ ꜰᴏʀᴄᴇ ꜱᴜʙ\nᴜꜱᴇ /fsub")        
    try:
       chat   = await bot.get_chat(f_sub)
       group  = await bot.get_chat(message.chat.id)
       c_link = chat.invite_link
       g_link = group.invite_link       
    except Exception as e:
       text = f"🚫  ᴇʀʀᴏʀ  - `{str(e)}`\n\nᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ɪ ᴀᴍ ᴀᴅᴍɪɴ ɪɴ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀʟʟ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ"
       return await m.edit(text)
    await update_group(message.chat.id, {"f_sub":False})
    await m.edit(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇᴍᴏᴠᴇᴅ ꜰᴏʀᴄᴇ ꜱᴜʙ ғʀᴏᴍ [{chat.title}]({c_link})", disable_web_page_preview=True)
    text = f"#RemoveFsub\n\nUser: {message.from_user.mention}\nGroup: [{group.title}]({g_link})\nChannel: [{chat.title}]({c_link})"
    await bot.send_message(chat_id=LOG_CHANNEL, text=text)

       
@Client.on_callback_query(filters.regex(r"^checksub"))
async def f_sub_callback(bot, update):
    user_id = int(update.data.split("_")[-1])
    group   = await get_group(update.message.chat.id)
    f_sub   = group["f_sub"]
    admin   = group["user_id"]

    if update.from_user.id!=user_id:
       return await update.answer("ᴛʜɪꜱ  ɪꜱ  ɴᴏᴛ  ꜰᴏʀ  ʏᴏᴜ  😊", show_alert=True)
    try:
       await bot.get_chat_member(f_sub, user_id)          
    except UserNotParticipant:
       await update.answer("ꜰɪʀꜱᴛ ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜɪꜱ ʙᴜᴛᴛᴏɴ", show_alert=True)
    except:       
       await bot.restrict_chat_member(chat_id=update.message.chat.id, 
                                      user_id=user_id,
                                      permissions=ChatPermissions(can_send_messages=True,
                                                                  can_send_media_messages=True,
                                                                  can_send_other_messages=True))
       await update.message.delete()
    else:
       await bot.restrict_chat_member(chat_id=update.message.chat.id, 
                                      user_id=user_id,
                                      permissions=ChatPermissions(can_send_messages=True,
                                                                  can_send_media_messages=True,
                                                                  can_send_other_messages=True))
       await update.message.delete()