import streamlit as st

from pages.results.page import render
from shared.style.theme import apply_app_style


st.set_page_config(
    page_title="DelayZero - Resultados",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_app_style()

render()
