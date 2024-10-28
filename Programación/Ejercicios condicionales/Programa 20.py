#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
var1=int(input("introduzca el primer número: "))
var2=int(input("introduzca el segundo número: "))
   
if var1>10 or var2>10:
    print("Uno o los dos números se pasa del rango de operacion")
elif var1>var2:
    print(f"El número {var1} es mayor que el número {var2}")
elif var1<var2:
    print(f"El número {var1} es menor que el número {var2}")
elif var1==var2:
    print("Ambos números son iguales")
            
