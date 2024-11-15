import streamlit as st
import pagina1
import pagina2
import pagina3
import estadosfinancieros
import pagina4
import pagina5  # Importar la nueva página para "Estados Financieros"
import estados_financieros_nit  # Importar la página 'estados_financieros_nit'
import emis_st  # Importar el archivo emis_st.py
import analisis_webscrap  # Importar la nueva página para "Scraping Supersociedades"

# Definir las páginas de navegación
pages = {
    "API SECOP II": pagina1.mostrar_estadisticas,
    "RUES": pagina2.mostrar_estadisticas,
    "Buscar proveedor": pagina3.mostrar_estadisticas,
    "SECOP II Busqueda inteligente": pagina4.mostrar_estadisticas,
    "Reportes Financieros": estadosfinancieros.mostrar_estadisticas,
    "Estados Financieros NIT": estados_financieros_nit.mostrar_estadisticas,
    "Informes EMIS": emis_st.mostrar_estadisticas,
    "Scraping Supersociedades": analisis_webscrap.mostrar_estadisticas  # Añadir la nueva página
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

# Agregar la imagen al principio del menú de navegación (usando use_container_width)
st.sidebar.image("https://p4s.co/photo/mp-startup-logo-4232-1730860177624.jpg", use_container_width=True)

# Menú de navegación con título en azul oscuro
st.sidebar.markdown("<h2>Menú Principal</h2>", unsafe_allow_html=True)

# Crear botones y actualizar `selected_page` en `session_state` al hacer clic
if st.sidebar.button("API SECOP II"):
    st.session_state.selected_page = "API SECOP II"
if st.sidebar.button("RUES"):
    st.session_state.selected_page = "RUES"
if st.sidebar.button("Buscar proveedor"):
    st.session_state.selected_page = "Buscar proveedor"
if st.sidebar.button("SECOP II Busqueda inteligente"):
    st.session_state.selected_page = "SECOP II Busqueda inteligente"
if st.sidebar.button("Reportes Financieros"):
    st.session_state.selected_page = "Reportes Financieros"
if st.sidebar.button("Estados Financieros NIT"):
    st.session_state.selected_page = "Estados Financieros NIT"
if st.sidebar.button("Informes EMIS"):
    st.session_state.selected_page = "Informes EMIS"
if st.sidebar.button("Scraping Supersociedades"):  # Botón para la nueva página de Scraping
    st.session_state.selected_page = "Scraping Supersociedades"

# Ejecutar la función asociada con la página seleccionada
if st.session_state.selected_page in pages:
    pages[st.session_state.selected_page]()  # Llamar a la función correspondiente de la página seleccionada
