#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
no distinguir entre mayúsculas y minúscula
var1="A quién madruga Dios ayuda"
print(var1)
frase1=var1.lower()
var2=input("Introduzca una palabra de la frase: ")
frase2=var2.lower()
var3=frase1.index(frase2)
if frase2 in frase1:
    print(f"la palabra esta en la frase y el indice es {var3}")
if frase2 not in frase1:
    print("la palabra no esta en la frase")
    

