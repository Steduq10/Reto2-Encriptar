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


    return encriptado,clave

def desencriptador(encriptado, clave):
    diccionarioInvertido = {}
    for key, value in clave.items():
        diccionarioInvertido[value] = key


    desencriptado = ""
    for i in encriptado:
        desencriptado += diccionarioInvertido[i]#diccionarioInvertido[i]
    return desencriptado

mensaje = input("Ingrese el mensaje: ")
encriptador(mensaje)

encriptado, clave = encriptador(mensaje)
desencriptador(encriptado,clave)
print("(",encriptado,end=",")
print(clave,end="")
print(")")
desencriptado = desencriptador(encriptado,clave)
print(desencriptado)

