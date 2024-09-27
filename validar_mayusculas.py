'''
Prototipo para validar 
'''

palabra_usuario = input("Introduzca el mensaje secreto: ")
mi_lista = []
palabra = ""



'''
Con este For recorremos la palabra e introducimos cada letra en una lista
'''
for letra in palabra_usuario:

    if letra.isupper() == True:

        mi_lista.clear()
        print(f"No se aceptan mayusculas: {palabra_usuario}")
        break

    elif letra.isupper() == False:

        mi_lista.append(letra) # append agrega un elemento al final de la lista

'''
Con este For tomo cada palabra de la lista y la uno para hacerla una sola palabra
'''

for palabra_secreta in mi_lista:

    palabra += palabra_secreta

vacia = len(mi_lista) == 0

if vacia == False:
    
    print(f"La palabra encriptada es: {palabra}")
