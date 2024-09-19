# Programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?

var1=int(input("Introduce un numero entero"))
var2=int(input("Introduce el segundo numero entero"))
var_suma=var1+var2
var_resta=var1-var2
var_producto=var1*var2
var_division=var1/var2
var_exponente=var1**var2
var_division_entera=var1//var2
print("La suma entre primer numero y el segundo es:",var_suma)
print("La resta entre primer numero y el segundo es:",var_resta)
print("La multiplicacion entre primer numero y el segundo es:",var_producto)
print("La division entre primer numero y el segundo es:","{:.2f}".format(var_division))
print("La potencia que tiene como la base el primer numero y el segundo como el exponente es:",var_exponente)
print("entre primer numero y el segundo es:",var_division_entera)
