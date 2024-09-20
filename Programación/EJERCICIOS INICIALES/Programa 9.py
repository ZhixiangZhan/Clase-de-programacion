# Programa que pida los segundos y muestre por pantalla y en la misma frase los y las horas

var1=int(input("introduzca un numero de segundos:"))
var_min=var1/60
var_seg=var1/3600
print("el numero de minutos es:","{:.2f}".format(var_min),"y el numero de horas es:","{:.4f}".format(var_seg))
