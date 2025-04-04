import sys

import pymysql

import app.shared.config as cfg
from app.infraestructure.adapters.db_adapter import \
    DBAdapter  
from app.shared.utils import Utils

class MappingRepository:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.database_adapter = DBAdapter("", self.ambiente)
        self.utils = Utils()

    def select_mapping(self, start_date: str, end_date: str):
        """Consulta los datos de mapeo entre las fechas dadas."""
        try:
           
            query = cfg.query_select_mapping_plantilla
            if(not self.utils.val_variable(query)):
                raise ValueError("Error DR: No existe query SQL de consulta id de la ejecución. \n mapping_repository/select_mapping")
            
            print(repr("Consultando mapeo de campos EWP vs Comviva. \n mapping_repository/select_mapping"))
            #params = (start_date, end_date)
            result = self.database_adapter.select_query(query, None )

            print(repr(f"Consulta exitosa mapeo de campos EWP vs Comviva. \n mapping_repository/select_mapping {result}"))
            return result
        except ValueError as e:
            print(repr(f"Error DR: Ocurrió un error select mapping: {e} \n mapping_repository/select_mapping"))

    def insert_idexecution(self, start_date, end_date):
        '''Inserta id de la ejecución del script'''
        try:
            query = '' #cfg.query_insert_idexecution
            if(not self.utils.val_variable(query)):
                raise ValueError("Error DR: No existe query SQL de consulta id de la ejecución. \n mapping_repository/insert_idexecution")

            param = (start_date)
            re_mysql = self.database_adapter.insert_query(query, param)

            if not re_mysql or re_mysql is None or re_mysql == 0:
                raise ValueError("Error DR: en la base de datos al insertar id de la ejecución.")

        except PermissionError as pe:
            print(repr(f"Error DR: Error de permiso insert idexecution: {pe}"))
            sys.exit(1)
        except ValueError as e:
            print(repr(f"Error DR: Ocurrió un error insert idexecution: {e}"))
            sys.exit(1)
        except pymysql.OperationalError as e:
            print(repr(f"Error DR: Conexión BD insert idexecution: {e}"))
            sys.exit(1)
        except pymysql.InternalError as e:
            print(repr(f"Error DR: Internal MySQL error insert idexecution: {e}"))
            sys.exit(1)
        except pymysql.MySQLError as e:
            print(repr(f"Error DR: General MySQL error insert idexecution: {e}"))
            sys.exit(1)
        except Exception as e:
            print(repr(f"Error DR: General error insert idexecution: {e}"))
            sys.exit(1)
