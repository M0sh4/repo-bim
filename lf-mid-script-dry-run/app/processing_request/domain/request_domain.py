''' DOMAIN DE REQUEST'''
import base64
import re
import traceback
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from jsonpath_ng.ext import parse
from unidecode import unidecode

import app.shared.config as cfg
from app.error.domain.error_model import CustomError
from app.infraestructure.adapters.db_adapter import DBAdapter
from app.infraestructure.adapters.lambda_adapter import LambdaAdapter
from app.shared.utils import Utils
from app.error.application.error_services import ErrorServices
class RequestDomain():

    def __init__(self, lista_ubligeo,ambiente, conexion, table_proceso):
        self.ambiente = ambiente
        self.conexion = conexion
        self.table_save_data = {}
        self.msisdn_token = ""
        self.sendingfri = None
        self.receivingfri = None
        self.monto = ""
        self.sendernote = None
        self.lista_ubligeo = lista_ubligeo
        self.financialtransactionid = ""
        self.tabla_usuarios = cfg.ambiente[str(self.ambiente)]["table_Values_Match"]
        self.tabla_transaccion = cfg.ambiente[str(self.ambiente)]["table_Values_Transaccion"]
        self.findtransaccion_match = cfg.ambiente[str(self.ambiente)]["findtransaccion_match"]
        self.table_reverse_reverse_cahorros = cfg.ambiente[str(self.ambiente)]["table_reverse_reverse_cahorros"]
        self.estado_reverse_reverse_cahorros = 0
        self.table_proceso = table_proceso

    ''' Class request Domain'''
    def get_request_ewp_in_json(self, request_ewp, id_item, contexto_encontrado) -> Optional[dict]:
        try:
            utils = Utils()
            auth_bytes = ""
            auth_bytes = self.get_token_auth(request_ewp["auth"])
            
            if(not utils.val_variable(request_ewp['message'])):
                raise ValueError(repr(f"Error DR: {id_item} \n No existe xml en el request EWP \n request_domain/get_request_ewp_in_json"))
            elif(not utils.is_date_xml(request_ewp['message']) and contexto_encontrado != "auth"):
                raise ValueError(repr(f"Error DR: {id_item} \n El request EWP no tiene un formato XML correcto \n request_domain/get_request_ewp_in_json"))
            
            json_data = utils.traslate_xml_in_json(request_ewp['message'])
            print(repr(f"{id_item} \n Request EWP JSON: {json_data} \n request_domain/get_request_ewp_in_json"))
            
            return json_data, auth_bytes
        
        except ValueError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace
  
            file_name = Path(__file__).name

            raise CustomError(
                id_log = id_item,
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
                id_log = id_item,
                error_type = type(e).__name__,
                message = f"Error DR: {str(e)}",
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

    def get_mapping_replace_values(self, message_request_ewp, lista_mapping, plantilla_mobiquity, id_item, auth_bytes, type_token_api, api_name, date_capture,contexto_http,agente):
        try:
            utils = Utils()
            lista_mapping[['valor_ewp', 'is_capture']] = lista_mapping.apply(
                lambda row: self.get_nested_value(
                    message_request_ewp, row['clave_ewp'], row['split_ewp'], row['valor_position_ewp'],
                    row['type_replace'], row['valor_ewp'], row['valor_comv'],  row['type_compare'],
                    auth_bytes, row['sel_value'],  row['table_save'], row['is_identifier'], type_token_api, id_item, api_name, date_capture,contexto_http,agente
                ),
                axis=1,
                result_type='expand'
            )

            lista_mapping_filtrada = lista_mapping[lista_mapping['is_capture'] == 1]

            for _, row in lista_mapping_filtrada.iterrows():
                try:

                    valor_ewp = row['valor_ewp']
                    clave_comv = row['clave_comv']
                    type_compare = row['type_compare']
                    valor_mob_origin = None

                    if (clave_comv is not None and clave_comv != ""):

                        jsonpath_expression = utils.translate_to_jsonpath(clave_comv)
                        parse_expression = parse(jsonpath_expression)
                        matches_mob = parse_expression.find(plantilla_mobiquity)
                       
                        
                        if (matches_mob and valor_ewp is not None):

                            if type_compare == "directa":
                                matches_mob = matches_mob[0]
                            context_value = matches_mob.context.value

                            if isinstance(context_value, dict):
                                key_to_update = matches_mob.path.fields[0]
                                original_type = type(context_value[key_to_update])
                                if str(context_value[key_to_update]).startswith("0") and len(str(context_value[key_to_update])) > 1:
                                    original_type = type("texto")

                                valor_mob_origin = context_value[key_to_update]
                                if(str(row["is_compare"]) == "1"):
                                    context_value[key_to_update] = original_type(valor_ewp)


                            elif isinstance(context_value, list) and context_value:
                                original_type = type(context_value[0])
                                if context_value[key_to_update].startswith("0") and len(context_value[key_to_update]) > 1:
                                    original_type = type("texto")
                                valor_mob_origin = context_value[0]
                                if(str(row["is_compare"]) == "1"):    
                                    context_value[0] = original_type(valor_ewp)

                        else:
                            raise ValueError(repr(f"Error DR: {id_item} \n No se encontró la clave {row["clave_comv"]} del Request de Comviva. \n request_domain/get_mapping_replace_values"))
                        
                    if((row["is_saved"] not in (None,"")) and (row["table_save"] not in (None, ""))):
                        if "," in row["is_saved"]:  # Verifica si existe una coma
                            data_valor = row["is_saved"].split(",")  # Divide en dos partes
                            self.table_save_data[str(data_valor[0])] = str(valor_ewp)
                            self.table_save_data[str(data_valor[1])] = str(valor_ewp)
                        else:
                            if(str(row["is_compare"]) == "1"):
                                self.table_save_data[row["is_saved"]] = str(valor_ewp)
                            else:
                                self.table_save_data[row["is_saved"]] = str(valor_mob_origin)


                except KeyError as e:
                    original_stack_trace = traceback.format_exc()
                    line_pos = original_stack_trace.find("line")
                    if line_pos != -1:
                        stack_trace = original_stack_trace[line_pos:]
                    else:
                        stack_trace = original_stack_trace

                    file_name = Path(__file__).name
                    raise CustomError(
                        id_log = id_item,
                        error_type = "KeyError",
                        message = f"Error DR: {str(e)}",
                        stack_trace = str(file_name+ " " + stack_trace),
                        id_mapping = row['id_mapping'],
                        clave_ewp = row['valor_ewp']
                    ) from e
                except TypeError as e:
                    original_stack_trace = traceback.format_exc()
                    line_pos = original_stack_trace.find("line")
                    if line_pos != -1:
                        stack_trace = original_stack_trace[line_pos:]
                    else: 
                        stack_trace = original_stack_trace

                    file_name = Path(__file__).name
                    raise CustomError(
                        id_log = id_item,
                        error_type = "KeyError",
                        message = f"Error DR: {str(e)}",
                        stack_trace = str(file_name+ " " + stack_trace),
                        id_mapping = row['id_mapping'],
                        clave_ewp = row['valor_ewp']
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
                        id_log = id_item,
                        error_type = "ValueError",
                        message = f"Error DR: {str(e)}",
                        stack_trace = str(file_name+ " " + stack_trace),
                        id_mapping = row['id_mapping'],
                        clave_ewp = row['valor_ewp']
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
                        id_log = id_item,
                        error_type = "KeyError",
                        message = f"Error DR: {str(e)}",
                        stack_trace = str(file_name+ " " + stack_trace),
                        id_mapping = row['id_mapping'],
                        clave_ewp = row['valor_ewp']
                    ) from e
                
            print(repr(f"{id_item} \n Request Comviva sin token {plantilla_mobiquity} \n request_domain/get_mapping_replace_values"))
            print(repr(f"{id_item} \n Datos a guardar de Request en la tabla DR {self.table_save_data} \n request_domain/get_mapping_replace_values"))
            print(repr(f"{id_item} \n msisdn del origen {self.msisdn_token} \n request_domain/get_mapping_replace_values"))
            return plantilla_mobiquity, self.table_save_data, self.msisdn_token, 1

        except KeyError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else:
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = id_item,
                error_type = "KeyError",
                message = f"Error DR: {str(e)}",
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e
        except TypeError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = id_item,
                error_type = "KeyError",
                message = f"Error DR: {str(e)}",
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

            adapter_error =  ErrorServices(
                id_item,
                "ValueError",
                repr(f"Error DR: {str(e)}"),
                str(file_name+ " " + stack_trace),
                None,
                None,
                self.ambiente,
                self.table_proceso
            )
        
            adapter_error.log_error()

            return '', '', '', 0

        except Exception as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else:
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            raise CustomError(
                id_log = id_item,
                error_type = type(e).__name__,
                message = f"Error DR: {str(e)}",
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

    def get_nested_value(self, message_request_ewp, clave_ewp, split_ewp, valor_position_ewp,type_replace, valor_ewp, valor_comv,type_compare, auth_bytes,sel_value,table_save, is_identifier, type_token_api, id_item, api_name,date_capture,contexto_http,agente):
        utils = Utils()
        is_compare_estatico = 0
        matches_ewp = None
        result = ""


        if(type_replace != "A" and type_replace != "T" ):
            matches_ewp, flag_match_ewp = utils.buscar_en_json(message_request_ewp, clave_ewp, type_compare)
        else:
            if(clave_ewp == "uuid"):
                matches_ewp = uuid.uuid4()
            elif(clave_ewp == "externalReferenceId"):
                matches_ewp, flag_match_ewp = utils.generar_codigo()
            elif(clave_ewp == "auth"):
                flag_match_ewp = True
                auth_decode_bytes = base64.b64decode(auth_bytes)
                matches_ewp = auth_decode_bytes.decode('utf-8')
            elif(clave_ewp == "otp"):
                if(self.msisdn_token != "" and self.monto != ""):
                    #ARMAR EL REQUEST MOBIQUITY
                    request_otp = {
                        "api_name": "api_transaction_generate_passcode",
                        "Authorization": "Bearer ",
                        "data": {
                            "sender": {
                                "idValue": self.msisdn_token,
                                "idType": "mobileNumber",
                                "workspace": "SUBSCRIBER"
                            },
                            "extensibleFields": {
                                "source": "http-xml_awspdp"
                            },
                            "initiator": "sender",
                            "transactionAmount": self.monto,
                            "currency": 101,
                            "language": "es",
                            "externalReferenceId": ""
                        }
                    }
                    print(repr(f"{id_item} \n Consultando Payload Generar OTP ATM: {request_otp} \n request_domain/get_nested_value"))
                    lambda_adapter = LambdaAdapter(
                        cfg.ambiente[str(self.ambiente)],
                        request_otp,
                        "msisdn",
                        id_item,
                        "",
                        self.msisdn_token,
                        self.ambiente,
                        self.conexion,
                        self.table_proceso
                    )

                    mobiquity = lambda_adapter.peticion_mobiquity()
                    print(repr(f"{id_item} \n Respuesta API Payload Generar OTP ATM: {mobiquity} \n request_domain/get_nested_value"))
                    
                    if "response_mob" in mobiquity and mobiquity["response_mob"].get("code") is not None:
                        if(str(mobiquity["response_mob"]["code"]) == "200"):
                            print(repr(f"{id_item} \n Consulta exitosa Payload Generar OTP ATM: {mobiquity} \n request_domain/get_nested_value"))

                            query_buscar = f'''
                                SELECT IFNULL(REGEXP_SUBSTR(t.message , '(?<!\\\\d)\\\\d{{4}}(?!\\\\d)', 1, 1),"") as otp
                                FROM {cfg.DBNC["db_table_atm_otp"]} t
                                WHERE (t.created_at = (
                                        SELECT MAX(sub.created_at)
                                        FROM {cfg.DBNC["db_table_atm_otp"]} sub
                                        WHERE sub.msisdn = t.msisdn
                                        AND (sub.created_at IS NOT NULL AND sub.created_at <> '')
                                    )
                                    OR (t.created_at IS NULL OR t.created_at = '')
                                )AND 
                                t.msisdn <> ""
                                and t.msisdn = "{str(self.msisdn_token)}"
                                ORDER BY t.msisdn ASC, 
                                        CASE 
                                            WHEN t.created_at IS NULL OR t.created_at = '' THEN 1  
                                            ELSE 0                                               
                                        END ASC,
                                        t.created_at DESC;
                            '''
                            database_adapter_nc = DBAdapter("mdw", self.ambiente)
                            print(repr(f"{id_item} \n Consultando OTP ATM de la BD \n request_domain/get_nested_value"))

                            resp_mysql = database_adapter_nc.select_query(query_buscar, None)
                            print(repr(f"{id_item} \n Respuesta Consulta OTP ATM de la BD : {resp_mysql} \n request_domain/get_nested_value"))

                            if resp_mysql and "otp" in resp_mysql[0]:
                                matches_ewp = resp_mysql[0]["otp"]
                            else:
                                matches_ewp = ""
                    #OBTENER LA PASS DEL MSISDN

        if split_ewp and split_ewp != "":
            if(valor_position_ewp != "" or valor_position_ewp is not None) and (split_ewp == ":"):
                result = matches_ewp.split(str(split_ewp))[int(valor_position_ewp)]
            if(split_ewp == "<>"):
                if(utils.normalizar_str(clave_ewp) == utils.normalizar_str(valor_comv)):
                    result = valor_comv
            elif(split_ewp == "-/"):
                data_real = matches_ewp.replace("-", "")
                result = data_real.replace("/", "-")
            elif(split_ewp) == "r_-":
                result = matches_ewp.replace("_", "-")
            elif(valor_position_ewp != "" or valor_position_ewp is not None) and (split_ewp == "/"):
                data_real = matches_ewp.split(':', 1)[1]
                result = data_real.split(str(split_ewp), 1)[int(valor_position_ewp)]
            elif(valor_position_ewp != "" or valor_position_ewp is not None) and (split_ewp == "@"):
                data_real = matches_ewp.split(':', 1)[1]
                result = data_real.split(str(split_ewp))[int(valor_position_ewp)]
                if('/' in result):
                    result = result.split('/')[0]
            elif(split_ewp == "Devolucion"):
                if matches_ewp or isinstance(matches_ewp, str):
                    result = matches_ewp.replace("Devolucion", "").strip()
                else:
                    result = ""
            else:
                result = matches_ewp.split(str(split_ewp))[int(valor_position_ewp)]
        else:
            result = matches_ewp
            
        if(type_replace == 'E') and (str(result).strip() == str(valor_ewp).strip()):
            result = valor_comv
            is_compare_estatico = 1
        elif(type_replace == 'C'):
            if(valor_ewp is not None and valor_ewp != ""):
                result = (str(result + valor_ewp).upper()).strip()
            if(isinstance(result, str)):
                result = result.strip()
            is_compare_estatico = 1
        elif(type_replace == 'P'):
            if (isinstance(result, list) and ((valor_position_ewp != "" and valor_position_ewp is not None))):
                replace_posicion = result[int(valor_position_ewp)]
                result = replace_posicion

            if valor_ewp.startswith("_"):
                if(clave_ewp == "information.birth.province" and valor_ewp == "_STATE"):
                    
                    buscar_state = self.lista_ubligeo[
                        self.lista_ubligeo['city']
                        .str.fullmatch(unidecode(result.lower()), na=False)
                    ]

                    if(not buscar_state.empty):
                        result = buscar_state['state'].iloc[0]
                    else:
                        result = self.lista_ubligeo[
                            self.lista_ubligeo['city']
                            .str.contains(unidecode(result.lower()), na=False)
                        ]['state'].iloc[0]

                result = utils.format_text_if_state(result)
                result = result if result is not None or result == "None" else ""
            result = result or ""
            result = (str(result + valor_ewp)).upper().strip()

            is_compare_estatico = 1
        elif(type_replace == 'A'):
            if(valor_ewp is not None and valor_ewp != ""):
                result = (str(result + valor_ewp).upper()).strip()
            is_compare_estatico = 1
        elif(type_replace == 'T'):
            result = str(result)
            is_compare_estatico = 1
        else:
            is_compare_estatico = 0

        if(sel_value not in (None,"") and table_save  not in (None,"")):
            where_adicional = ""
            if(api_name == "transfer" and not re.search(r'\d', result) and split_ewp == "Devolucion"):
                original_datetime = datetime.strptime(date_capture, "%Y-%m-%dT%H:%M:%S.%fZ")
                datetime_minus = original_datetime - timedelta(seconds=cfg.config_database["time_refund_tranfer"], hours=cfg.config_database["time_Lima"])

                print(repr(f"{id_item} \n Reversa rango de fechas a buscar : {datetime_minus} \n request_domain/get_nested_value"))

                query_buscar_sendernote = f'''
                SELECT 
                    TRIM(IFNULL(sendernote_hist, '')) AS FROMMESSAGE 
                FROM {self.table_reverse_reverse_cahorros}
                WHERE 
                    id_log_rever = {id_item}
                LIMIT 1
                '''

                print(repr(f"{id_item} \n Consultando sendernote de la reversa: {query_buscar_sendernote} \n request_domain/get_nested_value"))
                database_adapter = DBAdapter("", self.ambiente)
                resp_mysql = database_adapter.select_query(query_buscar_sendernote, None)
                print(repr(f"{id_item} \n Respuesta sendernote de la reversa: {resp_mysql} \n request_domain/get_nested_value"))

                if(len(resp_mysql) != 0):
                    result = resp_mysql[0]["FROMMESSAGE"]
                    self.estado_reverse_reverse_cahorros = 1
                else:
                    result = ""
                    self.estado_reverse_reverse_cahorros = 0
            if("|" in sel_value):
                array_filter = sel_value.split("|")
                tabla_filter = table_save.split("|")
                valor_encontrado = result
                for index, item_array in enumerate(array_filter):
                    tabla = ""
                    if(tabla_filter[index] == "table_Values_Match"):
                        tabla = self.tabla_usuarios
                        where_adicional = ""
                    elif(tabla_filter[index] == "table_Values_Transaccion"):
                        tabla = self.tabla_transaccion
                        where_adicional = "AND estado = 'SUCCEEDED'"
                    elif(tabla_filter[index] == "findtransaccion_match"):
                        if(self.estado_reverse_reverse_cahorros == 1):
                            valor_encontrado = result
                            continue
                        tabla = self.findtransaccion_match


                    valor_encontrado = self.get_valor_tabla(item_array, valor_encontrado, tabla,id_item,where_adicional)
                result = valor_encontrado
            else:
                if(table_save == "table_Values_Match"):
                    tabla = self.tabla_usuarios
                    where_adicional = ""
                elif(table_save == "table_Values_Transaccion"):
                    tabla = self.tabla_transaccion
                    where_adicional = "AND estado = 'SUCCEEDED'"
                elif(table_save == "findtransaccion_match"):
                    tabla = self.findtransaccion_match

                result = self.get_valor_tabla(sel_value, result, tabla,id_item,where_adicional)
            if(clave_ewp == "financialtransactionid"):
                self.financialtransactionid = result
                if(self.financialtransactionid == '' or not self.financialtransactionid):
                    raise ValueError(repr(f"Error DR: {id_item} \n No exite la transaccion origen \n request_domain/get_nested_value"))



        if(clave_ewp == "financialtransactionid"):
            result = self.financialtransactionid
        elif(clave_ewp == "contexto_ewp"):
            result = contexto_http
        elif(clave_ewp == "idvalue_ewp"):
            if(api_name in ['cashin']):
                idvalue_ewp = cfg.LOGIN_AUTH["type_auth"]["agente"][str(agente)]["msisdn"]
                result = idvalue_ewp
            elif(api_name in ['payment','merchantpayment']):
                idvalue_ewp = cfg.LOGIN_AUTH["type_auth"]["agente"][str(agente)]["usuario"]
                result = idvalue_ewp
            elif(api_name in ['cashout']):
                idvalue_ewp = cfg.LOGIN_AUTH["type_auth"]["agente"]["VIRTUALINTEROPCFBIM"]["msisdn"]
                result = idvalue_ewp


        if(type_token_api == "msisdn" and str(is_identifier) == "1"):
            self.msisdn_token = result
        
        if(api_name == "atmcashout"):
            if(clave_ewp == "msisdn"):
                self.msisdn_token = result
            elif(clave_ewp == "amount"):
                self.monto = result
        elif(api_name == "transfer" and valor_comv == "none"):
            if(clave_ewp == "sendingfri"):
                self.sendingfri = result
                is_compare_estatico = 0
            elif(clave_ewp == "receivingfri"):
                self.receivingfri = result
                is_compare_estatico = 0
            elif(clave_ewp == "amount"):
                self.monto = result
                is_compare_estatico = 0
            elif(clave_ewp == "sendernote"):
                self.sendernote = result

        return result,is_compare_estatico
       

    def get_valor_tabla(self, item_array, valor_encontrado,table_save,id_item,where_adicional):
        result = ""
        if("," in item_array):

                data_valor = item_array.split(",")
                clave_filtro = str(data_valor[0])
                valor_filtro = str(valor_encontrado)
                campo_buscar = str(data_valor[1])

                query_buscar = f'''
                SELECT {str(campo_buscar)} FROM {str(table_save)}
                WHERE  {str(clave_filtro)} = '{str(valor_filtro)}' {where_adicional}
                LIMIT 1
                '''
                print(repr(f"{id_item} \n Consultando {campo_buscar}: {query_buscar} \n request_domain/get_valor_tabla"))
                database_adapter = DBAdapter("", self.ambiente)
                resp_mysql = database_adapter.select_query(query_buscar, None)
                print(repr(f"{id_item} \n Respuesta {campo_buscar}: {resp_mysql} \n request_domain/get_valor_tabla"))
                if(len(resp_mysql) != 0):
                    result = resp_mysql[0][str(campo_buscar)]
        
        return result

    def get_token_auth(self, auth):

        if isinstance(auth, dict):
            if auth.get("TYPE") == "Basic":
                return auth.get("VALUE")
    
        elif isinstance(auth, str):
            match = re.match(r"Basic\s+(.+)", auth)
            if match:
                return match.group(1)