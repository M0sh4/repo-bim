''' Valida input/output'''
import traceback
from pathlib import Path

import app.shared.config as cfg
from app.error.domain.error_model import CustomError
from app.shared.utils import Utils

class EWPDomain():
    ''' Class MappingDomain'''
    def deserializacion_datos_ewp(self, item):
        try:
            utils = Utils()
            if(not utils.val_variable(item)):
                raise ValueError(repr(f"Error DR: {item["id"]} \n No existe registro a procesar. \n ewp_domain/deserializacion_datos_ewp"))
            if(not utils.val_variable(item["request_ewp"])):
                raise ValueError(repr(f"Error DR: {item["id"]} \n No existe registro de request EWP a procesar. \n ewp_domain/deserializacion_datos_ewp {item["id"]}"))
            
            request_ewp = utils.deserializacion_json(item["request_ewp"])
            response_ewp = utils.deserializacion_json(item["response_ewp"])
            
            print(repr(f"{item["id"]} \n Request EWP xml: {request_ewp}  \n  ewp_domain/deserializacion_datos_ewp"))
            print(repr(f"{item["id"]} \n Response EWP xml: {response_ewp} \n  ewp_domain/deserializacion_datos_ewp"))

            
            if (request_ewp is None or request_ewp == "null" or request_ewp == "None"):
                response_ewp = ""
            if request_ewp["api_name"] in cfg.JSON_API["especificos"]:
                contexto_encontrado = utils.buscar_y_tomar_valor(request_ewp, cfg.JSON_API["contextos"])
                print(repr(f"{item["id"]} \n Version Plantilla Mobiquity contextos: {contexto_encontrado}  \n  ewp_domain/deserializacion_datos_ewp"))
                if(contexto_encontrado is None):
                    raise ValueError(repr(f"Error DR: {item["id"]} \n No existe el contexto del servicio en la configuración de api-json.  \n  ewp_domain/deserializacion_datos_ewp"))
            else:
                if(request_ewp["api_name"] == "transfer") and utils.buscar_y_tomar_valor(request_ewp, cfg.JSON_API["msisdn_agente"]):
                    contexto_encontrado = "refund"
                else:
                    contexto_encontrado = "general"

                if(utils.traslate_xml_in_json(request_ewp['message']) is None or utils.traslate_xml_in_json(request_ewp['message']) == "null"):
                    contexto_encontrado = "auth"
                
                print(repr(f"{item["id"]} \n Version Plantilla Mobiquity: {contexto_encontrado}  \n  ewp_domain/deserializacion_datos_ewp"))

            return request_ewp, response_ewp, request_ewp["api_name"], contexto_encontrado

        except ValueError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else:
                stack_trace = original_stack_trace
  
            file_name = Path(__file__).name
            raise CustomError(
                id_log = item["id"],
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
                id_log = item["id"],
                error_type = type(e).__name__,
                message = f"Error DR: {str(e)}",
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e


    def deserializacion_mapping(self, item_id, lista_mapping, api_name, id_json):
        """ Deserializar Mapping para el proceso Dry Run"""
        try:

            utils = Utils()
            if(not utils.val_variable(lista_mapping)):
                raise ValueError(repr(f"Error DR: {item_id} \n No existe registro de mapping a procesar. \n ewp_repository/deserializacion_mapping"))
            
            lista_mapping_ewp_api = utils.transform_list_to_dataframe(lista_mapping[str(api_name)])
            
            if(lista_mapping_ewp_api.empty):
                raise ValueError(repr(f"Error DR: {item_id} \n El tipo de variable de mapping no es list. \n ewp_repository/deserializacion_mapping"))

            lista_mapping_input_ewp_api = lista_mapping_ewp_api[
                (lista_mapping_ewp_api['type_date'] == "I") & (lista_mapping_ewp_api['id_json_api'] == int(id_json))
            ]

            lista_mapping_output_ewp_api = lista_mapping_ewp_api[
                (lista_mapping_ewp_api['type_date'] == "O") & (lista_mapping_ewp_api['id_json_api'] == int(id_json))
]
            if (not utils.is_dataframe(lista_mapping_input_ewp_api)):
                raise ValueError(repr(f"Error DR: {item_id} \n No existe registro de mapping de comparación del request \n ewp_repository/deserializacion_mapping"))

            if (not utils.is_dataframe(lista_mapping_output_ewp_api)):
                raise ValueError(repr(f"Error DR: {item_id} \n No existe registro de mapping de comparación del response \n ewp_repository/deserializacion_mapping"))

            print(repr(f"{item_id} \n Se filtro mapeo de request y response del api"))
            return lista_mapping_input_ewp_api, lista_mapping_output_ewp_api

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
                message = f"Error DR: {str(e)}",
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e
        
    
    def deserializacion_plantilla(self, item_id,lista_plantilla_mobiquity):
        try:
            utils = Utils()
            if(not utils.val_variable(lista_plantilla_mobiquity)):
                raise ValueError(repr(f"Error DR: {item_id} \n No existe registro de la plantilla request mobiquity. \n ewp_doamin/deserializacion_plantilla"))
            
            lista_plantilla_mobiquity_by_api = utils.deserializacion_json(lista_plantilla_mobiquity)

            if(not utils.val_variable(lista_plantilla_mobiquity_by_api)):
                raise ValueError(repr(f"Error DR: {item_id} \n No existe registro de la plantilla request mobiquity. \n ewp_doamin/deserializacion_plantilla"))
            
            return lista_plantilla_mobiquity_by_api

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
                error_type = ValueError,
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
                message = f"Error DR: {str(e)}",
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e
        
    def deserializacion_token_api(self, item_id, type_token,api_name, contexto):
        try:
            utils = Utils()
            type_token_auth = ""
            id_json = 0

            if(not utils.val_variable(type_token)):
                raise ValueError(repr(f"Error DR: {item_id} \n Falta registro del tipo de token a utilizar en el api. \n  ewp_domain/deserializacion_token_api"))
            

            for item in type_token:
                if (item.get('version_json') == contexto and contexto != "" and item.get('clave_ewp') == api_name) or (contexto == "" and item.get('clave_ewp') == api_name):
                    type_token_auth = item.get('type_token')
                    id_json = item.get('id_json_api')

            print(repr(f"{item_id} \n Tipo de token: {type_token_auth} \n id Plantilla: {id_json} \n ewp_domain/deserializacion_token_api"))
            return type_token_auth, id_json

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
                message = f"Error DR: {str(e)}",
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e