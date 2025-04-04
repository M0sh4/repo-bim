import app.shared.config as cfg
from app.infraestructure.adapters.db_adapter import (  # Asumiendo que tienes un adaptador para MySQL
    DBAdapter, DBAsyncAdapter)
import uuid
last_id_log : int = 0

class EWPRepository:
    def __init__(self ,ambiente, table_proceso):
        self.ambiente = ambiente
        self.database_adapter = DBAsyncAdapter()
        self.database_adapter_sincrona = DBAdapter("",self.ambiente)
        self.tabla_usuario = cfg.ambiente[str(ambiente)]["table_Values_Match"]
        #self.tabla_log = cfg.ambiente[str(ambiente)]["table_log"]
        self.tabla_log = table_proceso

    async def select_log_ewp(self, start_date, end_date, limit, ambiente, flujo_api, id_logs):
        global last_id_log

        #tabla_log = cfg.ambiente[str(ambiente)]["table_log"] 
        tabla_log = self.tabla_log
        print(repr(f"Consultando tabla: {tabla_log} \n ewp_repository/select_log_ewp"))
        #query = cfg.query_flujos[str(flujo_api)].format(tabledata=tabla_log)

        if(id_logs != ""):
            filtro_id_logs = f'AND id IN ({id_logs})'
        else:
            filtro_id_logs = ''

        query = cfg.query_flujos[str(flujo_api)].format(tabledata=tabla_log, filtro_idlog=filtro_id_logs)

        query2 = cfg.query_update_estado_log.format(tabledata=tabla_log)
        param = (start_date, end_date, limit ) #,  last_id_log

        print(repr("Consultando log ewp para procesar. \n ewp_repository/select_log_ew"))
        re_mysql = await self.database_adapter.select_query_asincrona(query, param)
        print(repr(f"Consulta existosa log ewp para procesar. \n {re_mysql} \n ewp_repository/select_log_ew"))

        collected_ids =tuple(record["id"] for record in re_mysql)

        param2 = ( "COLA", collected_ids)

        print(repr(f"Actualizando estado log Cola \n {query2} \n {collected_ids} \n ewp_repository/select_log_ew"))
        re_mysql2 = await self.database_adapter.update_query_asincrona(query2, param2)

        if re_mysql is None:
            print(repr("No se recibieron resultados de Log. \n ewp_repository/select_log_ew"))
            return []

        if not re_mysql:
            return []

        
        last_id_log = re_mysql[-1]["id"]

        return re_mysql

    def select_log_ewp_sincrona(self, limit, ambiente, flujo_api, id_logs):

        tabla_log = self.tabla_log

        #if(id_logs != ""):
        #    filtro_id_logs = f'AND id IN ({id_logs})'
        #else:
        #    filtro_id_logs = ' '

        uuid4_text = str(uuid.uuid4())
        #query = cfg.query_flujos[str(flujo_api)].format(tabledata=tabla_log, filtro_idlog=filtro_id_logs, limite = limit, uuid_text = uuid4_text)
        print(f"{tabla_log},{flujo_api},{uuid4_text},{id_logs},{limit}")
        print(repr("Consultando log ewp para procesar. \n ewp_repository/select_log_ew"))
        re_mysql = self.database_adapter_sincrona.select_query_transaccion(tabla_log,flujo_api,uuid4_text,id_logs,limit)
        print(repr(f"Consulta existosa log ewp para procesar. \n {re_mysql} \n ewp_repository/select_log_ew"))

        if re_mysql is None:
            print("No se recibieron resultados.")
            return []

        if not re_mysql:
            return []

        if re_mysql is None:
            print(repr("No se recibieron resultados de Log. \n ewp_repository/select_log_ew"))
            return []

        return re_mysql


    def select_users_ewp_sincrona(self, table_proceso, id_logs, ambiente,flujo_api, queue_limit_sincrona):
        global last_id_log


        if(id_logs != ""):
            filtro_id_logs = f'AND id IN ({id_logs})'
        else:
            filtro_id_logs = ' '

        query = cfg.query_flujos[str(flujo_api)].format(tabledata=table_proceso, filtro_idlog=filtro_id_logs)
        query2 = cfg.query_update_estado_users.format(tabledata=table_proceso)

        param = (queue_limit_sincrona) #, limit last_id_log

        print(repr("Consultando log ewp para procesar. \n ewp_repository/select_users_ewp_sincrona"))
        re_mysql = self.database_adapter_sincrona.select_query(query, param)
        print(repr(f"Consulta existosa log ewp para procesar. \n {re_mysql} \n ewp_repository/select_users_ewp_sincrona"))

        if re_mysql is None:
            print("No se recibieron resultados.")
            return []

        if not re_mysql:
            return []

        collected_ids =tuple(record["id"] for record in re_mysql)
        param2 = ("COLA", collected_ids)
        print(repr(f"Actualizando estado log Cola \n {query2} \n {collected_ids} \n ewp_repository/select_users_ewp_sincrona"))


        re_mysql2 = self.database_adapter_sincrona.insert_query(query2, param2)
        
        
        if re_mysql is None:
            print(repr("No se recibieron resultados de Log. \n ewp_repository/select_users_ewp_sincrona"))
            return []
        
        last_id_log = re_mysql[-1]["id"]

        return re_mysql
    
    async def get_update_estado(self, id_log, ambiente):
        query2 = cfg.query_update_estado_log_unit.format(tabledata=self.tabla_log)
        collected_ids =(id_log,)

        param2 = ("ENPROCESO", collected_ids[0])

        print(repr(f"Actualizando estado log EnProceso. {query2} \n {param2} \n ewp_repository/get_update_estado"))
        re_mysql = await self.database_adapter.update_query_asincrona(query2, param2)


        if re_mysql is None or not re_mysql:
            print(repr("No se recibieron resultados. \n ewp_repository/get_update_estado"))
            return []

        return re_mysql

    def get_update_estado_sincrona(self, id_log, ambiente):
        query2 = cfg.query_update_estado_log_unit.format(tabledata=self.tabla_log)

        collected_ids =(id_log,)

        param2 = ("ENPROCESO", collected_ids[0])

        print(repr(f"{id_log} \n Actualizando estado log EnProceso. {query2} \n {param2} \n ewp_repository/get_update_estado_sincrona"))
        re_mysql = self.database_adapter_sincrona.insert_query(query2, param2)

        if re_mysql is None:
            print(repr(f"Error DR: {id_log} \n No se recibieron resultados. \n ewp_repository/get_update_estado_sincrona"))
            return []

        if not re_mysql:
            return []

        return re_mysql
#(435911, 435916, 435921, 435925, 435926)
#(436002, 436005, 436037, 436053, 436054)
#(436056, 436068, 436076, 436115, 436129)
    def get_update_estado_user_sincrona(self, id_user, table_proceso, ambiente):

        query2 = cfg.query_update_estado_users_unit.format(tabledata=table_proceso)

        collected_ids =(id_user,)

        param2 = ("ENPROCESO", collected_ids[0])

        print(repr(f"{id_user} \n Actualizando estado log EnProceso. {query2} \n {param2} \n ewp_repository/get_update_estado_user_sincrona"))
        re_mysql = self.database_adapter_sincrona.insert_query(query2, param2)

        if re_mysql is None:
            print(repr(f"Error DR: {id_user} \n No se recibieron resultados. \n ewp_repository/get_update_estado_user_sincrona"))
            return []

        if not re_mysql:
            return []

        return re_mysql