# Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar
var1=int(input("introduce el valor a dividir"))
var2=int(input("introduce el dividendo"))
var_cociente=var1/var2
var_resto=var1%var2

print("El cociente es: ","{:.2f}".format(var_cociente))
print("El resto es: ,"var_resto)
if var_resto%2==0:
    print("El dividendo es par")
if var_resto%2==1:
    print("El dividendo es impar")

