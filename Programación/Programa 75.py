lista1=["a","b","D","x","r","X","3","h","w","2","i"]
var1=0
var2=0
var3=0
var4=0
var5=0

for x in lista1:
    var1+=1
    if x.isnumeric() == True:
        var2+=1
        var5+=int(x)
    if x.isalpha()==True:
        var3+=1
        if x.isupper()==True:
            var4+=1
print(f"Numero de valores: {var1}")
print(f"Cantidad de numeros: {var2}")
print(f"cantidad de letras: {var3}")
print(f"Cantidad de mayusculas: {var4}")
print(f"suma de los numeros: {var5}")