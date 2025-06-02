import { check } from 'k6';
import http from 'k6/http';
import { API_ENDPOINTS, RESOURCES, API_KEY, AES } from '../config/default.js';
import { buildBasicAuthHeader } from '../utils/aes_encrypt.js';
import { log_req_res } from '../utils/log.js'


/**
 * Ejecute la función de prueba, Una vez por iteración, tantas veces como lo requieran las opciones de prueba
 */
export default function(users) {
    const user = users[__VU - 1]
    const payload = JSON.stringify({
        id_indigitall: user["id_indigitall"],
        traza_app: user["traza_app"]
    });
    let basicAuth = buildBasicAuthHeader(user["msisdn"], user["password"], AES.KEY, AES.IV);
    console.log("Basic Auth:", basicAuth);
    if(basicAuth !== "None"){
        const headers = {
            "Authorization": basicAuth,
            "x-api-key": API_KEY.OPERATIONS,
            "Content-Type":	"application/json"
        }
        const URL = API_ENDPOINTS.OPERATIONS + RESOURCES.LOGIN
        const res = http.post(URL, payload, {headers: headers});
        check(res, {
            'status is 200': () => res.status === 200,
        });


        // Lo imprimimos por stdout en formato JSON
        log_req_res({"URL": URL, "payload": payload, "headers": headers}, res, "LOGIN")
        console.log("token: ",res.headers.Token)
        return res.headers.Token;
    }
};