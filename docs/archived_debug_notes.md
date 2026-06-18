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
