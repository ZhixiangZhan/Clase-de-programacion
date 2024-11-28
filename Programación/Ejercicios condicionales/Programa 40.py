#Crea un programa que cuente todos los números pares hasta el número 50
var1=50
pares=0
impares=0

for X in range(var1):
    if X%2:
        pares=pares+1
    else:
        impares=impares+1
    

print(f"el numero de pares es: {pares}")
print(f"el numero de impares es: {impares}")
