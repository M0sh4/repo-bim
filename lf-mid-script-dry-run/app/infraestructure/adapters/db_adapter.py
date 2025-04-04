import sys
import time as t
from aws_xray_sdk.core import xray_recorder
import pymysql as pysql
from sqlalchemy import create_engine
from sqlalchemy.exc import (DataError, IntegrityError, InvalidRequestError,
                            OperationalError, SQLAlchemyError, StatementError)
from sqlalchemy.orm import joinedload, sessionmaker

from app.plantilla_request_mob.domain.plantilla_model import JsonNode

sys.path.insert(1,'libs')
import asyncio
import time

import aiomysql

import app.shared.config as cfg

class DBAdapter:
    """Database connection class."""

    def __init__(self, type_db, ambiente):
        self.ambiente = ambiente
        self.segment = xray_recorder.current_segment()
        self.table_user = cfg.ambiente[str(self.ambiente)]["table_Values_Match"]
        self.stored_log = cfg.ambiente[str(self.ambiente)]["stored_select_logs"] 
        if(type_db == "mdw"):
            self.db_host = cfg.ambiente[str(self.ambiente)]["DBNC"]["db_host"]
            self.db_username = cfg.ambiente[str(self.ambiente)]["DBNC"]["db_username"]
            self.db_password = cfg.ambiente[str(self.ambiente)]["DBNC"]["db_password"]
            self.db_port = cfg.ambiente[str(self.ambiente)]["DBNC"]["db_port"]
            self.db_name = cfg.ambiente[str(self.ambiente)]["DBNC"]["db_name"]
            self.conn = None
            self.pool = None
        else:
            self.db_host = cfg.DATABASEDR["db_host"]
            self.db_username = cfg.DATABASEDR["db_username"]
            self.db_password = cfg.DATABASEDR["db_password"]
            self.db_port = cfg.DATABASEDR["db_port"]
            self.db_name = cfg.DATABASEDR["db_name"]
            self.conn = None
            self.pool = None
        
    def open_connection(self):
        """Connect to MySQL Database."""
        connection_successful = False
        try:
            if self.conn is None or not self.conn.open:
                self.conn = pysql.connect(host=self.db_host, 
                                          db=self.db_name, 
                                          port=self.db_port, 
                                          user=self.db_username,
                                          password=self.db_password, 
                                          charset='utf8mb4', 
                                          cursorclass=pysql.cursors.DictCursor,
                                          connect_timeout=20)
                connection_successful = True
        except pysql.MySQLError as e:
            print(repr(f"Error DR: Conexión BD open_connection: {e}"))
            raise
        finally:
            if connection_successful:
                print('Connection opened successfully.')
            else:
                print('Error DR: Failed to open connection.')
        
    def close_connection(self):
        """Close the MySQL connection."""
        if self.conn:
            try:
                self.conn.close()
                print("Database connection closed.")
            except pysql.MySQLError as e:
                print(f"Error closing connection: {e}")
            finally:
                self.conn = None
            
    def select_query(self, query, param):
        """Execute SQL query."""
        try:
            
            self.open_connection()
            
            with self.conn.cursor() as cur:
                records = []
                cur.execute(query,param)
                for row in cur:
                    records.append(row)
                return records

        except pysql.OperationalError:
            raise
        except pysql.InternalError:
            raise
        except pysql.MySQLError:
            raise
        except Exception as e:
            print(repr(f'Error DR: General: db_adapter/select_query. {e}'))
            raise
        finally:
            self.close_connection()
            print('Database connection closed select_query db_adapter/select_query.')
    def select_query_transaccion(self, tabla_log,flujo_api,uuid4_text,id_logs,limit):
        """Execute SQL query."""
        try:
            subsegment = xray_recorder.begin_subsegment("consulta-log")
            self.open_connection()
            with self.conn.cursor() as cur:
                records = []
                cur.callproc(self.stored_log,[tabla_log,flujo_api,uuid4_text,id_logs,limit])
                for result_set in cur.fetchall():
                    records.append(result_set)
                cur.close()
                xray_recorder.end_subsegment()
                return records

        except pysql.OperationalError:
            raise
        except pysql.InternalError:
            raise
        except pysql.MySQLError:
            raise
        except Exception as e:
            print(repr(f'Error DR: General: db_adapter/select_query_transaccion. {e}'))
            raise
        finally:
            self.close_connection()
            print('Database connection closed select_query db_adapter/select_query_transaccion.')
    def insert_query(self, query, param):
        """Execute SQL query."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                result = cur.execute(query,param)
                self.conn.commit()
                affected = cur.rowcount
                return affected

        except pysql.OperationalError:
            raise
        except pysql.InternalError:
            raise
        except pysql.MySQLError:
            raise
        except Exception as e:
            print(repr(f'Error DR: General: {e}'))
            raise
        finally:
            self.close_connection()
            print('Database connection closed insert query.')

    def insert_query_transaccion(self, query, param):
        """Execute SQL query."""
        try:
            with self.conn.cursor() as cur:
                result = cur.execute(query,param)
                self.conn.commit()
                cur.execute("UNLOCK TABLES;")
                affected = cur.rowcount
                return affected

        except pysql.OperationalError:
            raise
        except pysql.InternalError:
            raise
        except pysql.MySQLError:
            raise
        except Exception as e:
            print(repr(f'Error DR: General: {e}'))
            raise
        finally:
            self.close_connection()
            print('Database connection closed insert query.')

    def insert_query_results(self, query1, param1, query2, param2, id_log,api_name_ewp):
        """Execute SQL query."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:

                print(repr(f"{id_log} \n Guardar datos Comviva en Log {id_log} \n {query1} {param1} \n db_adapter/insert_query_results"))
                result1 = cur.execute(query1,param1)
                print(repr(f"{id_log} \n Se Guardó datos Comviva en Log {id_log} \n {result1} \n db_adapter/insert_query_results"))

                if(api_name_ewp not in ['getaccountholderinfo','getbalance','gettransactionhistory']):
                    print(repr(f"{id_log} \n Guardar detalle de comparacion Ewp vs Comviva \n {query2} {param2} \n db_adapter/insert_query_results"))
                    result2 = cur.executemany(query2, param2)
                    print(repr(f"{id_log} \n Se Guardó detalle de comparacion Ewp vs Comviva \n {result2} \n db_adapter/insert_query_results"))
                self.conn.commit()
                affected = cur.rowcount
                return affected

        except pysql.MySQLError as e:
            print(repr(f'Error DR: {id_log} \n insert_query: {e} \n db_adapter/insert_query_results'))
        finally:
            self.close_connection()
            print(repr(f'{id_log} \n Database connection closed insert_query.  \n db_adapter/insert_query_results'))
                
    def insert_query_time(self, query, param,time_start_total):
        """Execute SQL query."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                end_time_total = t.perf_counter()
                time_total = end_time_total - time_start_total
                param = (time_total,) + param 
                result = cur.execute(query,param)
                self.conn.commit()
                affected = cur.rowcount
                return affected

        except pysql.MySQLError as e:
            print(repr(f'ERROR insert_query: {e}'))
        finally:
            self.close_connection()
            print('Database connection closed insert_query.')
    
    def insert_query_errors(self, query_error_insert, param_errors):
        """Execute SQL query to insert errors."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                cur.executemany(query_error_insert, param_errors)
                self.conn.commit()
                affected = cur.rowcount
                return affected

        except pysql.MySQLError as e:
            print(repr(f'ERROR insert_query_errors: {e}'))
        finally:
            self.close_connection()
            print('Database connection closed insert_query_errors.')

    def insert_query_data_user(self, query_duplicate, id_log):
        """Execute SQL query."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                # Intentar la actualización
                print(repr(f"{id_log} \n Guardar datos en DR \n {query_duplicate} \n db_adapter/insert_query_data_user"))
                cur.execute(query_duplicate, None)
                affected_rows = cur.rowcount
                self.conn.commit()
                print(repr(f"{id_log} \n Guardado datos en DR \n db_adapter/insert_query_data_user"))
                total_affected = cur.rowcount  # Esto reflejará las filas del último comando ejecutado
                return total_affected

        except pysql.MySQLError as e:
            raise pysql.MySQLError(repr(f"Error DR: {id_log} \n insert_query: {e}"))
        finally:
            self.close_connection()
            print(repr(f"{id_log} \n Database connection closed insert_query."))

    def update_accountoinfo_query(self, query_buscar, query_update, quey_inserts, mdn, id_item):
        """Execute SQL query to insert errors."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                print(repr(f"{id_item} \n Consultar msisdn registrado en DR \n {query_buscar} \n db_adapter/update_accountoinfo_query"))
                
                records = []
                records2 = []
                valor_record = 0
                cur.execute(query_buscar,None)
                for row in cur:
                    records.append(row)

                print(repr(f"{id_item} \n Respuesta msisdn registrado en DR \n {records[0]["conteo"]} \n db_adapter/update_accountoinfo_query"))

                if records[0]["conteo"] == 1:
                    print(repr(f"{id_item} \n Actualizar datos del msisdn registrado en DR \n {query_update} \n db_adapter/update_accountoinfo_query"))
                    cur.execute(query_update, None)
                    print(repr(f"{id_item} \n Actualizado datos del msisdn registrado en DR \n db_adapter/update_accountoinfo_query"))
                    valor_record = 1
                else:
                    print(repr(f"{id_item} \n Registrar datos del msisdn registrado en DR \n {quey_inserts} \n db_adapter/update_accountoinfo_query"))
                    cur.execute(quey_inserts, None)
                    print(repr(f"{id_item} \n Registrado datos del msisdn registrado en DR \n db_adapter/update_accountoinfo_query"))


                    print(repr(f"{id_item} \n Consultar msisdn registrado en DR \n {query_buscar} \n db_adapter/update_accountoinfo_query"))
                    cur.execute(query_buscar,None)
                    for row in cur:
                        records2.append(row)
                    print(repr(f"{id_item} \n Respuesta msisdn registrado en DR \n {records2[0]["conteo"]} \n db_adapter/update_accountoinfo_query"))
                    valor_record = records2[0]["conteo"]

                self.conn.commit()

                return valor_record

        except pysql.MySQLError as e:
            print(repr(f'Error DR: {id_item} \n insert_query_errors: {e} \n db_adapter/update_accountoinfo_query'))
        finally:
            self.close_connection()
            print(repr(f'{id_item} \n Database connection closed insert_query_errors. \n db_adapter/update_accountoinfo_query'))


class DBAdapterSQLAlchemy:
    """Database connection class using SQLAlchemy."""
    def __init__(self):
        self.db_host = cfg.DATABASEDR["db_host"]
        self.db_username = cfg.DATABASEDR["db_username"]
        self.db_password = cfg.DATABASEDR["db_password"]
        self.db_port = cfg.DATABASEDR["db_port"]
        self.db_name = cfg.DATABASEDR["db_name"]
        self.engine = None
        self.Session = None
        self.session = None
        self.JsonNode = JsonNode()

    def open_connection(self):
        """Create an SQLAlchemy engine and session."""
        try:
            if self.engine is None:
                self.engine = create_engine(
                    f"mysql+pymysql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}",
                    echo=False,
                )
                self.Session = sessionmaker(bind=self.engine)
                self.session = self.Session()
                print("Connection opened successfully with SQLAlchemy.")
        except OperationalError:
            raise
        except IntegrityError:
            raise
        except SQLAlchemyError:
            raise
        except Exception as e:
            print(repr(f"Error DR: general no esperado SQLAlchemy open: {e}"))
            raise

    def close_connection(self):
        """Close the session and engine."""
        try:
            if self.session:
                self.session.close()
                print("Connection closed SQLAlchemy.")
            if self.engine:
                self.engine.dispose()
                print("Connection pool closed SQLAlchemy.")
        except OperationalError:
            raise
        except IntegrityError:
            raise
        except SQLAlchemyError:
            raise
        except Exception as e:
            print(repr(f"Error DR: general no esperado SQLAlchemy open: {e}"))
            raise

    def select_query(self):
        """Execute SQL query with eager loading of the related 'document'."""
        try:
            self.open_connection()
            nodes = (
                self.session.query(JsonNode)
                .options(joinedload(JsonNode.document), joinedload(JsonNode.type))
                .all()
            )
            return nodes
        except OperationalError:
            raise
        except IntegrityError:
            raise
        except DataError:
            raise
        except StatementError:
            raise
        except InvalidRequestError:
            raise
        except Exception as e:
            print(repr(f"Error DR: general no esperado SQLAlchemy select: {e}"))
            raise
        finally:
            self.close_connection()

class DBAsyncAdapter:
    def __init__(self):
        self.db_host = cfg.DATABASEDR["db_host"]
        self.db_username = cfg.DATABASEDR["db_username"]
        self.db_password = cfg.DATABASEDR["db_password"]
        self.db_port = cfg.DATABASEDR["db_port"]
        self.db_name = cfg.DATABASEDR["db_name"]
        self.conn = None
        self.pool = None 

    async def open_connection(self):
        """Connect to MySQL Database."""
        timeout = cfg.config_database["timeout"]
        try:
            if self.pool is None:
                self.pool = await asyncio.wait_for(
                    aiomysql.create_pool(
                        host=self.db_host,
                        port=self.db_port,
                        user=self.db_username,
                        password=self.db_password,
                        db=self.db_name,
                        charset='utf8mb4',
                        autocommit=False
                    ),
                timeout=timeout
                )
            print("Conexión abierta con éxito")
        except aiomysql.MySQLError as e:
            print(repr(f"Error DR: al abrir conexión: {e}"))
        except asyncio.TimeoutError:
            print(repr(f"Error DR: El intento de conexión superó los {timeout} segundos de espera."))
        
    async def select_query(self, query, param):
        """Execute SQL query."""
        await self.open_connection()
        async with self.pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(query, param)
                records = await cur.fetchall()
                return records
            
    async def select_query_asincrona(self, query, param):
        print("Antes de abrir la conexión")
        await self.open_connection()

        try:
            async with self.pool.acquire() as conn:
                print("Conexión adquirida, ejecutando consulta")
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    await cur.execute(query, param)
                    print("Consulta ejecutada, obteniendo resultados")
                    
                    try:
                        records = await asyncio.wait_for(cur.fetchall(), timeout=5)
                        return records
                    except asyncio.TimeoutError:
                        print("Error DR: La consulta tomó demasiado tiempo.")
                        return []

        except aiomysql.MySQLError as e:
            print(repr(f'Error DR: select_query_asincrona: {e}'))
            return []

        except Exception as e:
            print(repr(f'Error DR: general en select_query_asincrona: {e}'))
            return []

        finally:
            print("Conexión cerrada.")
        
    async  def insert_query(self, query, param):
        """Execute SQL query."""
        await self.open_connection()
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                result = await cur.execute(query, param)
                return result

    async def insert_query_time(self, query, param,time_start_total):
        """Execute SQL query."""
        await self.open_connection()
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                end_time_total = time.perf_counter()
                time_total = end_time_total - time_start_total
                param = (time_total,) + param
                result = await cur.execute(query, param)
                return result
    

    async def update_query_asincrona(self, query_update, param_update):
        await self.open_connection()

        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(aiomysql.DictCursor) as cur:
                    try:
                        await cur.execute(query_update, param_update)
                        await conn.commit()  # Confirmar los cambios
                        return True
                    except aiomysql.MySQLError:
                        await conn.rollback()  # Deshacer cambios en caso de error
                        print(repr("Error DR: Rollback realizado cambio de estado \n bd_adapter/update_query_asincrona"))
                        return False
        except aiomysql.MySQLError as e:
            print(repr(f'Error DR: update_query_asincrona: {e} \n bd_adapter/update_query_asincrona'))
            return False
        except Exception as e:
            print(repr(f'Error DR: general en update_query_asincrona: {e} \n bd_adapter/update_query_asincrona'))
            return False
        finally:
            print(repr("Conexión cerrada después de la actualización \n bd_adapter/update_query_asincrona"))
            
        
    

