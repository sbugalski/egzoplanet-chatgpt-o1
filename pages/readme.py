import streamlit as st

st.set_page_config(page_title="Informacje o aplikacji")

st.title("O aplikacji Exoplanet Explorer")
st.markdown(
    """
Aplikacja **Exoplanet Explorer** wizualizuje informacje o odkrytych egzoplanetach.
Dane są pobierane z NASA Exoplanet Archive i prezentowane w formie interaktywnej mapy (RA vs DEC) z możliwością filtrowania po różnych parametrach takich jak:
- Masa planety (w masach Ziemi)
- Promień planety (w promieniach Ziemi)
- Rok odkrycia

Dodatkowo możesz sortować i wybierać interesujące Cię zakresy wartości, aby zawęzić liczbę wyświetlanych planet.

Dzięki temu narzędziu można szybko uzyskać wgląd w charakterystyki znanych egzoplanet oraz sprawdzić ich rozmieszczenie na sferze niebieskiej.

Aplikacja została całkowicie stworzona przy użyciu ChatGPT o1.
"""
)
