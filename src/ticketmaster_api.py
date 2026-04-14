import requests
import pandas as pd

from src.config import TICKETMASTER_API_KEY, is_non_empty


def get_events(city: str, country_code: str = "ES", keyword: str | None = None, size: int = 20) -> list[dict]:
    """
    Fetch events from Ticketmaster Discovery API.
    Returns the raw list of event dictionaries.
    """
    if not is_non_empty(TICKETMASTER_API_KEY):
        raise ValueError("TICKETMASTER_API_KEY is empty or missing in .env")

    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        "apikey": TICKETMASTER_API_KEY,
        "city": city,
        "countryCode": country_code,
        "size": size
    }

    if keyword:
        params["keyword"] = keyword

    response = requests.get(url, params=params, timeout=30)

    if response.status_code == 401:
        raise ValueError("Ticketmaster authentication failed. Check your API key.")

    response.raise_for_status()

    data = response.json()
    return data.get("_embedded", {}).get("events", [])


def normalize_events(events: list[dict]) -> pd.DataFrame:
    """
    Normalize raw Ticketmaster events into a clean DataFrame.
    """
    rows = []

    for event in events:
        venue = {}
        venues = event.get("_embedded", {}).get("venues", [])
        if venues:
            venue = venues[0]

        classifications = event.get("classifications", [])
        classification = classifications[0] if classifications else {}

        rows.append({
            "event_id": event.get("id"),
            "event_name": event.get("name"),
            "event_type": event.get("type"),
            "event_url": event.get("url"),
            "city": venue.get("city", {}).get("name"),
            "country_code": venue.get("country", {}).get("countryCode"),
            "venue_name": venue.get("name"),
            "venue_latitude": venue.get("location", {}).get("latitude"),
            "venue_longitude": venue.get("location", {}).get("longitude"),
            "event_date": event.get("dates", {}).get("start", {}).get("localDate"),
            "event_time": event.get("dates", {}).get("start", {}).get("localTime"),
            "segment": classification.get("segment", {}).get("name"),
            "genre": classification.get("genre", {}).get("name"),
            "subgenre": classification.get("subGenre", {}).get("name"),
            "min_price": (
                event.get("priceRanges", [{}])[0].get("min")
                if event.get("priceRanges") else None
            ),
            "max_price": (
                event.get("priceRanges", [{}])[0].get("max")
                if event.get("priceRanges") else None
            ),
            "currency": (
                event.get("priceRanges", [{}])[0].get("currency")
                if event.get("priceRanges") else None
            ),
            "data_source": "ticketmaster"
        })

    return pd.DataFrame(rows)