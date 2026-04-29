import random
from datetime import datetime
from telegram.ext import ContextTypes

from config import GROUP_IDS, TIMEZONE
from data.messages import MOOD_MESSAGES, CHEERUP_MESSAGES


# ===============================
# 🔁 GLOBAL STATE
# ===============================
RANDOM_MOOD_DAY = random.randint(1, 28)
LAST_MOOD_MONTH = -1

last_mood_index = -1
last_cheer_index = -1


# ===============================
# 😔 MONTHLY MOOD CHECK
# ===============================
async def monthly_mood_check(context: ContextTypes.DEFAULT_TYPE):
    global RANDOM_MOOD_DAY, LAST_MOOD_MONTH, last_mood_index

    now = datetime.now(TIMEZONE)

    # Check: same month me ek hi baar chale
    if now.day == RANDOM_MOOD_DAY and LAST_MOOD_MONTH != now.month:

        LAST_MOOD_MONTH = now.month
        RANDOM_MOOD_DAY = random.randint(1, 28)

        # Next mood message (no repeat pattern)
        last_mood_index = (last_mood_index + 1) % len(MOOD_MESSAGES)
        mood_msg = MOOD_MESSAGES[last_mood_index]

        for gid in GROUP_IDS:
            try:
                await context.bot.send_message(chat_id=gid, text=mood_msg)
            except Exception as e:
                print(f"Error sending mood msg to {gid}: {e}")

        # ⏳ 11 min baad cheer-up message
        context.job_queue.run_once(send_cheer_message, when=660)


# ===============================
# 😄 CHEER-UP MESSAGE
# ===============================
async def send_cheer_message(context: ContextTypes.DEFAULT_TYPE):
    global last_cheer_index

    last_cheer_index = (last_cheer_index + 1) % len(CHEERUP_MESSAGES)
    cheer_msg = CHEERUP_MESSAGES[last_cheer_index]

    for gid in GROUP_IDS:
        try:
            await context.bot.send_message(chat_id=gid, text=cheer_msg)
        except Exception as e:
            print(f"Error sending cheer msg to {gid}: {e}")