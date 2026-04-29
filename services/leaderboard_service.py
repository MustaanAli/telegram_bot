import json
import os
from datetime import datetime

USERS_FILE = "data/users.json"
HISTORY_FILE = "data/history.json"


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
# 📊 SAVE DAILY SNAPSHOT
# ===============================
def save_daily_leaderboard():

    users = load_json(USERS_FILE, {})
    history = load_json(HISTORY_FILE, [])

    today = datetime.now().strftime("%Y-%m-%d")

    # prevent duplicate save same day
    for entry in history:
        if entry["date"] == today:
            return

    # convert dict → list
    user_list = list(users.values())

    history.append({
        "date": today,
        "users": user_list
    })

    save_json(HISTORY_FILE, history)