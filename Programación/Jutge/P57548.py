numeros=input()
lista=[]
solucion=0
if len(numeros)>1:
    lista=numeros.split()
    for recorrer in lista:
        solucion+=int(recorrer)
    print(solucion)
else:
    lista.append(numeros)
    numeros=input()
    lista.append(numeros)
    lista=numeros.split()
    for recorrer in lista:
        solucion+=int(recorrer)
    print(solucion)