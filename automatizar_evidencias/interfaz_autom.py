from datetime import datetime
from typing import Dict, Any
import tkinter as tk
from tkinter import ttk, scrolledtext,filedialog, simpledialog, messagebox
import os
from reports.report_generator import ReportGenerator
from capture_logic import capture_screen_region
from PIL import Image, ImageTk
from control_version import VersionManager
import json
import uuid
from functools import partial
class AutocompleteCombobox(ttk.Combobox):
    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list, key=str.lower)
        self._current_value = ""
        self["values"] = self._completion_list
        self.bind("<KeyRelease>", self._on_keyrelease)
        self.bind("<FocusOut>", self._on_focus_out)

    def _on_keyrelease(self, event):
        if event.keysym in ("Return", "Escape", "Tab"):
            return

        current_text = self.get()
        if current_text == "":
            self["values"] = self._completion_list
        else:
            filtered = [item for item in self._completion_list if current_text.lower() in item.lower()]
            self["values"] = filtered

        self._current_value = current_text
        self.icursor(tk.END)  # mantener cursor al final

        # Mostrar el dropdown sin seleccionar nada
        self.after(0, self._open_dropdown)

    def _open_dropdown(self):
        if self._current_value:
            self.event_generate("<Down>")  # muestra el desplegable

    def _on_focus_out(self, event):
        self._current_value = ""
 
class ReportEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Reporte QA")
        self.root.geometry("732x900")
        self.root.minsize(720, 800)


        self.version_manager = VersionManager()
        self.version_id = None
        self.reporte = None
        self.namearchivo = ""
        self.nombre_proyecto_var = ""

        # Crear el contenedor principal
        self.main_frame = tk.Frame(self.root, bg="#F0F0F0")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.selector_frame = None
        self.interface_frame = None

        self.init_selector_ui()

    def init_selector_ui(self):

        if self.selector_frame:
            self.selector_frame.destroy()

        self.selector_frame = tk.Frame(self.main_frame, bg="#F0F0F0")
        self.selector_frame.pack(fill=tk.X, pady=10)

        # Botón subir JSON
        btn_subir_json = tk.Button(self.selector_frame, text="📁 Subir JSON", command=self.subir_json)
        btn_subir_json.grid(row=0, column=0, padx=5)

        # Checkbox para nuevo proyecto
        self.is_new_project_var = tk.BooleanVar(value=False)
        self.checkbox_nuevo = tk.Checkbutton(self.selector_frame, text="Nuevo", variable=self.is_new_project_var,
                                            command=self.toggle_new_project_entry)
        self.checkbox_nuevo.grid(row=0, column=1, padx=5)

        # Campo para nombre del proyecto (deshabilitado por defecto)
        self.entry_nombre_proyecto = tk.Entry(self.selector_frame, font=("Verdana", 10), width=25, state="disabled")
        self.entry_nombre_proyecto.grid(row=0, column=2, padx=5)

        # Botón Crear
        self.btn_crear_proyecto = tk.Button(self.selector_frame, text="Crear", command=self.crear_nuevo_proyecto)
        self.btn_crear_proyecto.grid(row=0, column=3, padx=5)
        self.btn_crear_proyecto.grid_remove()

        # Combo para seleccionar proyectos existentes
        self.proyecto_seleccionado = tk.StringVar()
        self.combo_jsons = AutocompleteCombobox(self.selector_frame, textvariable=self.proyecto_seleccionado, width=35)
        self.combo_jsons.set_completion_list(self.version_manager.get_project_display_names())
        project_list = self.version_manager.get_project_display_names()
        self.combo_jsons.set_completion_list(project_list)
        self.combo_jsons.grid(row=0, column=4, padx=5)
        self.combo_jsons.bind("<<ComboboxSelected>>", self.cargar_desde_excel)
        self.toggle_new_project_entry()
        
    def toggle_new_project_entry(self):
        if self.is_new_project_var.get():
            self.entry_nombre_proyecto.grid()
            self.btn_crear_proyecto.grid()
            self.combo_jsons.grid_remove()
            self.entry_nombre_proyecto.config(state="normal")  # ✅ permitir escribir
        else:
            self.entry_nombre_proyecto.grid_remove()
            self.btn_crear_proyecto.grid_remove()
            self.combo_jsons.grid()
            self.entry_nombre_proyecto.config(state="disabled")  # por si ya estaba visible



    def mostrar_editor(self):
        self.clear_editor()

        if self.interface_frame:
            self.interface_frame.destroy()

        self.interface_frame = tk.Frame(self.main_frame, bg="#F0F0F0")
        self.interface_frame.pack(fill=tk.BOTH, expand=True)

        self.create_interface(parent=self.interface_frame)

    def crear_nuevo_proyecto(self):
        nombre = self.entry_nombre_proyecto.get().strip()

        if not nombre:
            messagebox.showwarning("Advertencia", "Debes ingresar un nombre de proyecto.")
            return

        # Establecer nombre en el reporte base
        self.reporte = self.version_manager.generar_reporte_base(nombre)

        # Guardar y actualizar UUID
        self.version_manager.save_version(self.reporte)
        self.version_id = self.version_manager.version_id

        # 🟢 Actualizar lista de proyectos en el combo
        self.combo_jsons.set_completion_list(self.version_manager.get_project_display_names())

        # Limpiar y mostrar editor
        self.clear_editor()
        self.mostrar_editor()


    def subir_json(self):
        if self.reporte:
            self.version_manager.save_version(self.reporte)

        path = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        if not path:
            return

        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        nombre = data.get("DATOS_GENERALES", {}).get("Nombre_del_Proyecto", "Proyecto_Desconocido")

        # ✅ Deshabilitar porque se cargó un JSON
        self.entry_nombre_proyecto.config(state="disabled")

        self.reporte = self.version_manager.cargar_json_externo(path, nombre)
        self.version_id = self.version_manager.version_id
        self.mostrar_editor()

        return data

    def cargar_desde_excel(self, event):
        nombre_seleccionado = self.proyecto_seleccionado.get()

        if not nombre_seleccionado:
            return

        # Extraer solo el nombre del proyecto (antes del guion)
        nombre_proyecto = nombre_seleccionado.split(" - ")[0].strip()

        # Cargar el JSON correspondiente desde Excel
        self.reporte = self.version_manager.obtener_reporte_por_nombre(nombre_proyecto)
        self.version_id = self.version_manager.version_id

        self.clear_editor()
        self.mostrar_editor()


    def create_interface(self, parent=None):
        if parent is None:
            parent = self.main_frame

        main_frame = tk.Frame(parent, bg="#F0F0F0")
        main_frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(main_frame, bg="#F0F0F0")
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        scrollable_frame = tk.Frame(canvas, bg="#F0F0F0")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # ✅ Scroll con mouse
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)       # Windows
        canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux scroll up
        canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # Linux scroll down

        # Secciones
        self.create_section(scrollable_frame, "DATOS GENERALES", self.create_general_section, self.reporte["DATOS_GENERALES"])
        self.create_section(scrollable_frame, "DATOS DEL STREAM", self.create_general_section, self.reporte["DATOS_DEL_STREAM"])
        self.create_section(scrollable_frame, "ALCANCE DE LA PRUEBA", self.create_text_section, "ALCANCE_DE_LA_PRUEBA")
        self.create_section(scrollable_frame, "PRUEBAS FUNCIONALES", self.create_functional_tests_section)
        self.create_section(scrollable_frame, "PRUEBAS NO FUNCIONALES", self.create_non_functional_tests_section)


    def create_section(self, parent_frame, title, content_func, data=None):
        frame = tk.Frame(parent_frame, bg="#F0F0F0", bd=1, relief=tk.RAISED)
        frame.pack(fill=tk.X, pady=5, padx=10)

        label = tk.Label(frame, text=title, font=("Verdana", 12, "bold"), bg="#D3D3D3")
        label.pack(fill=tk.X)

        if data:
            content_func(frame, data)
        else:
            content_func(frame)

    def create_text_section(self, frame, key):
        text_frame = tk.Frame(frame, bg="#F0F0F0")
        text_frame.pack(fill=tk.X, padx=10, pady=2)

        # Caja de texto con scroll
        text_widget = scrolledtext.ScrolledText(text_frame, font=("Verdana", 10), width=50, height=6, fg="black", bg="#CCFFCC")
        text_widget.insert("1.0", self.get_data_from_key(key))
        text_widget.pack(fill=tk.X, expand=True)
        text_widget.bind("<KeyRelease>", lambda e, w=text_widget: self.mark_as_modified(w))

        # Botón para guardar el contenido de la caja de texto
        save_button = tk.Button(frame, text="Guardar", bg="#FFB347",
                                command=lambda: self.save_text(text_widget, key))
        save_button.pack(pady=5)

    def create_functional_tests_section(self, frame):
        self.functionals_frame = frame
        add_button = tk.Button(frame, text="Añadir Caso de Prueba", bg="#FFB347", font=("Verdana", 10, "bold"),
                               command=lambda: self.add_functional_test(frame))
        add_button.pack(pady=5)

        for case_data in self.reporte["DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA"]["PRUEBAS_FUNCIONALES"]:
            self.display_case(frame, case_data)

    def add_functional_test(self, frame):
        existing_ids = [c.get("id_caso", 0) for c in self.reporte["DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA"]["PRUEBAS_FUNCIONALES"]]
        next_id = max(existing_ids, default=0) + 1

        new_case = {
            "id_caso": next_id,
            "Caso_de_Prueba": f"CP{len(self.reporte['DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA']['PRUEBAS_FUNCIONALES']) + 1} - Prueba Funcional",
            "Escenario_de_Prueba": "Escenario Nuevo",
            "ID_Compartamos": "123456789",
            "Tipo_Billetera": "Billetera Digital",
            "Numero_Billetera_Origen": "51960287153",
            "Numero_Billetera_Destino": "51991022660",
            "ID_Operacion": "8502502201439266660484",
            "Definicion_Caso": "Definición del caso de prueba",
            "Resultado_Esperado": "Resultado esperado",
            "Tipo_Prueba": "Prueba Funcional",
            "Fecha": datetime.now().strftime("%d/%m/%Y"),
            "Hora": datetime.now().strftime("%H:%M"),
            "Flujo": []
        }

        self.reporte["DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA"]["PRUEBAS_FUNCIONALES"].append(new_case)
        self.generar_documento()
        self.display_case(frame, new_case)

    def create_general_section(self, frame, data):
        for key, value in data.items():
            entry_frame = tk.Frame(frame, bg="#F0F0F0")
            entry_frame.pack(fill=tk.X, padx=10, pady=2)

            label = tk.Label(entry_frame, text=key, font=("Verdana", 10, "bold"), anchor="w", width=20, bg="#D3D3D3")
            label.pack(side=tk.LEFT)

            entry = tk.Entry(entry_frame, font=("Verdana", 10), width=30, fg="black", bg="#CCFFCC")  # Verde al cargar
            entry.insert(0, value)
            entry.pack(side=tk.LEFT, padx=5)
            entry.bind("<KeyRelease>", lambda e, ent=entry: ent.config(bg="#FFE4B5"))  # Amarillo al editar

            save_button = tk.Button(entry_frame, text="Guardar", bg="#FFB347",
                                    command=lambda e=entry, k=key, d=data: self.save_entry(e, k, d))
            save_button.pack(side=tk.LEFT, padx=5)

    def display_case(self, frame, case_data):
        case_frame = tk.Frame(frame, bg="#F0F0F0", bd=1, relief=tk.RAISED)
        case_frame.pack(fill=tk.X, padx=10, pady=5)

        label = tk.Label(case_frame, text=f"Caso {case_data.get('id_caso', '')}: {case_data.get('Caso_de_Prueba', '')}", font=("Verdana", 10, "bold"))
        label.pack()

        for key, value in case_data.items():
            if key == "Flujo":
                continue  # el flujo se maneja aparte

            entry_frame = tk.Frame(case_frame, bg="#F0F0F0")
            entry_frame.pack(fill=tk.X, padx=5, pady=1)

            label = tk.Label(entry_frame, text=key, font=("Verdana", 9, "bold"), width=25, anchor="w", bg="#D3D3D3")
            label.pack(side=tk.LEFT)

            # Campo no editable para id_caso
            if key == "id_caso":
                entry = tk.Label(entry_frame, text=str(value), font=("Verdana", 10), bg="#F0F0F0")
                entry.pack(side=tk.LEFT)
            else:
                entry = tk.Entry(entry_frame, font=("Verdana", 10), width=40, fg="black", bg="#CCFFCC")  # verde al inicio
                entry.insert(0, value)
                entry.pack(side=tk.LEFT, padx=5)

                # Pintar de amarillo al editar
                entry.bind("<KeyRelease>", lambda e, ent=entry: ent.config(bg="#FFE4B5"))

                # Botón para guardar y pintar de verde
                save_btn = tk.Button(
                    entry_frame,
                    text="Guardar",
                    bg="#FFB347",
                    font=("Verdana", 8),
                    command=partial(self._guardar_y_colorear, entry, key, case_data)
                )
                save_btn.pack(side=tk.LEFT, padx=5)
        # Mostrar el flujo
        self.create_flows_section(case_frame, case_data)


    def _guardar_y_colorear(self, entry_widget, key, case_data):
        nuevo_valor = entry_widget.get()
        case_data[key] = nuevo_valor
        entry_widget.config(bg="#CCFFCC")
        self.generar_documento()



    def create_flows_section(self, frame, case_data):
        flow_frame = tk.Frame(frame, bg="#F0F0F0", bd=1, relief=tk.RAISED)
        flow_frame.pack(fill=tk.X, padx=10, pady=5)

        flow_label = tk.Label(flow_frame, text="Flujo", font=("Verdana", 10, "bold"), bg="#D3D3D3")
        flow_label.pack(fill=tk.X)

        add_step_button = tk.Button(flow_frame, text="Añadir Paso", bg="#FFB347", font=("Verdana", 10),
                                    command=lambda: self.add_flow_step(flow_frame, case_data))
        add_step_button.pack(pady=5)

        for step in case_data["Flujo"]:
            self.display_flow_step(flow_frame, step, case_data)

    def add_flow_step(self, frame, case_data):
        new_step = {
            "Paso": f"Paso {len(case_data['Flujo']) + 1}",
            "Foto": ""
        }
        case_data["Flujo"].append(new_step)
        self.display_flow_step(frame, new_step,case_data)
        self.generar_documento()

    def display_flow_step(self, frame, step_data,case_data):
        step_frame = tk.Frame(frame, bg="#F0F0F0")
        step_frame.pack(fill=tk.X, padx=5, pady=2)

        # Descripción del paso
        paso_label = tk.Entry(step_frame, font=("Verdana", 10), width=30)
        paso_label.insert(0, step_data["Paso"])
        paso_label.pack(side=tk.LEFT, padx=5)

        def take_screenshot():
            # Captura la pantalla directamente sin abrir otra ventana
            screenshot = capture_screen_region()  # Ejecuta la captura de pantalla
            if screenshot:
                folder = "automatizar_evidencias/screenshots"
                os.makedirs(folder, exist_ok=True)
                uuid_corto = self.version_id#.split("-")[0]
                id_caso = case_data.get("id_caso", "X")
                paso = step_data['Paso'].replace(" ", "_")[:30]
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                file_name = f"{folder}/{uuid_corto}_{id_caso}_{paso}_{timestamp}.png"
                            
                screenshot.save(file_name)  # Guarda la imagen capturada

                # Asegúrate de que 'Foto' sea una lista para cada paso
                if "Foto" not in step_data or not isinstance(step_data["Foto"], list):
                    step_data["Foto"] = []
                
                step_data["Foto"].append(file_name)  # Agrega la nueva imagen a la lista de fotos

                self.generar_documento()  # Actualiza el documento
                self.display_screenshot(step_frame, file_name)  # Muestra la imagen en la interfaz

        # Botón para capturar la pantalla
        capture_button = tk.Button(step_frame, text="Capturar", bg="#FFB347", font=("Verdana", 8), command=take_screenshot)
        capture_button.pack(side=tk.LEFT, padx=5)

        # Mostrar imagen si ya existe
        if step_data["Foto"]:
            self.display_screenshot(step_frame, step_data["Foto"])


    def display_screenshot(self, frame, file_name):
        try:
            image = Image.open(file_name)
            image.thumbnail((100, 100))
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(frame, image=photo)
            label.image = photo
            label.pack(side=tk.LEFT, padx=5)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

    def mark_as_modified(self, widget):
        widget.config(bg="#FFCC99")

    def save_entry(self, entry_widget, key, case_data):
        nuevo_valor = entry_widget.get()
        case_data[key] = nuevo_valor
        entry_widget.config(bg="#CCFFCC")  # Verde al guardar
        self.generar_documento()


    def save_case(self, case_data, description):
        case_data["Descripcion"] = description.get()
        self.version_manager.save_version(self.reporte)
        self.generar_documento()

    def delete_case(self, case_frame, case_data):
        self.reporte["DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA"]["PRUEBAS_FUNCIONALES"].remove(case_data)
        case_frame.destroy()
        self.generar_documento()

    def save_text(self, text_widget, key):
        text_content = text_widget.get("1.0", tk.END).strip()
        self.update_data_by_key(key, text_content)
        text_widget.config(bg="#C6FFAD")
        self.version_manager.save_version(self.reporte)
        self.generar_documento()

    def create_non_functional_tests_section(self, frame):
        no_func_data = self.reporte["DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA"]["PRUEBAS_NO_FUNCIONALES"]
        
        for key, value in no_func_data.items():
            subframe = tk.Frame(frame, bg="#F0F0F0")
            subframe.pack(fill=tk.X, padx=10, pady=2)

            label = tk.Label(subframe, text=key, font=("Verdana", 10, "bold"), anchor="w", bg="#D3D3D3")
            label.pack(fill=tk.X)
            
            text_widget = scrolledtext.ScrolledText(subframe, font=("Verdana", 10), width=50, height=6, fg="black", bg="#CCFFCC")
            text_widget.insert("1.0", value)
            text_widget.pack(fill=tk.X, expand=True)
            text_widget.bind("<KeyRelease>", lambda e: text_widget.config(bg="#FFE4B5"))            
            save_button = tk.Button(subframe, text="Guardar", bg="#FFB347",
                                    command=lambda w=text_widget, k=key: self.save_non_functional_test(w, k))
            save_button.pack(pady=5)

    def save_non_functional_test(self, text_widget, key):
        content = text_widget.get("1.0", tk.END).strip()
        self.reporte["DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA"]["PRUEBAS_NO_FUNCIONALES"][key] = content
        text_widget.config(bg="#C6FFAD")
        self.version_manager.save_version(self.reporte)
        self.generar_documento()

    def generar_documento(self):
        report = ReportGenerator()
        report.add_header()
        report.add_title("DATOS GENERALES")
        general_data = self.reporte["DATOS_GENERALES"]

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
        
        pruebas_funcionales = self.reporte["DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA"]["PRUEBAS_FUNCIONALES"]
        if pruebas_funcionales:
            report.add_title("PRUEBAS FUNCIONALES", level=2)
            
            for caso in pruebas_funcionales:
                # Procesar el flujo y acumular contenido si ya existe
                flujo_paragraph_content = []  # Crear un contenedor para los pasos y las imágenes

                if "Flujo" in caso and caso["Flujo"]:
                    for step in caso["Flujo"]:
                        # Añadir descripción del paso
                        flujo_paragraph_content.append({"tipo": "texto", "contenido": f"Paso: {step['Paso']}"})
                        
                        # Si existen imágenes en el paso (lista)
                        if isinstance(step["Foto"], list):
                            for foto in step["Foto"]:
                                flujo_paragraph_content.append({"tipo": "imagen", "ruta": foto})
                        elif isinstance(step["Foto"], str):
                            flujo_paragraph_content.append({"tipo": "imagen", "ruta": step["Foto"]})

                # Generar la tabla del caso
                report.create_table_functional_test(
                    caso_de_prueba=caso.get("Caso_de_Prueba", ""),
                    escenario_de_prueba=caso.get("Escenario_de_Prueba", ""),
                    id_compartamos=caso.get("ID_Compartamos", ""),
                    tipo_billetera=caso.get("Tipo_Billetera", ""),
                    numero_billetera_origen=caso.get("Numero_Billetera_Origen", ""),
                    numero_billetera_destino=caso.get("Numero_Billetera_Destino", ""),
                    id_operacion=caso.get("ID_Operacion", ""),
                    definicion_caso=caso.get("Definicion_Caso", ""),
                    resultado_esperado=caso.get("Resultado_Esperado", ""),
                    tipo_prueba=caso.get("Tipo_Prueba", ""),
                    flujo_basico=f"<Flujo_{caso.get('Caso_de_Prueba', '')}>",
                    log="<Log>",
                    fecha=caso.get("Fecha", ""),
                    hora=caso.get("Hora", "")
                )

                # 🔥 Acumular contenido usando el marcador específico
                report.add_content_in_cell(f"<Flujo_{caso.get('Caso_de_Prueba', '')}>", flujo_paragraph_content)
        report.add_title("PRUEBAS NO FUNCIONALES", level=2)
        no_func_data = self.reporte["DETALLE_DE_LA_EJECUCIÓN_DE_LA_PRUEBA"]["PRUEBAS_NO_FUNCIONALES"]
        for key, value in no_func_data.items():
            report.add_title(str(key), level=3)
            report.add_paragraph(f"{value}")

        # Guardar el documento en la carpeta especificada
        output_folder = "automatizar_evidencias/reports/documento_funcional"
        os.makedirs(output_folder, exist_ok=True)
        nombre_proyecto = self.reporte["DATOS_GENERALES"]["Nombre_del_Proyecto"]
        self.namearchivo = os.path.join(
            output_folder,
            f"PDP_005_Evidencias de Prueba_v1.1 {nombre_proyecto}.docx"
        )

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

    def get_estructura_base(self) -> Dict[str, Any]:
        return {
            "UUID": "",  # ← se llenará al crear o cargar proyecto
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
                "PRUEBAS_FUNCIONALES": [],
                "PRUEBAS_NO_FUNCIONALES": {
                    "Observaciones Reportadas": "<Observaciones>",
                    "Conclusión": "<Conclusión>",
                    "Recomendaciones": "<Recomendaciones>"
                }
            }
        }

    def seleccionar_o_crear_json(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Seleccionar o Crear Proyecto")
        ventana.geometry("400x250")
        ventana.grab_set()

        resultado = {"path": None, "uuid": None}

        def cargar_existente():
            path = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
            if not path:
                return

            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                if not isinstance(data, dict) or "DATOS_GENERALES" not in data:
                    raise ValueError("JSON inválido")

                self.reporte = data
                resultado["path"] = path
                resultado["uuid"] = data.get("UUID", str(uuid.uuid4()))

                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar JSON:\n{e}")

        def crear_nuevo():
            nombre = entry_nombre.get().strip()
            if not nombre:
                messagebox.showwarning("Falta nombre", "Ingrese el nombre del proyecto")
                return

            resultado["uuid"] = str(uuid.uuid4())
            self.reporte = self.get_estructura_base()
            self.reporte["DATOS_GENERALES"]["Nombre_del_Proyecto"] = nombre
            self.reporte["UUID"] = resultado["uuid"]
            resultado["path"] = os.path.join("automatizar_evidencias/versions/jsons", f"{nombre}.json")

            ventana.destroy()

        # Etiqueta y campo
        tk.Label(ventana, text="Nombre del nuevo proyecto:").pack(pady=5)
        entry_nombre = tk.Entry(ventana, width=40)
        entry_nombre.pack(pady=5)

        # Botones
        tk.Button(ventana, text="Cargar JSON Existente", command=cargar_existente).pack(pady=5)
        tk.Button(ventana, text="Crear Nuevo Proyecto", command=crear_nuevo).pack(pady=5)
        tk.Button(ventana, text="Cancelar", command=ventana.destroy).pack(pady=5)

        self.root.wait_window(ventana)

        if resultado["path"] and resultado["uuid"]:
            return resultado["path"], resultado["uuid"]
        else:
            return None
        
    def clear_editor(self):
        """Borra todo el contenido actual de la interfaz (editor de secciones)."""
        if self.interface_frame:
            self.interface_frame.destroy()
            self.interface_frame = None

        # También eliminar todas las secciones anteriores que puedan estar en main_frame
        for widget in self.main_frame.winfo_children():
            if widget != self.selector_frame:  # No borres el selector de JSON y nombre
                widget.destroy()

    
if __name__ == "__main__":
    root = tk.Tk()
    app = ReportEditorApp(root)  # Esto internamente llama seleccionar_o_crear_json y todo el flujo
    root.mainloop()