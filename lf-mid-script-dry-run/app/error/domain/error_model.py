''' Model de Excepcion personalizado'''
from datetime import datetime
import pytz
tz = pytz.timezone("America/Lima")

class CustomError(Exception):
    ''' Class de model excepcion'''
    def __init__(self, id_log, error_type,
                 message, stack_trace, id_mapping = None, clave_ewp = None):
        super().__init__(message)
        self.id_log = id_log
        self.timestamp_error = (datetime.now(tz)).strftime('%Y-%m-%d %H:%M:%S')
        self.error_type = error_type
        self.error_message = message
        self.stack_trace = stack_trace
        self.id_mapping = id_mapping
        self.clave_ewp = clave_ewp

    def to_dict(self):
        '''Diccionario del error personalizado'''
        return {
            "id_log": self.id_log,
            "timestamp_error": self.stack_trace,
            "error_type": self.error_type,
            "error_message": self.error_message,
            "stack_trace": self.stack_trace,
            "id_mapping": self.id_mapping,
            "clave_ewp": self.clave_ewp,
        }
