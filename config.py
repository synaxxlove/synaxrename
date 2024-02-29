import os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN = int(os.environ.get("ADMIN", ""))

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """𝐇𝐞𝐥𝐥𝐨 {} 👋 

➻ 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐚𝐧 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐚𝐧𝐝 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐑𝐞𝐧𝐚𝐦𝐞 𝐁𝐨𝐭.

➻ 𝐔𝐬𝐢𝐧𝐠 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐑𝐞𝐧𝐚𝐦𝐞 𝐚𝐧𝐝 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐨𝐟 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞𝐬.

➻ 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐚𝐥𝐬𝐨 𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐯𝐢𝐝𝐞𝐨 𝐓𝐨 𝐅𝐢𝐥𝐞 𝐚𝐧𝐝 𝐅𝐢𝐥𝐞 𝐓𝐨 𝐯𝐢𝐝𝐞𝐨.

➻ 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐚𝐥𝐬𝐨 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐂𝐮𝐬𝐭𝐨𝐦 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐚𝐧𝐝 𝐂𝐮𝐬𝐭𝐨𝐦 𝐂𝐚𝐩𝐭𝐢𝐨𝐧.

<b>𝐁𝐨𝐭 𝐢𝐬 𝐅𝐮𝐥𝐥𝐲 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 :</b> @synaxnetwork"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🌸 𝐌𝐲 𝐍𝐚𝐦𝐞</b> : {}
├<b>🌺 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫</b> : <a href=https://t.me/synaxnetwork>𝗦𝘆𝗻𝗮𝘅 𝗕𝗼𝘁𝘀</a> 
├<b>🥀 𝐎𝐰𝐧𝐞𝐫</b> : <a href=https://t.me/sanatanisynax>𝗦𝗮𝗻𝗮𝘁𝗮𝗻𝗶 𝗦𝘆𝗻𝗮𝘅</a>
├<b>📕 𝐋𝐢𝐛𝐫𝐚𝐫𝐲</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>📊 𝐁𝐮𝐢𝐥𝐝 𝐕𝐞𝐫𝐬𝐢𝐨𝐧</b> : <a href=https://instagram.com/sanatanisynax>Rename v4.5.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>𝐇𝐨𝐰 𝐓𝐨 𝐬𝐞𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 🌸</u></b>
  
➪ /start - 𝐒𝐭𝐚𝐫𝐭 𝐓𝐡𝐞 𝐁𝐨𝐭 𝐚𝐧𝐝 𝐒𝐞𝐧𝐝 𝐚𝐧𝐲 𝐏𝐡𝐨𝐭𝐨 𝐓𝐨 𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜𝐚𝐥𝐥𝐲 𝐒𝐞𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥.
➪ /del_thumb - 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐞𝐥𝐞𝐭𝐞 𝐘𝐨𝐮𝐫 𝐎𝐥𝐝 𝐓𝐡𝐮𝐦𝐛𝐚𝐢𝐥.
➪ /view_thumb - 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐯𝐢𝐞𝐰 𝐘𝐨𝐮𝐫 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥.

📑 <b><u>𝐇𝐨𝐰 𝐓𝐨 𝐒𝐞𝐭 𝐂𝐮𝐬𝐭𝐨𝐦 𝐂𝐚𝐩𝐭𝐢𝐨𝐧</u></b>

➪ /set_caption - 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐬𝐞𝐭 𝐚 𝐂𝐮𝐬𝐭𝐨𝐦 𝐂𝐚𝐩𝐭𝐢𝐨𝐧.
➪ /see_caption - 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐯𝐢𝐞𝐰 𝐘𝐨𝐮𝐫 𝐂𝐮𝐬𝐭𝐨𝐦 𝐂𝐚𝐩𝐭𝐢𝐨𝐧.
➪ /del_caption - 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐞𝐥𝐞𝐭𝐞 𝐘𝐨𝐮𝐫 𝐂𝐮𝐬𝐭𝐨𝐦 𝐂𝐚𝐩𝐭𝐢𝐨𝐧.
➪ Example - <code>/set_caption 📕 𝐍𝐚𝐦𝐞 ➠ : {filename}

🔗 𝐒𝐢𝐳𝐞 ➠ : {filesize} 

⏰ 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 ➠ : {duration}</code>

✏️ <b><u>𝐇𝐨𝐰 𝐓𝐨 𝐑𝐞𝐧𝐚𝐦𝐞 𝐚 𝐅𝐢𝐥𝐞</u></b>

➪ 𝐒𝐞𝐧𝐝 𝐚𝐧𝐲 𝐅𝐢𝐥𝐞 𝐚𝐧𝐝 𝐓𝐲𝐩𝐞 𝐍𝐞𝐰 𝐅𝐢𝐥𝐞 𝐍𝐚𝐦𝐞 𝐚𝐧𝐝 𝐒𝐞𝐥𝐞𝐜𝐭 𝐓𝐡𝐞 𝐅𝐨𝐫𝐦𝐚𝐭 [ 𝐃𝐨𝐜𝐮𝐦𝐞𝐧𝐭, 𝐕𝐢𝐝𝐞𝐨, 𝐀𝐮𝐝𝐢𝐨 ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/synaxnetwork>𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 𝐒𝐢𝐳𝐞 :</b> {1} | {2}
️ <b>⏳️ 𝐃𝐨𝐧𝐞 :</b> {0}%
 <b>🚀 𝐒𝐩𝐞𝐞𝐝 :</b> {3}/s
️ <b>⏰️ 𝐄𝐓𝐀 :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐒𝐡𝐨𝐰𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐢𝐧 𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧 ❤️</b>

𝐈𝐟 𝐘𝐨𝐮 𝐋𝐢𝐤𝐞 𝐌𝐲 𝐁𝐨𝐭𝐬 & 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬 , 𝐘𝐨𝐮 𝐂𝐚𝐧 🎁 𝐃𝐨𝐧𝐚𝐭𝐞 𝐌𝐞 𝐚𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐅𝐫𝐨𝐦 10 𝐑𝐬 𝐮𝐩𝐭𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐨𝐢𝐜𝐞.

<b>🛍 𝐔𝐩𝐢 𝐈𝐝:</b> `abhishekxsynax@fam`
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
