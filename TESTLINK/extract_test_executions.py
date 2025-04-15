import xmlrpc.client

# Configura URL y API Key
url = "http://testlink.mibim.pe/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
api_key = "1053c01b64867ce9b01feaaecaeb456d"

# Conectar con el servidor
server = xmlrpc.client.ServerProxy(url)

# Obtener proyectos
projects = server.tl.getProjects(api_key)
print("Proyectos disponibles:")
for p in projects:
    print(f"- {p['name']} (ID: {p['id']})")
