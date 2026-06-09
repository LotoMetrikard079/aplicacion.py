import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="LOTOMETRIKA RD",
    layout="wide"
)

menu = st.sidebar.radio(
    "Navegación",
    [
        "Inicio",
        "Históricos",
        "Estadísticas",
        "Predicciones",
        "Configuración"
    ]
)

if menu == "Inicio":

    st.title("LOTOMETRIKA RD")

    st.subheader("Motor Estadístico y Predictivo")

    st.write(
        "Sistema de análisis, estadísticas y predicciones para loterías de República Dominicana."
    )

    st.divider()

    st.write("Versión 1.0 - Infraestructura inicial operativa")

elif menu == "Históricos":

    st.title("Históricos")

    df = pd.read_csv("historicos.csv")

    st.success("✅ Históricos cargados correctamente")

    st.write(f"Total de sorteos registrados: {len(df)}")

    st.dataframe(df, use_container_width=True)
elif menu == "Estadísticas":

    st.title("Estadísticas")

    st.write("Módulo estadístico en construcción.")

elif menu == "Predicciones":

    st.title("Predicciones")

    st.write("Motor predictivo en construcción.")

elif menu == "Configuración":

    st.title("Configuración")

    st.write("Panel de configuración del sistema.")
