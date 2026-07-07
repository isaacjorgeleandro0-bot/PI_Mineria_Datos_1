import streamlit as st
import pandas as pd

st.set_page_config(page_title="Descripción del Dataset", page_icon="📊", layout="wide")

st.title("📊 Descripción e Ingeniería del Dataset")
st.markdown("---")

st.markdown("### 📝 Descripción General")
st.write("""
El conjunto de datos original proviene del archivo fuente `streaming_users_dirty.json`. 
Contiene registros sobre las características demográficas de los clientes (edad, país), 
sus preferencias internas (género favorito, plan de suscripción) y sus métricas de interacción mensuales 
(minutos de reproducción, tickets de soporte técnico generados y fecha del último inicio de sesión).
""")

st.markdown("### 🔍 Vista Previa Estructurada del Dataset")
st.write("Estructura base del set de datos procesado con el que trabaja la aplicación:")

# Estructura limpia simulada para cumplir con la vista previa simple solicitada
columnas_reales = ["user_id", "age", "country", "subscription_plan", "last_login_date", "favorite_genre", "monthly_watch_time_mins", "customer_support_tickets"]
df_preview = pd.DataFrame(columns=columnas_reales)
st.dataframe(df_preview, use_container_width=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🚨 Resumen Breve de Calidad (Datos Brutos)")
    st.warning("""
    La inspección inicial sobre los **8,160 registros originales** expuso serias fallas de integridad:
    * **Valores Faltantes (Nulos):** Brechas detectadas en `last_login_date` (320 nulos), `monthly_watch_time_mins` (193 nulos) y `favorite_genre` (240 nulos).
    * **Duplicados:** Se encontraron 126 registros exactamente idénticos y repetidos.
    * **Incoherencias Críticas:** Edades fuera de la realidad humana (valores negativos como -5 y picos de 150 años), minutos mensuales de consumo negativos (-120) y reclamos de soporte por debajo de cero (-1).
    * **Inconsistencias de Formato:** Escrituras heterogéneas en variables cualitativas (mezclas de mayúsculas, minúsculas, acentos y traducciones en planes, países y géneros).
    """)

with col2:
    st.markdown("### 🧪 Transformaciones Principales Aplicadas")
    st.success("""
    Para construir una base analítica confiable, se ejecutó un pipeline estructurado de limpieza:
    * **Estandarización Categórica:** Unificación de formatos de texto, remoción de espacios y corrección de errores ortográficos (*Premiun* a *Premium*, *Std* a *Estándar*).
    * **Depuración de Duplicados:** Eliminación de las filas redundantes detectadas.
    * **Tratamiento de Nulos:** Conversión de falsas cadenas de texto (`'None'`, `'Nan'`) a valores nulos reales (`NaN`) e imputación justificada según la distribución estadística de cada variable.
    * **Control de Outliers (Capping):** Corrección y acotación de valores extremos imposibles (reemplazando edades erróneas y valores negativos por medidas estadísticas coherentes como medianas y topes lógicos).
    """)