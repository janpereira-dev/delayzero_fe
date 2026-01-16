import streamlit as st

from shared.map.map import render_map
from shared.recommendations.recommendations import render_recommendations


def apply_results_layout():
    st.markdown(
        """
        <style>
        section[data-testid="stMain"] .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
            height: 100vh;
        }

        [data-testid="stApp"] {
            position: relative;
        }

        [data-testid="stDeckGlJsonChart"] {
            position: fixed !important;
            inset: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            z-index: 0 !important;
        }

        [data-testid="stVerticalBlock"] {
            position: relative;
            z-index: 1;
        }

        .dz-panel {
            position: fixed;
            top: 0;
            left: 0;
            width: 30vw;
            max-width: 420px;
            height: 100vh;
            overflow-y: auto;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(8px);
            padding: 20px;
            z-index: 2;
            box-sizing: border-box;
        }

        .dz-panel h2,
        .dz-panel h3 {
            margin: 0 0 12px 0;
        }

        .dz-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 12px;
            padding: 12px;
            margin-bottom: 12px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
        }

        .dz-card-title {
            font-weight: 600;
            margin-bottom: 6px;
        }

        .dz-card-meta {
            display: flex;
            justify-content: space-between;
            color: #555;
            font-size: 0.9rem;
        }

        section[data-testid="stSidebar"] {
            display: none !important;
        }

        div[data-testid="collapsedControl"] {
            display: none !important;
        }

        [data-testid="stHeaderActionElements"] {
            display: none !important;
        }

        [data-testid="stHeadingWithActionElements"] a {
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
    apply_results_layout()

    analysis = st.session_state.get("analysis")

    if not analysis:
        st.warning("No hay resultados aún. Redirigiendo a Home...")
        st.switch_page("app.py")
        return

    render_map(analysis.get("route_points", []))

    recommendations = analysis.get("recommendations", [])

    panel_html = [
        '<div class="dz-panel">',
        "<h2>Resultados</h2>",
        "<h3>Recomendaciones</h3>",
    ]

    if not recommendations:
        panel_html.append('<div class="dz-card">No hay recomendaciones todavía.</div>')
    else:
        for item in recommendations:
            title = item.get("title", "Recomendación")
            summary = item.get("summary", "")
            duration = item.get("duration", "N/D")
            score = item.get("score", "N/D")
            panel_html.append(
                """
                <div class="dz-card">
                  <div class="dz-card-title">{}</div>
                  <div>{}</div>
                  <div class="dz-card-meta">
                    <span>⏱ {}</span>
                    <span>⭐ {}</span>
                  </div>
                </div>
                """.format(
                    title, summary, duration, score
                )
            )

    panel_html.append("</div>")
    st.markdown("\n".join(panel_html), unsafe_allow_html=True)
