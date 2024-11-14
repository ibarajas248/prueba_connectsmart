import streamlit as st


# Función para mostrar la página de "Estados Financieros"
def mostrar_estadisticas():
    st.title("Estados Financieros")

    # Mostrar los tres botones
    if st.button("Botón 1"):
        st.write("Has hecho clic en Botón 1")

    if st.button("Botón 2"):
        st.write("Has hecho clic en Botón 2")

    if st.button("Botón 3"):
        st.write("Has hecho clic en Botón 3")

