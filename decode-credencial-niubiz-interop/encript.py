

import pyaes
import base64_custom as b64
#import config as cfg
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
from base64 import b64decode
class CryptoUtil():

    def __init__(self):
        self.semilla = "8bce46c89098407caa76f0cc3bc02274"

    def encript_word(self, word, semilla):

        byte_semilla = bytes(semilla, 'utf-8')
        aes = pyaes.AESModeOfOperationCTR(byte_semilla)
        word_enc_bytes = aes.encrypt(word)
        word_enc= b64.encode_b64(word_enc_bytes)
        return word_enc
    
    def decript_word(self, word_encripted, semilla):
        byte_semilla = bytes(semilla, 'utf-8')
        aes = pyaes.AESModeOfOperationCTR(byte_semilla)
        word_encripted_bytes = b64.decode_b64(word_encripted, encryptation=True)
        word = aes.decrypt(word_encripted_bytes)
        return str(word.decode("utf-8"))


    def encript_CBC(self, text, key, iv):
        # Agrega padding a los datos para que coincidan con el bloque de AES (128 bits)

        
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(text) + padder.finalize()

        # Crear el cifrador AES-256 en modo CBC
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Encriptar los datos
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        ciphertext_b64 = b64.encode_b64(ciphertext)#.decode('utf-8')
        return ciphertext_b64

    def decrypt_aes256_CBC(self, ciphertext, key, iv):
        key = key#.encode("utf-8")
        iv = iv#.encode("utf-8")

        aux = b64decode(ciphertext[6:])
        ciphertext = b64decode(aux.strip())
        # Crear un objeto Cipher AES en modo CBC
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

        # Crear un descifrador
        decryptor = cipher.decryptor()

        # Desencriptar el texto
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        # Remover el relleno
        unpadder = padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

        # Devolver el texto desencriptado como una cadena UTF-8
        return plaintext.decode("utf-8")
import hashlib

def hash_to_32_chars(text):
    # Crear un objeto hash SHA-256
    hash_object = hashlib.sha256(text.encode())
    
    # Obtener el digest en hexadecimal
    hash_hex = hash_object.hexdigest()
    
    # Tomar los primeros 32 caracteres del hash
    hash_32_chars = hash_hex[:32]
    
    return hash_32_chars

 
# Ejemplo de uso
text =  b"tEYcwr3SBCvv0xLjI8YEm1SNzpGd46eD/DnOW+msrdf5bXSN"
#hash_32bit = hash_to_32_chars(text)
#print("Hash de 32 bits:", hash_32bit)

semilla = "8bce46c89098407caa76f0cc3bc02274"
obj = CryptoUtil()
d = obj.encript_word("VklSVFVBTElOVEVST1BDRkJJTTpEZXZAVUFUIzI1MDExNQ==", semilla)
#{"value":"thwy17jBZzzpwDT8IMcih1fWyaeEzKukyyTWWunmudTmVF6N","mobileNumber":"51963897000"}
print(d)
d = obj.decript_word("thwy17jBZzzpwDT8IMcih1fWyaeEzKukyynOW+msrdf5bV6N", semilla)
print(d)
#tj4M0LvGfTfz0R3hOdJG7kCI5Z76lNCSmEQ=