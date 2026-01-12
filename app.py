"""
Streamlit Hello World Application with Custom CSS
"""

import streamlit as st


def apply_custom_css():
    """Apply custom CSS styling to the Streamlit app"""
    st.markdown(
        """
        <style>
        /* Main container styling */
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        /* Title styling */
        .title {
            font-size: 4rem;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            padding: 2rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            animation: fadeIn 2s ease-in;
        }
        
        /* Subtitle styling */
        .subtitle {
            font-size: 1.5rem;
            color: #f0f0f0;
            text-align: center;
            padding: 1rem;
            animation: fadeIn 3s ease-in;
        }
        
        /* Card container */
        .card {
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem auto;
            max-width: 600px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }
        
        /* Card text */
        .card-text {
            color: #333;
            font-size: 1.2rem;
            text-align: center;
            line-height: 1.8;
        }
        
        /* Animation keyframes */
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Button styling */
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
        </style>
        """,
        unsafe_allow_html=True
    )


def main():
    """Main application function"""
    # Set page configuration
    st.set_page_config(
        page_title="Hello World - Streamlit",
        page_icon="👋",
        layout="wide"
    )
    
    # Apply custom CSS
    apply_custom_css()
    
    # Main title
    st.markdown('<h1 class="title">👋 ¡Hola Mundo!</h1>', unsafe_allow_html=True)
    
    # Subtitle
    st.markdown(
        '<p class="subtitle">Bienvenido a tu primera aplicación Streamlit con CSS personalizado</p>',
        unsafe_allow_html=True
    )
    
    # Card with content
    st.markdown(
        """
        <div class="card">
            <p class="card-text">
                Esta es una aplicación de ejemplo que demuestra cómo usar 
                <strong>Streamlit</strong> con estilos CSS personalizados para crear 
                interfaces web interactivas y visualmente atractivas.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Interactive elements
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="🚀 Framework", value="Streamlit", delta="v1.31.0")
    
    with col2:
        st.metric(label="🎨 Tecnología", value="CSS", delta="Custom")
    
    with col3:
        st.metric(label="🐍 Lenguaje", value="Python", delta="3.x")
    
    st.markdown("---")
    
    # Interactive button
    if st.button("¡Haz clic aquí! 🎉"):
        st.balloons()
        st.success("¡Excelente! Has interactuado con la aplicación. 🎊")
    
    # Sidebar
    with st.sidebar:
        st.header("📋 Información")
        st.write("Esta aplicación demuestra:")
        st.write("✅ Estilos CSS personalizados")
        st.write("✅ Diseño responsivo")
        st.write("✅ Animaciones CSS")
        st.write("✅ Componentes interactivos")
        st.write("✅ Gradientes y sombras")
        
        st.markdown("---")
        st.info("💡 Tip: Edita el archivo `app.py` para personalizar la aplicación.")


if __name__ == "__main__":
    main()
