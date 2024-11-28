#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario tenga x oportunidades para ver si letra introducida está en esa palabra.
secreta=input("itroduzca una palabra secreta: ")
for x in range(len(secreta)):
    var=input("introduzca una letra: ")
    if var in secreta:
        print("la letra existe")
    else:
        print("la letra no existe")
