''' Valida input/output'''
from app.shared.utils import Utils

class MappingDomain:
    ''' Class MappingDomain'''

    def val_fecha_inicio_fin(self, start_date, end_date, format_fecha):
        ''' Validación de fecha inicio y fin'''
        try:
            utils = Utils()
            is_date = False
            bol_start_date = utils.is_formato_fecha_hora(start_date)
            bol_end_date = utils.is_formato_fecha_hora(start_date)

            if(bol_start_date is False):
                raise ValueError(
                    "Error DR: La fecha inicio no tiene el formato correcto"
                )
            if(bol_end_date is False):
                raise ValueError(
                    "Error DR: La fecha fin no tiene el formato correcto"
                )

            fecha_inicio = utils.transform_datetime(start_date, format_fecha)
            fecha_fin = utils.transform_datetime(end_date, format_fecha)

            if(bol_start_date and bol_end_date):
                is_date = True

            if fecha_fin < fecha_inicio:
                is_date = False
                raise ValueError("Error DR: La fecha inicio es mayor que la fecha fin.")
            return is_date
            
        except ValueError as e:
            print(repr(f"Error DR: Ocurrió un error select mapping: {e}"))
            return False
        
    def val_dict_mapping(self, resp_mysql):
        utils = Utils()
        message = "OK"

        if (not resp_mysql or len(resp_mysql) == 0) and not resp_mysql[0]["result_json"]["api_name"]:
            message ="No se encontró registros de mapping para realizar la comparación \n mapping_domain/val_dict_mapping"

        json_select = utils.deserializacion_json(resp_mysql[0]["result_json"])

        if (
            not json_select["type_token"]
            or len(json_select["type_token"]) == 0
        ):
            message = "No existe registros en Plantilla_json_api para la comparación \n mapping_domain/val_dict_mapping"

        return message, json_select