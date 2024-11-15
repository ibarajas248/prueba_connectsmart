import streamlit as st
import pandas as pd

# Función para mostrar el análisis de empresas
def mostrar_estadisticas():
    # Mostrar la imagen al inicio
    st.image("https://capacitacionvirtual.supersociedades.gov.co/pluginfile.php/1/theme_moove/logo/1608423457/logo_.png", use_container_width=True)

    # Título de la aplicación
    st.title("Análisis de Empresas")

    # Ruta del archivo Excel
    file_path = "data/web_scrappin_supersociedades.xlsx"  # Aquí deberás poner la ruta de tu archivo Excel

    # Intentar cargar el archivo directamente desde la ruta
    try:
        # Cargar los datos del archivo Excel
        df = pd.read_excel(file_path)

        # Verificar si las columnas necesarias están presentes
        required_columns = ['Empresa', 'Activos', 'Ingresos', 'Utilidad Neta']
        if not all(col in df.columns for col in required_columns):
            st.error("El archivo debe contener las columnas: 'Empresa', 'Activos', 'Ingresos' y 'Utilidad Neta'.")
        else:
            # Mostrar las primeras filas del dataframe
            #st.write("Datos cargados:", df.head(100))

            # Barra de búsqueda con sugerencias
            search_term = st.text_input("Busca una empresa")

            if search_term:
                # Filtrar el dataframe para mostrar solo las empresas que contienen el término de búsqueda
                filtered_df = df[df['Empresa'].str.contains(search_term, case=False, na=False)]

                # Si hay resultados, mostrarlos
                if not filtered_df.empty:
                    # Mostrar las tarjetas en una sola columna
                    for idx, row in filtered_df.iterrows():
                        # Tarjeta de la empresa
                        st.markdown(
                            f"""
                            <div style="background-color: #f1f1f1; padding: 20px; margin: 10px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                                <h4 style="font-weight: bold;">{row['Empresa']}</h4>
                                <p><strong>Activos:</strong> {row['Activos']}</p>
                                <p><strong>Ingresos:</strong> {row['Ingresos']}</p>
                                <p><strong>Utilidad Neta:</strong> {row['Utilidad Neta']}</p>
                            </div>
                            """, unsafe_allow_html=True)
                else:
                    st.write("No se encontraron resultados para la búsqueda.")
            else:
                # Si no se ha introducido texto, mostrar todas las empresas
                for idx, row in df.iterrows():
                    # Tarjeta de la empresa
                    st.markdown(
                        f"""
                        <div style="background-color: #f1f1f1; padding: 20px; margin: 10px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                            <h4 style="font-weight: bold;">{row['Empresa']}</h4>
                            <p><strong>Activos:</strong> {row['Activos']}</p>
                            <p><strong>Ingresos:</strong> {row['Ingresos']}</p>
                            <p><strong>Utilidad Neta:</strong> {row['Utilidad Neta']}</p>
                        </div>
                        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo: {e}")


# Ejecutar la función
if __name__ == "__main__":
    mostrar_estadisticas()
