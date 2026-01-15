import streamlit as st


def render_map(route_points):
    if not route_points:
        st.info("No hay datos de mapa para mostrar.")
        return

    st.map(route_points)
