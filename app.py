import streamlit as st
import plotly.express as px  # type: ignore[import]
from exoplanet_data import fetch_exoplanet_data, filter_exoplanets

st.set_page_config(page_title="Exoplanet Explorer", layout="wide")


@st.cache_data(ttl=3600)
def load_data():
    df = fetch_exoplanet_data()
    return df


st.title("Exoplanet Explorer")
st.markdown(
    """
Aplikacja prezentuje interaktywną mapę znanych egzoplanet.
Dane pochodzą z [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/).
"""
)

df = load_data()

st.sidebar.header("Filtry")
min_mass = st.sidebar.slider(
    "Minimalna masa [M_⊕]", 0.0, float(df["pl_bmasse"].max()), 0.0, step=0.1
)
max_mass = st.sidebar.slider(
    "Maksymalna masa [M_⊕]",
    0.0,
    float(df["pl_bmasse"].max()),
    float(df["pl_bmasse"].max()),
    step=0.1,
)
min_radius = st.sidebar.slider(
    "Minimalny promień [R_⊕]", 0.0, float(df["pl_rade"].max()), 0.0, step=0.1
)
max_radius = st.sidebar.slider(
    "Maksymalny promień [R_⊕]",
    0.0,
    float(df["pl_rade"].max()),
    float(df["pl_rade"].max()),
    step=0.1,
)
start_year = st.sidebar.number_input(
    "Rok odkrycia od:",
    min_value=int(df["disc_year"].min()),
    max_value=int(df["disc_year"].max()),
    value=int(df["disc_year"].min()),
)
end_year = st.sidebar.number_input(
    "Rok odkrycia do:",
    min_value=int(df["disc_year"].min()),
    max_value=int(df["disc_year"].max()),
    value=int(df["disc_year"].max()),
)

filtered_df = filter_exoplanets(
    df, min_mass, max_mass, min_radius, max_radius, start_year, end_year
)

st.markdown(f"**Liczba planet po filtracji:** {len(filtered_df)}")

fig = px.scatter(
    filtered_df,
    x="ra",
    y="dec",
    color="disc_year",
    hover_data=["pl_name", "hostname", "pl_bmasse", "pl_rade", "disc_year"],
    title="Mapa egzoplanet (RA vs DEC)",
)
fig.update_layout(height=700)
st.plotly_chart(fig, use_container_width=True)
