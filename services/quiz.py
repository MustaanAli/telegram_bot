import random
import json
import os
import time

from telegram import Update
from telegram.ext import ContextTypes

from config import GROUP_IDS
from data.quiz_data import QUIZZES

# ===============================
# 📂 FILE PATHS
# ===============================
USERS_FILE = "data/users.json"
USED_QUIZ_FILE = "data/used_quiz.json"

LAST_QUIZ = {}
ANSWERED_USERS = set()


# ===============================
# 🧠 LOAD / SAVE
# ===============================
def load_json(file, default):
    if not os.path.exists(file):
        return default
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return default


def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)


# ===============================
# 📊 SEND QUIZ
# ===============================
async def send_quiz_poll(context: ContextTypes.DEFAULT_TYPE):

    global ANSWERED_USERS
    ANSWERED_USERS.clear()

    # ===============================
    # 🟢 PREVIOUS ANSWER
    # ===============================
    if "data" in LAST_QUIZ:
        prev = LAST_QUIZ["data"]

        correct = prev["options"][prev["correct"]]

        msg = (
            f"📊 *Kal ke quiz ka answer:*\n\n"
            f"✅ {correct}\n"
            f"📘 {prev['explanation']}"
        )

        for gid in GROUP_IDS:
            try:
                await context.bot.send_message(
                    chat_id=gid,
                    text=msg,
                    parse_mode="Markdown"
                )
            except Exception as e:
                print(f"Answer error: {e}")

    # ===============================
    # 🔵 UNIQUE QUIZ PICK
    # ===============================
    used_ids = load_json(USED_QUIZ_FILE, [])

    # Assign stable ID (IMPORTANT FIX)
    for i, q in enumerate(QUIZZES):
        if "id" not in q:
            q["id"] = i

    unused = [q for q in QUIZZES if q["id"] not in used_ids]

    if not unused:
        used_ids = []
        unused = QUIZZES

    quiz = random.choice(unused)

    used_ids.append(quiz["id"])
    save_json(USED_QUIZ_FILE, used_ids)

    LAST_QUIZ["data"] = quiz

    # ===============================
    # 🔵 SEND POLL
    # ===============================
    for gid in GROUP_IDS:
        try:
            await context.bot.send_poll(
                chat_id=gid,
                question=quiz["question"],
                options=quiz["options"],
                type="quiz",
                correct_option_id=quiz["correct"],
                explanation=quiz["explanation"],
                is_anonymous=False
            )
        except Exception as e:
            print(f"Quiz error: {e}")


# ===============================
# 🧠 HANDLE ANSWERS
# ===============================
async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if "data" not in LAST_QUIZ:
        return

    answer = update.poll_answer
    user = answer.user
    uid = str(user.id)

    # ❌ Prevent multiple scoring
    if uid in ANSWERED_USERS:
        return

    selected = answer.option_ids[0]
    correct = LAST_QUIZ["data"]["correct"]

    users = load_json(USERS_FILE, {})

    if uid not in users:
        users[uid] = {
            "name": user.first_name,
            "points": 0,
            "last_correct": float("inf")   # tie-break field
        }

    # ✅ Correct answer logic
    if selected == correct:
        users[uid]["points"] += 3

        # only set if first correct OR earlier than existing
        if users[uid]["last_correct"] == float("inf"):
            users[uid]["last_correct"] = time.time()

    # mark answered (anti-cheat)
    ANSWERED_USERS.add(uid)

    save_json(USERS_FILE, users)