var1="A quién madruga Dios ayuda"
print(var1)
var2=input("Introduzca una palabra de la frase: ")
var3=var1.index(var2)
if var2 in var1:
    print(f"la palabra esta en la frase y el indice es {var3}")
if var2 not in var1:
    print("la palabra no esta en la frase")
    
