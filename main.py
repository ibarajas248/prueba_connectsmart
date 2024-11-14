import streamlit as st
import pagina1
import pagina2
import pagina3
import pagina4
import pagina5  # Importar la nueva página para "Estados Financieros"

# Definir las páginas de navegación
pages = {
    "API SECOP II": pagina1.mostrar_estadisticas,
    "SECOP II Busqueda inteligente": pagina4.mostrar_estadisticas,
    "RUES": pagina2.mostrar_estadisticas,
    "Buscar proveedor": pagina3.mostrar_estadisticas,
    "Estados Financieros": pagina5.mostrar_estadisticas  # Añadir "Estados Financieros"
}

# Inicializar `session_state` para el botón seleccionado
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "API SECOP II"  # Valor inicial

# Personalización del menú de navegación con CSS para estilo de botones
st.markdown(f"""
    <style>
        /* Fondo de la barra lateral */
        .sidebar .sidebar-content {{
            background-color: #0A2540;
            border-radius: 15px;
            padding: 10px;
        }}

        /* Título del menú en azul oscuro */
        .sidebar h2 {{
            color: #2C3E50;  /* Azul oscuro */
            font-weight: bold;
            font-size: 24px;
            margin-top: 0;
        }}

        /* Botones de navegación */
        .stButton > button {{
            width: 100%;
            color: #FFFFFF;
            background-color: #2C3E50;
            border: 2px solid #00CED1;
            border-radius: 8px;
            padding: 10px;
            margin: 5px 0;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
        }}

        /* Hover para los botones de navegación */
        .stButton > button:hover {{
            background-color: #1E90FF;
            color: #FFFFFF;
        }}
    </style>
""", unsafe_allow_html=True)

# Menú de navegación con título en azul oscuro
st.sidebar.markdown("<h2>Menú Principal</h2>", unsafe_allow_html=True)

# Crear botones y actualizar `selected_page` en `session_state` al hacer clic
if st.sidebar.button("API SECOP II"):
    st.session_state.selected_page = "API SECOP II"
if st.sidebar.button("SECOP II Busqueda inteligente"):
    st.session_state.selected_page = "SECOP II Busqueda inteligente"
if st.sidebar.button("RUES"):
    st.session_state.selected_page = "RUES"
if st.sidebar.button("Buscar proveedor"):
    st.session_state.selected_page = "Buscar proveedor"

if st.sidebar.button("Estados Financieros"):  # Botón para la nueva página
    st.session_state.selected_page = "Estados Financieros"

# Cargar la página seleccionada desde `session_state`
pages[st.session_state.selected_page]()
