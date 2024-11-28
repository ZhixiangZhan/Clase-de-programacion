# A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
var1=int(input("introduzca el numero de notas que quiere comprovar: "))
for x in range(var1):
    var2=float(input("Introduzca la nota: "))
    if var2<0 or var2>10:
        print("Has introducido una nota equivocada")
    if var2>=5:
        print("ha aprovat")
    else:
        print("ha suspes")


