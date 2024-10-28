#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla
var1=input("introduzca una letra: ")
x=var1.islower()
y=var1.isnumeric()
if x==True:
    print("la letra es minuscula")
if x==False and y==False:
    print("la letra es mayuscula")
if y==True:
    print("es un número")

