import logging

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ChatMemberHandler,
    PollAnswerHandler,
    ContextTypes
)

from handlers.start import start
from handlers.text_handler import handle_text
from handlers.admin import schedule_message, debug_id, cancel_all
from handlers.chat_member import bot_added
from handlers.leaderboard import leaderboard
from handlers.rank import rank

from services.quiz import handle_poll_answer
from services.scheduler import setup_jobs
from config import TOKEN


# ===============================
# 📝 LOGGING SETUP
# ===============================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


# ===============================
# ❗ GLOBAL ERROR HANDLER
# ===============================
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(msg="Exception while handling update:", exc_info=context.error)


# ===============================
# 🚀 BUILD APP (IMPORTANT)
# ===============================
def build_app():

    app = ApplicationBuilder().token(TOKEN).build()

    # ===============================
    # 🎯 COMMAND HANDLERS
    # ===============================
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("id", debug_id))
    app.add_handler(CommandHandler("schedule", schedule_message))
    app.add_handler(CommandHandler("leaderboard", leaderboard))
    app.add_handler(CommandHandler("rank", rank))
    app.add_handler(CommandHandler("cancel", cancel_all))

    # ===============================
    # 💬 MESSAGE HANDLER
    # ===============================
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text)
    )

    # ===============================
    # 🤖 BOT EVENTS
    # ===============================
    app.add_handler(
        ChatMemberHandler(bot_added, ChatMemberHandler.MY_CHAT_MEMBER)
    )

    # ===============================
    # 📊 QUIZ ANSWERS HANDLER
    # ===============================
    app.add_handler(PollAnswerHandler(handle_poll_answer))

    # ===============================
    # ⏰ JOBS
    # ===============================
    setup_jobs(app)

    # ===============================
    # ❗ ERROR HANDLER
    # ===============================
    app.add_error_handler(error_handler)

    return app


# ===============================
# ▶️ LOCAL TEST (OPTIONAL)
# ===============================
def main():
    app = build_app()

    logger.info("🚀 Bot started in polling mode (TEST)...")
    app.run_polling()


# ===============================
# ▶️ ENTRY POINT
# ===============================
if __name__ == "__main__":
    main()