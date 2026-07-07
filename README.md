# 🎬 Plataforma de Streaming: Análisis y Modelado de Usuarios

## Información general
- **Carrera**: Tecnicatura en Ciencia de Datos e Inteligencia Artificial - Turno Tarde - Sede Nodo
- **Integrantes:**
  - Integrante 1 : Jorge Leandro Isaac
  - Integrante 2 : Luis Lorenzo
  
- **Enlace a la app** [🔗 Acceder a la aplicación en Streamlit Cloud](https://isaacjorgeleandro0-bot-pi-mineria-datos-1-apphome-hofsum.streamlit.app/)

---

## Objetivo del proyecto
El propósito de este proyecto es diseñar e implementar un pipeline analítico e integral de ciencia de datos sobre el comportamiento de una base de usuarios de streaming. El objetivo central radica en transformar un conjunto de datos bruto y altamente ruidoso en un activo de información de alta confianza, estructurado y optimizado para el modelado analítico. A través de este proceso se busca identificar de manera fundamentada los perfiles críticos de clientes en riesgo de abandono (*churn*), descubrir patrones de interacción de variables latentes y condensar la dimensionalidad de los atributos operativos del servicio para guiar de forma eficiente futuras estrategias de retención y la toma de decisiones estratégicas del negocio.

---

## Dataset
El proyecto toma como fuente analítica el archivo original `streaming_users_dirty.json`. Este conjunto de datos registra el volumen histórico de interacciones de los clientes de la plataforma e incluye atributos demográficos de los usuarios, variables cualitativas asociadas a sus preferencias internas de catálogo y métricas continuas vinculadas al consumo mensual del servicio y la generación de reclamos técnicos. En su estado crudo, la fuente de información presentaba severos fallos de integridad distributiva, caracterizados por la presencia de registros duplicados, brechas de información con múltiples valores faltantes distribuidos en variables clave y distorsiones por valores atípicos fuera de los rangos lógicos del comportamiento humano y operativo.

---

## Estructura del repositorio
La organización de los recursos técnicos y la evidencia del proyecto se estructuran de la siguiente manera:
- `app/`: Carpeta contenedora del código fuente de la interfaz web multipágina.
  - `Home.py`: Archivo de entrada principal y marco de presentación de la aplicación.
  - `pages/`: Módulos independientes correspondientes a las secciones del flujo analítico.
    - `01_Dataset.py`: Resumen técnico del estado inicial y transformaciones aplicadas.
    - `02_EDA.py`: Dashboard con las 5 visualizaciones e interpretaciones obligatorias.
    - `03_PCA.py`: Explicación y proyección de la reducción dimensional.
    - `04_Conclusiones.py`: Hallazgos estratégicos, limitaciones y próximos pasos.
- `data/`: Directorio local destinado al almacenamiento de los datos bajo análisis.
- `logs/`: Registros históricos de auditoría de las ejecuciones del pipeline de datos.
- `notebooks/`: Archivos Jupyter (.ipynb) con la experimentación y evidencia metodológica paso a paso.
- `.gitignore`: Archivo de configuración para omitir la sincronización de archivos locales o pesados.
- `README.md`: Documentación principal y descripción del proyecto.
- `requirements.txt`: Lista de dependencias y librerías necesarias para el despliegue del entorno.

---

## Preparación y calidad de datos
El tratamiento de la calidad y la ingeniería de características se encuentra documentado minuciosamente en los archivos `notebooks/01_inspeccion_inicial.ipynb` y `notebooks/02_calidad_y_limpieza.ipynb`. El proceso inició con la depuración de los registros duplicados para evitar sesgos analíticos. Para las variables categóricas, se aplicaron técnicas de normalización de cadenas de texto y mapeos correctivos mediante diccionarios para unificar las inconsistencias ortográficas detectadas en los nombres de las suscripciones y países. Las falsas cadenas de texto nulo se transformaron a tipos reconocibles de Python, mientras que las brechas en variables críticas se resolvieron aplicando imputaciones justificadas según sus respectivas tendencias estadísticas centrales. Finalmente, se controlaron los valores anómalos y extremos imposibles mediante técnicas estructuradas de *capping*, sustituyéndolos por topes lógicos y medidas estadísticas coherentes. El resultado consolidado de esta etapa analítica quedó auditado de forma automática en el archivo de registro histórico de ejecución (log ETL).

---

## Resumen del análisis exploratorio
Los experimentos y gráficos analíticos desarrollados en el archivo `notebooks/03_eda.ipynb` exponen la dinámica de consumo de la plataforma. El análisis univariado del tiempo de reproducción describe el perfil general de engagement de la masa crítica de clientes. El análisis bivariado permitió descubrir la distribución de adopción de los planes comerciales y su relación directa con los niveles de fricción operativa medidos a través de la demanda de soporte técnico. El hallazgo metodológico más relevante surge de la interacción multivariable detallada en el informe del proyecto: al cruzar simultáneamente el consumo con las categorías de edad y tipo de suscripción, se detectó una sinergia decreciente conforme avanza la edad en el plan económico. Este segmento de usuarios presenta los niveles de reproducción más deprimidos, configurando un claro perfil "fantasma" propenso a la cancelación, lo que contrasta de forma absoluta con el comportamiento del plan de alta gama.

---

## Reducción de dimensionalidad
El modelado matemático para la reducción de variables continuas correlacionadas se detalla en el archivo `notebooks/04_pca.ipynb`. Se seleccionaron los atributos cuantitativos del usuario vinculados a la edad, minutos mensuales consumidos y cantidad de reclamos técnicos. Como preprocesamiento mandatorio, se aplicó una estandarización para centrar las variables con media cero y varianza unitaria, evitando que las diferencias de magnitud entre las variables continuas sesgaran los cálculos de los autovalores. El Análisis de Componentes Principales (PCA) resumió la variabilidad en componentes ortogonales e independientes. La Primera Componente Principal (PC1) logró modelar eficientemente una dimensión latente que describe de forma conjunta el nivel de actividad y la fricción operativa, permitiendo mapear con precisión a los usuarios que generan un alto consumo pero que simultáneamente demandan un soporte técnico constante.

---

## Visualización interactiva
Los resultados analíticos, las métricas del procesamiento de calidad y la síntesis visual de las interacciones de este proyecto se encuentran completamente integrados en la aplicación web multipágina desarrollada. Esta interfaz se encarga de traducir la evidencia técnica de los notebooks en una comunicación dinámica apta para el público general, sirviendo como plataforma de validación para los hallazgos explicados en el informe técnico.
- **Enlace de acceso a la producción:** [🔗 Ver Tablero en Streamlit Cloud](https://tu-app-de-streaming.streamlit.app/)

---

## Cómo ejecutar localmente
Para ejecutar la aplicación interactiva de forma local en tu computadora, asegurate de tener Python instalado y seguí estos breves pasos en tu terminal:

1. **Clonar el repositorio** y posicionarte dentro de la carpeta raíz del proyecto:
   ```bash
   cd proyecto_final_md

