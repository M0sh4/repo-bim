import boto3
from libs import pymysql
import os
import gzip
import io
import time
import re
import json
from datetime import datetime, timedelta

# Conexión a base de datos
RDS_HOST = 'db-mid-prod-mysql-dryrun.chy48i8i0qi1.us-east-1.rds.amazonaws.com'
DB_NAME = 'DRYRUN_CAPTURE'
TABLE_NAME = 'DR5_Log'
USER = 'admin'
PASSWORD = 'B1MPDP2024$'

COMPONENT = 'pago-credito-fcompartamos'

# S3
S3_BUCKET = 'pdp-exported-logs'

# Cliente S3
s3_client = boto3.client('s3')

def exec(manual, date_extract):
    if not test_db_connection():
        print("No se pudo conectar a la base de datos. Terminando la ejecución.")
        return

    # Calcular el prefijo del bucket
    LOG_GROUP_PREFIX = calculate_log_group_prefix(manual, date_extract)
    
    print(f"LOG Group -> {LOG_GROUP_PREFIX}")

    # Listar archivos en S3
    files = list_files_in_s3(S3_BUCKET, LOG_GROUP_PREFIX)
    
    print(f"Files -> {files}")

    if not files:
        print("No files found.")
        return

    processed_logs = []

    for s3_key in files:
        print(s3_key)
        log_data = get_and_decompress_gz(S3_BUCKET, s3_key)
        # print(log_data)
        if log_data is None:
            continue

        parsed_logs = parse_logs(log_data, s3_key)
        processed_logs.extend(parsed_logs)

        # for log in parsed_logs:
        #     print(log)

    save_logs_to_db(processed_logs)

def test_db_connection():
    connection = None
    try:
        connection = pymysql.connect(
            host=RDS_HOST, 
            db=DB_NAME, 
            port=3306, 
            user=USER,
            password=PASSWORD, 
            charset='utf8mb4', 
            cursorclass=pymysql.cursors.DictCursor, 
            connect_timeout=30)

        print("Conexión a la base de datos exitosa.")
        return True

    except pymysql.OperationalError as e:
        print(f"Error conectando a MySQL: {e}")
        return False

    finally:
        if connection:
            connection.close()

def calculate_log_group_prefix(manual, date_extract):
    if manual:
        return f"{COMPONENT}/{date_extract}"
    else:
        now = datetime.now()
        
        # Calcular la hora de corte (una hora atrás)
        cut_off_time = now - timedelta(hours=1)
        print(cut_off_time)
        # Formatear el prefijo del bucket con minutos en 00
    return f"pago-credito-fcompartamos/{cut_off_time.year}/{cut_off_time.month:02}/{cut_off_time.day:02}/{cut_off_time.hour}/"
    

def list_files_in_s3(bucket, prefix):
    result = []
    
    # Listar los objetos en el bucket    
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    
    # Obtener la lista de archivos
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f"Found file: {obj['Key']}")
            result.append(obj['Key'])
    else:
        print("No hay archivos")
    
    return result



def get_and_decompress_gz(bucket, key):
    try:
        response = s3_client.get_object(Bucket=bucket, Key=key)
        gz_body = response['Body'].read().decode('utf-8')
        # with gzip.GzipFile(fileobj=io.BytesIO(gz_body)) as gz_file:
        #     log_data = ""
        #     for line in gz_body:
        #         line_decoded = line.decode('utf-8')
        #         # print(line_decoded)
        #         log_data += line_decoded
        #     print(log_data)
        return gz_body

    except Exception as e:
        print(f"Error reading or decompressing {key}: {e}")
        return None

def parse_logs(log_data, s3_key):
    logs = []
    try:
        current_log = {}
        is_parsing = False

        for line in log_data.splitlines():
            # if "START RequestId:" in line:
            #     # Reiniciar el log actual
            #     current_log = {
            #         "request_ewp": "",
            #         "response_ewp": "",
            #         "api_name_ewp": "",
            #         "status_code_ewp": "",
            #         "funcionality": "APP",  # Se asigna el valor fijo
            #         "component": "lf-mdw-api-sender-awspdp",  # Se puede asignar un valor fijo o dinámico si se conoce
            #         "date_capture": "",
            #         "id_log": ""
            #     }
            #     is_parsing = True
            #     # Extraer el id_log de la línea de inicio
            #     id_log_match = re.search(r'START RequestId: ([\w-]+)', line)
            #     current_log["id_log"] = id_log_match.group(1) if id_log_match else ""
            #     print(f"Parsed id_log: {current_log['id_log']}")

            # elif "END RequestId:" in line and is_parsing:
            #     logs.append(current_log)
            #     is_parsing = False

            # elif is_parsing:
                # Captura de request_ewp
            if "('REQUEST', '" in line:
                if is_parsing:
                    logs.append(current_log)
                current_log = {
                    "request_ewp": "",
                    "response_ewp": "",
                    "api_name_ewp": "",
                    "status_code_ewp": "",
                    "funcionality": "pagos",  # Se asigna el valor fijo
                    "component": COMPONENT,  # Se puede asignar un valor fijo o dinámico si se conoce
                    "date_capture": "",
                    "id_log": "",
                    "path_s3": s3_key
                }
                event_start = line.index("('REQUEST', '") + len("('REQUEST', '")
                event_data = line[event_start:-2].strip()
                event_data = event_data.replace('\\\\', '\\')
                current_log["request_ewp"] = event_data
                current_log["api_name_ewp"] = json.loads(event_data)["api_name"]
                print(f"Parsed request_ewp: {current_log['request_ewp']}")
                is_parsing = True
            # Captura de response_ewp
            elif "('RESPONSE', '" in line:
                if is_parsing == False:
                    current_log = {
                        "request_ewp": "",
                        "response_ewp": "",
                        "api_name_ewp": "",
                        "status_code_ewp": "",
                        "funcionality": "pagos",  # Se asigna el valor fijo
                        "component": COMPONENT,  # Se puede asignar un valor fijo o dinámico si se conoce
                        "date_capture": "",
                        "id_log": "",
                        "path_s3": s3_key
                    }
                response_start = line.index("('RESPONSE', '") + len("('RESPONSE', '")
                response_data = line[response_start:-2].strip()
                response_data = response_data.replace('\\\\', '\\')
                current_log["response_ewp"] = response_data
                print(f"Parsed response_ewp: {current_log['response_ewp']}")

            # Captura de status_code_ewp
            elif "('STATUS_CODE', " in line:
                status_code_start = line.index("('STATUS_CODE', ") + len("('STATUS_CODE', ")
                status_code_data = line[status_code_start:-1].strip()
                current_log["status_code_ewp"] = status_code_data
                print(f"Parsed status_code_ewp: {current_log['status_code_ewp']}")
                parsed_datetime = datetime.strptime(line.split()[0]+" "+line.split()[1], "%Y-%m-%d %H:%M:%S,%f") + timedelta(hours=5)
                print(parsed_datetime)
                formatted_datetime_str = parsed_datetime.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
                current_log["date_capture"] = formatted_datetime_str  # Extraer solo la fecha
                print(f"Parsed date_capture: {current_log['date_capture']}")
                logs.append(current_log)
                is_parsing = False
        print(logs)
        return logs
    except Exception as e:
        print("Error de parsing: ", e)
        return logs

def save_logs_to_db(processed_logs):
    if not processed_logs:
        print("No logs to save.")
        return

    connection = None
    try:
        connection = pymysql.connect(
            host=RDS_HOST,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )

        with connection.cursor() as cursor:
            sql = f"""
            INSERT INTO {TABLE_NAME} (funcionality, component, date_capture, request_ewp, response_ewp, status_code_ewp,
                                        flg_status_registry, request_comviva_json, response_comviva_json, status_code_comviva,
                                        date_test_execution, is_result_equals, time_execution, id_log, api_name_ewp, path_s3)
            VALUES (%s, %s, %s, %s, %s, %s, '', '', '', '', '', '', '', %s, %s, %s)
            """
            param2 = [
                (
                    log['funcionality'],
                    log['component'],
                    log['date_capture'], 
                    log['request_ewp'], 
                    log['response_ewp'], 
                    log['status_code_ewp'], 
                    log['id_log'], 
                    log['api_name_ewp'], 
                    log['path_s3']
                )
                for log in processed_logs
            ]
            cursor.executemany(sql, param2)
            connection.commit()
            print(f"Logs inserted for {len(processed_logs)} entries.")

    except pymysql.OperationalError as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if connection:
            connection.close()
