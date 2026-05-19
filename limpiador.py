import pandas as pd
import logging
from pathlib import Path

class LimpiadorCSV:
    def __init__(self, entrada):
        
        logging.basicConfig(filename='registro.log', encoding='utf-8', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def ProcesarDatos(self):
        archivos_csv = list(Path("entrada").glob("*.csv"))
        if not archivos_csv:
            logging.warning("No se encontró ningún archivo .csv")
            return
        logging.info(f"Se encontraron {len(archivos_csv)} archivos .csv")

        for entrada in archivos_csv:
            try:
                df = pd.read_csv(entrada)
                logging.info(f"Archivo procesado exitosamente: {entrada.name}")
            except Exception as e:
                logging.error(f"Error procesando {entrada}: {e}")

mi_robot = LimpiadorCSV(entrada="Entrada")
mi_robot.ProcesarDatos()