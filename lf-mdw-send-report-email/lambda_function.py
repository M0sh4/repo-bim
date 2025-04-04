import json
from correo import enviar, enviarCorreoTimeOut

def lambda_handler(event, context):
    # TODO implement
    try:
        isTimeOut = event.get('timeout','')
        destinatarios = "loaypardo.vilchez.melvin@gmail.com"  # Cambia al correo del destinatario
        cc = ["rnzsnow14@gmail.com", "sthepfanye@gmail.com"]
        if isTimeOut == '':
            asunto = "DRY RUN - Reporte"
            #for destinatario in destinatarios.split(';'):
                #print(destinatario)
            enviar(destinatarios, asunto, cc)
        else:
            asunto = "TIMED OUT AGENTES Y ADMINS"
            enviarCorreoTimeOut(destinatarios, asunto, cc)

        return {
            'statusCode': 200,
            'body': 'correo enviado.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': e
        }
