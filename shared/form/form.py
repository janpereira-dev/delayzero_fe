from datetime import date
import streamlit as st


def render_route_form():
    with st.form("route_form"):
        origin = st.text_input("Origen", value="")
        destination = st.text_input("Destino", value="")
        travel_range = st.date_input(
            "Rango de fechas",
            value=(date.today(), date.today()),
            format="DD/MM/YYYY",
        )
        submitted = st.form_submit_button("Recomendar ruta")

    departure_date = None
    return_date = None
    if isinstance(travel_range, tuple) and len(travel_range) == 2:
        departure_date, return_date = travel_range

    return {
        "origin": origin,
        "destination": destination,
        "departure_date": departure_date,
        "return_date": return_date,
        "submitted": submitted,
    }
