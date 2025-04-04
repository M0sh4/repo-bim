    
from datetime import datetime
from time import time
import pytz
tz = pytz.timezone("America/Lima")

def generar_codigo():
        # Obtener la fecha y hora actual con microsegundos
        ahora = datetime.now(tz)
        
        # Redondear los segundos según el valor de los milisegundos
        segundo_redondeado = round(ahora.second + ahora.microsecond / 1_000_000)
        
        # Si el segundo redondeado es 60, incrementamos el minuto y restablecemos el segundo
        if segundo_redondeado == 60:
            ahora = ahora.replace(second=0)
            if ahora.minute == 59:
                ahora = ahora.replace(minute=0, hour=ahora.hour + 1 if ahora.hour < 23 else 0)
            else:
                ahora = ahora.replace(minute=ahora.minute + 1)
        else:
            ahora = ahora.replace(second=segundo_redondeado)
        
        # Formatear el código en el formato deseado
        codigo = ahora.strftime("%Y%m%d%H%M%S")
        return codigo,True

print(generar_codigo())