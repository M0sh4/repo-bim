// stress-test.js
import { sleep, check } from 'k6';
import http from 'k6/http';
import { API_ENDPOINTS, RESOURCES, API_KEY } from '../utils/constants.js';
import { buildBasicAuthHeader } from '../utils/aes_encrypt.js';

export default async function() {

  const key           = "Qa3vxOUsYpG7zhBFBY6WeUrg3TC5IyQA"; // 32 caracteres
  const iv            = "m2tEOdbMTgZx7QAi";                 // 16 caracteres
  const msisdn_user   = "51999999989";
  const password      = "202599";
  let basicAuth = "";
  try {
    basicAuth = await buildBasicAuthHeader(msisdn_user, password, key, iv);
    console.log("Basic Auth:", basicAuth);
  } catch (err) {
    console.error("Error en encriptación:", err);
  }

  const headers = {
    "Authorization": basicAuth,
    "x-api-key": API_KEY.OPERATIONS,
    "Content-Type":	"application/json"
  }
  const payload = JSON.stringify({
    id_indigitall: "fda8d529-b6c0-4046-8379-a1783e70beb9",
    traza_app: "eyJITVNfY29yZSI6IiIsInRva2VuIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SjBhVzFsSWpvaU1qQXlOUzB3TWkweU1GUXdNRG8wTlRveU1DNDFNVGd5T1RNck1EQTZNREFpZlEueGVHLV84V0lLNUd6c3FZQWU3cUJHOGZiVUt5YUg0c3hrOGZUSlRDdlE1VSIsIm51bXRlbCI6Ik5URTVNelU1T0RJNE1qUT0iLCJtYWNfd2lmaSI6IjAyOjAwOjAwOjAwOjAwOjAwIiwiaW1laSI6IiIsImlkX3RlbCI6IlFXNWtjbTlwWkRvNlptUXdOR0kzTm1Rek9EbGtZMlUzTXpvNlVtVmtiV2tnVG05MFpTQTRJRkJ5YnpvNldHbGhiMjFwT2pwTllXeHBMVWMzTmlCTlF6UTZPbTEwTmpjNE5UbzYiLCJpZF9vbGQiOiJabVF3TkdJM05tUXpPRGxrWTJVM013PT0iLCJzbyI6IkFuZHJvaWQiLCJ2ZXJzaW9uX3NvIjoiMTEiLCJtb2RlbG8iOiJSZWRtaSBOb3RlIDggUHJvIiwibGFyZ28iOiIyMTM0IiwiYW5jaG8iOiIxMDgwIiwibG9uZ2l0dWQiOiItNzcuMDE5NzE5NSIsImxhdGl0dWQiOiItMTIuMTcwMzE5NyIsInNlc2lvbiI6IjhlMzE5YTZmLWY2ODQtNGIyMy05NmJhLWM4MDAyODgwNmZkOSIsInZlcnNpb24iOiIxLjAuMCIsImlkX2ZpcmViYXNlIjoiY0VSNGx3cjFULS1XbUVDT2FKczd3QzpBUEE5MWJFZlI0My1mdWNwOF84VHZKTTJDdVk0blczV0tWLVhrdnVISzFId0lZbjg1SlNDSTg5a3YybjFYMmw5cW1OUEc4WHBQUVAyNEJvUFViSUVKTWRkMzJsa3VINzcwYjdSeUFPeUptOHYwMGVQejRJd1BaVSIsImlkX2RpZ2l0YWxpbm4iOiJNVGsxT1daa016UXRZV00wTnkwMFpqVTJMV0UyWVRJdE1qbGlPVGd3WVRSak9UVmsiLCJjbGFzZV9kaXNwb3NpdGl2byI6IlNtYXJ0cGhvbmUiLCJmYWJyaWNhbnRlIjoiWGlhb21pIiwibm9tYnJlX2Rpc3Bvc2l0aXZvIjoiYmVnb25pYSIsImJ1aWxkX3RpbWUiOiIwMS8xMS8yMDIyIDEwOjU3OjU0IiwicHJvY2VzYWRvciI6Im10Njc4NSIsImdwdV9yZW5kZXIiOiJNYWxpLUc3NiBNQzQiLCJpZF9pbnN0YWxhY2lvbiI6ImNFUjRsd3IxVC0tV21FQ09hSnM3d0MiLCJiYW5kYWJhc2UiOiJNT0xZLkxSMTMuUjEuVEM4LlNQLlYyLlA1OSxNT0xZLkxSMTMuUjEuVEM4LlNQLlYyLlA1OSIsIkVNVUkiOiIifQ==,51962333371,2,eyJITVNfY29yZSI6IiIsInRva2VuIjoiIiwibnVtdGVsIjoiTlRFNU5qSXpNek16TnpFPSIsIm1hY193aWZpIjoiMDI6MDA6MDA6MDA6MDA6MDAiLCJpbWVpIjoiIiwiaWRfdGVsIjoiUVc1a2NtOXBaRG82T1RKak5qbGlORGs0TmpNME1URXdOam82Ylc5MGJ5Qm5LRGtwSUhCc1lYazZPbTF2ZEc5eWIyeGhPanBCWkhKbGJtOGdLRlJOS1NBMk1UQTZPbkZqYjIwNk9nPT0iLCJpZF9vbGQiOiJPVEpqTmpsaU5EazROak0wTVRFd05nPT0iLCJzbyI6IkFuZHJvaWQiLCJ2ZXJzaW9uX3NvIjoiMTAiLCJtb2RlbG8iOiJtb3RvIGcoOSkgcGxheSIsImxhcmdvIjoiMTQ3MyIsImFuY2hvIjoiNzIwIiwibG9uZ2l0dWQiOiItNzcuMDc1ODYwMSIsImxhdGl0dWQiOiItMTEuOTg0MDE3NSIsInNlc2lvbiI6ImRlYzhhOWVjLTcwZTEtNDU3ZS04MTgwLThhMTNhZDViZjcxNCIsInZlcnNpb24iOiIxLjAuMCIsImlkX2ZpcmViYXNlIjoiZmhIU01JR3hUbGVYWDlqM2R6cnpwZzpBUEE5MWJGVWMzaktEYlZTZ2NLZGNWWVBYMXg1UTI3VGRKQkFmTllDWUlfRXpTVVZQYnJNRndtNWNPWDNzUEF1QTRRM2pDWkt4bFAzSXdmYVhRNXRUX2hLclRQQTBlTWpVX0F2VjU2VUFudGFNeHVTMGRNSWxSayIsImlkX2RpZ2l0YWxpbm4iOiJZVGRrTkRsak9UY3RaRE5tTkMwMFpHTTJMV0kzWW1JdE16SXdPR05pTVRBellqbGwiLCJjbGFzZV9kaXNwb3NpdGl2byI6IlNtYXJ0cGhvbmUiLCJmYWJyaWNhbnRlIjoibW90b3JvbGEiLCJub21icmVfZGlzcG9zaXRpdm8iOiJndWFtcCIsImJ1aWxkX3RpbWUiOiIxMi8zMS8yMDIwIDEyOjQ5OjQ5IiwicHJvY2VzYWRvciI6InFjb20iLCJncHVfcmVuZGVyIjoiQWRyZW5vIChUTSkgNjEwIiwiaWRfaW5zdGFsYWNpb24iOiJmaEhTTUlHeFRsZVhYOWozZHpyenBnIiwiYmFuZGFiYXNlIjoiTTQyNTBfMDcuMTMxLjAxLjU1UiBHVUFNUF9MQVRBTV9DVVNUIiwiRU1VSSI6IiJ9"
  });
  const res = http.post(API_ENDPOINTS.OPERATIONS + RESOURCES.LOGIN, payload, {headers: headers});
  check(res, {
    'status is 200': () => res.status === 200,
  });
  sleep(1);
};