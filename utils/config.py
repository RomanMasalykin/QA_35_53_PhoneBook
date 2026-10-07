from os import getenv

from dotenv import load_dotenv

load_dotenv()

BASE_URL = getenv("BASE_URL")
EXISTING_EMAIL = getenv("EXITING_EMAIL")
EXISTING_USER_PASSWORD = getenv("EXITING_USER_PASSWORD")