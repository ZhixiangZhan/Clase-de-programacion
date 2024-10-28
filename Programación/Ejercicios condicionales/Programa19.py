# Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales

var1=int(input("introduzca el primer número"))
var2=int(input("introduzca el segundo número"))

if var1>var2:
    print(f"El número {var1} es mayor que el número {var2}")
if var1<var2:
    print(f"El número {var1} es menor que el número {var2}")
if var1==var2:
    print("Ambos números son iguales")


