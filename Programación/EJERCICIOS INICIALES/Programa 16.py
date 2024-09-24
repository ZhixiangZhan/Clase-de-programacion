#Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).
var1=float(input("Introduzca el valor de la raiz."))
import math
raiz=math.sqrt(var1)
division=raiz/2
print("la raiz de",var1,"es igual a","{:.1f}".format(raiz))
print("El resultado de la division es: ","{:.1f}".format(division))
