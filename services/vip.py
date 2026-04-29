from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime

from config import MUSTAAN_ID, AMAN_SIR_ID, TIMEZONE


# ===============================
# 🔁 GLOBAL STATE
# ===============================
last_session_date = None


# ===============================
# 👑 VIP TRIGGERS
# ===============================
async def vip_triggers(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global last_session_date

    # Safety
    if not update.message or not update.message.text:
        return False

    user_id = update.effective_user.id
    text = update.message.text.lower()
    today = datetime.now(TIMEZONE).date()

    # ===============================
    # 🔥 AMAN SIR TRIGGER
    # ===============================
    if user_id == AMAN_SIR_ID and "session" in text:

        # ek din me ek baar hi trigger ho
        if last_session_date != today:
            last_session_date = today

            await update.message.reply_text(
                "🔥 Aman Sir ne bola hai SESSION!\n"
                "Aaj session me maza aane wala hai 🚀📈"
            )

        return True

    # ===============================
    # 👑 MUSTAAN TRIGGER
    # ===============================
    if user_id == MUSTAAN_ID and "bot" in text:

        await update.message.reply_text(
            "👑 BOSS ENTRY DETECTED 😎\n"
            "Yeahhhhh bhaiya aa gaye!!! 🔥\n"
            "Main underground ho raha hu 🫡\n\n"
            "Bade bhaiya boliye, kya order hai? 🚀"
        )

        return True

    return False