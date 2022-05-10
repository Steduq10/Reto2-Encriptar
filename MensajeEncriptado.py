mensaje = input("Ingrese el mensaje: ")
#ABC = ["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ABC = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
listaMensaje = []
for i in mensaje:
    listaMensaje.append(i)
print(listaMensaje)

diccionario = {}
print("('",end="")
#i = 0
#while i <= len(listaMensaje):
   # print(ABC[i],end="")
   # i += 1


#print("' ,")

for i in range(len(listaMensaje)):
    print(ABC[i], end="")
print("' ,")


for i in range(len(listaMensaje)):

    diccionario[listaMensaje[i]] = ABC[i]
    diccionario.update({listaMensaje[i]:ABC[i]})

print(diccionario,")")
#i = 0
#while i <= len(listaMensaje):
    #diccionario[listaMensaje[i]] = ABC[i]
    #print(diccionario)
    #i += 1

#print(")")

##DEBO INVERTIR LAS LLAVES CON LOS VALORES
print(diccionario.values())
print(diccionario.keys())

diccionarioInvertido = {} #SE CREA UN NUEVO DICCIONARIO VACIO QUE ALMACENARÁ EL NUEVO DICCIONARIO INVERTIDO
for key, value in diccionario.items(): #SE CREA UN CICLO FOR PARA INTERCAMBIAR LOS ELEMENTOS DEL DICCIONARIO
    diccionarioInvertido[value] = key

print(diccionarioInvertido)
print(diccionarioInvertido.values())
print(diccionarioInvertido.keys())


#ABC = {"A":listaMensaje[0],"B":listaMensaje[1],"C":listaMensaje[2],"D":listaMensaje[3],
    #   "E":listaMensaje[4],"F":listaMensaje[5],"G":listaMensaje[6],"H":listaMensaje[7],
   #    "I":listaMensaje[8],"J":listaMensaje[9],"K":listaMensaje[10],"L":listaMensaje[11],
   #    "M":listaMensaje[12],"N":listaMensaje[13],"O":listaMensaje[14],"P":listaMensaje[15],
   #    "Q":listaMensaje[16],"R":listaMensaje[17],"S":listaMensaje[18],"T":listaMensaje[19],
     #  "U":listaMensaje[20],"V":listaMensaje[21],"W":listaMensaje[22],"X":listaMensaje[23],
  #     "Y":listaMensaje[24],"Z":listaMensaje[25]}

#print(ABC)
#for i in mensaje :
    #print(i)
   # listaMensaje[i]
    #ABC[i]

    #diccionario[ABC] = listaMensaje
#print(diccionario)


