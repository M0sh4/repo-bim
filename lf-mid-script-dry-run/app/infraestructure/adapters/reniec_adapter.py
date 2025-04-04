import jwt
import time
import uuid

from core.libs.call_api.request_custom import Call


def consult_api_reniec(self, documento):
    documento = "70342970"
    # ?dniConsultante=07643916&dniSolicitado=72103845&tipoConsulta=12&formatoFirma=1
    url = (
        "http://dev.consulta.reniec.pe:9000/interconexion-reniec/ws/reniec/consultaPersonasPorDNI"
        + "?dniConsultante="
        + "07643916"
        + "&dniSolicitado="
        + documento
        + "&tipoConsulta=12&formatoFirma=1"
    )

    payload = {}
    params = {}
    token = self.get_token_reniec(self.secret_data)
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + str(token),
    }

    response_api = call_api.call_api_json("GET", url, payload, params, headers)

    if not response_api[0]:
        return False

    return response_api[2]
