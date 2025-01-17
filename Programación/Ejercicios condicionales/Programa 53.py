var1=int(input("Introduzca un numero: "))
var2=int(input("Introduzca un numero: "))
var_suma=var1+var2
var_suma_total=0
var_suma_total=var_suma_total+var_suma
rep=1

print(var_suma)
var3=int(input("Quiere repetir la operacion? si=1 no=2: "))
while var3==1:
    var1=int(input("Introduzca un numero: "))
    var2=int(input("Introduzca un numero: "))
    var_suma=var1+var2
    var_suma_total=var_suma_total+var_suma
    rep=rep+1
    print(var_suma)
    var3=input("Quiere repetir la operacion? si=1 no=2: ")
else:
    print("resumen")    
    print(f"El total es {var_suma_total} el numero de repeticiones es {rep}")