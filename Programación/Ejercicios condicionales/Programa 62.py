var1=int(input("Introduzca un numero: "))
var2=int(input("Introduzca un numero: "))
pares=0
impares=0

if var1<var2:
    contador=var1
    for x in range(var1,var2):
        if contador%2==0:
            pares=pares+str(x)
        else:
            impares=impares+""
        contador+=1    
if var1>var2:
    contador=var2        
    for contador in range(var2,var1):
        if contador%2==0:
            pares+=str(contador)
        else:
            impares+=str(contador)
        contador+=1 
print(pares,end="-")
print(impares,end="-")