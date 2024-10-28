#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos
var1=float(input("introduzca la nota: "))

   
if var1>10 or var1<0:
    print("La nota que has introducido no está entre 0 y 10")
elif var1>8.5:
    print("Has sacado un excelente")
elif var1<8.5 or var1>6.5:
    print("Has sacado un notable")
elif var1<6.5 or var1>5 or var1==5:
    print("Has sacado un satisfactorio")
elif var1<5:
   print("Has sacado insuficiente")
