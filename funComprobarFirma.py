from Crypto import Signature
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from tkinter import messagebox as MessageBox



def verificarFirma(archivo,llave,sig):

    signature= sig
    f=open(archivo, "rb")
    message=f.read()


    #print(signature)

    
        

    key = RSA.import_key(open(llave).read())
    h = SHA256.new(message)
    print(message)
    try:
        
        pkcs1_15.new(key).verify(h, signature)
        MessageBox.showinfo("Alerta!", "La firma es Correcta")
        
        print ("La llave es valida.")
    # print(signature.decode("utf-8"))
        
    except (ValueError, TypeError):
        print ("La llave NO es valida.")
        MessageBox.showinfo("Alerta!", "La firma No es Correcta")
        #print(message)
        