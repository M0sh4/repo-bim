'''Utils'''
import ast
import base64
import json
import re
import unicodedata
import xml.etree.ElementTree as xml
from datetime import datetime
from time import time
from xml.etree.ElementTree import fromstring, tostring

import pandas as pds
import xmltodict
from jsonpath_ng import parse
from xmljson import badgerfish, parker
import pytz
tz = pytz.timezone("America/Lima")

class Utils:
    def is_formato_fecha_hora(self, fecha_hora):
        # Expresión regular para validar el formato YYYY-MM-DDTHH:MM:SS.SSSZ
        patron = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$"
        if re.match(patron, fecha_hora):
            return True
        else:
            return False

    def transform_datetime(self, date, format_fecha):
        return datetime.strptime(date, format_fecha)

    def normalizar_str(self, text):
        return unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8').lower()
    
    def deserializacion_json(self,text_data):
        '''Metodo para deserializar las variables'''
        result = None
        if(text_data is None or not text_data):
            result = ""
        elif(isinstance(text_data, str)):
            if not text_data.strip().startswith("{"):
                    text_data = "{" + text_data
            if("''") in text_data:
                text_data = text_data.replace("''","'")

            if any(char in text_data for char in ['{', '[']):
                try:
                    result = (ast.literal_eval(text_data))
                except ValueError:
                    clean_text = self.sanitize_json(text_data)
                    clean_text = self.clean_json_string(clean_text)
                    result = json.loads(clean_text)
                except SyntaxError:
                    
                    clean_text = self.sanitize_json(text_data)
                    clean_text = self.clean_json_string(clean_text)
                    result = json.loads(clean_text)
            else:
                result = text_data
        elif(isinstance(text_data, dict)):
            result = text_data
            
        return result

    def transform_list_to_dataframe(self,data_dict):
        '''Metodo transformar lista a dataframe con pandas'''
        result = None
        if(data_dict is None or not data_dict or data_dict == ""):
            result = ''
        elif(isinstance(data_dict, list)):
            result =  pds.DataFrame(data_dict)
        return result
    
    def sanitize_json(self,text):
        # Escapar las comillas dobles en el valor del XML
        start_message = text.find('"<?xml') + 1  # Inicio del campo message
        end_message = text.rfind('>"}')  # Final del campo message
        if start_message != -1 and end_message != -1:
            xml_content = text[start_message:end_message]
            escaped_xml = xml_content.replace('"', '\\"')  # Escapar comillas
            sanitized_text = text[:start_message] + escaped_xml + text[end_message:]
            return sanitized_text
        return text
    
    def clean_json_string(self, json_string):
        # Eliminar saltos de línea y tabulaciones
        cleaned = json_string.replace("\n", "").replace("\t", "")
        
        # Eliminar espacios excesivos entre palabras
        cleaned = ' '.join(cleaned.split())
        
        return cleaned


    def val_variable(self, query):
        bquery = True
        if(isinstance(query, str)):
            if(query == ""):
                bquery = False
        else:
            if(not query or query is None):
                bquery = False

        return bquery

    def get_replace_values_json(self, data, before_value, new_value):

        data2 = json.dumps(data).replace(before_value,new_value)
        return data2


    def translate_to_jsonpath(self, clave_ewp):
        """
        Convertir una clave en formato 'clave1.clave2.clave3' en una expresión JSONPath válida,
        manejando filtros dinámicos como '?(@.property == value)' si se provee.
        """
        filtro_property=None
        filtro_value=None

        parts_clave_ewp = clave_ewp.split('.')
        jsonpath_expression = '$'  # La expresión JSONPath debe comenzar con '$'
        
        for part in parts_clave_ewp:
            if '[' in part and ']' in part:  # Detectamos si es un arreglo
                jsonpath_expression += f'.{part}'
            else:
                jsonpath_expression += f'.{part}'
        
        # Agregar lógica para el filtro dinámico si se proveen `filtro_property` y `filtro_value`
        if filtro_property and filtro_value:
            jsonpath_expression += f'[?(@.{filtro_property} == "{filtro_value}")]'
        
        return jsonpath_expression

    def force_string_values (self, message):
        if message.text and message.text.strip():
            message.text = message.text.strip()  # Asegura que el texto no tenga espacios
        for child in message:
            self.force_string_values(child)


    def remove_namespaces(self, xml_dict):
        """Elimina los prefijos de espacio de nombres en el diccionario generado por xmltodict."""
        def clean_dict(d):
            if isinstance(d, dict):
                return {k.split(":")[-1]: clean_dict(v) for k, v in d.items()}
            elif isinstance(d, list):
                return [clean_dict(i) for i in d]
            else:
                return d

        return clean_dict(xml_dict)
    
    def traslate_xml_in_json(self, message):

        json_data = xmltodict.parse(message)
        root_key = next(iter(json_data))
        result_json = json.dumps(json_data[root_key])

        return result_json

    def es_posible_xml(self, response_ewp):
        return response_ewp.strip().startswith("<") and response_ewp.strip().endswith(">")


    def buscar_en_json(self, data_json, clave, type_compare):
        ''' Busca valor de la clave con jsonpath '''

        data_json = self.deserializacion_json(data_json)
        jsonpath_expression = self.translate_to_jsonpath(clave)
        parse_expression_ = parse(jsonpath_expression)

        matches = [str(match.value) if isinstance(match.value, (int, float)) else match.value for match in parse_expression_.find(data_json)]

        if not matches:
            return None, False

        if type_compare == "arreglos":
            result = matches
        else:
            result = matches[0]

        return result, True
    
    def compare_values_formate(self, valor_ewp, valor_mob , valor_ewp_replace, valor_mob_replace, type_replace) -> bool:
            # Validar si los valores son nulos
            if valor_ewp is None or valor_mob is None:   
                return False
            elif (isinstance(valor_ewp, (int, float)) or (isinstance(valor_ewp, str) and valor_ewp.replace('.', '', 1).isdigit())) and \
            (isinstance(valor_mob, (int, float)) or (isinstance(valor_mob, str) and valor_mob.replace('.', '', 1).isdigit())):
                # Si las cadenas no son numéricas, imprime un mensaje de error
                key1_float = float(valor_ewp)
                key2_float = float(valor_mob)
                # Formatear los números a 4 decimales para comparación
                key1_formatted = f"{key1_float:.4f}"
                key2_formatted = f"{key2_float:.4f}"

                # Comparar los valores formateados
                if key1_formatted != key2_formatted:
                    return False
                else:
                    return True
            elif (self.is_potential_date(valor_ewp) and self.is_potential_date(valor_mob)):
                valor_ident_date_ewp = self.parse_datetime(valor_ewp)
                valor_ident_date_mob = self.parse_datetime(valor_mob)

                valor_ident_date_ewp_formatted = self.format_datetime(valor_ident_date_ewp)
                valor_ident_date_mob_formatted = self.format_datetime(valor_ident_date_mob)

                # Comparar fechas formateadas
                if valor_ident_date_ewp_formatted != valor_ident_date_mob_formatted:
                    print(repr(f"No coinciden las fechas: {valor_ident_date_ewp_formatted} != {valor_ident_date_mob_formatted}"))
                    return False
                else:
                    print(repr(f"Coinciden las fechas: {valor_ident_date_ewp_formatted} == {valor_ident_date_mob_formatted}"))
                    return True
            else:
                is_compare_estatico = 0 # valor_ewp_replace, valor_comv_replace,

                if((type_replace == 'E') and (str(valor_ewp_replace) == str(valor_ewp)) and (str(valor_mob_replace) == str(valor_mob))):
                    is_compare_estatico = 1
                elif((type_replace == 'C') and str(valor_ewp) == str(valor_mob)):
                    is_compare_estatico = 1
                else:
                    is_compare_estatico = 0

                if is_compare_estatico == 0:
                    return False
                else:
                    return True

    def parse_datetime(self, value):
        """Intenta convertir un valor a datetime según múltiples formatos."""
        if not isinstance(value, str):
            raise ValueError(f"Error DR: El valor no es una cadena válida: {value}")
        date_formats = [
            "%Y-%m-%dT%H:%M:%S.%f%z",  # Con microsegundos y zona horaria
            "%Y-%m-%dT%H:%M:%S%z",      # Con zona horaria
            "%Y-%m-%dT%H:%M:%S",         # Sin zona horaria
            "%Y-%m-%d %H:%M:%S",         # Fecha y hora
        ]
        for fmt in date_formats:
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue  # Si falla, intenta el siguiente formato
        raise ValueError(f"Error DR: Formato de fecha no reconocido para el valor: {value}")

    def format_datetime(self, dt):
        """Formatear el datetime a solo fecha, hora, minutos y segundos sin microsegundos."""
        return dt.strftime("%Y-%m-%d %H:%M:%S")  # Devolver en formato deseado


    def is_potential_date(self, value):
        """Determina si un valor es potencialmente una fecha basada en su formato de cadena."""
        if isinstance(value, str) and all(char in value for char in ['-', ':', 'T']):
            return True
        return False
    
    def is_dataframe (self, date):
        result = True
        if (not isinstance(date, pds.DataFrame)):
            result = False
        return result
    
    def is_date_xml(self, response_ewp):
        try:
            xml.fromstring(response_ewp)
            return True
        except xml.ParseError:
            return False
    
    def buscar_y_tomar_valor(self, json_data, contextos):
        # Convertir JSON a una cadena de texto para realizar la búsqueda
        json_texto = json.dumps(json_data)
        
        for key, valor in contextos.items():
            if key in json_texto:
                return valor
        return None  # Retorna None si no se encuentra ninguna clave
    
    def generate_internal_trx(self, phoneNumber):
        timestamp_actual = int(time() * 100)  # #Centesimas de segundo
        print(repr(f"Timestamp actual: {timestamp_actual}"))
        timestamp_actual = self.get_time_pass(timestamp_actual)
        print(repr(f"Timestamp Recortado: {timestamp_actual}"))
        msisdn = phoneNumber[2:]
        id_new = str(timestamp_actual)[:19] + str(msisdn)
        print(repr(f"NEW ID {id_new}"))
        return self.combinar_digitos(id_new)
    
    def get_time_pass(self, timestamp_actual):
        today_date_midnight = datetime.now(tz).strftime("%Y") + "-01-01 00:00:00"

        date_format = "%Y-%m-%d %H:%M:%S"
        date_object = datetime.strptime(today_date_midnight, date_format)
        timestamp = datetime.timestamp(date_object)
        dif = int((timestamp_actual - timestamp * 100))  # #Centesimas de segundo
        return dif

    def combinar_digitos(self, numero):
        # Convertir el número a una cadena de caracteres
        numero_str = str(numero)
        # Inicializar una cadena para almacenar el resultado
        resultado = ""
        # Recorrer la cadena de caracteres en pasos de dos
        for i in range(0, len(numero_str), 2):
            # Concatenar y combinar los dos dígitos y agregarlos al resultado
            resultado += numero_str[i : i + 2][::-1]
        return resultado
    
    def generar_codigo(self):
        # Obtener la fecha y hora actual con microsegundos
        ahora = datetime.now(tz)
        
        # Redondear los segundos según el valor de los milisegundos
        segundo_redondeado = round(ahora.second + ahora.microsecond / 1_000_000)
        
        # Si el segundo redondeado es 60, incrementamos el minuto y restablecemos el segundo
        if segundo_redondeado == 60:
            ahora = ahora.replace(second=0)
            if ahora.minute == 59:
                ahora = ahora.replace(minute=0, hour=ahora.hour + 1 if ahora.hour < 23 else 0)
            else:
                ahora = ahora.replace(minute=ahora.minute + 1)
        else:
            ahora = ahora.replace(second=segundo_redondeado)
        
        # Formatear el código en el formato deseado
        codigo = ahora.strftime("%Y%m%d%H%M%S")
        return codigo,True

    def encode_b64(self, message: str) -> str:
        message_bytes = message.encode("utf-8")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("utf-8")
        return base64_message
    
    def clean_text(self, text):
      
        if not isinstance(text, str) or text.strip() == "":
            return text  # Retorna el texto original si no es una cadena válida

        try:
            # Caso 1: Convertir escapes Unicode como \u00d1 a caracteres legibles
            text = text.encode('utf-8').decode('unicode_escape')
        except (UnicodeDecodeError, AttributeError):
            pass  # Continúa si no aplica

        try:
            # Caso 2: Resolver problemas de codificación mal interpretada (como \x91)
            text = text.encode('latin1').decode('utf-8')
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass  # Continúa si no aplica
        return text
    
    def format_text_if_state(self, text):
        text = text.replace(" ", "").upper()
        return text

    # def decrypt_aes256(self, ciphertext):
    #     key = cfg.Key_.encode("utf-8")
    #     iv = cfg.IV.encode("utf-8")

    #     aux = b64decode(ciphertext[6:])
    #     ciphertext = b64decode(aux.strip())
    #     # Crear un objeto Cipher AES en modo CBC
    #     cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    #     # Crear un descifrador
    #     decryptor = cipher.decryptor()

    #     # Desencriptar el texto
    #     padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    #     # Remover el relleno
    #     unpadder = padding.PKCS7(128).unpadder()
    #     plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    #     # Devolver el texto desencriptado como una cadena UTF-8
    #     return plaintext.decode("utf-8")