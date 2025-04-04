from database import get_status, get_seguimiento, get_general
def generate():
    table_1 = tabla_error()
    table_2 = tabla_seguimiento()
    table_3 = tabla_general()

    # Combinar tablas en un solo HTML
    html_content = """
    <html>
    <head>
        <title>Reporte</title>
    </head>
    <body>
        <h1>Status General de Transacciones: </h1>
        {table_3}
        <h1>Seguimiento de Peticiones por Api: </h1>
        {table_2}
        <h1>Detalle de Errores por Api: </h1>
        {table_1}
    </body>
    </html>
    """.format(table_2=table_2, table_1=table_1, table_3 = table_3)

    return html_content


def tabla_error():
    headers = ["API NAME", "STATUS CODE", "ERROR CODE", "MESSAGE CORE", "CODE CORE", "ERROR USER MSG", "CANTIDAD", "FECHA RECIENTE"]

    rows = get_status()

    html_table = """
    <div style='overflow-x: auto;'>
        <table border='1' style='border-collapse: collapse; width: 100%; table-layout: auto;'>
            <thead style='background-color: red; color: white;'>
                <tr>
                    """ + "".join([f"<th>{col}</th>" for col in headers]) + """
                </tr>
            </thead>
            <tbody>
    """

    # Agregar filas (manteniendo tu formato original)
    for row in rows:
        html_table += "<tr>"
        
        # Alinear la columna API_NAME a la izquierda
        html_table += f"<td style='word-wrap: break-word; text-align: left;'>{row['api_name_ewp']}</td>"
        
        # Para las columnas numéricas, alinearlas a la derecha
        html_table += f"<td style='word-wrap: break-word; text-align: left;'>{row['statusCode']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: left;'>{row['error_code']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: left;'>{row['message_core']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: left;'>{row['code_core']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: left;'>{row['error_user_msg']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: left;'>{row['count']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: left;'>{row['date_reciente']}</td>"
        html_table += "</tr>"
    html_table += """
            </tbody>
        </table>
    </div>
    """

    return html_table



def tabla_seguimiento():
    headers = ["API NAME", "TOTAL", "CANTIDAD ERROR EWP", "CANTIDAD EXITOSOS EWP", "%",
            "CANTIDAD PROCESADOS COMV", "%", "CANTIDAD EXITOSOS COMV", "%", "CANTIDAD ERROR COMV", "%",
            "CANTIDAD POR PROCESAR COMV", "%", "CANTIDAD EN PROCESO COMV", "%","MIN TIME","AVG TIME","MAX TIME"]

    rows = get_seguimiento()

    html_table = """
    <div style='overflow-x: auto;'>
        <table border='1' style='border-collapse: collapse; width: 100%; table-layout: auto;'>
            <thead style='background-color: red; color: white;'>
                <tr>
                    """ + "".join([f"<th>{col}</th>" for col in headers]) + """
                </tr>
            </thead>
            <tbody>
    """

    # Agregar filas (manteniendo tu formato original)
    for row in rows:
        html_table += "<tr>"
        
        # Alinear la columna API_NAME a la izquierda
        html_table += f"<td style='word-wrap: break-word; text-align: left;'>{row['API_NAME']}</td>"
        
        # Para las columnas numéricas, alinearlas a la derecha
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['TOTAL']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['CANTIDAD_ERROR_EWP']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['CANTIDAD_EXITOSOS_EWP']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['EXITOSOS_EWP']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['CANTIDAD_PROCESADOS_COMV']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['PROCESADOS_COMV']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['CANTIDAD_EXITOSOS_COMV']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['EXITOSOS_COMV']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['CANTIDAD_ERROR_COMV']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['ERROR_COMV']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['CANTIDAD_POR_PROCESAR_COMV']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['POR_PROCESAR_COMV']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['CANTIDAD_EN_PROCESO_COMV']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['EN_PROCESO_COMV']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['MIN_TIME']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['AVG_TIME']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['MAX_TIME']}</td>"
        html_table += "</tr>"

    html_table += """
            </tbody>
        </table>
    </div>
    """

    return html_table


def tabla_general():
    headers = ["DETALLE", "CANTIDAD", "PORCENTAJE"]

    rows = get_general()

    html_table = """
    <div style='overflow-x: auto;'>
        <table border='1' style='border-collapse: collapse; width: 100%; table-layout: auto;'>
            <thead style='background-color: red; color: white;'>
                <tr>
                    """ + "".join([f"<th>{col}</th>" for col in headers]) + """
                </tr>
            </thead>
            <tbody>
    """

    # Agregar filas (manteniendo tu formato original)
    for row in rows:
        html_table += "<tr>"
        
        # Alinear la columna API_NAME a la izquierda
        html_table += f"<td style='word-wrap: break-word; text-align: left;'>{row['metric']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['value']}</td>"
        html_table += f"<td style='word-wrap: break-word; text-align: right;'>{row['percentage']}</td>"
        html_table += "</tr>"

    html_table += """
            </tbody>
        </table>
    </div>
    """

    return html_table
