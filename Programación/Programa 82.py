import random

lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
valor_ran=random.choice(lista)
var=""
var1=""
print(lista)
var=input("Introducir un valor de la lista: ")
while var1==False :
    
    if var==valor_ran:
        print("ACERTASTE")
        
    else:
        print("SIGUE JUGANDO")
        var=input("Introducir un valor de la lista: ")