"""PLANTILLA SERVICES
"""
import sys
from typing import Optional

import pandas as pds
from sqlalchemy.exc import (DataError, IntegrityError, InvalidRequestError,
                            OperationalError, StatementError)
from unidecode import unidecode

import app.shared.config as cfg
from app.plantilla_request_mob.domain.plantilla_domain import PlantillaDomain
from app.plantilla_request_mob.infraestructure.repositories.plantilla_repository import \
    PlantillaRepository
from app.plantilla_request_mob.ports.plantilla_ports import PlantillaPort

class PlantillaService(PlantillaPort):
    ''' Class de plantilla de los request de api Mobiquity'''
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.mapping_domain = PlantillaDomain()
        self.mapping_repository = PlantillaRepository()
        

    def get_plantilla_json_mobiquity(self) -> Optional[dict]:
        try:
            resp_sqlalchemy = self.mapping_repository.select_plantilla_mobiquity()
            plantillas = self.mapping_domain.build_json_structure(resp_sqlalchemy)

            return plantillas

        except OperationalError as e:
            print(repr(f"Error DR: de conexión a la base de datos SQLAlchemy: {e} \n plantilla_services/get_plantilla_json_mobiquity"))
            sys.exit(1)
        except IntegrityError as e:
            print(repr(f"Error DR: de integridad en la base de datos SQLAlchemy: {e} \n plantilla_services/get_plantilla_json_mobiquity"))
            sys.exit(1)
        except DataError as e:
            print(repr(f"Error DR: de datos inválidos SQLAlchemy: {e} \n plantilla_services/get_plantilla_json_mobiquity"))
            sys.exit(1)
        except StatementError as e:
            print(repr(f"Error DR: en la ejecución de la sentencia SQL SQLAlchemy: {e} \n plantilla_services/get_plantilla_json_mobiquity"))
            sys.exit(1)
        except InvalidRequestError as e:
            print(repr(f"Error DR: Se intentó una operación inválida SQLAlchemy: {e} \n plantilla_services/get_plantilla_json_mobiquity"))
            sys.exit(1)
        except ValueError as ve:
            print(repr(f"Error DR: de valor json_structure: {ve} \n plantilla_services/get_plantilla_json_mobiquity"))
        except IndexError as ie:
            print(repr(f"Error DR: de índice json_structure: {ie} \n plantilla_services/get_plantilla_json_mobiquity"))
        except KeyError as ke:
            print(repr(f"Error DR: de clave json_structure: {ke} \n plantilla_services/get_plantilla_json_mobiquity"))
        except TypeError as te:
            print(repr(f"Error DR: de tipo json_structure: {te} \n plantilla_services/get_plantilla_json_mobiquity"))
        except AttributeError as ae:
            print(repr(f"Error DR: de atributo: {ae} \n plantilla_services/get_plantilla_json_mobiquity"))
        except Exception as e:
            print(repr(f"Error DR: general no esperado Plantilla_json_api: {e} \n plantilla_services/get_plantilla_json_mobiquity"))
            sys.exit(1)

    def get_tabla_ubligeo(self):
        df = pds.read_csv(cfg.ruta_csv_ubligeo, sep=';')
        df['state'] = df['state'].str.replace(r"^\d+\s", "", regex=True)
        df['city'] = df['city'].str.replace(r'^\d+\s', '', regex=True)
        df['distrito'] = df['distrito'].str.replace(r'^\d+\s', '', regex=True)

        for column in ['state','city', 'distrito']:
            df[column] = df[column].fillna('')  # Rellenar NaN con cadenas vacías
            df[column] = df[column].astype(str).str.strip().str.normalize('NFKD').str.casefold().apply(unidecode)
        return df
