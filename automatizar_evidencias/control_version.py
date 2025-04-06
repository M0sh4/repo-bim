import os
import uuid
import pandas as pd
from datetime import datetime
from tkinter import ttk, scrolledtext,filedialog, simpledialog, messagebox
import json

VERSION_FILE_PATH = "automatizar_evidencias/versions/version_log.xlsx"
VERSIONS_FOLDER = "automatizar_evidencias/versions/jsons"
os.makedirs(VERSIONS_FOLDER, exist_ok=True)
os.makedirs(os.path.dirname(VERSION_FILE_PATH), exist_ok=True)


class VersionManager:
    def __init__(self):
        self.version_id = str(uuid.uuid4())
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def save_version(self, reporte: dict):
        nombre_proyecto = reporte.get("DATOS_GENERALES", {}).get("Nombre_del_Proyecto", "Proyecto_Desconocido")
        safe_project_name = nombre_proyecto.replace(" ", "_").replace(":", "_").replace("/", "_")
        timestamp_id = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_name = f"{safe_project_name}_{timestamp_id}.json"
        json_path = os.path.join(VERSIONS_FOLDER, file_name)

        # Guardar JSON con el nombre del proyecto y timestamp
        pd.Series(reporte).to_json(json_path, force_ascii=False, indent=4)

        # Actualizar Excel con esta versión
        self._save_to_excel(
            version_id=self.version_id,
            nombre_proyecto=nombre_proyecto,
            file_path=json_path,
            timestamp=self.timestamp,
            timestamp_id=timestamp_id
        )


    def update_version(self, reporte: dict):
        """Actualiza el archivo JSON existente y la entrada en Excel con nueva fecha."""
        json_path = os.path.join(VERSIONS_FOLDER, f"{self.version_id}.json")
        pd.Series(reporte).to_json(json_path, force_ascii=False, indent=4)

        # Actualizar timestamp en Excel
        if os.path.exists(VERSION_FILE_PATH):
            df = pd.read_excel(VERSION_FILE_PATH)
            df.loc[df["version_id"] == self.version_id, "updated_at"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            df.to_excel(VERSION_FILE_PATH, index=False)

    def _save_to_excel(self, version_id: str, nombre_proyecto: str, file_path: str, timestamp: str, timestamp_id: str):
        row = {
            "version_id": version_id,
            "nombre_proyecto": nombre_proyecto,
            "json_path": file_path,
            "created_at": timestamp,
            "updated_at": timestamp,
            "timestamp_id": timestamp_id
        }

        if os.path.exists(VERSION_FILE_PATH):
            df = pd.read_excel(VERSION_FILE_PATH)
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        else:
            df = pd.DataFrame([row])

        df.to_excel(VERSION_FILE_PATH, index=False)



    def load_json(self, nombre_proyecto: str) -> dict:
        json_path = os.path.join(VERSIONS_FOLDER, f"{nombre_proyecto}.json")
        if os.path.exists(json_path):
            return pd.read_json(json_path, typ='series').to_dict()
        else:
            raise FileNotFoundError(f"El JSON {nombre_proyecto}.json no existe.")
        


    def generar_reporte_base(self, nombre_proyecto):
        return {
            "uuid": str(uuid.uuid4()),
            "DATOS_GENERALES": {
                "Nombre_del_Proyecto": nombre_proyecto,
                "Etapa_del_Proyecto": "<etapa_del_proyecto>",
                "Analista_QA": "<analista_qa>",
                "fecha": datetime.now().strftime('%d/%m/%Y'),
                "Nombre_de_Sistema": "<sistema>"
            },
            "DATOS_DEL_STREAM": {
                "Versión_del_APK": "<version_del_apk>"
            },
            "ALCANCE_DE_LA_PRUEBA": "<Parrafo alcance>",
            "DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA": {
                "PRUEBAS_FUNCIONALES": [],
                "PRUEBAS_NO_FUNCIONALES": {
                    "Observaciones Reportadas": "<Observaciones>",
                    "Conclusión": "<Conclusión>",
                    "Recomendaciones": "<Recomendaciones>"
                }
            }
        }

    def get_project_names(self):
        if not os.path.exists(VERSION_FILE_PATH):
            return []

        df = pd.read_excel(VERSION_FILE_PATH)
        return df["nombre_proyecto"].dropna().unique().tolist()


    def cargar_json_externo(self, path_json: str, nombre_proyecto: str):
        # Cargar el contenido del JSON
        with open(path_json, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Generar un nuevo UUID para la sesión
        self.version_id = str(uuid.uuid4())

        # Generar nuevo nombre de archivo con timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        nombre_archivo = f"{nombre_proyecto}_{timestamp}.json"
        destino = os.path.join(VERSIONS_FOLDER, nombre_archivo)

        # Copiar el archivo sin usar shutil
        with open(path_json, 'rb') as origen:
            contenido = origen.read()
        with open(destino, 'wb') as destino_archivo:
            destino_archivo.write(contenido)

        # Registrar en el Excel de versiones
        row = {
            "version_id": self.version_id,
            "json_path": destino,
            "project_name": nombre_proyecto,
            "created_at": timestamp,
            "updated_at": timestamp
        }

        if os.path.exists(VERSION_FILE_PATH):
            df = pd.read_excel(VERSION_FILE_PATH)
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        else:
            df = pd.DataFrame([row])

        df.to_excel(VERSION_FILE_PATH, index=False)

        # Devolver el contenido del JSON para usarlo en la app
        return data

    def obtener_reporte_por_nombre(self, nombre_proyecto: str) -> dict:
        if not os.path.exists(VERSION_FILE_PATH):
            raise FileNotFoundError("No se encuentra el archivo de versiones.")

        df = pd.read_excel(VERSION_FILE_PATH)
        fila = df[df["nombre_proyecto"] == nombre_proyecto].sort_values("created_at", ascending=False).head(1)

        if fila.empty:
            raise ValueError(f"No se encontró el proyecto '{nombre_proyecto}' en el Excel.")

        path_json = fila.iloc[0]["json_path"]
        with open(path_json, "r", encoding="utf-8") as f:
            return json.load(f)
        
    
    def get_project_display_names(self):
        if not os.path.exists(VERSION_FILE_PATH):
            return []

        df = pd.read_excel(VERSION_FILE_PATH)
        df = df.dropna(subset=["nombre_proyecto", "created_at"])

        # Asegurar que la columna 'created_at' sea tipo datetime
        df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
        df = df.dropna(subset=["created_at"])  # Eliminar filas con fechas no válidas

        # Ordenar por fecha descendente
        df = df.sort_values(by="created_at", ascending=False)

        # Devolver lista con formato: Proyecto - Fecha
        return [f"{row['nombre_proyecto']} - {row['created_at'].strftime('%Y-%m-%d %H:%M:%S')}" for _, row in df.iterrows()]
