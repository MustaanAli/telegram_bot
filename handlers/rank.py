from telegram import Update
from telegram.ext import ContextTypes
import json
import os

USERS_FILE = "data/users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


# ===============================
# 📊 USER RANK COMMAND
# ===============================
async def rank(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = str(update.effective_user.id)

    users = load_users()

    if not users:
        await update.message.reply_text("⚠️ Abhi data nahi hai bhai 😅")
        return

    # sort leaderboard
    sorted_users = sorted(
        users.items(),
        key=lambda x: (
            -x[1].get("points", 0),
            x[1].get("last_correct", float("inf"))
        )
    )

    # find user rank
    rank_position = None
    for i, (uid, data) in enumerate(sorted_users, start=1):
        if uid == user_id:
            rank_position = i
            user_data = data
            break

    if rank_position is None:
        await update.message.reply_text("❌ Tumne abhi tak quiz attempt nahi kiya")
        return

    total_users = len(sorted_users)

    name = user_data.get("name", "Unknown")
    points = user_data.get("points", 0)
    streak = user_data.get("streak", 0)

    msg = (
        f"📊 *Your Stats*\n\n"
        f"👤 Name: {name}\n"
        f"🏆 Rank: #{rank_position} / {total_users}\n"
        f"💰 Points: {points}\n"
        f"🔥 Streak: {streak} days\n\n"
        "🚀 Keep going bhai!"
    )

    await update.message.reply_text(msg, parse_mode="Markdown")