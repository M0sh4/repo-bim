from datetime import datetime

from app.infraestructure.adapters.db_adapter import DBAdapter
import app.shared.config as cfg
import pytz
tz = pytz.timezone("America/Lima")
class ErrorServices():
    def __init__(self, id_log, tipo_error : str, message : str, stack_trace : str, id_mapping, clave_ewp, ambiente, table_proceso):
        self.id_log = id_log
        self.tipo_error = tipo_error
        self.message = message
        self.stack_trace = stack_trace
        self.id_mapping = id_mapping
        self.clave_ewp = clave_ewp
        self.database_adapter = DBAdapter("", ambiente)
        self.table_error = cfg.ambiente[str(ambiente)]["table_Error"]
        #self.table_log = cfg.ambiente[str(ambiente)]["table_log"]
        self.table_log = table_proceso

    def log_error(self):
        """Captura y registra los detalles del error."""
        error_details = {
            "id_log": self.id_log,  # El ID del item procesado
            "timestamp_error": (datetime.now(tz)).strftime('%Y-%m-%d %H:%M:%S'),  # Hora UTC del error
            "error_type": str(self.tipo_error),  # Tipo de error
            "error_message": str(self.message),  # Mensaje de error
            "stack_trace": str(self.stack_trace),  # Stack trace completo
            "id_mapping": self.id_mapping,  # En caso de que falle durante la comparación
            "clave_ewp": self.clave_ewp,  # Si el error ocurre al comparar claves
                        #"file_name": error.__traceback__.tb_frame.f_code.co_filename, 
            #"line_number": error.__traceback__.tb_lineno,  
            #"function_name": error.__traceback__.tb_frame.f_code.co_name,  
        }

        print(repr(f"{self.id_log} \n Error DR: {str(error_details)} \n error_services/log_error"))
        # Guardar el error en la base de datos
        self.save_error_to_db(error_details)

    def save_error_to_db(self, error_details):
        start_datetime = error_details["timestamp_error"]

        """Función para guardar los detalles del error en la base de datos."""
        # Aquí se implementa la lógica para enviar los errores a la BD
        query1 = cfg.query_insert_error_log.format(tabledata=self.table_error)
        param1 = (
            error_details["id_log"],
            error_details["timestamp_error"],
            error_details["error_type"],
            error_details["error_message"],
            error_details["stack_trace"],
            error_details["id_mapping"],
            error_details["clave_ewp"]
        )

        self.database_adapter.insert_query(query1,param1)

        # query2 = cfg.query_update_log_comviva_error.format(tabledata=self.table_log)
        # param2 = (
        #     '1',
        #     str(start_datetime),
        #     self.id_execution,
        #     'ERROR',
        #     error_details["id_log"]
        # )

        # self.database_adapter.insert_query(query2,param2)
