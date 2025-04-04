from lxml import etree
import os

# Función para convertir XML a un formato de diccionario aplanado
def xml_to_dict(element, parent_key='', sep='.'):
    items = {}
    for child in element:
        new_key = f"{parent_key}{sep}{child.tag}" if parent_key else child.tag
        if len(child) > 0:
            # Si el elemento tiene hijos, llamamos recursivamente
            items.update(xml_to_dict(child, new_key, sep=sep))
        else:
            # Si el elemento no tiene hijos, lo agregamos
            items[new_key] = child.text
    return items

# Función para extraer claves y valores del XML
def extraer_claves_y_valores_xml(xml_file):
    if not os.path.isfile(xml_file):
        print(f"El archivo {xml_file} no se encuentra en la ubicación especificada.")
        return {}

    try:
        tree = etree.parse(xml_file)
        root = tree.getroot()
        return xml_to_dict(root)
    except etree.XMLSyntaxError as e:
        print(f"Error de sintaxis XML: {e}")
        return {}
    except Exception as e:
        print(f"Error al leer el archivo XML: {e}")
        return {}

# Función para guardar las claves y valores en un archivo de texto tabulado con alineación
def guardar_claves_y_valores_alineados(diccionario, nombre_archivo):
    max_len = max(len(clave) for clave in diccionario)  # Longitud máxima de las claves
    with open(nombre_archivo, 'w') as f:
        for clave, valor in diccionario.items():
            espacios = ' ' * (max_len - len(clave))  # Espacios necesarios para alinear
            f.write(f"{clave}{espacios} \t {valor}\n")

# Archivo XML de entrada
xml_file = 'app/test/transform/data.xml'

# Extraer y guardar las claves y valores
claves_y_valores = extraer_claves_y_valores_xml(xml_file)
if claves_y_valores:
    guardar_claves_y_valores_alineados(claves_y_valores, 'app/test/transform/cabeceras_vertical_XML.txt')
    print("Las claves y valores del XML han sido guardados en 'app/test/transform/cabeceras_vertical_XML.txt'.")
else:
    print("No se pudieron extraer claves y valores del archivo XML.")
