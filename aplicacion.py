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

    import os

    st.title("Históricos")

    st.write("Ruta actual:")
    st.write(os.getcwd())

    st.write("Archivos visibles:")
    st.write(os.listdir("."))

    if os.path.exists("historicos.csv"):
        st.success("✅ historicos.csv encontrado")
    else:
        st.error("❌ historicos.csv NO encontrado")
elif menu == "Estadísticas":

    st.title("Estadísticas")

    st.write("Módulo estadístico en construcción.")

elif menu == "Predicciones":

    st.title("Predicciones")

    st.write("Motor predictivo en construcción.")

elif menu == "Configuración":

    st.title("Configuración")

    st.write("Panel de configuración del sistema.")
