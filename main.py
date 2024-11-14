import streamlit as st
import pagina1
import pagina2
import pagina3

# Definir las páginas de navegación
pages = {
    "API SECOP II": pagina1.mostrar_estadisticas,
    "RUES": pagina2.mostrar_estadisticas,
    "Buscar proveedor": pagina3.mostrar_estadisticas
}

# Configurar el menú de navegación en la barra lateral usando selectbox
selected = st.sidebar.selectbox(
    "Menú Principal",
    list(pages.keys()),
    index=0
)

# Personalización del menú de la barra lateral con CSS
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
            border-radius: 10px;
        }
        .css-1d391kg {
            padding: 12px;
            font-weight: bold;
        }
        .css-1d391kg select {
            background-color: #f8f9fa;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            font-size: 18px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Lógica para cargar la página seleccionada
pages[selected]()
