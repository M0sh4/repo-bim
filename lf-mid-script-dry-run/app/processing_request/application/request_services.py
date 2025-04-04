"""Request services
"""

import copy
import time
from app.processing_request.domain.request_domain import RequestDomain


class RequestService:
    """Class de Proceso de convert Request EWP a Mobiquity"""

    def __init__(
        self,
        request_ewp,
        lista_mapping,
        plantilla_mobiquity,
        id_item,
        contexto_encontrado,
        type_token_api,
        lista_ubligeo,
        date_capture,
        ambiente,
        conexion,
        table_proceso,
        contexto_http
    ):
        self.ambiente = ambiente
        self.conexion = conexion
        self.table_proceso =  table_proceso
        self.request_domain = RequestDomain(lista_ubligeo, self.ambiente, self.conexion, self.table_proceso)
        self.request_ewp = copy.deepcopy(request_ewp)
        self.lista_mapping = (lista_mapping.copy()).sort_values(by='id_mapping', ascending=True)
        self.plantilla_mobiquity = copy.deepcopy(plantilla_mobiquity)
        self.id_item = id_item
        self.agente = contexto_encontrado
        self.type_token_api = type_token_api
        self.date_capture = date_capture
        self.contexto_http = contexto_http
        
    def get_convert_request_ewp_to_mob(self) -> dict:
        """convertir request EWP a request Mobiquity"""
        message_ewp_json, auth_bytes = self.request_domain.get_request_ewp_in_json(
            self.request_ewp, self.id_item, self.agente
        )
        
        pre_request_mobiquity, table_save_data, msisdn_token, continue_transacc = (
            self.request_domain.get_mapping_replace_values(
                message_ewp_json,
                self.lista_mapping,
                self.plantilla_mobiquity,
                self.id_item,
                auth_bytes,
                self.type_token_api,
                self.request_ewp["api_name"],
                self.date_capture,self.contexto_http,self.agente
            )
        )

        return pre_request_mobiquity, table_save_data, msisdn_token, continue_transacc
