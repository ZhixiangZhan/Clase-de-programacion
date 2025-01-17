import random
intentos=0
var1=random.randint(1, 5)
var2=int(input("Introduzca un valor entre el 1 y 5:"))
intentos+=1
while intentos<3:
    print("Número no acertado")
    var2=int(input("Introduzca un valor entre el 1 y 5:"))
    intentos+=1
else:
    print("Número no acertado")
    


