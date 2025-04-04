"""Main"""

import asyncio
import time as t
import traceback
import sys
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from aws_xray_sdk.core import xray_recorder

import app.shared.config as cfg
#from test_activation import Activation_user
from app.error.application.error_services import ErrorServices
from app.infraestructure.adapters.lambda_adapter import LambdaAdapter
from app.log_ewp.application.ewp_services import EWPService
from app.mapping_config.application.mapping_services import MappingService
from app.plantilla_request_mob.application.plantilla_services import PlantillaService
from app.processing_request.application.request_services import RequestService
from app.processing_response.application.response_services import ResponseService
from app.processing_response.infraestructure.repositories.response_repository import (
    ResponseRepository,ResponseRepositoryReset
)
from app.error.domain.error_model import CustomError



class DryRunMain:
    """CLASE DRYRUN PROCESO GENERAL"""

    def __init__(self, event_data = None):
        self.event_data = event_data
        custom_body = event_data.get('body', '{}')
        print(f"INICIO DR {custom_body}")
        self.proceso_dr = custom_body['proceso_dr'] #activation_migrate
        self.flujo_api = custom_body['flujo_api']
        self.id_logs = custom_body['id_log']
        self.ambiente = custom_body['ambiente']
        self.conexion = custom_body['conexion']
        self.start_date = custom_body['start_date']
        self.end_date = custom_body['end_date']
        self.table_proceso = custom_body['table']

        self.queue = asyncio.Queue()
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.queue_limit = 2  # 20
        self.queue_limit_sincrona = 2  # 20
        self.mapping_service = MappingService(self.ambiente)
        self.plantilla_service = PlantillaService(self.ambiente)
        self.ewp_service = EWPService(self.ambiente, self.table_proceso)
        self.id_execution = None
        self.lista_mapping = None
        self.lista_plantilla_mobiquity = cfg.plantilla_comviva_dryrun #None
        self.type_token = None
        self.error_log = {}
        self.error_in_query = False
        self.lista_ubligeo = None
        self.lista_log = []
        self.timer_start = None
        self.stop_execution = False
        self.response_mob = None

    async def pre_dryrun_main(self):
        """Consulta de las configuraciones pre DryRun"""
        self.timer_start = t.time()  # Inicia el temporizador
        execution_time_limit = 13 * 60  # 15 minutos en segundos
        grace_period = 3 * 60  # 5 minutos en segundos
        # 1: Consultar congifuraciones principales para el proceso DryRun

        #   1.1: Consultar Mapping de claves EWP VS Mobiquity
        self.lista_mapping, self.type_token = (
            self.mapping_service.get_mapping_ewp_comviva(
                self.start_date, self.end_date, cfg.format_fecha
            )
        )
        #   1.2: Consultar Plantillas Request Mobiquity"
        #self.lista_plantilla_mobiquity = (
        #    self.plantilla_service.get_plantilla_json_mobiquity()
        #)

        #self.lista_ubligeo = self.plantilla_service.get_tabla_ubligeo()

        #   1.3. Consultar registros EWP e ir colocando en cola
        flg_async = False
        if(flg_async):
            consulta_task = asyncio.create_task(self.get_ewp_queue())
            await self.process_list_queue()
            await consulta_task
        else:
            if(self.proceso_dr == "activation_migrate"):
                print("activacion migrate")
                # while not self.stop_execution:

                #     # Validación de tiempo antes de comenzar la iteración (al inicio del while)
                #     elapsed_time = t.time() - self.timer_start
                #     time_remaining = execution_time_limit - elapsed_time
                #     if time_remaining <= grace_period:
                #         print(f"Quedan {time_remaining:.2f} segundos antes de procesar más registros. Deteniendo ejecución.")
                #         self.stop_execution = True
                #         break  # Detener la ejecución del while

                #     # Obtener los siguientes 10 registros
                #     list_users = self.ewp_service.get_select_users_sincrona(self.table_proceso, self.id_logs, self.flujo_api, self.queue_limit_sincrona)

                #     # Si no hay más registros, finalizar el bucle
                #     if not list_users:
                #         print(repr("No se encontraron más registros. Terminando la ejecución."))
                #         break
                    
                #     registros_pendientes = []
                #     # Procesar cada registro del lote uno por uno
                #     for record in list_users:
                #         # Validación de tiempo antes de procesar cada registro
                #         elapsed_time = t.time() - self.timer_start
                #         time_remaining = execution_time_limit - elapsed_time
                #         if time_remaining <= grace_period:
                #             print(f"Quedan {time_remaining:.2f} segundos después de procesar un registro. Deteniendo ejecución.")
                            
                #             # Capturar los registros no procesados (desde el registro actual hasta el final de list_ewp)
                #             registros_pendientes = list_users[list_users.index(record):]  # Registros pendientes desde el actual

                #             # Manejar los registros pendientes
                #             self.handle_pendientes(registros_pendientes)

                #             # Detener la ejecución de ambos bucles
                #             self.stop_execution = True
                #             break  # Salir del bucle for
                
                #         # Actualizar estado del registro
                #         self.ewp_service.get_update_estado_user_sincrona(record["id"],self.table_proceso)
                        

                #         active_usuario = Activation_user(record["fri"])
                #         # Procesar el registro con dryrun_main
                #         active_usuario.activar_usario_migrado()

                #     if self.stop_execution:
                #         print("Ejecución detenida por límite de tiempo.")
                #         break  # Salir del bucle while si ya se ha detenido
                    
                #     list_users = []
                #     print("Lote procesado, consultando más registros...")
            elif(self.proceso_dr == "proceso_dryrun"):
                await self.process_encolamiento(execution_time_limit, grace_period)
            elif(self.proceso_dr == "proceso_stress"):
                self.process_stress()
            else:
                print(f"Proceso {self.proceso_dr} no reconocido.")
     
        return self.response_mob

    async def process_encolamiento(self, execution_time_limit, grace_period):
        """EJECUCION EN COLA SINCRONA"""
        registros_pendientes = []
        while not self.stop_execution:
            # Validación de tiempo antes de comenzar la iteración (al inicio del while)
            elapsed_time = t.time() - self.timer_start
            time_remaining = execution_time_limit - elapsed_time
            if time_remaining <= grace_period:
                print(f"Quedan {time_remaining:.2f} segundos antes de procesar más registros. Deteniendo ejecución.")
                self.stop_execution = True
                break

            # Obtener los siguientes 10 registros
            list_ewp = self.ewp_service.get_select_log_sincrona(limit=self.queue_limit_sincrona, flujo_api = self.flujo_api, id_logs = self.id_logs)
            #ids_tuple = tuple(int(record["id"]) for record in list_ewp if "id" in record and record["id"] is not None)

            #async with aiofiles.open("IDTUPLES.txt", "a", encoding="utf-8") as archivo:
            #    await archivo.write(str(ids_tuple) + "\n")

            # Si no hay más registros, finalizar el bucle
            if not list_ewp:
                print(repr("No se encontraron más registros. Terminando la ejecución."))
                break
            
            registros_pendientes = []
            # Procesar cada registro del lote uno por uno
            for record in list_ewp:
                # Validación de tiempo antes de procesar cada registro
                elapsed_time = t.time() - self.timer_start
                time_remaining = execution_time_limit - elapsed_time
                if time_remaining <= grace_period:
                    print(f"Quedan {time_remaining:.2f} segundos después de procesar un registro. Deteniendo ejecución.")
                    
                    # Capturar los registros no procesados (desde el registro actual hasta el final de list_ewp)
                    registros_pendientes = list_ewp[list_ewp.index(record):]  # Registros pendientes desde el actual

                    # Manejar los registros pendientes
                    self.handle_pendientes(registros_pendientes)

                    # Detener la ejecución de ambos bucles
                    self.stop_execution = True
                    break  # Salir del bucle for
        
                # Actualizar estado del registro
                self.ewp_service.get_update_estado_sincrona(record["id"])
                
                # Procesar el registro con dryrun_main
                self.dryrun_main(record)

            if self.stop_execution:
                print("Ejecución detenida por límite de tiempo.")
                break  # Salir del bucle while si ya se ha detenido
            
            list_ewp = []
            print("Lote procesado, consultando más registros...")

    def process_stress(self):
        """
        Procesar un solo registro y finalizar la ejecución.
        """
        print("Modo POR UNIDAD activado. Procesando un único registro y finalizando.")
        
        list_ewp = self.ewp_service.get_select_log_sincrona(
        limit=1,  # Solo 1 registro
        flujo_api=self.flujo_api,
        id_logs=self.id_logs
        )

        if not list_ewp:
            print("No se encontró ningún registro para procesar. Finalizando ejecución.")
            return
    
        # Procesar el único registro
        record = list_ewp[0]
        
        # Actualizar estado del registro
        self.ewp_service.get_update_estado_sincrona(record["id"])
        
        # Procesar el registro con dryrun_main
        self.dryrun_main(record)
        
        print(f"Registro con ID {record['id']} procesado. Finalizando ejecución.")
        
    def dryrun_main(self, item):
        try:
            response_service = None
            table_save_data = {}
            start_time_total = t.perf_counter()
            msisdn_token = ""
            contexto_http = item["contexto"]
            date_capture = item["date_capture"]
            mobiquity = {}

            print(repr(f"{item["id"]} START PROCESO \n main/dryrun_main"))
            # 2 Deserialización
            # 2.1 Deserialización del requestEWP, responseEWP
            # 2.2. Extraer información del mapping y plantilla según api

            start_time_request = t.perf_counter()
            ewp_services_item = EWPService(self.ambiente, self.table_proceso)
            (
                request_ewp,
                response_ewp,
                lista_mapping_input_ewp_api,
                lista_mapping_output_ewp_api,
                lista_plantilla_mobiquity_by_api,
                type_token_api,
                contexto_encontrado,
            ) = ewp_services_item.deserializacion_datos(
                item,
                self.lista_mapping,
                self.lista_plantilla_mobiquity,
                self.type_token,
            )

            # 4. Generar request Mobiquity
            request_service = RequestService(
                request_ewp,
                lista_mapping_input_ewp_api,
                lista_plantilla_mobiquity_by_api,
                item["id"],
                contexto_encontrado,
                type_token_api,
                self.lista_ubligeo,
                date_capture,
                self.ambiente,
                self.conexion,
                self.table_proceso,
                contexto_http
            )

            request_mobiquity, table_save_request, msisdn_token, continue_transacc = (
                request_service.get_convert_request_ewp_to_mob()
            )

            table_save_data.update(table_save_request)

            end_time_request = t.perf_counter()
            ejecution_time_request = end_time_request - start_time_request
            if(continue_transacc == 1):

                start_time_peticion_comv = t.perf_counter()

                # 5.Realizar la petición Mobiquity
                lambda_adapter = LambdaAdapter(
                    cfg.ambiente[str(self.ambiente)],
                    request_mobiquity,
                    type_token_api,
                    item["id"],
                    contexto_encontrado,
                    msisdn_token,
                    self.ambiente,
                    self.conexion,
                    self.table_proceso
                )

                mobiquity = lambda_adapter.peticion_mobiquity()
                end_time_peticion_comv = t.perf_counter()
                ejecution_time_ppeticion_comv = end_time_peticion_comv - start_time_peticion_comv

                if(mobiquity["flg_continue"] == 1):

                    star_time_response = t.perf_counter()
                    # 6.Comparación de response EWP vs Mobiquity
                    response_service = ResponseService(
                        mobiquity["response_mob"],
                        response_ewp,
                        lista_mapping_output_ewp_api,
                        item["id"],
                    )

                    #if(item["api_name_ewp"] in ['getaccountholderinfo','getbalance','gettransactionhistory']):
                    #    table_save_response = {}
                    #    error_logs = []
                    #    is_result_equals = 0
                    #    result_compare_details = {}
                    #    print("API DE CONSULTA")
                    #else:
                    (
                        result_compare_details,
                        is_result_equals,
                        error_logs,
                        table_save_response,
                    ) = response_service.get_pre_compare_ewp_mob()
                
        
                    table_save_data.update(table_save_response)
                    end_time_response = t.perf_counter()
                    ejecution_time_response = end_time_response - star_time_response


                    start_time_save_bd = t.perf_counter()
                    # 7.Insertar los valores de Mobiquity en la tabla
                    result_mobiquity = {
                        "id": item["id"],
                        "mobiquity": mobiquity,
                        "is_result_equals": is_result_equals,
                    }
    
                    response_repository = ResponseRepository(
                        result_mobiquity,
                        result_compare_details,
                        error_logs,
                        table_save_data,
                        item["api_name_ewp"],
                        self.ambiente,
                        item["id"],
                        ejecution_time_request,
                        ejecution_time_ppeticion_comv,
                        ejecution_time_response,
                        start_time_save_bd,
                        start_time_total,
                        self.conexion,
                        self.id_execution,
                        self.table_proceso
                    )

                    mobiquity.update({
                        "id_log":item["id"],
                        "ejecution_time_request" :ejecution_time_request,
                        "ejecution_time_ppeticion_comv" :ejecution_time_ppeticion_comv,
                        "ejecution_time_response" :ejecution_time_response,
                        "start_time_save_bd" :start_time_save_bd,
                        "start_time_total" :start_time_total
                    })

                    self.response_mob = mobiquity

                    response_repository.set_update_log()
                elif(mobiquity["flg_continue"] == 0):
                    response_repository = ResponseRepository(
                        {},
                        {},
                        {},
                        (),
                        item["api_name_ewp"],
                        self.ambiente,
                        item["id"],
                        ejecution_time_request,
                        '',
                        '',
                        '',
                        '',
                        self.conexion,
                        self.id_execution,
                        self.table_proceso
                    )

                    response_repository.set_update_log_error()
            elif(continue_transacc == 0):
                response_repository = ResponseRepository(
                        {},
                        {},
                        {},
                        (),
                        item["api_name_ewp"],
                        self.ambiente,
                        item["id"],
                        ejecution_time_request,
                        '',
                        '',
                        '',
                        '',
                        self.conexion,
                        self.id_execution,
                        self.table_proceso
                    )

                response_repository.set_update_log_error()

        except CustomError as e:
            error_data = e.to_dict()
            error_services = ErrorServices(
                error_data["id_log"],
                error_data["error_type"],
                error_data["error_message"],
                error_data["stack_trace"],
                error_data["id_mapping"],
                error_data["clave_ewp"],
                self.ambiente,
                self.table_proceso
            )
            error_services.log_error()

        except Exception as e:
            original_stack_trace = traceback.format_exc()
            line_pos = original_stack_trace.find("line")
            if line_pos != -1:
                stack_trace = original_stack_trace[line_pos:]
            else:
                stack_trace = original_stack_trace

            file_name = Path(__file__).name
            id_log_error = item["id"]
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

    async def get_ewp_queue(self):
        try:
            finished = False
            while not self.error_in_query and not finished:
                list_ewp = await self.ewp_service.get_select_log_asincrona(
                    self.start_date, self.end_date, limit=self.queue_limit, flujo_api = self.flujo_api, id_logs = self.id_logs 
                )
                if not list_ewp:
                    print(repr("No se encontraron más registros Log. Terminando la ejecución. \n main/get_ewp_queue"))
                    await self.queue.put(None)
                    break

                for item in list_ewp:
                    await self.queue.put(item)

                if len(list_ewp) < self.queue_limit:
                    finished = True
                    await self.queue.put(None)

                # await self.queue.put(None)

        except Exception as e:
            print(repr(f"Error DR: al consultar registros: {e}"))
            print("Error DR: Deteniendo la consulta de nuevos registros.")
            self.error_in_query = True  # Señalar que ha ocurrido un error
            await self.queue.put(None)  # Señal de que ya no habrá más elementos

    async def process_list_queue(self):

        while True:
            elapsed_time = t.time() - self.timer_start
            remaining_time = 15 * 60 - elapsed_time  # Tiempo restante en segundos
            print(repr(f"Tiempo transcurrido: {elapsed_time / 60:.2f} minutos"))
            print(repr(f"Tiempo restante: {remaining_time / 60:.2f} minutos"))
            #if remaining_time <= 180:  # Quedan 3 minutos o menos
            print("Quedan 3 minutos o menos, procesando elementos restantes.")
                #await self.process_remaining_items()
                #break

            item = await self.queue.get()
            if item is None:
                break

            # Ejecución en paralelo - ocurencias
            loop = asyncio.get_event_loop()
            await self.ewp_service.get_update_estado(
                    item["id"]
                )
            loop.run_in_executor(self.executor, self.dryrun_main, item)
            self.queue.task_done()


    async def process_remaining_items(self):
        """Procesa los elementos restantes de la cola antes de que se acabe el tiempo."""
        remaining_ids = []
        while not self.queue.empty():
            item = await self.queue.get()
            if item:
                remaining_ids.append(item["id"])
            self.queue.task_done()

        # Procesa los IDs restantes
        if remaining_ids:
            print(repr(f"Procesando IDs restantes: {remaining_ids}"))
            # Aquí puedes implementar la lógica para procesar los IDs restantes
            #await self.ewp_service.process_ids(remaining_ids)

    def handle_pendientes(self, registros_pendientes):
        """
        Método para manejar registros pendientes.
        """
        print(f"Procesando {len(registros_pendientes)} registros pendientes...")
        # Implementa la lógica para manejar los registros pendientes
        # Por ejemplo, guardarlos en un log, actualizar estados, etc.
        print(f"Registros pendientes: {str(registros_pendientes)}")


        ids_tuple = tuple(int(record["id"]) for record in registros_pendientes if "id" in record and record["id"] is not None)

        response_repository = ResponseRepositoryReset(
                    ids_tuple,
                    self.ambiente,
                    self.id_execution,
                    self.conexion,
                    self.table_proceso
                )

        response_repository.set_reset_status_log()

if __name__ == "__main__":

    if len(sys.argv) > 1:
        try:
            # Captura y decodifica el JSON desde el argumento
            json_string = sys.argv[1]
            # Elimina las comillas dobles al principio y al final del string
            #json_event = json_string.replace("'","")
            json_string = json_string.replace("'", '"')
            event_data = json.loads(json_string)
        except json.JSONDecodeError:
            print("Error DR: El argumento proporcionado no es un JSON válido.")
            sys.exit(1)
    else:
        print("Error DR: Por favor, proporciona un JSON como argumento.")
        sys.exit(1)

    dry_run_main = DryRunMain(event_data=event_data)
    asyncio.run(dry_run_main.pre_dryrun_main())
