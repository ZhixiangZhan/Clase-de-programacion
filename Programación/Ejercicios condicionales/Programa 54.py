var1=int(input("Introduzca un numero: "))
var2=int(input("Introduzca un numero: "))
var_suma=var1+var2
var_suma_total=0
var_suma_total=var_suma_total+var_suma
ope=1
print(f"el resultado de la suma es: {var_suma}")
print(f"El total acomulado es: {var_suma_total} y el numero de operaciones es {ope}")

while var_suma_total<50:
    var1=int(input("Introduzca un numero: "))
    var2=int(input("Introduzca un numero: "))
    var_suma=var1+var2
    var_suma_total=var_suma_total+var_suma
    ope=ope+1
    print(f"el resultado de la suma es: {var_suma}")
    print(f"El total acomulado es: {var_suma_total} y el numero de operaciones es {ope}")
    if var_suma_total>50:
        print("Programa finalizado")    