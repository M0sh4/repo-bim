import config_token as cfg
import asyncio
import uuid
import random
import string
import base64
import requests
import json
import boto3
import boto3.session
import http.client
import base64
from db_adapter_tk import DBAdapter
import sys
from datetime import datetime
import pytz
tz = pytz.timezone("America/Lima")

class AuthMain():

    def __init__(self):
        self.ambiente = "preprod"
        self.list_bussines = None
        self.conexion = "arn" #arn
        self.boto3_session = None
        self.db_adapter = DBAdapter("",self.ambiente)


    def peticion_token(self):
       
       self.token_agente()
       self.token_a()

    def token_agente(self):
         self.list_bussines = cfg.AGENTE[str(self.ambiente)]
         for bussines in self.list_bussines:
            
            usuario: str = bussines["usuario"]
            password: str = bussines["password"]
            workspace: str = bussines["workspace"]
            identifier_type: str = bussines["identifier_type"]
            authentication_type: str = bussines["authentication_type"]

            credentials = self.encode_b64(f"{usuario}:{password}")

            auth = f"Basic {credentials}"

            body =  {
                "api_name": "api_ums_user_login",
                "Authorization": f"{auth}",
                "data": {
                    "workspace": workspace,
                    "identifier_type": identifier_type,
                    "authentication_type": authentication_type
                }
            }
            self.blocktable()
            token = self.request_api(body)
            print(f"token agente  {usuario} : {token}")

            self.save_tk(usuario, token, "agente")
            
    def token_a(self):
        #key_generate = self.generate_custom_uuid()
        body = { "api_name": "api_ums_user_login",
                "Authorization": "",
                "data": {
                }
        }
        self.blocktable()
        token = self.request_api(body)
        print(f"token none : {token}")
        self.save_tk("none", token, "none")

    def generate_custom_uuid(self):
        base_uuid = str(uuid.uuid4())
        random_char = random.choice(string.ascii_letters + string.digits)
        custom_uuid = base_uuid + random_char
        return custom_uuid
    
    def encode_b64(self, message: str) -> str:
        message_bytes = message.encode("utf-8")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("utf-8")
        return base64_message
    

    def request_api(self, body):
        try:
            payload_res = None
            if(self.conexion == "arn"):
                #self.boto3_session = boto3.Session(profile_name = cfg.ambiente[str(self.ambiente)]["profile_name"])
                lambda_client = boto3.client("lambda", region_name= cfg.ambiente[str(self.ambiente)]["region"])

                response = lambda_client.invoke(
                    FunctionName=cfg.ambiente[str(self.ambiente)]["arn_lambda_api_sender"],
                    InvocationType="RequestResponse",
                    Payload=json.dumps(body), 
                    
                )

                payload_res = json.loads(response["Payload"].read().decode("utf-8"))
                print(f"RESPUESTA API-SENDER: {payload_res}")
                response_timeout = payload_res.get("errorMessage", "")
                if response_timeout != "":
                    try:
                        response = lambda_client.invoke(
                        FunctionName="lf-mdw-send-report-email",
                        InvocationType="RequestResponse",
                        Payload=json.dumps({"timeout": "F"}),
                        )
                        print("Correo Enviado")
                    except:
                        print("Correo fallo")
            elif(self.conexion == "api"):

                conn = http.client.HTTPSConnection(cfg.ambiente[str(self.ambiente)]["httpconnect"])
                payload = json.dumps(body)
                headers = {
                'x-api-key': cfg.ambiente[str(self.ambiente)]["x_api"],
                'Content-Type': 'application/json'
                }
                conn.request("POST", cfg.ambiente[str(self.ambiente)]["recurso"], payload, headers)
                res = conn.getresponse()

                payload_res = json.loads(res.read().decode("utf-8"))

            response1 = {"code": payload_res["statusCode"], "body": payload_res["body"]}

            print(repr(f"Respuesta token json: {response1} \n api_adapter/request_api_sindata"))

            if(str(response1["code"]) != str(200)):
                raise requests.ConnectionError(repr(f"Error DR: \n {response1} \n api_adapter/request_api_sindata"))
                
            if(not self.val_variable(response1)):
                raise ValueError(repr("Error DR: el token de la respuesta del api no tiene valor \n api_adapter/request_api_sindata"))

            return response1["body"]["token"]["access_token"]
        
        except Exception as e:
            message = repr(f"Error DR: \n Error al realizar la petición al api token: {str(e)} \n api_adapter/request"),
            print(f"{message}")



    def val_variable(self, query):
        bquery = True
        if(isinstance(query, str)):
            if(query == ""):
                bquery = False
        else:
            if(not query or query is None):
                bquery = False

        return bquery
    
    def save_tk(self, usuario, token, tipo_token):
        try:
            tabla_tk = cfg.ambiente[str(self.ambiente)]["tabla_tk"]
            print(repr(f"tabla_tk: {tabla_tk}"))
            fecha_actual = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
            query_insert = f"""
                INSERT INTO {tabla_tk} (token_name, token_desc, ambiente, tipo_token, date_commit)
                VALUES('{usuario}', '{token}', '{self.ambiente}', '{tipo_token}','{fecha_actual}')
                ON DUPLICATE KEY UPDATE 
                    token_name = '{usuario}',
                    token_desc = '{token}',
                    ambiente = '{self.ambiente}',
                    tipo_token = '{tipo_token}',
                    date_commit = '{fecha_actual}'
            """
            
            re_mysql = self.db_adapter.insert_query(query_insert, None)
            print(repr(f"re_mysql: {re_mysql}"))
            if not re_mysql or re_mysql is None or re_mysql == 0:
                raise ValueError("Error DR: en la base de datos al insertar id de la ejecución.")

        except PermissionError as pe:
            print(repr(f"Error DR: Error de permiso insert idexecution: {pe}"))
            sys.exit(1)
        except ValueError as e:
            print(repr(f"Error DR: Ocurrió un error insert idexecution: {e}"))
            sys.exit(1)
        except Exception as e:
            print(repr(f"Error DR: General error insert idexecution: {e}"))
            sys.exit(1)

    def blocktable(self):
        self.db_adapter.blocktable()


if __name__ == "__main__":
    auth_main = AuthMain()
    asyncio.run(auth_main.peticion_token())