import json
import os
from datetime import date

import requests
import streamlit as st

DEFAULT_TIMEOUT = 15
DEFAULT_MOCK_PATH = "data/mock_response.json"


def get_api_base_url():
    return st.secrets.get("API_BASE_URL", os.getenv("API_BASE_URL", "")).rstrip("/")


def use_mock():
    value = st.secrets.get("USE_MOCK", os.getenv("USE_MOCK", "true"))
    return str(value).lower() in {"1", "true", "yes", "y"}


def load_mock_from_file():
    path = st.secrets.get(
        "MOCK_DATA_PATH", os.getenv("MOCK_DATA_PATH", DEFAULT_MOCK_PATH)
    )
    if not path or not os.path.exists(path):
        return None

    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError):
        return None


@st.cache_data(show_spinner=False)
def call_api(path, params=None):
    base_url = get_api_base_url()
    if not base_url:
        return None

    url = f"{base_url}/{path.lstrip('/')}"
    response = requests.get(url, params=params, timeout=DEFAULT_TIMEOUT)
    response.raise_for_status()
    return response.json()


def fetch_route_analysis(origin, destination, travel_date: date):
    _ = (origin, destination, travel_date)

    if not use_mock():
        payload = {
            "origin": origin,
            "destination": destination,
            "date": travel_date.isoformat(),
        }
        data = call_api("routes/analyze", params=payload)
        if data:
            return data

    file_data = load_mock_from_file()
    if file_data:
        return file_data

    return {
        "route_points": [
            {"lat": 40.4168, "lon": -3.7038},
            {"lat": 40.9630, "lon": -1.1600},
            {"lat": 41.3874, "lon": 2.1686},
        ],
        "recommendations": [
            {
                "title": "Tren Alta Velocidad",
                "summary": "La opción más rápida con menos demoras.",
                "duration": "2h 30m",
                "score": 9.8,
            },
            {
                "title": "Ruta Mixta (Bus + Tren)",
                "summary": "Alternativa económica con buen balance.",
                "duration": "3h 45m",
                "score": 8.5,
            },
            {
                "title": "Bus Directo",
                "summary": "Menor costo, duración más extensa.",
                "duration": "5h 20m",
                "score": 7.6,
            },
            {
                "title": "Coche Compartido",
                "summary": "Flexible en horarios, sujeto a disponibilidad.",
                "duration": "4h 10m",
                "score": 7.9,
            },
        ],
    }
