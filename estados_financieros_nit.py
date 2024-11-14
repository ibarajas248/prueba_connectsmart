import streamlit as st
import requests

# Función para obtener los datos desde la URL
def obtener_datos(nit):
    if nit:  # Si el NIT no está vacío
        url = f"https://www.datos.gov.co/resource/6cat-2gcs.json?nit={nit}"
        response = requests.get(url)

        # Verificar si la respuesta fue exitosa
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            st.error("No se pudo obtener la información del NIT.")
            return None
    else:
        return None

# Función para mostrar el NIT y los resultados en forma de tarjeta
def mostrar_estadisticas():
    # Crear el diseño de la aplicación en Streamlit
    st.title("Consulta de Información por NIT")

    # Obtener el NIT directamente desde la interfaz de usuario
    nit = st.text_input("Ingresa el NIT, ejemplo 901526800")

    # Si se ingresa un NIT, consultar los datos
    if nit:
        # Llamar a la función para obtener los datos
        datos = obtener_datos(nit)

        # Si se obtuvieron datos
        if datos:
            for item in datos:
                st.markdown(f"""
                <div style="border: 1px solid #ddd; padding: 16px; border-radius: 8px; background-color: #f9f9f9; width: 100%; max-width: 600px; margin: 10px 0;">
                    <h3 style="text-align: center;">Información del NIT: {item.get('nit', 'No disponible')}</h3>
                    <ul>
                        <li><strong>Razón Social:</strong> {item.get('raz_n_social', 'No disponible')}</li>
                        <li><strong>Supervisor:</strong> {item.get('supervisor', 'No disponible')}</li>
                        <li><strong>Región:</strong> {item.get('regi_n', 'No disponible')}</li>
                        <li><strong>Departamento de Domicilio:</strong> {item.get('departamento_domicilio', 'No disponible')}</li>
                        <li><strong>Ciudad de Domicilio:</strong> {item.get('ciudad_domicilio', 'No disponible')}</li>
                        <li><strong>CIUU:</strong> {item.get('ciiu', 'No disponible')}</li>
                        <li><strong>Macrosector:</strong> {item.get('macrosector', 'No disponible')}</li>
                        <li><strong>Ingresos Operacionales:</strong> {item.get('ingresos_operacionales', 'No disponible')}</li>
                        <li><strong>Ganancia o Pérdida:</strong> {item.get('ganancia_p_rdida', 'No disponible')}</li>
                        <li><strong>Total Activos:</strong> {item.get('total_activos', 'No disponible')}</li>
                        <li><strong>Total Pasivos:</strong> {item.get('total_pasivos', 'No disponible')}</li>
                        <li><strong>Total Patrimonio:</strong> {item.get('total_patrimonio', 'No disponible')}</li>
                        <li><strong>Año de Corte:</strong> {item.get('a_o_de_corte', 'No disponible')}</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No se encontraron datos para este NIT.")
    else:
        st.warning("Por favor ingresa un NIT para consultar.")


# Ejecutar la función
if __name__ == "__main__":
    mostrar_estadisticas()
