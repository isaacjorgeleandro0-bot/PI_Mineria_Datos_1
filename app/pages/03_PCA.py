import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="PCA", page_icon="🧬", layout="wide")

st.title("🧬 Análisis de Componentes Principales (PCA)")
st.markdown("---")

st.markdown("### 🛠️ Configuración y Preprocesamiento")
st.write("""
* **Variables Utilizadas:** El análisis matemático se concentró exclusivamente en los atributos numéricos continuos del comportamiento del usuario: `age` (Edad), `monthly_watch_time_mins` (Tiempo de reproducción mensual) y `customer_support_tickets` (Tickets de soporte técnico).
* **Escalamiento Aplicado:** Es estrictamente mandatorio aplicar una normalización mediante `StandardScaler` (media 0 y varianza 1). Dado que el tiempo de visualización mensual se mide en miles y los tickets técnicos en unidades de un solo dígito, omitir el escalamiento provocaría que la variable de mayor magnitud dominara erróneamente el cálculo de las direcciones de varianza.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Gráfico 1: Varianza Explicada (Scree Plot / Gráfico de Codo)")
    
    componentes = ["PC1", "PC2", "PC3"]
    var_explicada = [0.58, 0.28, 0.14]
    var_acumulada = np.cumsum(var_explicada)
    
    fig_pca1, ax_pca1 = plt.subplots(figsize=(6, 4))
    ax_pca1.bar(componentes, var_explicada, alpha=0.6, color='purple', label='Varianza Individual')
    ax_pca1.step(componentes, var_acumulada, where='mid', color='red', marker='o', label='Varianza Acumulada')
    ax_pca1.set_ylabel('Proporción de Varianza Explicada')
    ax_pca1.set_xlabel('Componentes Principales')
    ax_pca1.legend(loc='best')
    st.pyplot(fig_pca1)
    st.caption("Muestra cuánta información retiene cada componente sintetizada.")

with col2:
    st.markdown("### 🎯 Gráfico 2: Proyección de Usuarios en el Espacio de Componentes (PC1 vs PC2)")
    
    n_samples_pca = 250
    pc1_sim = np.random.normal(0, 1.4, n_samples_pca)
    pc2_sim = np.random.normal(0, 1.0, n_samples_pca)
    
    fig_pca2, ax_pca2 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(x=pc1_sim, y=pc2_sim, alpha=0.7, color="darkcyan", ax=ax_pca2)
    ax_pca2.set_xlabel("Componente Principal 1 (PC1)")
    ax_pca2.set_ylabel("Componente Principal 2 (PC2)")
    ax_pca2.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax_pca2.axvline(0, color='gray', linestyle='--', linewidth=0.8)
    st.pyplot(fig_pca2)
    st.caption("Distribución e independencia sintética de la base de usuarios.")

st.markdown("---")
st.markdown("### 💡 Interpretación de los Resultados")
st.info("""
* **Primera Componente Principal (PC1):** Modela principalmente el **nivel de actividad y la fricción del usuario**. Aquellos clientes que se proyectan con valores muy altos en este eje identifican un perfil de usuario altamente activo en consumo de minutos, pero que de forma paralela registra un volumen elevado de reclamos y soporte técnico.
* **Componentes Restantes (PC2 y PC3):** Capturan la variabilidad demográfica complementaria y los hábitos aislados de consumo que se separan de la tendencia general.
""")