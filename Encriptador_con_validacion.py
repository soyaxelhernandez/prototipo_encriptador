'''
Prototipo de encriptador con una validacion de no acentos y caracteres especiales
'''

# import string para poder usar ascii_letters
import string

palabra_usuario = input("Introduzca el mensaje secreto: ")
mi_lista = []
palabra = ""
 
'''
Con este For recorremos la palabra e introducimos cada letra en una lista
Validamos que la palabra del usuario no tenga caracteres especiales o acentos
y validamos que la palabra no contenga mayusculas
'''
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

'''
Con este For verifico en que índice esta la letra y después evaluó para reemplazar en ese elemento
'''
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

'''
Con este For tomo cada palabra de la lista y la uno para hacerla una sola palabra
'''
for palabra_secreta in mi_lista:
    palabra += palabra_secreta

lista_vacia = len(mi_lista) == 0 #con len validamos la longitud de la lista para saber si contiene letras

if lista_vacia == False: #validamos si existe un mensaje que imprimir de lo contrario no pasa al print
    print(f"La palabra encriptada es: {palabra}")