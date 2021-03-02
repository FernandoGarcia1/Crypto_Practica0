from os import read
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def generarFirma(archivo,llave):

    archivo=f=open(archivo, "rb")
    message=archivo.read()        
    archivo.close()

    key = RSA.import_key(open(llave).read())
    h = SHA256.new(message)
    print(h)
    signature = pkcs1_15.new(key).sign(h)
    return signature 