import streamlit as st
import streamlit.components.v1 as components

# Configuración de página limpia
st.set_page_config(
    page_title="Un ramito para Zoé 💜",
    page_icon="💜",
    layout="wide"
)

# Ocultar barras por defecto de Streamlit para que parezca una app nativa
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div.block-container {padding: 0 !important;}
    iframe {border: none !important;}
    </style>
""", unsafe_allow_html=True)

# Leer tu archivo index.html que está en la misma carpeta
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Mostrar la experiencia interactiva a pantalla completa
components.html(html_code, height=850, scrolling=True)
