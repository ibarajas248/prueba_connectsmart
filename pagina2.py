import streamlit as st
import pandas as pd
import requests

# Función para mostrar el buscador en la página
def mostrar_estadisticas():


    # Mostrar la imagen de RUES con tamaño reducido
    image_url = "https://ccipiales.org.co/wp-content/uploads/2018/07/rues.png"
    st.image(image_url, caption='', use_container_width=False, width=400)  # Ajusté el tamaño a 200 píxeles

    # URL de la API
    json_url = "https://www.datos.gov.co/resource/c82u-588k.json"

    # Input para el número o identificador de búsqueda
    search_number = st.text_input(" Ingrese el número de identificación que desea buscar:")

    # Función para buscar un registro específico en la API con un límite aumentado
    @st.cache_data
    def fetch_record_by_number(json_url, search_number, limit=1000000000):
        try:
            # Usar el campo numero_identificacion en el filtro de búsqueda
            response = requests.get(f"{json_url}?$where=numero_identificacion='{search_number}'&$limit={limit}")
            if response.status_code == 200:
                data = response.json()
                if data:
                    df = pd.DataFrame(data)
                    return df
                else:
                    st.warning("No se encontraron registros con ese número de identificación.")
                    return pd.DataFrame()
            else:
                st.error("Error al obtener datos de la API")
                return pd.DataFrame()
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")
            return pd.DataFrame()

    # Ejecutar búsqueda cuando se ingresa un número
    if search_number:
        df = fetch_record_by_number(json_url, search_number)
        if not df.empty:
            st.write(f"Resultados para el número de identificación '{search_number}':")

            # Mostrar los datos en formato de tarjeta
            for index, row in df.iterrows():
                with st.expander(f"Resultado de busqueda por nit:  {search_number}"):

                    st.write(f"**Razón Social:** {row.get('razon_social', 'No disponible')}")
                    st.write(f"**Número de Identificación:** {row.get('numero_identificacion', 'No disponible')}")
                    st.write(f"**Tipo de Sociedad:** {row.get('tipo_sociedad', 'No disponible')}")
                    st.write(f"**Estado de Matrícula:** {row.get('estado_matricula', 'No disponible')}")
                    st.write(f"**Fecha de Matricula:** {row.get('fecha_matricula', 'No disponible')}")
                    st.write(f"**Categoría de Matrícula:** {row.get('categoria_matricula', 'No disponible')}")
                    st.write(f"**Representante Legal:** {row.get('representante_legal', 'No disponible')}")
                    st.write(f"**Primer Nombre del Representante:** {row.get('primer_nombre', 'No disponible')}")
                    st.write(f"**Primer Apellido del Representante:** {row.get('primer_apellido', 'No disponible')}")
                    st.write(f"**Fecha de Renovación:** {row.get('fecha_renovacion', 'No disponible')}")
        else:
            st.info("Ingrese un número de identificación para buscar un registro específico.")

# Ejecutar la función
if __name__ == "__main__":
    mostrar_estadisticas()
