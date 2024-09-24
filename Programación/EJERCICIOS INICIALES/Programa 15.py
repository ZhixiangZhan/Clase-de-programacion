#Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
pi=math.pi
var1=int(input("Introduzca el radio del cilindro:"))
var2=int(input("Introduzca la altura del cilindro:"))
area=2*pi*var1*var2+2*pi*var1**2
volumen=pi*var1**2*var2
print("El volumen de un cilindro es. ","{:.2f}".format(volumen))
print("El area de un cilindro es. ","{:.2f}".format(area))
