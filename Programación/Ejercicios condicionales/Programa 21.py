a=int(input("Introduzca el primer número: "))
b=int(input("Introduzca el segundo número: "))
c=int(input("Introduzca el tercer número: "))
import math
sqrt=math.sqrt
raiz=b**2-4*a*c
divisor=2*a
if raiz>0:
   var2=-b+math.sqrt(raiz)
   var3=-b-math.sqrt(raiz)
   var4=var2/divisor
   var5=var3/divisor
   print("x1= ",var4)
   print("x2= ",var5)
if raiz<0:
    print("La raíz no puede ser un valor negativo")


