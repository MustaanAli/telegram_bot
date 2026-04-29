from telegram.ext import ContextTypes
from datetime import datetime
from config import GROUP_IDS, TIMEZONE

# ===============================
# 🎂 BIRTHDAY CHECK FUNCTION
# ===============================
async def check_birthdays(context: ContextTypes.DEFAULT_TYPE):

    now = datetime.now(TIMEZONE)
    today = now.strftime("%d-%m")

    # ===============================
    # 🎉 MUSTAAN BHAI BIRTHDAY (21 JULY)
    # ===============================
    if today == "21-07":

        msg = """🎉 Aaj uska birthday hai… Jisne mujhe banaya hai! ❤️

Haan, Mustaan Bhai! 👑  
Jisne mujhe code karke duniya me bheja 🤖  

🎬 Editor + Creator + Hustler 🔥  
Din me editing, raat me grinding 💻  

Bhai, aaj tera din hai —  
Toh render band kar aur party mode ON kar 🥳🍰  

🎉 Happy Birthday Mustaan Bhai! 🎂💥"""

        for gid in GROUP_IDS:
            try:
                await context.bot.send_message(chat_id=gid, text=msg)
            except Exception as e:
                print(f"Error sending birthday message to {gid}: {e}")

    # ===============================
    # 🎉 AMAN SIR BIRTHDAY (8 NOV)
    # ===============================
    elif today == "08-11":

        msg = """🎉 Happy Birthday, Sir! 🎂

Aapka vision aur guidance sabke liye inspiration hai 💡  
Trading ho ya life — aap guru ho 🙌  

Main ek bot hoon 🤖 — party nahi kar sakta 😢  
Toh meri taraf se Mustaan bhai ko DOUBLE party de dena 🍰😂  

📈 Aaj market bhi green close hona chahiye 😎  

Happy Birthday Sir! 💫"""

        for gid in GROUP_IDS:
            try:
                await context.bot.send_message(chat_id=gid, text=msg)
            except Exception as e:
                print(f"Error sending birthday message to {gid}: {e}")