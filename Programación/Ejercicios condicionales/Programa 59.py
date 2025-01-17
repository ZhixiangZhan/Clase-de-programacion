import random
intentos=0
var1=random.randint(0, 1000)
var2=int(input("Introduce un valor comprendido entre 1 y 1000: "))
intentos+=1 
while var2!=var1:
    if var2<var1:
        print("El número que has introducido es menor")
    if var2>var1:
        print("El número que has introducido es mayor")
    var2=int(input("Introduce un valor comprendido entre 1 y 1000: "))
    intentos+=1
else:
    print(f"Acertaste, has realizado {intentos} intentos")