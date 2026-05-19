import pandas as pd
import os

class MotorObras:
    def __init__(self, nombre_obra):
        self.ruta_obra = os.path.join("data", nombre_obra)
        
    def buscar_archivo(self, palabra_clave):
        """Busca cualquier archivo que contenga la palabra clave en su nombre."""
        for archivo in os.listdir(self.ruta_obra):
            if palabra_clave.lower() in archivo.lower() and archivo.endswith(('.xls', '.xlsx')):
                return os.path.join(self.ruta_obra, archivo)
        return None

    def cargar_presupuesto(self):
        ruta = self.buscar_archivo("presupuesto")
        if ruta:
            # skiprows=4 es un estándar, pero lo puedes cambiar si tus archivos varían
            df = pd.read_excel(ruta, skiprows=4)
            df.columns = [str(c).lower().replace(" ", "_") for c in df.columns]
            return df
        return None