import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VipX import app  

photo = [
    "https://te.legra.ph/file/eb5b17bf2fdc09f73f6b2.jpg",
    "https://te.legra.ph/file/d4bf46af570e1d72eabd5.jpg",
    "https://graph.org/file/40ce67d14a3f5a7136090.jpg",
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"🌷𝐇ᴇʏ {message.from_user.mention}
💜😍 ਤੁਹਾਡਾ ਸਾਡੇ ਛੋਟੇ ਜੇਹੇ ਗਰੁੱਪ ਚ ਸਵਾਗਤ ਆ
╔═════════════════╗
💓 ᴋᴇᴇᴘ sᴍɪʟᴇ ᴏɴ ʏᴏᴜʀ ғᴀᴄᴇ💓  
╚═════════════════╝
╔══════════════════\n\n"
                f"╠ ❤️𝗡𝗔𝗠𝗘⇝@{message.first}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"╠ 🖤𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 ⇝@{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"╠ 💜𝗨𝗦𝗘𝗥 𝗜'𝗱 ⇝ {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"╠❤️𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉"
╚══════════════════
                f"° ਰੂਲਜ਼  :- ❤️ 🧸
┏━━━━━━━━━━━━━━━━━
┣ 𝟏 = ਗਾਲਾਂ ਨਾ ਕੱਢੋ = ❤️🤙
┣ 𝟐 = ਕੁੜੀਆਂ ਨੂੰ ਡੀ ਐਮ ਨਾ ਕਰੋ = 🥲❤️
┣ 𝟑 = ਸਪੈਮ ਕਰਨਾ ਮਨਾ ਹੈ = ❤️🙌
┣ 𝟒 = ਗੰਦੀਆਂ ਚੀਜਾਂ ਤੋਂ ਗਰੁੱਪ ਨੂੰ ਐਲਰਜੀ ਆ ❤️👻
┗━━━━━━━━━━━━━━━━━
┏━━━━━━━
   ⎯꯭‌🇨🇦꯭꯭ ⃪В꯭α꯭∂ ꯭м꯭υ꯭η∂꯭α_꯭آآ⎯꯭ ꯭‌🌸
┗━━━━━━━
┏━━━━━━━━━━━━━━━━━
👉 ਸਾਡਾ ਵੈਲਕਮ ਮੈਸਜ ਕੋਪੀ ਨਾ ਕਰਿਓ 😊
[ - ਕੁੜੀਆਂ ਦੀ ਇੱਜਤ ਕਰੋ ❤️💫
┗━━━━━━━━━━━━━━━━━
• ਰੂਲਜ਼ ਨੂੰ ਮੱਦੇਨਜ਼ਰ ਰੱਖਦੇ ਹੋਏ ਗੱਲ ਕਰੋ :- ✨ 🕊☝️
• ਧੰਨਵਾਦ 🥀💛🌹🤞💫\n\n"
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🥳ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄʜᴀᴛ🥳", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
