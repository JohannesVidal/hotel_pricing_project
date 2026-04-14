import requests
import pandas as pd

from src.config import OPENWEATHER_API_KEY, is_non_empty


def get_current_weather(city: str, country_code: str = "") -> dict:
    """
    Fetch current weather for a city using OpenWeather.
    Returns a normalized dictionary.
    """
    if not is_non_empty(OPENWEATHER_API_KEY):
        raise ValueError("OPENWEATHER_API_KEY is empty or missing in .env")

    query = city if not country_code else f"{city},{country_code}"

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": query,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    return {
        "city": data.get("name"),
        "country_code": data.get("sys", {}).get("country"),
        "temp": data.get("main", {}).get("temp"),
        "temp_min": data.get("main", {}).get("temp_min"),
        "temp_max": data.get("main", {}).get("temp_max"),
        "humidity": data.get("main", {}).get("humidity"),
        "pressure": data.get("main", {}).get("pressure"),
        "weather_main": data.get("weather", [{}])[0].get("main"),
        "weather_description": data.get("weather", [{}])[0].get("description"),
        "wind_speed": data.get("wind", {}).get("speed"),
        "clouds_pct": data.get("clouds", {}).get("all"),
        "data_source": "openweather"
    }


def weather_dict_to_df(weather_dict: dict) -> pd.DataFrame:
    """
    Convert one normalized weather dictionary into a one-row DataFrame.
    """
    return pd.DataFrame([weather_dict])