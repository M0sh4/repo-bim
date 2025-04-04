import sys
import pymysql as pysql

DB_CONFIG = {
    'user': 'admin',
    'password': 'B1MPDP2024$',
    'host': 'db-mid-prod-mysql-dryrun.chy48i8i0qi1.us-east-1.rds.amazonaws.com',
    'database': 'DRYRUN_CAPTURE',
    'port': 3306
}
STORED_PROCEDURE_NAME1 = 'status_error'
STORED_PROCEDURE_NAME2 = 'status_seguimiento'
STORED_PROCEDURE_NAME3 = 'status_general'
def open_connection():
    """Connect to MySQL Database."""
    connection_successful = False
    try:
        conn = pysql.connect(host=DB_CONFIG['host'], 
                            db=DB_CONFIG['database'], 
                            port=DB_CONFIG['port'], 
                            user=DB_CONFIG['user'],
                            password=DB_CONFIG['password'], 
                            charset='utf8mb4', 
                            cursorclass=pysql.cursors.DictCursor,
                            connect_timeout=20)
        connection_successful = True
        return conn
    except pysql.MySQLError as e:
        print(repr(f"Error DR: Conexión BD open_connection: {e}"))
        raise
    finally:
        if connection_successful:
            print('Connection opened successfully.')
        else:
            print('Error DR: Failed to open connection.')


def get_status():  
    conn = open_connection()
    try:    
        with conn.cursor() as cur:
            cur.callproc(STORED_PROCEDURE_NAME1)
            results = []
            while True:
                result_set = cur.fetchall()
                if result_set:
                    results.extend(result_set)
                if not cur.nextset():
                    break
            return results

    except pysql.OperationalError:
        raise
    except pysql.InternalError:
        raise
    except pysql.MySQLError:
        raise
    except Exception as e:
        print(repr(f'Error: {e}'))
        raise
    finally:
        if conn:
            conn.close()
            conn = None
            print('Database connection closed')

def get_seguimiento():  
    conn = open_connection()
    try:    
        with conn.cursor() as cur:
            cur.callproc(STORED_PROCEDURE_NAME2)
            results = []
            while True:
                result_set = cur.fetchall()
                if result_set:
                    results.extend(result_set)
                if not cur.nextset():
                    break
            return results

    except pysql.OperationalError:
        raise
    except pysql.InternalError:
        raise
    except pysql.MySQLError:
        raise
    except Exception as e:
        print(repr(f'Error: {e}'))
        raise
    finally:
        if conn:
            conn.close()
            conn = None
            print('Database connection closed')


def get_general():  
    conn = open_connection()
    try:    
        with conn.cursor() as cur:
            cur.callproc(STORED_PROCEDURE_NAME3)
            results = []
            while True:
                result_set = cur.fetchall()
                if result_set:
                    results.extend(result_set)
                if not cur.nextset():
                    break
            return results

    except pysql.OperationalError:
        raise
    except pysql.InternalError:
        raise
    except pysql.MySQLError:
        raise
    except Exception as e:
        print(repr(f'Error: {e}'))
        raise
    finally:
        if conn:
            conn.close()
            conn = None
            print('Database connection closed')
