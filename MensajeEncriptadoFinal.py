def encriptador(mensaje):

    ABC = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    listaMensaje = []

    for i in mensaje:
        listaMensaje.append(i)

    clave = {}

    letras = {}  # Creamos un diccionario solo con keys, que incorpora las letras que contiene el mensaje ingresado
    for letra in mensaje:
        letras[letra] = []
    listaletras = list(letras)  # convertimos el diccionario en una lista


    for i in range(len(listaletras)):  # Crea el diccionario, con clave y valor  #listaletras
        clave[listaletras[i]] = ABC[i]  # listaletras


    encriptado = ""

    for i in listaMensaje:
        encriptado += clave[i]

    #print(f"Con {mensaje} como mensaje, se obtuvo el siguiente mensaje encriptado, ")
    #print(" ")
    #print("clave y mensaje desencriptado respectivamente:",end=" ")
    print(encriptado+",",clave,end=", ")
    #print("('" + encriptado, end="',")
    #print(clave, end="")
    #print(",",end=" ")

    #print("Con",mensaje,"como mensaje, se obtuvo el siguiente mensaje encriptado,\n"+"clave y mensaje desencriptado respectivamente:", encriptado+",", clave,",",end=" ")
    return encriptado,clave

def desencriptador(encriptado, clave):
    diccionarioInvertido = {}
    for key, value in clave.items():
        diccionarioInvertido[value] = key


    desencriptado = ""
    for i in encriptado:
        desencriptado += diccionarioInvertido[i]#diccionarioInvertido[i]
    print(desencriptado)
    return desencriptado

mensaje = input("Ingrese el mensaje: ")
#encriptador(mensaje)

encriptado, clave = encriptador(mensaje)
desencriptador(encriptado,clave)
#print("('"+encriptado,end="',")
#print(clave,end="")
#print(")")
#desencriptado = desencriptador(encriptado,clave)
#print(desencriptado)

