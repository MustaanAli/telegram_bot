import json
import os
from datetime import datetime
from telegram.ext import ContextTypes

from config import GROUP_IDS, TIMEZONE

USERS_FILE = "data/users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_users(data):
    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ===============================
# 🏆 MONTHLY TOP 3 + RESET
# ===============================
async def monthly_winner(context: ContextTypes.DEFAULT_TYPE):

    now = datetime.now(TIMEZONE)

    # ❗ Sirf 28th ko run kare
    if now.day != 28:
        return

    users = load_users()

    if not users:
        return

    # ===============================
    # 🔥 SORT USERS (POINTS + TIME)
    # ===============================
    sorted_users = sorted(
        users.values(),
        key=lambda x: (
            -x.get("points", 0),
            x.get("last_correct", float("inf"))
        )
    )

    # Top 3 nikaalo (safe slicing)
    top_3 = sorted_users[:3]

    # ===============================
    # 🏆 MESSAGE BUILD
    # ===============================
    medals = ["🥇", "🥈", "🥉"]

    msg = "🏆 *Monthly Leaderboard Winners* 🏆\n\n"

    if not top_3:
        msg += "Koi participant nahi tha iss month 😅"
    else:
        for i, user in enumerate(top_3):
            name = user.get("name", "Unknown")
            points = user.get("points", 0)

            msg += f"{medals[i]} {name} — {points} pts\n"

    msg += "\n🔥 Leaderboard reset ho raha hai!\nNew month, new battle 🚀"

    # ===============================
    # 📤 SEND MESSAGE
    # ===============================
    for gid in GROUP_IDS:
        try:
            await context.bot.send_message(
                chat_id=gid,
                text=msg,
                parse_mode="Markdown"
            )
        except Exception as e:
            print(f"Error sending monthly msg: {e}")

    # ===============================
    # 🔄 RESET LEADERBOARD
    # ===============================
    for uid in users:
        users[uid]["points"] = 0
        users[uid]["last_correct"] = float("inf")
        users[uid]["streak"] = 0  # optional reset

    save_users(users)