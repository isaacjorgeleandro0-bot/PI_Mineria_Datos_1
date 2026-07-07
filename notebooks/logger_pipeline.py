import os
import pandas as pd
from datetime import datetime

LOG_FILE = "../logs/pipeline_log.csv"

def registrar_transformacion(notebook_name, paso, dataframe_antes=None, dataframe_despues=None, estado="EXITOSO", error_msg=""):
    """Registra una transformación relevante en el archivo CSV de logs."""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    shape_antes = dataframe_antes.shape if dataframe_antes is not None else None
    shape_despues = dataframe_despues.shape if dataframe_despues is not None else None
    
    nuevo_log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "notebook": notebook_name,
        "transformacion": paso,
        "shape_antes": str(shape_antes),
        "shape_despues": str(shape_despues),
        "estado": estado,
        "error": error_msg
    }
    
    df_log = pd.DataFrame([nuevo_log])
    
    if not os.path.exists(LOG_FILE):
        df_log.to_csv(LOG_FILE, index=False)
    else:
        df_log.to_csv(LOG_FILE, mode='a', header=False, index=False)