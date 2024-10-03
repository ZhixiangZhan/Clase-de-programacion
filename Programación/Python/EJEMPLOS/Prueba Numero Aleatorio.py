#Como hacer diferentes operaciones en un programa
import random
var1=random.randint(1,100)
var2=random.randint(1,10)
var3=var1+var2
print("var1 es:",var1)
print("var2 es:",var2)
respuesta=int(input("introduzca el resultado de (var1)+(var2) :"))
if var3==respuesta:
    print("LA RSPUESTA ES CORRECTA")
if var3!=respuesta:
    print("la respuesta esta incorrecta")
