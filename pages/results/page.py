import streamlit as st

from shared.map.map import render_map
from shared.recommendations.recommendations import render_recommendations


def render():
    st.header("Results")
    analysis = st.session_state.get("analysis")

    if not analysis:
        st.warning("No hay resultados aún. Completa el formulario en Home.")
        return

    st.subheader("Ruta sugerida")
    render_map(analysis.get("route_points", []))

    st.subheader("Recomendaciones")
    render_recommendations(analysis.get("recommendations", []))
