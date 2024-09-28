'''
Prototipo para validar 
'''

palabra_usuario = input("Introduzca el mensaje secreto: ")
mi_lista = []
palabra = ""




for letra in palabra_usuario:

    if letra.isupper() == True: #validamos si la letra que recorre el for es mayúscula

        mi_lista.clear() #si alguna es mayuscula limpiamos la lista
        print(f"No se aceptan mayusculas: {palabra_usuario}")
        break

    elif letra.isupper() == False: #de lo contrario se valida que no se tiene alguna mayúscula

        mi_lista.append(letra) # append agrega un elemento al final de la lista

'''
Con este For tomo cada palabra de la lista y la uno para hacerla una sola palabra
'''

for palabra_secreta in mi_lista:

    palabra += palabra_secreta

vacia = len(mi_lista) == 0 #con len validamos la longitud de la lista para saber si contiene letras

if vacia == False: #validamos si existe un mensaje que imprimir de lo contrario no pasa al print
    
    print(f"La palabra encriptada es: {palabra}")
