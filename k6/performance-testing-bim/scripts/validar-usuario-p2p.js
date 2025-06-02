import { check } from 'k6';
import http from 'k6/http';
import { API_ENDPOINTS, RESOURCES, API_KEY } from '../config/default.js';
import { encryptB64 } from '../utils/b64_encrypt.js';
import { log_req_res } from '../utils/log.js'


/**
 * Ejecute la función de prueba, Una vez por iteración, tantas veces como lo requieran las opciones de prueba
 */
export default function(users, token) {
    const user = users[__VU - 1]
    const payload = JSON.stringify({
        destination_msisdn: "NTE5NjIzMzMzNzE=",
        traza_app: user["traza_app"]
    });
    let msisdn = user["msisdn"]
    let credentials = encryptB64(msisdn +":"+user["password"])
    let msisdnEncoded = encryptB64(msisdn)
    console.log("Basic Auth:", credentials);
    console.log("Msisdn encode b64:", msisdnEncoded);
    if(credentials !== "None"){
        const headers = {
            // "Authorization": "Basic " + credentials,
            "x-api-key": API_KEY.OPERATIONS,
            "pantalla": "TXNObVB0VF8xMjc=",
            "msisdn": msisdnEncoded,
            "token": token
        }
        const URL = API_ENDPOINTS.OPERATIONS + RESOURCES.VALIDAR_USUARIO_MANDAR_PLATA
        const res = http.post(URL, payload, {headers:  headers});
        check(res, {
            'status is 200': () => res.status === 200,
        });
        log_req_res({"URL": URL, "payload": payload, "headers": headers}, res, "VALIDAR_USUARIO_MANDAR_PLATA")
        return res;
    }
};