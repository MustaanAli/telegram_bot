from telegram import Update
from telegram.ext import ContextTypes
import random
import re

from data.triggers import TRIGGER_RESPONSES
from services.anti_spam import anti_spam_reply
from services.vip import vip_triggers


# ===============================
# 💬 TEXT HANDLER
# ===============================
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Safety: message + text check
    if not update.message or not update.message.text:
        return

    # Normalize text
    text = update.message.text.lower().strip()

    # ===============================
    # 👑 VIP TRIGGERS (HIGHEST PRIORITY)
    # ===============================
    if await vip_triggers(update, context):
        return

    # ===============================
    # 🛡️ ANTI-SPAM
    # ===============================
    if await anti_spam_reply(update, context):
        return

    # ===============================
    # 🎯 TRIGGER RESPONSES (SMART MATCH)
    # ===============================
    for trigger, responses in TRIGGER_RESPONSES.items():

        # word boundary matching (better than simple "in")
        pattern = r"\b" + re.escape(trigger) + r"\b"

        if re.search(pattern, text):
            await update.message.reply_text(random.choice(responses))
            return  # ek hi response

    # ===============================
    # 🤖 SMART FALLBACK REPLIES
    # ===============================

    greetings = ["hi", "hello", "hey", "hii"]
    thanks_words = ["thanks", "thank you", "thx"]
    bye_words = ["bye", "good night", "gn"]

    if any(word in text for word in greetings):
        await update.message.reply_text(
            "👋 Hello bhai! Try karo:\n👉 motivate\n👉 rule\n👉 journal 😎"
        )

    elif any(word in text for word in thanks_words):
        await update.message.reply_text(
            "😄 Welcome bhai! Always here 🚀"
        )

    elif any(word in text for word in bye_words):
        await update.message.reply_text(
            "👋 Bye bhai! Kal market me milte hain 📈"
        )

    # ===============================
    # 🤫 SILENT IGNORE (ANTI-SPAM UX)
    # ===============================
    # Agar kuch match nahi hua → bot chup rahe