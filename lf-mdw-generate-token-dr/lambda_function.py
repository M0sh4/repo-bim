from update_token import AuthMain
import traceback

def lambda_handler(event, context):
    try:
        AuthMain().peticion_token()
        return "Generacion de token correcta."
    except Exception as e:
        print(e)