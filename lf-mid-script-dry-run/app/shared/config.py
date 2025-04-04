ambiente = {
    "dev": {
        "arn_lambda_api_sender" : "arn:aws:lambda:us-east-1:730335559791:function:lf-mdw-api-sender",
        "profile_name": "PDP-DEV-NC",
        "region":"us-east-1",
        "httpconnect": "edxgq24nqi.execute-api.us-east-1.amazonaws.com",
        "x_api":"M7qxQupagL3Puj9wRgJja9g304rcknbI7HrXhLj7",
        "recurso": "/dev/webservice/sender",
        "table_log": "Log_26112024",
        "table_Values_Match": "Values_Match",
        "table_Values_Transaccion": "Values_Transaccion",
        "table_Error":"Error_log",
        "findtransaccion_match": "findtransaccion_match",
        "table_reverse_reverse_cahorros": "DR2_REVERSA_COMPARTAMOS_AHORROS_20241230",
        "stored_select_logs": "SP_SELECT_LOG",
        "DBNC" : {
            "db_password" : "y1eJPOuKvRTr5oAGSouw",
            "db_name" : "dbmdwdevtest",
            "db_host" : "localhost",
            "db_port":8090,
            "connect_timeout": 30,
            "db_username" : "root",
            "db_table_atm_otp": "atm_otp_test"
        },
        "p_migracion": "1357",
        "p_default": "202505"
    },
    "uat": {
        "arn_lambda_api_sender" : "arn:aws:lambda:us-east-1:730335559791:function:lf-mdw-api-sender",
        "profile_name": "PDP-DEV-NC",
        "region":"us-east-1",
        "httpconnect": "mqfndijsjh.execute-api.us-east-1.amazonaws.com",
        "x_api":"EoMxtKHj1X9eEOFVbM9RM7CJTrDgVSdN2HCbP4Tb",
        "recurso": "/qa/b1m/pdp/b3po7/00qmv8dj45",
        "table_log": "Log_08122024",
        "table_Values_Match": "USERS_UAT_1",
        "table_Values_Transaccion": "Values_Transaccion_uat",
        "table_Error":"Error_log",
        "findtransaccion_match": "TD_TRANSACTION_HISTORY_20241208",
        "table_reverse_reverse_cahorros": "DR2_REVERSA_COMPARTAMOS_AHORROS_20241230",
        "stored_select_logs": "SP_SELECT_LOG",
        "DBNC" : {
            "db_password" : "y1eJPOuKvRTr5oAGSouw",
            "db_name" : "dbmdwdevtest",
            "db_host" : "localhost",
            "db_port":8090,
            "connect_timeout": 30,
            "db_username" : "root",
            "db_table_atm_otp": "atm_otp_test"
        },
        "p_migracion": "1357",
        "p_default": "202405"
    },
    "preprod": {
        "arn_lambda_api_sender" : "arn:aws:lambda:us-east-1:474668388170:function:lf-mdw-api-sender",
        "profile_name": "PDP-PROD-NC-6",
        "region":"us-east-1",
        "httpconnect": "mqfndijsjh.execute-api.us-east-1.amazonaws.com",
        "x_api":"EoMxtKHj1X9eEOFVbM9RM7CJTrDgVSdN2HCbP4Tb",
        "recurso": "/qa/b1m/pdp/b3po7/00qmv8dj45",
        "table_log": "DR_LOAD_TEST", #DR4_TD_Log_20250104
        "table_Values_Match": "USER_LOAD_TEST",
        "table_Values_Transaccion": "DR4_Transaccion_CASHIN",# DR5_USERS_UAT_1 DR5_Transaccion DR4_Transaccion_20250104 DR4_Transaccion_CASHIN  Values_Transaccion_dr3_cashin_20241230 #Values_Transaccion_dr3_preprod_20241230
        "table_Error":"Error_log",
        "findtransaccion_match": "DR4_TD_TRANSACTION_HISTORY_20250104",
        "table_reverse_reverse_cahorros": "DR4_REVERSA_COMPARTAMOS_AHORROS_20251014",
        "stored_select_logs": "SP_SELECT_LOG",
        "DBNC" : {
            "db_password" : "BCz-a^X<j]Mq)WA|-%w8",
            "db_name" : "app_bim_prod_1",
            "db_host" : "localhost",
            "db_port":3306,
            "connect_timeout": 30,
            "db_username" : "apps_user",
            "db_table_atm_otp": "atm_otp"
        },
        "p_migracion": "1357",
        "p_default": "202503"
    },
}

LOGIN_AUTH = {
    "type_auth": {
        "admin": {
            "usuario": "RenzoFerroQA",
            "password": "123renzo@QA",
            "workspace": "ADMIN",
            "identifier_type": "LOGINID",
            "authentication_type": "PASSWORD"
        },
        "msisdn":{
            "usuario": "",
            "password": "",
            "workspace": "SUBSCRIBER",
            "identifier_type": "MSISDN",
            "authentication_type": "PIN"
        },
        "agente":{
            "VIRTUALINTEROPCFBIM" :{ 
                "usuario": "VIRTUALINTEROPCFBIM", #VIRTUALINTEROPCFBIM
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BUSINESS",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51991022660" 
            },
            "VIRTUALINTEROPCFCCE":{  
                "usuario": "VIRTUALINTEROPCFCCE",
                "password": "Pdp@Uat@135@13",
                "workspace": "BUSINESS",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51963564251"
            },
            "AgenteBNacion":{  
                "usuario": "AgenteBNacion", 
                "password": "bNUat@135@15", 
                "workspace": "BUSINESS",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51987987007" 
            },
            "COMPWVIRTUAL163":{
                "usuario": "COMPWVIRTUAL163",
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BUSINESS",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51938948480"
            }, 
            "COMPWKASNET":{ 
                "usuario": "COMPWKASNET",
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BUSINESS",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51989294475"
            },
            "COMPWFULLCARGA":{  
                "usuario": "COMPWFULLCARGA", 
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BUSINESS",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51969752322"
            },
            "COMPWGOPAY":{  
                "usuario": "COMPWGOPAY",  #COMPWFULLCARGA
                "password": "pny7mx/qpn*qKyJk6#Ew",  #Dev@UAT#250112 pny7mx/qpn*qKyJk6#Ew
                "workspace": "BUSINESS",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51915962396"  #51969752322
            },
            "atmcompartamos":{
                "usuario": "AgenteFCompartamos", 
                "password": "Tev@UAT#0812",
                "workspace": "BUSINESS",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51987987005"
            },
            "atmfullcargas":{
                "usuario": "AgenteFullcarga", 
                "password": "Comvivapdp123456789#",
                "workspace": "BUSINESS",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51987987004"
            },
            "cashout":{
                "usuario": "VIRTUALINTEROPCFBIM", #VIRTUALINTEROPCFBIM
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BUSINESS",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51991022660" 
            },
            "cashin":{
                "usuario": "VIRTUALINTEROPCFBIM", #VIRTUALINTEROPCFBIM
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BUSINESS",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51991022660" 
            },
            "azulito":{
                "usuario": "lindley",
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BILLER",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51999000008"
            },
            "bitel":{
                "usuario": "bitel",
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BILLER",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51999000003"
            },
            "unique":{
                "usuario": "unique",
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BILLER",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51999000005"
            },
            'airtimebitel':{
                "usuario": "airtimebitel", #airtimemovistar
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BILLER",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51999000002" #51988603874
            },
            'airtimemovistar':{
                "usuario": "airtimemovistar", #airtimemovistar airtimebitel
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BILLER",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51988603874" #51988603874  51999000002
            },
            'sunat':{
                "usuario": "sunat", 
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BILLER",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51975133632" 
            },
            "CRAPW0061":{
                "usuario": "CRAPW0061",
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BILLER",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51913069818"
            },
            "COMPW0086":{
                "usuario": "COMPW0086",
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BILLER",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51938440932"
            },
            "COMPW0165":{
                "usuario": "COMPW0165",
                "password": "pny7mx/qpn*qKyJk6#Ew",
                "workspace": "BILLER",
                "identifier_type": "LOGINID",
                "authentication_type": "PASSWORD",
                "msisdn": "51985020019"
            }
        }
    },
    "api_url": "https://44.209.0.100/mobiquitypay/ums/v4/user/auth/login",
    "device_info": {
        "appIdentifier": "PDP.DEV",
        "appName": "MobiquityPay",
        "appVersion": "10.09",
        "deviceId": "25343d4a-6d36-453e-a82a-78e3f575ef12d",
        "isPublicDevice": "N",
        "model": "motorola moto",
        "os": "ANDROID"
    }
}

#d
# DATABASE = {
#     "db_password" : "2024b1mBIM",
#     "db_name" : "dryrun-capture",
#     "db_host" : "localhost",
#     "db_port":3306,
#     "connect_timeout": 30,
#     "db_username" : "admin"
#  }
#pp
DATABASEDR = {
    "db_password" : "B1MPDP2024$",
    "db_name" : "DRYRUN_CAPTURE",
    "db_host" : "db-mid-prod-mysql-dryrun.chy48i8i0qi1.us-east-1.rds.amazonaws.com",
    "db_port":3306,
    "connect_timeout": 30,
    "db_username" : "admin"
 }


config_database = {
    "timeout" : 10,
    "db_gethistory": "DR4_TD_TRANSACTION_HISTORY_20250104",
    "time_refund_tranfer": 8,
    "time_Lima":5 
}

JSON_API = {
    "especificos" : [
        "merchantpayment",
        "payment",
        "cashin",
        "bnacion_ofi_ci/cashin",
        "merchantpayment/quote",
        "payment/quote",
        "updateaccountholderpersonalinformation",
        "atmcashout",
        "refund",
        "reversetransaction"
    ],
 "contextos": {
        "sunat":"sunat",
        "unique":"unique",
        "azulito": "azulito",
        "lindley": "azulito",
        "airtimebitel":"airtimebitel",
        "airtimemovistar":"airtimemovistar",
        "bitel":"bitel",
        "claro":"claro",
        "pmpcompras":"pmpcompras",
        "backus":"backus",
        "digiflow":"wu",
        "VIRTUALINTEROPCFBIM" : "VIRTUALINTEROPCFBIM",
        "VIRTUALINTEROPCFCCE" : "VIRTUALINTEROPCFCCE",
        "COMPWGOPAY": "COMPWGOPAY",
        "BNAPWVIRTUAL157" : "AgenteBNacion",
        "COMPWFULLCARGA" : "COMPWFULLCARGA",
        "COMPWVIRTUAL163" : "COMPWVIRTUAL163",
        "COMPWKASNET" : "COMPWKASNET",
        "51913069818":"CRAPW0061", #crandes
        "51938440932":"COMPW0086", #creditos
        "51985020019":"COMPW0165", #Ahorros
        "wu":"wu",  #51087000115
        "Actualizacion por RENIEC OnLine":"reniec",
        "Actualizacion desde Perfil WU":"wu",
        "Actualizacion de nombre":"nombre",
        "Actualizacion por Cambio de Emisor":"emisor",
        "Q09NUFdWSVJUVUFMMTYzOkNGLjRnM250My5W": "atmcompartamos",
        "Q09NUFdGVUxMQ0FSR0E6RkNfRnVsbGNAcmdhJDIwMjJBYnJpbA==":"atmfullcargas",
        "CASH_OUT":"cashout",
        "CASH_IN":"cashin"
    },
    "msisdn_agente":
    {
        "51985020019" : "COMPARTAMOS AHORROS",
        "51946594070" : "EXPERIAN PERU S.A.C",
        "51913069818" : "CRANDES",
        "51989102431" : "WU",
        "51938440932" : "COMPARTAMOS CREDITOS"
    }
}

format_fecha  = '%Y-%m-%dT%H:%M:%S.%fZ'

ruta_csv_ubligeo = 'app/shared/ubigeo.csv'

query_select_mapping_plantilla = '''
    SELECT
        JSON_OBJECT(
            'api_name', (
                SELECT
                    JSON_OBJECTAGG(api_ewp, api_data)
                FROM (
                    SELECT
                        api_ewp,
                        JSON_ARRAYAGG(
                            JSON_OBJECT(
                                'api_ewp', api_ewp,
                                'id_json_api',  IFNULL(id_json_api, 0),
                                'clave_ewp', clave_ewp,
                                'split_ewp', split_ewp,
                                'type_date', type_date,
                                'valor_ewp', valor_ewp,
                                'clave_comv', clave_comv,
                                'valor_comv', valor_comv,
                                'type_replace', type_replace,
                                'id_mapping', id_mapping,
                                'valor_position_ewp', valor_position_ewp,
                                'is_compare', is_compare,
                                'type_compare', type_compare,
                                'parent_id_mapping', IFNULL(parent_id_mapping,0),
                                'is_identifier', IFNULL(is_identifier,0),
                                'is_capture', 0,
                                'is_saved', IFNULL(is_saved,""),
                                'sel_value', IFNULL(sel_value,""),
                                'table_save', IFNULL(table_save,"")
                            )
                        ) AS api_data
                    FROM Mapping
                    Where id_json_api IS NOT NULL
                    GROUP BY api_ewp
                    order by id_mapping asc
                ) AS subquery
            ),
        'type_token', (
                SELECT
                    JSON_OBJECTAGG(api_name, api_data_array)
                FROM (
                    SELECT
                        api_name,
                        JSON_ARRAYAGG(
                            JSON_OBJECT(
                                'id_json_api', id_json_api,
                                'clave_ewp', api_name,
                                'type_token', COALESCE(type_token, 'admin'),
                                'version_json', version_json
                            )
                        ) AS api_data_array
                    FROM Plantilla_json_api
                    WHERE status_json = 1
                    GROUP BY api_name
                ) AS subquery2
            )
        ) AS result_json;
'''

query_flujos = {
    "registration" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("registration")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("registration")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "activation" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("activation")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("activation")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
                "updateaccountholderpersonalinformation" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("updateaccountholderpersonalinformation")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    and request_ewp  REGEXP 'Actualizacion por RENIEC OnLine'
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("updateaccountholderpersonalinformation")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    and l.request_ewp  REGEXP 'Actualizacion por RENIEC OnLine'
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "getbalance" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("getbalance")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("getbalance")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "gettransactionhistory" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("gettransactionhistory")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("gettransactionhistory")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "getaccountholderinfo" : '''
                    UPDATE {tabledata} l
                    SET l.status = '{uuid_text}'
                    WHERE l.id IN
                    (
                        SELECT id FROM {tabledata} j
                        WHERE j.api_name_ewp = "getaccountholderinfo"
                        AND j.status_code_ewp = '200'
                        AND j.status_code_comviva <> '200'
                        and j.flg_status_registry = ""
                        AND j.status = '' {filtro_idlog}
                        ORDER BY j.date_capture_datetime desc
                        LIMIT {limite}
                        FOR UPDATE SKIP LOCKED
                    )
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto
                    FROM {tabledata} l
                    WHERE 
                    l.api_name_ewp in ("getaccountholderinfo")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "cashin_VIRTUALINTEROPCFBIM" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("cashin")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    and request_ewp REGEXP 'VIRTUALINTEROPCFBIM'
                    and contexto <> ''
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("cashin")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.request_ewp REGEXP 'VIRTUALINTEROPCFBIM'
                    and l.status = '{uuid_text}'
                    and l.contexto <> ''
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "cashin_COMPWVIRTUAL163" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("cashin")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    and request_ewp REGEXP 'COMPWVIRTUAL163'
                    and contexto <> ''
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("cashin")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.request_ewp REGEXP 'COMPWVIRTUAL163'
                    and l.status = '{uuid_text}'
                    and l.contexto <> ''
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "cashin_COMPWKASNET" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("cashin")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    and request_ewp REGEXP 'COMPWKASNET'
                    and contexto <> ''
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("cashin")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.request_ewp REGEXP 'COMPWKASNET'
                    and l.status = '{uuid_text}'
                    and l.contexto <> ''
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "cashin_COMPWFULLCARGA" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("cashin")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    and request_ewp REGEXP 'COMPWFULLCARGA'
                    and contexto <> ''
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("cashin")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.request_ewp REGEXP 'COMPWFULLCARGA'
                    and l.status = '{uuid_text}'
                    and l.contexto <> ''
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "cashin_COMPWGOPAY" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("cashin")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    and request_ewp REGEXP 'COMPWGOPAY'
                    and contexto <> ''
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("cashin")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.request_ewp REGEXP 'COMPWGOPAY'
                    and l.status = '{uuid_text}'
                    and l.contexto <> ''
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "reversetransaction_cashin" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    AND ((api_name_ewp IN ("reversetransaction") and request_ewp REGEXP 'CASH_IN'))
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    ((l.api_name_ewp IN ("reversetransaction") and l.request_ewp REGEXP 'CASH_IN'))
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "cashout" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("cashout")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    and contexto <> ''
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("cashout")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    and l.contexto <> ''
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "reversetransaction_cashout" : '''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    AND ((api_name_ewp IN ("reversetransaction") and request_ewp REGEXP 'CASH_OUT'))
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    ((l.api_name_ewp IN ("reversetransaction") and l.request_ewp REGEXP 'CASH_OUT'))
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
                ''',
    "payment":'''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("payment")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    and request_ewp REGEXP  '@unique'
                    ORDER BY date_capture_datetime asc
                    LIMIT 10;
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("payment")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    and l.request_ewp REGEXP '@unique'
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
            ''',
    "merchantpayment":'''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("merchantpayment")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    and request_ewp regexp '51938440932'
                    and contexto <> ''
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("merchantpayment")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    and l.contexto <> ''
                    and l.request_ewp regexp '51938440932'
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
            ''',
    "transfer_ahorro":'''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("transfer")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    AND request_ewp REGEXP 'Reversa ahorro compartamos'
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("transfer")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    AND l.request_ewp REGEXP 'Reversa ahorro compartamos'
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
            ''',
    "transfer_credito":'''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("transfer")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    AND request_ewp REGEXP 'Devolucion[0-9]+'
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("transfer")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    AND l.request_ewp REGEXP 'Devolucion[0-9]+'
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
            ''',
    "transfer":'''
                    UPDATE {tabledata}
                    SET status = '{uuid_text}'
                    WHERE status = '' {filtro_idlog}
                    and api_name_ewp in ("transfer")
                    AND status_code_ewp = '200'
                    AND status_code_comviva <> '200'
                    and flg_status_registry = ""
                    AND NOT (request_ewp REGEXP 'Devolucion.*-.*-.*-.*-')
                    AND NOT (request_ewp REGEXP 'Devolucion[0-9]+')
                    AND NOT (request_ewp REGEXP 'Reversa ahorro compartamos')
                    and contexto <> ''
                    ORDER BY date_capture_datetime asc
                    LIMIT {limite};
                    |
                    SELECT 
                    l.id,
                    l.date_capture,
                    l.request_ewp,	
                    l.response_ewp,
                    l.status_code_ewp,
                    
                    l.api_name_ewp,
                    l.date_capture_datetime,
                    l.contexto,
                    l.agente
                    FROM {tabledata} l
                    force INDEX (idx_log_query)
                    WHERE 
                    l.api_name_ewp in ("transfer")
                    AND l.status_code_ewp = '200' {filtro_idlog}
                    AND l.status_code_comviva <> '200'
                    and l.flg_status_registry = ""
                    and l.status = '{uuid_text}'
                    and l.contexto <> ''
                    AND NOT (l.request_ewp REGEXP 'Devolucion.*-.*-.*-.*-')
                    AND NOT (l.request_ewp REGEXP 'Devolucion[0-9]+')
                    AND NOT (l.request_ewp REGEXP 'Reversa ahorro compartamos')
                    ORDER BY l.date_capture_datetime asc
                    LIMIT {limite};
            ''',
    "consulta_user":'''
            SELECT 
            l.id,
            l.date_capture,
            l.request_ewp,	
            l.response_ewp,
            l.status_code_ewp,
            
            l.api_name_ewp,
            l.date_capture_datetime
            FROM {tabledata} l
            force INDEX (idx_log_query)
            WHERE 
            l.date_capture_datetime BETWEEN %s AND %s
            AND l.api_name_ewp in ("getaccountholderaddress")
            AND l.status_code_ewp = '200' {filtro_idlog}
            AND l.status_code_comviva <> '200'
            and l.flg_status_registry = "" and l.status = ""
            ORDER BY l.date_capture_datetime asc
            LIMIT %s
    ''',
    "activation_migrate":'''
            SELECT
                u.id,
                u.fri,
                u.status
            FROM {tabledata} u
            WHERE u.status = "" {filtro_idlog}
            ORDER BY u.id asc
            LIMIT %s
    ''',
    "refund":'''
            UPDATE {tabledata}
            SET status = '{uuid_text}'
            WHERE status = '' {filtro_idlog}
            and api_name_ewp in ("refund")
            AND status_code_ewp = '200'
            AND status_code_comviva <> '200'
            and flg_status_registry = ""
            and contexto <> ''
            ORDER BY date_capture_datetime asc
            LIMIT 10;
            |
            SELECT 
            l.id,
            l.date_capture,
            l.request_ewp,	
            l.response_ewp,
            l.status_code_ewp,
            
            l.api_name_ewp,
            l.date_capture_datetime,
            l.contexto,
            l.agente
            FROM {tabledata} l
            force INDEX (idx_log_query)
            WHERE 
            l.api_name_ewp in ("refund")
            AND l.status_code_ewp = '200' {filtro_idlog}
            AND l.status_code_comviva <> '200'
            and l.flg_status_registry = ""
            and l.status = '{uuid_text}'
            and l.contexto <> ''
            ORDER BY l.date_capture_datetime asc
            LIMIT {limite};
    ''',
    "atmcashout":'''
            UPDATE {tabledata}
            SET status = '{uuid_text}'
            WHERE status = '' {filtro_idlog}
            and api_name_ewp in ("atmcashout")
            AND status_code_ewp = '200'
            AND status_code_comviva <> '200'
            and flg_status_registry = ""
            and contexto <> ''
            ORDER BY date_capture_datetime asc
            LIMIT 10;
            |
            SELECT 
            l.id,
            l.date_capture,
            l.request_ewp,	
            l.response_ewp,
            l.status_code_ewp,
            
            l.api_name_ewp,
            l.date_capture_datetime,
            l.contexto,
            l.agente
            FROM {tabledata} l
            force INDEX (idx_log_query)
            WHERE 
            l.api_name_ewp in ("atmcashout")
            AND l.status_code_ewp = '200' {filtro_idlog}
            AND l.status_code_comviva <> '200'
            and l.flg_status_registry = ""
            and l.status = '{uuid_text}'
            and l.contexto <> ''
            ORDER BY l.date_capture_datetime asc
            LIMIT {limite};
    '''
}

query_select_log ='''
    SELECT * FROM {tabledata} l
    WHERE 
    l.date_capture IS NOT NULL 
    AND l.date_capture <> ''
    AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME(3)) 
        BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME(3)) 
        AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME(3))
    AND l.api_name_ewp in ("getaccountholderinfo","registration")
    AND l.status_code_ewp = '200'
    and ((l.flg_status_registry = '0' or l.flg_status_registry IS NULL or l.flg_status_registry = "") 
    		and (l.status NOT REGEXP 'PROCESADO|ENPROCESO|COLA' or l.status IS NULL or l.status = ""))
    ORDER BY CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME(3)) ASC
    LIMIT %s
'''
#AND (l.api_name_ewp IN ("cashin") OR (l.api_name_ewp IN ("reversetransaction") and l.request_ewp REGEXP 'CASH_IN'))
#    AND l.id in (6078601) correcto getaccountholderinfo
#    AND l.id in (5986803) no correcto pero no existe en uat


#EJECUCION LOGIN
#     SELECT * FROM {tabledata} l
#     WHERE 
#     CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)  AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.api_name_ewp in ("registration","activation","updateaccountholderpersonalinformation")
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     AND l.status_code_ewp = '200'
#     and ((l.flg_status_registry = '0' or l.flg_status_registry IS NULL or l.flg_status_registry = "") 
#     		and (l.status NOT REGEXP 'PROCESADO|ENPROCESO|COLA' or l.status IS NULL or l.status = ""))
#     ORDER BY CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#     LIMIT %s
# '''



#FLUJO CASHIN
#    SELECT * FROM {tabledata} l
#    WHERE 
#    l.date_capture IS NOT NULL 
#    AND l.date_capture <> ''
#    AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME(3)) 
#        BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME(3)) 
#        AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME(3))
#    AND (l.api_name_ewp = "cashin" OR (l.api_name_ewp = "reversetransaction" and l.request_ewp REGEXP 'CASH_IN') or l.api_name_ewp = "getaccountholderinfo" )
#    AND l.status_code_ewp = '200'
#    and ((l.flg_status_registry = '0' or l.flg_status_registry IS NULL or l.flg_status_registry = "") 
#    		and (l.status NOT REGEXP 'PROCESADO|ENPROCESO|COLA' or l.status IS NULL or l.status = ""))
#    ORDER BY CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME(3)) ASC
#    LIMIT %s
#'''










# '''
#     SELECT * FROM Log_26112024 
#     WHERE (flg_status_registry <> '1' OR flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#     BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)  AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND id > %s
#     AND (request_ewp REGEXP 'getaccountholderinfo')
#     AND request_ewp NOT REGEXP 'closeaccountholder'
#     order by id asc, api_name_ewp desc
#     , CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) asc
# LIMIT %s
# '''

#    and id = 435323

#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp in ("updateaccountholderpersonalinformation")
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     and l.request_ewp  REGEXP 'Actualizacion por RENIEC OnLine'
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#     LIMIT %s
# '''














#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp in ("refund","payment")  
# 	and l.status_code_ewp ="200"
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     and l.id in (669577,669540)
#     order by CAST(REPLACE(REPLACE(l.date_capture , 'T', ' '), 'Z', '') AS DATETIME) asc
#     LIMIT %s
# '''       




#reversa merchantpayment 

    #"COMPARTAMOS CREDITOS" : (669565,1454466)
    #"COMPARTAMOS AHORROS" : (668901,669785)
    #"CRANDES":
    #"EXPERIAN PERU S.A.C" : 

#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp in ("merchantpayment","transfer")
# 	and l.status_code_ewp ="200"
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     and l.id in (669565,1454466)
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#     LIMIT %s
# '''







#reversa cashin 
    #kasnet: (7142768,7143186)
    #interop cce : (7142718,7142719)
    #full cargas : (7142831,7142833)
    #niubiz external : (7142832,7142835)
    #compartamos : (7187456,7187458)
    #bn : (7214025,7214027)
#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp in ("reversetransaction","cashin","bnacion_ofi_ci/cashin")  
# 	and l.status_code_ewp ="200"
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     and l.id in (7214025,7214027)
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#     LIMIT %s
# '''       

#reversa cashout
#         SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp in ("reversetransaction","cashout")  
# 	and l.status_code_ewp ="200"
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     and l.id in (485990,485992,485994,485996,485998,486001)
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
    
#     LIMIT %s
# '''       


# reversa payment 
#AZULITO  (669577,669540)
#DIGIFLOW  (680933,653652)
#backus (687216,660423)
#pmpcompras (1346651,1328689)

#airitme (2495316)
#unique  (676241)
#bitel (592869)
#claro (678814)
#sunar (685455)


#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp in ("refund","payment")  
# 	and l.request_ewp REGEXP "lindley"
# 	and l.status_code_ewp ="200"
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     and l.id in (669577,669540)
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
    
#     LIMIT %s
# '''       



# atm cashaout
#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp in ("atmcashout")
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#     LIMIT %s
# '''  


# merchantpayment
#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp in ("merchantpayment")
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#     LIMIT %s
# '''       






    # AND EXISTS (
    #     SELECT 1
    #     FROM Values_Match vm
    #     WHERE l.request_ewp REGEXP CONCAT('FRI:', vm.mdn, '/MSISDN')
    #     and vm.ctr_user IS NOT NULL
    # )



#CASHIN
#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp REGEXP ("cashin|bnacion_ofi_ci/cashin")
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     and l.response_ewp NOT like '%INPUT%'
#     and l.response_ewp NOT like '%OUTPUT%'
#     AND EXISTS (
#         SELECT 1
#         FROM Values_Match vm
#         WHERE l.request_ewp REGEXP CONCAT('FRI:', vm.mdn, '/MSISDN')
#     )
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#     LIMIT %s
# '''

#updateaccountholderpersonalinformation
#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp in ("updateaccountholderpersonalinformation")
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     and l.request_ewp  REGEXP 'Actualizacion por RENIEC OnLine'
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#     LIMIT %s
# '''       

#getaccounts
#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp in ("getaccounts")
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#     LIMIT %s
# '''       

#merchantpayment
#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp in ("merchantpayment")
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     AND l.request_ewp REGEXP CONCAT('\\b', (SELECT GROUP_CONCAT(vm.mdn SEPARATOR '|') 
#                                             FROM Values_Match vm 
#                                             WHERE vm.ctr_user IS NOT NULL), '\\b')
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#     LIMIT %s
# '''       
    



#presentacion
#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp in ("cashout","cashin","transfer")
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     AND l.request_ewp REGEXP CONCAT('\\b', (SELECT GROUP_CONCAT(vm.mdn SEPARATOR '|') 
#                                             FROM Values_Match vm 
#                                             WHERE vm.ctr_user IS NOT NULL), '\\b')
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#     LIMIT %s
# '''       


#CASHIN
#     SELECT * FROM Log_26112024 
#     WHERE (flg_status_registry <> '1' OR flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#     BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)  AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND id > %s
#     and api_name_ewp = "cashin"
#     AND request_ewp NOT REGEXP 'closeaccountholder'
#     and response_ewp NOT REGEXP 'INPUT'
#     and response_ewp NOT REGEXP 'OUTPUT'
#     order by id asc, api_name_ewp desc
#     , CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) asc
#     LIMIT %s
# '''       

#payment
#     SELECT * 
#     FROM Log_26112024 l
#     WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#         AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND l.id > %s
#     AND l.api_name_ewp = "payment"
#     AND l.request_ewp NOT REGEXP 'closeaccountholder'
#     AND l.request_ewp REGEXP CONCAT('\\b', (SELECT GROUP_CONCAT(vm.mdn SEPARATOR '|') 
#                                             FROM Values_Match vm 
#                                             WHERE vm.ctr_user IS NOT NULL), '\\b')
#     ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#     LIMIT %s
# '''       

#     SELECT * FROM Log_26112024 
#     WHERE (flg_status_registry <> '1' OR flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#     BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)  AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND id > %s
#     and api_name_ewp = "transfer"
#     AND request_ewp NOT REGEXP 'closeaccountholder'
#     order by id asc, api_name_ewp desc
#     , CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) asc
# LIMIT %s
# '''


#         SELECT * FROM Log_26112024 
#         WHERE (flg_status_registry <> '1' OR flg_status_registry <> 1)
#         AND CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)  AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#         AND id > %s
#         AND status_code_ewp = "200"
#         AND (request_ewp REGEXP 'registration' or request_ewp REGEXP 'activation')
#         AND request_ewp NOT REGEXP 'closeaccountholder'
#         order by id asc, api_name_ewp desc
#         , CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) asc
#     LIMIT %s
# '''

# SELECT * 
# FROM Log_26112024 l
# WHERE (l.flg_status_registry <> '1' OR l.flg_status_registry <> 1)
#   AND CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#       BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME) 
#       AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#   AND l.id > %s
#   AND l.api_name_ewp = "payment"
#   AND l.request_ewp NOT REGEXP 'closeaccountholder'
#   AND l.request_ewp REGEXP CONCAT('\\b', (SELECT GROUP_CONCAT(vm.mdn SEPARATOR '|') 
#                                           FROM Values_Match vm 
#                                           WHERE vm.ctr_user IS NOT NULL), '\\b')
# ORDER BY l.id ASC, l.api_name_ewp DESC, CAST(REPLACE(REPLACE(l.date_capture, 'T', ' '), 'Z', '') AS DATETIME) ASC
#  LIMIT %s
# '''       





#transfer
#     SELECT * FROM Log_26112024 
#     WHERE (flg_status_registry <> '1' OR flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#     BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)  AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND id > %s
#     and api_name_ewp = "transfer"
#     AND request_ewp NOT REGEXP 'closeaccountholder'
#     order by id asc, api_name_ewp desc
#     , CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) asc
# LIMIT %s
# '''

#getaccountholderidentification
#     SELECT * FROM Log_26112024 
#     WHERE (flg_status_registry <> '1' OR flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#     BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)  AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND id > %s
#     AND id > 460030
#     AND (request_ewp REGEXP 'getaccountholderidentification')
#     AND request_ewp NOT REGEXP 'closeaccountholder'
#     order by id asc, api_name_ewp desc
#     , CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) asc
# LIMIT %s
# '''

#getaccountholderemail
#     SELECT * FROM Log_26112024 
#     WHERE (flg_status_registry <> '1' OR flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#     BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)  AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND id > %s
#     AND id > 435370
#     AND (request_ewp REGEXP 'getaccountholderemail')
#     AND request_ewp NOT REGEXP 'closeaccountholder'
#     order by id asc, api_name_ewp desc
#     , CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) asc
# LIMIT %s
#'''

#getbalance
#     SELECT * FROM Log_26112024 
#     WHERE (flg_status_registry <> '1' OR flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#     BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)  AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND id > %s
#     AND id > 509770
#     AND (request_ewp REGEXP 'getbalance')
#     AND request_ewp NOT REGEXP 'closeaccountholder'
#     order by id asc, api_name_ewp desc
#     , CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) asc
# LIMIT %s
# '''



#         SELECT * FROM Log_26112024 
#         WHERE (flg_status_registry <> '1' OR flg_status_registry <> 1)
#         AND CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#         BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)  AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#         AND id > %s
#         AND status_code_ewp = "200"
#         AND (request_ewp REGEXP 'registration' or request_ewp REGEXP 'activation')
#         AND request_ewp NOT REGEXP 'closeaccountholder'
#         order by id asc, api_name_ewp desc
#         , CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) asc
#     LIMIT %s
# '''

#getaccountholderaddress
#     SELECT * FROM Log_26112024 
#     WHERE (flg_status_registry <> '1' OR flg_status_registry <> 1)
#     AND CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) 
#     BETWEEN CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)  AND CAST(REPLACE(REPLACE(%s, 'T', ' '), 'Z', '') AS DATETIME)
#     AND id > %s
#     AND (request_ewp REGEXP 'getaccountholderaddress')
#     AND request_ewp NOT REGEXP 'closeaccountholder'
#     order by id asc, api_name_ewp desc
#     , CAST(REPLACE(REPLACE(date_capture, 'T', ' '), 'Z', '') AS DATETIME) asc
# LIMIT %s
# '''

query_update_log_comviva = '''
                                update {tabledata}
                              set 
                                flg_status_registry = %s,
                                request_comviva_json = %s,
                                response_comviva_json = %s,
                                status_code_comviva = %s,
                                date_test_execution = %s,
                                is_result_equals = %s,
                                status = %s,
                                time_convert_request = %s,
                                time_execution_apisender = %s,
                                time_compare_response = %s,
                                time_process_apisender = %s
                                where id = %s
                                and flg_status_registry IS NULL
                                and status_code_comviva <> '200'
                                '''
query_update_log_comviva_error = '''
                                update {tabledata}
                              set 
                                flg_status_registry = %s,
                                date_test_execution = %s,
                                status = %s
                                where id = %s
                                and (flg_status_registry IS NULL)
                                '''

query_update_log_time = '''
                        update {tabledata}
                            set 
                            time_execution = %s,
                            time_save_bd = %s
                            where id = %s
                            and (time_save_bd IS NULL or time_save_bd = '')
                        '''


query_insert_result_details ='''
    INSERT INTO Result_compare_log 
        (id_log, id_mapping, parent_id_mapping, index_array_ewp, index_array_mob, 
        clave_ewp, valor_ewp, clave_mob, valor_mob, message_compare, is_result_equals) 
        VALUES (
        %s, 
        %s, 
        %s, 
        %s, 
        %s, 
        %s, 
        %s,
        %s, 
        %s, 
        %s,  
        %s)'''

query_consulta_pin = '''
    SELECT IFNULL(ctr_user,"") as ctr_user FROM {tabledata}
    WHERE mdn = %s
'''

query_update_estado_log = '''
    UPDATE  {tabledata} as l
    SET l.status = %s
	where 
    l.status_code_comviva <> '200'
	and l.id in %s
'''

query_update_estado_log_unit = '''
    UPDATE  {tabledata}
    SET status = %s
	where 
    status_code_comviva <> '200'
	and id = %s
'''

query_insert_error_log ='''
    INSERT INTO Error_log 
        (id_log, timestamp_error, error_type, error_message, stack_trace,id_mapping,clave_ewp)
        VALUES (
        %s, 
        %s, 
        %s, 
        %s, 
        %s, 
        %s, 
        %s
)'''

update_reset_estado_log = '''
    UPDATE {tabledata}
    SET
        status = '' ,
        flg_status_registry = ''
    WHERE status IS NOT NULL
    and status_code_comviva <> '200'
    and id in %s
'''

query_update_estado_users = '''
    UPDATE  {tabledata}
    SET status = %s
	where 
	id in %s
'''


query_update_estado_users_unit = '''
    UPDATE  {tabledata}
    SET status = %s
	where 
	id = %s
'''

plantilla_comviva_dryrun = {
    "1": {
        "getbalance": {
            "api_name": "api_ums_user_wallet_balance",
            "Authorization": "Bearer map_token",
            "data": {
                "currency": "101",
                "openingBalanceReq": "Y",
                "language": "en",
                "user": {
                    "idType": "map_idType",
                    "workspace": "SUBSCRIBER",
                    "idValue": "map_idValue"
                },
                "isChildDataRequired": "N",
                "isDefaultAccountGroupRequired": "Y",
                "isUserAccountDataRequired": "Y",
                "perPage": 5,
                "pageNumber": 1
            }
        }
    },
    "2": {
        "getaccountholderemail": {
            "api_name": "api_ums_user_account_detail_enquiry",
            "Authorization": "Bearer map_token",
            "data": {
                "workspace": "SUBSCRIBER",
                "identifierType": "map_idType",
                "identifierValue": "map_idValue",
                "includes": "accountDetails"
            }
        }
    },
    "3": {
        "gettransactionhistory": {
            "api_name": "api_transaction_history",
            "Authorization": "Bearer map_token",
            "data": {
                "user": {
                    "idType": "",
                    "idValue": ""
                },
                "serviceType": [],
                "status": [
                    "SUCCESS"
                ],
                "offset": 1,
                "order": "ASC",
                "limit": 20
            }
        }
    },
    "4": {
        "getaccountholderidentification": {
            "api_name": "api_ums_user_account_detail_enquiry",
            "Authorization": "Bearer map_token",
            "data": {
                "workspace": "SUBSCRIBER",
                "identifierType": "map_idType",
                "identifierValue": "map_idValue",
                "includes": "accountDetails"
            }
        }
    },
    "5": {
        "registration": {
            "api_name": "api_ums_user_account_creation",
            "Authorization": "Bearer token",
            "data": {
                "source": "MOBILE",
                "registrationType": "ADM_ASSTD_REGISTRATION",
                "userInformation": {
                    "basicInformation": {
                        "loginIdentifiers": [
                            {
                                "type": "KYCID",
                                "value": "a"
                            }
                        ],
                        "paymentHandleIdentifiers": [
                            {
                                "type": "MSISDN",
                                "value": "a"
                            }
                        ],
                        "preferredLanguage": "es",
                        "mobileNumber": "a",
                        "attr1": "entel",
                        "remarks": "CUSTOMER_SELF_REGISTRATION"
                    },
                    "workspaceInformation": {
                        "workspace": "SUBSCRIBER",
                        "categoryName": "Final User",
                        "categoryCode": "SUBS"
                    }
                },
                "kycs": [
                    {
                        "kycIdType": "DNI",
                        "kycIdValue": "a",
                        "kycIdIssueDate": "2019-10-07",
                        "isPrimaryKYCId": "Yes"
                    }
                ],
                "profileDetails": {
                    "authProfile": "SubsDefault",
                    "marketingProfile": "a",
                    "regulatoryProfile": "FULL_KYC",
                    "securityProfile": "SP.23742842818527"
                }
            }
        }
    },
    "6": {
        "getaccountholderpersonalinformation": {
            "api_name": "api_ums_user_account_detail_enquiry",
            "Authorization": "Bearer map_token",
            "data": {
                "workspace": "SUBSCRIBER",
                "identifierType": "map_idType",
                "identifierValue": "map_idValue",
                "includes": "accountDetails,balances"
            }
        }
    },
    "7": {
        "getaccounts": {
            "api_name": "api_ums_user_account_detail_enquiry",
            "Authorization": "Bearer map_token",
            "data": {
                "workspace": "SUBSCRIBER",
                "identifierType": "map_idType",
                "identifierValue": "map_idValue",
                "includes": "accountDetails,balances"
            }
        }
    },
    "8": {
        "getaccountholderinfo": {
            "api_name": "api_ums_user_account_detail_enquiry",
            "Authorization": "Bearer map_token",
            "data": {
                "workspace": "SUBSCRIBER",
                "identifierType": "map_idType",
                "identifierValue": "map_idValue",
                "includes": "accountDetails"
            }
        }
    },
    "9": {
        "getaccountholdersbyidentification": {
            "api_name": "api_ums_user_account_detail_enquiry",
            "Authorization": "Bearer map_token",
            "data": {
                "workspace": "SUBSCRIBER",
                "identifierType": "map_idType",
                "identifierValue": "map_idValue",
                "includes": "accountDetails,balances"
            }
        }
    },
    "17": {
        "activation": {
            "api_name": "api_ums_user_change_authentication",
            "data": {
                "requestedBy": "SELF",
                "authFactor": "PIN",
                "workspace": "SUBSCRIBER",
                "identifierType": "MSISDN",
                "identifierValue": "a",
                "newAuthenticationValue": "929292",
                "confirmedAuthenticationValue": "929292",
                "oldAuthenticationValue": "000000"
            },
            "Authorization": "Bearer token"
        }
    },
    "29": {
        "initiatepinreset": {
            "api_name": "api_ums_user_change_authentication_using_2fa",
            "Authorization": "Bearer token",
            "data": {
                "workspace": "SUBSCRIBER",
                "identifierType": "",
                "identifierValue": " ",
                "language": "en",
                "authFactor": "PIN"
            }
        }
    },
    "11": {
        "setemail": {
            "api_name": "api_ums_user_account_modification",
            "Authorization": "Bearer token",
            "data": {
                "source": "MOBILE",
                "userId": "US.5989118439713558",
                "initiationMode": "SELF_MODIFICATION",
                "userInformation": {
                    "basicInformation": {
                        "emailId": "apfatanelson@gmail.com",
                        "preferredLanguage": "en",
                        "remarks": "Actualización de email mediante perfil"
                    },
                    "workspaceInformation": {
                        "categoryName": "Final User",
                        "categoryCode": "SUBS"
                    }
                },
                "profileDetails": {
                    "regulatoryProfile": "FULL_KYC"
                }
            }
        }
    },
    "14": {
        "updateaccountholderaddress": {
            "api_name": "api_ums_user_account_modification",
            "Authorization": "Bearer token",
            "data": {
                "source": "",
                "userId": "",
                "initiationMode": "ASSTD_MODIFICATION",
                "userInformation": {
                    "basicInformation": {
                        "preferredLanguage": "en",
                        "state": "",
                        "city": "",
                        "district": "",
                        "address1": "",
                        "remarks": "Actualizacion de direccion"
                    },
                    "workspaceInformation": {
                        "workspace": "SUBSCRIBER",
                        "categoryName": "Final User",
                        "categoryCode": "SUBS"
                    }
                },
                "profileDetails": {
                    "regulatoryProfile": "FULL_KYC"
                }
            }
        }
    },
    "25": {
        "closeaccount": {
            "api_name": "api_ums_user_deletion_self",
            "data": {
                "remarks": "CIERRE POR APP BIM"
            },
            "Authorization": "Bearer token"
        }
    },
    "10": {
        "setaccountprofile": {
            "api_name": "api_ums_user_account_modification",
            "Authorization": "Bearer ",
            "data": {
                "source": "MOBILE",
                "userId": "US.5989118439713558",
                "initiationMode": "SELF_MODIFICATION",
                "userInformation": {
                    "basicInformation": {
                        "remarks": "Cambio cuenta simplificada a general"
                    },
                    "workspaceInformation": {
                        "workspace": "SUBSCRIBER",
                        "categoryName": "Final User",
                        "categoryCode": "SUBS"
                    }
                },
                "profileDetails": {
                    "authProfile": "SubsDefault",
                    "marketingProfile": "MKPFGFCOMP02",
                    "regulatoryProfile": "FULL_KYC",
                    "securityProfile": "SP.23742842818527"
                }
            }
        }
    },
    "13": {
        "setmsisdn": {
            "api_name": "api_ums_user_account_modification",
            "data": {
                "source": "MOBILE",
                "userId": "US.7251241497531698",
                "initiationMode": "ASSTD_MODIFICATION",
                "userInformation": {
                    "basicInformation": {
                        "mobileNumber": "51958411491",
                        "attr1": "claro",
                        "remarks": "Cambio de numero OnLine"
                    },
                    "workspaceInformation": {
                        "workspace": "SUBSCRIBER",
                        "categoryCode": "SUBS"
                    }
                },
                "profileDetails": {
                    "regulatoryProfile": "FULL_KYC"
                }
            },
            "Authorization": "Bearer token"
        }
    },
    "12": {
        "sethomechargingregion": {
            "api_name": "api_ums_user_account_modification",
            "data": {
                "source": "MOBILE",
                "userId": "US.7251241497531698",
                "initiationMode": "ASSTD_MODIFICATION",
                "userInformation": {
                    "basicInformation": {
                        "mobileNumber": "51958411491",
                        "attr1": "bitel",
                        "remarks": "Cambio de numero OnLine"
                    },
                    "workspaceInformation": {
                        "workspace": "SUBSCRIBER",
                        "categoryCode": "SUBS"
                    }
                },
                "profileDetails": {
                    "regulatoryProfile": "FULL_KYC"
                }
            },
            "Authorization": "Bearer token"
        }
    },
    "36": {
        "updatecredential": {
            "api_name": "api_ums_user_change_authentication",
            "data": {
                "requestedBy": "SELF",
                "authFactor": "PIN",
                "workspace": "SUBSCRIBER",
                "identifierType": "MSISDN",
                "identifierValue": "51989331240",
                "newAuthenticationValue": "202501",
                "confirmedAuthenticationValue": "202501",
                "oldAuthenticationValue": "190622"
            },
            "Authorization": "Bearer token"
        }
    },
    "40": {
        "setprofile": {
            "api_name": "api_ums_user_update_issuer",
            "Authorization": "Bearer token",
            "data": {
                "source": "MOBILE",
                "userId": "US.7251241497531698",
                "initiationMode": "SELF_MODIFICATION",
                "userInformation": {
                    "basicInformation": {
                        "accountGroupName": "Personal",
                        "preferredLanguage": "en"
                    },
                    "workspaceInformation": {
                        "workspace": "SUBSCRIBER",
                        "categoryName": "Final User",
                        "categoryCode": "SUBS"
                    }
                },
                "profileDetails": {
                    "authProfile": "SubsDefault",
                    "marketingProfile": "MKPFSQAPAQ04",
                    "regulatoryProfile": "FULL_KYC",
                    "securityProfile": "SP.23742842818527"
                }
            }
        }
    },
    "16": {
        "updateaccountholderpersonalinformation": {
            "api_name": "api_ums_user_account_modification",
            "data": {
                "source": "MOBILE",
                "userId": "",
                "initiationMode": "ASSTD_MODIFICATION",
                "userInformation": {
                    "basicInformation": {
                        "firstName": "",
                        "lastName": "",
                        "dateOfBirth": "",
                        "attr2": "",
                        "attr3": "",
                        "attr4": "",
                        "remarks": ""
                    },
                    "workspaceInformation": {
                        "workspace": "SUBSCRIBER",
                        "categoryCode": "SUBS"
                    }
                },
                "profileDetails": {
                    "regulatoryProfile": "FULL_KYC"
                }
            },
            "Authorization": "Beare****"
        }
    },
    "15": {
        "updateaccountholderidentification": {
            "api_name": "api_ums_user_account_modification",
            "Authorization": "Bearer",
            "data": {
                "source": "MOBILE",
                "userId": "US.1294181365345023",
                "initiationMode": "SELF_MODIFICATION",
                "userInformation": {
                    "basicInformation": {
                        "remarks": "Actualizacion desde Perfil WU"
                    },
                    "employmentDetail": {},
                    "workspaceInformation": {
                        "categoryCode": "SUBS"
                    }
                },
                "profileDetails": {
                    "regulatoryProfile": "FULL_KYC"
                },
                "kycs": [
                    {
                        "kycIdValue": "70342970",
                        "kycIdType": "DNI",
                        "kycIdIssueDate": "2022-11-22",
                        "kycIdValidFrom": "2022-11-22",
                        "kycIdValidTo": "2030-11-22",
                        "isPrimaryKYCId": "Yes",
                        "action": "UPDATE"
                    }
                ]
            }
        }
    },
    "27": {
        "getapprovals": {
            "api_name": "api_transaction_history",
            "Authorization": "Beare****",
            "data": {
                "user": {
                    "idValue": "51906305831",
                    "idType": "mobileNumber"
                },
                "status": [
                    "PENDING"
                ],
                "serviceType": [
                    "CASHOUT"
                ],
                "order": "DESC"
            }
        }
    },
    "32": {
        "payment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Bearer ",
            "data": {
                "transactionAmount": "",
                "currency": 101,
                "language": "en",
                "remarks": "",
                "sender": {
                    "idType": "mobileNumber",
                    "idValue": "",
                    "workspace": "SUBSCRIBER",
                    "accountGroupId": "",
                    "productId": 12
                },
                "receiver": {
                    "idType": "userCode",
                    "idValue": "wu"
                },
                "notificationUrl": "",
                "partnerData": {
                    "sendernote": "",
                    "trxid": "",
                    "receivermessage": "",
                    "destinoOriginal": "",
                    "codigoPago": ""
                },
                "extensibleFields": {
                    "source": "wu",
                    "field1": "wu",
                    "field2": "",
                    "field3": "0.0"
                }
            }
        }
    },
    "50": {
        "payment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Bearer ",
            "data": {
                "transactionAmount": "",
                "currency": 101,
                "language": "en",
                "remarks": "",
                "sender": {
                    "idType": "mobileNumber",
                    "idValue": "",
                    "workspace": "SUBSCRIBER",
                    "accountGroupId": "",
                    "productId": 12
                },
                "receiver": {
                    "idType": "loginId",
                    "idValue": "unique"
                },
                "notificationUrl": "",
                "partnerData": {
                    "codConsultora": "",
                    "nomConsultora": "",
                    "numDocumento": "",
                    "tipoDocumento": "1"
                },
                "extensibleFields": {
                    "source": "http-xml_awspdp",
                    "field1": "YANBAL",
                    "field2": ""
                }
            }
        }
    },
    "48": {
        "payment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Beare****",
            "data": {
                "transactionAmount": "3.00",
                "currency": 101,
                "language": "en",
                "remarks": "988945761",
                "sender": {
                    "idType": "mobileNumber",
                    "idValue": "51957135445",
                    "workspace": "SUBSCRIBER",
                    "accountGroupId": "",
                    "productId": 12
                },
                "receiver": {
                    "idType": "loginId",
                    "idValue": "a"
                },
                "notificationUrl": "",
                "partnerData": {
                    "receivermessage": "988945761",
                    "sendernote": "988945761",
                    "codigoPago": "988945761"
                },
                "extensibleFields": {
                    "source": "http-xml_awspdp",
                    "field1": "azulito",
                    "field2": "azulito"
                }
            }
        }
    },
    "49": {
        "payment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Beare****",
            "data": {
                "transactionAmount": "",
                "currency": 101,
                "language": "en",
                "remarks": "Pago postpago por  soles",
                "sender": {
                    "idType": "mobileNumber",
                    "idValue": "",
                    "workspace": "SUBSCRIBER",
                    "accountGroupId": "",
                    "productId": 12
                },
                "receiver": {
                    "idType": "loginId",
                    "idValue": "bitel"
                },
                "notificationUrl": "",
                "partnerData": {
                    "company": "Bitel",
                    "amount": "",
                    "codigoPago": ""
                },
                "extensibleFields": {
                    "source": "http-xml_awspdp",
                    "field1": "Bitel"
                }
            }
        }
    },
    "51": {
        "payment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Beare****",
            "data": {
                "transactionAmount": "",
                "currency": 101,
                "language": "en",
                "remarks": "",
                "sender": {
                    "idType": "mobileNumber",
                    "idValue": "",
                    "workspace": "SUBSCRIBER",
                    "accountGroupId": "",
                    "productId": 12
                },
                "receiver": {
                    "idType": "userCode",
                    "idValue": "digiflow"
                },
                "notificationUrl": "",
                "partnerData": {},
                "extensibleFields": {
                    "source": "GENERIC",
                    "field0": "Claro"
                }
            }
        }
    },
    "52": {
        "payment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "****",
            "data": {
                "transactionAmount": "",
                "currency": 101,
                "language": "en",
                "remarks": "",
                "sender": {
                    "idType": "mobileNumber",
                    "idValue": "",
                    "workspace": "SUBSCRIBER",
                    "accountGroupId": "",
                    "productId": 12
                },
                "receiver": {
                    "idType": "loginId",
                    "idValue": "sunat"
                },
                "notificationUrl": "",
                "partnerData": {
                    "sendernote": "",
                    "receivermessage": ""
                },
                "extensibleFields": {
                    "source": "a",
                    "field1": "SUNAT-RUS"
                }
            }
        }
    },
    "53": {
        "payment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Bearer ",
            "data": {
                "transactionAmount": "14.50",
                "currency": 101,
                "language": "en",
                "remarks": "77520228_Electro Puno",
                "sender": {
                    "idType": "mobileNumber",
                    "idValue": "51906305831",
                    "workspace": "SUBSCRIBER",
                    "accountGroupId": "",
                    "productId": 12
                },
                "receiver": {
                    "idType": "userCode",
                    "idValue": "gmoney"
                },
                "notificationUrl": "",
                "partnerData": {
                    "idTransaccion": "4110545422127",
                    "trxid": "4110545422127",
                    "paramValor": "11223344"
                },
                "extensibleFields": {
                    "source": "GENERIC",
                    "field0": "Electro Puno",
                    "field1": "0.0"
                }
            }
        }
    },
    "54": {
        "payment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Bearer token",
            "data": {
                "transactionAmount": "5",
                "remarks": "",
                "sender": {
                    "workspace": "SUBSCRIBER",
                    "idValue": "",
                    "idType": "mobileNumber",
                    "productId": 12
                },
                "receiver": {
                    "idValue": "",
                    "idType": "loginId",
                    "productId": 12
                },
                "extensibleFields": {
                    "source": "a",
                    "field0": "a"
                },
                "currency": 101,
                "language": "es",
                "initiator": "sender",
                "externalReferenceId": ""
            }
        }
    },
    "19": {
        "cashin": {
            "api_name": "api_transaction_cashin",
            "Authorization": "Bearer",
            "data": {
                "x_channel": "MOBILE",
                "body": {
                    "initiator": "transactor",
                    "transactionAmount": "",
                    "currency": 101,
                    "language": "en",
                    "remarks": "Cashin",
                    "externalReferenceId": "",
                    "receiver": {
                        "idType": "mobileNumber",
                        "idValue": "",
                        "productId": 12,
                        "workspace": "SUBSCRIBER"
                    },
                    "transactor": {
                        "idType": "mobileNumber",
                        "idValue": "",
                        "productId": 12,
                        "workspace": "BUSINESS"
                    },
                    "partnerData": {
                        "sendernote": "",
                        "receivermessage": ""
                    },
                    "extensibleFields": {
                        "source": "",
                        "field4": "INTEROP_NIUBIZ",
                        "field9": "",
                        "field10": ""
                    }
                }
            }
        }
    },
    "22": {
        "merchantpayment/quote": {
            "api_name": "api_transaction_get_fee",
            "Authorization": "Bearer",
            "data": {
                "x_channel": "MOBILE",
                "body": {
                    "requestedServiceCode": "BILLPAY",
                    "transactionAmount": "17.70",
                    "initiator": "sender",
                    "currency": 101,
                    "language": "es",
                    "sender": {
                        "workspace": "SUBSCRIBER",
                        "idType": "mobileNumber",
                        "idValue": "51902195929"
                    },
                    "receiver": {
                        "workspace": "BUSINESS",
                        "idType": "userCode",
                        "idValue": "wu"
                    },
                    "partnerData": {
                        "origin": "51902195929"
                    }
                }
            }
        }
    },
    "65": {
        "payment/quote": {
            "api_name": "api_transaction_get_fee",
            "Authorization": "Bearer ---",
            "data": {
                "body": {
                    "remarks": "51902195929",
                    "transactionAmount": "10",
                    "sender": {
                        "idValue": "51902195929",
                        "idType": "mobileNumber"
                    },
                    "receiver": {
                        "idValue": "airtimebitel",
                        "idType": "userCode"
                    },
                    "requestedServiceCode": "BILLPAY",
                    "initiator": "sender",
                    "currency": 101
                },
                "x_channel": "MOBILE"
            }
        }
    },
    "61": {
        "payment/quote": {
            "api_name": "api_transaction_get_fee",
            "Authorization": "Bearer ",
            "data": {
                "x_channel": "MOBILE",
                "body": {
                    "requestedServiceCode": "BILLPAY",
                    "transactionAmount": "39.90",
                    "initiator": "sender",
                    "currency": 101,
                    "language": "es",
                    "sender": {
                        "workspace": "SUBSCRIBER",
                        "idType": "mobileNumber",
                        "idValue": "51902195929"
                    },
                    "receiver": {
                        "workspace": "BUSINESS",
                        "idType": "userCode",
                        "idValue": "bitel"
                    },
                    "partnerData": {
                        "origin": "51902195929"
                    }
                }
            }
        }
    },
    "62": {
        "payment/quote": {
            "api_name": "api_transaction_get_fee",
            "Authorization": "Bearer ---",
            "data": {
                "x_channel": "MOBILE",
                "body": {
                    "requestedServiceCode": "BILLPAY",
                    "transactionAmount": "1.0",
                    "initiator": "sender",
                    "currency": 101,
                    "language": "es",
                    "sender": {
                        "workspace": "SUBSCRIBER",
                        "idType": "mobileNumber",
                        "idValue": "51902195929"
                    },
                    "receiver": {
                        "workspace": "BUSINESS",
                        "idType": "userCode",
                        "idValue": "unique"
                    },
                    "partnerData": {
                        "origin": "51902195929"
                    }
                }
            }
        }
    },
    "63": {
        "payment/quote": {
            "api_name": "api_transaction_get_fee",
            "Authorization": "Bearer ",
            "data": {
                "x_channel": "MOBILE",
                "body": {
                    "requestedServiceCode": "BILLPAY",
                    "transactionAmount": "3.02",
                    "initiator": "sender",
                    "currency": 101,
                    "language": "es",
                    "sender": {
                        "workspace": "SUBSCRIBER",
                        "idType": "mobileNumber",
                        "idValue": "51902195929"
                    },
                    "receiver": {
                        "workspace": "BUSINESS",
                        "idType": "userCode",
                        "idValue": "claro"
                    },
                    "partnerData": {
                        "origin": "51902195929"
                    }
                }
            }
        }
    },
    "64": {
        "payment/quote": {
            "api_name": "api_transaction_get_fee",
            "Authorization": "****",
            "data": {
                "x_channel": "MOBILE",
                "body": {
                    "requestedServiceCode": "BILLPAY",
                    "transactionAmount": "1.0",
                    "currency": 101,
                    "language": "en",
                    "remarks": "payment quote RUS str(ruc)='10212875541'",
                    "initiator": "sender",
                    "sender": {
                        "idType": "mobileNumber",
                        "idValue": "51902195929",
                        "workspace": "SUBSCRIBER",
                        "productId": 12
                    },
                    "receiver": {
                        "idType": "userCode",
                        "idValue": "sunat",
                        "productId": 12
                    },
                    "notificationUrl": "",
                    "partnerData": {}
                }
            }
        }
    },
    "20": {
        "cashout": {
            "api_name": "api_transaction_cashout",
            "Authorization": "Bearer",
            "data": {
                "transactionAmount": "1.00",
                "initiator": "withdrawer",
                "currency": 101,
                "language": "en",
                "externalReferenceId": "1",
                "remarks": "Interoperabilidad",
                "transactor": {
                    "idType": "mobileNumber",
                    "idValue": "51963897000",
                    "productId": 12,
                    "workspace": "BUSINESS"
                },
                "withdrawer": {
                    "idType": "mobileNumber",
                    "idValue": "",
                    "productId": 12,
                    "workspace": "SUBSCRIBER"
                },
                "notificationUrl": "",
                "partnerData": {
                    "refid": "PDP20241107145301"
                },
                "extensibleFields": {
                    "source": "http-fcompartamos_niubiz_interope",
                    "field4": "INTEROP_NIUBIZ"
                }
            }
        }
    },
    "34": {
        "transfer": {
            "api_name": "api_transaction_p2p",
            "Authorization": "Bearer ***",
            "data": {
                "transactionAmount": "",
                "initiator": "sender",
                "currency": 101,
                "language": "es",
                "remarks": "",
                "sender": {
                    "idType": "mobileNumber",
                    "idValue": "",
                    "productId": 12
                },
                "receiver": {
                    "idType": "mobileNumber",
                    "idValue": "",
                    "productId": 12
                },
                "partnerData": {
                    "sendernote": "",
                    "receivermessage": ""
                },
                "extensibleFields": {
                    "source": "a"
                }
            }
        }
    },
    "68": {
        "getbalance": {
            "api_name": "api_ums_user_wallet_balance",
            "Authorization": "Bearer map_token",
            "data": {
                "currency": "101",
                "openingBalanceReq": "Y",
                "language": "en",
                "user": {
                    "idType": "MSISDN",
                    "workspace": "SUBSCRIBER",
                    "idValue": "map_idValue"
                },
                "isChildDataRequired": "N",
                "isDefaultAccountGroupRequired": "Y",
                "isUserAccountDataRequired": "Y",
                "perPage": 5,
                "pageNumber": 1
            }
        }
    },
    "66": {
        "getaccountholderaddress": {
            "api_name": "api_ums_user_account_detail_enquiry",
            "Authorization": "Bearer map_token",
            "data": {
                "workspace": "SUBSCRIBER",
                "identifierType": "map_idType",
                "identifierValue": "map_idValue",
                "includes": "accountDetails"
            }
        }
    },
    "55": {
        "cashin": {
            "api_name": "api_transaction_cashin",
            "Authorization": "Bearer ***",
            "data": {
                "body": {
                    "transactionAmount": "",
                    "initiator": "transactor",
                    "currency": 101,
                    "language": "es",
                    "externalReferenceId": "",
                    "remarks": "transction",
                    "transactor": {
                        "idType": "mobileNumber",
                        "idValue": "51963564251",
                        "workspace": "BUSINESS"
                    },
                    "receiver": {
                        "idType": "mobileNumber",
                        "idValue": "",
                        "workspace": "SUBSCRIBER"
                    },
                    "partnerData": {
                        "sendernote": "",
                        "receivermessage": ""
                    },
                    "extensibleFields": {
                        "source": "http-fcompartamos_cce_interope"
                    }
                },
                "x_channel": "MOBILE"
            }
        }
    },
    "56": {
        "bnacion_ofi_ci/cashin": {
            "api_name": "api_transaction_cashin",
            "Authorization": "Bearer ",
            "data": {
                "body": {
                    "receiver": {
                        "idValue": "",
                        "idType": "mobileNumber"
                    },
                    "transactor": {
                        "idValue": "51977208888",
                        "idType": "mobileNumber"
                    },
                    "extensibleFields": {
                        "source": "bnacion_ofi_ci"
                    },
                    "initiator": "transactor",
                    "transactionAmount": "",
                    "currency": 101,
                    "externalReferenceId": ""
                },
                "x_channel": "MOBILE"
            }
        }
    },
    "57": {
        "cashin": {
            "api_name": "api_transaction_cashin",
            "Authorization": "token",
            "data": {
                "body": {
                    "receiver": {
                        "idValue": "",
                        "idType": "mobileNumber",
                        "workspace": "SUBSCRIBER"
                    },
                    "transactor": {
                        "idValue": "51938948480",
                        "idType": "mobileNumber",
                        "workspace": "BUSINESS"
                    },
                    "extensibleFields": {
                        "source": "http-fcompartamos_app"
                    },
                    "initiator": "transactor",
                    "transactionAmount": "",
                    "currency": 101,
                    "externalReferenceId": ""
                },
                "x_channel": "AGENTE"
            }
        }
    },
    "58": {
        "cashin": {
            "api_name": "api_transaction_cashin",
            "Authorization": "Bearer --",
            "data": {
                "body": {
                    "receiver": {
                        "idValue": "",
                        "idType": "mobileNumber",
                        "workspace": "SUBSCRIBER"
                    },
                    "transactor": {
                        "idValue": "51989294475",
                        "idType": "mobileNumber",
                        "workspace": "BUSINESS"
                    },
                    "extensibleFields": {
                        "source": "http-ci_kasnet_partner"
                    },
                    "initiator": "transactor",
                    "transactionAmount": "",
                    "currency": 101,
                    "externalReferenceId": ""
                },
                "x_channel": "AGENTE"
            }
        }
    },
    "33": {
        "refund": {
            "api_name": "api_transaction_order_cancel",
            "Authorization": "Be****",
            "data": {
                "originalTransactionId": "",
                "transactor": {
                    "idType": "loginId",
                    "idValue": "NetworkTest0509"
                },
                "externalReferenceId": "",
                "isServiceChargeReversible": True,
                "isCommissionReversible": True,
                "isTCPCheckRequired": True,
                "remarks": "",
                "partnerData": {
                    "receivermessage": "",
                    "sendernote": "",
                    "codigoPago": ""
                },
                "extensibleFields": {
                    "source": "http-awspdp",
                    "field1": "azulito",
                    "field2": "azulito"
                }
            }
        }
    },
    "69": {
        "refund": {
            "api_name": "api_transaction_order_cancel",
            "Authorization": "Bearer ",
            "data": {
                "originalTransactionId": "",
                "transactor": {
                    "idType": "loginId",
                    "idValue": "NetworkTest0509"
                },
                "externalReferenceId": "",
                "isServiceChargeReversible": True,
                "isCommissionReversible": True,
                "isTCPCheckRequired": True,
                "remarks": "",
                "partnerData": {},
                "extensibleFields": {
                    "source": "http-xml_awspdp",
                    "field1": "wu",
                    "field2": ""
                }
            }
        }
    },
    "59": {
        "atmcashout": {
            "api_name": "api_transaction_atm_cashout",
            "Authorization": "Beare****",
            "data": {
                "body": {
                    "sender": {
                        "idValue": "",
                        "idType": "mobileNumber"
                    },
                    "receiver": {
                        "idValue": "51987987005",
                        "idType": "mobileNumber"
                    },
                    "passcode": "",
                    "extensibleFields": {
                        "source": "fcompartamos_atm"
                    },
                    "transactionAmount": "",
                    "currency": 0,
                    "externalReferenceId": ""
                },
                "x_channel": "ATM"
            }
        }
    },
    "31": {
        "merchantpayment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Bearer ++",
            "data": {
                "transactionAmount": "",
                "currency": 101,
                "initiator": "sender",
                "externalReferenceId": "",
                "remarks": "",
                "sender": {
                    "workspace": "SUBSCRIBER",
                    "idType": "mobileNumber",
                    "idValue": "",
                    "accountGroupId": "",
                    "productId": 12
                },
                "receiver": {
                    "workspace": "BUSINESS",
                    "idType": "mobileNumber",
                    "idValue": "",
                    "productId": 12
                },
                "partnerData": {
                    "codigoPago": "",
                    "sendernote": "a",
                    "receivermessage": "a"
                },
                "extensibleFields": {
                    "field2": "",
                    "source": "http-xml_awspdp",
                    "field1": "a",
                    "field9": "a",
                    "field10": "a"
                }
            }
        }
    },
    "70": {
        "updateaccountholderpersonalinformation": {
            "api_name": "api_ums_user_account_modification",
            "Authorization": "Beare****",
            "data": {
                "source": "MOBILE",
                "userId": "",
                "initiationMode": "ASSTD_MODIFICATION",
                "userInformation": {
                    "basicInformation": {
                        "preferredLanguage": "es",
                        "firstName": "",
                        "dateOfBirth": "",
                        "nationality": "",
                        "attr2": "",
                        "remarks": "",
                        "country": "",
                        "lastName": ""
                    },
                    "employmentDetail": {
                        "occupation": ""
                    },
                    "workspaceInformation": {
                        "categoryCode": "SUBS"
                    }
                },
                "profileDetails": {
                    "regulatoryProfile": "FULL_KYC"
                }
            }
        }
    },
    "71": {
        "updateaccountholderpersonalinformation": {
            "api_name": "api_ums_user_account_modification",
            "Authorization": "Beare****",
            "data": {
                "source": "MOBILE",
                "userId": "",
                "initiationMode": "ASSTD_MODIFICATION",
                "userInformation": {
                    "basicInformation": {
                        "preferredLanguage": "es",
                        "firstName": "",
                        "lastName": "",
                        "remarks": ""
                    },
                    "workspaceInformation": {
                        "categoryCode": "SUBS"
                    }
                },
                "profileDetails": {
                    "regulatoryProfile": "FULL_KYC"
                }
            }
        }
    },
    "72": {
        "updateaccountholderpersonalinformation": {
            "api_name": "api_ums_user_account_modification",
            "Authorization": "Beare****",
            "data": {
                "source": "MOBILE",
                "userId": "",
                "initiationMode": "ASSTD_MODIFICATION",
                "userInformation": {
                    "basicInformation": {
                        "preferredLanguage": "es",
                        "firstName": "",
                        "lastName": "",
                        "remarks": ""
                    },
                    "workspaceInformation": {
                        "categoryCode": "SUBS"
                    }
                },
                "profileDetails": {
                    "regulatoryProfile": "FULL_KYC"
                }
            }
        }
    },
    "74": {
        "atmcashout": {
            "api_name": "api_transaction_atm_cashout",
            "Authorization": "Bearer token",
            "data": {
                "body": {
                    "sender": {
                        "idValue": "",
                        "idType": "mobileNumber"
                    },
                    "receiver": {
                        "idValue": "51987987005",
                        "idType": "mobileNumber"
                    },
                    "passcode": "",
                    "extensibleFields": {
                        "source": "fcompartamos_fullcarga"
                    },
                    "transactionAmount": "",
                    "currency": 101,
                    "externalReferenceId": ""
                },
                "x_channel": "AGENTE"
            }
        }
    },
    "76": {
        "refund": {
            "api_name": "api_transaction_order_cancel",
            "Authorization": "Beare****",
            "data": {
                "originalTransactionId": "",
                "transactor": {
                    "idType": "loginId",
                    "idValue": "NetworkTest0509"
                },
                "externalReferenceId": "",
                "isServiceChargeReversible": True,
                "isCommissionReversible": True,
                "isTCPCheckRequired": True,
                "remarks": "",
                "partnerData": {
                    "receivermessage": "",
                    "sendernote": "",
                    "codigoPago": "",
                    "xLwacExecuteAs": "ID-pmpcompras-USER"
                },
                "extensibleFields": {
                    "source": "http-xml_awspdp",
                    "field1": "wu",
                    "field2": "IZIPAY"
                }
            }
        }
    },
    "75": {
        "refund": {
            "api_name": "api_transaction_order_cancel",
            "Authorization": "Beare****",
            "data": {
                "originalTransactionId": "",
                "transactor": {
                    "idType": "loginId",
                    "idValue": "NetworkTest0509"
                },
                "externalReferenceId": "",
                "isServiceChargeReversible": True,
                "isCommissionReversible": True,
                "isTCPCheckRequired": True,
                "remarks": "",
                "partnerData": {
                    "receivermessage": "",
                    "sendernote": "",
                    "codigoPago": "",
                    "xLwacExecuteAs": "ID-backus-USER"
                },
                "extensibleFields": {
                    "source": "http-xml_awspdp",
                    "field1": "niubizpagosqr",
                    "field2": "NIUBIZ"
                }
            }
        }
    },
    "67": {
        "payment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Beare****",
            "data": {
                "transactionAmount": "",
                "currency": 101,
                "language": "en",
                "remarks": "Pago IZIPAY ",
                "sender": {
                    "idType": "mobileNumber",
                    "idValue": "",
                    "workspace": "SUBSCRIBER",
                    "accountGroupId": "",
                    "productId": 12
                },
                "receiver": {
                    "idType": "userCode",
                    "idValue": "niubizpagosqr"
                },
                "notificationUrl": "",
                "partnerData": {
                    "receivermessage": "",
                    "sendernote": "",
                    "codigoPago": "",
                    "idPDP": ""
                },
                "extensibleFields": {
                    "source": "GENERIC",
                    "field1": "niubizpagosqr",
                    "field2": "NIUBIZ"
                }
            }
        }
    },
    "77": {
        "payment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Beare****",
            "data": {
                "transactionAmount": "",
                "currency": 101,
                "language": "en",
                "remarks": "Pago IZIPAY",
                "sender": {
                    "idType": "mobileNumber",
                    "idValue": "",
                    "workspace": "SUBSCRIBER",
                    "accountGroupId": "",
                    "productId": 12
                },
                "receiver": {
                    "idType": "userCode",
                    "idValue": "izipaypagoqr"
                },
                "notificationUrl": "",
                "partnerData": {
                    "receivermessage": "",
                    "sendernote": "",
                    "codigoPago": "",
                    "idPDP": ""
                },
                "extensibleFields": {
                    "source": "GENERIC",
                    "field1": "izipaypagoqr",
                    "field2": "IZIPAY Compras"
                }
            }
        }
    },
    "37": {
        "reversetransaction": {
            "api_name": "api_transaction_reverse",
            "Authorization": "Beare****",
            "data": {
                "x_channel": "MOBILE",
                "body": {
                    "bearerCode": "MOBILE",
                    "originalTransactionId": "0",
                    "transactor": {
                        "idType": "loginId",
                        "idValue": "NetworkTest0509"
                    },
                    "externalReferenceId": "",
                    "isServiceChargeReversible": True,
                    "isCommissionReversible": True,
                    "isTCPCheckRequired": False,
                    "remarks": "Interoperabilidad reversal",
                    "partnerData": {
                        "comment": ""
                    },
                    "extensibleFields": {
                        "source": "http-fcompartamos_niubiz_interope",
                        "comment": ""
                    }
                }
            }
        }
    },
    "73": {
        "reversetransaction": {
            "api_name": "api_transaction_reverse",
            "Authorization": "",
            "data": {
                "x_channel": "MOBILE",
                "body": {
                    "bearerCode": "MOBILE",
                    "originalTransactionId": "0",
                    "transactor": {
                        "idType": "mobileNumber",
                        "idValue": "51991022660",
                        "workspace": "BUSINESS",
                        "productId": 12
                    },
                    "externalReferenceId": "",
                    "isServiceChargeReversible": True,
                    "isCommissionReversible": True,
                    "isTCPCheckRequired": False,
                    "remarks": "Reversa cashin",
                    "partnerData": {},
                    "extensibleFields": {
                        "source": "http-fcompartamos_niubiz_interope"
                    }
                }
            }
        }
    },
    "78": {
        "transfer": {
            "api_name": "api_transaction_order_cancel",
            "Authorization": "Bearer --",
            "data": {
                "originalTransactionId": "",
                "transactor": {
                    "idType": "loginId",
                    "idValue": "NetworkTest0509"
                },
                "isServiceChargeReversible": True,
                "isCommissionReversible": True,
                "isTCPCheckRequired": True,
                "remarks": "",
                "extensibleFields": {
                    "source": "http-awspdp"
                }
            }
        }
    },
    "79": {
        "getbalancedelete": {
            "api_name": "api_ums_user_wallet_balance",
            "Authorization": "Bearer map_token",
            "data": {
                "currency": "101",
                "openingBalanceReq": "Y",
                "language": "en",
                "user": {
                    "idType": "map_idType",
                    "workspace": "SUBSCRIBER",
                    "idValue": "map_idValue"
                },
                "isChildDataRequired": "N",
                "isDefaultAccountGroupRequired": "Y",
                "isUserAccountDataRequired": "Y",
                "perPage": 5,
                "pageNumber": 1
            }
        }
    },
    "80": {
        "cashin": {
            "api_name": "api_transaction_cashin",
            "Authorization": "****",
            "data": {
                "body": {
                    "receiver": {
                        "idValue": "",
                        "idType": "mobileNumber",
                        "workspace": "SUBSCRIBER"
                    },
                    "transactor": {
                        "idValue": "51969752322",
                        "idType": "mobileNumber",
                        "workspace": "BUSINESS"
                    },
                    "extensibleFields": {
                        "source": "http-fcompartamos_fullcarga"
                    },
                    "initiator": "transactor",
                    "transactionAmount": "",
                    "currency": 101,
                    "externalReferenceId": ""
                },
                "x_channel": "AGENTE"
            }
        }
    },
    "81": {
        "merchantpayment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Bearer ++",
            "data": {
                "transactionAmount": "",
                "currency": 101,
                "initiator": "sender",
                "externalReferenceId": "",
                "remarks": "",
                "sender": {
                    "workspace": "SUBSCRIBER",
                    "idType": "mobileNumber",
                    "idValue": ""
                },
                "receiver": {
                    "workspace": "BUSINESS",
                    "idType": "mobileNumber",
                    "idValue": ""
                },
                "partnerData": {
                    "codigoPago": ""
                },
                "extensibleFields": {
                    "field2": "",
                    "source": "http-xml_awspdp",
                    "field1": "a",
                    "field9": "a",
                    "field10": "a"
                }
            }
        }
    },
    "82": {
        "merchantpayment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Bearer ++",
            "data": {
                "transactionAmount": "",
                "currency": 101,
                "initiator": "sender",
                "externalReferenceId": "",
                "remarks": "",
                "sender": {
                    "workspace": "SUBSCRIBER",
                    "idType": "mobileNumber",
                    "idValue": ""
                },
                "receiver": {
                    "workspace": "BUSINESS",
                    "idType": "mobileNumber",
                    "idValue": ""
                },
                "partnerData": {
                    "codigoPago": ""
                },
                "extensibleFields": {
                    "field2": "",
                    "source": "a",
                    "field1": "a"
                }
            }
        }
    },
    "83": {
        "cashin": {
            "api_name": "api_transaction_cashin",
            "Authorization": "****",
            "data": {
                "body": {
                    "receiver": {
                        "idValue": "",
                        "idType": "mobileNumber",
                        "workspace": "SUBSCRIBER"
                    },
                    "transactor": {
                        "idValue": "51915962396",
                        "idType": "mobileNumber",
                        "workspace": "BUSINESS"
                    },
                    "extensibleFields": {
                        "source": "prueba_dryrun"
                    },
                    "initiator": "transactor",
                    "transactionAmount": "",
                    "currency": 101,
                    "externalReferenceId": ""
                },
                "x_channel": "AGENTE"
            }
        }
    },
    "84": {
        "payment": {
            "api_name": "api_transaction_order_billpay",
            "Authorization": "Bearer token",
            "data": {
                "transactionAmount": "5",
                "remarks": "",
                "sender": {
                    "workspace": "SUBSCRIBER",
                    "idValue": "",
                    "idType": "mobileNumber",
                    "productId": 12
                },
                "receiver": {
                    "idValue": "",
                    "idType": "loginId",
                    "productId": 12
                },
                "extensibleFields": {
                    "source": "a",
                    "field0": "a"
                },
                "currency": 101,
                "language": "es",
                "initiator": "sender",
                "externalReferenceId": ""
            }
        }
    }
}