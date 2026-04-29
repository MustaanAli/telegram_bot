from telegram import Update
from telegram.ext import ContextTypes


# ===============================
# 🤖 BOT ADDED TO GROUP
# ===============================
async def bot_added(update: Update, context: ContextTypes.DEFAULT_TYPE):

    result = update.my_chat_member

    old_status = result.old_chat_member.status
    new_status = result.new_chat_member.status

    # Check: bot added to group
    if old_status in ("left", "kicked") and new_status in ("member", "administrator"):

        chat = update.effective_chat

        msg = """
👋 Hello Everyone!

Main hoon *lil Yuwan Bot* 🤖  
Aur mujhe banaya hai mere creator — **Mustaan Bhai** ne 👑  

💡 *Main kya kya karta hoon:*

📈 Trading motivation deta hoon  
📘 Journal reminders  
📊 Quiz & learning polls  
🌞 Daily good morning messages  
😂 Thoda masti roast bhi  
🧠 Mood messages + cheer up  
🛡️ Anti-spam protection  

Aur haan…  
Main abhi bhi seekh raha hoon 🧑‍💻  

Agar kuch galti karu toh Mustaan bhai ko blame mat karna 😂❤️  

Chalo phir, group me thoda knowledge aur thoda fun add karte hain! 🎉
"""

        await context.bot.send_message(
            chat_id=chat.id,
            text=msg,
            parse_mode="Markdown"
        )