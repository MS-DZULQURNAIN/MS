from pyrogram import Client, filters, idle

API_ID = int(26915599)
API_HASH = "76438a4fa64f9e43b3921a204a79e000"
BOT_TOKEN = "5895166821:AAFix2nQtVRZqqOtl1QBHw1Uln7hsf_u01M"

#Botting Process
app = Client(name="Okk", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, in_memory=True)

#Command Running

@app.on_message(filters.command([start, "st"] & filters.private)
async def _(app, message):
    await message.reply_text("APA NJING")
