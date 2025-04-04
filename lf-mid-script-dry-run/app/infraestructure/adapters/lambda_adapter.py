import copy
import http.client
import json
import time
import traceback
from datetime import datetime
from pathlib import Path
from aws_xray_sdk.core import xray_recorder
import boto3
import boto3.session
import botocore
from botocore.exceptions import ClientError
from app.auth.application.auth_services import AuthService
from app.error.domain.error_model import CustomError
from app.shared.utils import Utils
from app.error.application.error_services import ErrorServices
import pytz
tz = pytz.timezone("America/Lima")
class LambdaAdapter:
    def __init__(self, cfg_lambda: str, request_mobiquity, type_token_api, item_id, contexto_encontrado, msisdn_token, ambiente: str, conexion, table_proceso):
        self.cfg_lambda = cfg_lambda
        self.arn_lambda_api_sender = cfg_lambda["arn_lambda_api_sender"]
        self.boto3_session = None
        self.payload = copy.deepcopy(request_mobiquity)
        self.type_token_api = type_token_api
        self.item_id = item_id
        self.contexto_encontrado = contexto_encontrado
        self.msisdn_token = msisdn_token
        self.ambiente  = ambiente
        self.start_time_peticion_comv = None
        self.end_time_peticion_comv = None
        self.ejecution_time_peticion_comv = None
        self.response_json =  {}
        self.var_p = True
        self.conexion = conexion
        self.table_proceso = table_proceso
        self.segment = xray_recorder.current_segment()
    def peticion_mobiquity(self):
        try:
            auth_service = AuthService(self.ambiente,  self.conexion, self.table_proceso)
            self.response_json =  {}
            utils = Utils()

            if(not utils.val_variable(self.arn_lambda_api_sender)):
                raise ValueError(repr(f"Error DR: {self.item_id} \n El valor de arn_lambda_api_sender esta vacío \n lambda_adapter/peticion_mobiquity"))

            if(self.type_token_api == "none" or self.type_token_api == "agente"):

                print(repr(f"{self.item_id} \n Consultando token API \n lambda_adapter/peticion_mobiquity"))
                token_request = auth_service.get_token_login(self.type_token_api, self.item_id, self.contexto_encontrado, self.msisdn_token)
                
                if(token_request == 'None' or not token_request):
                    raise ValueError(repr(f"Error DR: {self.item_id} \n No se obtuvo el token \n lambda_adapter/peticion_mobiquity"))
                print(repr(f"{self.item_id} \n Resultado token API: {token_request} \n lambda_adapter/peticion_mobiquity"))
            else:
                print(repr(f"{self.item_id} \n Consultando token API \n lambda_adapter/peticion_mobiquity"))
                token_request = auth_service.get_token_login(self.type_token_api, self.item_id, self.contexto_encontrado, self.msisdn_token)
                print(repr(f"{self.item_id} \n Resultado token API: {token_request} \n lambda_adapter/peticion_mobiquity"))

            self.var_p = False

            start_datetime = datetime.now(tz)

            self.response_json = self.get_token_login_pre(token_request, self.var_p)

            if self.response_json.get("statusCode") == 200:
                return {
                    "response_mob": self.response_json,
                    "time_out_apisender": self.ejecution_time_peticion_comv,
                    "date_test_execution": start_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                    "request_mob":self.payload,
                    "flg_continue":1
                }
            
            return {
                "response_mob": self.response_json,
                "time_out_apisender": self.ejecution_time_peticion_comv,
                "date_test_execution": start_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                "request_mob":self.payload,
                "flg_continue":1
            }
        except ValueError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name

            adapter_error =  ErrorServices(
                self.item_id,
                "ValueError",
                repr(f"Error DR: {str(e)}"),
                str(file_name+ " " + stack_trace),
                None,
                None,
                self.ambiente,
                self.table_proceso
            )
        
            adapter_error.log_error()

            start_datetime = datetime.now(tz)
            self.response_json = self.get_token_login_pre("", self.var_p)
            

            return {
                "response_mob": self.response_json,
                "time_out_apisender": self.ejecution_time_peticion_comv,
                "date_test_execution": start_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                "request_mob":self.payload,
                "flg_continue":0
            }
        
        except ClientError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else:
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = self.item_id,
                error_type = type(e).__name__,
                message = f"Error DR: {str(e)}",
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e
        
        except botocore.exceptions.NoCredentialsError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else:
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = self.item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {self.item_id} \n No se encontraron las credenciales de AWS: {str(e)} \n lambda_adapter/peticion_mobiquity"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e
        
        except botocore.exceptions.PartialCredentialsError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else:
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = self.item_id,
                error_type = type(e).__name__,
                message = repr(f"Error DR: {self.item_id} \n Las credenciales de AWS están incompletas: {str(e)} \n lambda_adapter/peticion_mobiquity"),
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e
        
        except Exception as e:
            #aqui
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else:
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = self.item_id,
                error_type = type(e).__name__,
                message = f"Error DR: {str(e)}",
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e
    
    def get_token_login_pre(self, token_request,var_p):
        if 'Authorization' not in self.payload and not self.payload['Authorization']:
                raise ValueError(repr(f"Error DR: {self.item_id} \n En la plantilla Request Mobiquity no existe la clave ['Authorization'] \n lambda_adapter/peticion_mobiquity"))

        self.payload["Authorization"] = f"Bearer {str(token_request)}"
        print(repr(f"{self.item_id} \n Request Comviva con token {self.payload} \n lambda_adapter/peticion_mobiquity"))
        arn_lambda = self.arn_lambda_api_sender
        
        if(self.conexion == "arn"):
            subsegment = xray_recorder.begin_subsegment("apisender-arn")
            #self.boto3_session = boto3.Session(profile_name = self.cfg_lambda["profile_name"])
            invoke_lambda = boto3.client("lambda", region_name="us-east-1")

            self.start_time_peticion_comv = time.perf_counter()
            print(repr(f"{self.item_id} \n Consultando API SENDER {self.payload} \n lambda_adapter/peticion_mobiquity"))
            response = invoke_lambda.invoke(
                FunctionName=arn_lambda,
                InvocationType="RequestResponse",
                Payload=json.dumps(self.payload)
            )
            xray_recorder.end_subsegment()
            print(repr(f"{self.item_id} \n Respuesta API SENDER {response} \n lambda_adapter/peticion_mobiquity"))
            self.end_time_peticion_comv = time.perf_counter()
            self.ejecution_time_peticion_comv = self.end_time_peticion_comv - self.start_time_peticion_comv

            response_json = json.loads(response["Payload"].read().decode("utf-8"))
            print(repr(f"{self.item_id} \n Respuesta API SENDER dec {response_json} \n lambda_adapter/peticion_mobiquity"))
            return response_json
        elif(self.conexion == "api"):
            subsegment = xray_recorder.begin_subsegment("apisender-api")
            conn = http.client.HTTPSConnection(self.cfg_lambda["httpconnect"])
            payload = json.dumps(self.payload)
            headers = {
            'x-api-key': self.cfg_lambda["x_api"],
            'Content-Type': 'application/json'
            }
            print(repr(f"{self.item_id} \n Consultando API SENDER {payload} \n lambda_adapter/peticion_mobiquity"))
            xray_recorder.end_subsegment()
            self.start_time_peticion_comv = time.perf_counter()
            conn.request("POST", self.cfg_lambda["recurso"], payload, headers)
            res = conn.getresponse()
            self.end_time_peticion_comv = time.perf_counter()
            self.ejecution_time_peticion_comv = self.end_time_peticion_comv - self.start_time_peticion_comv
            print(repr(f"{self.item_id} \n Respuesta API SENDER {res} \n lambda_adapter/peticion_mobiquity"))
            response_json = json.loads(res.read().decode("utf-8"))
            print(repr(f"{self.item_id} \n Respuesta API SENDER dec {response_json} \n lambda_adapter/peticion_mobiquity"))
            return response_json