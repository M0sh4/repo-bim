def process_json(json_data, parent_node_id=None, level=1, start_id=[1]):
    result = []
    id_json_api = 5  # Cambia esto según el ID de tu API

    # Mapa de tipos de datos
    json_type_map = {
        str: 1,    # String
        int: 2,    # Number
        float: 6,  # Float
        dict: 3,   # Object
        list: 4,   # Array
        type(None): 1  # Null o None lo asignamos como String para simplificar
    }

    # Función interna para manejar los nodos
    def add_node(key, value, parent_id, node_level):
        id_json_type = json_type_map[type(value)]  # Obtener tipo de dato
        node_value = None if value == '' else str(value) if value is not None else None
        # Agregar el ID del nodo al inicio de la tupla
        result.append((start_id[0], id_json_api, key, node_value, parent_id, node_level, id_json_type))
        start_id[0] += 1  # Incrementar el ID del nodo

    # Recorrer el JSON
    for key, value in json_data.items():
        if isinstance(value, dict):  # Si el valor es un objeto (dict)
            add_node(key, None, parent_node_id, level)  # Nodo padre con valor None
            child_nodes = process_json(value, start_id=start_id, parent_node_id=start_id[0] - 1, level=level + 1)  # Procesar el objeto anidado
            result.extend(child_nodes)
        elif isinstance(value, list):  # Si el valor es un array (list)
            add_node(key, None, parent_node_id, level)  # Nodo padre con valor None
            for item in value:  # Procesar cada elemento del array
                if isinstance(item, dict):
                    child_nodes = process_json(item, start_id=start_id, parent_node_id=start_id[0] - 1, level=level + 1)
                    result.extend(child_nodes)
                else:
                    add_node(key, str(item), parent_node_id, level)  # Para elementos que no son dict
        else:  # Si es un tipo de dato primitivo (string, int, float)
            add_node(key, value, parent_node_id, level)

    return result

def json_to_table(json_data, output_file, start_id=1):
    # Procesa el JSON en una estructura tabular
    result = process_json(json_data, start_id=[start_id])  # start_id como lista para ser mutable

    # Escribir en el archivo reemplazando None por 'NULL'
    with open(output_file, 'w', encoding='utf-8') as file:
        for row in result:
            row_str = str(row).replace("None", "NULL")  # Reemplazar None por 'NULL'
            file.write(f"{row_str},\n")  # Escribir cada tupla en una nueva línea

    print(f"El archivo se ha guardado exitosamente en: {output_file}")

# Ejemplo de JSON
json_data = {
    "api_name": "api_transaction_order_cancel",
    "Authorization": "Bearer --",
    "data": {
        "originalTransactionId": "6032411151252375790082",
        "transactor": {
            "idType": "loginId",
            "idValue": "networkadminQA"
        },
        "isServiceChargeReversible": "True",
        "isCommissionReversible": "True",
        "isTCPCheckRequired": "False",
        "remarks": "Devolucion 6032411151252375790082"
    }
}

# Convertir JSON a tabla y exportar a archivo, especificando el ID de inicio
json_to_table(json_data, 'app/test/json_to_datatable/tupla_plantila.txt', start_id=1150)
