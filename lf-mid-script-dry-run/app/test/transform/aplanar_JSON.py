import json
import os

# Cargar el JSON desde un archivo
def cargar_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return json.load(archivo)

# Función para aplanar el JSON y extraer claves y valores
def extraer_claves_y_valores(json_data):
    def aplanar_dict(d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(aplanar_dict(v, new_key, sep=sep).items())
            elif isinstance(v, list):
                # Incluir arreglos, si el arreglo contiene diccionarios, procesar cada diccionario
                if all(isinstance(i, dict) for i in v):
                    for i in v:
                        items.extend(aplanar_dict(i, new_key, sep=sep).items())
                else:
                    # Si el arreglo contiene valores simples, unirlos como una cadena para mostrar en el archivo
                    items.append((new_key, ', '.join(map(str, v))))
            else:
                items.append((new_key, v))
        return dict(items)

    return aplanar_dict(json_data)

# Función para guardar las claves y valores en un archivo de texto tabulado con alineación
def guardar_claves_y_valores_alineados(diccionario, nombre_archivo):
    max_len = max(len(clave) for clave in diccionario)  # Longitud máxima de las claves
    with open(nombre_archivo, 'w') as f:
        for clave, valor in diccionario.items():
            espacios = ' ' * (max_len - len(clave))  # Espacios necesarios para alinear
            f.write(f"{clave}{espacios} \t {valor}\n")

# Cargar y procesar el JSON
json_data = cargar_json('app/test/transform/data.json')
claves_y_valores = extraer_claves_y_valores(json_data)

# Guardar las claves y valores en un archivo de texto alineado
guardar_claves_y_valores_alineados(claves_y_valores, 'app/test/transform/cabeceras_vertical_JSON.txt')

print("Las claves y valores han sido guardados en 'app/test/transform/cabeceras_vertical_JSON.txt'.")
