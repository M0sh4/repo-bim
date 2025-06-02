import encoding from "k6/encoding";

/**
 * Encripta en base 64
 */
export function encryptB64(text) {
    try{
        const base64str = encoding.b64encode(text);
        return base64str;
    }catch(err){
        console.log(err)
        return "None"
    }
}