
var1=int(input("Deme el primer numero: "))
var2=int(input("Deme el segundo numero: "))

var_suma=var1+var2
print(var_suma)
var_pregunta=int(input("quiere seguir con las operaciones? si=1  no=2: "))
while var_pregunta==1:
    var1=int(input("Deme el primer numero: "))
    var2=int(input("Deme el segundo numero: "))

    var_suma=var1+var2
    print(var_suma)
    var_pregunta=int(input("quiere seguir con las operaciones? si=1  no=2: "))
else:
    print("Programa Finalizado")