import streamlit as st
import pandas as pd
import requests

# Lista de algunas ciudades de Colombia (puedes agregar más según sea necesario)
ciudades_colombia = [
    "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Bucaramanga", "Pereira",
    "Cúcuta", "Santa Marta", "Manizales", "Ibagué", "Neiva", "Tunja", "Villavicencio",
    "Valledupar", "Popayán", "Montería", "Armenia", "Sincelejo", "Quibdó"
]

# Función para mostrar el buscador en la página
def mostrar_estadisticas():
    # Título
    st.title("Consulta de Proveedor")

    # Cuadro de texto para ingresar el valor de búsqueda
    valor_busqueda = st.text_input("Ingrese el valor de búsqueda:")

    # Spinner para elegir la categoría de búsqueda
    opcion_busqueda = st.selectbox(
        "Seleccione el tipo de búsqueda:",
        ["codigo_principal_de_categoria", "nit"]
    )

    # Si se selecciona la búsqueda por código de categoría, muestra un ejemplo
    if opcion_busqueda == "codigo_principal_de_categoria":
        st.text("Valor de ejemplo: V1.81101500")
    elif opcion_busqueda== "nit":
        st.text("Valor de ejemplo: 830515117")




    # Spinner para elegir la ciudad (opción para todas las ciudades)
    ciudad_seleccionada = st.selectbox("Seleccione la ciudad:", ["Todas las Ciudades"] + ciudades_colombia)

    # Botón de búsqueda
    if st.button("Buscar"):
        if valor_busqueda:
            if opcion_busqueda == "codigo_principal_de_categoria":
                # Acción cuando se selecciona 'codigo_principal_de_categoria'
                url_php = f"https://ivanbarajastech.com/app_b2bhackaton/base.php?codigo_principal_de_categoria={valor_busqueda}"

                try:
                    response = requests.get(url_php)

                    if response.status_code == 200:
                        data = response.json()
                        df = pd.DataFrame(data)

                        if not df.empty:
                            if ciudad_seleccionada != "Todas las Ciudades":
                                df_ciudad = df[df['ciudad_proveedor'] == ciudad_seleccionada]
                            else:
                                df_ciudad = df

                            # Agrupación para obtener el top 10 de proveedores con más contratos
                            df_grouped = df_ciudad.groupby(['nombre_del_proveedor', 'ciudad_proveedor',
                                                            'nit_del_proveedor_adjudicado']).size().reset_index(
                                name='total_contratos')
                            df_top_10 = df_grouped.sort_values(by='total_contratos', ascending=False).head(10)

                            # Agrupación para obtener el top 10 de proveedores con el mayor valor de adjudicación
                            df_valor_adjudicado = df_ciudad.groupby('nombre_del_proveedor')[
                                'valor_total_adjudicacion'].sum().reset_index()
                            df_valor_adjudicado = df_valor_adjudicado.sort_values(by='valor_total_adjudicacion',
                                                                                  ascending=False).head(10)

                            # Agrupación para obtener las ciudades con más proveedores
                            df_proveedores_ciudad = df_ciudad.groupby('ciudad_proveedor').size().reset_index(
                                name='total_proveedores')
                            df_proveedores_ciudad = df_proveedores_ciudad.sort_values(by='total_proveedores',
                                                                                      ascending=False).head(10)

                            # Mostrar las estadísticas en Streamlit
                            st.write(
                                f"Top 10 Proveedores en {ciudad_seleccionada if ciudad_seleccionada != 'Todas' else 'Todas las Ciudades'} con Más Contratos:")
                            st.dataframe(df_top_10)

                            st.write(
                                f"Top 10 Proveedores en {ciudad_seleccionada if ciudad_seleccionada != 'Todas' else 'Todas las Ciudades'} con Mayor Valor de Adjudicación:")
                            st.dataframe(df_valor_adjudicado)

                            st.write(
                                f"Top 10 Ciudades con Más Proveedores en {ciudad_seleccionada if ciudad_seleccionada != 'Todas' else 'Todas las Ciudades'}:")
                            st.dataframe(df_proveedores_ciudad)

                        else:
                            st.warning(f"No se encontraron registros para la ciudad {ciudad_seleccionada}.")
                    else:
                        st.error(f"Error al obtener los datos. Código de estado: {response.status_code}")

                except requests.exceptions.RequestException as e:
                    st.error(f"Ocurrió un error al hacer la solicitud: {e}")


            elif opcion_busqueda == "nit":

                # Acción cuando se selecciona 'nit'

                url_php = f"https://ivanbarajastech.com/app_b2bhackaton/nit.php?nit={valor_busqueda}"

                try:

                    response = requests.get(url_php)

                    if response.status_code == 200:

                        data = response.json()

                        df = pd.DataFrame(data)

                        if not df.empty:

                            if ciudad_seleccionada != "Todas las Ciudades":
                                df_ciudad = df[df['ciudad_proveedor'] == ciudad_seleccionada]
                            else:
                                df_ciudad = df

                            # Mostrar el DataFrame completo

                            st.write(f"Datos obtenidos para el NIT {valor_busqueda}:")

                            st.dataframe(df)  # Muestra el DataFrame directamente




                                # Agrupar y contar registros
                            df_grouped = df_ciudad.groupby(['nombre_del_proveedor'],).size().reset_index(
                                name='cantidad_contratos')

                            # Mostrar las estadísticas en una tarjeta
                            with st.container():
                                st.write(f"**Cantidad de Contratos por Proveedor para {valor_busqueda}:**")
                                st.dataframe(df_grouped)  # Muestra el DataFrame agrupado

                                #dddd

                            df_proveedores_ciudad = df_ciudad.groupby('ciudad_proveedor').size().reset_index(
                                name='total_proveedores')
                            df_proveedores_ciudad = df_proveedores_ciudad.sort_values(by='total_proveedores',
                                                                                      ascending=False).head(10)





                        else:

                            st.warning(f"No se encontraron registros para el NIT {valor_busqueda}.")


                    else:

                        st.error(f"Error al obtener los datos. Código de estado: {response.status_code}")


                except requests.exceptions.RequestException as e:

                    st.error(f"Ocurrió un error al hacer la solicitud: {e}")


        else:
            st.warning("Por favor ingrese un valor para buscar.")


# Ejecutar la función
if __name__ == "__main__":
    mostrar_estadisticas()
