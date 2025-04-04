"""s
"""
import sys
import pymysql
from app.mapping_config.domain.mapping_domain import MappingDomain
from app.mapping_config.ports.mapping_ports import MappingPort
from app.mapping_config.infraestructure.repositories.mapping_repository import MappingRepository

class MappingService(MappingPort):

    def __init__(self,ambiente):
        self.ambiente = ambiente
        self.mapping_domain = MappingDomain()
        self.mapping_repository = MappingRepository(self.ambiente)
        

    def get_mapping_ewp_comviva(self, start_date, end_date, format_fecha):
        """Función consultar mapping"""
        try:
            print(repr(f"Iniciando: fecha inicio: {start_date} \n fecha fin: {end_date} \n mapping_services/get_mapping_ewp_comviva"))
            if not self.mapping_domain.val_fecha_inicio_fin(start_date, end_date, format_fecha):
                raise ValueError("Error DR: Fechas inválidas mapping_services/get_mapping_ewp_comviva")
            
            resp_mysql = self.mapping_repository.select_mapping(start_date, end_date)
            
            message_val, pre_id_execution = self.mapping_domain.val_dict_mapping(resp_mysql)
            
            #if pre_id_execution["idexecution"] == 0:
            #    self.mapping_repository.insert_idexecution(start_date, end_date)
            #    resp_mysql = self.mapping_repository.select_mapping(start_date, end_date)
            #    message_val, pre_id_execution = self.mapping_domain.val_dict_mapping(resp_mysql)

            if message_val != "OK":
                raise ValueError(message_val)
            
            return (
                pre_id_execution["api_name"],
                pre_id_execution["type_token"]
            )
        except ValueError as e:
            print(repr(f"Error DR: Ocurrió un error select mapping: {e} \n mapping_services/get_mapping_ewp_comviva"))
            sys.exit(1)
        except pymysql.OperationalError as e:
            print(repr(f"Error DR: Conexión BD select mapping: {e} \n mapping_services/get_mapping_ewp_comviva"))
            sys.exit(1)
        except pymysql.InternalError as e:
            print(repr(f"Error DR: Internal MySQL error select mapping: {e} \n mapping_services/get_mapping_ewp_comviva"))
            sys.exit(1)
        except pymysql.MySQLError as e:
            print(repr(f"Error DR: General MySQL error select mapping: {e} \n mapping_services/get_mapping_ewp_comviva"))
            sys.exit(1)
        except Exception as e:
            print(repr(f"Error DR: General error select mapping: {e} \n mapping_services/get_mapping_ewp_comviva"))
            sys.exit(1)