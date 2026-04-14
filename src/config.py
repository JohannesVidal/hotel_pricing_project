import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "").strip()
TICKETMASTER_API_KEY = os.getenv("TICKETMASTER_API_KEY", "").strip()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "").strip()


GOOGLE_HOTEL_RAPIDAPI_HOST = os.getenv("GOOGLE_HOTEL_RAPIDAPI_HOST", "").strip()

def is_non_empty(value: str) -> bool:
    return bool(value and value.strip())