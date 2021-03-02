from os.path import split
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from tkinter import messagebox as MessageBox
import os

def desifrar(llavee,direccionArchDescifrar):

    
    arrDireccionArchDescifrar = os.path.split(direccionArchDescifrar) 
    nombreNuevoArchivo= arrDireccionArchDescifrar[1]
    try:
      nombreNuevoArchivo=nombreNuevoArchivo.split("_C.")
      nombreNuevoArchivo= nombreNuevoArchivo[0]+"_D."+nombreNuevoArchivo[1]
      nombreNuevoArchivo= arrDireccionArchDescifrar[0]+"/"+nombreNuevoArchivo
    except IndexError:
      MessageBox.showinfo("Alerta!", "El archivo a descifrar no cumple con las caracteristicas.")
      return 

    print(nombreNuevoArchivo)
    

    try:
      f = open(direccionArchDescifrar, "rb")
      mensaje = f.read()


      llave = RSA.importKey(open(llavee , "r").read())
      cifrado = PKCS1_OAEP.new(llave)
      try:
        mensajeDescifrado = cifrado.decrypt(mensaje)
        print ("El mensaje es: " + mensajeDescifrado.decode("utf-8"))
        MessageBox.showinfo("Alerta!", "Mensaje Descifrado")
        f = open(nombreNuevoArchivo, "w")
        f.write(mensajeDescifrado.decode("utf-8"))
        f.close()
        
        return mensajeDescifrado.decode("utf-8")
      except ValueError :
          print("La llave es Erronea")
          MessageBox.showinfo("Alerta!","La llave  es Erronea")
      except TypeError :
          print("La llave es Erronea")
          MessageBox.showinfo("Alerta!","La llave  es Erronea")
          

          #La llave publica puede cifrar pero no descifrar
    except TypeError:
      MessageBox.showinfo("Alerta!","Debe escoger un archivo para descifrar")