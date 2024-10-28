#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
var1=input("introduzca una letra: ")
x=var1.islower()

if x==True:
    print("la letra es minuscula")
if x==False:
    print("la letra es mayuscula")
