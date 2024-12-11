# exoplanet_data.py

import requests
import pandas as pd
from io import StringIO
import json
import os
import time

EXOPLANET_DATA_URL = (
    "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query="
    "select+pl_name,hostname,ra,dec,pl_rade,pl_bmasse,disc_year,pl_refname+from+ps&format=csv"
)

CACHE_FILE = "exoplanet_cache.json"
CACHE_TTL = 3600  # czas w sekundach, np. 3600 = 1 godzina


def fetch_exoplanet_data(url: str = EXOPLANET_DATA_URL) -> pd.DataFrame:
    """
    Pobiera dane o egzoplanetach z zewnętrznego źródła lub cache.

    Args:
        url (str): URL do pobrania danych CSV.

    Returns:
        pd.DataFrame: DataFrame z danymi egzoplanet.
    """
    # Sprawdź, czy istnieje cache i czy nie jest przeterminowany
    if os.path.exists(CACHE_FILE):
        mod_time = os.path.getmtime(CACHE_FILE)
        if time.time() - mod_time < CACHE_TTL:
            # Wczytaj dane z pliku cache
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            df = pd.DataFrame(data)
            return df

    # Jeśli brak ważnego cache, pobierz dane z sieci
    response = requests.get(url)
    response.raise_for_status()
    df = pd.read_csv(StringIO(response.text))

    # Zapisz dane do pliku JSON (cache)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(df.to_dict(orient="records"), f, ensure_ascii=False)

    return df


def filter_exoplanets(
    df: pd.DataFrame,
    min_mass: float = None,
    max_mass: float = None,
    min_radius: float = None,
    max_radius: float = None,
    start_year: int = None,
    end_year: int = None,
) -> pd.DataFrame:
    """
    Filtruje egzoplanety na podstawie podanych kryteriów.

    Args:
        df (pd.DataFrame): DataFrame z danymi egzoplanet.
        min_mass (float, optional): Minimalna masa planety w masach Ziemi.
        max_mass (float, optional): Maksymalna masa planety w masach Ziemi.
        min_radius (float, optional): Minimalny promień planety w promieniach Ziemi.
        max_radius (float, optional): Maksymalny promień planety w promieniach Ziemi.
        start_year (int, optional): Rok odkrycia od.
        end_year (int, optional): Rok odkrycia do.

    Returns:
        pd.DataFrame: Przefiltrowany DataFrame z egzoplanetami.
    """
    filtered = df.copy()

    if min_mass is not None:
        filtered = filtered[filtered["pl_bmasse"] >= min_mass]

    if max_mass is not None:
        filtered = filtered[filtered["pl_bmasse"] <= max_mass]

    if min_radius is not None:
        filtered = filtered[filtered["pl_rade"] >= min_radius]

    if max_radius is not None:
        filtered = filtered[filtered["pl_rade"] <= max_radius]

    if start_year is not None:
        filtered = filtered[filtered["disc_year"] >= start_year]

    if end_year is not None:
        filtered = filtered[filtered["disc_year"] <= end_year]

    return filtered
