from pathlib import Path
import logging
import pandas as pd
import requests

class ProcessadorAPI:
    def __init__(self, url):
        self.url = url
        pass

    def obtener_datos(self):
        try:
            response = requests.get(self.url)
            resp_json = response.json()
            return resp_json
        except Exception as e:
            print(f"Error de conexión: {e}")
            return[]
    def crear_reporte(self):
        datos = self.obtener_datos()
        if not datos:
            print("No hay datos que procesar.")
            return
        df = pd.DataFrame(datos)
        columnas = df[["id", "name", "email"]]
        print(columnas)

integrador = ProcessadorAPI("https://jsonplaceholder.typicode.com/users")
integrador.crear_reporte()