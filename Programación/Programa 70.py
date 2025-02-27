
lista1=[]
lista2=[]
var1=0
var1=int(input("Introduzca la cantidad de palabras que quiere introducir: "))
for x in range(0,var1):
    lista1.append(input("Introduce una palabra: "))
lista1.sort()
lista2=lista1.copy()
lista2.sort(reverse=True)
print(lista1)
print(lista2)
