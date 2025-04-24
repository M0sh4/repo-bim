import requests
import os
from bs4 import BeautifulSoup

ID = "7377"
DEV_KEY = "04ded488fa8e0eddd19cb22e32092189"
API_URL = f"http://testlink.mibim.pe/testlink/lnl.php?type=exec&id={ID}&apikey={DEV_KEY}"

resp = requests.get(API_URL)
soup = BeautifulSoup(resp.text, 'html.parser')

# Extraer el nombre del caso de prueba
title_row = soup.find("th")
nombre_caso = title_row.text.strip().split(":")[-1].split("[")[0].strip()

# Extraer resumen
resumen = soup.find('span', string="Resumen:").find_next("p").text.strip()

# Extraer precondiciones
precondiciones = soup.find('span', string="Precondiciones:").find_next("p").text.strip()

# Extraer los pasos
pasos = []
for fila in soup.find_all("tr"):
    columnas = fila.find_all("td")
    if len(columnas) >= 5 and columnas[0].text.strip().isdigit():
        paso_num = columnas[0].text.strip()
        accion = columnas[1].text.strip()
        esperado = columnas[2].text.strip()
        estado = columnas[4].text.strip()

        # Buscar adjuntos justo después del paso (en una fila independiente)
        siguiente = fila.find_next_sibling("tr")
        imagenes = []
        if siguiente and "Execution Attachments" in siguiente.text:
            imgs = siguiente.find_all("img")
            for img in imgs:
                imagenes.append(img["src"])

        pasos.append({
            "paso": paso_num,
            "accion": accion,
            "esperado": esperado,
            "estado": estado,
            "adjuntos": imagenes
        })

# Extraer duración, tester, resultado, etc.
datos = {}
labels = {
    "Tester": "tester",
    "Resultado de la Ejecución:": "resultado",
    "Modo de Ejecución:": "modo",
    "Duración de le ejecución (min):": "duracion"
}

for fila in soup.find_all("tr"):
    columnas = fila.find_all("td")
    if len(columnas) >= 2:
        label = columnas[0].text.strip()
        valor = columnas[1].text.strip()
        if label in labels:
            datos[labels[label]] = valor

# Mostrar todo
print(f"📄 Caso: {nombre_caso}")
print(f"📌 Resumen: {resumen}")
print(f"⚙️ Precondiciones: {precondiciones}")
print(f"👤 Tester: {datos.get('tester')}")
print(f"⏱ Duración: {datos.get('duracion')} minutos")
print(f"✅ Resultado: {datos.get('resultado')}\n")

print("📋 Pasos:")
i = 0
for p in pasos:
    print(f"  🔢 Paso {p['paso']}")
    print(f"     Acción: {p['accion']}")
    print(f"     Esperado: {p['esperado']}")
    print(f"     Estado: {p['estado']}")
    if p["adjuntos"]:
        print(f"     Adjuntos: {', '.join(p['adjuntos'])}")
        for adjunto in p['adjuntos']:
            _image = requests.get(adjunto)
            if _image.status_code == 200:
                filename = f"adjunto_paso_{i}.png"
                with open(filename, 'wb') as f:
                    f.write(_image.content)
                print(f"✅ Imagen guardada: {filename}")
            else:
                print(f"❌ No se pudo descargar: {adjunto} (Status: {_image.status_code})")
            print(_image)
            i = i+1
