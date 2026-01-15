import streamlit as st

from pages.home.page import render as render_home
from pages.results.page import render as render_results


def apply_custom_css():
    st.markdown(
        """
        <style>
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .stButton > button {
            background-color: #667eea;
            color: white;
            border-radius: 25px;
            padding: 0.75rem 2rem;
            font-size: 1.1rem;
            border: none;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #764ba2;
            box-shadow: 0 6px 20px rgba(118, 75, 162, 0.6);
            transform: translateY(-2px);
        }

        h1 a svg,
        h2 a svg,
        h3 a svg,
        h4 a svg,
        h5 a svg,
        h6 a svg {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    st.set_page_config(page_title="DelayZero", page_icon="🗺️", layout="wide")

    apply_custom_css()

    with st.sidebar:
        st.title("DelayZero")
        page = st.radio("Navegación", ["Home", "Results"], index=0)

    if page == "Home":
        render_home()
    else:
        render_results()


if __name__ == "__main__":
    main()
