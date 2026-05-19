from integrador import ProcessadorAPI
from limpiador import LimpiadorCSV
import pandas as pd
from pathlib import Path


def ejecutar_automatizacion():
    url_api = "https://jsonplaceholder.typicode.com/users"
    RUTA_PROYECTO = Path(__file__).parent.resolve()
    carpeta_destino = RUTA_PROYECTO /"entrada"
    archivo_csv =  carpeta_destino / "usuarios_api.csv"

    Path(carpeta_destino).mkdir(exist_ok=True)

    extractor = ProcessadorAPI(url_api)
    datos_df = extractor.crear_reporte()

    datos_df.to_csv(archivo_csv, index = False)
    print(f"Archivo guardado con éxito en: {archivo_csv}")

    limpiador = LimpiadorCSV(str(carpeta_destino))
    limpiador.ProcesarDatos()

if __name__ == "__main__":
    ejecutar_automatizacion()