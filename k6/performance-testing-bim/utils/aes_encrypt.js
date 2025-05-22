import CryptoJS from "https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js";

/**
 * Encripta en AES-CBC con PKCS7 y devuelve un header Basic con doble Base64.
 */
export function buildBasicAuthHeader(msisdn_user, password, keyStr, ivStr) {
    let doubleBase64 = ""
    try{
        const plaintext = `${msisdn_user}:${password}`;

        // 1) Convertir clave e IV a wordarrays UTF8
        const key = CryptoJS.enc.Utf8.parse(keyStr);
        const iv  = CryptoJS.enc.Utf8.parse(ivStr);

        // 2) Encriptar con AES-CBC + PKCS7
        const encrypted = CryptoJS.AES.encrypt(plaintext, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7,
        });

        // encrypted.toString() ya es Base64
        const cipherBase64 = encrypted.toString();

        // 3) Doble Base64 y formatear header
        doubleBase64 = typeof btoa === "function"
            ? btoa(cipherBase64)
            : CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(cipherBase64));
            
        return `Basic ${doubleBase64}`;
    }catch(err){
        console.log(err)
        return "None"
    }
}