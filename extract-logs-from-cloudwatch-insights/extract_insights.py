import boto3
import time
from datetime import datetime, timezone, timedelta
from openpyxl import Workbook
from concurrent.futures import ThreadPoolExecutor, as_completed

def run_cloudwatch_insights_query(log_group_name, query, start_time, end_time):
    # Crea el cliente de CloudWatch Logs
    boto3_session = boto3.Session(profile_name="PDP-PROD-NC")
    logs_client = boto3_session.client("logs", region_name="us-east-1")
    start_time_utc = to_utc_ms(start_time)
    end_time_utc = to_utc_ms(end_time)
    # Inicia la consulta
    start_query_response = logs_client.start_query(
        logGroupName=log_group_name,
        queryString=query,
        startTime=start_time_utc,  # Tiempos en formato epoch (segundos desde 1970-01-01)
        endTime=end_time_utc
    )

    query_id = start_query_response['queryId']
    print(f"Query iniciada con el ID: {query_id}")

    # Espera hasta que la consulta finalice
    while True:
        response = logs_client.get_query_results(queryId=query_id)
        status = response['status']

        if status == 'Complete':
            print("Consulta completada.")
            return response['results']
        elif status in ['Failed', 'Cancelled']:
            print(f"Consulta con estado: {status}")
            return []

        print("Consulta en progreso... esperando 2 segundos.")
        time.sleep(2)


def to_utc_ms(dt):
    return int(dt.astimezone(timezone.utc).timestamp() * 1000)


def save_excel(results):
    wb = Workbook()
    ws = wb.active
    ws.append(["@timestamp", "serviceFlow", "status", "serviceRequestId", "@message"])
    counter = 0
    for row in results:
        for col in row:
            #     print(row)
            field = col.get('field')
            value = col.get('value')
            match field:
                case "@timestamp":
                    tt = value
                case "serviceFlow":
                    sf = value
                case "status":
                    st = value
                case "serviceRequestId":
                    sr = value
                case "@message":
                    ms = value
        ws.append([tt, sf, st, sr, ms])
        counter += 1
    print(counter)
    wb.save("logs.xlsx")


def threads_future(intervals):
    max_workers = 10  # Ajusta según lo que AWS te permita, no uses demasiados para evitar rate limits
    all_results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Lanzamos cada intervalo en paralelo
        future_to_interval = {
            executor.submit(
                run_cloudwatch_insights_query, 
                log_group, 
                insights_query, 
                start, 
                end
            ): (start, end) 
            for (start, end) in intervals
        }

        # Recolectamos resultados a medida que se completan
        for future in as_completed(future_to_interval):
            (start, end) = future_to_interval[future]
            try:
                data = future.result()
                # Agregamos 'data' a la lista total
                all_results.extend(data)
            except Exception as exc:
                print(f"Error procesando intervalo {start} - {end}: {exc}")
    
    return all_results

if __name__ == "__main__":
    # Ejemplo de uso
    log_group = "/aws/lambda/lf-mdw-api-sender"
    # Consulta de CloudWatch Insights (ejemplo sencillo: obtén los 20 eventos más recientes)
    insights_query = """
    fields @timestamp,
       serviceFlow,
       status,
       serviceRequestId,
       @message,
       @logStream,
       @log
    | filter @message like '[lambda_function:64]'
        and ispresent(status)
        and ispresent(serviceFlow)
        and (@message like 'LOGIN_POLICY_V2'
            or @message like 'SELFSETAUTHMFA_V2'
            or @message like 'SYSTEMTOKEN'
            or @message like 'GET_USER_AND_ACCOUNT_DETAILS_V3'
            or @message like 'CHANGEAUTHFACTOR_V3'
            or @message like 'USER_SELF_DEL_V2'
            or @message like 'BALENQ_V2'
            or @message like 'MODUSERV2'
            or @message like 'GET_USER_DETAILS_WITH_ACC'
            or @message like 'ADDUSERV2'
            or @message like 'GETFEES'
            or @message like 'INITATMPINWAC'
            or @message like 'BALENQ_SYS_TOKEN'
                or @message like 'USRTXNDTLS_POST')
    | display @timestamp, serviceFlow, status, serviceRequestId, @message, @logStream, @log
    | sort @timestamp desc
    """
    PERU_TIMEZONE = timezone(timedelta(hours=-5))
    START_TIME_PERU = datetime(2025, 4, 1, 15, 29, 0, 0, tzinfo=PERU_TIMEZONE)
    END_TIME_PERU = datetime(2025, 4, 1, 15, 56, 0, 0, tzinfo=PERU_TIMEZONE)
    
    END_TIME_MOD = START_TIME_PERU
    intervals = []
    while END_TIME_MOD.timestamp() < END_TIME_PERU.timestamp():
        START_TIME_MOD = END_TIME_MOD
        END_TIME_MOD = END_TIME_MOD + timedelta(minutes=1)
        intervals.append((START_TIME_MOD, END_TIME_MOD))
        print(f"{START_TIME_MOD}  {END_TIME_MOD}")
    results = threads_future(intervals)
    save_excel(results)
    