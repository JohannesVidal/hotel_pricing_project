import requests
from src.config import GEOAPIFY_API_KEY

BASE_URL = "https://api.geoapify.com/v2/places"


def get_tourism_pois(lat, lon, radius=500, limit=20):
    params = {
        "categories": "tourism.sights,tourism.attraction,heritage",
        "filter": f"circle:{lon},{lat},{radius}",
        "limit": limit,
        "apiKey": GEOAPIFY_API_KEY
    }

    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json()