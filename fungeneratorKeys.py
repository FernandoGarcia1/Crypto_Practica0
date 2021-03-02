from Crypto.PublicKey import RSA
from tkinter import messagebox as MessageBox

def generarLLaves(llavePriv, llavePublic):
    llave = RSA.generate(2048)

    f = open(llavePriv, "wb")
    f.write(llave.exportKey('PEM'))
    f.close

    f = open(llavePublic, "wb")
    f.write(llave.public_key().export_key('PEM'))
    f.close 

    MessageBox.showinfo("Alerta!", "LLaves Generadas")