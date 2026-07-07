import streamlit as st

st.set_page_config(page_title="Conclusiones", page_icon="🏁", layout="wide")

st.title("🏁 Conclusiones, Limitaciones y Próximos Pasos")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 Hallazgos Principales")
    st.write("""
    1. **La Calidad de Datos como Pilar:** El proceso de curaduría y limpieza permitió transformar un archivo crudo sumamente ruidoso (`streaming_users_dirty.json`) en una base analítica consistente, minimizando la pérdida de información mediante técnicas de capping e imputaciones bien fundamentadas.
    2. **Mitigación de Churn (Abandono):** El EDA identificó con claridad un nicho de riesgo: usuarios mayores de 46 años adheridos al Plan Básico que muestran un consumo casi nulo. Este hallazgo dota a la empresa de una oportunidad concreta para aplicar promociones o cambiar la usabilidad para retenerlos.
    3. **Sintetización del Comportamiento (PCA):** La transformación condensó de forma exitosa las variables numéricas en componentes ortogonales independientes, mapeando con precisión los niveles de actividad y fricción de los clientes.
    """)

with col2:
    st.markdown("### ⚠️ Limitaciones del Estudio")
    st.write("""
    * **Brecha Temporal:** Los valores nulos originales presentes en las fechas de último inicio de sesión (`last_login_date`) limitaron la posibilidad de realizar un análisis de series de tiempo más profundo sobre la estacionalidad del negocio.
    * **Espacio de Atributos Restringido:** Al contar con solo tres variables continuas aptas para PCA, el modelado matemático de componentes quedó acotado, impidiendo añadir más dimensiones operativas del negocio al espacio resumido.
    """)

st.markdown("---")
st.markdown("### 🔮 Próximos Pasos")
st.success("""
* **Modelado Predictivo de Bajas:** Entrenar modelos de Machine Learning supervisados (como Random Forest o Regresión Logística) sobre la base limpia para predecir con exactitud qué usuarios individuales muestran alta probabilidad de cancelar su suscripción.
* **Segmentación Automatizada (Clustering):** Aplicar algoritmos de agrupamiento no supervisado (K-Means) sobre las Componentes Principales obtenidas para construir de forma automática grupos específicos de clientes y personalizar el catálogo de contenidos según su actividad.
""")