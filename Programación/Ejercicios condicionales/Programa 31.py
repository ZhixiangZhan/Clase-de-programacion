#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
índice.

var1="A quién madruga Dios ayuda"
print(var1)
var2=input("Introduzca una palabra de la frase: ")
var3=var1.index(var2)
if var2 in var1:
    print(f"la palabra esta en la frase y el indice es {var3}")
if var2 not in var1:
    print("la palabra no esta en la frase")
    
