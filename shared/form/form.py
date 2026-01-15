from datetime import date
import streamlit as st


def render_route_form():
    with st.form("route_form"):
        origin = st.text_input("Origen", value="")
        destination = st.text_input("Destino", value="")
        travel_date = st.date_input("Fecha", value=date.today())
        submitted = st.form_submit_button("Recomendar ruta")

    return {
        "origin": origin,
        "destination": destination,
        "date": travel_date,
        "submitted": submitted,
    }
