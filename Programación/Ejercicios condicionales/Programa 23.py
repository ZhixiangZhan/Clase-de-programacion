var1=float(input("introduzca la nota: "))

   
if var1>10 or var1<0:
    print("La nota que has introducido no está entre 0 y 10")
elif var1>8.5:
    print("Has sacado un excelente")
elif var1<8.5 or var1>6.5:
    print("Has sacado un excelente")
elif var1<6.5 or var1>5 or var1==5:
    print("Has aprovado")

