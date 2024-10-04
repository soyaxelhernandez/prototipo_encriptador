'''
Encriptador de textos con validacion terminado.
'''

# import string para poder usar ascii_letters
import string



eleccion = input("Introduzca 'e' para encriptar un mensaje o 'd' para desencriptarlo: ")
mi_lista = []
palabra = ""

'''
Se declara una funcion que contiene el For con el que recorremos la palabra e introducimos 
cada letra en una lista validamos que la palabra del usuario no tenga caracteres especiales 
o acentos y validamos que la palabra no contenga mayusculas
'''
def validar():
    
    for letra in palabra_usuario:
        
        if letra not in string.ascii_letters:
            mi_lista.clear() #si alguna tiene caracter diferente a letras limpia la lista
            print(f"No se aceptan caracteres especiales: {palabra_usuario}")
            break
        elif letra.isupper() == True: #validamos si la letra que recorre el for es mayúscula 
            mi_lista.clear() #si alguna es mayuscula limpiamos la lista
            print(f"No se aceptan mayusculas: {palabra_usuario}")
            break
        
        elif letra.isupper() == False: #de lo contrario se valida que no se tiene alguna mayúscula
            mi_lista.append(letra) # append agrega un elemento al final de la lista
            

def sniffer(u, a, b): #con esta funcion buscamos las palabras que queremos

    mi_lista = u.split(a)
    separador = b
    nueva_palabra = separador.join(mi_lista)
    return nueva_palabra


def desencriptar(palabra_usuario):

    if palabra_usuario.split("ai"):
        resultado = sniffer(palabra_usuario, "ai", "a") #utilizamos la funcion sniffer para buscar
        
        if resultado.split("imes"):
            resultado = sniffer(resultado, "imes", "i")

            if resultado.split("enter"):
                resultado = sniffer(resultado, "enter", "e")

                if resultado.split("ober"):
                    resultado = sniffer(resultado, "ober", "o")

                if resultado.split("ufat"):
                    resultado = sniffer(resultado, "ufat", "u")
    print(resultado)

'''
Con este For verifico en que índice esta la letra y después evaluó para reemplazar en ese elemento
'''

def encriptar():

    for letras in mi_lista:
    
        elemento = letras
        indice = mi_lista.index(elemento) #index() indica el índice de la primera aparición de un elemento

        if letras == "a":
            mi_lista.remove("a")
            mi_lista.insert(indice, "ai")
        
        elif letras == "e":
            mi_lista.remove("e")
            mi_lista.insert(indice, "enter")

        elif letras == "i":
            mi_lista.remove("i")
            mi_lista.insert(indice, "imes")

        elif letras == "o":
            mi_lista.remove("o")
            mi_lista.insert(indice, "ober")

        elif letras == "u":
            mi_lista.remove("u")
            mi_lista.insert(indice, "ufat")

#Con este if iniciamos el programa para validar si se desea encriptar o desencriptar
if eleccion== "e":
    palabra_usuario = input("Introduzca el mensaje a encriptar: ")
    validar()
    encriptar()

if eleccion == "d":

    palabra_usuario = input("Introduzca el mensaje a desencriptar: ")
    validar()
    desencriptar(palabra_usuario)

else:
    print("Debe seleccionar una opción valida para continuar")


'''
Con este For tomo cada palabra de la lista y la uno para hacerla una sola palabra
'''
for palabra_secreta in mi_lista:
    palabra += palabra_secreta

lista_vacia = len(mi_lista) == 0 #con len validamos la longitud de la lista para saber si contiene letras

if lista_vacia == False: #validamos si existe un mensaje que imprimir de lo contrario no pasa al print
    print(f"La palabra encriptada es: {palabra}")

