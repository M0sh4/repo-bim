import app.shared.config as cfg
import uuid
import random
import string
from app.infraestructure.adapters.api_adapter import APIAdapter
from app.infraestructure.adapters.db_adapter import DBAdapter
from app.shared.utils import Utils


class AuthRepository:
    def __init__(self, ambiente, conexion, table_proceso):
        self.ambiente = ambiente
        self.conexion = conexion
        self.table_proceso = table_proceso
        self.api_adapter = APIAdapter(self.ambiente, self.conexion, self.table_proceso)
        self.db_adapter = DBAdapter("",self.ambiente)
        self.tabla_user = cfg.ambiente[str(self.ambiente)]["table_Values_Match"]

    def get_token(self, type_token_api: str, item_id, contexto_encontrado: str, msisdn_token):
        
        if(type_token_api == "msisdn"):
            workspace: str = cfg.LOGIN_AUTH["type_auth"][str(type_token_api)]["workspace"]
            identifier_type: str = cfg.LOGIN_AUTH["type_auth"][str(type_token_api)]["identifier_type"]
            authentication_type: str = cfg.LOGIN_AUTH["type_auth"][str(type_token_api)]["authentication_type"]

            utils = Utils()
            print(repr(f"{item_id} \n Consultando pin de msisdn {msisdn_token} \n auth_repository/get_token"))
            result_pin = self.select_pass(msisdn_token)
            print(repr(f"{item_id} \n Respuesta pin de msisdn {result_pin} \n auth_repository/get_token"))

            if(result_pin is None or not result_pin):
                print(repr(f"Error DR: {item_id} \n No existe el número {msisdn_token} registrado en el Dry Run \n auth_repository/get_token"))
                raise ValueError(repr(f"Error DR: {item_id} \n No existe el número {msisdn_token} registrado en el Dry Run \n auth_repository/get_token"))
            elif(result_pin[0]["ctr_user"] == "" or not result_pin[0]["ctr_user"]):
                raise ValueError(repr(f"Error DR: {item_id} \n No activado el número {msisdn_token} registrado en el Dry Run \n auth_repository/get_token"))

            pin_token = result_pin[0]["ctr_user"]
            credentials = utils.encode_b64(f"{msisdn_token}:{pin_token}")
            auth = f"Basic {credentials}"
            body = {
                "api_name": "api_ums_user_login",
                "Authorization": f"{auth}",
                "data": {
                    "workspace": workspace,
                    "identifier_type": identifier_type,
                    "authentication_type": authentication_type
                },
            }
            
            return self.api_adapter.request_api_sindata(body, item_id)
        
        elif(type_token_api == "agente"):
            usuario: str = cfg.LOGIN_AUTH["type_auth"][str(type_token_api)][str(contexto_encontrado)]["usuario"]
            password: str = cfg.LOGIN_AUTH["type_auth"][str(type_token_api)][str(contexto_encontrado)]["password"]
            workspace: str = cfg.LOGIN_AUTH["type_auth"][str(type_token_api)][str(contexto_encontrado)]["workspace"]
            identifier_type: str = cfg.LOGIN_AUTH["type_auth"][str(type_token_api)][str(contexto_encontrado)]["identifier_type"]
            authentication_type: str = cfg.LOGIN_AUTH["type_auth"][str(type_token_api)][str(contexto_encontrado)]["authentication_type"]
        
            query_select_token = f'''
                SELECT token_desc FROM token_auth
                WHERE token_name = '{usuario}'
                and ambiente = '{self.ambiente}'
                and tipo_token  = 'agente'
                LIMIT 1
            '''
            print(repr(f"{item_id} \n Consultando token admi DR {str(query_select_token)} \n lambda_adapter/peticion_mobiquity"))
            print(repr(f"{item_id} \n Consultando token admi DR 2 {str(query_select_token)} \n lambda_adapter/peticion_mobiquity"))
            token_obtenido = self.db_adapter.select_query(query_select_token, None)
            print(repr(f"{item_id} \n Resultado token admi DR {token_obtenido} \n lambda_adapter/peticion_mobiquity"))

            if(token_obtenido or token_obtenido is not None or len(token_obtenido)!= 0):
                token_request = token_obtenido[0]["token_desc"]
            else:
                token_request = ''
            
            return token_request
        elif(type_token_api == "none"):
            # body = { "api_name": "api_ums_user_login",
            #         "Authorization": "",
            #         "data": {
            #         }
            # }
            # token_admin = self.api_adapter.request_api_sindata(body, item_id)
            # return token_admin

            query_select_token = f'''
                    SELECT token_desc FROM token_auth
                    WHERE token_name = 'none'
                    and ambiente = '{self.ambiente}'
                    and tipo_token  = 'none'
                    LIMIT 1
                '''
            print(repr(f"{item_id} \n Consultando token admi DR {str(query_select_token)} \n lambda_adapter/peticion_mobiquity"))
            print(repr(f"{item_id} \n Consultando token admi DR 2 {str(query_select_token)} \n lambda_adapter/peticion_mobiquity"))
            token_obtenido = self.db_adapter.select_query(query_select_token, None)
            print(repr(f"{item_id} \n Resultado token admi DR {token_obtenido} \n lambda_adapter/peticion_mobiquity"))

            if(token_obtenido or token_obtenido is not None or len(token_obtenido)!= 0):
                token_request = token_obtenido[0]["token_desc"]
            else:
                token_request = ''
            
            return token_request

    def select_pass(self, msisdn_token):
        try:
            utils = Utils()
            query = cfg.query_consulta_pin.format(tabledata=self.tabla_user)
            if(not utils.val_variable(query)):
                raise ValueError("Error DR: No existe query SQL de consulta id de la ejecución.")
            params = (msisdn_token)
            result = self.db_adapter.select_query(query, params)

            return result
        except ValueError as e:
            print(repr(f"Error DR: Ocurrió un error select mapping: {e}"))

    def generate_custom_uuid(self):
        base_uuid = str(uuid.uuid4())
        random_char = random.choice(string.ascii_letters + string.digits)
        custom_uuid = base_uuid + random_char
        return custom_uuid
 