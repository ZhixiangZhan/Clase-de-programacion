#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.

var1=input("introduzcan una frase: ")
len=len(var1)
if len==11:
    print("la longitud de la frase es igual a 11")
elif len<11:
    print("la longitud de la frase es menor a 11")
elif len>11:
    print("la longitud de la frase es mayor a 11")

