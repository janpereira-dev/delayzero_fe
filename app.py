import streamlit as st

from pages.home.page import render as render_home
from shared.style.theme import apply_app_style


def main():
    st.set_page_config(
        page_title="DelayZero",
        page_icon="🗺️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    apply_app_style()

    render_home()


if __name__ == "__main__":
    main()
