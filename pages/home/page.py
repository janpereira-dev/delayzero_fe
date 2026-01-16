import streamlit as st

from shared.form.form import render_route_form
from shared.api.client import fetch_route_analysis


def apply_clean_home_layout():
    st.markdown(
        """
        <style>
        section[data-testid="stSidebar"] {
            display: none !important;
        }

        div[data-testid="collapsedControl"] {
            display: none !important;
        }

        [data-testid="stHeaderActionElements"] {
            display: none !important;
        }

        [data-testid="stHeader"] {
            display: none !important;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render():
    apply_clean_home_layout()

    st.header("DelayZero")
    st.write("Planifica tu ruta y revisa las recomendaciones.")

    with st.container(border=True):
        form_data = render_route_form()

    if form_data["submitted"]:
        with st.spinner("Analizando ruta..."):
            analysis = fetch_route_analysis(
                origin=form_data["origin"],
                destination=form_data["destination"],
                departure_date=form_data["departure_date"],
                return_date=form_data["return_date"],
            )

        st.session_state["analysis"] = analysis
        st.success("Resultados listos. Redirigiendo a resultados...")
        st.switch_page("pages/resultados.py")
