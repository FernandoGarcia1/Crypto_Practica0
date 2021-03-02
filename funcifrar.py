from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def cifrar(mens,llaveP,direccion):
    print("mensaje recibido="+mens+".  LLaveRecibida="+llaveP+".Direccion=" )


    mensaje = mens
    llave = RSA.importKey(open(llaveP , "rb").read())
    cifrado = PKCS1_OAEP.new(llave)

    mensajeCifrado = cifrado.encrypt(mensaje.encode())
    nomArchivo= direccion[1]
    nomArchivo=nomArchivo.split('.')
    nuevoNomArchivo= nomArchivo[0]+"_C."+nomArchivo[1]
    print(nuevoNomArchivo)
    rutaArchivoCifrado = direccion[0] +"/" +nuevoNomArchivo
    print(rutaArchivoCifrado)

    f = open(rutaArchivoCifrado, "wb")
    f.write(mensajeCifrado)
    f.close


