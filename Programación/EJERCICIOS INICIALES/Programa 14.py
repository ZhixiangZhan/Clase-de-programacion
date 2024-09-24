#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math
pi=math.pi
var1=int(input("Introduzca el valor de el diametro del circulo"))
var_perimetro=var1*pi
var_radio=var1/2
var_area=pi*var_radio**2
print("El valor de la circunferencia es:","{:.1f}".format(var_perimetro))
print("El valor de la area es:","{:.1f}".format(var_area))
