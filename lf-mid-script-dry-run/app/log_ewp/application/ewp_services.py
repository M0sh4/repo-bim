"""s
"""
from app.log_ewp.domain.ewp_domain import EWPDomain
from app.log_ewp.ports.ewp_ports import EWPPort
from app.log_ewp.infraestructure.repositories.ewp_repository import EWPRepository

class EWPService(EWPPort):

    def __init__(self, ambiente, table_proceso):
        self.ambiente = ambiente
        self.table_proceso = table_proceso
        self.auth_domain = EWPDomain()
        self.auth_repository = EWPRepository(self.ambiente, self.table_proceso)
        
        
        
    async def get_update_estado(self, id_log):
        list_ewp = await self.auth_repository.get_update_estado(id_log, self.ambiente)
        return list_ewp

    async def get_select_log_asincrona(self, start_date, end_date, limit, flujo_api, id_logs):
        list_ewp = await self.auth_repository.select_log_ewp(start_date, end_date, limit, self.ambiente, flujo_api, id_logs)
        return list_ewp
    
    def deserializacion_datos(self, item, lista_mapping, lista_plantilla_mobiquity, type_token):
        auth_domain_val = EWPDomain()
        request_ewp , response_ewp, api_name, contexto_encontrado = auth_domain_val.deserializacion_datos_ewp(item)
        type_token_api, id_json= auth_domain_val.deserializacion_token_api(item["id"],type_token[api_name],api_name,contexto_encontrado)

        
        lista_mapping_input_ewp_api, lista_mapping_output_ewp_api = auth_domain_val.deserializacion_mapping(item["id"], lista_mapping, request_ewp["api_name"], id_json)
        lista_plantilla_mobiquity_by_api = auth_domain_val.deserializacion_plantilla(item["id"],lista_plantilla_mobiquity[str(id_json)][str(api_name)])
        return request_ewp, response_ewp, lista_mapping_input_ewp_api ,lista_mapping_output_ewp_api, lista_plantilla_mobiquity_by_api , type_token_api, contexto_encontrado

    def get_select_log_sincrona(self, limit, flujo_api, id_logs):
        list_ewp = self.auth_repository.select_log_ewp_sincrona(limit, self.ambiente, flujo_api, id_logs)
        return list_ewp

    def get_update_estado_sincrona(self, id_log):
        list_ewp = self.auth_repository.get_update_estado_sincrona(id_log, self.ambiente)
        return list_ewp
    
    def get_select_users_sincrona(self, table_proceso, id_logs, flujo_api, queue_limit_sincrona):
        list_users = self.auth_repository.select_users_ewp_sincrona(table_proceso, id_logs, self.ambiente, flujo_api, queue_limit_sincrona)
        return list_users

    def get_update_estado_user_sincrona(self, id_user,table_proceso):
        list_ewp = self.auth_repository.get_update_estado_user_sincrona(id_user, table_proceso, self.ambiente)
        return list_ewp