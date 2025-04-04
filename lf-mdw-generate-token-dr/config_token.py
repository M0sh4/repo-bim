AGENTE = {
    "uat": [
        #{
        #    "usuario": "VIRTUALINTEROP2",
        #    "password": "Com@135@18",
        #    "workspace": "BUSINESS",
        #    "identifier_type": "LOGINID",
        #    "authentication_type": "PASSWORD",
        #    "msisdn": "51963897000",
        #},
        #{
        #    "usuario": "VIRTUALINTEROPCFCCE",
        #    "password": "Pdp@Uat@135@13",
        #    "workspace": "BUSINESS",
        #    "identifier_type": "LOGINID",
        #    "authentication_type": "PASSWORD",
        #    "msisdn": "51963564251",
        #},
        #{
        #    "usuario": "AgenteBNacionDNI",
        #    "password": "Com@135@13",
        #    "workspace": "BUSINESS",
        #    "identifier_type": "LOGINID",
        #    "authentication_type": "PASSWORD",
        #    "msisdn": "51977208888",
        #},
        #{
        #    "usuario": "AgenteFCompartamos",
        #    "password": "Dev@UAT#0811",
        #    "workspace": "BUSINESS",
        #    "identifier_type": "LOGINID",
        #    "authentication_type": "PASSWORD",
        #    "msisdn": "51987987005",
        #},
        {
            "usuario": "AgenteKasnet",
            "password": "Dev@UAT#250112",
            "workspace": "BUSINESS",
            "identifier_type": "LOGINID",
            "authentication_type": "PASSWORD",
            "msisdn": "51989294475",
        }
        #{
        #    "usuario": "AgenteFullcarga",
        #    "password": "Dev@UAT#0811",
        #    "workspace": "BUSINESS",
        #    "identifier_type": "LOGINID",
        #    "authentication_type": "PASSWORD",
        #    "msisdn": "51987987004",
        #}
    ],
    "dev": [
        {
            "usuario": "AgenteFCompartamos",
            "password": "Comv23@AFn",
            "workspace": "BUSINESS",
            "identifier_type": "LOGINID",
            "authentication_type": "PASSWORD",
            "msisdn": "51987987005",
        },
    ] ,
   "preprod": [
        {
            "usuario": "VIRTUALINTEROPCFBIM",
            "password": "Dev@UAT#250112",
            "workspace": "BUSINESS",
            "identifier_type": "LOGINID",
            "authentication_type": "PASSWORD",
            "msisdn": "51991022660"
        },
       #{
       #  "usuario": "VIRTUALINTEROPCFCCE",
       #  "password": "pny7mx@qpnqKyJk6#Ew",
       #   "workspace": "BUSINESS",
       #    "identifier_type": "LOGINID",
       #    "authentication_type": "PASSWORD",
       #     "msisdn": "51973913652",
       # },
       {
          "usuario": "COMPWVIRTUAL163",
          "password": "Dev@UAT#250112",
          "workspace": "BUSINESS",
          "identifier_type": "LOGINID",
          "authentication_type": "PASSWORD",
          "msisdn": "51938948480"
       }
       ,# pny7mx/qpn*qKyJk6#Ew
       #{
       #    "usuario": "COMPWKASNET",
       #    "password": "Dev@UAT#250112",
       #    "workspace": "BUSINESS",
       #    "identifier_type": "LOGINID",
       #    "authentication_type": "PASSWORD",
       #    "msisdn": "51989294475"
       #}#,
       #{
       #     "usuario": "COMPWFULLCARGA", 
       #    "password": "Dev@UAT#2501123",
       #    "workspace": "BUSINESS",
       #    "identifier_type": "LOGINID",
       #    "authentication_type": "PASSWORD",
       #    "msisdn": "51969752322"
       #}#,
       #{
       #    "usuario": "COMPWGOPAY",
       #    "password": "pny7mx/qpn*qKyJk6#Ew",
       #    "workspace": "BUSINESS",
       #    "identifier_type": "LOGINID",
       #    "authentication_type": "PASSWORD",
       #    "msisdn": "51915962396",
       #}
    ]
}


ambiente = {
    "dev": {
        "arn_lambda_api_sender" : "arn:aws:lambda:us-east-1:730335559791:function:lf-mdw-api-sender",
        "profile_name": "PDP-DEV-NC",
        "region":"us-east-1",
        "httpconnect": "edxgq24nqi.execute-api.us-east-1.amazonaws.com",
        "x_api":"M7qxQupagL3Puj9wRgJja9g304rcknbI7HrXhLj7",
        "recurso": "/dev/webservice/sender",
        "tabla_tk": "token_auth",
        "DBNC" : {
            "db_password" : "y1eJPOuKvRTr5oAGSouw",
            "db_name" : "dbmdwdevtest",
            "db_host" : "localhost",
            "db_port":8090,
            "connect_timeout": 30,
            "db_username" : "root",
            "db_table_atm_otp": "atm_otp_test"
        }
    },
    "uat": {
        "arn_lambda_api_sender" : "arn:aws:lambda:us-east-1:654654564402:function:lf-mdw-api-sender-dr",
        "profile_name": "PDP-DEV-NC",
        "region":"us-east-1",
        "httpconnect": "mqfndijsjh.execute-api.us-east-1.amazonaws.com",
        "x_api":"EoMxtKHj1X9eEOFVbM9RM7CJTrDgVSdN2HCbP4Tb",
        "recurso": "/qa/b1m/pdp/b3po7/00qmv8dj45",
        "tabla_tk": "token_auth",
        "DBNC" : {
            "db_password" : "y1eJPOuKvRTr5oAGSouw",
            "db_name" : "dbmdwdevtest",
            "db_host" : "localhost",
            "db_port":8090,
            "connect_timeout": 30,
            "db_username" : "root",
            "db_table_atm_otp": "atm_otp_test"
        }
    },
    "preprod": { 
        "arn_lambda_api_sender" : "arn:aws:lambda:us-east-1:474668388170:function:lf-mdw-api-sender",
        "profile_name": "PDP-PROD-NC-6",
        "region":"us-east-1",
        "httpconnect": "mqfndijsjh.execute-api.us-east-1.amazonaws.com",
        "x_api":"EoMxtKHj1X9eEOFVbM9RM7CJTrDgVSdN2HCbP4Tb",
        "recurso": "/qa/b1m/pdp/b3po7/00qmv8dj45",
        "tabla_tk": "token_auth",
        "DBNC" : {
            "db_password" : "y1eJPOuKvRTr5oAGSouw",
            "db_name" : "dbmdwdevtest",
            "db_host" : "localhost",
            "db_port":8090,
            "connect_timeout": 30,
            "db_username" : "root",
            "db_table_atm_otp": "atm_otp_test"
        }
    },


}


DATABASEDR = {
    "db_password" : "B1MPDP2024$",
    "db_name" : "DRYRUN_CAPTURE",
    "db_host" : "db-mid-prod-mysql-dryrun.chy48i8i0qi1.us-east-1.rds.amazonaws.com",
    "db_port":3306,
    "connect_timeout": 30,
    "db_username" : "admin"
 }