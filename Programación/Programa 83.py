import random

lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
var=""
var1=""
lista_punt=[]
media=0

print(lista)
var1=input("quiere empezar una partida (s/n): ")
while var1=="s" :
    intentos=0
    valor_ran=random.choice(lista)
    var=input("Introducir un valor de la lista: ")
    while var!=valor_ran:
        print("SIGUE JUGANDO")
        intentos+=1
        var=input("Introducir un valor de la lista: ")
    print("acertaste")
    lista_punt.append(8-intentos)
    var1=input("quiere empezar una partida (s/n): ")
    
else:
    print(lista_punt)
    media=len(lista_punt)*4
    if sum(lista_punt)>media:
        print("Tienes buena suerte")
    else:
        print("Dedicate al parchís")
    
    print("tu puntuacion es:", sum(lista_punt))
