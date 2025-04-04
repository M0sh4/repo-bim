import sys
import pymysql as pysql
import config_token as cfg
sys.path.insert(1,'libs')

class DBAdapter:
    """Database connection class."""

    def __init__(self, type_db, ambiente):
        
        self.ambiente = ambiente
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
            if self.conn is None:
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
            if self.conn:
                self.conn.close()
                self.conn = None
                print('Database connection closed select_query db_adapter/select_query.')

    def insert_query(self, query, param):
        """Execute SQL query."""
        try:
            with self.conn.cursor() as cur:
                result = cur.execute(query,param)
                self.conn.commit()
                affected = cur.rowcount
                cur.execute("UNLOCK TABLES;")
                print("Tabla desbloqueada exitosamente.")
                cur.close()
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

            if self.conn:
                self.conn.close()
                self.conn = None
                print('Database connection closed insert query.')
    
    def blocktable(self):
        """Execute SQL query."""
        try:
           self.open_connection()
           with self.conn.cursor() as cur:
                cur.execute("LOCK TABLES token_auth WRITE;")
                print("Tabla bloqueada exitosamente.")

        except pysql.OperationalError:
            raise
        except pysql.InternalError:
            raise
        except pysql.MySQLError:
            raise
        except Exception as e:
            print(repr(f'Error DR: General: {e}'))
            raise
        #finally:
            # if self.conn:
            #     self.conn.close()
            #     self.conn = None
            #print('Database connection closed insert query.')