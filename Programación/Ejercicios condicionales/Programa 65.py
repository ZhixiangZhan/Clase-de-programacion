var1=int(input("Introduzca un numeo entre el -100 y el 100: "))
pares=0
negativos=0
positivos=0
impares=0
ceros=0
menor=var1
mayor=var1
total_suma=0
while var1!=-99:
    if var1%2==0:
        pares+=1
    if var1%2!=0:
        impares+=1
    if var1<0:
        negativos+=1
    if var1>0:
        positivos+=1
    if var1==0:
        ceros+=1
    if var1>mayor:
        mayor=var1
    if var1<menor:
        menor=var1
    total_suma+=var1
    var1=int(input("Introduzca un numeo entre el -100 y el 100: "))
else:
    print(f"El numero de pares es: {pares}")
    print(f"el numero de impares es: {impares}")
    print(f"el numero de negativos es: {negativos}")
    print(f"el numero de positivos es: {positivos}")
    print(f"el numero de ceros es: {ceros}")
    print(f"el total es: {total_suma}")
    print(f"el numero más pequeño es: {menor} y el más grande es: {mayor} ")
    
