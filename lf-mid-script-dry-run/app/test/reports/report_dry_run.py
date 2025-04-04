from jinja2 import Environment, FileSystemLoader
import dry_run.data_db.conexion_logic as conection_mysql
import ast
import json as json
import sys as s
from datetime import datetime
import config as cfg

def get_report():
    id_execution = 6
    print("Inicio reporte",id_execution)
    file_loader = FileSystemLoader('dry_run/reports') 
    env = Environment(loader=file_loader)
    template = env.get_template('report_dry_run.html')

    data_summary = conection_mysql.get_select_report_summary(id_execution,cfg.start_date, cfg.end_date)
    data_details = conection_mysql.get_select_report_details(id_execution,cfg.start_date, cfg.end_date)
    fecha_str = cfg.start_date
    fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    fecha_formateada = fecha_obj.strftime("%d/%m/%Y")

    print(fecha_str,fecha_obj,fecha_formateada)
    expanded_data = []

    for error in data_details:
        detalles_errores = error.get('detalles_errores', None) 
        if detalles_errores:
            try:
                error_convert_to_array = ast.literal_eval(detalles_errores.replace("'", "\""))
            except (ValueError, SyntaxError) as e:
                print(f"Error al convertir detalles_errores: {e}")
                error_convert_to_array = []
        else:
            error_convert_to_array = []

        num_campos = len(error_convert_to_array)

        expanded_data.append({
            'numero': int(error["nrow_details"]),
            'funcionalidad': error['funcionalidad'],
            'api_ewp': error['api_name_ewp'],
            'api_comviva': error['api_name_comviva'],
            'campos': error_convert_to_array,
            'num_campos': num_campos,
            'time_request_comviva' : error['time_request_comviva'],
            'time_execution': error['time_execution']
        })

    if data_summary:
        resultados_esperados = data_summary[0]["resultados_esperados"]
        resultados_exitosos = data_summary[0]["resultados_exitosos"]
        resultados_errores = data_summary[0]["resultados_errores"]
    else:
        resultados_esperados = 0
        resultados_exitosos = 0
        resultados_errores = 0

    output = template.render({
        "fecha": fecha_formateada,
        "resultados_esperados": resultados_esperados,
        "resultados_exitosos": resultados_exitosos,
        "resultados_errores": resultados_errores,
        "detalles_errores": expanded_data
    })
    conection_mysql.set_update_Execution_log(resultados_esperados,resultados_exitosos,resultados_errores,id_execution)
    output_file = "reporte_dry_run.html"
    with open(output_file, "w") as f:
        f.write(output)

    print(f"Reporte generado: {output_file}")
