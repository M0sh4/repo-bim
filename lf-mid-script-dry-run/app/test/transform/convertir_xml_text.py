import json

# El XML que quieres almacenar como texto
xml_text = '''<?xml version= \"1.0\" encoding= \"UTF-8\" standalone= \"yes\"?><ns2:cashinrequest xmlns:ns2= \"http://www.ericsson.com/em/emm/financial/v1_0\"><sendingfri>FRI:COMPWKASNET/USER</sendingfri><receivingfri>FRI:51902195929/MSISDN</receivingfri><amount>100.0</amount><sendernote>1127820241120192439</sendernote><receivermessage>1127820241120192439</receivermessage></ns2:cashinrequest>'''

# Estructura JSON donde guardarás el XML como texto
data = {
        "xml": xml_text  # Aquí guardas el XML como texto
}

# Convertir a JSON
json_data = json.dumps(data)

# Guardar en un archivo o usar la cadena en el programa
with open('app/test/transform/xml_to_text.json', 'w') as f:
    f.write(json_data)

print("El XML fue guardado como texto en el JSON.")