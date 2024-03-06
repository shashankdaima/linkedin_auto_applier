import os
from dotenv import load_dotenv

load_dotenv()
CRACKED_DEV_API_KEY = os.environ.get("CRACKED_DEV_API_KEY")
CRACKED_DEV_CREDS=[os.environ.get("CRACKED_DEV_EMAIL"),os.environ.get("CRACKED_DEV_PASSWORD")]