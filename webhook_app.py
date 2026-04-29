import asyncio
from flask import Flask, request

from telegram import Update
from main import build_app

app = Flask(__name__)

telegram_app = build_app()


# ===============================
# TELEGRAM WEBHOOK ROUTE
# ===============================
@app.route('/webhook', methods=['POST'])
def webhook():

    update = Update.de_json(request.get_json(force=True), telegram_app.bot)

    asyncio.run(telegram_app.process_update(update))

    return "ok"


# ===============================
# RUN SERVER
# ===============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)