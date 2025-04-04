''' Valida input/output'''
import json
import traceback
from pathlib import Path
import ulid
from app.error.domain.error_model import CustomError
from app.shared.utils import Utils

class ResponseDomain:
    ''' Class MappingDomain'''
    def __init__(self):
        self.compare_details = []
        self.message_compare_ok = "Los valores de los campos coinciden"
        self.no_compare_details = []
        self.error_logs = []
        self.table_save_data = {}

    def get_response_ewp_in_json(self, response_ewp, id_log):
        try:
            statuscode_ewp = ""
            if(response_ewp != "" and response_ewp is not None):
                response_ewp_message = response_ewp.get("message", response_ewp.get("body"))
                statuscode_ewp = str(response_ewp["code"])

                utils = Utils()
                response_convert = ""

                if(utils.is_date_xml(response_ewp_message) and utils.es_posible_xml(response_ewp_message)):
                    response_convert = utils.traslate_xml_in_json(response_ewp_message)

                if(str(statuscode_ewp) == "200" and isinstance(response_convert, str)):
                    response_convert = utils.deserializacion_json(response_convert)

            else:
                response_convert = ""
                statuscode_ewp = "500"

            print(repr(f"{id_log} \n Response EWP json body : {response_convert} \n response_domain/get_response_ewp_in_json"))
            print(repr(f"{id_log} \n Response EWP json status code: {statuscode_ewp} \n response_domain/get_response_ewp_in_json"))
            return response_convert, statuscode_ewp
        
        except ValueError as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else: 
                stack_trace = original_stack_trace
  
            file_name = Path(__file__).name
            raise CustomError(
                id_log = id_log,
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
                id_log = id_log,
                error_type = type(e).__name__,
                message = f"Error DR: {str(e)}",
                stack_trace = str(file_name+ " " + stack_trace),
                id_mapping = None,
                clave_ewp = None
            ) from e

    def get_compare_ewp_mob(self, service):
        # Comparar status y message - EWP VS MOBIQUITY
        self.get_compare_status_message(service.statuscode, service.response_mobiquity["statusCode"], service.id_log, service.response_mobiquity)

        if(service.response_message_ewp != "" and isinstance(service.response_message_ewp, dict)):
            # Mapping de comparaciones directa - EWP VS MOBIQUITY
            lista_mapping_direct = service.lista_mapping[
                (service.lista_mapping["type_compare"] == "directa") &
                (
                    (service.lista_mapping["parent_id_mapping"] == 0) |
                    (service.lista_mapping["parent_id_mapping"].isnull())
                )
            ]

            # Mapping de comparaciones de arreglos - EWP VS MOBIQUITY
            lista_mapping_arrays = service.lista_mapping[
                (service.lista_mapping["type_compare"] == "arreglos") &
                (service.lista_mapping["parent_id_mapping"] == 0)
            ]

            # Comparaciones directas
            if not lista_mapping_direct.empty:
                for _, row_mapping_direct in lista_mapping_direct.iterrows():
                    self.get_compare_direct(row_mapping_direct, service.response_message_ewp, service.response_body_mobiquity, service.id_log, service.response_mobiquity["statusCode"])

            # Comparaciones de arreglos
            if not lista_mapping_arrays.empty:
                for _, row_mapping_arrays in lista_mapping_arrays.iterrows():
                    self.get_compare_arrays(row_mapping_arrays, service.response_message_ewp, service.response_body_mobiquity, service.id_log, service.lista_mapping)


        is_result_equals = 0 if any(item["is_result_equals"] == 0 for item in self.compare_details) else 1


        print(repr(f"{service.id_log} \n Detalle de Comparacion de Response EWP vs Comviva \n {self.compare_details} \n response_domain/get_compare_ewp_mob"))
        print(repr(f"{service.id_log} \n Datos de Response a guardar en tabla DR  \n {self.table_save_data} \n response_domain/get_compare_ewp_mob"))

        return self.compare_details, is_result_equals, self.error_logs, self.table_save_data
       
    def get_compare_status_message(self, statuscode_ewp, statuscode_mob, id_log, response_mobiquity):
        try:
            flag_status_code = 0

            # 1 validación Code Status EWP VS MOBIQUITY
            if str(statuscode_ewp) == str(statuscode_mob):
                flag_status_code = 1


            self.set_result_compare("statusCode",
                                    "statusCode",
                                    str(statuscode_ewp),
                                    str(statuscode_mob),
                                    flag_status_code,
                                    self.message_compare_ok,
                                    id_log,
                                    "",
                                    "",
                                    "",
                                    "")

            # 2 validación message error Mobiquity
            if int(statuscode_mob) != 200:
                
                if "body" in response_mobiquity:
                    if (
                        "errors" in response_mobiquity["body"]
                        and isinstance(response_mobiquity["body"]["errors"], list)
                        and len(response_mobiquity["body"]["errors"]) > 0
                    ):
                        message_error = (
                            "Error: " + response_mobiquity["body"]["errors"][0]["message"]
                        )
                    elif "messageCore" in response_mobiquity["body"]:
                        message_error = "messageCore: " + str(
                            response_mobiquity["body"]["messageCore"]
                        )
                    else:
                        message_error = "No hay errors ni messageCore en body."
                elif "message" in response_mobiquity:
                    message_error = "message: " + str(response_mobiquity["message"])
                else:
                    message_error = "No se encontró mensaje de error."
                
                message_compare = "Los valores de los campos no coinciden"
                self.set_result_compare("message","message",str(""),str(message_error),flag_status_code, message_compare,id_log,"","","","")

        except ValueError as ve: 
            self.log_error(id_log, repr(f"Error DR: {id_log} \n valor en el match de statusCode: {str(ve)} \n response_domain/get_compare_ewp_mob"), ve, None, None)
        except IndexError as ie:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n índice en el match de statusCode: {str(ie)} \n response_domain/get_compare_ewp_mob"), ie, None, None)
        except KeyError as ke:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n clave en el match de statusCode: {str(ke)} \n response_domain/get_compare_ewp_mob"), ke, None, None)
        except TypeError as te:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n tipo en el match de statusCode: {str(te)} \n response_domain/get_compare_ewp_mob"), te, None, None)
        except AttributeError as ae:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n atributo en el match de statusCode: {str(ae)} \n response_domain/get_compare_ewp_mob"), ae, None, None)
        except Exception as e:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n general encontrado en match de statusCode: {str(e)} \n response_domain/get_compare_ewp_mob"), e, None, None)

    def get_compare_direct(self, row_mapping_direct, response_ewp, response_body_mobiquity, id_log, statucode_comviva):
        '''
            Comparación directa de claves EWP - MOBIQUITY
        '''
        try:
            is_compare_estatico = 0
            utils = Utils()
            response_message_ewp = response_ewp
            if(not isinstance(response_ewp, dict)):
                response_message_ewp = json.loads(response_ewp)

            valor_ewp, flag_match_ewp = utils.buscar_en_json(response_message_ewp, row_mapping_direct["clave_ewp"], row_mapping_direct["type_compare"])
            
            if row_mapping_direct["split_ewp"] and row_mapping_direct["split_ewp"] != "":
                if(row_mapping_direct["valor_position_ewp"] != "" or row_mapping_direct["valor_position_ewp"] is not None) and (row_mapping_direct["split_ewp"] == "/"):
                    data_real = valor_ewp.split(':', 1)[1]
                    valor_ewp = data_real.split(str(row_mapping_direct["split_ewp"]), 1)[int(row_mapping_direct["valor_position_ewp"])]

            if(row_mapping_direct["type_replace"] == 'E'):
                if( (str(valor_ewp).strip() == str(row_mapping_direct["valor_ewp"]).strip())):
                    is_compare_estatico = 1
                else:
                    is_compare_estatico = 0
            elif(row_mapping_direct["type_replace"] == 'P'):
                if (not isinstance(valor_ewp, str) and ((row_mapping_direct["valor_position_ewp"] != "" and row_mapping_direct["valor_position_ewp"] is not None))):
                    replace_posicion = valor_ewp[int(row_mapping_direct["valor_position_ewp"])]
                    valor_ewp = str(replace_posicion + row_mapping_direct["valor_ewp"]).upper()
                elif(row_mapping_direct["valor_position_ewp"] == "0" and isinstance(valor_ewp, str)):
                    row_mapping_direct["is_compare"] = 0
                is_compare_estatico = 1
            else:
                is_compare_estatico = 1
            
            valor_mob, flag_match_mob = utils.buscar_en_json(response_body_mobiquity, row_mapping_direct["clave_comv"], row_mapping_direct["type_compare"])
            # Verificar si se encontró un valor
            if(is_compare_estatico == 1):
                if flag_match_ewp:
                    flag_compare_direct = 0
                    message_compare = ""
                    is_compare = utils.compare_values_formate(valor_ewp, valor_mob, row_mapping_direct["valor_ewp"], row_mapping_direct["valor_comv"], row_mapping_direct["type_replace"])

                    if(row_mapping_direct["is_compare"] == 1):
                        if(is_compare):
                            flag_compare_direct = 1
                            message_compare = "Los valores de los campos coinciden"
                        else:
                            message_compare = "Los valores de los campos no coinciden"

                        self.set_result_compare(str(row_mapping_direct["clave_ewp"]),
                                                str(row_mapping_direct["clave_comv"]),
                                                str(valor_ewp),
                                                str(valor_mob),
                                                flag_compare_direct,
                                                message_compare,
                                                id_log,
                                                "",
                                                "",
                                                str(row_mapping_direct["id_mapping"]),
                                                str(row_mapping_direct["parent_id_mapping"])
                                                )
                
                if((row_mapping_direct["is_saved"] not in (None,"")) and (row_mapping_direct["table_save"] not in (None, ""))):
                    valor_mob_table = valor_mob
                    # if(valor_mob == "None" or valor_mob is None) and ():
                    # valor_mob_table = ulid.new()

                    if "," in row_mapping_direct["is_saved"]:  # Verifica si existe una coma
                        data_valor = row_mapping_direct["is_saved"].split(",")  # Divide en dos partes
                        self.table_save_data[str(data_valor[0]).strip()] = str(valor_ewp)

                        if((str(valor_mob_table) == "None") and (str(data_valor[1]).strip() == "transactionId_comv")):
                            valor_mob_table = ulid.ulid()

                        self.table_save_data[str(data_valor[1]).strip()] = str(valor_mob_table)
                    else:
                        if((str(valor_mob_table) == "None" or valor_mob_table is None) and (row_mapping_direct["is_saved"].strip() == "transactionId_comv")):
                            valor_mob_table = ulid.ulid()

                        self.table_save_data[row_mapping_direct["is_saved"].strip()] = str(valor_mob_table)

        except ValueError as ve: 
            self.log_error(id_log, repr(f"Error DR: {id_log} \n valor en el match directo: {str(ve)} \n response_domain/get_compare_direct"), ve, str(row_mapping_direct["id_mapping"]), str(row_mapping_direct["clave_ewp"]))
        except IndexError as ie:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n índice en el match directo: {str(ie)} \n response_domain/get_compare_direct"), ie, str(row_mapping_direct["id_mapping"]), str(row_mapping_direct["clave_ewp"]))
        except KeyError as ke:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n clave en el match directo: {str(ke)} \n response_domain/get_compare_direct"), ke, str(row_mapping_direct["id_mapping"]), str(row_mapping_direct["clave_ewp"]))
        except TypeError as te:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n tipo en el match directo: {str(te)} \n response_domain/get_compare_direct"), te, str(row_mapping_direct["id_mapping"]), str(row_mapping_direct["clave_ewp"]))
        except AttributeError as ae:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n atributo en el match directo: {str(ae)} \n response_domain/get_compare_direct"), ae, str(row_mapping_direct["id_mapping"]), str(row_mapping_direct["clave_ewp"]))
        except Exception as e:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n general encontrado en match directo: {str(e)} \n response_domain/get_compare_direct"), e, str(row_mapping_direct["id_mapping"]), str(row_mapping_direct["clave_ewp"]))

    def get_compare_arrays(self, row_mapping_arrays, response_message_ewp, response_body_mobiquity, id_log, lista_mapping):
        try:
            ''' Comparación de arrays de claves EWP - MOBIQUITY '''
            utils = Utils()
            list_array_ewp, flag_match_list_ewp = utils.buscar_en_json(response_message_ewp, row_mapping_arrays["clave_ewp"], row_mapping_arrays["type_compare"])
            if flag_match_list_ewp:
                list_array_mob, flag_match_list_mob = utils.buscar_en_json(response_body_mobiquity, row_mapping_arrays["clave_comv"], row_mapping_arrays["type_compare"])
                
                child_identifiers = lista_mapping[
                    (lista_mapping["parent_id_mapping"] == row_mapping_arrays["id_mapping"]) & 
                    (lista_mapping["is_identifier"] == 1)
                ]

                child_comparisons = lista_mapping[
                    (lista_mapping["parent_id_mapping"] == row_mapping_arrays["id_mapping"])
                ]

                combinaciones_unicas = set()

                for i, array_ewp in enumerate(list_array_ewp):
                    match_found = False
                    self.no_compare_details.clear()

                    if(list_array_mob is not None):
                        for j, array_mob in enumerate(list_array_mob):
                            flag_match = True
                            
                            # Comparar identificadores
                            for _, row_identifiers in child_identifiers.iterrows():
                                valor_ident_ewp, flag_match_ewp = utils.buscar_en_json(array_ewp, row_identifiers["clave_ewp"], row_identifiers["type_compare"])
                                if flag_match_ewp:

                                    valor_ident_mob, flag_match_mob = utils.buscar_en_json(array_mob, row_identifiers["clave_comv"], row_identifiers["type_compare"])

                                    try:
                                        flag_match = utils.compare_values_formate(valor_ident_ewp, valor_ident_mob, row_identifiers["valor_ewp"], row_identifiers["valor_comv"], row_identifiers["type_replace"])

                                        if not flag_match:
                                            combinacion_unica = (i, row_identifiers["id_mapping"], row_identifiers["clave_ewp"])
                                            if combinacion_unica not in combinaciones_unicas:
                                                combinaciones_unicas.add(combinacion_unica)
                                                result_no_compare = {
                                                    "id_log": str(id_log),
                                                    "id_mapping": str(row_identifiers["id_mapping"]),
                                                    "parent_id_mapping": str(row_identifiers["parent_id_mapping"]),
                                                    "index_array_ewp": str(i),
                                                    "index_array_mob": "",
                                                    "clave_ewp": str((row_mapping_arrays["clave_ewp"]).replace("*", str(i)) + "." + row_identifiers["clave_ewp"]),
                                                    "valor_ewp": str(valor_ident_ewp),
                                                    "clave_mob": "",
                                                    "valor_mob": "",
                                                    "message_compare": "No se encontró match de la lista",
                                                    "is_result_equals": 0,
                                                }
                                                self.no_compare_details.append(result_no_compare)

                                    except ValueError as ve:
                                        flag_match = False
                                        self.log_error(id_log, repr(f"Error DR: {id_log} \n valor en el match identificador de arreglos: {str(ve)} \n response_domain/get_compare_arrays"), ve, row_identifiers["id_mapping"], row_identifiers["clave_ewp"])
                                        break
                                    except IndexError as ie:
                                        flag_match = False
                                        self.log_error(id_log, repr(f"Error DR: {id_log} \n índice en el match identificador de statusCode: {str(ie)} \n response_domain/get_compare_arrays"), ie, row_identifiers["id_mapping"], row_identifiers["clave_ewp"])
                                        break
                                    except KeyError as ke:
                                        flag_match = False
                                        self.log_error(id_log, repr(f"Error DR: {id_log} \n clave en el match identificador de statusCode: {str(ke)} \n response_domain/get_compare_arrays"), ke, row_identifiers["id_mapping"], row_identifiers["clave_ewp"])
                                        break
                                    except TypeError as te:
                                        flag_match = False
                                        self.log_error(id_log, repr(f"Error DR: {id_log} \n tipo en el match identificador de statusCode: {str(te)} \n response_domain/get_compare_arrays"), te, row_identifiers["id_mapping"], row_identifiers["clave_ewp"])
                                        break
                                    except AttributeError as ae:
                                        flag_match = False
                                        self.log_error(id_log, repr(f"Error DR: {id_log} \n atributo en el match identificador de statusCode: {str(ae)} \n response_domain/get_compare_arrays"), ae, row_identifiers["id_mapping"], row_identifiers["clave_ewp"])
                                        break
                                    except Exception as e:
                                        flag_match = False
                                        self.log_error(id_log, repr(f"Error DR: {id_log} \n general encontrado en match identificador de statusCode: {str(e)} \n response_domain/get_compare_arrays"), e, row_identifiers["id_mapping"], row_identifiers["clave_ewp"])
                                        break

                            
                            if flag_match:
                                match_found = True
                                self.no_compare_details.clear()  # Limpiar detalles no comparables
                                
                                # Comparar claves hijas que no son identificadores
                                for _, row_child in child_comparisons.iterrows():
                                    try:
                                        valor_child_ewp, flag_match_child_ewp = utils.buscar_en_json(array_ewp, row_child["clave_ewp"], row_child["type_compare"])
                                        valor_child_mob, flag_match_child_mob = utils.buscar_en_json(array_mob, row_child["clave_comv"], row_child["type_compare"])
                                        flag_compare_direct = 0
                                        message_compare = ""
                                        is_compare = utils.compare_values_formate(valor_child_ewp, valor_child_mob, row_child["valor_ewp"], row_child["valor_comv"], row_child["type_replace"])
                                        

                                        if row_child["is_compare"] == 1:
                                            if is_compare:
                                                flag_compare_direct = 1
                                                message_compare = "Los valores de los campos coinciden"
                                            else:
                                                message_compare = "Los valores de los campos no coinciden"

                                            self.set_result_compare(
                                                str((row_mapping_arrays["clave_ewp"]).replace("*", str(i)) + "." + row_child["clave_ewp"]),
                                                str((row_mapping_arrays["clave_comv"]).replace("*", str(j)) + "." + row_child["clave_comv"]),
                                                str(valor_child_ewp),
                                                str(valor_child_mob),
                                                flag_compare_direct,
                                                message_compare,
                                                id_log,
                                                i, j,
                                                row_child["id_mapping"],
                                                row_child["parent_id_mapping"]
                                            )
                                    except ValueError as ve:
                                        flag_match = False
                                        self.log_error(id_log, repr(f"Error DR: {id_log} \n Error de valor en el match de arreglos de arreglos: {str(ve)} \n response_domain/get_compare_arrays"), ve, row_child["id_mapping"], str((row_mapping_arrays["clave_ewp"]).replace("*", str(i)) + "." + row_child["clave_ewp"]))
                                        break
                                    except IndexError as ie:
                                        flag_match = False
                                        self.log_error(id_log, repr(f"Error DR: {id_log} \n Error de índice en el match de arreglos de statusCode: {str(ie)} \n response_domain/get_compare_arrays"), ie, row_child["id_mapping"], str((row_mapping_arrays["clave_ewp"]).replace("*", str(i)) + "." + row_child["clave_ewp"]))
                                        break
                                    except KeyError as ke:
                                        flag_match = False
                                        self.log_error(id_log, repr(f"Error DR: {id_log} \n Error de clave en el match de arreglos de statusCode: {str(ke)} \n response_domain/get_compare_arrays"), ke, row_child["id_mapping"], str((row_mapping_arrays["clave_ewp"]).replace("*", str(i)) + "." + row_child["clave_ewp"]))
                                        break
                                    except TypeError as te:
                                        flag_match = False
                                        self.log_error(id_log, repr(f"Error DR: {id_log} \n Error de tipo en el match de arreglos de statusCode: {str(te)} \n response_domain/get_compare_arrays"), te, row_child["id_mapping"], str((row_mapping_arrays["clave_ewp"]).replace("*", str(i)) + "." + row_child["clave_ewp"]))
                                        break
                                    except AttributeError as ae:
                                        flag_match = False
                                        self.log_error(id_log, repr(f"Error DR: {id_log} \n Error de atributo en el match de arreglos de statusCode: {str(ae)} \n response_domain/get_compare_arrays"), ae, row_child["id_mapping"], str((row_mapping_arrays["clave_ewp"]).replace("*", str(i)) + "." + row_child["clave_ewp"]))
                                        break
                                    except Exception as e:
                                        flag_match = False
                                        self.log_error(id_log, repr(f"Error DR: {id_log} \n Error general encontrado en match de arreglos de statusCode: {str(e)} \n response_domain/get_compare_arrays"), e, row_child["id_mapping"], str((row_mapping_arrays["clave_ewp"]).replace("*", str(i)) + "." + row_child["clave_ewp"]))
                                        break
                                break  # Salir del loop si se encuentra un match
                    else:
                        for _, row_identifiers in child_identifiers.iterrows():
                                valor_ident_ewp, flag_match_ewp = utils.buscar_en_json(array_ewp, row_identifiers["clave_ewp"], row_identifiers["type_compare"])
                            
                                match_found = False
                                result_no_compare = {
                                    "id_log": str(id_log),
                                    "id_mapping": str(row_identifiers["id_mapping"]),
                                    "parent_id_mapping": str(row_identifiers["parent_id_mapping"]),
                                    "index_array_ewp": str(i),
                                    "index_array_mob": "",
                                    "clave_ewp": str((row_mapping_arrays["clave_ewp"]).replace("*", str(i)) + "." + row_identifiers["clave_ewp"]),
                                    "valor_ewp": str(valor_ident_ewp),
                                    "clave_mob": "",
                                    "valor_mob": "",
                                    "message_compare": "No se encontró match de la lista",
                                    "is_result_equals": 0,
                                }

                                self.no_compare_details.append(result_no_compare)
           
                    # Solo después de iterar todos los j se acumulan los detalles no comparados
                    if not match_found:
                        self.compare_details.extend(self.no_compare_details)
                        combinaciones_unicas.clear()

        except ValueError as ve:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n valor en el match de arreglos de arreglos: {str(ve)} \n response_domain/get_compare_arrays"), ve, row_mapping_arrays["id_mapping"], row_mapping_arrays["clave_ewp"])
        except IndexError as ie:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n índice en el match de arreglos de statusCode: {str(ie)} \n response_domain/get_compare_arrays"), ie, row_mapping_arrays["id_mapping"], row_mapping_arrays["clave_ewp"])
        except KeyError as ke:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n clave en el match de arreglos de statusCode: {str(ke)} \n response_domain/get_compare_arrays"), ke, row_mapping_arrays["id_mapping"], row_mapping_arrays["clave_ewp"])
        except TypeError as te:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n tipo en el match de arreglos de statusCode: {str(te)} \n response_domain/get_compare_arrays"), te, row_mapping_arrays["id_mapping"], row_mapping_arrays["clave_ewp"])
        except AttributeError as ae:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n atributo en el match de arreglos de statusCode: {str(ae)} \n response_domain/get_compare_arrays"), ae, row_mapping_arrays["id_mapping"], row_mapping_arrays["clave_ewp"])
        except Exception as e:
            self.log_error(id_log, repr(f"Error DR: {id_log} \n general encontrado en match de arreglos de statusCode: {str(e)} \n response_domain/get_compare_arrays"), e, row_mapping_arrays["id_mapping"], row_mapping_arrays["clave_ewp"])

    def set_result_compare(self, clave_ewp, clave_mob, valor_ewp, valor_mob, flag, message,id_log,index_array_ewp,index_array_mob,id_mapping,parent_id_mapping):
            result_compare = {
                "id_log":str(id_log),
                "id_mapping":str(id_mapping),
                "parent_id_mapping":str(parent_id_mapping),
                "index_array_ewp":str(index_array_ewp),
                "index_array_mob":str(index_array_mob),
                "clave_ewp": str(clave_ewp),
                "valor_ewp": str(valor_ewp),
                "clave_mob": str(clave_mob),
                "valor_mob": str(valor_mob),
                "message_compare": str(message),
                "is_result_equals": flag
            }
            print(repr(f"{id_log} \n Response comparacion de campos \n {result_compare} \n response_domain/set_result_compare"))
            self.compare_details.append(result_compare)


    def log_error(self, id_log, message, error, id_mapping, clave_ewp):
        original_stack_trace = traceback.format_exc()
        line_pos = original_stack_trace.find("line")
        stack_trace = original_stack_trace[line_pos:] if line_pos != -1 else original_stack_trace
        print(repr(f"{message}"))
        file_name = Path(__file__).name
        custom_error = CustomError(
            id_log=id_log,
            error_type=type(error).__name__,
            message=f"{str(message)}",
            stack_trace=str(file_name + " " + stack_trace),
            id_mapping=id_mapping,
            clave_ewp=clave_ewp
        )
        self.error_logs.append(custom_error)


        