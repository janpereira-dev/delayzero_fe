import streamlit as st


def render_recommendations(items):
    if not items:
        st.info("No hay recomendaciones todavía.")
        return

    for item in items:
        with st.container(border=True):
            st.subheader(item.get("title", "Recomendación"))
            st.write(item.get("summary", ""))
            col1, col2 = st.columns(2)
            with col1:
                st.caption(f"⏱ {item.get('duration', 'N/D')}")
            with col2:
                st.caption(f"⭐ {item.get('score', 'N/D')}")
