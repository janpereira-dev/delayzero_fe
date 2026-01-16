import streamlit as st


def apply_app_style():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Google+Sans:ital,opsz,'
                    'wght@0,17..18,400..700;1,17..18,400..700&family=Roboto:ital,'
                    'wght@0,100..900;1,100..900&display=swap');

        html, body, .stApp, .stMarkdown, .stTextInput, .stTextArea, .stSelectbox,
        .stRadio, .stCheckbox, .stNumberInput, .stDateInput, .stTimeInput,
        .stButton, button, input, textarea, select, label, p, span, div {
            font-family: "Roboto", sans-serif;
            font-optical-sizing: auto;
            font-weight: 400;
            font-style: normal;
            font-variation-settings: "wdth" 100;
        }

        html, body, .stApp {
            background: linear-gradient(135deg, #6a2c91 0%, #c63c8a 45%, #f28a2e 100%);
        }

        .main {
            background: transparent;
        }

        .stButton > button {
            background-color: #6a2c91;
            color: white;
            border-radius: 25px;
            padding: 0.75rem 2rem;
            font-size: 1.1rem;
            border: none;
            box-shadow: 0 4px 15px rgba(106, 44, 145, 0.35);
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #c63c8a;
            box-shadow: 0 6px 20px rgba(198, 60, 138, 0.45);
            transform: translateY(-2px);
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            position: relative;
            border: 0 !important;
            padding: 12px !important;
            border-radius: 14px !important;
            overflow: hidden;
            background: transparent !important;
        }

        [data-testid="stVerticalBlockBorderWrapper"]::before {
            content: "";
            position: absolute;
            z-index: 0;
            left: -50%;
            top: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(135deg, #6a2c91, #c63c8a, #f28a2e);
            animation: dzBorderRotate 6s linear infinite;
        }

        [data-testid="stVerticalBlockBorderWrapper"]::after {
            content: "";
            position: absolute;
            z-index: 1;
            left: 2px;
            top: 2px;
            width: calc(100% - 4px);
            height: calc(100% - 4px);
            background: rgba(255, 255, 255, 0.92);
            border-radius: 12px;
        }

        [data-testid="stVerticalBlockBorderWrapper"] > div {
            position: relative;
            z-index: 2;
        }

        @keyframes dzBorderRotate {
            100% {
                transform: rotate(1turn);
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
