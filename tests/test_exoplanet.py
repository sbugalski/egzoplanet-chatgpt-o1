# tests/test_exoplanet_data.py

import pytest
import pandas as pd
from unittest.mock import patch
from exoplanet_data import fetch_exoplanet_data, filter_exoplanets
import requests

TEST_CSV = """pl_name,hostname,ra,dec,pl_rade,pl_bmasse,disc_year,pl_refname
PlanetA,HostA,10.0,-5.0,1.1,2.0,2010,RefA
PlanetB,HostB,20.0,-10.0,2.0,10.0,2015,RefB
PlanetC,HostC,30.0,5.0,0.5,0.8,2020,RefC
"""


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "pl_name": ["PlanetA", "PlanetB", "PlanetC"],
            "pl_bmasse": [2.0, 10.0, 0.8],
            "pl_rade": [1.1, 2.0, 0.5],
            "disc_year": [2010, 2015, 2020],
        }
    )


@patch("exoplanet_data.requests.get")
def test_fetch_exoplanet_data(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = TEST_CSV
    mock_get.return_value.raise_for_status = lambda: None

    df = fetch_exoplanet_data("http://dummy_url")
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert set(df["pl_name"]) == {"PlanetA", "PlanetB", "PlanetC"}


@patch("exoplanet_data.requests.get")
@patch("exoplanet_data.os.path.exists")
@patch("exoplanet_data.os.path.getmtime")
@patch("exoplanet_data.time.time")
def test_fetch_exoplanet_data_cache_expired(
    mock_time, mock_getmtime, mock_exists, mock_get
):
    # Symuluj istnienie przeterminowanego cache
    mock_exists.return_value = True
    mock_time.return_value = 2000000
    mock_getmtime.return_value = 1000000  # CACHE_TTL = 3600, więc przeterminowany

    # Symuluj odpowiedź HTTP
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = TEST_CSV
    mock_get.return_value.raise_for_status = lambda: None

    df = fetch_exoplanet_data("http://dummy_url")
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert set(df["pl_name"]) == {"PlanetA", "PlanetB", "PlanetC"}


@patch("exoplanet_data.requests.get")
@patch("exoplanet_data.os.path.exists")
def test_fetch_exoplanet_data_http_error(mock_exists, mock_get):
    # Symuluj brak cache
    mock_exists.return_value = False

    # Symuluj odpowiedź HTTP z błędem
    mock_get.return_value.status_code = 404
    mock_get.return_value.raise_for_status.side_effect = requests.HTTPError("Not Found")

    with pytest.raises(requests.HTTPError):
        fetch_exoplanet_data("http://dummy_url")


def test_filter_exoplanets(sample_df):
    # Przykład filtrowania masy
    filtered = filter_exoplanets(sample_df, min_mass=1.0, max_mass=5.0)
    assert len(filtered) == 1
    assert filtered.iloc[0]["pl_name"] == "PlanetA"


def test_filter_exoplanets_no_filters(sample_df):
    # Bez filtrów, zwracane są wszystkie dane
    filtered = filter_exoplanets(sample_df)
    assert len(filtered) == 3


def test_filter_exoplanets_min_mass(sample_df):
    # Filtruj po minimalnej masie
    filtered = filter_exoplanets(sample_df, min_mass=1.0)
    assert len(filtered) == 2
    assert set(filtered["pl_name"]) == {"PlanetA", "PlanetB"}


def test_filter_exoplanets_max_mass(sample_df):
    # Filtruj po maksymalnej masie
    filtered = filter_exoplanets(sample_df, max_mass=2.0)
    assert len(filtered) == 2
    assert set(filtered["pl_name"]) == {"PlanetA", "PlanetC"}


def test_filter_exoplanets_mass_range(sample_df):
    # Filtruj po zakresie masy
    filtered = filter_exoplanets(sample_df, min_mass=1.0, max_mass=5.0)
    assert len(filtered) == 1
    assert filtered.iloc[0]["pl_name"] == "PlanetA"


def test_filter_exoplanets_year_range(sample_df):
    # Filtruj po zakresie lat odkrycia
    filtered = filter_exoplanets(sample_df, start_year=2012, end_year=2018)
    assert len(filtered) == 1
    assert filtered.iloc[0]["pl_name"] == "PlanetB"


def test_filter_exoplanets_combined_filters(sample_df):
    # Filtruj po kombinacji filtrów
    filtered = filter_exoplanets(
        sample_df, min_mass=1.0, max_mass=5.0, start_year=2000, end_year=2012
    )
    assert len(filtered) == 1
    assert filtered.iloc[0]["pl_name"] == "PlanetA"
