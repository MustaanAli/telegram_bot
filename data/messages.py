import random
from config import GROUP_IDS

# ===============================
# 🌞 GOOD MORNING MESSAGES
# ===============================

GOOD_MORNING_MESSAGES = [
    "🌞 Good Morning Traders! Let's crush the market today! 🚀",
    "⚡ Good Morning! Wake up and chase your dreams like you chase the trendline!",
    "📈 Good Morning! New day, new opportunity. Let’s trade smart!",
    "🌅 Good Morning! Let the charts guide you to success!",
    "💹 Good Morning! Another day to hustle and grow your portfolio!",
    "🔥 Good Morning! Light up the market with your discipline!",
    "💰 Good Morning! Profits don’t sleep, so let’s get started!",
    "🚀 Good Morning! Blast off into a profitable day!",
    "🎯 Good Morning! Aim high and hold your targets steady!",
    "💪 Good Morning! Discipline + Strategy = Success!",
    "📊 Good Morning! Let the candles tell you their story!",
    "🌄 Good Morning! Rise early, trade wisely!",
    "👨‍💻 Good Morning! Another day to be a chart wizard!",
    "⚖️ Good Morning! Balance your emotions before your trades!",
    "🌻 Good Morning! Plant your trades, grow your gains!",
    "🚦 Good Morning! Green signals ahead, let’s ride them!",
    "📘 Good Morning! Journal your trades, master your mindset!",
    "🔍 Good Morning! Observe, analyze, then strike!",
    "🏆 Good Morning! Every morning is a new chance at winning!",
    "🧠 Good Morning! Smart traders wake up early!",
    "🎉 Good Morning! Let's celebrate discipline today!",
    "☕ Good Morning! Sip your coffee and scan the charts!",
    "🎓 Good Morning! Learn, trade, repeat!",
    "🧘‍♂️ Good Morning! Stay calm and chart on!",
    "🔋 Good Morning! Recharge, then execute your plan!",
    "📅 Good Morning! A new candle has begun—own it!",
    "💼 Good Morning! It's time to handle your trades like a boss!",
    "🧭 Good Morning! Stay on course, follow your trading plan!",
    "🎢 Good Morning! Ride the market waves, don’t fear them!",
    "🛡️ Good Morning! Protect your capital, respect your SL!",
]

# ===============================
# 😔 MOOD MESSAGES
# ===============================

MOOD_MESSAGES = [
    "Aaj mann udaas lag raha hai... 😔",
    "Dil thoda heavy sa hai aaj... 💭",
    "Kuch khaali khaali sa lag raha hai... 🌧️",
    "Thoda low feel ho raha hai... 😕",
    "Lagta hai aaj sab kuch slow chal raha hai... 🐌",
    "Kisi ne yaad nahi kiya aaj... 😞",
    "Bas yunhi chup rehne ka mann kar raha hai... 🤐",
    "Aaj dil thoda thak gaya hai... 🥀",
    "Kabhi kabhi bina wajah bhi udaasi ghira leti hai... 💧",
    "Dil bhar aaya... kuch samajh nahi aa raha... 😢",
    "Har waqt hasi nahi hoti na... 😶",
    "Aaj apno ki yaad zyada aa rahi hai... 🫂",
    "Bas aise hi... udaas sa... 😔",
    "Man nahi lag raha... pata nahi kyun... 😔",
    "Kya sab kuch sahi ho jayega? 💔",
    "Dil me ek halka sa bojh mehsoos ho raha hai... 🪨",
    "Kisi ka sath chahiye... 😟",
    "Udaasi bhi ajeeb hoti hai... 🕳️",
    "Aaj dil kaafi sensitive ho gaya hai... 💓",
    "Kabhi kabhi bas kisi ki ek muskurahat chahiye hoti hai... 😊",
]

# ===============================
# 😄 CHEER UP MESSAGES
# ===============================

CHEERUP_MESSAGES = [
    "Ab thik ho gaya, Mustaan bhai ne thik kar diya ❤️",
    "System restart complete — mood optimized 😎",
    "Motivation received successfully 🚀",
    "Patch deployed successfully 😄",
    "Mood upgrade complete 😁",
    "Positive vibes delivered ✨",
    "Smile restored successfully 😄",
    "System status: Happy & Motivated 😄",
    "Recharged with positive vibes 🔋",
    "Now everything feels better ❤️",
]

# ===============================
# 🔥 FUNCTIONS
# ===============================

async def send_good_morning(context):
    msg = random.choice(GOOD_MORNING_MESSAGES)

    for gid in GROUP_IDS:
        await context.bot.send_message(chat_id=gid, text=msg)


async def send_mood_message(context):
    msg = random.choice(MOOD_MESSAGES)

    for gid in GROUP_IDS:
        await context.bot.send_message(chat_id=gid, text=msg)


async def send_cheer_message(context):
    msg = random.choice(CHEERUP_MESSAGES)

    for gid in GROUP_IDS:
        await context.bot.send_message(chat_id=gid, text=msg)