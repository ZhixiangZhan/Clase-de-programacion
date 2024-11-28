#Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
var1=int(input("introduzca el numero de notas que quiere comprovar: "))
for x in range(var1):
    var2=float(input("Introduzca la nota: "))
    if var2>=5:
        print("ha aprovat")
    else:
        print("ha suspes")

