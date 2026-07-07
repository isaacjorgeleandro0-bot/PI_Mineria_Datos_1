import streamlit as st

# Configuración inicial de la plataforma
st.set_page_config(
    page_title="Streaming Analytics - Home",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Plataforma de Streaming: Análisis y Modelado de Usuarios")
st.markdown("---")

st.markdown("### 📝 Contexto del Proyecto")
st.write("""
Este proyecto aborda el análisis integral del comportamiento de los usuarios en una plataforma de streaming. 
A partir de un set de datos bruto con severas inconsistencias, se diseñó e implementó un pipeline completo de ciencia de datos: 
desde la **Inspección Inicial** y **Limpieza de Calidad**, pasando por un profundo **Análisis Exploratorio (EDA)**, 
hasta la reducción de dimensionalidad mediante **Componentes Principales (PCA)**. 

El objetivo final es transformar datos ruidosos en conocimiento estratégico para el negocio, permitiendo identificar 
patrones de consumo y segmentos de usuarios críticos con alto riesgo de abandono de la plataforma.
""")

st.write("""
*Nota: Esta aplicación web está diseñada para comunicar los resultados de forma clara y visual a un público general, 
y actúa como complemento de la evidencia técnica resguardada en el repositorio del proyecto.*
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👥 Integrantes")
    st.markdown("- *Jorge Leandro Isaac*")
    st.markdown("- *Luis Lorenzo*")
    
    
    st.markdown("**Comisión:** Turno Tarde")
    st.markdown("**Año:**2026")

with col2:
    st.markdown("### 📂 Evidencia Técnica y Código")
    st.write("Podés acceder a los notebooks de desarrollo (.ipynb), scripts de ingeniería de datos y documentación técnica completa a través de nuestro repositorio público:")
    
    # 🚨 REEMPLAZÁ ESTE ENLACE CON TU REPOSITORIO REAL DE GITHUB
    st.markdown("[🔗 Enlace al Repositorio de GitHub](https://https://github.com/isaacjorgeleandro0-bot/PI_Mineria_Datos_1)")