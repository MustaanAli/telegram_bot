from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime

from config import MUSTAAN_ID, TIMEZONE, GROUP_IDS


# ===============================
# 🧪 DEBUG ID
# ===============================
async def debug_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    chat = update.effective_chat
    await update.message.reply_text(
        f"Chat ID: {chat.id}\nType: {chat.type}"
    )


# ===============================
# 📅 SCHEDULE MESSAGE (PRIVATE ONLY)
# ===============================
async def schedule_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    # ❗ ONLY PRIVATE
    if update.effective_chat.type != "private":
        return

    # ❗ ONLY ADMIN
    if update.effective_user.id != MUSTAAN_ID:
        await update.message.reply_text("❌ Only admin allowed")
        return

    try:
        args = context.args

        if len(args) < 3:
            await update.message.reply_text(
                "❌ Format:\n/schedule YYYY-MM-DD HH:MM message"
            )
            return

        date_str = args[0]
        time_str = args[1]
        message = " ".join(args[2:]).strip()

        dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        dt = TIMEZONE.localize(dt)

        now = datetime.now(TIMEZONE)
        delay = (dt - now).total_seconds()

        if delay <= 0:
            await update.message.reply_text("❌ Future time daalo bhai")
            return

        # 🔥 IMPORTANT: NAME ADD KRNA HAI
        context.job_queue.run_once(
            send_scheduled_message,
            when=delay,
            data={"message": message},
            name="user_schedule"   # 👈 ye key hai cancel ke liye
        )

        await update.message.reply_text(
            f"✅ Scheduled for {dt.strftime('%d-%m %H:%M')}"
        )

    except ValueError:
        await update.message.reply_text(
            "❌ Date format galat hai!\nUse:\nYYYY-MM-DD HH:MM"
        )

    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")


# ===============================
# ❌ CANCEL ALL SCHEDULED
# ===============================
async def cancel_all(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    # only private
    if update.effective_chat.type != "private":
        return

    # only admin
    if update.effective_user.id != MUSTAAN_ID:
        await update.message.reply_text("❌ Only admin allowed")
        return

    args = context.args

    if not args or args[0].lower() != "all":
        await update.message.reply_text("❌ Use: /cancel all")
        return

    job_queue = context.application.job_queue   # 🔥 IMPORTANT CHANGE

    jobs = job_queue.jobs()

    if not jobs:
        await update.message.reply_text("⚠️ Koi scheduled message nahi mila")
        return

    count = 0

    for job in jobs:
        if job.name == "user_schedule":
            job.schedule_removal()
            count += 1

    if count == 0:
        await update.message.reply_text("⚠️ Koi scheduled message nahi mila")
        return

    await update.message.reply_text(
        f"🧹 {count} scheduled messages cancel ho gaye ✅"
    )


# ===============================
# 📤 SEND SCHEDULED MESSAGE
# ===============================
async def send_scheduled_message(context: ContextTypes.DEFAULT_TYPE):

    msg = context.job.data.get("message", "")

    for gid in GROUP_IDS:
        try:
            await context.bot.send_message(chat_id=gid, text=msg)
        except Exception as e:
            print(f"Error sending to {gid}: {e}")