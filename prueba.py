from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont
from tkinter import messagebox as MessageBox

raiz=Tk()
frame=Frame(raiz)
frame.pack()

def seleccionar ():
    ficheroCifrar = filedialog.askopenfilename(title = "Seleccionar", filetypes = [("Ficheros TXT", "*.txt"), ("Todos los archivos", "*.*")])
    global archCifrar
    archCifrar = ficheroCifrar
    print (archCifrar)

botonSelCifrar = Button(frame, text='Abrir', command=seleccionar, width=20)
botonSelCifrar.grid(row=3, column=3, padx=10)

raiz.mainloop()
