import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Función para obtener datos paginados desde la API
def obtener_datos():
    url = "https://www.datos.gov.co/resource/6cat-2gcs.json"
    limit = 10000  # El límite máximo por consulta
    offset = 0  # Desplazamiento inicial
    all_data = []

    while True:
        # Hacer la solicitud con los parámetros limit y offset
        response = requests.get(url, params={"$limit": limit, "$offset": offset})
        data = response.json()

        if not data:
            break  # Si no hay más datos, salimos del bucle

        all_data.extend(data)  # Agregar los nuevos datos a la lista
        offset += limit  # Incrementar el desplazamiento para la siguiente página

    return all_data

# Función para mostrar el análisis de estadísticas
def mostrar_estadisticas():
    # Título de la aplicación
    st.title("Análisis de Empresas Colombianas")

    # Cargar datos con paginación
    data = obtener_datos()

    # Convertir JSON a DataFrame
    df = pd.DataFrame(data)

    # Preprocesamiento de datos: eliminar caracteres especiales y convertir a numérico
    for col in ['ingresos_operacionales', 'ganancia_p_rdida', 'total_activos', 'total_pasivos', 'total_patrimonio']:
        # Eliminar caracteres no numéricos y convertir a flotante
        df[col] = df[col].str.replace("$", "").str.replace(",", "").astype(float, errors='ignore')

    # Filtros definidos por el usuario en la página principal
    st.header("Filtros")

    # Filtro para elegir qué columna filtrar
    columnas = ['nit', 'raz_n_social', 'supervisor', 'macrosector', 'a_o_de_corte']
    filtro_columna = st.selectbox("Selecciona el campo para filtrar", columnas)

    # Dependiendo de la columna seleccionada, crear un filtro
    if filtro_columna == "nit":
        filtro_valor = st.text_input("Ingrese el NIT")
        if filtro_valor:
            df = df[df['nit'].str.contains(filtro_valor, na=False)]
    elif filtro_columna == "raz_n_social":
        filtro_valor = st.text_input("Ingrese la Razón Social")
        if filtro_valor:
            df = df[df['raz_n_social'].str.contains(filtro_valor, na=False)]
    elif filtro_columna == "supervisor":
        filtro_valor = st.text_input("Ingrese el Supervisor")
        if filtro_valor:
            df = df[df['supervisor'].str.contains(filtro_valor, na=False)]
    elif filtro_columna == "macrosector":
        # Mostrar el spinner dentro de la página
        with st.spinner('Filtrando por macrosector...'):
            filtro_valor = st.selectbox("Seleccione el Macrosector", df['macrosector'].unique())
            df = df[df['macrosector'] == filtro_valor]
    elif filtro_columna == "a_o_de_corte":
        filtro_valor = st.selectbox("Seleccione el Año de Corte", df['a_o_de_corte'].unique())
        df = df[df['a_o_de_corte'] == filtro_valor]

    # Mostrar el DataFrame filtrado
    st.subheader("Datos de Empresas Filtrados")
    st.dataframe(df)

    # Estadísticas descriptivas
    st.subheader("Estadísticas descriptivas")
    st.write(df[['ingresos_operacionales', 'ganancia_p_rdida', 'total_activos', 'total_pasivos',
                 'total_patrimonio']].describe())

    # Gráficos
    st.subheader("Gráficos")

    # Gráfico de barras: Ingresos operacionales por macrosector
    st.write("Ingresos Operacionales por Macrosector")
    macrosector_ingresos = df.groupby('macrosector')['ingresos_operacionales'].sum()
    fig, ax = plt.subplots()
    macrosector_ingresos.plot(kind='bar', ax=ax)
    plt.title("Ingresos Operacionales por Macrosector")
    plt.xlabel("Macrosector")
    plt.ylabel("Ingresos Operacionales (miles de Millones)")
    st.pyplot(fig)

    # Gráfico de pastel: Distribución de sectores
    st.write("Distribución de Empresas por Macrosector")
    sector_counts = df['macrosector'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(sector_counts, labels=sector_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Distribución de Empresas por Macrosector")
    st.pyplot(fig)

    # Gráfico de dispersión: Ganancia/Pérdida vs Total Activos
    st.write("Relación entre Ganancia/Pérdida y Total de Activos")
    fig, ax = plt.subplots()
    ax.scatter(df['total_activos'], df['ganancia_p_rdida'])
    plt.title("Ganancia/Pérdida vs Total Activos")
    plt.xlabel("Total Activos (Millones)")
    plt.ylabel("Ganancia/Pérdida (Millones)")
    st.pyplot(fig)

# Ejecutar la función
if __name__ == "__main__":
    mostrar_estadisticas()
