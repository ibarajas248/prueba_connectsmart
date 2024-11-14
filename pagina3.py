import streamlit as st
import pandas as pd
import requests

# Función para mostrar el buscador en la página
def mostrar_estadisticas():

    # Mostrar título
    st.title("Buscar proveedor")

    # Mostrar la imagen de RUES con tamaño reducido
    image_url = "https://blogger.googleusercontent.com/img/a/AVvXsEhWytS90hKcN0Ycn0qDQc9HVPioeV9tISGBDXO3s1_hnhfNHl7AayiN3b7kqoSv12dRMSG-Uoktz1Vwc4aPHz1b3flW-1Mq-P4OXvC2xw2BXUCp5WPG0ZOSSJHjheQcuSEEX_iRT7kCmiEF49iC4NS98vC9rUcWaQnTnyb6j1dDSdW6Gmhnn_JPNm3B"
    st.image(image_url, caption='', use_container_width=False, width=400)  # Ajusté el tamaño a 200 píxeles

    # URL de la API
    json_url = "https://www.datos.gov.co/resource/qmzu-gj57.json"

    # Input para el número o identificador de búsqueda
    search_nit = st.text_input("Ingrese el NIT que desea buscar:")

    # Función para buscar un registro específico en la API con un límite aumentado
    @st.cache_data
    def fetch_record_by_nit(json_url, search_nit, limit=1000000000):
        try:
            # Usar el campo nit en el filtro de búsqueda
            response = requests.get(f"{json_url}?$where=nit='{search_nit}'&$limit={limit}")
            if response.status_code == 200:
                data = response.json()
                if data:
                    df = pd.DataFrame(data)
                    return df
                else:
                    st.warning("No se encontraron registros con ese NIT.")
                    return pd.DataFrame()
            else:
                st.error("Error al obtener datos de la API")
                return pd.DataFrame()
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")
            return pd.DataFrame()

    # Ejecutar búsqueda cuando se ingresa un NIT
    if search_nit:
        df = fetch_record_by_nit(json_url, search_nit)
        if not df.empty:
            st.write(f"Resultados para el NIT '{search_nit}':")

            # Mostrar los datos en formato de tarjeta
            for index, row in df.iterrows():
                with st.expander(f"Resultado de búsqueda por NIT: {search_nit}"):

                    # Mostrar cada columna encontrada
                    for col, value in row.items():
                        st.write(f"**{col.replace('_', ' ').title()}:** {value if value else 'No disponible'}")

        else:
            st.info("Ingrese un NIT para buscar un registro específico.")

# Ejecutar la función
if __name__ == "__main__":
    mostrar_estadisticas()
