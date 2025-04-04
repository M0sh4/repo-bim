import http.client
import json
import traceback
from pathlib import Path
from app.error.application.error_services import ErrorServices
import boto3
import boto3.session
import requests
import urllib3

import app.shared.config as cfg
from app.error.domain.error_model import CustomError
from app.shared.utils import Utils

urllib3.disable_warnings()

class APIAdapter():
    def __init__(self, ambiente, conexion, table_proceso) :
        self.boto3_session = None
        self.ambiente = ambiente
        self.conexion = conexion
        self.table_proceso = table_proceso
    def request_api(self, api_url, headers, body, item_id):
        try:
            utils = Utils()
            response = requests.request(
                "POST",
                api_url,
                data=json.dumps(body),
                headers=headers,
                timeout=30,
                verify=False,
            )
            response.encoding = "utf-8"
            print(repr(f"{item_id} \n Consultando token {body} \n api_adapter/request_api"))
                
            response = {"code": response.status_code, "body": json.loads(response.text)}

            print(repr(f"{item_id} \n Respuesta token: {response} \n api_adapter/request_api"))

            if(str(response["code"]) != str(200)):
                raise requests.ConnectionError(repr(f"Error DR: {item_id} \n {response} \n api_adapter/request_api"))

            if(not utils.val_variable(response)):
                raise ValueError(repr(f"Error DR: {item_id} \n el token de la respuesta del api no tiene valor \n api_adapter/request_api"))

            return response["body"]["token"]["access_token"]

        except requests.Timeout as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {item_id} \n Timeout al realizar la solicitud a la API: {str(e)} \n api_adapter/request_api"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

        except requests.ConnectionError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {item_id} \n No se pudo establecer conexión con la API: {str(e)} \n api_adapter/request_api"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

        except requests.HTTPError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {item_id} \n La API respondió con un error HTTP {e.response.status_code}: {str(e)} \n api_adapter/request_api"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

        except json.JSONDecodeError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {item_id} \n No se pudo decodificar el JSON de la respuesta de la API : {str(e)} \n api_adapter/request_api"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

        except requests.RequestException as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {item_id} \n Ocurrió un error en la solicitud HTTP : {str(e)} \n api_adapter/request_api"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

        except ValueError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = "ValueError",
                message = f"Error DR: {str(e)}",
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

        except Exception as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {item_id} \n Error al realizar la petición al api token: {str(e)} \n api_adapter/request_api"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

    def request_api_sindata(self, body, item_id):
        try:
            utils = Utils()

            if(self.conexion == "arn"):
                #self.boto3_session = boto3.Session(profile_name = cfg.ambiente[str(self.ambiente)]["profile_name"])
                lambda_client = boto3.client("lambda", region_name= cfg.ambiente[str(self.ambiente)]["region"])

                response = lambda_client.invoke(
                    FunctionName=cfg.ambiente[str(self.ambiente)]["arn_lambda_api_sender"],
                    InvocationType="RequestResponse",
                    Payload=json.dumps(body),
                )
                payload_res = json.loads(response["Payload"].read().decode("utf-8"))
            elif(self.conexion == "api"):
                print(repr(f"{item_id} \n Payload login token {body} \n api_adapter/request_api_sindata"))
                conn = http.client.HTTPSConnection(cfg.ambiente[str(self.ambiente)]["httpconnect"])
                payload = json.dumps(body)
                headers = {
                'x-api-key': cfg.ambiente[str(self.ambiente)]["x_api"],
                'Content-Type': 'application/json'
                }
                print(repr(f"{item_id} \n Consultando token {body} \n api_adapter/request_api_sindata"))
                conn.request("POST", cfg.ambiente[str(self.ambiente)]["recurso"], payload, headers)
                res = conn.getresponse()

                print(repr(f"{item_id} \n Respuesta token: {res} \n api_adapter/request_api_sindata"))
                payload_res = json.loads(res.read().decode("utf-8"))
                print(repr(f"{item_id} \n Respuesta token utf-8: {payload_res} \n api_adapter/request_api_sindata"))
            response1 = {"code": payload_res["statusCode"], "body": payload_res["body"]}
            print(repr(f"{item_id} \n Respuesta token json: {response1} \n api_adapter/request_api_sindata"))

            if(str(response1["code"]) != str(200)):
                #aqui
                raise requests.ConnectionError(repr(f"Error DR: {item_id} \n {response1} \n api_adapter/request_api_sindata"))
                
            if(not utils.val_variable(response1)):
                raise ValueError(repr(f"Error DR: {item_id} \n el token de la respuesta del api no tiene valor \n api_adapter/request_api_sindata"))

            return response1["body"]["token"]["access_token"]
        
        except requests.Timeout as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {item_id} \n Timeout al realizar la solicitud a la API: {str(e)} \n api_adapter/request_api_sindata"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

        except requests.ConnectionError as e:
            #aqui
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else:
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            id_log_error = item_id
            error_type_error = type(e).__name__
            message_error = f"{str(e)}"
            stack_trace_error = str(file_name + " " + stack_trace)
            id_mapping_error = None
            clave_ewp_error = None

            error_services = ErrorServices(
                id_log_error,
                error_type_error,
                message_error,
                stack_trace_error,
                id_mapping_error,
                clave_ewp_error,
                self.ambiente,
                self.table_proceso
            )
            error_services.log_error()
            return ''
            # original_stack_trace = traceback.format_exc()
            # line_pos = original_stack_trace.find("line")
            # if line_pos != -1:
            #     stack_trace = original_stack_trace[line_pos:]
            # else: 
            #     stack_trace = original_stack_trace

            # file_name = Path(__file__).name
            # raise CustomError(
            #     id_log = item_id,
            #     error_type = type(e).__name__,
            #     message = repr(f"Error DR: {item_id} \n No se pudo establecer conexión con la API: {str(e)} \n api_adapter/request_api_sindata"),
            #     stack_trace = str(file_name+ " " + stack_trace),
            #     id_mapping = None,
            #     clave_ewp = None
            # ) from e

        except requests.HTTPError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {item_id} \n La API respondió con un error HTTP {e.response.status_code}: {str(e)} \n api_adapter/request_api_sindata"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

        except json.JSONDecodeError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {item_id} \n No se pudo decodificar el JSON de la respuesta de la API : {str(e)} \n api_adapter/request_api_sindata"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

        except requests.RequestException as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {item_id} \n Ocurrió un error en la solicitud HTTP : {str(e)} \n api_adapter/request_api_sindata"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e
        
        except ValueError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace
  
            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = "ValueError",
                message = f"Error DR: {str(e)}",
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e
        
        except Exception as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {item_id} \n Error al realizar la petición al api token: {str(e)} \n api_adapter/request_api_sindata"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e