import streamlit as st

from shared.form.form import render_route_form
from shared.map.map import render_map
from shared.recommendations.recommendations import render_recommendations
from shared.api.client import fetch_route_analysis


def render():
    st.header("DelayZero")
    st.write("Planifica tu ruta y revisa las recomendaciones.")

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
        st.success("Resultados listos. Ve a la pestaña Results para ver el detalle.")

    analysis = st.session_state.get("analysis")
    if analysis:
        st.subheader("Vista rápida")
        render_map(analysis.get("route_points", []))
        render_recommendations(analysis.get("recommendations", []))
