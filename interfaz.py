from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont
from tkinter import messagebox as MessageBox

from fungeneratorKeys import *
from funcifrar import *
from fundesifrar import *
from funFirma import *
from funComprobarFirma import *
import os



raiz=Tk()
frame=Frame(raiz)
frame.pack()


fontStyle = tkFont.Font(family="Lucida Grande", size=40)

llaveCifrar = ""
llaveDecifrar = ""
TextCifrar1=""
ficheroCifrar=[]
ficheroDescifrar= []
ficheroFirmar= ""
verFicheroFirmar=""
llaveFirmar=""
verLLaveFirmar=""
signature=""
#---------------------------------------------------------------
def enviarBotonKeys():
    TextKeys= entryKeys.get()
    PrivKey= "LLavePrivada_"+TextKeys+".pem"
    PublicKey= "LLavePublica_"+TextKeys+".pem"
    print(TextKeys )
    print(PrivKey)
    print(PublicKey)
    generarLLaves(PrivKey,PublicKey)

def seleccionar ():
    global ficheroCifrar
    ficheroCifrar = filedialog.askopenfilename(title = "Seleccionar", filetypes = [("Ficheros TXT", "*.txt"), ("Todos los archivos", "*.*")])
    rutaFicheroCifrar= ficheroCifrar
    ficheroCifrar = os.path.split(ficheroCifrar)     
    global TextCifrar1
    print(ficheroCifrar)
    leerTexto= open(rutaFicheroCifrar, "r")
    TextCifrar1=leerTexto.read()
   # print(TextCifrar1)
    leerTexto.close()    
    


def abrirCifrar ():
    
    ficheroCifrar = filedialog.askopenfilename(title = "Abrir", filetypes = [("Ficheros PEM", "*.pem"), ("Todos los archivos", "*.*")])
    global llaveCifrar
    llaveCifrar = ficheroCifrar
   # print (llaveCifrar)
    
def enviarCifrar ():
    global llaveCifrar
    global TextCifrar1    
    global ficheroCifrar
  
    if llaveCifrar == "":
        MessageBox.showinfo("Alerta!", "Debes seleccionar un archivo")
    else: 
        TextCifrar1==""
        if TextCifrar1 == "":
           MessageBox.showinfo("Alerta!","Debes Escribir un Texto")
        else :
            print(TextCifrar1)
            print(llaveCifrar)
            cifrar(TextCifrar1,llaveCifrar,ficheroCifrar)
            
            MessageBox.showinfo("Alerta!","Mensaje Cifrado en el archivo ")
            


def abrirLLaveDescifrar():
    LLaveCifrar = filedialog.askopenfilename(title = "Abrir", filetypes = [("Ficheros PEM", "*.pem"), ("Todos los archivos", "*.*")])
    global llaveDecifrar
    llaveDecifrar = LLaveCifrar
    print (llaveDecifrar)

def abrirArchivoDescifrar():
    global ficheroDescifrar
    ficheroDescifrar= filedialog.askopenfilename(title = "Seleccionar", filetypes = [("Ficheros TXT", "*.txt"), ("Todos los archivos", "*.*")])
    

    


def enviarDescifrar ():
    global llaveDecifrar
    print(llaveDecifrar)
    if (llaveDecifrar) == "":
        MessageBox.showinfo("Alerta!", "Debes seleccionar un archivo")
    else:
        print(llaveDecifrar)
        mensajeDes= desifrar(llaveDecifrar,ficheroDescifrar)               
    #    messageRSA.config(text=mensajeDes)

def limpiar():
    limpio=""
    messageRSA.config(text=limpio)


def abrirArchFirma():
    global ficheroFirmar
    ficheroFirmar= filedialog.askopenfilename(title = "Seleccionar", filetypes = [("Ficheros TXT", "*.txt"), ("Todos los archivos", "*.*")])
   # print(ficheroFirmar)


def abrirLLaveFirma():
    global llaveFirmar
    llaveFirmar= filedialog.askopenfilename(title = "Abrir Llave", filetypes = [("Ficheros PEM", "*.pem"), ("Todos los archivos", "*.*")])
    #print(llaveFirmar)

def crearArchivo(rutaArchivo, signature, caracter):

    
    rutaArchivo=os.path.split(rutaArchivo)
    nombreArchivo= rutaArchivo[1]
    nombreArchivo=nombreArchivo.split(".")
    nuevoNombre=nombreArchivo[0]+"_"+caracter+"."+nombreArchivo[1]
    nuevoArchivo= rutaArchivo[0]+"/"+nuevoNombre

    f = open(nuevoArchivo, "wb")
    f.write(signature)
    f.close()

    








def enviarFirma():
    global llaveFirmar
    print(llaveFirmar)
    global ficheroFirmar
    print(ficheroFirmar)
    
    if llaveFirmar=="":
        MessageBox.showinfo("Alerta!", "Debes seleccionar una LLave")
    else:
        if ficheroFirmar=="":
            MessageBox.showinfo("Alerta!", "Debes seleccionar un archivo")
        else:            
            signature=generarFirma(ficheroFirmar,llaveFirmar)            
            crearArchivo(ficheroFirmar,signature,"C")
            MessageBox.showinfo("Alerta!", "Archivo Firmado")




def abrirVerArchFirma():
    global verFicheroFirmar
    verFicheroFirmar= filedialog.askopenfilename(title = "Seleccionar", filetypes = [("Ficheros TXT", "*.txt"), ("Todos los archivos", "*.*")])

def abrirVerLLaveFirma():
    global verLLaveFirmar
    verLLaveFirmar= filedialog.askopenfilename(title = "Abrir Llave", filetypes = [("Ficheros PEM", "*.pem"), ("Todos los archivos", "*.*")])

def abrirVerSignatureFirma():
    global signature
    archivo= filedialog.askopenfilename(title = "Abrir Llave", filetypes = [("Ficheros TXT", "*.txt"), ("Todos los archivos", "*.*")])
    f = open(archivo, "rb")
    signature= f.read()
    f.close()
    



def enviarVerFirma():
    global verLLaveFirmar    
    global verFicheroFirmar    
    global signature

    if verLLaveFirmar=="":
        MessageBox.showinfo("Alerta!", "Debes seleccionar una LLave")
    else:
        if verFicheroFirmar=="":
            MessageBox.showinfo("Alerta!", "Debes seleccionar un archivo")
        else:
            verificarFirma(verFicheroFirmar,verLLaveFirmar,signature)
            f= open(verFicheroFirmar,"rb")
            mensaje= f.read()
            f.close()
            crearArchivo(verFicheroFirmar,mensaje,"D")


            

    




#---------------------------------------------------------------

titleRSA = Label(frame,text="ALGORITMO RSA",pady=20, font=fontStyle)
titleRSA.grid(row=1,column=1,columnspan=4)

#------------------------------ Linea 1

labelKeys = Label(frame,text="Generar Llaves",pady=20)
labelKeys.grid(row=2,column=1)
entryKeys = Entry(frame)
entryKeys.grid(row=2,column=2, padx=10)
botonKeys = Button(frame, text='Procesar', command=enviarBotonKeys, width=20)
botonKeys.grid(row=2, column=3, padx=10)

#------------------------------- Linea 2

labelCifrar = Label(frame,text="Cifrar",pady=20)
labelCifrar.grid(row=3,column=1, padx=10)

botonSelText = Button(frame, text='Seleccionar', command=seleccionar, width=20)
botonSelText.grid(row=3, column=2, padx=10)

botonSelCifrar = Button(frame, text='Abrir', command=abrirCifrar, width=20)
botonSelCifrar.grid(row=3, column=3, padx=10)

botonEnviarCifrar = Button(frame, text='Enviar', command=enviarCifrar, width=20)
botonEnviarCifrar.grid(row=3, column=4, padx=10)


#------------------------------- Linea 3

labelDescifrar = Label(frame,text="Descifrar",pady=20)
labelDescifrar.grid(row=4,column=1, padx=10)

botonArchivoDescifrar = Button(frame, text='Seleccionar archivo', command=abrirArchivoDescifrar,  width=20)
botonArchivoDescifrar.grid(row=4, column=2, padx=10)


botonSelDescifrar = Button(frame, text='Seleccionar LLave', command=abrirLLaveDescifrar, width=20)
botonSelDescifrar.grid(row=4, column=3, padx=10)

botonEnviarDescifrar = Button(frame, text='Enviar', command=enviarDescifrar, width=20)
botonEnviarDescifrar.grid(row=4, column=4, padx=10)


#------------------------------- Linea 4
labelFirmar = Label(frame,text="Firmar Documento",pady=20)
labelFirmar.grid(row=5,column=1, padx=10)

btAbrirArchFirma= Button(frame, text="Abrir Archivo", command=abrirArchFirma, width=20)
btAbrirArchFirma.grid(row=5, column=2, padx=10)


btnAbrirLLaveFirma= Button(frame, text="Abrir LLave", command=abrirLLaveFirma, width=20)
btnAbrirLLaveFirma.grid(row=5, column=3, padx=10)
btnEnviarFirma= Button(frame, text="Abrir LLave", command=enviarFirma, width=20)
btnEnviarFirma.grid(row=5, column=4, padx=10)



#------------------------------ Linea 5
labelVerFirmar = Label(frame,text="Verificar Firmar",pady=20)
labelVerFirmar.grid(row=6,column=1, padx=10)

btAbrirVerArchFirma= Button(frame, text="Abrir Archivo", command=abrirVerArchFirma, width=20)
btAbrirVerArchFirma.grid(row=6, column=2, padx=10)


btnAbrirVerLLaveFirma= Button(frame, text="Abrir LLave", command=abrirVerLLaveFirma, width=20)
btnAbrirVerLLaveFirma.grid(row=6, column=3, padx=10)

btnAbrirVerSignature= Button(frame, text="Archivo Cifrado", command=abrirVerSignatureFirma, width=20)
btnAbrirVerSignature.grid(row=6, column=4, padx=10)

btnEnviarVerFirma= Button(frame, text="Enviar", command=enviarVerFirma, width=20)
btnEnviarVerFirma.grid(row=6, column=5, padx=10)





messageRSA = Label(frame,text="",pady=20, font=fontStyle)
messageRSA.grid(row=7,column=1,columnspan=4)



raiz.mainloop()
