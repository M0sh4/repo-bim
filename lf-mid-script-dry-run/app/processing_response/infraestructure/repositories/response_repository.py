from app.infraestructure.adapters.db_adapter import DBAdapter
from app.infraestructure.adapters.lambda_adapter import LambdaAdapter
import app.shared.config as cfg
import json
import time as t
from datetime import datetime
import pytz
tz = pytz.timezone("America/Lima")
class ResponseRepository:

    def __init__(
        self,
        result_mobiquity,
        result_compare_details,
        error_logs,
        table_save_data,
        api_name_ewp,
        ambiente,
        id_log,
        ejecution_time_request,
        ejecution_time_ppeticion_comv,
        ejecution_time_response,
        start_time_save_bd,
        start_time_total,
        conexion,
        id_execution,
        table_proceso
    ):
        self.database_adapter = DBAdapter("", ambiente)
        self.result_mobiquity = result_mobiquity
        self.result_compare_details = result_compare_details
        self.error_logs = error_logs
        self.table_save_data = table_save_data
        self.api_name_ewp = api_name_ewp
        self.ambiente = ambiente
        #self.tabla_log = cfg.ambiente[str(self.ambiente)]["table_log"]
        self.table_proceso = table_proceso
        self.tabla_log = self.table_proceso
        self.tabla_usuarios = cfg.ambiente[str(self.ambiente)]["table_Values_Match"]
        self.tabla_transaccion = cfg.ambiente[str(self.ambiente)]["table_Values_Transaccion"]
        self.id_log = id_log
        self.ejecution_time_request = ejecution_time_request
        self.ejecution_time_ppeticion_comv = ejecution_time_ppeticion_comv
        self.ejecution_time_response = ejecution_time_response
        self.start_time_save_bd = start_time_save_bd
        self.start_time_total =  start_time_total
        self.start_time_activation = 0
        self.end_time_activation = 0
        self.total_time_activation = 0
        self.conexion = conexion
        self.id_execution = id_execution
        
    def set_update_log(self):
        try:
            column_adicional = ""
            value_adicional = ""

            query1 = cfg.query_update_log_comviva.format(tabledata=self.tabla_log)
            query2 = cfg.query_insert_result_details.format(tabledata=self.tabla_log)

            param1 = (
                str(1),
                str(json.dumps(self.result_mobiquity["mobiquity"]["request_mob"])),
                str(json.dumps(self.result_mobiquity["mobiquity"]["response_mob"])),
                str(self.result_mobiquity["mobiquity"]["response_mob"]["statusCode"]),
                str(self.result_mobiquity["mobiquity"]["date_test_execution"]),
                self.result_mobiquity["is_result_equals"],
                "PROCESADO",
                str(self.ejecution_time_request),
                str(self.result_mobiquity["mobiquity"]["time_out_apisender"]),
                str(self.ejecution_time_response),
                str(self.ejecution_time_ppeticion_comv),
                int(self.result_mobiquity["id"])
            )

            param2 = [
                (
                    int(item["id_log"]),
                    (
                        None
                        if item["id_mapping"] == "" or item["id_mapping"] == "0"
                        else int(item["id_mapping"])
                    ),
                    (
                        None
                        if item["parent_id_mapping"] == ""
                        or item["parent_id_mapping"] == "0"
                        else int(item["parent_id_mapping"])
                    ),
                    item["index_array_ewp"],
                    item["index_array_mob"],
                    item["clave_ewp"],
                    item["valor_ewp"],
                    item["clave_mob"],
                    item["valor_mob"],
                    item["message_compare"],
                    int(item["is_result_equals"]),
                )
                for item in self.result_compare_details
            ]

            re_mysql = self.database_adapter.insert_query_results(
                query1, param1, query2, param2, self.id_log, self.api_name_ewp
            )

            print(repr(f"{self.id_log} \n Iniciando Guardar datos en el DR: {self.table_save_data} \n response_repository/set_update_log"))
            if self.table_save_data:
                print("validar self.table_save_data entro")
                tabla_name = ""
                if (
                    "transactionId_comv" in self.table_save_data
                    or "sendernote" in self.table_save_data
                    or "transactionId_ewp" in self.table_save_data
                ):
                    tabla_name = self.tabla_transaccion
                else:
                    tabla_name = self.tabla_usuarios
                    if(self.api_name_ewp == "activation"):
                        column_adicional = "active"
                        value_adicional = 1

                if (
                    tabla_name == self.tabla_usuarios
                    and str(
                        self.result_mobiquity["mobiquity"]["response_mob"]["statusCode"]
                    )
                    == "200"
                ) or (tabla_name == self.tabla_transaccion):
                    if self.api_name_ewp == "getaccountholderinfo":

                        query_buscar = f"""
                            SELECT COUNT(1) as conteo FROM {tabla_name}
                            WHERE mdn = '{self.table_save_data["mdn"]}'
                            and ctr_user IS NOT NULL
                            LIMIT 1
                        """

                        query_update = f"""
                            UPDATE {tabla_name}
                            SET
                                id_user_ewp = '{self.table_save_data["id_user_ewp"]}',
                                id_user_comv = '{self.table_save_data["id_user_comv"]}',
                                catcode = '{self.table_save_data["catcode"]}',
                                authpro = '{self.table_save_data["authpro"]}',
                                secpro = '{self.table_save_data["secpro"]}',
                                dni = '{self.table_save_data["dni"]}'
                            WHERE mdn = '{self.table_save_data["mdn"]}'
                        """

                        query_insert = f"""
                           INSERT INTO {tabla_name} (id_user_ewp, id_user_comv, catcode, authpro, secpro, mdn, id_log, dni) 
                           VALUES('{self.table_save_data["id_user_ewp"]}', '{self.table_save_data["id_user_comv"]}', '{self.table_save_data["catcode"]}', '{self.table_save_data["authpro"]}', '{self.table_save_data["secpro"]}','{self.table_save_data["mdn"]}', {self.result_mobiquity["id"]}, '{self.table_save_data["dni"]}')
                           ON DUPLICATE KEY UPDATE 
                                id_user_ewp = '{self.table_save_data["id_user_ewp"]}',
                                id_user_comv = '{self.table_save_data["id_user_comv"]}',
                                catcode = '{self.table_save_data["catcode"]}',
                                authpro = '{self.table_save_data["authpro"]}',
                                secpro = '{self.table_save_data["secpro"]}',
                                dni = '{self.table_save_data["dni"]}';
                        """

                        re_mysql3 = self.database_adapter.update_accountoinfo_query(
                            query_buscar,
                            query_update,
                            query_insert,
                            self.table_save_data["mdn"],
                            self.result_mobiquity["id"]
                        )

                        if re_mysql3 == 0:
                            request_activation = {
                                "api_name": "api_ums_user_change_authentication",
                                "data": {
                                    "requestedBy": "SELF",
                                    "authFactor": "PIN",
                                    "workspace": "SUBSCRIBER",
                                    "identifierType": "MSISDN",
                                    "identifierValue": str(self.table_save_data["mdn"]),
                                    "newAuthenticationValue": f"{cfg.ambiente[str(self.ambiente)]["p_default"]}",
                                    "confirmedAuthenticationValue": f"{cfg.ambiente[str(self.ambiente)]["p_default"]}",
                                    "oldAuthenticationValue": f"{cfg.ambiente[str(self.ambiente)]["p_migracion"]}"
                                },
                                "Authorization": "Bearer"
                            }

                            lambda_adapter =  LambdaAdapter(
                                cfg.ambiente[str(self.ambiente)],
                                request_activation,
                                "none", 
                                self.id_log,
                                "",
                                self.table_save_data["mdn"],
                                self.ambiente,
                                self.conexion,
                                self.table_proceso
                            )

                            print(repr(f"{self.id_log} \n Activacion de usuarios de migracion \n {request_activation} \n db_adapter/update_accountoinfo_query"))
                            self.start_time_activation = t.perf_counter()
                            mobiquity = lambda_adapter.peticion_mobiquity()
                            self.end_time_activation = t.perf_counter()
                            self.total_time_activation = self.end_time_activation - self.start_time_activation
                            print(repr(f"{self.id_log} \n Respuesta de Activacion de usuarios de migracion \n {mobiquity} \n db_adapter/update_accountoinfo_query"))

                            if "response_mob" in mobiquity and mobiquity["response_mob"].get("code") is not None:
                                if(str(mobiquity["response_mob"]["code"]) == "200"):

                                    query_update_activation = f"""
                                        UPDATE {self.tabla_usuarios}
                                        SET 
                                        ctr_user  = '{cfg.ambiente[str(self.ambiente)]["p_default"]}',
                                        active = 1
                                        WHERE 
                                        mdn = '{self.table_save_data["mdn"]}'
                                    """
                                    print(repr(f"{self.id_log} \n Actualizar pin de msisdn \n {query_update_activation} \n db_adapter/update_accountoinfo_query"))
                                    self.database_adapter.insert_query(query_update_activation, None)
                                    print(repr(f"{self.id_log} \n Actualizado pin de msisdn \n db_adapter/update_accountoinfo_query"))
                    else:
                        columnas = tuple(self.table_save_data.keys())
                        valores = tuple(
                            f"{val}" if isinstance(val, str) else str(val)
                            for val in self.table_save_data.values()
                        )

                        columnas = columnas + (
                            "id_log",
                        )  # Añadir la columna como tupla
                        valores = valores + (
                            int(self.result_mobiquity["id"]),
                        )  # Añadir el valor como tupla

                        if column_adicional != '' and value_adicional != '':
                            columnas += (column_adicional,)
                            valores += (value_adicional,)

                        # Crear la parte dinámica para el UPDATE
                        set_clause = ", ".join(
                            [
                                f"{key} = '{value}'"
                                for key, value in self.table_save_data.items()
                            ]
                        )

                        set_clause += f", id_log = {int(self.result_mobiquity["id"])}"

                        if column_adicional != '' and value_adicional != '':
                            set_clause += f", {column_adicional} = {value_adicional}"
    
                        query_duplicate = f"""
                        INSERT INTO {tabla_name} 
                        {str(columnas).replace("'","")}
                        VALUES {str(valores)}
                        ON DUPLICATE KEY UPDATE {set_clause};
                        """

                        re_mysql2 = self.database_adapter.insert_query_data_user(
                            query_duplicate, self.id_log
                        )
                

            end_time_save_bd = t.perf_counter()
            ejecution_time_save_bd = (end_time_save_bd - self.start_time_save_bd) - self.total_time_activation

            end_time_total = t.perf_counter()
            ejecution_time_total = end_time_total - self.start_time_total

            query3 = cfg.query_update_log_time.format(tabledata=self.tabla_log)
            param3 = (str(ejecution_time_total),str(ejecution_time_save_bd),self.id_log)
            re_mysql3 = self.database_adapter.insert_query(query3, param3)

            print(
                repr(f"{self.id_log} Tiempo de procesamiento del registro total: {ejecution_time_total:.4f} segundos  tiempo request: {self.ejecution_time_request:.4f}  tiempo peticion api sende: {self.ejecution_time_ppeticion_comv:.4f} tiempo response {self.ejecution_time_response:.4f}  guardar resultado: {ejecution_time_save_bd:.4f} \n main")
            )

            print(
                repr(f"{self.id_log} END PROCESO \n main")
            )
        except PermissionError as pe:
            print(repr(f"Error DR: {self.id_log} \n de permiso set_update_log: {pe}"))
            return False
        except Exception as e:
            raise Exception(repr(f"Error DR: {self.id_log} \n inesperado set_update_log: {e}"))

    def set_update_log_error(self):
        try:
            timestamp_error = (datetime.now(tz)).strftime('%Y-%m-%d %H:%M:%S')
            query1 = cfg.query_update_log_comviva_error.format(tabledata=self.tabla_log)
            param1 = (
            '1',
            str(timestamp_error),
            self.id_execution,
            'ERROR',
            self.id_log
            )

            re_mysql4 = self.database_adapter.insert_query(query1,param1)
            
        except PermissionError as pe:
            print(repr(f"Error DR: {self.id_log} \n de permiso set_update_log_error: {pe}"))
            return False
        except Exception as e:
            raise Exception(repr(f"Error DR: {self.id_log} \n inesperado set_update_log_error: {e}"))
        
class ResponseRepositoryReset:
    def __init__(self,ids_tuple, ambiente, id_execution, conexion, table_proceso):
        self.database_adapter = DBAdapter("", ambiente)
        self.ambiente = ambiente
        #self.tabla_log = cfg.ambiente[str(self.ambiente)]["table_log"]
        self.tabla_log = table_proceso
        self.tabla_usuarios = cfg.ambiente[str(self.ambiente)]["table_Values_Match"]
        self.tabla_transaccion = cfg.ambiente[str(self.ambiente)]["table_Values_Transaccion"]
        self.conexion = conexion
        self.ids_tuple = ids_tuple

    def set_reset_status_log(self):
        try:
            query1 = cfg.update_reset_estado_log.format(tabledata=self.tabla_log)
            param1 = (self.ids_tuple,)

            print(f"reset status query1:{query1}  param1: {tuple(self.ids_tuple)}")

            re_mysql5 = self.database_adapter.insert_query(query1,param1)

        except PermissionError as pe:
            print(repr(f"Error DR: \n de permiso set_reset_status_log: {pe}"))
            return False
        except Exception as e:
            print(repr(f"Error DR: \n inesperado set_reset_status_log: {e}"))