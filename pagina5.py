import streamlit as st
import estadosfinancieros
import estados_financieros_nit  # Asegúrate de importar correctamente

# Función para mostrar la página de "Estados Financieros"
def mostrar_estadisticas():
    st.title("Estados Financieros")

    # Inicializar el estado para controlar la visibilidad de la página
    if "mostrar_pagina" not in st.session_state:
        st.session_state.mostrar_pagina = False  # Estado inicial: página oculta

    # Mostrar el botón para alternar la visibilidad
    if st.button("Botón 1"):
        # Alternar el estado de la página (mostrar/ocultar)
        st.session_state.mostrar_pagina = not st.session_state.mostrar_pagina

    # Si la página debe mostrarse, llamar a la función de estadosfinancieros
    if st.session_state.mostrar_pagina:
        estadosfinancieros.mostrar_estadisticas()
    else:
        st.write("Página oculta")

    # Los otros botones
    if st.button("Botón 2"):
        # Llamar la función de estadosfinancieros_nit para mostrar la información del NIT
        estados_financieros_nit.mostrar_estados_financieros_nit()  # Llamada correcta a la función

    if st.button("Botón 3"):
        st.write("Has hecho clic en Botón 3")
