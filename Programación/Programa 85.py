lista=[]
lista1=[]
lista2=[]
var1="s"
var2=[]
while var1=="s":
    var2.append(input("Introduzca estudiante: "))
    lista.append(int(input("introduzca nota ingles: ")))
    lista1.append(int(input("introduzca nota castellano: ")))
    lista2.append(int(input("introduzca nota catalan: ")))
    var1=input("Quiere introducir otro alumno s/n: ")
lista.sort()
lista1.sort()
lista2.sort()

if len(lista)%2==0:
    print("La mediana de ingles:",lista[len(lista)/2])
if len(lista)%2!=0:
    print("La mediana de ingles:",lista[len(lista)//2])
if len(lista1)%2==0:
    print("La mediana de castellano:",lista1[len(lista1)/2])
if len(lista1)%2!=0:
    print("La mediana de castellano:",lista1[len(lista1)//2])
if len(lista2)%2==0:
    print("La mediana de catalan:",lista2[len(lista2)/2])
if len(lista2)%2!=0:
    print("La mediana de catalan:",lista2[len(lista2)//2])
    
    
print("la media de ingles: ",sum(lista)/len(lista))
print("la media de castellano: ",sum(lista1)/len(lista1))
print("la media de catalan: ",sum(lista2)/len(lista2))
