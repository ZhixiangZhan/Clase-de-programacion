lista=[]
var1=0
var1=int(input("Introduzca la cantidad de numeros que quiere introducir: "))

for x in range(0,var1):
    lista.append(int(input("Introduce un número: ")))
lista.sort()
print(lista)
