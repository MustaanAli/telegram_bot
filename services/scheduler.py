from datetime import time

from services.quiz import send_quiz_poll
from services.mood import monthly_mood_check
from services.roast import random_roast
from services.birthday import check_birthdays
from data.messages import send_good_morning
from services.monthly import monthly_winner

from config import TIMEZONE


# ===============================
# ⏰ SETUP ALL JOBS
# ===============================
def setup_jobs(app):

    job_queue = app.job_queue   # ✅ IMPORTANT

    # ===============================
    # 🌞 DAILY JOBS
    # ===============================
    job_queue.run_daily(
        send_good_morning,
        time=time(hour=8, minute=0, tzinfo=TIMEZONE)
    )

    job_queue.run_daily(
        send_quiz_poll,
        time=time(hour=20, minute=0, tzinfo=TIMEZONE)
    )

    job_queue.run_daily(
        check_birthdays,
        time=time(hour=0, minute=0, tzinfo=TIMEZONE)
    )

    # ===============================
    # 🏆 MONTHLY WINNER (28th)
    # ===============================
    job_queue.run_daily(
        monthly_winner,
        time=time(hour=23, minute=0, tzinfo=TIMEZONE),
        name="monthly_winner"
    )

    # ===============================
    # 🔁 REPEATING JOBS
    # ===============================
    job_queue.run_repeating(
        monthly_mood_check,
        interval=43200,   # 12 hours
        first=20
    )

    job_queue.run_repeating(
        random_roast,
        interval=28800,   # 8 hours
        first=30
    )