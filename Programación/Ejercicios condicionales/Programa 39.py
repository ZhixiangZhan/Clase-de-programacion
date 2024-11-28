#Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.
var1=int(input("Introduce la cantidad de números que deseas introducir: "))
positivo=0
negativo=0
cero=0
for x in range(var1):
    var2=float(input("Introduzca un numero: "))
    if var2==0:
       zero=zero+1 
    if var2<0:
        negativo=negativo+1
    if var2>0:
        positivo=positivo+1

print(f"el numero de positivos es igual a {positivo}")
print(f"el numero de negativos es igual a {negativo}")
print(f"el numero de ceros es igual a {cero}")