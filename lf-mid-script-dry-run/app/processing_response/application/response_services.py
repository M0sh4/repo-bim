"""s
"""
from app.processing_response.domain.response_domain import ResponseDomain

class ResponseService():

    def __init__(self,response_mobiquity, response_ewp, lista_mapping, id_log):
        
        self.table_save_data = {}
        self.response_domain = ResponseDomain()
        self.response_mobiquity = response_mobiquity
        self.response_body_mobiquity = response_mobiquity["body"]
        self.response_message_ewp, self.statuscode = self.response_domain.get_response_ewp_in_json(response_ewp,id_log)
        self.lista_mapping = lista_mapping.copy()
        self.message_error = ""
        self.compare_details = []
        self.no_compare_details = []
        self.id_log = id_log
        

    def get_pre_compare_ewp_mob(self):
        """Servicio de realizar la comparación de response EWP y Mobiquity"""
        compare_details, is_result_equals, error_logs, self.table_save_data = self.response_domain.get_compare_ewp_mob(self)

        return  compare_details, is_result_equals, error_logs, self.table_save_data