import os
from dotenv import load_dotenv
import pytz

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
MUSTAAN_ID = int(os.getenv("MUSTAAN_ID"))
AMAN_SIR_ID = int(os.getenv("AMAN_SIR_ID"))

TIMEZONE = pytz.timezone("Asia/Kolkata")

GROUP_IDS = [-1001814915121, -1003768400404]