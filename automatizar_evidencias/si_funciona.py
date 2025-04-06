from datetime import datetime
from typing import Dict, Any
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import os
from reports.report_generator import ReportGenerator


class ReportEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Reporte QA")
        self.root.geometry('500x700')  # Tamaño inicial fijo
        self.root.minsize(500, 200)  # Tamaño mínimo permitido
        self.namearchivo = None

        # 📌 Definir la estructura base del reporte
        self.reporte: Dict[str, Any] = {
            "DATOS_GENERALES": {
                "Nombre_del_Proyecto": "<nombre_proyecto>",
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
                "PRUEBAS_FUNCIONALES": "<Pruebas Funcionales>",
                "PRUEBAS_NO_FUNCIONALES": {
                    "Observaciones Reportadas": "<Observaciones>",
                    "Conclusión": "<Conclusión>",
                    "Recomendaciones": "<Recomendaciones>"
                }
            }
        }

        self.entries = {}
        self.create_interface()

    def create_interface(self):
        main_frame = tk.Frame(self.root, bg="#F0F0F0")
        main_frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(main_frame, bg="#F0F0F0")
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollable_frame = tk.Frame(canvas, bg="#F0F0F0")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.root.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        self.create_general_section(scrollable_frame, "DATOS GENERALES", self.reporte["DATOS_GENERALES"])
        self.create_general_section(scrollable_frame, "DATOS DEL STREAM", self.reporte["DATOS_DEL_STREAM"])
        self.create_text_section(scrollable_frame, "ALCANCE DE LA PRUEBA", "ALCANCE_DE_LA_PRUEBA")
        self.create_functional_tests_section(scrollable_frame)
        self.create_non_functional_tests_section(scrollable_frame)

    def create_general_section(self, frame, section_name, data):
        label = tk.Label(frame, text=section_name, font=("Verdana", 12, "bold"), bg="#D3D3D3")
        label.pack(fill=tk.X, pady=5)

        for key, value in data.items():
            entry_frame = tk.Frame(frame, bg="#F0F0F0")
            entry_frame.pack(fill=tk.X, padx=10, pady=2)

            label = tk.Label(entry_frame, text=key, font=("Verdana", 10, "bold"), anchor="w", width=15, bg="#D3D3D3")
            label.pack(side=tk.LEFT)

            entry = tk.Entry(entry_frame, font=("Verdana", 10), width=30, fg="black", bg="#FFE4B5")
            entry.insert(0, value)
            entry.pack(side=tk.LEFT, padx=5)
            entry.bind("<KeyRelease>", lambda e, ent=entry: self.mark_as_modified(ent))

            save_button = tk.Button(entry_frame, text="Guardar", font=("Verdana", 10), bg="#FFB347",
                                    command=lambda e=entry, key=key, d=data: self.save_single_edit(e, key, d))
            save_button.pack(side=tk.LEFT, padx=5)

            self.entries[key] = entry

    def create_text_section(self, frame, section_name, key):
        label = tk.Label(frame, text=section_name, font=("Verdana", 12, "bold"), bg="#D3D3D3")
        label.pack(fill=tk.X, pady=5)

        text_frame = tk.Frame(frame, bg="#F0F0F0")
        text_frame.pack(fill=tk.X, padx=10, pady=2)

        text_widget = scrolledtext.ScrolledText(text_frame, font=("Verdana", 10), width=45, height=4, fg="black", bg="#FFEB99")
        text_widget.insert("1.0", self.get_data_from_key(key))
        text_widget.pack(side=tk.LEFT, fill=tk.X, expand=True)
        text_widget.bind("<KeyRelease>", lambda e, ent=text_widget: self.mark_as_modified(ent))

        save_button = tk.Button(text_frame, text="Guardar", font=("Verdana", 10), bg="#FFB347",
                                command=lambda: self.save_text_edit(text_widget, key))
        save_button.pack(side=tk.LEFT, padx=5)

        self.entries[key] = text_widget

    def create_functional_tests_section(self, frame):
        self.create_text_section(frame, "PRUEBAS FUNCIONALES", "DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA.PRUEBAS_FUNCIONALES")

    def create_non_functional_tests_section(self, frame):
        label = tk.Label(frame, text="PRUEBAS NO FUNCIONALES", font=("Verdana", 12, "bold"), bg="#D3D3D3")
        label.pack(fill=tk.X, pady=5)

        for key in self.reporte["DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA"]["PRUEBAS_NO_FUNCIONALES"].keys():
            self.create_text_section(frame, key,
                                     f"DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA.PRUEBAS_NO_FUNCIONALES.{key}")

    def mark_as_modified(self, widget):
        widget.config(bg="#FFEB99")

    def save_single_edit(self, entry, key, data):
        data[key] = entry.get()
        entry.config(bg="#C6FFAD")
        self.generar_documento()

    def save_text_edit(self, text_widget, key):
        self.update_data_by_key(key, text_widget.get("1.0", tk.END).strip())
        text_widget.config(bg="#C6FFAD")
        self.generar_documento()
    def generar_documento(self):
        report = ReportGenerator()
        report.add_header()
        report.add_title("DATOS GENERALES")
        general_data = self.reporte["DATOS_GENERALES"]

        # Renombrar las claves antes de pasarlas al método
        report.create_table_general_data(
            nombre_proyecto=general_data["Nombre_del_Proyecto"],
            etapa_del_proyecto=general_data["Etapa_del_Proyecto"],
            analista=general_data["Analista_QA"],
            sistema=general_data["Nombre_de_Sistema"],
            fecha=general_data["fecha"]
        )

        report.add_title("DATOS DEL STREAM")
        stream_data = self.reporte["DATOS_DEL_STREAM"]
        report.create_table_stream_data(apk_name=stream_data["Versión_del_APK"])

        report.add_title("ALCANCE DE PRUEBA")
        report.add_paragraph(self.reporte["ALCANCE_DE_LA_PRUEBA"])

        report.add_title("DETALLE DE EJECUCIÓN DE PRUEBAS")
        report.add_title("PRUEBAS FUNCIONALES", level=2)
        report.add_paragraph(self.reporte["DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA"]["PRUEBAS_FUNCIONALES"])

        report.add_title("PRUEBAS_NO_FUNCIONALES", level=2)
        no_func_data = self.reporte["DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA"]["PRUEBAS_NO_FUNCIONALES"]
        for key, value in no_func_data.items():
            report.add_title(str(key), level=3)
            report.add_paragraph(f"{value}")

        output_folder = "automatizar_evidencias/reports/documento_funcional"
        os.makedirs(output_folder, exist_ok=True)
        self.namearchivo = f"{output_folder}/Reporte_Actualizado.docx"
        report.save_document(self.namearchivo)
        print(f"✅ Documento generado en: {self.namearchivo}")
        
    def get_data_from_key(self, key):
        keys = key.split('.')
        data = self.reporte
        for k in keys:
            data = data[k]
        return data

    def update_data_by_key(self, key, value):
        keys = key.split('.')
        data = self.reporte
        for k in keys[:-1]:
            data = data[k]
        data[keys[-1]] = value


if __name__ == "__main__":
    root = tk.Tk()
    app = ReportEditorApp(root)
    root.mainloop()
