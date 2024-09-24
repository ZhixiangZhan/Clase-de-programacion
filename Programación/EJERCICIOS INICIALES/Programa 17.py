#Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.

kg=float(input("Introduzca su peso: "))
m=float(input("Introduzca su altura: "))
imc=kg/m**2
if imc>25:
        print("si pesas ",kg,"kilos y mides",m,", tu IMC es: ","{:.2f}".format(imc),"Hay sobrepeso")
if imc<25:
        print("si pesas ",kg,"kilos y mides",m,", tu IMC es: ","{:.2f}".format(imc))
if imc=25:
        print("si pesas ",kg,"kilos y mides",m,", tu IMC es: ","{:.2f}".format(imc),"Hay sobrepeso")
