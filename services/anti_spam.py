import random
from telegram import Update
from telegram.ext import ContextTypes

# ===============================
# 🔁 USER MENTION TRACKING
# ===============================
MENTION_COUNT = {}

# ===============================
# 😂 ANTI-SPAM MESSAGES
# ===============================
ANTI_SPAM_MESSAGES = [
    "Arey bhai 😭 main is kaam ke liye nahi bana hu...\nThoda time dijiye, Mustaan bhaiya dekh rahe hain 👀",
    "Arre arre itna mat bulao mujhe 😭\nMain abhi training phase me hoon bhai...",
    "Bhai system overload ho raha hai 😵\nThoda shaanti rakho...",
    "Main abhi beta version hoon bhai 😭\nThoda patience rakho...",
    "AI hoon bhai, call center nahi 😂 ek ek karke bolo",
    "Bot bhi emotional ho jata hai bhai 😭",
    "Error 404: Human Conversation Not Found 😂",
    "CPU ghoom raha hai fan ki tarah 🌀 thoda shaanti rakho",
    "Main reply likh raha tha… par thought hi bhool gaya 🤯",
    "AI hoon bhai, magician nahi 🎩",
    "Abhi system meditation pe hai 🧘‍♂️ disturb mat karo",
    "Arey bhai ruk jao 😭 mera RAM full ho gaya hai…",
    "Bot ko bhi anxiety ho rahi hai itna mention se 😵",
    "Human personality update abhi pending hai 😂",
    "Server pe chai gir gayi hai ☕💻 thoda time lagega..."
]

# ===============================
# 🛡️ ANTI-SPAM FUNCTION
# ===============================
async def anti_spam_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message or not update.message.text:
        return False

    user_id = update.effective_user.id
    text = update.message.text.lower()

    # Trigger only when "bot" mentioned
    if "bot" in text:

        MENTION_COUNT[user_id] = MENTION_COUNT.get(user_id, 0) + 1

        # Limit reached
        if MENTION_COUNT[user_id] >= 5:
            MENTION_COUNT[user_id] = 0

            await update.message.reply_text(
                random.choice(ANTI_SPAM_MESSAGES)
            )

            return True

    return False