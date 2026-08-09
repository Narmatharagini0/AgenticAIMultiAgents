import requests
from langchain.tools import tool

from config import WEATHER_API_KEY


@tool
def weather(city: str) -> str:
    """
    Get the current weather information for a given city
    using WeatherAPI.com.
    """

    if not WEATHER_API_KEY:
        return "Weather API key is not configured."

    try:
        response = requests.get(
            "https://api.weatherapi.com/v1/current.json",
            params={
                "key": WEATHER_API_KEY,
                "q": city,
                "aqi": "no"
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        location = data["location"]
        current = data["current"]

        return (
            f"Weather in {location['name']}, {location['country']}:\n"
            f"Temperature: {current['temp_c']}°C\n"
            f"Feels like: {current['feelslike_c']}°C\n"
            f"Condition: {current['condition']['text']}\n"
            f"Humidity: {current['humidity']}%\n"
            f"Wind: {current['wind_kph']} km/h\n"
            f"Wind Direction: {current['wind_dir']}\n"
            f"Local Time: {location['localtime']}"
        )

    except requests.exceptions.HTTPError:
        return "Unable to retrieve weather information. Please check the city name or API key."

    except Exception as e:
        return f"Weather service error: {str(e)}"