from telegram import Update
from telegram.ext import ContextTypes
import json
import os
import time

from config import MUSTAAN_ID

USERS_FILE = "data/users.json"

# ===============================
# 🧠 COOLDOWN SYSTEM
# ===============================
USER_COOLDOWN = {}   # user_id -> last_used_time


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


# ===============================
# 🏆 LEADERBOARD COMMAND
# ===============================
async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    now = time.time()

    # ===============================
    # ❗ COOLDOWN (24 HOURS)
    # ===============================
    if user_id != MUSTAAN_ID:  # admin bypass
        if user_id in USER_COOLDOWN:
            if now - USER_COOLDOWN[user_id] < 86400:
                await update.message.reply_text(
                    "⏳ Bhai thoda ruk jao 😅\n"
                    "Leaderboard roz ek baar hi dekh sakte ho ❤️"
                )
                return

        USER_COOLDOWN[user_id] = now

    # ===============================
    # 📊 LOAD USERS
    # ===============================
    users = load_users()

    if not users:
        await update.message.reply_text("⚠️ Abhi tak koi data nahi hai bhai 😅")
        return

    # ===============================
    # 🔥 SORT (POINTS + TIMESTAMP)
    # ===============================
    sorted_users = sorted(
        users.values(),
        key=lambda x: (
            -x.get("points", 0),                     # high points first
            x.get("last_correct", float("inf"))      # earlier = better
        )
    )

    top = sorted_users[:5]

    # ===============================
    # 🏆 BUILD MESSAGE
    # ===============================
    msg = "🏆 *Top 5 Traders Leaderboard:*\n\n"

    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

    for i, user in enumerate(top):
        name = user.get("name", "Unknown")
        points = user.get("points", 0)

        msg += f"{medals[i]} {name} — {points} pts\n"

    msg += "\n🔥 Keep learning, keep earning!"

    await update.message.reply_text(msg, parse_mode="Markdown")