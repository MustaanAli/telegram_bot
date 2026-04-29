import random
from datetime import datetime, timedelta
from telegram.ext import ContextTypes

from config import GROUP_IDS, TIMEZONE


# ===============================
# 😂 ROAST DATA
# ===============================
ROAST_NAMES = [
    "Nauman", "Rahul", "Rudra", "Satyam",
    "Palak", "Anju", "Riya", "Tejas"
]

ROAST_MESSAGES = [
    "aaj kuch zyada hi silent ho... loss hua kya? 😝",
    "chart ne dhoka de diya kya? 😂",
    "entry li thi ya bas dekhte reh gaye? 👀",
    "SL hit hua kya bhai? 😭",
    "profit book kiya ya sapna hi reh gaya? 😆",
]


# ===============================
# 🔁 GLOBAL STATE
# ===============================
NEXT_ROAST_TIME = None


# ===============================
# 🎯 SCHEDULE NEXT ROAST
# ===============================
def schedule_next_roast():
    global NEXT_ROAST_TIME

    now = datetime.now(TIMEZONE)

    # Random day (next 1–28 days)
    random_days = random.randint(1, 28)

    # Random hour & minute
    random_hour = random.randint(9, 23)   # din me roast 😎
    random_minute = random.randint(0, 59)

    NEXT_ROAST_TIME = now + timedelta(days=random_days)

    NEXT_ROAST_TIME = NEXT_ROAST_TIME.replace(
        hour=random_hour,
        minute=random_minute,
        second=0
    )


# ===============================
# 🔥 MAIN ROAST FUNCTION
# ===============================
async def random_roast(context: ContextTypes.DEFAULT_TYPE):

    global NEXT_ROAST_TIME

    now = datetime.now(TIMEZONE)

    # First time setup
    if NEXT_ROAST_TIME is None:
        schedule_next_roast()
        return

    # Time match → send roast
    if now >= NEXT_ROAST_TIME:

        name = random.choice(ROAST_NAMES)
        roast = random.choice(ROAST_MESSAGES)

        msg = f"😂 {name} bhai... {roast}"

        for gid in GROUP_IDS:
            try:
                await context.bot.send_message(chat_id=gid, text=msg)
            except Exception as e:
                print(f"Error sending roast: {e}")

        # Next roast schedule
        schedule_next_roast()