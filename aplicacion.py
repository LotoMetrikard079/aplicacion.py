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

    df = pd.read_csv("historicos.csv")

    st.write(f"Total de sorteos: {len(df)}")

    numeros = pd.concat([
        df["primero"],
        df["segundo"],
        df["tercero"]
    ])

    frecuencia = numeros.value_counts()
    numero_caliente = frecuencia.index[0]
    apariciones_caliente = frecuencia.iloc[0]

    numero_frio = frecuencia.index[-1]
    apariciones_frio = frecuencia.iloc[-1]

    st.success(
        f"🔥 Número más frecuente: {numero_caliente} ({apariciones_caliente} apariciones)"
    )

    st.info(
        f"❄️ Número menos frecuente: {numero_frio} ({apariciones_frio} apariciones)"
    )

    st.subheader("Top 10 números más frecuentes")

    st.dataframe(
        frecuencia.head(10).reset_index(),
        use_container_width=True
    )
    st.subheader("Distribución por lotería")

    st.dataframe(
        df["loteria"].value_counts().reset_index(),
        use_container_width=True
    )

elif menu == "Predicciones":

    st.title("Predicciones")

    st.write("Motor predictivo en construcción.")

elif menu == "Configuración":

    st.title("Configuración")

    st.write("Panel de configuración del sistema.")
