mensaje = input("Ingrese el mensaje: ")
#ABC = ["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ABC = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
listaMensaje = []

for i in mensaje:
    listaMensaje.append(i)
print(listaMensaje)

diccionario = {}
print("('",end="")



#print("' ,")



print("Se imprime el diccionario")
for i in range(len(listaMensaje)):
    #diccionario[ABC[i]] = listaMensaje[i]
    #diccionario.update({ABC[i]: listaMensaje[i]})

    diccionario[listaMensaje[i]] = ABC[i]
    #diccionario.update({listaMensaje[i]:ABC[i]})


print(diccionario,")")
print("CLAVE")
valor = diccionario.values()
#clave = diccionario.keys()

lista =list(diccionario)
print(lista)
print("FOR")
'''
for i in diccionario:
    #print(i)
    print(diccionario[i])
'''
#Creamos un ciclo for para reescribir el mensaje original por el código de encriptación, Para ello hacemos un
#ciclo anidado en el cual tenemos: un for externo para que itere dentro del diccionario y uno interno para que
#itere en el rango del tamaño del mensaje ingresado con el condicional de que si la clave del diccionario
#coincide con el caracter del mensaje, coga el valor del diccionario y se lo asigne a la lista.
for i in diccionario:
    for j in range(len(listaMensaje)):
        if i == listaMensaje[j]:
            listaMensaje[j] = diccionario[i]


print(listaMensaje)

#i = 0
#while i <= len(listaMensaje):
    #diccionario[listaMensaje[i]] = ABC[i]
    #print(diccionario)
    #i += 1

#print(")")

#DECODIFICADOR

##DEBO INVERTIR LAS LLAVES CON LOS VALORES
print("Se imprime el diccionario invertido")
diccionarioInvertido = {} #SE CREA UN NUEVO DICCIONARIO VACIO QUE ALMACENARÁ EL NUEVO DICCIONARIO INVERTIDO
for key, value in diccionario.items(): #SE CREA UN CICLO FOR PARA INTERCAMBIAR LOS ELEMENTOS DEL DICCIONARIO
    diccionarioInvertido[value] = key

print(diccionarioInvertido)
print(diccionarioInvertido.values())
print(diccionarioInvertido.keys())

for i in diccionarioInvertido.values():
    print(i,end="")












